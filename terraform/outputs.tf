output "resource_group_id" {
  value = azurerm_resource_group.main.id
}

output "storage_account_id" {
  value = azurerm_storage_account.main.id
}

output "key_vault_id" {
  value = azurerm_key_vault.main.id
}