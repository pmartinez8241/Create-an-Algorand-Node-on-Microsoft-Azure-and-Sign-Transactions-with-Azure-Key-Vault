from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient


credentials = ManagedIdentityCredential()
secret_client = SecretClient(r'https://algo-tutorial-secrets.vault.azure.net/',credentials)

# The name of the secret is used to get the secret in the get_keyvault_secret() function
def set_keyvault_secret(secret_name, secret_value):
    result = secret_client.set_secret(secret_name,secret_value)
    created_secret = "Secret created\nName = {}\nDate Create = {}".format(result.name,result.properties.created_on)
    print(created_secret)
'''
The get_secret functions returns all of the information regarding a Secret. 
For this tutorial we will only be retrieving the value.
'''
def get_keyvault_secret(secret_name):
    result = secret_client.get_secret(secret_name)
    return result.value