###################
# Security group  #
###################
resource "aws_security_group" "security_group" {
  name = "${var.owner_name}-security-group-${var.region}-${var.project_name}"
  vpc_id      = var.vpc_id

    // Inbound rules (allowing all inbound traffic)
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = ["0.0.0.0/0"]
  }

  // Outbound rules (allowing all outbound traffic)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name      = "${var.owner_name}-security-group-${var.region}-${var.project_name}"
    Terraform = "true"
  }
}
