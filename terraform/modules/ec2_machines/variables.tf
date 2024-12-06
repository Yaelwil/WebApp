########################
# General project vars #
########################

variable "owner_name" {
  description = "owner_name"
type        = string
}

variable "project_name" {
  description = "project_name"
type        = string
}

variable "region" {
description = "Deployment region"
type        = string
}

variable "public_key_name" {
  description = "public ssh key path"
  type = string
}

################
# Network Vars #
################

variable "vpc_id" {
  description = "vpc_id"
type        = string
}

variable "public_subnet_id" {
  description = "public_subnet_id"
type        = string
}

#################
# Instance Vars #
#################

variable "ubuntu_ami" {
  description = "ubuntu_ami"
type        = string
}

variable "instance_type" {
  description = "instance_type"
type        = string
}