clear
sudo apt install -y zip


DIRNAME=$(dirname "$0")

zip $DIRNAME/deployment.zip -r ./ -x *.git* -x *aws* -x terraform*

$DIRNAME/terraform/bin/terraform init $DIRNAME/terraform
$DIRNAME/terraform/bin/terraform apply $DIRNAME/terraform

# rm $DIRNAME/deployment.zip