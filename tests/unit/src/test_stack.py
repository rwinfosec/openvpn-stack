from src.stack import Stack
from robber import expect
import json


def test_ec2_openvpn_stack():
    output = (json.loads(Stack().template_to_json()))
    properties = output["Resources"]["OpenVPN"]["Properties"]

    expect(properties["ImageId"]).to.eq('ami-027cab9a7bf0155df')
    expect(properties["InstanceType"]).to.eq('t1.micro')
    expect(properties["KeyName"]).to.eq('rwalker')
