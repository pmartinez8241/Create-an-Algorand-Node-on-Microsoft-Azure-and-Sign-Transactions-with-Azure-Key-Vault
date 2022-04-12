import os
from algosdk.future import transaction
from algosdk.future.transaction import PaymentTxn
from algosdk import constants
import azure_keyvault_helpers as kv_helpers
from algosdk.v2client import algod
from dotenv import load_dotenv

load_dotenv()
#NODE VARIABLES

#NODE HTTP ADDRESS
algorand_node_address = os.environ['ALGORAND_NODE_ADDRESS']

#NODE REST API TOKEN
algorand_node_rest_token = os.environ['ALGORAND_NODE_REST_TOKEN']


#ACCOUNT VARIABLES
algorand_sender_account_address = os.environ['ALGORAND_SENDER_ACCOUNT_ADDRESS']
algorand_account_private_key = kv_helpers.get_keyvault_secret(algorand_sender_account_address+"-PK")

#RECEIVER ACCOUNT ADDRESS
algorand_receiver_account = os.environ['ALGORAND_RECEIVER_ACCOUNT_ADDRESS']

algod_client = algod.AlgodClient(algorand_node_rest_token,algorand_node_address)

my_address = algorand_sender_account_address
params = algod_client.suggested_params()
params.flat_fee = True

# The MIN_TXN_FEE constant is equal to 1000 microAlgos
params.fee = constants.MIN_TXN_FEE

note = "Algorand on Azure Tutorial Transaction".encode()

'''
Transfer amounts are done in microAlgos

Ten Million microAlgos are equal to Ten Algos
'''
amount = 10000000

# PREPARE THE TRANSACTION FOR SIGNING
unsigned_txn = transaction.PaymentTxn(algorand_sender_account_address, params, algorand_receiver_account, amount, None, note)

# NOW WE CAN SIGN THE TRANSACTION WITH OUR PRIVATE KEY

signed_txn = unsigned_txn.sign(algorand_account_private_key)

# LAST WE WILL SEND OUR TRANSACTION AND PRINT THE TRANSACTION NUMBER

transaction_id = algod_client.send_transaction(signed_txn)

print(transaction_id)