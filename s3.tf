resource "aws_s3_bucket" "static_web_bucket" {
  bucket = "aq60258terraformhw"
  tags = {
    Name        = "Static-Web-Bucket"
    Environment = "Production"
  }
}


resource "aws_s3_bucket_website_configuration" "static_web_hosting" {
  bucket = aws_s3_bucket.static_web_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}

resource "aws_s3_bucket_public_access_block" "block_public" {
  bucket = aws_s3_bucket.static_web_bucket.id

  block_public_acls       = false  # Required for public reads
  block_public_policy     = false  # Required for public reads
  ignore_public_acls      = false
  restrict_public_buckets = false
}


resource "aws_s3_bucket_policy" "public_read" {
  bucket = aws_s3_bucket.static_web_bucket.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid       = "PublicReadGetObject",
        Effect    = "Allow",
        Principal = "*",
        Action    = "s3:GetObject",
        Resource  = "${aws_s3_bucket.static_web_bucket.arn}/*"
      }
    ]
  })
}


resource "aws_s3_object" "index" {
  bucket       = aws_s3_bucket.static_web_bucket.id
  key          = "index.html"
  content      = <<EOF
<html>
  <body>
    <h1>Static Website Hosted on S3!</h1>
  </body>
</html>
EOF
  content_type = "text/html"
}


output "s3_website_url" {
  value = aws_s3_bucket.static_web_bucket.website_endpoint
}