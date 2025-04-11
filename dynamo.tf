resource "aws_dynamodb_table" "user_logins" {
  name           = "UserLogins"
  billing_mode   = "PAY_PER_REQUEST"  # Auto-scaling (no capacity planning)
  hash_key       = "UserID"           # Primary key
  range_key      = "LoginTimestamp"   # Sort key (optional)

  # Attribute definitions
  attribute {
    name = "UserID"
    type = "S"  # String
  }

  attribute {
    name = "LoginTimestamp"
    type = "N"  # Number (Unix timestamp)
  }

  # Global Secondary Index (GSI) for querying by email (optional)
  global_secondary_index {
    name               = "EmailIndex"
    hash_key           = "Email"
    projection_type    = "ALL"  # Include all attributes in the index
    write_capacity    = 1      # Only used if billing_mode = PROVISIONED
    read_capacity     = 1
  }

  attribute {
    name = "Email"
    type = "S"
  }

  # Encryption at rest (enabled by default)
  server_side_encryption {
    enabled = true
  }

  tags = {
    Name        = "User-Login-Table"
    Environment = "Production"
  }
}

# Output the table name
output "dynamodb_table_name" {
  value = aws_dynamodb_table.user_logins.name
}