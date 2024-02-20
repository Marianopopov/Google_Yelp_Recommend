import pandas as pd
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

reviews_2022_path = 'gs://proyecto_final_henry/reviews_2022.csv.gz'
reviews_2022 = pd.read_csv(reviews_2022_path)


sid = SentimentIntensityAnalyzer()
reviews_2022['sentiment'] = reviews_2022['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
reviews_2022['sentiment_numeric'] = reviews_2022['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))

columnas_a_eliminar4 = ['text', 'sentiment']
reviews_2022 = reviews_2022.drop(columnas_a_eliminar4, axis=1)

nuevos_nombres = {
    'review_id': 'Review_Id',
    'user_id': 'User_Id',
    'business_id':'Business_Id',
    'stars': 'Estrellas',
    'useful': 'Review_Util',
    'funny': 'Review_Graciosa',
    'cool': 'Review_Cool',
    'date': 'Fecha',
    'año': 'Año',
    'sentiment_numeric': 'Analisis_Sentimiento'
}

reviews_2022.rename(columns=nuevos_nombres, inplace=True)

reviews_clear = pd.read_csv('gs://datos_procesados/reviews_clear.csv.gz')

reviews_clear_full = pd.concat([reviews_clear, reviews_2022])
reviews_clear_full.drop_duplicates(inplace=True)

reviews_clear_full.to_csv('gs://datos_procesados/reviews_clear.csv.gz',compression='gzip',index=False)

eliminar_archivo_gs('proyecto_final_henry','reviews_2022.csv.gz')

