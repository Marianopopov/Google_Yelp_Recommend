# <a name="readme-top"></a>

# <h1 align="center">*GOOGLE MAPS_YELP - RECOMMENDATIONS*</h1>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="100">
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="100">

## *Índice de Contenidos*

- [Introducción](#introducción)
- [Contexto](#contexto)
- [Alcance](#alcance)
  - [Cronograma](#cronograma)
  - [Diagrama de Gantt](#diagrama-de-gantt)
  - [KPIs](#kpis)
  - [Restricciones y Limitaciones](#restricciones-y-limitaciones)
- [Entregables](#entregables)
- [Stack tecnológico](#stack-tecnológico)
- [Fuentes de datos](#fuentes-de-datos)
- [Acerca de nosotros](#acerca-de-nosotros)


## *Introducción*

Como parte de una consultora de datos, hemos sido contratados para llevar a cabo un análisis del mercado estadounidense. Nuestro cliente forma parte de un conglomerado de empresas relacionadas con restaurantes relacionadas al rubro fast food, y buscan obtener un análisis detallado de las opiniones de los usuarios en Yelp y cruzarlas con las de Google Maps en relación a dicho rubro. Utilizando análisis de sentimientos, nuestro objetivo es prever si el rubro fast food experimentará un mayor crecimiento o declive.

Además nuestro cliente desea determinar estratégicamente la ubicación de nuevos locales de restaurantes, implementando un sistema de recomendación de restaurantes fast food para usuarios en ambas plataformas. Este sistema ofrecería a los usuarios la oportunidad de descubrir nuevos sabores basados en sus experiencias previas


## Contexto

<summary><h2>Alcance</h2></summary>

El presente documento establece el alcance del proyecto de análisis de opiniones de usuarios

### Objetivos del Proyecto

### Diagrama de Gantt

El proyecto seguirá una metodología de trabajo en equipo que incluye las siguientes etapas:


<div align="center">

<img src="./images/gantt.jpg" >
</div>

### *KPIs*

- **Respuestas de negocios**

$$\frac{\frac{\text{$\sum$ resp año actual}}{\text{$\sum$ reseñas año actual}} - \frac{\text{$\sum$ resp año anterior}}{\text{$\sum$ reseñas año anterior}} }{\frac{\text{$\sum$ resp año anterior}}{\text{$\sum$ reseñas año anterior}}}
$$




<p align='center'> <b>Objetivo:</b> Queremos aumentar las respuestas de negocios en un 10% respecto al año anterior.

----------------------
- **Evolución de la Cantidad de negocios**

$$\frac{\text{$\sum$ business actual} - \text{$\sum$ business anterior} }{\text{$\sum$  business anterior}}
$$

 <p align='center'><b>Objetivo:</b> Queremos aumentar las respuestas de negocios en un 10% respecto al año anterior.

-----------------

- **Cantidad de Rating positivos**
  $$\frac{\sum \text{(reviews positivas actuales)} - \sum\text{(reviews positivas año anterior)}}{\sum\text{(reviews positivas año anterior)}}$$

 Una review positiva es cuando recibe 4 o 5 estrellas.

 <p align='center'><b>Objetivo:</b> Queremos aumentar las respuestas de negocios en un 10% respecto al año anterior.

--------

- **Densidad de area de negocio**

  $$Ratio_{area}  = \frac{\sum \text{(business actual)} }{\text{Área estado}}$$

  <p align='center'> <b>Objetivo:</b> Queremos aumentar las respuestas de negocios en un 10% respecto al año anterior.


--------------------

- **Satisfacción de clientes**

    $$\frac{\sum{reviews(_{positivos}^{sentimiento})}}{\sum{reviews}}$$

 <p align='center'><b>Objetivo:</b> Queremos aumentar las respuestas de negocios en un 10% respecto al año anterior.

--------------------

### *Entregables*

### *Restricciones y Limitaciones*

El proyecto se limita al análisis de datos disponibles en Yelp y Google Maps para el mercado estadounidense.
La disponibilidad y calidad de los datos pueden afectar los resultados del análisis.
El alcance del proyecto no incluye la implementación de sistemas en producción, sino la entrega de modelos y recomendaciones listos para su implementación.

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

</details>

### *Stack tecnológico*

- [![Visual Studio Code](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-blue)](https://code.visualstudio.com/)
- [![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange)](https://jupyter.org/)
- [![Pandas](https://img.shields.io/badge/Library-Pandas-brightgreen)](https://pandas.pydata.org/)
- [![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-blue)](https://matplotlib.org/)
- [![Seaborn](https://img.shields.io/badge/Library-Seaborn-yellow)](https://seaborn.pydata.org/)
- [![Folium](https://img.shields.io/badge/Library-Folium-green)](https://python-visualization.github.io/folium/)
- [![GitHub](https://img.shields.io/badge/Platform-GitHub-lightgrey)](https://github.com/)
- [![Git](https://img.shields.io/badge/Version%20Control-Git-blue)](https://git-scm.com/)
- [![MySQL](https://img.shields.io/badge/Database-MySQL-orange)](https://www.mysql.com/)
- [![Power BI](https://img.shields.io/badge/BI%20Tool-Power%20BI-yellow)](https://powerbi.microsoft.com/)

## Cronograma

El proyecto se desarrollará en un período de 6 semanas, con tres sprint que son los siguientes:

- Sprint 1: Puesta en macha del proyecto. 2 Semanas

- Sprint 2: Data Engineering. 2 Semanas

- Sprint 3: Data Analitics y Machine learning. 2 Semanas.

## *Fuentes de datos*

- [Diccionario de Datos](https://docs.google.com/document/d/1ASLMGAgrviicATaP1UJlflpmBCXtuSTHQGWdQMN6_2I/edit)
### Fuentes de datos obligatorias:
- [Dataset de Google Maps](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=share_link)

- [Dataset de Yelp!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing)

## *Acerca de nosotros*

Completar ..... 


[linkedin-logo]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=whiteLogoDelDi%CC%81a-LinkedIn-un-emblema-que-esta%CC%81-22dentro22-1110x366.jpg

[github-logo]: https://img.shields.io/badge/Platform-GitHub-lightgrey

[github-belen]:https://github.com/belenvbecker

[github-mariano]:https://github.com/marianopopov

[github-martin]: https://github.com/martinarielriveros

[github-alejo]: https://github.com/dalejandroramirez

[github-marcelo]: https://github.com/marceloortizz

[linkedin-belen]: https://www.linkedin.com/in/belen-viglioglia-becker/

[linkedin-mariano]: https://www.linkedin.com/in/mariano-popov-3a4570290/

[linkedin-martin]: https://www.linkedin.com/in/martinriveros/

[linkedin-alejo]: https://www.linkedin.com/in/dalejandroramirez/

[linkedin-marcelo]: https://www.linkedin.com/in/marceloortizz/


<table align="center">
  <tr>
    <td align="center"><b>Marcelo Ortiz</td>
    <td align="center"><b>Belén Viglioglia Becker</b></td>
    <td align="center"><b>Alejandro Ramírez</b></td>
    <td align="center"><b>Mariano Popov</b></td>
    <td align="center"><b>Martín Riveros</b></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/marceloortizz/"><img src="https://media.licdn.com/dms/image/D4D03AQHxyKdkjxaNIw/profile-displayphoto-shrink_200_200/0/1703053789448?e=1712188800&v=beta&t=NmtJKYCnsSSZRYZuaTgbDd1_CtBzOdnGHcoUeU6Vnz8" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/belen-viglioglia-becker/"><img src="https://media.licdn.com/dms/image/D4D35AQFiZNYv93A08Q/profile-framedphoto-shrink_200_200/0/1678551884037?e=1707440400&v=beta&t=V2kPAuRNl0E4EQWnhkDp8z5nkPbNvBGroxL9MUxmmrs" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/dalejandroramirez/"><img src="https://media.licdn.com/dms/image/D4E35AQECkqfYTtJetw/profile-framedphoto-shrink_200_200/0/1687559285382?e=1707440400&v=beta&t=sR_ri9ifjcdm9ClpKsLAPPhKAEwk9huQntCl07iL8c4" width=48 style="border-radius:50%"></a></td>
    <td align="center"><a href="https://www.linkedin.com/in/mariano-popov-3a4570290/"><img src="https://media.licdn.com/dms/image/D4E03AQGg5qnxEtISmQ/profile-displayphoto-shrink_200_200/0/1706830288635?e=1712188800&v=beta&t=zlPzR7Hzvz5aiJsdi1LR7ahCyExgvRkcZN6yBXofD0Q" width=48 style="border-radius:50%"> </a></td>
    <td align="center"><a href="https://www.linkedin.com/in/martinriveros/"><img src="https://media.licdn.com/dms/image/D4D03AQHVVaakawEo_g/profile-displayphoto-shrink_800_800/0/1699990983364?e=1712188800&v=beta&t=cvc73VmxiIzKcjSSLqPm9i69xMOCVFXSSA-pSdyTZSY" width=48 style="border-radius:50%"></a></td>
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
</table>
