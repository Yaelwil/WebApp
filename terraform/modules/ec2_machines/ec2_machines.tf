resource "aws_instance" "ec2_instance" {
  ami                    = var.ubuntu_ami
  instance_type          = var.instance_type
  subnet_id              = var.public_subnet_id[0]
  key_name               = var.public_key_name
  security_groups        = [aws_security_group.security_group.id]

  tags = {
    Name      = "${var.owner_name}-ec2-instance-${var.region}-${var.project_name}"
    Terraform = "true"
  }

}
