import aws_cdk as core
import aws_cdk.assertions as assertions

from bilenivar_infra.bilenivar_infra_stack import BilenivarInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in bilenivar_infra/bilenivar_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BilenivarInfraStack(app, "bilenivar-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
