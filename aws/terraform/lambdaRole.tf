# Create lambda role
resource "aws_iam_role" "lambda-role" {
  name = "${var.name-prefix}-chaos-beaver-role"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

# Associate ssm built-in policy
resource "aws_iam_policy_attachment" "lambda-role-policy-attachment" {
  name       = "lambda-role-policy-attachment"
  roles      = ["${aws_iam_role.lambda-role.name}"]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonSSMAutomationRole"
}

# Associate inline policy for CloudWatch
resource "aws_iam_role_policy" "lambda-policy" {
  name = "${var.name-prefix}-chaos-beaver-policy"
  role = "${aws_iam_role.lambda-role.id}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    }
  ]
}
EOF
}