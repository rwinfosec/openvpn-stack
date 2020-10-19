from troposphere.ec2 import SecurityGroup


class EC2SecurityGroup(SecurityGroup):
    def __init__(self, ingress, egress, vpc_id):
        super(EC2SecurityGroup, self).__init__(
            "OpenVPNSecurityGroup",
            GroupName="OpenVPN",
            GroupDescription="This is a security group for OpenVPN",
            SecurityGroupEgress=egress,
            SecurityGroupIngress=ingress,
            VpcId=vpc_id
        )
