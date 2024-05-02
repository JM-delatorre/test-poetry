from fastapi import Query
from pydantic import BaseModel

class SeederRequestDTO(BaseModel):
    #Fields for BCC Services
    bcc_user: str = Query(description="BCC User.", min_length=5)
    bcc_password: str = Query(description="BCC Password.", min_length=5)
    bcc_cipher_key_1: str = Query(description="BCC Cipher Key 1.", min_length=5)
    bcc_cipher_key_2: str = Query(description="BCC Cipher Key 2.", min_length=5)
    bcc_url: str = Query(description="BCC URL.", min_length=5)

    #Fields for ASNET Services
    asnet_user: str = Query(description="ASNET User.", min_length=5)
    asnet_password: str = Query(description="ASNET Password.", min_length=5)
    asnet_cipher_key_1: str = Query(description="ASNET Cipher Key 1.", min_length=5)
    asnet_cipher_key_2: str = Query(description="ASNET Cipher Key 2.", min_length=5)
    asnet_pin_block_key_1: str = Query(description="ASNET Pin Block Key 1.", min_length=5)
    asnet_pin_block_key_2: str = Query(description="ASNET Pin Block Key 2.", min_length=5)
    asnet_url: str = Query(description="ASNET URL.", min_length=5)

    #Fields for SFTP
    sftp_user: str = Query(description="SFTP User.", min_length=5)
    sftp_password: str = Query(description="SFTP Password.", min_length=5)
    sftp_url: str = Query(description="SFTP URL.", min_length=5)

