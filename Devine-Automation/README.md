# Initializing the environment

## Prerequisite Requirements
* AWS CLI
* Terraform
* Docker Engine

## Linux Setup
### AWS CLI
Following the guide at https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html, use the Linux tab and follow the Command line installer guide for the current system
In order to setup the AWS CLI, the AWS account needs to have an access key created. Follow https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey to create a key. Do not click out of the "Retrieve acceess key" page without downloading the csv file or copying and storing the "Secret access key".
In a terminal, run ```aws configure``` and input the Access Key ID and Secret Access Key created in the previous step. Set the default region to us-east-1 and default output format to json.

### Terraform
Following the guide at https://developer.hashicorp.com/terraform/install#linux, install the terraform package.

### Docker Engine
Following the guide at https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository, install docker.
After the installation is complete, a group named "docker" should be created. If the docker group is missing, run the following `sudo addgroup docker`.
Add your user account to the docker group by using the following: `sudo adduser *USERNAME* docker` replacing *USERNAME* with your username. This step will require you to log out of your account and log in again for changes to take place.

## Windows Setup
TBD

## Running the Terraform Builder
Copy main.tf into the same directory as the Dockerfile and all required dependencies.
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
This will ensure AWS credits are not wasted while the application is being modified locally. The approximate cost for 5 minutes of runtime is $0.10. *However, the cost for 24 hours of runtime is approximately $30.00.*

## References
https://earthly.dev/blog/deploy-dockcontainers-to-awsecs-using-terraform/
https://www.linkedin.com/pulse/how-upload-docker-images-aws-ecr-using-terraform-hendrix-roa

