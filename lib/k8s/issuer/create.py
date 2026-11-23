import time
import yaml
from lib import filter_helper
from menu.common import get_confirmation


class K8sIssuerCreate():
    def __init__(self):
        pass

    def get_issuer_body(self, namespace, name, secret_name):
        body = {}
        body['apiVersion'] = 'cert-manager.io/v1'
        body['kind'] = 'Issuer'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['ca'] = {}
        body['spec']['ca']['secretName'] = secret_name
        return body

    def create_issuer(self, namespace, name, secret_name, confirmation=False, my_output=None, wait=True):
        body = self.get_issuer_body(
            namespace,
            name,
            secret_name
        )

        success, _ = self.create_resource(body, object_name='issuer', my_output=my_output, confirmation=confirmation)
        if not success:
            return False

        if not wait:
            return True

        success = self.wait_issuer(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True