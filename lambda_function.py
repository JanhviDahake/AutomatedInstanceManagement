import boto3


def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')


    # Auto-Stop
    stop_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto_Stop_ec2']}]
    )
    for instance in stop_instances:
        if instance.state['Name'] == 'running':
            instance.stop()
            print(f"Stopped instance: {instance.id}")
        else:
            print(f"Instance {instance.id} not in 'running' state")


    # Auto-Start
    start_instances = ec2.instances.filter(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto_Start_ec2']}]
    )
    for instance in start_instances:
        if instance.state['Name'] == 'stopped':
            instance.start()
            print(f"Started instance: {instance.id}")
        else:
            print(f"Instance {instance.id} not in 'stopped' state")
