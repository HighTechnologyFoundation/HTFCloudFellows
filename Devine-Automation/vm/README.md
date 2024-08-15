# Initializing the environment

## Prerequisite Requirements
* AWS CLI
* Terraform
* SSH Key

## Linux Setup
### AWS CLI
Following the guide at https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html, use the Linux tab and follow the Command line installer guide for the current system
In order to setup the AWS CLI, the AWS account needs to have an access key created. Follow https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey to create a key. Do not click out of the "Retrieve acceess key" page without downloading the csv file or copying and storing the "Secret access key".
In a terminal, run ```aws configure``` and input the Access Key ID and Secret Access Key created in the previous step. Set the default region to us-east-1 and default output format to json.

### Terraform
Following the guide at https://developer.hashicorp.com/terraform/install#linux, install the terraform package.

### SSH Key
Run the following command to generate an ssh key for use when interacting with your VM. By default it will be stored in `~/.ssh/id_rsa` if this is not where you choose to store your key, the path to the keys must be updated in `main.tf`.
```
ssh-keygen -t rsa -b 4096
```

## Windows Setup
TBD

## Running the Terraform Builder
Copy `main.tf` and `install_docker.sh` into the same directory as the Dockerfile and all required dependencies.
Run the following commands in the same directory as main.tf:
```
terraform init
terraform plan
terraform apply
```

The command `terraform plan` will provide an output describing the resources to be created.

**REMEMBER**
When completed with testing the application, run:
```
terraform destroy
```

## Running the docker container
Using an ssh client and the ssh key generated in previous steps, connect to the public IP of your AWS VM. Upon connecting, you can run the following commands to build and run your webapp container:
```
docker build -t whatever .
docker run -it -p host_port:container_port whatever
```
In the above commands, replace *whatever* with your desired container name. Also, replace *host_port* and *container_port* with the correct port numbers that the webserver runs on.


## References
N/A