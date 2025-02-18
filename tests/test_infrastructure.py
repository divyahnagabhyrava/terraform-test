import os
import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.core.exceptions import ResourceNotFoundError

def test_resource_group_exists(terraform_config):
    """Test if resource group exists and has correct properties"""
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(
        credential, 
        os.getenv("ARM_SUBSCRIPTION_ID")
    )
    
    try:
        rg = client.resource_groups.get(
            terraform_config["variables"]["resource_group_name"]
        )
        assert rg.name == terraform_config["variables"]["resource_group_name"]
        assert rg.location == terraform_config["variables"]["location"]
    except ResourceNotFoundError:
        pytest.fail(f"Resource group {terraform_config['variables']['resource_group_name']} not found. Ensure Terraform apply was successful.")