import time
import yaml
from lib import filter_helper


class K8sInstallplanApprove():
    def __init__(self):
        pass

    def approve_installplan(self, namespace, name, my_output=None, confirmation=False):
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1alpha1'
        body['kind'] = 'InstallPlan'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['approved'] = True

        if not self.patch_resource(body, object_name='installplan', my_output=my_output, confirmation=confirmation):
            return False

        return True
    