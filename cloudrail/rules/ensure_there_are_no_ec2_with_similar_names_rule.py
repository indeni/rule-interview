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
        ec2_a = env_context.ec2s.__getitem__(0).name
        ec2_b = env_context.ec2s.__getitem__(1).name
        len1 = len(ec2_a)
        len2 = len(ec2_b)
        equalLen = len1 == len2
        res = False

        if equalLen:
            flag = 0
            for i in range(len1):
                if ec2_a[i] != ec2_b[i]:
                    if flag == 0:
                        flag = 1
                    else:
                        res = True
                        break
        else:
            if len1 < len2:
                res = self.not_similar(len1, ec2_a, ec2_b)
            else:
                res = self.not_similar(len2, ec2_b, ec2_a)

        if res:
            issues.append(Issue(self.get_expl_issue(), ec2_a, ec2_b))

        return issues

    def not_similar(self, length: int, short: str, long: str) -> bool:
        j = 0
        for i in range(length):
            if short[i] != long[i+j]:
                if j == 0:
                    j = 1
                    if short[i] != long[i+j]:
                        return True
                else:
                    return True

        return False

    def get_id(self) -> str:
        return 'ensure_there_are_no_ec2_with_similar_names_rule'

    def should_run_rule(self, environment_context: AwsEnvironmentContext) -> bool:
        return True

    def get_expl_issue(self):
        return 'the words are not the same'