provider "aws" {
  region                    = "${var.region}"
  shared_credentials_file   = "${var.aws-credentials}"
  profile                   = "${var.aws-profile}"
  version                   = "0.1.4"
}