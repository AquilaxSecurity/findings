resource "aws_security_group" "example" {
  name        = "restricted-sg"
  description = "Security group with restricted ingress rules"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["192.168.1.0/24"]  # Restricted to a private network
  }
}
