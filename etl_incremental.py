# %%
import pandas as pd
import ast
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

csv_file_path = 'gs://proyecto_final_henry/users_2022.csv.gz'

df = pd.read_csv(csv_file_path, compression='gzip')

df.drop_duplicates(inplace=True)
columnas_a_eliminar = ['compliment_more', 'compliment_profile', 'compliment_cute',
       'compliment_list', 'compliment_note', 'compliment_plain',
       'compliment_cool', 'compliment_funny', 'compliment_writer',
       'compliment_photos', 'friends', 'compliment_hot', 'yelping_since', 'elite']

df = df.drop(columnas_a_eliminar, axis=1)


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

df.rename(columns=nuevos_nombres, inplace=True)

df.to_csv('gs://datos_procesados/users_clean_2022.csv.gz',compression='gzip',index=False)

## businees

# csv_file_path = 'gs://proyecto_final_henry/business.csv.gz'
# df_business = pd.read_csv(csv_file_path)

# def extract_values(row):
#     try:
#         attributes_dict = ast.literal_eval(row['attributes'])
#         take_out = attributes_dict.get('RestaurantsTakeOut', None)
#         delivery = attributes_dict.get('RestaurantsDelivery', None)
#         good_for_kids = attributes_dict.get('GoodForKids', None)
#         accepts_credit_cards = attributes_dict.get('BusinessAcceptsCreditCards', None)
#         reservations = attributes_dict.get('RestaurantsReservations', None)

#         return pd.Series({
#             'RestaurantsTakeOut': take_out,
#             'RestaurantsDelivery': delivery,
#             'GoodForKids': good_for_kids,
#             'BusinessAcceptsCreditCards': accepts_credit_cards,
#             'RestaurantsReservations': reservations
#         })
#     except (SyntaxError, ValueError):
#         return pd.Series({
#             'RestaurantsTakeOut': None,
#             'RestaurantsDelivery': None,
#             'GoodForKids': None,
#             'BusinessAcceptsCreditCards': None,
#             'RestaurantsReservations': None
#         })
        
# new_columns = df_business.apply(extract_values, axis=1)

# df_business = pd.concat([df_business, new_columns], axis=1)
# df_business['hours'] = df_business['hours'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
# df_business = pd.concat([df_business.drop(['hours'], axis=1), df_business['hours'].apply(pd.Series)], axis=1)

# df_business = df_business.rename(columns={
#     'Monday': 'Monday_Hours',
#     'Tuesday': 'Tuesday_Hours',
#     'Wednesday': 'Wednesday_Hours',
#     'Thursday': 'Thursday_Hours',
#     'Friday': 'Friday_Hours',
#     'Saturday': 'Saturday_Hours',
#     'Sunday': 'Sunday_Hours'
# })

# columnas_a_eliminar2 = ['postal_code', 'attributes', 'categories',
#        0]

# df_business = df_business.drop(columnas_a_eliminar2, axis=1)

# nuevos_nombres = {
#     'business_id': 'Business_Id',
#     'name': 'Nombre',
#     'address': 'Direccion',
#     'city': 'Ciudad',
#     'state': 'Estado',
#     'latitude': 'Latitud',
#     'longitude': 'Longitud',
#     'stars': 'Estrellas',
#     'review_count': 'Cantidad_Reviews',
#     'is_open': 'Negocio_Abierto',
#     'RestaurantsDelivery': 'Delivery',
#     'RestaurantsTakeOut': 'Comida_Para_Llevar',
#     'GoodForKids': 'Amigable_Para_Chicos',
#     'BusinessAcceptsCreditCards': 'Acepta_Tarjeta_Credito',
#     'RestaurantsReservations': 'Acepta_Reservaciones',
#     'Monday_Hours': 'Horario_Lunes',
#     'Tuesday_Hours': 'Horario_Martes',
#     'Wednesday_Hours': 'Horario_Miercoles',
#     'Thursday_Hours':'Horario_Jueves',
#     'Friday_Hours': 'Horario_Viernes',
#     'Saturday_Hours':'Horario_Sabado',
#     'Sunday_Hours': 'Horario_Domingo'


# }

# df_business.rename(columns=nuevos_nombres, inplace=True)

# df_business.to_csv('gs://proyecto_final_henry/clear/business_clear.csv.gz')

## Tips

csv_file_path = 'gs://proyecto_final_henry/tip_2022.csv.gz'
df_tip = pd.read_csv(csv_file_path)

df_tip.drop_duplicates(inplace=True)

print('antes del analis de sentimiento ')
sid = SentimentIntensityAnalyzer()
df_tip['sentiment'] = df_tip['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
df_tip['sentiment_numeric'] = df_tip['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))
print('Ya se hizo el analisis')

columnas_a_eliminar3 = ['text', 'compliment_count', 'sentiment']
df_tip = df_tip.drop(columnas_a_eliminar3, axis=1)

nuevos_nombres = {
    'user_id': 'User_Id',
    'business_id': 'Business_Id',
    'date': 'Fecha',
    'año': 'Año',
    'sentiment_numeric': 'Analisis_Sentimiento',
   }

df_tip.rename(columns=nuevos_nombres, inplace=True)

print('sigue cargar tips')
df_tip.to_csv('gs://datos_procesados/tip_clear_2022.csv.gz')

## Reviews

csv_file_path = 'gs://proyecto_final_henry/reviews_2022.csv.gz'
df_reviews = pd.read_csv(csv_file_path)


sid = SentimentIntensityAnalyzer()
df_reviews['sentiment'] = df_reviews['text'].apply(lambda x: sid.polarity_scores(str(x))['compound'])
df_reviews['sentiment_numeric'] = df_reviews['sentiment'].apply(lambda x: 2 if x > 0.05 else (1 if -0.05 <= x <= 0.05 else 0))

columnas_a_eliminar4 = ['text', 'sentiment']
df_reviews = df_reviews.drop(columnas_a_eliminar4, axis=1)

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

df_reviews.rename(columns=nuevos_nombres, inplace=True)

df_reviews.to_csv('gs://datos_procesados/reviews_clear_2022.csv.gz',index='False')


