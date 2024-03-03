import pandas as pd
from google.cloud import storage

csv_file_path = 'gs://data_raw_pf/info_estados.csv.gz'
info = pd.read_csv(csv_file_path)

nuevos_nombres = {
    'nombre_estado': 'Estado',
    ' poblacion': 'Poblacion',
    'PBI_pc': 'PBI',
    'area_kms': 'Area_Kms',
    'ingreso_medio': 'Ingreso_Medio',
}
info.rename(columns=nuevos_nombres, inplace=True)


def eliminar_archivo_gs(bucket_name, file_name):
    # Inicializa el cliente de Google Cloud Storage
    client = storage.Client()

    # Obtiene el bucket
    bucket = client.bucket(bucket_name)

    # Elimina el archivo
    blob = bucket.blob(file_name)
    blob.delete()


info.to_csv('gs://data_clear/info_estados_clear.csv.gz',compression='gzip',index=False)
eliminar_archivo_gs('data_raw_pf','info_estados.csv.gz')
