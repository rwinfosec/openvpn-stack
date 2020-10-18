from src.stack import Stack
from robber import expect


def test_ec2_openvpn_stack():
    output = (Stack().template_to_json())
    properties = output["Resources"]["OpenVPN"]["Properties"]

    expect(properties["ImageId"]).to.eq('ami-0b69ea66ff7391e80')
    expect(properties["InstanceType"]).to.eq('t2.micro')
    expect(properties["KeyName"]).to.eq('rwalker')
