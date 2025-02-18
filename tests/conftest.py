import os
import pytest
from python_terraform import Terraform
import subprocess

@pytest.fixture(scope="session")
def terraform_config():
    return {
        "root_path": "./terraform",
        "variables": {
            "environment": "test",
            "resource_group_name": "rg-test-001",
            "location": "eastus"
        }
    }

@pytest.fixture(scope="session")
def tf():
    tf = Terraform(working_dir="./terraform")
    return tf

@pytest.fixture(scope="session", autouse=True)
def terraform_setup(tf, terraform_config):
    # Initialize and apply Terraform
    tf.init()
    tf.apply(skip_plan=True, vars=terraform_config["variables"])
    yield
    # Cleanup
    tf.destroy(auto_approve=True, vars=terraform_config["variables"])