# Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault
Tutorial on how to create an Algorand node on a Azure Virtual Machine, as well as Storing Secrets in Azure 


# 1. Create A Virtual Machine

On the Azure Portal Home page search for Virtual machines, then Select Virtual machines under Services as shown in **Figure 1-1**

![EditorImages/2022/03/26 22:44/Figure_1-1_Search_for_and_Select_Virtual_machines.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2022%3A44/Figure_1-1_Search_for_and_Select_Virtual_machines.png) 

Figure 1-1: Search for and Select Virtual machines


On the Virtual machines page select **Create** followed by **Azure virtual machine** as shown in **Figure 1-2**

![EditorImages/2022/03/26 22:54/Figure_1-2_Under_Create_select_Azure_Virtual_Machine.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2022%3A54/Figure_1-2_Under_Create_select_Azure_Virtual_Machine.png)

Figure 1-2: Select **Create** then **Azure virtual machine**
<table align="center">
	<tr>
		<th align="center">
        		<p align="center">
        			:warning: Tip
        		</p>
        	</th>
	</tr>
	<tr>
		<td>
			It is easiest to work with many different resources when they all have a common naming convention. </br>For this tutorial lets name our Virtual Machine AlgorandOnAzureTutorial-VM as shown in Figure 1-3
		</td>
	</tr>
</table>


```
AlgorandOnAzureTutorial-VM
```

![EditorImages/2022/03/26 23:12/Figure_1-3_Set_Virtual_Machine_Name.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A12/Figure_1-3_Set_Virtual_Machine_Name.png)

Figure 1-3: Enter Virtual machine name

!!! Tip
    In this tutorial we will be using image: Ubuntu Server 20.04 LTS - Gen2
* To meet the requirements of 2-4 vCPU, 4-8GB RAM we will be using:
&nbsp;&nbsp;- VM Size: Standard_D2s_v3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + 2 VCPUs
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + 8GB ram

	

<table align="center">
	<tr>
		<th align="center">
        <p align="center">
        	:warning: Tip
        </p>
        </th>
	</tr>
	<tr>
		<td>
			Select a Region closest to your location.
            </br>
            To find a location that is closet to you
            
<div align="center">

[Click Here](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies) 

<div>

</td>
    </tr>
</table>



Currently you should have the same configurations selected as in Figure 1-4, Except for the region which depends on your location. After making sure you configurations look like those of Figure 1-4, click Next : Disks >

![EditorImages/2022/03/26 23:29/Figure_1-4_Virtual_Machine_Configuration.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A29/Figure_1-4_Virtual_Machine_Configuration.png) 

Figure 1-4: Verify your Configuration

!!! Tip
    Azure Virtual Machines come with very little storage so, we are going to have to add a disk
Click on ** Create and attach a new Disk ** as shown in Figure 1-5
![EditorImages/2022/03/26 23:38/Figure_1-5_Create_and_attach_a_new_disk.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A38/Figure_1-5_Create_and_attach_a_new_disk.png) 

Figure 1-5: Select **Create and attach a new Disk**

Click on **Change Size** as shown in Figure 1-6

![EditorImages/2022/03/26 23:43/Figure_1-6_Change_Size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A43/Figure_1-6_Change_Size.png) 

Figure 1-6: Select **Change Size**

To meet the minimum storage requirements dictated by the Algorand Foundation we will create a **256GB Standard SSD**. Once your drive selection looks like Figure 1-7, **click OK**

![EditorImages/2022/03/26 23:56/Figure_1-7_Select_a_disk_size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A56/Figure_1-7_Select_a_disk_size.png) 

Figure 1-7: Create 256GB Standard SSD

**Click OK** once more on the Create a new disk page, shown in Figure 1-8.

![EditorImages/2022/03/27 00:05/Figure_1-8_Disk_Selection_Conclusion.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A05/Figure_1-8_Disk_Selection_Conclusion.png) 

Figure 1-8: Create a new disk page, click OK

!!! Tip
    This is just a basic tutorial, so Networking, Management, advanced, and tags will be left with their default settings
    
From Disks we are going to head straight to ** Review + create **, as highlighted in Figure 1-9

![EditorImages/2022/03/27 00:12/Figure_1-9_Review.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A12/Figure_1-9_Review.png) 

Figure 1-9: Click on Review + create, to review the Virtual Machines final configuration

On the Create a virtual machine page, Check the top of the page to see if you configuration is valid, then select **Create**. Figure 1-10 highlights a configuration that passes validation.

![EditorImages/2022/03/27 01:54/Figure_1-10_Create_the_VM.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2001%3A54/Figure_1-10_Create_the_VM.png)

Figure 1-10: Validate configuration then press Create

Once you click **Create** you are given the option to Download the Key Pair for SSH click ** Download private key and create resource ** as shown in figure 1-11

![EditorImages/2022/03/27 03:04/Figure_1-11_Download_key_pair.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2003%3A04/Figure_1-11_Download_key_pair.png) 

Figure 1-11: Download Private Key and Create Resources


!!! Alert
    When having Azure generate a key pair you may not get a .PEM file, but something else such as a .cer or .crt. The key generated by Azure will be usable for creation of a SSH Connection regardless of the extension. 

Once the SSH private key is download , as shown in figure 1-12, the Resources required for your virtual machine will be created

![EditorImages/2022/03/28 22:01/Figure_1-12_Download_SSH_Private_Key.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/28%2022%3A01/Figure_1-12_Download_SSH_Private_Key.png)

