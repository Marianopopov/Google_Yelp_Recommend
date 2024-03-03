
import pandas as pd
import os
import ast
from datetime import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from google.cloud import storage

def eliminar_archivo_gs(bucket_name, file_name):
    # Inicializa el cliente de Google Cloud Storage
    client = storage.Client()

    # Obtiene el bucket
    bucket = client.bucket(bucket_name)

    # Elimina el archivo
    blob = bucket.blob(file_name)
    blob.delete()

metadata = pd.read_csv('gs://data_raw_pf/metadata.csv.gz')

metadata[metadata.duplicated()]
print('Duplicados eliminados...')

columnas_a_eliminar = ['description', 'category', 'url',
       'category2', 'price', 'relative_results', 'hours', 'MISC']

metadata = metadata.drop(columnas_a_eliminar, axis=1)
print('Datos eliminado...')
def categorizar_estado(x):
    if 'Permanently closed' in str(x):
        return 'Closed'
    elif 'Temporarily closed' in str(x):
        return 'Temporarily closed'
    else:
        return 'Open'

metadata['state'] = metadata['state'].apply(categorizar_estado)

metadata = metadata.rename(columns={
    'name': 'Nombre',
    'address': 'Direccion',
    'gmap_id': 'Gmap_id',
    'latitude': 'Latitud',
    'longitude': 'Longitud',
    'avg_rating': 'Promedio_rating',
    'num_of_reviews': 'Cantidad_Reviews',
    'state' : 'Estado'

})

metadata.to_csv('gs://data_clear/metadata_clear.csv.gz',index= False)
print('preparando para eliminar')
eliminar_archivo_gs('data_raw_pf', 'metadata.csv.gz')


## Estados

path_estados = 'gs://data_raw_pf/estados_concatenados.csv.gz'
estados = pd.read_csv(path_estados)
print('Tabla estados cargadando')

def convertir_a_diccionario(texto):
    try:
        return ast.literal_eval(texto)
    except (SyntaxError, ValueError):
        return {}


estados['resp'] = pd.Series(estados['resp']).apply(lambda x:  convertir_a_diccionario(x))

def obtener_resp_time(diccionario):
    return diccionario.get('time', None)

def obtener_resp_text(diccionario):
    return diccionario.get('text', None)

estados = pd.concat([estados.drop('resp', axis=1),
                    pd.Series(estados['resp'].apply(lambda x: obtener_resp_time(x)), name='resp_time'),
                    pd.Series(estados['resp'].apply(lambda x: obtener_resp_text(x)), name='resp_text')],
                    axis=1)

estados.drop(columns='pics',inplace=True)

def convertir_fecha(x):
  if x!=0:
    timestamp_unix = x/ 1000 
    fecha = datetime.utcfromtimestamp(timestamp_unix)
    return(fecha.strftime('%Y-%m-%d %H:%M:%S'))
  else:
    return(None)
  
estados['fecha'] = estados['time'].apply(convertir_fecha)
estados['resp_fecha'] = estados['resp_time'].fillna(0).apply(convertir_fecha)
estados.drop(columns=['time','resp_time'],inplace=True)


estados['fecha_anho_mes'] = pd.to_datetime(estados['fecha']).dt.date
estados['anho'] = pd.to_datetime(estados['fecha']).dt.year

def respuesta_tranformacion(x):
  if str(x) == 'nan':
    return(0)
  else:
    return(1)
estados['resp_text'] = estados['resp_text'].apply(respuesta_tranformacion)

print('Inicializamos analisis de sentimiento...')

sid = SentimentIntensityAnalyzer()
estados['sentiment'] = estados['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])

print('analisis de sentimiento realizado')

estados['sentiment_numeric'] = estados['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))


estados.drop(columns=['text','sentiment','fecha','resp_fecha'],inplace=True)
estados['nombre_estado'] = estados['nombre_estado'].apply(lambda x : x[:-8])


estados.to_csv('gs://data_clear/estados_concatenados_clear.csv.gz',index = False)
print('preparando para eliminar')
eliminar_archivo_gs('data_raw_pf', 'estados_concatenados.csv.gz')


print('ETL realizado con exito...')
