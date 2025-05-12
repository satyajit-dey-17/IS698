output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs (for ALB)"
  value       = [
    aws_subnet.public1.id,
    aws_subnet.public2.id
  ]
}

output "private_subnet_ids" {
  description = "List of private subnet IDs (for RDS)"
  value       = [
    aws_subnet.private1.id,
    aws_subnet.private2.id
  ]
}

