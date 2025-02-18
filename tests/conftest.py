import os
import pytest
from python_terraform import Terraform

@pytest.fixture(scope="session")
def terraform_config():
    """Provides test configuration"""
    return {
        "variables": {
            "resource_group_name": "rg-test-001",
            "location": "eastus",
            "environment": "test"
        }
    }

@pytest.fixture(scope="session")
def tf():
    """Initialize Terraform"""
    tf = Terraform()
    tf.init()
    return tf

@pytest.fixture(scope="session", autouse=True)
def terraform_setup(tf, terraform_config):
    """Apply Terraform and cleanup after tests"""
    try:
        # Apply the configuration
        tf.apply(skip_plan=True, vars=terraform_config["variables"])
        yield
    finally:
        # Cleanup after tests
        tf.destroy(auto_approve=True, vars=terraform_config["variables"])