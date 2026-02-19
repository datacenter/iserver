import yaml
from menu.common import get_confirmation


class K8sHyperConvergedPatch():
    def __init__(self):
        pass

    def get_hyperconverged_patch_body(self, my_output=None):
        hyperconverged_mo = self.get_hyperconverged(return_mo=True, cache_enabled=False)
        if hyperconverged_mo is None:
            if my_output is not None:
                my_output.error('Failed to get hyperconverged CR')
            return None
        
        body = {}
        body['apiVersion'] = hyperconverged_mo['apiVersion']
        body['kind'] = hyperconverged_mo['kind']
        body['metadata'] = {}
        body['metadata']['namespace'] = hyperconverged_mo['metadata']['namespace']
        body['metadata']['name'] = hyperconverged_mo['metadata']['name']
        body['spec'] = {}

        return body

    def disable_hyperconverged_boot_image_import(self, confirmation=False, my_output=None):
        body = self.get_hyperconverged_patch_body(my_output=my_output)
        if body is None:
            return False
        
        body['spec']['featureGates'] = {}
        body['spec']['featureGates']['enableCommonBootImageImport'] = False

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
            
        if not self.patch_hyperconverged_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('HyperConverged boot image import disabled', before_newline=True, after_newline=True)

        return True

    def enable_hyperconverged_boot_image_import(self, confirmation=False, my_output=None):
        body = self.get_hyperconverged_patch_body(my_output=my_output)
        if body is None:
            return False
        
        body['spec']['featureGates'] = {}
        body['spec']['featureGates']['enableCommonBootImageImport'] = True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False
            
        if not self.patch_hyperconverged_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('HyperConverged boot image import enabled', before_newline=True, after_newline=True)

        return True
    