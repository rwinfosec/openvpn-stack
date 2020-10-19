import boto3
import json
import botocore
from src.stack import Stack
from settings import stack_name

cf = boto3.client('cloudformation')


def main():
    template = json.dumps(Stack().template_to_json())
    params = {'StackName': stack_name, 'TemplateBody': template}

    try:
        cf.validate_template(TemplateBody=template)
        if _stack_exists(stack_name):
            print('Updating {}'.format(stack_name))
            cf.update_stack(**params)
            waiter = cf.get_waiter('stack_update_complete')
        else:
            print('Creating {}'.format(stack_name))
            cf.create_stack(**params)
            waiter = cf.get_waiter('stack_create_complete')
        print("...waiting for stack to be ready...")
        waiter.wait(StackName=stack_name)
    except botocore.exceptions.ClientError as ex:
        error_message = ex.response['Error']['Message']
        if error_message == 'No updates are to be performed.':
            print("No changes")
        else:
            raise


def _stack_exists(stack_name):
    stacks = cf.list_stacks()['StackSummaries']
    for stack in stacks:
        if stack['StackStatus'] == 'DELETE_COMPLETE':
            continue
        if stack_name == stack['StackName']:
            return True
    return False


if __name__ == '__main__':
    main()
