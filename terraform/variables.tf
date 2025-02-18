variable "resource_group_name" {
  type        = string
  description = "Resource group name"
  default     = "example-resources"
}

variable "location" {
  type        = string
  description = "Azure region"
  default     = "eastus"
}

variable "environment" {
  type        = string
  description = "Environment name"
  default     = "test"
}

variable "subscription_id" {
  type        = string
  description = "Azure Subscription ID"
}

variable "tenant_id" {
  type        = string
  description = "Azure Tenant ID"
}

variable "client_id" {
  type        = string
  description = "Azure Client ID"
}

variable "client_secret" {
  type        = string
  description = "Azure Client Secret"
}