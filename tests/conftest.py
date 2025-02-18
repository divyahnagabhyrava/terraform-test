import os
import pytest
from python_terraform import Terraform

@pytest.fixture(scope="session")
def terraform_config():
    """Provides test configuration"""
    # These values must match your Terraform variables
    return {
        "variables": {
            "resource_group_name": "example-resources",  # Match your Terraform config
            "location": "eastus",
            "environment": "test"
        }
    }

@pytest.fixture(scope="session")
def tf():
    """Initialize Terraform"""
    # Specify the path to your Terraform files
    tf = Terraform(working_dir="./terraform")
    tf.init()
    return tf

@pytest.fixture(scope="session", autouse=True)
def terraform_setup(tf, terraform_config):
    """Apply Terraform and cleanup after tests"""
    try:
        print("Applying Terraform configuration...")
        return_code, stdout, stderr = tf.apply(
            skip_plan=True,
            vars=terraform_config["variables"],
            capture_output=True
        )
        if return_code != 0:
            print(f"Terraform apply failed: {stderr}")
            raise Exception("Terraform apply failed")
        print("Terraform apply successful")
        yield
    finally:
        print("Cleaning up resources...")
        tf.destroy(auto_approve=True, vars=terraform_config["variables"])