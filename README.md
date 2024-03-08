# <a name="readme-top"></a>

# <h1 align="center">*Recomendación de negocios*</h1>

<p align="center">
  <img src="images/logo_empresa.jpg"  height="200">
<p align="center">

## *Índice de Contenidos*

- [Introducción](#introducción)
- [Contexto](#contexto)
- [Alcance](#alcance)
  - [Flujo de Trabajo](#flujo-de-trabajo)
  - [Cronograma](#cronograma)
  - [DER](#diagramas-entidad-relación)
  - [Diagrama de Gantt](#diagrama-de-gantt)
  - [KPIs](#kpis)
  - [Restricciones y Limitaciones](#restricciones-y-limitaciones)
- [Deploy](#deploy-en-google-cloud-run)
- [Dashboard](#dashboard-interactivo)
- [Modelo-Recomendación](#modelo-de-recomendación)  
- [Fuentes de datos](#fuentes-de-datos)
- [Acerca de nosotros](#acerca-de-nosotros)
- [Stack tecnológico](#stack-tecnológico)

## *Introducción*

Como parte de una consultora de datos, hemos sido contratados para llevar a cabo un análisis del mercado estadounidense. Nuestro cliente forma parte de un conglomerado de empresas relacionadas con restaurantes relacionadas al rubro fast food, y buscan obtener un análisis detallado de las opiniones de los usuarios en Yelp y cruzarlas con las de Google Maps en relación a dicho rubro. Utilizando análisis de sentimientos, nuestro objetivo es prever si el rubro fast food experimentará un mayor crecimiento o declive.

Además nuestro cliente desea determinar estratégicamente la ubicación de nuevos locales de restaurantes, implementando un sistema de recomendación de restaurantes fast food para usuarios en ambas plataformas. Con nuestro producto los clientes podran identificar oportunidades de creación o compra de negocios.

## Contexto

La retroalimentación de los usuarios, cada vez más abundante gracias a plataformas de reseñas, es un recurso valioso para los negocios de comida rápida. Yelp y Google Maps son dos plataformas destacadas que ofrecen reseñas específicamente para este tipo de establecimientos. Los usuarios comparten sus experiencias, proporcionando a las empresas de comida rápida una visión detallada de cómo son percibidas por sus clientes. Esta información resulta esencial para evaluar el rendimiento, utilidad y áreas de mejora de los servicios ofrecidos por cada local de comida rápida. La capacidad de los usuarios para tomar decisiones basadas en estas reseñas subraya la importancia crítica de mantener una imagen positiva en estas plataformas para el éxito comercial en la industria de la comida rápida.

## Alcance

El presente documento establece el alcance del proyecto de análisis de opiniones de usuarios

### Flujo de Trabajo

<div align="center">
  <img src="images/workflow.png">
</div>
&nbsp;

Elegimos realizar la visualizacion e interaccion con los dos productos terminados que ofrecemos, hacerlo a traves de una web. Esta web permite interactuar con los dos grandes resultados de nuestro trabajo:

- EL Dashboard
- El modelo entrenado de ML

Pero para que la la interfaz web pueda mostrar los datos, se tuvieron que realizar varias elecciones y trabajos previos que a continuacion se detallan de manera general, asi como algunas de las justificaciones de esas selecciones y los trabajos previos necesarios.

***La WEB:***

**Streamlit como front-end framework general:**

Su simplicidad de uso permitio que nos centremos en los aspectos fundamentales del trabajo enconmendado: obtener informacion en base a los datos.
Su  simple API no requiere conocimientos avanzados de configuracion de rutas, escribir y correr el back-end, manejar consultas HTTP, conectar el front-end, escrbir HTML, CSS, JS, etc. Si bien no tiene un alto nivel de configuracion sin incorporacion de otras herramientas, cumple su cometido sin problemas.

**Docker como plataforma para contenedorizar la interfaz web:**

Docker es una plataforma para generar unidades auto contenidas que tiene todo lo que la app necesita para correr y ejecutar su funcionalidad. A Estas unidades se las denomina contenedores y tienen las siguientes caracteristicas:

- Incluyen todas las dependencias: el codigo de la aplicacion, el runtime de ejecucion y las librerias se empaquetan juntas.
- Cada contenedor corre independientemente del resto, compartiendo el Kernel del sistema operativo pero no recursos.
- Son portables y pueden ser facilmente movidos entre diferentes entornos sin romper la aplicacion.
- Son mas eficientes que las maquinas virtuales al compartir el kernel.

La interfaz web esta integremente empacada en un contenedor de Docker (un estandar internacional).

Algunas de las librerias que se estan incluidas en el contenedor de la app:

- Python (3.9 Slim)
- Streamlit
- Pandas
- Numpy
- Slack
- Folium
- Google Cloud Bigquery y Google CLoud Storage

**Google Cloud Run como servicio para realizar el deploy de la web:**

Si bien Stremlit dispone de un servicio apto para realizar el deploy de manera simple y rapida (Streamlit Comunity Cloud), nos volcamos por realizarlo mediante Google Cloud Run porque:

- Docker es una de las tecnologias soportadas por Cloud Run, la cual recomienda en su documentacion (si bien admite deploys no-contenedorizados como Node JS o Go).
- Serverless: Cloud Run se encarga de la adminstracion e infraestrutura ante aumentos o disminuciones de trafico.
- Cambiando streamlit como front-end framework (por ejemplo por React JS), el deploy en la nube previo creado el contenedor, es identico.


El proceso para disponibilizar un endpoint publico de la web fue:

1) Localmente crear el contenedor con todas las dependencias
2) Subirlo a Google Artifact Registry: un repositorio de contenedores (y mas) en la nube.
3) Crear el servicio en Google Cloud Run: como resultado de la creacion, se disponibiliza un endpoint publico para su consumo.


***El Dashboard y el modelo de ML:***


Para ambos, si bien responden a origenes de datos y objetivos diferentes, comparten el mismo camino en la nube:

1) Los datos crudos provenentes de la informacion suministrada y alguna adicional que se sumo, se suben a Google Cloud Storage.
2) Una funcion creada en Google Cloud Functions se gatilla cada vez que un Storage es actualizado tanto la primera vez, como toda vez que se agreguen datos nuevos.
3) Esta funcion envia trabajos (Jobs) a Google Cloud DataProc para realizar tanto el ETL automatizado como para obtener el modelo de ML entrenado. Siempre se tienen en cuenta los datos nuevos, obteniendo nuevas versiones actualizadas de los datos.
4) Algunas notificaciones son enviadas por Slack a medida que los procesos se cumplen satisfactoriamente.
5) Los archivos con los trabajos terminados se guardan nuevamente en Google Cloud Storage para ser consumidos tanto por PowerBI (Dashborad) como por el front-end.


Este flujo de trabajo garantiza una correcta actualizacion y permanente disponibilidad de datos actualizados para la toma de decisiones.

***Nota con respecto a la visualizacion de los mapas en el modelo de ML:***

Para mantener el trafico de datos liviano entre los ordenadores que realizan las consultas y la nube en cuanto a la visualizacion de los puntos de interes en los mapas, se realizan internamente dos requests HTTP.

- request 1: se envian los parametos seleccionados al modelo de ML entrenado que reside en la nube. Esta primera request devuelve solo entre 5 y 15 indices, correpondientes a la identificacion de los comercios relevantes de acuerdo al modelo elegido.

- request 2: los indices son enviados nuevamente a la nube, de manera que la la busqueda y devolucion de los datos relevantes para ser representados son solo los que se dibujan. Esto hace que el trafico si bien se realiza dos veces, el volumen de datos es despreciable.




## Cronograma

El proyecto se desarrollará en un período de 6 semanas, con tres sprint que son los siguientes:

- Sprint 1: Puesta en macha del proyecto. 2 Semanas

  - Inicialización del proyecto realizando mineria de datos y documentación del datawarehouse.
  - Establecimiento del stack tecnologica que utilzaremos durante el proyecto.
  - Implementamos la metodología SCRUM realizando daylis, para optimizar la producción.
  - Realización de tareas puntuales como EDA, KPI's y diagrama de Gantt.
  - Equipo de trabajo, Roles y responsabilidades.
- Sprint 2: Data Engineering. 2 Semanas
  - Realización de extracción transformación y carga de la data.
  - Creación de un flujo automatizado anual, en el que nuestro cliente podra estar actualizado de forma automatica.
  - Durante la creación del flujo automatico se nos notificará via el slack de la empresa las valizaciones de la tarea de manera automatica.
  - Documentación: Diagrama entidad relación, Diccionario de datos, Workflow y tecnologías.
  - MVP/ Proof of Concept de producto de ML ó MVP/ Proof of Concept de Dashboard.
- Sprint 3: Data Analitics y Machine learning. 2 Semanas.
  - Diseño de Dashboard realizado en power BI, vizualizado en la página web de la empresa.
  - Creación de un modelo de recomendación para nuestro cliente y puesta en producción en la página web.
  - Documentación: selección del modelo, feature engineering, informe de análisis.
  - Video del proyecto realizado, para ser votado y, en caso de ganar, ser presentado en la graduación final.

### Diagramas entidad relación

<p align="center">
<img src="./images/DER-Google.png"  width="600">
<img src="./images/DER-Yelp.png"  width="600">

### Diagrama de Gantt

El proyecto seguirá una metodología de trabajo en equipo que incluye las siguientes etapas:

<div align="center">Sprint 1
</div>
<div align="center">
  <img src="./images/gantt.jpg" width=600>
</div>

<div align="center">Sprint 2
</div>

<div align="center">
  <img src="./images/gantt2.png" width=600>
</div>

<div align="center">Sprint 3
</div>

<div align="center">
  <img src="./images/Sprint3.png" width=600>
</div>


### *KPIs*

<div align="center">

<img src="./images/kpis/respuesta_Negocios.png" width=600>
</div>

<p align='center'> <b>Objetivo:</b> Aumentar las respuestas de negocios en un 45% respecto al año anterior.

<div align="center">

<img src="./images/kpis/rating_positivos.png" width=600>
</div>

 <p align='center'><b>Objetivo:</b> Aumentar un 10% las reviews positivas comparadas con el año anterior.
<p align='center'>(Una review positiva es cuando recibe 4 o 5 estrellas)

<div align="center">
<img src="./images/kpis/satisfaccion_clientes.png" width=600>
</div>

 <p align='center'><b>Objetivo:</b> Aumentar un 5% los reviews de sentimientos positivos respecto
  <p align='center'> al total de reviews comparados con el año anterior.

### *Restricciones y Limitaciones*

El proyecto se limita al análisis de datos disponibles en Yelp y Google Maps para el mercado estadounidense.
La disponibilidad y calidad de los datos pueden afectar los resultados del análisis.
El alcance del proyecto no incluye la implementación de sistemas en producción, sino la entrega de modelos y recomendaciones listos para su implementación.

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

</details>

## Deploy en Google Cloud Run

Realizamos una página web interactiva a través de la herramienta streamlit mediante el cual presentamos nuestros productos desarrollados como son un dashboard y un modelo de recomendación. 

<a href="https://datavision-hfdze4a6jq-uc.a.run.app/">Link Página web</a>

<div align="center">
  <img src="images/dash1.gif" width=400>
  <img src="images/dash2.gif" width=400>
</div>

<div align="center">
  <img src="images/mml1.gif" width=400>
  <img src="images/mml2.gif" width=400>
</div>

## Dashboard Interactivo
Desarrollamos un dashboard interactivo que brinda información gráfica y detallada de nuestros análisis que permite visualizar de manera clara y concisa los insights obtenidos durante el proceso de análisis de mercado.
<div align="center">
  <img src="images/powerbi.jpg">
</div>


## Modelo de recomendación

 Nuestro modelo predictivo de machine learning con base en la proximidad geográfica, la evaluación de usuarios y la oferta de servicios, devuelve recomendaciones valiosas acerca de los negocios de comida rápida en Estados unidos.
<div align="center">
  <img src="images/modelo_ML.jpg">
</div>



## *Fuentes de datos*

- [Diccionario de Datos](https://docs.google.com/document/d/1JyRMQQJPGitQEPz7D5zgcfMOSEScAjzd-6Sq229kZZQ/edit)

### Fuentes de datos obligatorias

- [Dataset de Google Maps](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=share_link)

- [Dataset de Yelp!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing)

## *Acerca de nosotros*

<table align="center">
  <tr>
    <td align="center"><b>Marcelo Ortiz</td>
    <td align="center"><b>Belén Viglioglia Becker</b></td>
    <td align="center"><b>Alejandro Ramírez</b></td>
    <td align="center"><b>Mariano Popov</b></td>
    <td align="center"><b>Martín Riveros</b></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/marceloortizz/"><img src="images/marcelo.jfif" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/belen-viglioglia-becker/"><img src="images/belen.jfif" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/dalejandroramirez/"><img src="images/alejandro.jfif" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/mariano-popov-3a4570290/"><img src="images/mariano.jfif" width=48 style="border-radius:50%"> </a></td>
    <td align="center"><a href="https://www.linkedin.com/in/martinriveros/"><img src="images/martin.jfif" width=48 style="border-radius:50%"></a></td>
  </tr>
  <tr>
    <td align="center">Data Analyst</td>
    <td align="center">Data Analyst</td>
    <td align="center">Data Engineer</td>
    <td align="center">Data Engineer</td>
    <td align="center">Data Science</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/marceloortizz"><img src="https://img.shields.io/badge/Platform-GitHub-lightgrey"></a></td>
    <td align="center"><a href="https://github.com/belenvbecker"><img src="https://img.shields.io/badge/Platform-GitHub-lightgrey"></a></td>
    <td align="center"><a href="https://github.com/dalejandroramirez"><img src="https://img.shields.io/badge/Platform-GitHub-lightgrey"></a></td>
    <td align="center"><a href="https://github.com/marianopopov"><img src="https://img.shields.io/badge/Platform-GitHub-lightgrey"> </a></td>
    <td align="center"><a href="https://github.com/martinarielriveros"><img src="https://img.shields.io/badge/Platform-GitHub-lightgrey"></a></td>
  </tr>
  <tr>
      <td align="center"><a href="https://www.linkedin.com/in/marceloortizz/"><img src="https://img.shields.io/badge/Platform-LinkedIn-blue"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/belen-viglioglia-becker/"><img src="https://img.shields.io/badge/Platform-LinkedIn-blue"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/dalejandroramirez/"><img src="https://img.shields.io/badge/Platform-LinkedIn-blue"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/mariano-popov-3a4570290/"><img src="https://img.shields.io/badge/Platform-LinkedIn-blue"> </a></td>
    <td align="center"><a href="https://www.linkedin.com/in/martinriveros/"><img src="https://img.shields.io/badge/Platform-LinkedIn-blue"></a></td>
  </tr>
</table>

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## Stack tecnológico 

 [![Visual Studio Code](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-blue)](https://code.visualstudio.com/)
 [![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](https://jupyter.org/)
 [![Pandas](https://img.shields.io/badge/Library-Pandas-brightgreen)](https://pandas.pydata.org/)
 [![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-blue)](https://matplotlib.org/)
 [![Seaborn](https://img.shields.io/badge/Library-Seaborn-yellow)](https://seaborn.pydata.org/)
 [![Folium](https://img.shields.io/badge/Library-Folium-green)](https://python-visualization.github.io/folium/)
 [![scikit-learn](https://img.shields.io/badge/Library-scikit--learn-red)](https://scikit-learn.org/)
 [![Streamlit](https://img.shields.io/badge/Framework-Streamlit-purple)](https://streamlit.io/)
 [![Apache Spark](https://img.shields.io/badge/Big%20Data-Apache%20Spark-yellow)](https://spark.apache.org/)
 [![GitHub](https://img.shields.io/badge/Platform-GitHub-lightgrey)](https://github.com/)
 [![Git](https://img.shields.io/badge/Version%20Control-Git-blue)](https://git-scm.com/)
 [![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)](https://powerbi.microsoft.com/)
 [![Google Cloud Platform](https://img.shields.io/badge/Cloud%20Provider-Google%20Cloud%20Platform-blue)](https://cloud.google.com/)


