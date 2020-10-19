from .resources.ec2 import Ec2Instance
from .resources.security_groups import EC2SecurityGroup
from troposphere import Template, Ref
from settings import vpc_id, ssh_key
import json


class Stack:
    def __init__(self):
        self._template = Template()
        template = self._template

        ingress_sg = [{"CidrIp": "0.0.0.0/0", "IpProtocol": "tcp",
                       "FromPort": 22, "ToPort": 22},
                      {"CidrIp": "0.0.0.0/0", "IpProtocol": "udp",
                       "FromPort": 1194, "ToPort": 1194}]
        egress_sg = [{"CidrIp": "0.0.0.0/0", "IpProtocol": -1,
                      "FromPort": -1, "ToPort": -1}]

        openvpn_security_group = template.add_resource(
            EC2SecurityGroup(ingress_sg,
                             egress_sg,
                             vpc_id))

        template.add_resource(Ec2Instance(
            ami="ami-0b69ea66ff7391e80",
            key_name=ssh_key,
            security_groups=Ref(
                openvpn_security_group
            )
        ))

    def template_to_json(self):
        print(self._template.to_json())
        return json.loads(self._template.to_json())
