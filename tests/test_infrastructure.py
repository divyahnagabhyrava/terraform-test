# tests/test_infrastructure.py
import os
import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import ResourceNotFoundError

# Test Resource Group
def test_resource_group_properties():
    """
    Verifies:
    1. Resource Group exists
    2. Correct location
    3. Required tags present
    """
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, os.getenv("ARM_SUBSCRIPTION_ID"))
    
    rg = client.resource_groups.get("example-resources")
    assert rg.location == "eastus"
    assert rg.tags['Environment'] == 'test'
    assert rg.tags['Managed_By'] == 'Terraform'

# Test Storage Account
def test_storage_account_security():
    """
    Verifies:
    1. Storage Account exists
    2. TLS version is 1.2
    3. Encryption is enabled
    4. Public access is blocked
    """
    credential = DefaultAzureCredential()
    client = StorageManagementClient(credential, os.getenv("ARM_SUBSCRIPTION_ID"))
    
    storage = client.storage_accounts.get_properties(
        "example-resources",
        "examplestorage"
    )
    assert storage.minimum_tls_version == "TLS1_2"
    assert storage.encryption.services.blob.enabled
    assert storage.allow_blob_public_access is False