
## Requirement
#  google-cloud-dataproc
#  google-cloud-core
# nltk 
# pandas

def hello_gcs(event, context):
    from google.cloud import dataproc_v1 as dataproc
    from google.cloud.dataproc_v1.types import Job
    from google.api_core.client_options import ClientOptions

    file = event
    print(f"Processing file: {file['name']}.")
  
    # Configura el cliente de Cloud Dataproc con el punto final correcto
    client_options = ClientOptions(api_endpoint='us-central1-dataproc.googleapis.com:443')
    
    print('antes del criente')
    client = dataproc.JobControllerClient(client_options=client_options)
    print('despues del cliente')
    
    # Especifica los parámetros del job de PySpark
    project_id = 'bionic-store-413117'
    region = 'us-central1'
    cluster_name = 'cluster-dc06'
    job_file_uri = 'gs://proyecto_final_henry/etl_incremental.py'
    
    print('prejob')
    
    # Define la configuración del job
    job = Job(
        placement=dict(
            cluster_name=cluster_name
        ),
        pyspark_job=dict(
            main_python_file_uri=job_file_uri
        )
    )

    # Envía el job a Cloud Dataproc
    print('enviar el trabajo...')
    operation = client.submit_job_as_operation(
        project_id=project_id,
        region=region,
        job=job
    )
    print('finalizaciin de trabajo...')

    # Espera a que el job se complete
    operation.result()

    print('Job completado con éxito.')
