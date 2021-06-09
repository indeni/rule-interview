from typing import Dict, List

from cloudrail.knowledge.context.aws.aws_environment_context import AwsEnvironmentContext
from cloudrail.knowledge.rules.aws.aws_base_rule import AwsBaseRule
from cloudrail.knowledge.rules.base_rule import Issue
from cloudrail.knowledge.rules.rule_parameters.base_paramerter import ParameterType


class EnsureNoProductionTagRule(AwsBaseRule):
    def execute(self, env_context: AwsEnvironmentContext, parameters: Dict[ParameterType, any]) -> List[Issue]:
        issues: List[Issue] = []
        # TODO: Part 2 - using cloudrail-knowledge package write rule logic that alerts (creates an issue)
        # if the cloud resource contains environment=production tag
        # documentation can be found here: https://knowledge.docs.cloudrail.app/)
        return issues

    def get_id(self) -> str:
        return 'ensure_no_production_tag_rule'

    def should_run_rule(self, environment_context: AwsEnvironmentContext) -> bool:
        return True
