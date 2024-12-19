variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-2"
}

variable "telegram_bot_token" {
  description = "Telegram Bot Token"
  type        = string
}

variable "openai_api_key" {
  description = "OpenAI API Key"
  type        = string
} 