
import os
import pytest
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.core.exceptions import ResourceNotFoundError


def test_resource_group_properties():
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, os.getenv("ARM_SUBSCRIPTION_ID"))
    
    rg = client.resource_groups.get("example-resources")
    assert rg.location == "eastus"
    assert rg.tags['Environment'] == 'test'
    assert rg.tags['Managed_By'] == 'Terraform'


def test_storage_account_security():
    credential = DefaultAzureCredential()
    client = StorageManagementClient(credential, os.getenv("ARM_SUBSCRIPTION_ID"))
    
    storage = client.storage_accounts.get_properties(
        "example-resources",
        "examplestorage"
    )
    assert storage.minimum_tls_version == "TLS1_2"
    assert storage.encryption.services.blob.enabled
    assert storage.allow_blob_public_access is False