import troposphere.ec2 as ec2


class Ec2Instance(ec2.Instance):
    def __init__(self, ami, key_name, security_groups):
        super(Ec2Instance, self).__init__(
            "EC2OpenVPN",
            ImageId=ami,
            InstanceType="t2.micro",
            KeyName=key_name,
            SecurityGroupIds=[security_groups]
        )
