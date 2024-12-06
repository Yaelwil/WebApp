module "vpc" {
  source = "./modules/vpc"

  owner              = "yaelwil"
  project            = "WebApp"
  main_vpc_cidr      = "10.0.0.0/16"
  public_subnet_1    = "10.0.0.0/24"
  public_subnet_2    = "10.0.1.0/24"
  availability_zone_1 = "eu-west-1a"
  availability_zone_2 = "eu-west-1b"
  region = "eu-west-1"
}

module "ec2_machines" {
    source = "./modules/ec2_machines"

  instance_type    = "t2.micro"
  owner_name       = "yaelwil"
  project_name     = "WebApp"
  public_key_name  = ""
  public_subnet_id = [module.vpc.public_subnet_id_1,module.vpc.public_subnet_id_2]
  region           = "eu-west-1"
  ubuntu_ami       = ""
  vpc_id           = module.vpc.vpc_id
}
