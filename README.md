# Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault
Tutorial on how to create an Algorand node on a Azure Virtual Machine, as well as Storing Secrets in Azure 

# Requirements

- Azure Pay-As-You-Go subscription, or better
- Selection of Azure VM with at least the [minimum node system requirements](https://algorand.foundation/algorand-protocol/network) specified by the Algorand Foundation
&nbsp;&nbsp; - 2-4 vCPU
&nbsp;&nbsp; - 4-8GB RAM
&nbsp;&nbsp; - 100 - 200GB SSD
&nbsp;&nbsp; - 100 Mbps broadband

# Background

To achieve high availability and fault tolerance, running your Algorand node on Microsoft Azure is one of your best options. Azure makes it easy to configure a virtual machine with specifications that won’t burn through your money. For this tutorial, we will deploy a virtual machine that meets the minimum system requirements of an Algorand node.


We will also be configuring Azure Key Vault to hold our Private Key used for signing Algorand transactions. All python code will be available at this [GitHub](https://github.com/pmartinez8241/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault)

# Steps

</br>
</br>

## Optional - Use an Azure Arm Template to deploy all resources needed for this tutorial

In steps one and four of this tutorial, we'll create two resources, a Linux virtual machine and an azure KeyVault. Everything, including the permissions needed for the Virtual Machine to access Azure Keyvault, can be made using an Azure arm template. ARM stands for Azure Resource Manager, and it enables you to create, update, and delete resources in your Azure account.

If you would like to create all the resources required for this tutorial using the Azure Portal, skip this section and start at Step One, otherwise after clicking `Deploy to Azure` prepare to do the following:

- For Resource Group, Click Create New and use this Name
```
AlgorandOnAzureTutorial-VM_group
```
- For `Key pair name`, use the following name
```
AlgorandOnAzureTutorial-VM_key
```

- Last, make sure that the Region is correct, if not select the proper region from the dropdown field

Figure 0-1 highlights the fields that need modifying, and what your `Custom Deployment` page should look like


<div align="center">

![EditorImages/2022/04/18 00:56/Figure_0-1_Important_fields.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/18%2000%3A56/Figure_0-1_Important_fields.png) 
</div>

<table>
	<tr>
		<th>
Figure 0-1: modify the highlighted fields
		</th>
	</tr>
</table>

On the `Review + create` page check to see the Template Passes Validation then click `create`, as shown in Figure 0-2


<div align="center">

![EditorImages/2022/04/18 01:06/Figure_0-2_validation.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/18%2001%3A06/Figure_0-2_validation.png) 
</div>

<table>
	<tr>
		<th>
Figure 0-2: Check if template is valid then click `create`
		</th>
	</tr>
</table>


Finally, download your private key as shown in figure 0-3


<div align="center">

![EditorImages/2022/04/18 01:19/Figure_0-3_Download_ssh_key_pair.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/18%2001%3A19/Figure_0-3_Download_ssh_key_pair.png)
</div>

<table>
	<tr>
		<th>
Figure 0-3: Download private key
		</th>
	</tr>
</table>

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
            Right-click on `Deploy to Azure` and open in `New Tab` or `New Window`; if you don't, you will be redirected off this tutorial to the `Custom Deployment` azure page.
		</td>
	</tr>
</table>

    

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fpmartinez8241%2FCreate-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault%2Fmain%2Fazure-algorand-template%2Fazurealgodeploy.json)

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
            If you did not run into any problems with your Deployment, then you can skip `Step one` and `Step four`.
		</td>
	</tr>
</table>
    

</br>
</br>


## 1. Create A Virtual Machine

Search for Virtual machines on the Azure Portal Home page, then Select Virtual machines under Services as shown in **Figure 1-1**.

<div align="center">

![EditorImages/2022/03/26 22:44/Figure_1-1_Search_for_and_Select_Virtual_machines.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2022%3A44/Figure_1-1_Search_for_and_Select_Virtual_machines.png) 
</div>

<table>
	<tr>
		<th>
 Figure 1-1: Search for and Select Virtual machines 
		</th>
	</tr>
</table>


On the Virtual machines page, select **Create** followed by **Azure virtual machine** as shown in ***_Figure 1-2_***.

<div align="center">

![EditorImages/2022/03/26 22:54/Figure_1-2_Under_Create_select_Azure_Virtual_Machine.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2022%3A54/Figure_1-2_Under_Create_select_Azure_Virtual_Machine.png)
</div>

<table>
	<tr>
		<th>
Figure 1-2: Select **Create** then **Azure virtual machine** 
		</th>
	</tr>
</table>



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
            It is easiest to work with many different resources when they all have a common naming convention.
		</td>
	</tr>
</table>

For this tutorial, let's name our Virtual Machine AlgorandOnAzureTutorial-VM, as shown in Figure 1-3.

```
AlgorandOnAzureTutorial-VM
```

<div align="center">

![EditorImages/2022/03/26 23:12/Figure_1-3_Set_Virtual_Machine_Name.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A12/Figure_1-3_Set_Virtual_Machine_Name.png)
</div>

<table>
	<tr>
		<th>
Figure 1-3: Enter Virtual machine name 
		</th>
	</tr>
</table>

In this tutorial we will be using image: Ubuntu Server 20.04 LTS - Gen2 To meet the requirements of 2-4 vCPU, 4-8GB RAM we will be using VM Size: Standard_D2s_v3, 2 VCPUs and 8GB ram


    
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
                <p align="center">Select a Region closest to your location.</br>To find a location that is closest to you</p>
<div align="center">

[Click Here](https://azure.microsoft.com/en-us/global-infrastructure/geographies/#geographies)
</div>
            </td>
    </tr>
</table>




Currently, you should have the same configurations selected as in Figure 1-4, Except for the region, which depends on your location. Select a Region closest to your location. After making sure you configurations look like those of Figure 1-4, click Next : Disks >.

<div align="center">

![EditorImages/2022/03/26 23:29/Figure_1-4_Virtual_Machine_Configuration.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A29/Figure_1-4_Virtual_Machine_Configuration.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-4: Verify your Configuration
		</th>
	</tr>
</table>

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
Azure Virtual Machines come with very little storage, so we are going to have to add a disk
		</td>
	</tr>
</table>

Click on  ***Create and attach a new Disk*** as shown in Figure 1-5.

<div align="center">

![EditorImages/2022/03/26 23:38/Figure_1-5_Create_and_attach_a_new_disk.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A38/Figure_1-5_Create_and_attach_a_new_disk.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-5: Select Create and attach a new Disk
		</th>
	</tr>
</table>

Click on **Change Size** as shown in Figure 1-6.

<div align="center">

![EditorImages/2022/03/26 23:43/Figure_1-6_Change_Size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A43/Figure_1-6_Change_Size.png) 
</div>

<table>
	<tr>
<th>
Figure 1-6: Select Change Size
</th>
	</tr>
</table>

To meet the minimum storage requirements dictated by the Algorand Foundation, we will create a **256GB Standard SSD**. Once your drive selection looks like Figure 1-7, **click OK**.

<div align="center">

![EditorImages/2022/03/26 23:56/Figure_1-7_Select_a_disk_size.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/26%2023%3A56/Figure_1-7_Select_a_disk_size.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-7: Create 256GB Standard SSD
		</th>
	</tr>
</table>

**Click OK** once more on the Create a new disk page, shown in Figure 1-8.

<div align="center">

![EditorImages/2022/03/27 00:05/Figure_1-8_Disk_Selection_Conclusion.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A05/Figure_1-8_Disk_Selection_Conclusion.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-8: Create a new disk page, click OK
		</th>
	</tr>
</table>



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
            This is just a basic tutorial, so Networking, Management, advanced, and tags will be left with their default settings.
		</td>
	</tr>
</table>
    
From Disks, we will head straight to ** Review + create **, as highlighted in Figure 1-9.

<div align="center">

![EditorImages/2022/03/27 00:12/Figure_1-9_Review.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2000%3A12/Figure_1-9_Review.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-9: Click on Review + create, to review the Virtual Machines final configuration
		</th>
	</tr>
</table>

On the Create a virtual machine page, Check the top of the page to see if you configuration is valid, then select **Create**. Figure 1-10 highlights a configuration that passes validation.

<div align="center">

![EditorImages/2022/03/27 01:54/Figure_1-10_Create_the_VM.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2001%3A54/Figure_1-10_Create_the_VM.png)
</div>

<table>
	<tr>
		<th>
Figure 1-10: Validate configuration then press Create
		</th>
	</tr>
</table>

Once you click **Create**, you are given the option to Download the Key Pair for SSH click ** Download private key and create resource ** as shown in figure 1-11.

<div align="center">

![EditorImages/2022/03/27 03:04/Figure_1-11_Download_key_pair.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/27%2003%3A04/Figure_1-11_Download_key_pair.png) 
</div>

<table>
	<tr>
		<th>
Figure 1-11: Download Private Key and Create Resources
		</th>
	</tr>
</table>


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
    When Azure generates a key pair, you may not get a .PEM file, but something else such as a .cer or .crt. The key generated by Azure will be usable for the creation of an SSH Connection regardless of the extension.
		</td>
	</tr>
</table>

Once the SSH private key is downloaded, as shown in figure 1-12, the creation of the Resources required for your virtual machine should be nearly complete.

<div align="center">

![EditorImages/2022/03/28 22:01/Figure_1-12_Download_SSH_Private_Key.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/28%2022%3A01/Figure_1-12_Download_SSH_Private_Key.png)
</div>

<table>
	<tr>
		<th>
Figure 1-12: Download SSH Key
		</th>
	</tr>
</table>

---

## Create an Identity for your Virtual Machine

By default, our Virtual Machine Doesn't come with an Identity, which means that it won't be able to access other Azure Resources in the Resource Group. Before we connect to our Virtual Machine using SSH, let's give our Virtual Machine an identity.

When your Virtual Machine deployment is complete, select the drop-down arrow to the left of the words **Deployment details**. Now you should see a list of resources; choose your virtual machine. Figure 1-13 highlights the drop-down arrow and your Virtual Machine in the Resource List.

<div align="center">

![EditorImages/2022/04/08 00:43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A43/Figure_1-13_select_your_virtual_machine_in_dropdown_list.png)
</div>

<table>
	<tr>
		<th>
Figure 1-13: Find you Virtual Machine in Drop Down list
		</th>
	</tr>
</table>

Now in the search bar under the name of your Virtual Machine, type identity. Then click on Identity, as shown in figure 1-14.

<div align="center">

![EditorImages/2022/04/08 00:49/Figure_1-14_search_for_and_click_Identitty.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2000%3A49/Figure_1-14_search_for_and_click_Identitty.png)
</div>

<table>
	<tr>
		<th>
Figure 1-14: Search for identity, then click Identity
		</th>
	</tr>
</table>

We are going to turn **On** System Assigned Managed Identity. Set status to **On**on the Identity page, then click **Save**. Figure 1-15 shows the Status switch, which must be turned on, and the save button must be clicked for the status to be changed.

<div align="center">

![EditorImages/2022/04/08 01:03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A03/Figure_1-15_Set_status_switch_to_On_and_click_Save.png)
</div>

<table>
	<tr>
		<th>
Figure 1-15: Set status switch to **On**, then click Save
		</th>
	</tr>
</table>

There will be one more prompt asking if you would like to Enable System Assigned Managed Identity, click Yes as shown in figure 1-16.

<div align="center">

![EditorImages/2022/04/08 01:06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A06/Figure_1-16_Click_Yes_to_enabling_System_assigned_Managed_Identity.png)
</div>

<table>
	<tr>
		<th>
Figure 1-16 Click **Yes** Enabling system assigned Identity
		</th>
	</tr>
</table>

## 2. Connect to Virtual Machine using SSH

In figure 1-11, we downloaded a private key that we will use to connect to our Virtual Machine using SSH.


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
            Azure doesn't always output a .PEM file when it Generates an SSH key pair. Do not be alarmed if you receive a .cer or a .crt file.
		</td>
	</tr>
</table>
    
When we created the Virtual Machine, we created an Administrative user named **azureuser**.
Figure 2-1 is a snippet of figure 1-4 where we can find the name of our user.

<div align="center">

![EditorImages/2022/04/08 01:34/Figure_2-1_get_username.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A34/Figure_2-1_get_username.png)
</div>

<table>
	<tr>
		<th>
Figure 2-1: Username location
		</th>
	</tr>
</table>

Now we need to get the Public IP Address to our Virtual Machine. On the Azure Portal Home Page select Virtual Machines as shown in Figure 2-2.

<div align="center">

![EditorImages/2022/04/08 01:37/Figure_2-2_Click_on_Virtual_machines.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A37/Figure_2-2_Click_on_Virtual_machines.png)
</div>

<table>
	<tr>
		<th>
Figure 2-2: Click on Virtual Machines on Azure Portal Home Page
		</th>
	</tr>
</table>

On the Record for the AlgorandOnAzureTutorial-VM, take note of the Public IP address. Figure 2-3 shows where you can find the Public IP Address.

<div align="center">

![EditorImages/2022/04/08 01:45/Figure_2-3_get_public_ip_address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/08%2001%3A45/Figure_2-3_get_public_ip_address.png)
</div>

<table>
	<tr>
		<th>
Figure 2-3: take note of the Public IP Address
		</th>
	</tr>
</table>

The following commands assume that you haven't moved your Private Key out of the Downloads folder.

This SSH Command should work for Mac and Linux. Make sure to change the file extension; if it is not .pem, replace XYZ with your Public IP Address.

```
ssh -i ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem azureuser@XYZ
```

The following SSH command is for Windows 10 & 11 (Windows Powershell). Make sure to change the file extension; if it is not .pem, replace XYZ with your Public IP Address.

```
ssh -i $HOME"\Downloads\AlgorandOnAzureTutorial-VM_key.pem" azureuser@XYZ
```

___

## SSH Private Key Permissions

SSH keys are a single user's identity, so OpenSSH will not allow you to use a key it considers "too open." OpenSSH (Client \ Server) is now integrated into operating systems such as Microsoft Windows, macOS, and most Linux distributions.

Figure 2-4 illustrates the error you will get if your Private key is Accessible to others. The area highlighted in green shows that the private key has Permissions 0644. Permissions 0644 means that the User has read and write permissions, the group associated with the file has read permissions, and All other users have Read Permission.

<div align="center">

![EditorImages/2022/04/12 03:41/Figure_2-4_Private_Key_Permissions_Error.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2003%3A41/Figure_2-4_Private_Key_Permissions_Error.png) 
</div>

<table>
	<tr>
		<th>
Figure 2-4: Private Key permissions are "too open"
		</th>
	</tr>
</table>

The very least the User needs is Read Permissions, while the group associated with the file and everyone else should have no permissions.

Assuming that the Private Key downloaded in Step 1 is still in the Downloads directory, the following commands should help you change the Permission of your private key. **Please Change File Extension if the Private Key you have is not `.pem` **.


For macOS and Linux:

```
chmod 600 ~/Downloads/AlgorandOnAzureTutorial-VM_key.pem
```

For Windows 10 (Powershell):

```
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /reset
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /grant:r "$($env:username):(r)"
icacls.exe $HOME\Downloads\AlgorandOnAzureTutorial-VM_key.pem /inheritance:r

```


## 3. Install Algorand node

Use the following command to update and upgrade the currently installed Ubuntu packages.
``` 
sudo apt update && sudo apt upgrade 
```
 
Now we can create a Directory for our node and install the update script. If there is no node installed on your system, the update script pulls the latest Algorand update package from AWS s3 and installs it on your system.
```
mkdir ~/node
cd ~/node
curl https://raw.githubusercontent.com/algorand/go-algorand-doc/master/downloads/installers/update.sh -O

```


After downloading the update script it will only have read, and write permissions. We will have to change the permissions so we can read and execute the script. The following command gives our user read and execute permissions

```
sudo chmod 544 ~/node/update.sh
```

Now we are going to run the script.

```
./update.sh -i -c stable -p ~/node -d ~/node/data -n
```


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
-n = no automatic start after download
		</td>
	</tr>
</table>
    
For this tutorial, I will install a Testnet node, but the default configuration is on the Mainnet, so modifications will have to be made to the data files. Configuration files for four different networks are available in the `~/node/genesisfiles` folder.

Let's create a directory for our testnet data and then copy the Testnet configuration file to that directory

```
mkdir ~/node/testnet_data
cp ~/node/genesisfiles/testnet/genesis.json ~/node/testnet_data/genesis.json
```

We will need to append the `~/node` directory to the `PATH` Environmental Variable and create an Environmental Variable with the location of our testnet data. The best way to modify, add, or manage Environmental Variable in linux is by adding them to `~/.bashrc.` The following commands append the modified `PATH` and the created `ALGORAND_DATA` Environmental Variable to the bottom of the `~/.bashrc` file. The last command reads and executes `~/.bashrc.`


```
echo 'export PATH="$HOME/node:$PATH"' >> ~/.bashrc
echo 'export ALGORAND_DATA="$HOME/node/testnet_data"' >> ~/.bashrc
source ~/.bashrc

```

Now you can start your node with the following command.



```
goal node start
```

To see the status of your node, use the following command.

```
goal node status
```

When Sync Time, highlighted in figure 3-1, equals 0.0, your node is fully synced.

<div align="center">

![EditorImages/2022/03/29 22:38/Figure_3-1_check_the_status_of_your_node.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/29%2022%3A38/Figure_3-1_check_the_status_of_your_node.png)
</div>

<table>
	<tr>
		<th>
Figure 3-1: Check node status
		</th>
	</tr>
</table>


Later in this tutorial, we will need the Node HTTP Address and the node Rest API Token. Now that your node is up and running, you can see these values with the following command.

```
printf "HTTP ADDRESS = http://$(cat ~/node/testnet_data/algod.net) \nREST API Token = $(cat ~/node/testnet_data/algod.token)\n"
```

Now we can add these values as environmental variables for later use. We will append these new Environmental variables to the bottom of `~/.bashrc.`

```
echo "export ALGORAND_NODE_ADDRESS=\"http://$(cat ~/node/testnet_data/algod.net)\"" >> ~/.bashrc
echo "export ALGORAND_NODE_REST_TOKEN=\"$(cat ~/node/testnet_data/algod.token)\"" >> ~/.bashrc
source ~/.bashrc
```


---

Fast Catchup allows for rapid node updates by using snapshots. If you don't use this feature, your node could take hours or days to synchronize.

The catchup point for the testnet network is available at the following address.

```
https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint
```

The code for the catchup point should look like a string of numbers and letters, as shown in figure 3-2.

<div align="center">

![EditorImages/2022/04/11 16:25/Figure_3-2_get_latest_catchpoint.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2016%3A25/Figure_3-2_get_latest_catchpoint.png)  
</div>

<table>
	<tr>
		<th>
Figure 3-2: Testnet catchup point
		</th>
	</tr>
</table>


Enter the following command to use Fast Catchup.
```
goal node catchup $(curl https://algorand-catchpoints.s3.us-east-2.amazonaws.com/channel/testnet/latest.catchpoint)
```



## 4. Create an Azure Key Vault

On the Azure Portal Home Page, Search for Key vaults, then click Key Vaults as Highlighted in Figure 4-1.

<div align="center">

![EditorImages/2022/04/09 00:22/Figure_4-1_search_and_click_Key_vaults.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-1_search_and_click_Key_vaults.png) 
</div>

<table>
	<tr>
		<th>
Figure 4-1: Search for Key vaults then click Key vaults under services
		</th>
	</tr>
</table>

In the center of the Key vaults Page, Click Create key vault, as shown in Figure 4-2.
<div align="center">

![EditorImages/2022/04/09 00:22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A22/Figure_4-2_select_Create_key_vault_on_key_vault_page.png) 
</div>

<table>
	<tr>
		<th>
Figure 4-2: Click Create key vault on the center of the page
		</th>
	</tr>
</table>

Now we are at the Create a key vault page. For the ** Resource group **, select the same group your virtual machine is in. The Region should be the same as your Resource group, and the Key vault name used for this tutorial is:

```
algo-tutorial-secrets
```

Make sure that your configuration looks like Figure 4-3, except for the region if it is different.

<div align="center">

![EditorImages/2022/04/09 00:23/Figure_4-3_Set_Resource_Group_Region_and_Name.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-3_Set_Resource_Group_Region_and_Name.png) 
</div>

<table>
	<tr>
		<th>
Figure 4-3: Set Resource group, region, Key vault name, then click Next: Access policy >
		</th>
	</tr>
</table>

On the Access Policy page, select **Add Access Policy** as highlighted in Figure 4-4.

<div align="center">

![EditorImages/2022/04/09 00:23/Figure_4-4_Click_on_Add_Access_Policy.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-4_Click_on_Add_Access_Policy.png)  
</div>

<table>
	<tr>
		<th>
Figure 4-4: click on Add Access Policy
		</th>
	</tr>
</table>

In the **Configure from template** Drop-Down, select Secret Management as shown in Figure 4-5.

<div align="center">

![EditorImages/2022/04/09 00:23/Figure_4-5_Select_Secret_Management.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A23/Figure_4-5_Select_Secret_Management.png)
</div>

<table>
	<tr>
		<th>
Figure 4-5: Select Secret Management from Configure from template Drop-Down
		</th>
	</tr>
</table>

Now select **None selected** under Select Principal as highlighted in Figure 4-6.

<div align="center">

![EditorImages/2022/04/09 00:24/Figure_4-6_select_None_selected_under_Select_Principal.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-6_select_None_selected_under_Select_Principal.png)  
</div>

<table>
	<tr>
		<th>
Figure 4-6: select **None selected** under Select Principal
		</th>
	</tr>
</table>

On the right side of the page, you will be asked to select a principal. Our principal will be our Virtual Machine. Select our virtual machine, then click Select as illustrated in Figure 4-7.

<div align="center">

![EditorImages/2022/04/09 00:24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-7_Select_Virtual_Machine_the_click_Select.png)  
</div>

<table>
	<tr>
		<th>
Figure 4-7: Select Virtual Machine then click Select
		</th>
	</tr>
</table>

Now click add, as highlighted in Figure 4-8.

<div align="center">

![EditorImages/2022/04/09 00:24/Figure_4-8_Click_Add.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-8_Click_Add.png) 
</div>


<table>
	<tr>
		<th>
Figure 4-8: Click add to add Access Policy
		</th>
	</tr>
</table>

On the Create a key vault page, you will see the Access Policy you just created under Applications. Click on Review + create, as illustrated in Figure 4-9.

<div align="center">

![EditorImages/2022/04/09 00:24/Figure_4-9_Click_on_Review__create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-9_Click_on_Review__create.png) 
</div>

<table>
	<tr>
		<th>
Figure 4-9: Click on Review + create
		</th>
	</tr>
</table>

Now confirm that your configuration is valid, click Create as shown in Figure 4-10.

<div align="center">

![EditorImages/202/04/09 00:24/Figure_4-10_Check_Validation_and_click_Create.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/09%2000%3A24/Figure_4-10_Check_Validation_and_click_Create.png) 
</div>

<table>
	<tr>
		<th>
Figure 4-10: Confirm configuration is valid then click Create
		</th>
	</tr>
</table>

## 5. Create Python Virtual Environment, and clone Tutorial GitHub Repository

Let's create a virtual environment for our python code in this step. This environment will hold all the packages we need to run the scripts we will be downloading from GitHub.

First, let's download Virtualenv for Linux using the following command:

```
sudo apt install python3.8-venv
```

Then let's create a directory for our python project and create a Virtual Environment inside it.

```
mkdir ~/algorand_on_azure_project
cd ~/algorand_on_azure_project
python3 -m venv algorand_on_azure_env
```

Now lets ACTIVATE our Virtual Environment.

```
source ~/algorand_on_azure_project/algorand_on_azure_env/bin/activate
```

    


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
		    If you have successfully activated your Virtual Environment, you will see the name of your Virtual Environment appended to the beginning of your command line.

<div align="center">

![EditorImages/2022/03/31 21:14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/03/31%2021%3A14/Figure_7-1_Successful_Activation_of_Virtual_Environment.png)
</div>
		</td>
	</tr>
</table>

Now that the Virtual Environment is Activated; let's add all the python packages we will need for this tutorial

```
pip3 install py-algorand-sdk azure-identity azure-keyvault-secrets python-dotenv
```

Last we will clone this tutorials GitHub repository into your `algorand_on_azure_project` Directory with the following command.

```
git clone https://github.com/pmartinez8241/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault.git
```

## 6. Create Algorand accounts

For this tutorial, we will be creating two accounts, one account that will send ALGO, and another account that will receive ALGO. Inside the git hub repository, you downloaded a file called `create_algorand_account.py`, and run the following command to create both accounts.

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_account.py
```

So now, in the `.env` file, that is in your `~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/` directory, you will see 2 Environmental Variable `ALGORAND_SENDER_ACCOUNT_ADDRESS`, and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS`.


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

In step one, we enable `System Managed Identity`, which is used to Authenticate our Secret client. When we created an Azure keyvault, we added an Access Policy that allows our Virtual Machine to access it. So `ManagedIdentityCredential()` retrieves the Managed Identity Credentials of our Virtual Machine then, and then we input them into our Secret Client for Authentication. The Secret Client is a Python library used to manage Azure KeyVault. Setting secrets only requires a name for your secret and the value of your secret to create it. To get a secret, all that is needed is the name of your secret.


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


The `create_algorand_account.py` file creates two environment variables, `ALGORAND_SENDER_ACCOUNT_ADDRESS` and `ALGORAND_RECEIVER_ACCOUNT_ADDRESS,` both of which hold the Account Address of an Algorand Account. Both environmental variables are stored in the `.env` file, which will be located in the same directory as the `create_algorand_account.py` python script.

## 7. Use Algorand Dispenser to fill account with ALGO

We will fill the `SENDER` account with 20 ALGO for this step. To fill the Account with ALGO, we will need the Account Address located in the directory of the GitHub repository we downloaded; run the following command from inside that directory.

```
grep "ALGORAND_SENDER" .env | cut -d "=" -f2 |  sed 's/"//g'
```

The output from the command above is shown in figure 7-1.

<div align="center">

![EditorImages/2022/04/11 20:27/Figure_7-1_Get_Sender_Account_Address.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/11%2020%3A27/Figure_7-1_Get_Sender_Account_Address.png) 
</div>

<table>
	<tr>
		<th>
Figure 7-1: Account Address for the send account
		</th>
	</tr>
</table>

The Address that was output from Figure 7-1 needs to be copied and pasted into the Algorand dispenser. The Algorand dispenser outputs Algo that is usable only in the `Test Network.` Once copy the Account Address, go to the following website.
```
https://bank.testnet.algorand.network/
```

Once at the site above, verify that you are not a robot, paste your Account Address into the Text Field, and last click dispense. Once you click dispense, you should see the `Transaction ID` as illustrated in figure 7-2.

<div align="center">

![EditorImages/2022/04/15 02:53/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/15%2002%3A53/Figure_7-2_Paste_Address_check_not_a_robot_and_see_if_successful.png) 
</div>

<table>
	<tr>
		<th>
Figure 7-2: Verify not a robot, paste account address, click dispense
		</th>
	</tr>
</table>

>>>>>>> deploy-template
Each time you put your address into the Algorand Dispenser, you will get 5 algo. Refresh your browser after each use. You will need to use the Algorand Dispenser four times to get the 20 Algo you will need for this tutorial.

## 8. Create and Sign an Algorand Transaction

We have all of the variables we will need to create a transaction and sign it. Run the following command to broadcast the signed transaction throughout the Test Network.

```
python ~/algorand_on_azure_project/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault/create_algorand_transaction.py
```

The command above outputs a `Transaction ID,` as shown in Figure 8-1.

![EditorImages/2022/04/12 18:05/Figure_8-1_Transaction_ID.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/12%2018%3A05/Figure_8-1_Transaction_ID.png)

<table>
	<tr>
		<th>
Figure 8-1: Transaction Id
		</th>
	</tr>
</table>

Now let's head to the Algorand Testnet explorer.

```
https://testnet.algoexplorer.io/
```

Finally, type your `Transaction ID` in the Search Field to see the Transaction Overview, shown in Figure 8-2.

![EditorImages/2022/04/13 17:46/Figure_8-2_Transaction_Information.png](https://algorand-devloper-portal-app.s3.amazonaws.com/static/EditorImages/2022/04/13%2017%3A46/Figure_8-2_Transaction_Information.png) 

<table>
	<tr>
		<th>
Figure 8-2: Transaction Overview
		</th>
	</tr>
</table>


---

create_algorand_transaction.py

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
** - Portions of create_algorand_transaction.py came from [Algorand Developer Partal](https://developer.algorand.org/docs/sdks/python/#sign-first-transaction) **


In the create_algorand_transaction.py script, we sent 10 ALGOS from the Sender Account to the Receiver Account. The amount is 10,000,000 because the amount sent is in MicroAlgos; 1,000,000 MicroAlgo equals 1 Algo. For the transaction fee, I used the constant MIN_TXN_FEE, which is equal to .001 Algo.

Once the prepared transaction is made, inserting the `Private Key` of your Algorand key into the `sign()` function makes it ready to be broadcast through the Algorand Testnet. To finalize the transaction, all that is needed is to send the transaction using the `send_transaction()` function.


---

# Conclusion

In this tutorial, we learned about some of the services azure provides and how to secure those services. We now know the basics of storing **Secrets** in Azure Key Vault and Deploying a Linux virtual machine. Storing API Keys, SSH Key, and Cryptocurrency Private keys in Azure Key Vault will significantly reduce the burden of keeping these values safe. We have also learned how to deploy an Algorand node and synchronize it using Fast Catchup. If you did this tutorial using Azure Web Portal, try at least once deploying your Azure web resources using the template in this [GitHub Repository](https://github.com/pmartinez8241/Create-an-Algorand-Node-on-Microsoft-Azure-and-Sign-Transactions-with-Azure-Key-Vault) to see how much less complicated it makes deployments.

</br>
</br>
</br>
</br>
</br>

---

<B>:warning:project is not audited and should not be used in a production environment.</B>