import yaml
from menu.common import get_confirmation


class K8sDataScienceClusterCreate():
    def __init__(self):
        pass

    def create_data_science_cluster(self, body, my_output=None, confirmation=False, wait=True):
        if my_output is None:
            confirmation = False

        name = body['metadata']['name']
        if my_output is not None:
            my_output.default('Create Data Science Cluster', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if self.is_data_science_cluster(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
                return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_data_science_cluster_mo(body):
            if my_output is not None:
                my_output.error('DataScienceCluster create failed')
            return False

        if my_output is not None:
            my_output.default('DataScienceCluster created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for data science cluster crd [timeout:60]...')

        if not self.wait_data_science_cluster(name, max_time=30):
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        if my_output is not None:
            my_output.default('Wait for data science cluster ready...')

        success = self.wait_data_science_cluster_ready(name, my_output=my_output)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')
            
            return False

        if my_output is not None:
            my_output.default('Wait for data science cluster resources...')

        return True    