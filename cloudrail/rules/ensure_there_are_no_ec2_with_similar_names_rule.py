from typing import Dict, List

from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.rules.aws.aws_base_rule import AwsBaseRule
from cloudrail.knowledge.rules.base_rule import Issue
from cloudrail.knowledge.rules.rule_parameters.base_paramerter import ParameterType


class EnsureThereAreNoEc2WithSimilarNamesRule(AwsBaseRule):
    def execute(self, env_context: AwsEnvironmentContext, parameters: Dict[ParameterType, any]) -> List[Issue]:
        issues: List[Issue] = []
        # TODO: Part 3 - using cloudrail-knowledge package write rule logic that alerts (creates an issue)
        # if the 2 ec2 instances contain similar name. See readme.md for similarity definition
        # use your own solution, without importing external package
        return issues

    def get_id(self) -> str:
        return 'ensure_there_are_no_ec2_with_similar_names_rule'

    def should_run_rule(self, environment_context: AwsEnvironmentContext) -> bool:
        return True
