########################
# General project vars #
########################

output "owner_name" {
  description = "owner_name"
  value       = var.owner_name
}

output "project_name" {
  description = "project_name"
  value       = var.project_name
}

output "region" {
description = "Deployment region"
  value     = var.region
}

output "public_key_name" {
  description = "public ssh key path"
  value       = var.public_key_name
}

################
# Network Vars #
################

output "vpc_id" {
  description = "vpc_id"
  value       = var.vpc_id
}

output "public_subnet_id" {
  description = "public_subnet_id"
  value       = var.public_subnet_id
}

#################
# Instance Vars #
#################

output "ubuntu_ami" {
  description = "ubuntu_ami"
  value       = var.ubuntu_ami
}

output "instance_type" {
  description = "instance_type"
  value       = var.instance_type
}