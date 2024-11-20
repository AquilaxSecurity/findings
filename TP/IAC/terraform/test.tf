resource "aws_security_group" "example" {
  name        = "open-sg"
  description = "Security group with open rules"
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
