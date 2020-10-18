from .resources.ec2 import Ec2Instance
from troposphere import Template
import json


class Stack:
    def __init__(self):
        self._template = Template()
        template = self._template

        open_vpn = {"ami": "ami-0b69ea66ff7391e80",
                    "resourceName": "OpenVPN",
                    "keyName": "rwalker"}

        template.add_resource(Ec2Instance(name=open_vpn["resourceName"],
                                          ami=open_vpn["ami"],
                                          key_name=open_vpn["keyName"]))

    def template_to_json(self):
        print(self._template.to_json())
        return json.loads(self._template.to_json())


if __name__ == '__main__':
    Stack()
