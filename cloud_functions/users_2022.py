import pandas as pd

from google.cloud import storage

def eliminar_archivo_gs(bucket_name, file_name):
    # Inicializa el cliente de Google Cloud Storage
    client = storage.Client()

    # Obtiene el bucket
    bucket = client.bucket(bucket_name)

    # Elimina el archivo
    blob = bucket.blob(file_name)
    blob.delete()

users_2022_file_path = 'gs://data_raw_pf/users_2022.csv.gz'
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
users_file_path = 'gs://data_clear/users_clear.csv.gz'
users_clear = pd.read_csv(users_file_path, compression='gzip')

users_clear_full = pd.concat([users_clear, users_2022])
users_clear_full.drop_duplicates(inplace=True)
users_clear_full.to_csv('gs://data_clear/users_clear.csv.gz',compression='gzip',index=False)

eliminar_archivo_gs('data_raw_pf','users_2022.csv.gz')
