import pandas as pd

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

## Enviar mensajes desde slack

import subprocess
library_to_install = 'slack-sdk'

subprocess.check_call(['pip', 'install', library_to_install])

API_KEY_SLACK = config('API_KEY_SLACK')

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_API_TOKEN_BOT = API_KEY_SLACK
channel_id = 'C06KT0S0QRF' # Canal gc-notifications
client = WebClient(token=SLACK_API_TOKEN_BOT)


def send_message(message):
        try:
            response = client.chat_postMessage(
                channel=channel_id,
                text=message
             )
            print(f"Message sent: {response['ts']}")
        except SlackApiError as e:
            print(f"Error sending message: {e.response['error']}")


send_message(f'Se Inicalizó carga incremental de tip del año 2022')

from google.cloud import storage
def eliminar_archivo_gs(bucket_name, file_name):
    # Inicializa el cliente de Google Cloud Storage
    client = storage.Client()

    # Obtiene el bucket
    bucket = client.bucket(bucket_name)

    # Elimina el archivo
    blob = bucket.blob(file_name)
    blob.delete()

tip_2022_path = 'gs://proyecto_final_henry/tip_2022.csv.gz'
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
tip_file_path = 'gs://datos_procesados/tip_clear.csv.gz'
tip_clear = pd.read_csv(tip_file_path, compression='gzip')

tip_clear_full = pd.concat([tip_clear, tip_2022])
tip_clear_full.drop_duplicates(inplace=True)
tip_clear_full.to_csv(tip_file_path ,compression='gzip',index=False)

eliminar_archivo_gs('proyecto_final_henry','tip_2022.csv.gz')

