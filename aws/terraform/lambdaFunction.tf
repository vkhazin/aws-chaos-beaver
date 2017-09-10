resource "aws_lambda_function" "lambda-function" {
  filename         = "./deployment.zip"
  function_name    = "${var.name-prefix}-chaos-beaver"
  role             = "${aws_iam_role.lambda-role.arn}"
  handler          = "lambdaHandler.handler"
  runtime          = "Python 2.7"
}