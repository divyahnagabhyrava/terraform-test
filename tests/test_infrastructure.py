import os
import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient

def test_resource_group_exists(terraform_config):
    """Test if resource group exists and has correct properties"""
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(
        credential, 
        os.getenv("ARM_SUBSCRIPTION_ID")
    )
    
    rg = client.resource_groups.get(
        terraform_config["variables"]["resource_group_name"]
    )
    assert rg.name == terraform_config["variables"]["resource_group_name"]
    assert rg.location == terraform_config["variables"]["location"]

def test_storage_account_exists(terraform_config):
    """Test if storage account exists and has correct properties"""
    credential = DefaultAzureCredential()
    client = StorageManagementClient(
        credential, 
        os.getenv("ARM_SUBSCRIPTION_ID")
    )
    
    storage_accounts = client.storage_accounts.list_by_resource_group(
        terraform_config["variables"]["resource_group_name"]
    )
    storage_account = next(storage_accounts)
    
    assert storage_account.sku.name == "Standard_LRS"
    assert storage_account.minimum_tls_version == "TLS1_2"