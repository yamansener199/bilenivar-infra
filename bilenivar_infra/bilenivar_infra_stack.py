import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_s3 as s3
from aws_cdk import Stack, Tags
from constructs import Construct

class BilenivarInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc_name = 'vpcmain'
        self.vpc_cidr = '192.168.0.0/16'

        self.__create_vpc()
    
    def __create_vpc(self):
        vpc_construct_id = 'vpc'

        self.vpc: ec2.Vpc = ec2.Vpc(
            self, vpc_construct_id,
            vpc_name=self.vpc_name,
            ip_addresses=ec2.IpAddresses.cidr(self.vpc_cidr),
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name='Public',
                    cidr_mask=20
                ), ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name='Compute',
                    cidr_mask=20
                ), ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name='RDS',
                    cidr_mask=20
                )
            ],
            nat_gateways=1
        )