Figure 1-12: Download SSH Key

---

By default our Virtual Machine Doesn't come with an Identity, which means that it wont be able to access other Azure Resources in the Resource Group. Before we move on to connecting to our Virtual Machine using SSH, lets give our Virtual Machine an identity.

When your Virtual Machine deployment is complete, select the drop down arrow to the left of the words **Deployment details**. Now you should see a list of resource, select your virtual machine. Figure 1-13 highlights the drop down arrow and your Virtual Machine in the Resource list.

![EditorImages/2022/04/08 00:43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png)

Figure 1-13: Find you Virtual Machine in Drop Down list

Now in the search bar under the name of your Virtual Machine, type identity. Then click on Identity, as shown in figure 1-14

![EditorImages/2022/04/08 00:49/Figure_1-14_search_for_and_click_Identitty.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A49/Figure_1-14_search_for_and_click_Identitty.png)

Figure 1-14: Search for identity, then click Identity

What we are going to do is turn **on** System Assigned Managed Identity. On the Identity page, set status to **On**, then click **Save**. Figure 1-15 show the Status switch which must be turned on, and the save button that must be clicked for status to be changed.

![EditorImages/2022/04/08 01:03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png)

Figure 1-15: Set status switch to **On**, then click Save

There will be one more prompt, asking if you would like to Enable System Assigned Managed Identity, click Yes as shown in figure 1-16

![EditorImages/2022/04/08 01:06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png)

Figure 1-16 Click **Yes** Enabling system assigned Identity

# 2. Connect to Virtual Machine using SSH

In figure 1-11 we downloaded a private key that we will use to connect to out Virtual Machine using SSH.

!!! Alert
    Azure doesn't always output a .PEM file when it Generate SSH key pair. Do not be alarmed if you receive a .cer or a .crt file.
    
When we create the Virtual Machine we created an Administrative user named **azureuser**.
Figure 2-1 is a snippet of figure 1-4 where we can find the name of our user.

![EditorImages/2022/04/08 01:34/Figure_2-1_get_username.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A34/Figure_2-1_get_username.png) 

Now we need to get the Public IP Address to our Virtual Machine. On the Azure Portal Home Page select Virtual Machines as shown in Figure 2-2

![EditorImages/2022/04/08 01:37/Figure_2-2_Click_on_Virtual_machines.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A37/Figure_2-2_Click_on_Virtual_machines.png)

Figure 2-2: Click on Virtual Machines on Azure Portal Home Page

On the Record for the AlgorandOnAzureTutorial-VM, take note of the Public IP address. Figure 2-3 shows where you can find the Public IP Address

![EditorImages/2022/04/08 01:45/Figure_2-3_get_public_ip_address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A45/Figure_2-3_get_public_ip_address.png)

Figure 2-3: take note of the Public IP Address

The following commands assume that you havent move your Private Key out of the Downloads folder.

This SSH Command should work for Mac and Linux. Make sure to change the file extension if it is not .pem, also replace XYZ with your Public IP Address.

```
ssh -i ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem azureuser@XYZ
```

The following SSH command is for Windows 10 & 11 (Windows Powershell). Make sure to change the file extension if it is not .pem, also replace XYZ with your Public IP Address.

```
ssh -i $HOME"\Downloads\AlgorandOnAzureTutorial-VM_key.pem" azureuser@XYZ
```

___


SSH keys are the identity of a single user, so OpenSSH will not allow you to use a key it considers "too open". OpenSSH (Client \ Server) is now integrated into operating systems such as Microsoft Windows, macOS, and most Linux distributions.

Figure 2-4 illustrates the error you will get if your Private key is Accessible to others. The area highlighted in green shows that the private key has Permissions 0644. Permissions 0644 means that the User has read and write permissions, the group associated with the file has read permissions, and All other users have Read Permission

![EditorImages/2022/04/12 03:41/Figure_2-4_Private_Key_Permissions_Error.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2003%3A41/Figure_2-4_Private_Key_Permissions_Error.png) 

Figure 2-4: Private Key permissions are "too open"

The very least the User needs is Read Permissions, while the group associated with the file and everyone else should have no permissions.

Assuming that the Private Key downloaded in Step 1 is still in the Downloads Directory, the following commands should help you change the Permission of your private key. **Please Change File Extension if the Private Key you have is not `.pem` **


For macOS and Linux

```
chmod 600 ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem
```

For Windows 10 (Powershell)

```
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /reset
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /grant:r "$($env:username):(r)"
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /inheritance:r

```


# 3. Install Algorand node

Use the following command to update and upgrade the packages currently installed on Ubuntu

``` 
sudo apt update && sudo apt upgrade 
```
 
Now we can create a Directory for our node and install the update script. If there is no node installed on your on your system, the update script pulls the latest Algorand update package from AWS s3 and install it on your system.

```
mkdir ~/node
cd ~/node
curl https://raw.githubusercontent.com/algorand/go-algorand-doc/master/downloads/installers/update.sh -O

```

![EditorImages/2022/03/03 01:48/Download_updater_script.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/03%2001%3A48/Download_updater_script.png)

After downloading the update script it will only have read, and write permissions. We will have to change the permissions so we can read and execute the script. The following command gives our user read and execute permissions

```
sudo chmod 544 ~/node/update.sh
```

Now we are going to run the script

```
./update.sh -i -c stable -p ~/node -d ~/node/data -n
```

!!! Tip
    -n = no automatic start after download
    
