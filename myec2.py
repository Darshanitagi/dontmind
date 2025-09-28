import boto3

def launch_ec2_instance(ami_id, instance_type, key_name, security_group_ids, subnet_id, region_name):
    ec2 = boto3.resource('ec2', region_name=region_name)
    instance = ec2.create_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        SubnetId=subnet_id,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Jenkins-Managed-Instance'},
                ]
            },
        ]
    )
    print(f"Launched EC2 instance with ID: {instance[0].id}")
    return instance[0].id

if __name__ == "__main__":
     
    ami = "ami-0a716d3f3b16d290c"  # Example AMI ID
    instance_type = "t3.micro"
    key_pair = "myec2instance"
    security_groups = ["sg-0862b15607924d71b"] # Example Security Group ID
    subnet = "subnet-0e89ef6df77a03b2d" # Example Subnet ID
    aws_region = "eu-north-1"

    launch_ec2_instance(ami, instance_type, key_pair, security_groups, subnet, aws_region)