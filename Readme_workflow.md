Elegimos realizar la visualizacion e interaccion con los dos productos terminados que ofrecemos, hacerlo a traves de una web. Esta web prrermite interactuar con los dos grandes resultados de nuestro trabajo:

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
= Cada contenedor corre independientemente del resto, compartiendo el Kernel del sistema operativo pero no recursos.
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
- Cambiando streamlit como fron-end framework (por ejemplo por React JS), el deploy en la nube previo creado el contenedor, es identico.


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



