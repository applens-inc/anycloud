import boto3

batch_client = boto3.client('batch')


def create_job_definition(job_definition_name: str,
                          job_type: str,
                          container_properties: dict,
                          platform_capabilities: tuple):
    job_def = batch_client.register_job_definition(
        jobDefinitionName=job_definition_name,
        type=job_type,
        containerProperties=container_properties,
        platformCapabilities=platform_capabilities,
    )
    return job_def['jobDefinitionArn']
