import yaml
from menu.common import get_confirmation


class K8sPlanDelete():
    def __init__(self):
        pass

    def get_plan_archive_body(self, namespace, name):
        body = {}
        body['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        body['kind'] = 'Plan'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['archived'] = True
        return body

    def delete_plan(self, namespace, name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Delete Migration Plan', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_plan(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.error('not found')
            return False

        if my_output is not None:
            my_output.default('- state: %s' % (info['state']))

        if confirmation:
            if not get_confirmation():
                return False
        
        if 'Archived' not in info['conditions']:
            body = self.get_plan_archive_body(namespace, name)
            if my_output is not None:
                my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

            success = self.patch_plan_mo(body)
            if not success:
                if my_output is not None:
                    my_output.error('rest api failed')
                return False
            
            if my_output is not None:
                my_output.default('Migration plan patched', before_newline=True)
                my_output.default('Wait for plan archived...')

            if not self.wait_plan_archived(namespace, name):
                if my_output is not None:
                    my_output.error('timed out')
                return False
            
        success = self.delete_plan_mo(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('rest api failed')
            return False
        
        if my_output is not None:
            my_output.default('Migration plan deleted', before_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for migration plan gone')

        success = self.wait_no_plan(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('timed out')
            return False
        
        return success
    