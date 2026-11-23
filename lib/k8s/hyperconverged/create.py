import yaml
from menu.common import get_confirmation


class K8sHyperConvergedCreate():
    def __init__(self):
        pass

    def create_hyperconverged(self, body, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create HyperConverged Instance', before_newline=True, underline=True)

        if self.is_hyperconverged(cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True
        
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        success, _ = self.create_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('HyperConverged instance created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for hyperconverged instance and resources...')

        if not self.wait_instance_cnv_ready(my_output=my_output):
            return False

        return True    