For this tutorial I am going to install a Testnet node, but the default configuration is on the Mainnet, so modifications will have to be made. Configuration files for four different networks are available in the `~/node/genesisfiles` folder.

Lets create a directory for our testnet data, and then copy the Testnet configuration file to that directory

```
mkdir ~/node/testnet_data
cp ~/node/genesisfiles/testnet/genesis.json ~/node/testnet_data/genesis.json
```

We will need to append the `~/node` directory to the `PATH` Environmental Variable, and create an Environmental Variable with the location of our testnet data. The best way to modify, add, or manage Environmental Variable in linux is adding them to `~/.bashrc`. The following commands append the modified `PATH` and the created `ALGORAND_DATA` Environmental Variable to the bottom of the `~/.bashrc` file. The last command reads and executes `~/.bashrc`


```
echo 'export PATH="$HOME/node:$PATH"' >> ~/.bashrc
echo 'export ALGORAND_DATA="$HOME/node/testnet_data"' >> ~/.bashrc
source ~/.bashrc

```

Now you can start your node with the following command



```
goal node start
```

To see the status of your node use the following command

```
goal node status
```

When Sync Time, highlighted in figure 3-1, equals 0.0 your node is fully synced


![EditorImages/2022/03/29 22:38/Figure_3-1_check_the_status_of_your_node.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/29%2022%3A38/Figure_3-1_check_the_status_of_your_node.png)

Figure 3-1: Check node status


Later in this tutorial we will need the Node HTTP Address, and the node Rest API Token. Now that your node is up and running you can now see these values with the following command

```
printf "HTTP ADDRESS = http://$(cat ~/node/testnet_data/algod.net) \nREST API Token = $(cat ~/node/testnet_data/algod.token)\n"
```

Now we can add these values as environmental variables for later use. We will append these new Environmental Variable to the bottom of `~/.bashrc`

```
echo "export ALGORAND_NODE_ADDRESS=\"http://$(cat ~/node/testnet_data/algod.net)\"" >> ~/.bashrc
echo "export ALGORAND_NODE_REST_TOKEN=\"$(cat ~/node/testnet_data/algod.token)\"" >> ~/.bashrc
source ~/.bashrc
```


---

Fast Catchup allow for rapid node updates by using snapshots. If you don't uses this feature then your node could take hours or days to synchronize

The catchup point, for the testnet network, is available at the following address

```
https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint
```

The code for the catchup point should looks like a string of numbers and letters, as shown in figure 3-2

![EditorImages/2022/04/11 16:25/Figure_3-2_get_latest_catchpoint.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2016%3A25/Figure_3-2_get_latest_catchpoint.png)  

Figure 3-2: Testnet catchup point


Enter the following command to use Fast Catchup
```
goal node catchup $(curl https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint)
```



# 4. Create an Azure Key Vault

On the Azure Portal Home Page, Search for Key vaults, then click Key Vaults as Highlighted in Figure 4-1

![EditorImages/2022/04/09 00:22/Figure_4-1_search_and_click_Key_vaults.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-1_search_and_click_Key_vaults.png) 

Figure 4-1: Search for Key vaults then click Key vaults under services

In the center of the Key vaults Page, Click Create key vault, as shown in Figure 4-2

![EditorImages/2022/04/09 00:22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png) 

Figure 4-2: Click Create key vault on the center of the page

Now we are at the Create a key vault page. For the ** Resource group ** select the same group your virtual machine is in. The Region should be the same as you Resource group, and the Key vault name used for this tutorial is:

```
algo-tutorial-secrets
```

Make sure that your configuration looks like Figure 4-3, except for the region if it is different

![EditorImages/2022/04/09 00:23/Figure_4-3_Set_Resource_Group_Region_and_Name.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-3_Set_Resource_Group_Region_and_Name.png) 

Figure 4-3: Set Resource group, region, Key vault name, then click Next: Access policy >

On the Access Policy page, select **Add Access Policy** as highlighted in Figure 4-4

![EditorImages/2022/04/09 00:23/Figure_4-4_Click_on_Add_Access_Policy.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-4_Click_on_Add_Access_Policy.png)  

Figure 4-4: click on Add Access Policy

In the **Configure from template** Drop-Down select Secret Management as shown in Figure 4-5

![EditorImages/2022/04/09 00:23/Figure_4-5_Select_Secret_Management.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-5_Select_Secret_Management.png)  

Figure 4-5: Select Secret Management from Configure from template Drop-Down

Now select **None selected** under Select Principal as highlighted in Figure 4-6

![EditorImages/2022/04/09 00:24/Figure_4-6_select_None_selected_under_Select_Principal.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-6_select_None_selected_under_Select_Principal.png)  

Figure 4-6: select **None selected** under Select Principal

On the right side of the page you will be asked to Select a principal, our principal will be our Virtual Machine. Select our virtual machine, then click Select as illustrated in Figure 4-7

![EditorImages/2022/04/09 00:24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png)  

Figure 4-7: Select Virtual Machine then click Select

Now click add, as highlighted in Figure 4-8

![EditorImages/2022/04/09 00:24/Figure_4-8_Click_Add.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-8_Click_Add.png)  


Figure 4-8: Click add to add Access Policy

On the Create a key vault page, you will now see the Access Policy you just created under Applications. Click on Review + create, as illustrated in Figure 4-9

![EditorImages/2022/04/09 00:24/Figure_4-9_Click_on_Review__create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-9_Click_on_Review__create.png) 

