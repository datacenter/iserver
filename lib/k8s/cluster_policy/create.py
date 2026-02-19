import yaml
from menu.common import get_confirmation


class K8sClusterPolicyCreate():
    def __init__(self):
        pass

    def create_cluster_policy(
            self, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create NVIDIA Cluster Policy', before_newline=True, underline=True)
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_cluster_policy_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Cluster policy created', before_newline=True, after_newline=True)

        if wait:
            if my_output is not None:
                my_output.default('Wait for cluster policy [timeout:60]...')

            if not self.wait_cluster_policy(body['metadata']['name'], max_time=60):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

            if my_output is not None:
                my_output.default('Wait for cluster policy ready [timeout:180]...')

            if not self.wait_cluster_policy_ready(body['metadata']['name'], max_time=180):
                if my_output is not None:
                    my_output.error('Timed out')
                
                return False

        return True    
