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

tip_2022_path = 'gs://data_raw_pf/tip_2022.csv.gz'
tip_2022 = pd.read_csv(tip_2022_path)

tip_2022.drop_duplicates(inplace=True)

sid = SentimentIntensityAnalyzer()
tip_2022['sentiment'] = tip_2022['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
tip_2022['sentiment_numeric'] = tip_2022['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))


columnas_a_eliminar3 = ['text', 'compliment_count', 'sentiment']
tip_2022 = tip_2022.drop(columnas_a_eliminar3, axis=1)

nuevos_nombres = {
    'user_id': 'User_Id',
    'business_id': 'Business_Id',
    'date': 'Fecha',
    'año': 'Año',
    'sentiment_numeric': 'Analisis_Sentimiento',
   }

tip_2022.rename(columns=nuevos_nombres, inplace=True)

#concatenarlo
tip_file_path = 'gs://data_clear/tip_clear.csv.gz'
tip_clear = pd.read_csv(tip_file_path, compression='gzip')

tip_clear_full = pd.concat([tip_clear, tip_2022])
tip_clear_full.drop_duplicates(inplace=True)
tip_clear_full.to_csv(tip_file_path ,compression='gzip',index=False)

eliminar_archivo_gs('data_raw_pf','tip_2022.csv.gz')

