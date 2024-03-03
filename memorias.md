# 31-enero

- Desanidamos la columna resp, para extraer el texto de respuesta de la empresa junto con la fecha

- Verificamos nulos, duplicados y eliminamos duplicados, las columnas con datos faltantes con mas del 96%
las eliminamos

- Convertimos la fecha de formato unix a formato fecha año mes y dia.

- Graficos con los estados

## 1-febrero

- Organizar el readme

## Division de tareas

Mariano : dataflow, etl final en pyspark (google)  
 
Martin : dataflow, etl final en pyspark (google)

Belen : dataflow, etl final en pyspark (google)

Alejo :  dataflow, etl final en pyspark (yelp)

Marcelo : dataflow, etl final en pyspark (yelp)

- Entendimiento de la situación actual:

- Objetivos

- Alcance

- Objetivos y KPIs asociados (planteo)


## Creacion de tabla en bigquery

CREATE OR REPLACE EXTERNAL TABLE `bionic-store-413117.yelp.users`
OPTIONS (
  format='CSV',
  uris=['gs://datos_procesados/users_clear.csv.gz']
);

