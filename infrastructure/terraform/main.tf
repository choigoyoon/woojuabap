provider "aws" {
  region = var.aws_region
}

resource "aws_lambda_function" "crypto_webhook" {
  filename         = "lambda_function.zip"
  function_name    = "crypto_webhook"
  role            = aws_iam_role.lambda_role.arn
  handler         = "lambda_handler.lambda_handler"
  runtime         = "python3.9"

  environment {
    variables = {
      TELEGRAM_BOT_TOKEN = var.telegram_bot_token
      OPENAI_API_KEY     = var.openai_api_key
    }
  }
} 