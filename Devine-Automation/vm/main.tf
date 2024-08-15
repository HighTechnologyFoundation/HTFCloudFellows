# main.tf
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "us-east-1" 
  shared_config_files = ["~/.aws/config"]
  shared_credentials_files = ["~/.aws/credentials"]
}

resource "aws_key_pair" "deployer" {
  key_name = "tf-deploy-key"
  public_key = "${file("~/.ssh/id_rsa.pub")}"
}


resource "aws_security_group" "instance_security_group" {
  # change this to the required port for access to the webapp
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow traffic in from all sources
  }

  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow traffic in from all sources
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# if provided a custom AMI, change ami to be equal to that AMI
resource "aws_instance" "app_instance" {
  ami = "ami-0a0e5d9c7acc336f1"
  instance_type = "t2.micro" # change this if more resources are required (this is the only available free tier instance in us-east-1)
  key_name = aws_key_pair.deployer.key_name
}

resource "aws_network_interface_sg_attachment" "sg_attachment" {
  security_group_id    = aws_security_group.instance_security_group.id
  network_interface_id = aws_instance.app_instance.primary_network_interface_id
}


resource "null_resource" "docker_file" {
  provisioner "file" {
    connection {
      type = "ssh"
      user = "ubuntu"
      private_key = "${file("~/.ssh/id_rsa")}"
      host = aws_instance.app_instance.public_ip
    }
    source = "Dockerfile"
    destination = "/home/ubuntu/Dockerfile"
  }
}

resource "null_resource" "docker_installer"{
  provisioner "file" {
    connection {
      type = "ssh"
      user = "ubuntu"
      private_key = "${file("~/.ssh/id_rsa")}"
      host = aws_instance.app_instance.public_ip
    }
    source = "install_docker.sh"
    destination = "/home/ubuntu/install_docker.sh"
  }
}

resource "null_resource" "docker_depend"{
  # change this with the directory name for the Dockerfile's dependency
  provisioner "file" {
    connection {
      type = "ssh"
      user = "ubuntu"
      private_key = "${file("~/.ssh/id_rsa")}"
      host = aws_instance.app_instance.public_ip
    }
    source = "demo_app"
    destination = "/home/ubuntu/demo_app"
  }
}

resource "null_resource" "install" {
  provisioner "remote-exec" {
    connection {
      type = "ssh"
      user = "ubuntu"
      private_key = "${file("~/.ssh/id_rsa")}"
      host = aws_instance.app_instance.public_ip
    }
    inline = [
      "chmod +x /home/ubuntu/install_docker.sh",
      "/home/ubuntu/install_docker.sh",
      "sudo addgroup docker",
      "sudo adduser ubuntu docker"
    ]
  }
  depends_on = [
    null_resource.docker_installer
  ]
}

output "instance_ip" {
  value = aws_instance.app_instance.public_ip
}