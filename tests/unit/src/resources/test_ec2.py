from robber import expect
from src.resources.ec2 import Ec2Instance


def test_ec2_instance():
    output = Ec2Instance(name='MyInstance',
                         ami='ami-123456',
                         key_name='ssh-key'
                         )
    expect(output.title).to.eq('MyInstance')
    expect(output.properties['ImageId']).to.eq('ami-123456')
    expect(output.properties['InstanceType']).to.eq('t2.micro')
    expect(output.properties['KeyName']).to.eq('ssh-key')
