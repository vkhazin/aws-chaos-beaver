clear
sudo apt install -y zip

pwd=$(pwd)
cd ./aws/terraform

curl -O https://releases.hashicorp.com/terraform/0.10.4/terraform_0.10.4_linux_amd64.zip
unzip ./terraform_0.10.4_linux_amd64.zip

zip ./deployment.zip -r ./ -x *.git* -x *aws* -x terraform*
./terraform init ./ -yes
./terraform apply ./

rm ./deployment.zip

cd $pwd