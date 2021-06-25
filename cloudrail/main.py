import json
from typing import List

from cloudrail.entities.ec2 import Ec2

def load_instances(cloud_json_data) -> List[Ec2]:
    # TODO: Part 1.a -  given a json object, parse it to a list of ec2
    res = []
    keys = []
    for instance in cloud_json_data['Instances']:
        d = {}
        for i, v in instance.items():
            d[i] = v
            keys.append(i)
        res.append(d)

    return res

def get_ec2_contains_production_tag(ec2s: List[Ec2]) -> List[Ec2]:
    # TODO: Part 1.b - find all ec2s that have tag environment=production
    res = []
    for ec2 in ec2s:
        for tag in ec2['Tags']:
            if (tag['Key'] == 'environment') and (tag['Value'] == 'production'):
                res.append(ec2)

    return res

def main():
    cloud_json_data_file = 'cloud-data/ec2-describe-instances.json'
    with open(cloud_json_data_file, 'r') as json_file:
        cloud_json_data = json.load(json_file)

    ec2s: List[Ec2] = load_instances(cloud_json_data)

    ec2s_with_issue = get_ec2_contains_production_tag(ec2s)
    print('Found {} ec2s with issues'.format(len(ec2s_with_issue)))


if __name__ == '__main__':
    main()
