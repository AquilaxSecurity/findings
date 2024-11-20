resource "aws_security_group" "example" {
  name        = "open-sg"
  description = "Security group with open ingress rules"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
