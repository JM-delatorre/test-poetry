from app.dto.requests.seeder_request_dto import SeederRequestDTO
from app.dto.responses.seeder_response_dto import SeederResponsetDTO
import boto3

BCC_USER = "bcc_user"
BCC_PASSWORD = "bcc_password"
BCC_CIPHER_KEY_1 = "bcc_cipher_key_1"
BCC_CIPHER_KEY_2 = "bcc_cipher_key_2"
BCC_URL = "bcc_url"
ASNET_USER = "asnet_user"
ASNET_PASSWORD = "asnet_password"
ASNET_CIPHER_KEY_1 = "asnet_cipher_key_1"
ASNET_CIPHER_KEY_2 = "asnet_cipher_key_2"
ASNET_PIN_BLOCK_KEY_1 = "asnet_pin_block_key_1"
ASNET_PIN_BLOCK_KEY_2 = "asnet_pin_block_key_2"
ASNET_URL = "asnet_url"
SFTP_USER = "sftp_user"
SFTP_PASSWORD = "sftp_password"
SFTP_URL = "sftp_url"

class SeederService:

    def __init__(self) -> None:
        pass

    def list(self) -> str:
        aws_secrets_manager_client = boto3.client("secretsmanager")
        secret_list = aws_secrets_manager_client.list_secrets()
        return secret_list["SecretList"]

    def save(self, seeder_request: SeederRequestDTO) -> None:
        aws_secrets_manager_client = boto3.client("secretsmanager")
        aws_secrets_manager_client.create_secret(NAme = BCC_USER, SecretString = seeder_request.bcc_user)
        aws_secrets_manager_client.create_secret(NAme = BCC_PASSWORD, SecretString = seeder_request.bcc_password)
        aws_secrets_manager_client.create_secret(NAme = BCC_CIPHER_KEY_1, SecretString = seeder_request.bcc_cipher_key_1)
        aws_secrets_manager_client.create_secret(NAme = BCC_CIPHER_KEY_2, SecretString = seeder_request.bcc_cipher_key_2)
        aws_secrets_manager_client.create_secret(NAme = BCC_URL, SecretString = seeder_request.bcc_url)
        aws_secrets_manager_client.create_secret(NAme = ASNET_USER, SecretString = seeder_request.asnet_user)
        aws_secrets_manager_client.create_secret(NAme = ASNET_PASSWORD, SecretString = seeder_request.asnet_password)
        aws_secrets_manager_client.create_secret(NAme = ASNET_CIPHER_KEY_1, SecretString = seeder_request.asnet_cipher_key_1)
        aws_secrets_manager_client.create_secret(NAme = ASNET_CIPHER_KEY_2, SecretString = seeder_request.asnet_cipher_key_2)
        aws_secrets_manager_client.create_secret(NAme = ASNET_PIN_BLOCK_KEY_1, SecretString = seeder_request.asnet_pin_block_key_1)
        aws_secrets_manager_client.create_secret(NAme = ASNET_PIN_BLOCK_KEY_2, SecretString = seeder_request.asnet_pin_block_key_2)
        aws_secrets_manager_client.create_secret(NAme = ASNET_URL, SecretString = seeder_request.asnet_url)
        aws_secrets_manager_client.create_secret(NAme = SFTP_USER, SecretString = seeder_request.sftp_user)
        aws_secrets_manager_client.create_secret(NAme = SFTP_PASSWORD, SecretString = seeder_request.sftp_password)
        aws_secrets_manager_client.create_secret(NAme = SFTP_URL, SecretString = seeder_request.sftp_url)

    def update(self, seeder_request: SeederRequestDTO) -> None:
        aws_secrets_manager_client = boto3.client("secretsmanager")
        aws_secrets_manager_client.put_secret_value(NAme = BCC_USER, SecretString = seeder_request.bcc_user)
        aws_secrets_manager_client.put_secret_value(NAme = BCC_PASSWORD, SecretString = seeder_request.bcc_password)
        aws_secrets_manager_client.put_secret_value(NAme = BCC_CIPHER_KEY_1, SecretString = seeder_request.bcc_cipher_key_1)
        aws_secrets_manager_client.put_secret_value(NAme = BCC_CIPHER_KEY_2, SecretString = seeder_request.bcc_cipher_key_2)
        aws_secrets_manager_client.put_secret_value(NAme = BCC_URL, SecretString = seeder_request.bcc_url)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_USER, SecretString = seeder_request.asnet_user)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_PASSWORD, SecretString = seeder_request.asnet_password)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_CIPHER_KEY_1, SecretString = seeder_request.asnet_cipher_key_1)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_CIPHER_KEY_2, SecretString = seeder_request.asnet_cipher_key_2)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_PIN_BLOCK_KEY_1, SecretString = seeder_request.asnet_pin_block_key_1)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_PIN_BLOCK_KEY_2, SecretString = seeder_request.asnet_pin_block_key_2)
        aws_secrets_manager_client.put_secret_value(NAme = ASNET_URL, SecretString = seeder_request.asnet_url)
        aws_secrets_manager_client.put_secret_value(NAme = SFTP_USER, SecretString = seeder_request.sftp_user)
        aws_secrets_manager_client.put_secret_value(NAme = SFTP_PASSWORD, SecretString = seeder_request.sftp_password)
        aws_secrets_manager_client.put_secret_value(NAme = SFTP_URL, SecretString = seeder_request.sftp_url)
