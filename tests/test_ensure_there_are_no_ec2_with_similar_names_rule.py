import unittest

from cloudrail.dev_tools.rule_test_utils import create_empty_entity
from cloudrail.knowledge.context.aws.ec2.ec2_instance import Ec2Instance
from cloudrail.knowledge.context.environment_context import EnvironmentContext
from cloudrail.knowledge.rules.base_rule import RuleResultType

from cloudrail.rules.ensure_there_are_no_ec2_with_similar_names_rule import EnsureThereAreNoEc2WithSimilarNamesRule


class TestEnsureThereAreNoEc2WithSimilarNamesRule(unittest.TestCase):
    def setUp(self):
        self.rule = EnsureThereAreNoEc2WithSimilarNamesRule()

    def test_are_not_similar_fail(self):
        # Arrange
        ec2_1: Ec2Instance = create_empty_entity(Ec2Instance)
        tags_1 = {'name': 'cat'}
        ec2_1.tags = tags_1
        ec2_2: Ec2Instance = create_empty_entity(Ec2Instance)
        tags_2 = {'name': 'dog'}
        ec2_2.tags = tags_2
        context = EnvironmentContext(ec2s=[ec2_1, ec2_2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.FAILED, result.status)
        self.assertEqual(1, len(result.issues))

    def test_are_similar_pass(self):
        # Arrange
        ec2_1: Ec2Instance = create_empty_entity(Ec2Instance)
        tags_1 = {'name': 'god'}
        ec2_1.tags = tags_1
        ec2_2: Ec2Instance = create_empty_entity(Ec2Instance)
        tags_2 = {'name': 'good'}
        ec2_2.tags = tags_2
        context = EnvironmentContext(ec2s=[ec2_1, ec2_2])
        # Act
        result = self.rule.run(context, {})
        # Assert
        self.assertEqual(RuleResultType.SUCCESS, result.status)
        self.assertEqual(0, len(result.issues))