Figure 4-9: Click on Review + create

Now confirm that you configuration is valid then click Create as shown if Figure 4-10

![EditorImages/2022/04/09 00:24/Figure_4-10_Check_Validation_and_click_Create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-10_Check_Validation_and_click_Create.png) 

Figure 4-10: Confirm configuration is valid then click Create

# 5. Create Python Virtual Environment, and clone Tutorial GitHub Repository

In this step, lets create a virtual environment for our pythons code. This environment will hold all the packages we need to run the scripts we will be writing.

First lets download Virtualenv for linux using the following command

```
sudo apt install python3.8-venv
```

Then lets create a directory for our python project, and create a Virtual Environment inside of it

```
mkdir ~/algorand_on_azure_project
cd ~/algorand_on_azure_project
python3 -m venv algorand_on_azure_env
```

Now lets ACTIVATE our Virtual Environment

```
source ~/algorand_on_azure_project/algorand_on_azure_env/bin/activate
```

!!! Alert
    If you have successfully activated you Virtual Environment, you will see the name of your Virtual Environment appended to the beginning of your command line
    
    ![EditorImages/2022/03/31 21:14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/31%2021%3A14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png) 


Now that the Virtual Environment is Activated, lets add all the python packages we will need for this tutorial

```
pip3 install py-algorand-sdk azure-identity azure-keyvault-secrets python-dotenv
```

Last we will clone this tutorials GitHub repository into your `algorand_on_azure_project` Directory with the following command

```
git clone https://github.com/pmartinez8241/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault.git
```

# 6. Create Algorand accounts

For this tutorial we will be creating 2 accounts, one account that will send ALGO, and another account that will receive ALGO. Inside the git hub repository you download is a file called `create_algorand_account.py`, run the following command to create both accounts

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_account.py
```

So now in the `.env` file, that is in your `~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/` directory, you will see 2 Environmental Variable `ALGORAND_SENDER_ACCOUNT_ADDRESS`, and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS`


azure_keyvault_helpers.py

```
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient


credentials = ManagedIdentityCredential()
secret_client = SecretClient(r'https://algo-tutorial-secrets.vault.azure.net/',credentials)




def set_keyvault_secret(secret_name, secret_value):
    result = secret_client.set_secret(secret_name,secret_value)
    created_secret = "Secret created\nName = {}\nDate Create = {}".format(result.name,result.properties.created_on)
    print(created_secret)




def get_keyvault_secret(secret_name):
    result = secret_client.get_secret(secret_name)
    return result.value
```

In step one, we enable `System Managed Identity` which is used to Authenticate our Secret client. When we created an Azure keyvault we added an Access Policy that allows our Virtual Machine to access it. So `ManagedIdentityCredential()` retrieves the Managed Identity Credentials of our Virtual Machine then, we input them into our Secret Client for Authentication. The Secret Client is a Python Library used to manage Azure KeyVault. Setting secrets only requires a name for your secret, and the value of your secret, in order to create it. To get a secret all that is required is the name of your secret.


create_algorand_account.py

```
from algosdk import account, mnemonic
import azure_keyvault_helpers as azure_kv
import os




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
```

The `algosdk` has a function that generates an account for you, consisting of a `Private Key` and an `Address`. If you need to create a `mnemonic` for your account, there is a mnemonic class that requires only the private key of your account in order to generate one. In the code above we save the `private key` and the `mnemonic` to Azure Keyvault, when we want to get the private key we will use the the account address with a `-PK` appended to the end. You can get the mnemonic key by appending a `-MNEMONIC' to the end of your account address.


The `create_algorand_account.py` file creates two environment variable `ALGORAND_SENDER_ACCOUNT_ADDRESS` and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS`, both of which hold the Account Address of an Algorand Account. Both of the environmental variables are stored in the `.env` file, which will be located in the same directory as the `create_algorand_account.py` python script.

# 7. Use Algorand Dispenser to fill account with ALGO

For this step we will fill the `SENDER` account with 20 ALGO. In order to fill the Account with ALGO we will need the Account Address, which is located in the directory of the GitHub repository we downloaded, run the following command from inside that directory

```
grep "ALGORAND_SENDER" .env | cut -d "=" -f2 |  sed 's/"//g'
```

The output from the command above is shown in figure 7-1.

![EditorImages/2022/04/11 20:27/Figure_7-1_Get_Sender_Account_Address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2020%3A27/Figure_7-1_Get_Sender_Account_Address.png) 

Figure 7-1: Account Address for the send account

The Address that was output from Figure 7-1 needs to be copied and pasted into the Algorand dispenser. The Algorand dispenser outputs Algo that is usable only in the `Test Network`. Once copy the Account Address, go to the following website

```
https://bank.testnet.algorand.network/
```

Once at the site above, verify that your are not a robot, then paste you Account Address into the Text Field, and last click dispense. Once you click dispense, you should see `Status: Code 200 success` as illustrated in figure 7-2.

![EditorImages/2022/04/11 20:43/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2020%3A43/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png)

Figure 7-2: Verify not a robot, paste account address, click dispense

Each time you put your address into the Algorand Dispenser you will get 10 algo. Refresh your browser after each use. You will need to use the Algorand Dispenser twice to get the 20 Algo you will need for this tutorial.

# 8. Create and Sign an Algorand Transaction

