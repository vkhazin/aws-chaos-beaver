clear

pwd=$(pwd)
cd ./aws/terraform

sudo apt install -y zip

zip ./deployment.zip -r ./ -x *.git* -x *aws* -x terraform*
./bin/terraform init ./ -yes
./bin/terraform apply ./

rm ./deployment.zip

cd $pwd