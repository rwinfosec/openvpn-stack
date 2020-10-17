import troposphere.ec2 as ec2


class Ec2Instance(ec2.Instance):
    def __init__(self, name, ami, key_name=""):
        super(Ec2Instance, self).__init__(name,
                                          ImageId=ami,
                                          InstanceType="t1.micro",
                                          KeyName=key_name,
                                          )
