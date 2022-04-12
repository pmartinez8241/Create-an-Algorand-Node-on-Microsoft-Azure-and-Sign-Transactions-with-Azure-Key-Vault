import os
import azure_keyvault_helpers as azure_kv
from algosdk import account, mnemonic






def create_algorand_account(env_variable_name):

    # CREATE the PRIVATE KEY and ACCOUNT ADDRESS

    account_private_key, account_address = account.generate_account()

    # CREATE a MNEMONIC

    account_mnemonic = mnemonic.from_private_key(account_private_key)

    # ADD PRIVATE KEY to KEYVAULT

    azure_kv.set_keyvault_secret(secret_name="{}-PK".format(account_address),secret_value=account_private_key)

    # ADD MNEMONIC KEY to KEYVAULT
    azure_kv.set_keyvault_secret(secret_name="{}-MNEMONIC".format(account_address),secret_value=account_mnemonic)

    # ADD ALGORAND_ACCOUNT_ADDRESS Environmental Variable to .env

    os.system(r'echo ALGORAND_{}_ACCOUNT_ADDRESS=\"{}\" >> ./.env'.format(env_variable_name,account_address))




create_algorand_account("SENDER")
create_algorand_account("RECEIVER")