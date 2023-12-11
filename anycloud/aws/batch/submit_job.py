import boto3

batch_client = boto3.client('batch')


def submit_job(job_def_arn, job_queue, job_name):
    job_response = batch_client.submit_job(
        jobName=job_name,
        jobQueue=job_queue,
        jobDefinition=job_def_arn,
        # Add any additional parameters needed
    )
    return job_response['jobId']
