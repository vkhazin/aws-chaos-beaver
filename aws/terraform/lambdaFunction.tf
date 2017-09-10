resource "aws_lambda_function" "lambda-function" {
  filename         = "../../deployment.zip"
  function_name    = "${var.name-prefix}-chaos-beaver"
  description      = "Stop services, kill processes, and remove firewall ports to emulate failures"
  role             = "${aws_iam_role.lambda-role.arn}"
  handler          = "lambdaHandler.handler"
  runtime          = "python2.7"
}