clear
sudo apt install -y zip
zip ./deployment.zip -r ./ -x *.git* -x aws\*

pwd=$(pwd)
cd ./aws/terraform

curl -O https://releases.hashicorp.com/terraform/0.10.4/terraform_0.10.4_linux_amd64.zip
unzip -q ./terraform_0.10.4_linux_amd64.zip

./terraform init ./

chmod +x ./.terraform/plugins/linux_amd64/terraform-provider-aws_v0.1.4_x4
./terraform apply ./

rm ./terraform
rm ./terraform_0.10.4_linux_amd64.zip

cd $pwd
rm ./deployment.zip