Now we have all of the variables we will need to create a transaction and sign it. Run the following command to have the signed transaction broadcast through out the Test Network

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_transaction.py
```

The command above outputs a `Transaction ID`, as shown in Figure 8-1.

![EditorImages/2022/04/12 18:05/Figure_8-1_Transaction_ID.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2018%3A05/Figure_8-1_Transaction_ID.png)



---



```
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
params.fee = constants.MIN_TXN_FEE

note = "Algorand on Azure Tutorial Transaction".encode()
amount = 10000000


# PREPARE THE TRANSACTION FOR SIGNING
unsigned_txn = transaction.PaymentTxn(algorand_sender_account_address, params, algorand_receiver_account, amount, None, note)

# NOW WE CAN SIGN THE TRANSACTION WITH OUR PRIVATE KEY

signed_txn = unsigned_txn.sign(algorand_account_private_key)

# LAST WE WILL SEND OUR TRANSACTION AND PRINT THE TRANSACTION NUMBER

transaction_id = algod_client.send_transaction(signed_txn)

print(transaction_id)
```
Figure 1-3: Enter Virtual machine name

!!! Tip
    In this tutorial we will be using image: Ubuntu Server 20.04 LTS - Gen2
* To meet the requirements of 2-4 vCPU, 4-8GB RAM we will be using:
&nbsp;&nbsp;- VM Size: Standard_D2s_v3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + 2 VCPUs
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + 8GB ram

!!! Tip
    Select a Region closest to your location.
    To find a location that is closet to you [Click Here](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies)

Currently you should have the same configurations selected as in Figure 1-4, Except for the region which depends on your location. After making sure you configurations look like those of Figure 1-4, click Next : Disks >

![EditorImages/2022/03/26 23:29/Figure_1-4_Virtual_Machine_Configuration.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A29/Figure_1-4_Virtual_Machine_Configuration.png) 

Figure 1-4: Verify your Configuration

!!! Tip
    Azure Virtual Machines come with very little storage so, we are going to have to add a disk
Click on ** Create and attach a new Disk ** as shown in Figure 1-5
![EditorImages/2022/03/26 23:38/Figure_1-5_Create_and_attach_a_new_disk.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A38/Figure_1-5_Create_and_attach_a_new_disk.png) 

Figure 1-5: Select **Create and attach a new Disk**

Click on **Change Size** as shown in Figure 1-6

![EditorImages/2022/03/26 23:43/Figure_1-6_Change_Size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A43/Figure_1-6_Change_Size.png) 

Figure 1-6: Select **Change Size**

To meet the minimum storage requirements dictated by the Algorand Foundation we will create a **256GB Standard SSD**. Once your drive selection looks like Figure 1-7, **click OK**

![EditorImages/2022/03/26 23:56/Figure_1-7_Select_a_disk_size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A56/Figure_1-7_Select_a_disk_size.png) 

Figure 1-7: Create 256GB Standard SSD

**Click OK** once more on the Create a new disk page, shown in Figure 1-8.

![EditorImages/2022/03/27 00:05/Figure_1-8_Disk_Selection_Conclusion.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A05/Figure_1-8_Disk_Selection_Conclusion.png) 

Figure 1-8: Create a new disk page, click OK

!!! Tip
    This is just a basic tutorial, so Networking, Management, advanced, and tags will be left with their default settings
    
From Disks we are going to head straight to ** Review + create **, as highlighted in Figure 1-9

![EditorImages/2022/03/27 00:12/Figure_1-9_Review.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A12/Figure_1-9_Review.png) 

Figure 1-9: Click on Review + create, to review the Virtual Machines final configuration

On the Create a virtual machine page, Check the top of the page to see if you configuration is valid, then select **Create**. Figure 1-10 highlights a configuration that passes validation.

![EditorImages/2022/03/27 01:54/Figure_1-10_Create_the_VM.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2001%3A54/Figure_1-10_Create_the_VM.png)

Figure 1-10: Validate configuration then press Create

Once you click **Create** you are given the option to Download the Key Pair for SSH click ** Download private key and create resource ** as shown in figure 1-11

![EditorImages/2022/03/27 03:04/Figure_1-11_Download_key_pair.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2003%3A04/Figure_1-11_Download_key_pair.png) 

Figure 1-11: Download Private Key and Create Resources


!!! Alert
    When having Azure generate a key pair you may not get a .PEM file, but something else such as a .cer or .crt. The key generated by Azure will be usable for creation of a SSH Connection regardless of the extension. 

Once the SSH private key is download , as shown in figure 1-12, the Resources required for your virtual machine will be created

![EditorImages/2022/03/28 22:01/Figure_1-12_Download_SSH_Private_Key.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/28%2022%3A01/Figure_1-12_Download_SSH_Private_Key.png)

Figure 1-12: Download SSH Key

---

By default our Virtual Machine Doesn't come with an Identity, which means that it wont be able to access other Azure Resources in the Resource Group. Before we move on to connecting to our Virtual Machine using SSH, lets give our Virtual Machine an identity.

When your Virtual Machine deployment is complete, select the drop down arrow to the left of the words **Deployment details**. Now you should see a list of resource, select your virtual machine. Figure 1-13 highlights the drop down arrow and your Virtual Machine in the Resource list.

![EditorImages/2022/04/08 00:43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png)

Figure 1-13: Find you Virtual Machine in Drop Down list

Now in the search bar under the name of your Virtual Machine, type identity. Then click on Identity, as shown in figure 1-14

![EditorImages/2022/04/08 00:49/Figure_1-14_search_for_and_click_Identitty.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A49/Figure_1-14_search_for_and_click_Identitty.png)

Figure 1-14: Search for identity, then click Identity

What we are going to do is turn **on** System Assigned Managed Identity. On the Identity page, set status to **On**, then click **Save**. Figure 1-15 show the Status switch which must be turned on, and the save button that must be clicked for status to be changed.

![EditorImages/2022/04/08 01:03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png)

Figure 1-15: Set status switch to **On**, then click Save

There will be one more prompt, asking if you would like to Enable System Assigned Managed Identity, click Yes as shown in figure 1-16

![EditorImages/2022/04/08 01:06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png)

Figure 1-16 Click **Yes** Enabling system assigned Identity

# 2. Connect to Virtual Machine using SSH

In figure 1-11 we downloaded a private key that we will use to connect to out Virtual Machine using SSH.

!!! Alert
    Azure doesn't always output a .PEM file when it Generate SSH key pair. Do not be alarmed if you receive a .cer or a .crt file.
    
When we create the Virtual Machine we created an Administrative user named **azureuser**.
Figure 2-1 is a snippet of figure 1-4 where we can find the name of our user.

![EditorImages/2022/04/08 01:34/Figure_2-1_get_username.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A34/Figure_2-1_get_username.png) 

Now we need to get the Public IP Address to our Virtual Machine. On the Azure Portal Home Page select Virtual Machines as shown in Figure 2-2

![EditorImages/2022/04/08 01:37/Figure_2-2_Click_on_Virtual_machines.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A37/Figure_2-2_Click_on_Virtual_machines.png)

Figure 2-2: Click on Virtual Machines on Azure Portal Home Page

On the Record for the AlgorandOnAzureTutorial-VM, take note of the Public IP address. Figure 2-3 shows where you can find the Public IP Address

![EditorImages/2022/04/08 01:45/Figure_2-3_get_public_ip_address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A45/Figure_2-3_get_public_ip_address.png)

Figure 2-3: take note of the Public IP Address

The following commands assume that you havent move your Private Key out of the Downloads folder.

This SSH Command should work for Mac and Linux. Make sure to change the file extension if it is not .pem, also replace XYZ with your Public IP Address.

```
ssh -i ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem azureuser@XYZ
```

The following SSH command is for Windows 10 & 11 (Windows Powershell). Make sure to change the file extension if it is not .pem, also replace XYZ with your Public IP Address.

```
ssh -i $HOME"\Downloads\AlgorandOnAzureTutorial-VM_key.pem" azureuser@XYZ
```

___


SSH keys are the identity of a single user, so OpenSSH will not allow you to use a key it considers "too open". OpenSSH (Client \ Server) is now integrated into operating systems such as Microsoft Windows, macOS, and most Linux distributions.

Figure 2-4 illustrates the error you will get if your Private key is Accessible to others. The area highlighted in green shows that the private key has Permissions 0644. Permissions 0644 means that the User has read and write permissions, the group associated with the file has read permissions, and All other users have Read Permission

![EditorImages/2022/04/12 03:41/Figure_2-4_Private_Key_Permissions_Error.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2003%3A41/Figure_2-4_Private_Key_Permissions_Error.png) 

Figure 2-4: Private Key permissions are "too open"

The very least the User needs is Read Permissions, while the group associated with the file and everyone else should have no permissions.

Assuming that the Private Key downloaded in Step 1 is still in the Downloads Directory, the following commands should help you change the Permission of your private key. **Please Change File Extension if the Private Key you have is not `.pem` **


For macOS and Linux

```
chmod 600 ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem
```

For Windows 10 (Powershell)

```
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /reset
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /grant:r "$($env:username):(r)"
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /inheritance:r

