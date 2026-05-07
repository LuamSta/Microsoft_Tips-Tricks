from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import NoEncryption

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = ''
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = ''
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = ''
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = ''
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '' 
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = f'https://login.microsoftonline.com/{TENANT_ID}'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''
    
        
    #cert file path
    CERT_LOCATION = r'./.../....filename.pfx'
    
    #cert pass
    CERT_PASS = b'pass for cert'
    
    with open(CERT_LOCATION, "rb") as f:
        pfx_data = f.read()

    private_key, certificate, additional_certificates = load_key_and_certificates(
        pfx_data,
        CERT_PASS
    )

    # Get SHA1 thumbprint
    CERT_THUMBPRINT = certificate.fingerprint(hashes.SHA1()).hex().upper()
    
    PRIVATE_KEY_PEM = private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=NoEncryption()
    ).decode()


