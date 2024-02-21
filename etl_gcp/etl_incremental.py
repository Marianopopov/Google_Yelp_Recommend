# %%
import pandas as pd
import ast
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

users_2022_file_path = 'gs://proyecto_final_henry/users_2022.csv.gz'
users_2022 = pd.read_csv(users_2022_file_path, compression='gzip')

users_2022.drop_duplicates(inplace=True)

columnas_a_eliminar = ['compliment_more', 'compliment_profile', 'compliment_cute',
       'compliment_list', 'compliment_note', 'compliment_plain',
       'compliment_cool', 'compliment_funny', 'compliment_writer',
       'compliment_photos', 'friends', 'compliment_hot', 'yelping_since', 'elite']
users_2022 = users_2022.drop(columnas_a_eliminar, axis=1)

nuevos_nombres = {
    'user_id': 'User_Id',
    'name': 'Nombre',
    'review_count': 'Cantidad_Reviews',
    'useful': 'Review_Util',
    'funny': 'Review_Graciosa',
    'cool': 'Review_Cool',
    'fans': 'Cantidad_Fans',
    'average_stars': 'Promedio_Estrellas',
    'date_create_user': 'Fecha_Creación_Usuario'
}
users_2022.rename(columns=nuevos_nombres, inplace=True)

## concatenarlo
users_file_path = 'gs://datos_procesados/users_clear.csv.gz'
users_clear = pd.read_csv(users_file_path, compression='gzip')

users_clear_full = pd.concat([users_clear, users_2022])
users_clear_full.to_csv('gs://datos_procesados/users_clear.csv.gz',compression='gzip',index=False)

############# Tips

tip_2022_path = 'gs://proyecto_final_henry/tip_2022.csv.gz'
tip_2022 = pd.read_csv(tip_2022_path)

tip_2022.drop_duplicates(inplace=True)

print('antes del analis de sentimiento ')
sid = SentimentIntensityAnalyzer()
tip_2022['sentiment'] = tip_2022['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
tip_2022['sentiment_numeric'] = tip_2022['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))
print('Ya se hizo el analisis')

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
tip_clear_full.to_csv(tip_file_path ,compression='gzip',index=False)


## Reviews

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

reviews_clear_full.to_csv('gs://datos_procesados/reviews_clear.csv.gz',compression='gzip',index=False)



