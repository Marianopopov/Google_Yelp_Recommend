
## Requirement
# google-cloud-dataproc
# google-cloud-core
# nltk 
# pandas
# slack-sdk
# python-decouple


from decouple import config 

API_KEY_SLACK = config('API_KEY_SLACK')


def hello_gcs(event, context):
    from google.cloud import dataproc_v1 as dataproc
    from google.cloud.dataproc_v1.types import Job
    from google.api_core.client_options import ClientOptions

    import subprocess
    library_to_install = 'slack-sdk'
    subprocess.check_call(['pip', 'install', library_to_install])
    
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



    
    
    file = event
    print(f"Processing file: {file['name']}.")
    send_message(f"Comenzando carga incremental de: {file['name']}.")
    

    # Configura el cliente de Cloud Dataproc con el punto final correcto
    client_options = ClientOptions(api_endpoint='us-central1-dataproc.googleapis.com:443')
    
    print('antes del criente')
    cliente = dataproc.JobControllerClient(client_options=client_options)
    print('despues del cliente')
  
    try:
      # Especifica los parámetros del job de PySpark
      project_id = 'bionic-store-413117'
      region = 'us-central1'
      cluster_name = 'cluster-dc06'
      job_file_uri = f"gs://data_raw_pf/cloud_function_py/{file['name'][:-6] +'py'}"
      
    except:
      print('Este archivo no existe')
    
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
    operation = cliente.submit_job_as_operation(
        project_id=project_id,
        region=region,
        job=job
    )
    print('finalizaciin de trabajo...')

    # Espera a que el job se complete
    operation.result()

    print('Job completado con éxito.')
    send_message(f"Finalizando carga incremental de: {file['name']}.")