```


# 3. Install Algorand node

Use the following command to update and upgrade the packages currently installed on Ubuntu

``` 
sudo apt update && sudo apt upgrade 
```
 
Now we can create a Directory for our node and install the update script. If there is no node installed on your on your system, the update script pulls the latest Algorand update package from AWS s3 and install it on your system.

```
mkdir ~/node
cd ~/node
curl https://raw.githubusercontent.com/algorand/go-algorand-doc/master/downloads/installers/update.sh -O

```

![EditorImages/2022/03/03 01:48/Download_updater_script.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/03%2001%3A48/Download_updater_script.png)

After downloading the update script it will only have read, and write permissions. We will have to change the permissions so we can read and execute the script. The following command gives our user read and execute permissions

```
sudo chmod 544 ~/node/update.sh
```

Now we are going to run the script

```
./update.sh -i -c stable -p ~/node -d ~/node/data -n
```

!!! Tip
    -n = no automatic start after download
    
For this tutorial I am going to install a Testnet node, but the default configuration is on the Mainnet, so modifications will have to be made. Configuration files for four different networks are available in the `~/node/genesisfiles` folder.

Lets create a directory for our testnet data, and then copy the Testnet configuration file to that directory

```
mkdir ~/node/testnet_data
cp ~/node/genesisfiles/testnet/genesis.json ~/node/testnet_data/genesis.json
```

We will need to append the `~/node` directory to the `PATH` Environmental Variable, and create an Environmental Variable with the location of our testnet data. The best way to modify, add, or manage Environmental Variable in linux is adding them to `~/.bashrc`. The following commands append the modified `PATH` and the created `ALGORAND_DATA` Environmental Variable to the bottom of the `~/.bashrc` file. The last command reads and executes `~/.bashrc`


```
echo 'export PATH="$HOME/node:$PATH"' >> ~/.bashrc
echo 'export ALGORAND_DATA="$HOME/node/testnet_data"' >> ~/.bashrc
source ~/.bashrc

