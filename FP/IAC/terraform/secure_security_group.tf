resource "aws_security_group" "example" {
  name        = "restricted-sg"
  description = "Security group with restricted ingress rules"

  ingress {
    description = "Allow SSH access from private network"  # Add rule description
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["192.168.1.0/24"]
  }

  egress {
    description = "Allow all outbound traffic"  # Add rule description
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
