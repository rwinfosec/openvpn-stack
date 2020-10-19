from src.stack import Stack
from robber import expect
from settings import vpc_id


def test_openvpn_ec2_instance():
    output = (Stack().template_to_json())
    properties = output["Resources"]["EC2OpenVPN"]["Properties"]

    expect(properties["ImageId"]).to.eq('ami-0b69ea66ff7391e80')
    expect(properties["InstanceType"]).to.eq('t2.micro')
    expect(properties["KeyName"]).to.eq('rwalker')


def test_openvpn_security_group():
    output = (Stack().template_to_json())
    properties = output["Resources"]["OpenVPNSecurityGroup"]["Properties"]

    expect(properties["GroupName"]).to.eq('OpenVPN')
    expect(properties["GroupDescription"]).to.eq(
        'This is a security group for OpenVPN'
    )
    expect(properties["SecurityGroupIngress"]).to.eq(
        [
            {
                "CidrIp": "0.0.0.0/0",
                "IpProtocol": "tcp",
                "FromPort": 22,
                "ToPort": 22
             },
            {
                "CidrIp": "0.0.0.0/0",
                "IpProtocol": "udp",
                "FromPort": 1194,
                "ToPort": 1194
            }
        ]
    )
    expect(properties["SecurityGroupEgress"]).to.eq(
        [
            {'CidrIp': '0.0.0.0/0',
             'FromPort': -1,
             'IpProtocol': -1,
             'ToPort': -1
             }
        ]
    )
    expect(properties["VpcId"]).to.eq(vpc_id)