```

Now you can start your node with the following command



```
goal node start
```

To see the status of your node use the following command

```
goal node status
```

When Sync Time, highlighted in figure 3-1, equals 0.0 your node is fully synced


![EditorImages/2022/03/29 22:38/Figure_3-1_check_the_status_of_your_node.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/29%2022%3A38/Figure_3-1_check_the_status_of_your_node.png)

Figure 3-1: Check node status


Later in this tutorial we will need the Node HTTP Address, and the node Rest API Token. Now that your node is up and running you can now see these values with the following command

```
printf "HTTP ADDRESS = http://$(cat ~/node/testnet_data/algod.net) \nREST API Token = $(cat ~/node/testnet_data/algod.token)\n"
```

Now we can add these values as environmental variables for later use. We will append these new Environmental Variable to the bottom of `~/.bashrc`

```
echo "export ALGORAND_NODE_ADDRESS=\"http://$(cat ~/node/testnet_data/algod.net)\"" >> ~/.bashrc
echo "export ALGORAND_NODE_REST_TOKEN=\"$(cat ~/node/testnet_data/algod.token)\"" >> ~/.bashrc
source ~/.bashrc
```


---

Fast Catchup allow for rapid node updates by using snapshots. If you don't uses this feature then your node could take hours or days to synchronize

The catchup point, for the testnet network, is available at the following address

```
https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint
```

The code for the catchup point should looks like a string of numbers and letters, as shown in figure 3-2

![EditorImages/2022/04/11 16:25/Figure_3-2_get_latest_catchpoint.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2016%3A25/Figure_3-2_get_latest_catchpoint.png)  

Figure 3-2: Testnet catchup point


Enter the following command to use Fast Catchup
```
goal node catchup $(curl https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint)
```



# 4. Create an Azure Key Vault

On the Azure Portal Home Page, Search for Key vaults, then click Key Vaults as Highlighted in Figure 4-1

![EditorImages/2022/04/09 00:22/Figure_4-1_search_and_click_Key_vaults.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-1_search_and_click_Key_vaults.png) 

Figure 4-1: Search for Key vaults then click Key vaults under services

In the center of the Key vaults Page, Click Create key vault, as shown in Figure 4-2

![EditorImages/2022/04/09 00:22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png) 

Figure 4-2: Click Create key vault on the center of the page

Now we are at the Create a key vault page. For the ** Resource group ** select the same group your virtual machine is in. The Region should be the same as you Resource group, and the Key vault name used for this tutorial is:

```
algo-tutorial-secrets
```

Make sure that your configuration looks like Figure 4-3, except for the region if it is different

![EditorImages/2022/04/09 00:23/Figure_4-3_Set_Resource_Group_Region_and_Name.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-3_Set_Resource_Group_Region_and_Name.png) 

Figure 4-3: Set Resource group, region, Key vault name, then click Next: Access policy >

On the Access Policy page, select **Add Access Policy** as highlighted in Figure 4-4

![EditorImages/2022/04/09 00:23/Figure_4-4_Click_on_Add_Access_Policy.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-4_Click_on_Add_Access_Policy.png)  

Figure 4-4: click on Add Access Policy

In the **Configure from template** Drop-Down select Secret Management as shown in Figure 4-5

![EditorImages/2022/04/09 00:23/Figure_4-5_Select_Secret_Management.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-5_Select_Secret_Management.png)  

Figure 4-5: Select Secret Management from Configure from template Drop-Down

Now select **None selected** under Select Principal as highlighted in Figure 4-6

![EditorImages/2022/04/09 00:24/Figure_4-6_select_None_selected_under_Select_Principal.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-6_select_None_selected_under_Select_Principal.png)  

Figure 4-6: select **None selected** under Select Principal

On the right side of the page you will be asked to Select a principal, our principal will be our Virtual Machine. Select our virtual machine, then click Select as illustrated in Figure 4-7

![EditorImages/2022/04/09 00:24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png)  

Figure 4-7: Select Virtual Machine then click Select

Now click add, as highlighted in Figure 4-8

![EditorImages/2022/04/09 00:24/Figure_4-8_Click_Add.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-8_Click_Add.png)  


Figure 4-8: Click add to add Access Policy

On the Create a key vault page, you will now see the Access Policy you just created under Applications. Click on Review + create, as illustrated in Figure 4-9

![EditorImages/2022/04/09 00:24/Figure_4-9_Click_on_Review__create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-9_Click_on_Review__create.png) 

Figure 4-9: Click on Review + create

Now confirm that you configuration is valid then click Create as shown if Figure 4-10

![EditorImages/2022/04/09 00:24/Figure_4-10_Check_Validation_and_click_Create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-10_Check_Validation_and_click_Create.png) 

Figure 4-10: Confirm configuration is valid then click Create

# 5. Create Python Virtual Environment, and clone Tutorial GitHub Repository

In this step, lets create a virtual environment for our pythons code. This environment will hold all the packages we need to run the scripts we will be writing.

First lets download Virtualenv for linux using the following command

```
sudo apt install python3.8-venv
```

Then lets create a directory for our python project, and create a Virtual Environment inside of it

```
mkdir ~/algorand_on_azure_project
cd ~/algorand_on_azure_project
python3 -m venv algorand_on_azure_env
```

Now lets ACTIVATE our Virtual Environment

```
source ~/algorand_on_azure_project/algorand_on_azure_env/bin/activate
```

!!! Alert
    If you have successfully activated you Virtual Environment, you will see the name of your Virtual Environment appended to the beginning of your command line
    
    ![EditorImages/2022/03/31 21:14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/31%2021%3A14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png) 


Now that the Virtual Environment is Activated, lets add all the python packages we will need for this tutorial

```
pip3 install py-algorand-sdk azure-identity azure-keyvault-secrets python-dotenv
```

Last we will clone this tutorials GitHub repository into your `algorand_on_azure_project` Directory with the following command

```
git clone https://github.com/pmartinez8241/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault.git
```

# 6. Create Algorand accounts

For this tutorial we will be creating 2 accounts, one account that will send ALGO, and another account that will receive ALGO. Inside the git hub repository you download is a file called `create_algorand_account.py`, run the following command to create both accounts

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_account.py
```

