from register_job_definition import create_job_definition
from submit_job import submit_job


def main():
    job_def_arn = create_job_definition(job_definition_name="TestJobDefinition",
                                        job_type="container",
                                        container_properties={
                                            "image": "230484698727.dkr.ecr.us-west-2.amazonaws.com/calculate_primes:latest",
                                            'command': ['python', 'calculate_primes.py'],
                                            'resourceRequirements': [
                                                {
                                                    'value': '0.5',
                                                    "type": "VCPU",
                                                },
                                                {
                                                    "value": "1024",
                                                    "type": "MEMORY",
                                                }
                                            ],
                                            "executionRoleArn":"arn:aws:iam::230484698727:role/TestBatchRole",
                                            'networkConfiguration': {
                                                'assignPublicIp': 'ENABLED',
                                            },
                                        },
                                        platform_capabilities=("FARGATE",))
    job_queue = 'CalculatePrimeJobQueue'
    job_name = 'CalculatePrimes'

    job_id = submit_job(job_def_arn, job_queue, job_name)
    print(f"Job submitted with ID: {job_id}")


if __name__ == "__main__":
    main()
