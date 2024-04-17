import base64
import imghdr
from google.cloud import storage

async def upload_image_to_gcs(image_string: str, filename: str):
    try:
        # Decodifique a string base64 para obter os bytes da imagem
        image_bytes = base64.b64decode(image_string)

        # Determine a extensão da imagem
        image_extension = imghdr.what(None, h=image_bytes)

        # Verifique se a extensão da imagem é suportada (por exemplo, 'png' ou 'jpeg')
        if not image_extension or image_extension not in ('png', 'jpeg'):
            raise ValueError('Formato de imagem não suportado')

        # Inicialize o cliente do Google Cloud Storage
        storage_client = storage.Client()

        # Seu nome do bucket no Google Cloud Storage
        bucket_name = "med-image"

        # Inicialize o objeto Blob
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"{filename}.{image_extension}")

        # Faça o upload do arquivo de imagem para o Google Cloud Storage
        blob.upload_from_string(image_bytes, content_type=f"image/{image_extension}")

        # Gere uma URL de acesso público para o objeto
        public_url = f"https://storage.googleapis.com/{bucket_name}/{filename}.{image_extension}"

        # Defina a política de controle de acesso para permitir acesso público ao bucket
        policy = bucket.get_iam_policy(requested_policy_version=3)
        policy.bindings.append(
            {
                "role": "roles/storage.objectViewer",
                "members": {"allUsers"},
            }
        )
        bucket.set_iam_policy(policy)

        # Retorne a URL do arquivo de imagem no Google Cloud Storage
        return public_url

    except Exception as e:
        # Trate qualquer exceção que possa ocorrer durante o processo de upload
        print(f"Erro ao enviar arquivo {filename} para o Google Cloud Storage: {e}")
        return None