So now in the `.env` file, that is in your `~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/` directory, you will see 2 Environmental Variable `ALGORAND_SENDER_ACCOUNT_ADDRESS`, and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS`


azure_keyvault_helpers.py

```
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient


credentials = ManagedIdentityCredential()
secret_client = SecretClient(r'https://algo-tutorial-secrets.vault.azure.net/',credentials)




def set_keyvault_secret(secret_name, secret_value):
    result = secret_client.set_secret(secret_name,secret_value)
    created_secret = "Secret created\nName = {}\nDate Create = {}".format(result.name,result.properties.created_on)
    print(created_secret)




def get_keyvault_secret(secret_name):
    result = secret_client.get_secret(secret_name)
    return result.value
```

In step one, we enable `System Managed Identity` which is used to Authenticate our Secret client. When we created an Azure keyvault we added an Access Policy that allows our Virtual Machine to access it. So `ManagedIdentityCredential()` retrieves the Managed Identity Credentials of our Virtual Machine then, we input them into our Secret Client for Authentication. The Secret Client is a Python Library used to manage Azure KeyVault. Setting secrets only requires a name for your secret, and the value of your secret, in order to create it. To get a secret all that is required is the name of your secret.


create_algorand_account.py

```
from algosdk import account, mnemonic
import azure_keyvault_helpers as azure_kv
import os




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
```

The `algosdk` has a function that generates an account for you, consisting of a `Private Key` and an `Address`. If you need to create a `mnemonic` for your account, there is a mnemonic class that requires only the private key of your account in order to generate one. In the code above we save the `private key` and the `mnemonic` to Azure Keyvault, when we want to get the private key we will use the the account address with a `-PK` appended to the end. You can get the mnemonic key by appending a `-MNEMONIC' to the end of your account address.


The `create_algorand_account.py` file creates two environment variable `ALGORAND_SENDER_ACCOUNT_ADDRESS` and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS`, both of which hold the Account Address of an Algorand Account. Both of the environmental variables are stored in the `.env` file, which will be located in the same directory as the `create_algorand_account.py` python script.

# 7. Use Algorand Dispenser to fill account with ALGO

For this step we will fill the `SENDER` account with 20 ALGO. In order to fill the Account with ALGO we will need the Account Address, which is located in the directory of the GitHub repository we downloaded, run the following command from inside that directory

```
grep "ALGORAND_SENDER" .env | cut -d "=" -f2 |  sed 's/"//g'
```

The output from the command above is shown in figure 7-1.

![EditorImages/2022/04/11 20:27/Figure_7-1_Get_Sender_Account_Address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2020%3A27/Figure_7-1_Get_Sender_Account_Address.png) 

Figure 7-1: Account Address for the send account

The Address that was output from Figure 7-1 needs to be copied and pasted into the Algorand dispenser. The Algorand dispenser outputs Algo that is usable only in the `Test Network`. Once copy the Account Address, go to the following website

```
https://bank.testnet.algorand.network/
```

Once at the site above, verify that your are not a robot, then paste you Account Address into the Text Field, and last click dispense. Once you click dispense, you should see `Status: Code 200 success` as illustrated in figure 7-2.

![EditorImages/2022/04/11 20:43/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2020%3A43/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png)

Figure 7-2: Verify not a robot, paste account address, click dispense

Each time you put your address into the Algorand Dispenser you will get 10 algo. Refresh your browser after each use. You will need to use the Algorand Dispenser twice to get the 20 Algo you will need for this tutorial.

# 8. Create and Sign an Algorand Transaction

Now we have all of the variables we will need to create a transaction and sign it. Run the following command to have the signed transaction broadcast through out the Test Network

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_transaction.py
```

The command above outputs a `Transaction ID`, as shown in Figure 8-1.

![EditorImages/2022/04/12 18:05/Figure_8-1_Transaction_ID.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2018%3A05/Figure_8-1_Transaction_ID.png)



---



```
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
params.fee = constants.MIN_TXN_FEE

note = "Algorand on Azure Tutorial Transaction".encode()
amount = 10000000


# PREPARE THE TRANSACTION FOR SIGNING
unsigned_txn = transaction.PaymentTxn(algorand_sender_account_address, params, algorand_receiver_account, amount, None, note)

# NOW WE CAN SIGN THE TRANSACTION WITH OUR PRIVATE KEY

signed_txn = unsigned_txn.sign(algorand_account_private_key)

# LAST WE WILL SEND OUR TRANSACTION AND PRINT THE TRANSACTION NUMBER

transaction_id = algod_client.send_transaction(signed_txn)

print(transaction_id)
```