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
  <img src="images/workflow.jpg" width=600>
</div>

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

## Deploy en Streamlit

Realizamos una página web interactiva a través de la herramienta streamlit mediante el cual presentamos nuestros productos desarrollados como son un dashboard y un modelo de recomendación. 

<a href="https://datavision-hfdze4a6jq-uc.a.run.app/">Link Página web</a>

<!-- <div align="center">
  <img src="images/dashboard.gif" width=400>
  <img src="images/dashboard2.gif" width=400>
</div>

<div align="center">
  <img src="images/modelo_480.gif" width=400>
  <img src="images/modelo_480_2.gif" width=400>
</div> -->

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


