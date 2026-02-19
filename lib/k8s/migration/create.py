import yaml
from lib import ip_helper
from menu.common import get_confirmation


class K8sMigrationCreate():
    def __init__(self):
        pass

    def get_migration_create_body(self, namespace, name, plan):
        body = {}
        body['apiVersion'] = 'forklift.konveyor.io/v1beta1'
        body['kind'] = 'Migration'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}

        body['spec']['plan'] = {}
        body['spec']['plan']['namespace'] = namespace
        body['spec']['plan']['name'] = plan
        return body
    
    def create_migration(self, namespace, plan_name, confirmation=False, my_output=None, wait=True):
        if my_output is None:
            confirmation = False

        name = '%s-%s' % (plan_name, ip_helper.get_short_uuid())
        if my_output is not None:
            my_output.default('Start Migration', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- plan: %s' % (plan_name))
            my_output.default('- migration: %s' % (name))
        
        if self.is_migration(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.error('migration found')
            return False

        plan = self.get_plan(namespace, plan_name, cache_enabled=False)
        if plan is None:
            if my_output is not None:
                my_output.error('plan not found')
            return False
        
        if not plan['start_ready']:
            if my_output is not None:
                my_output.error('plan not ready to start')
            return False
        
        body = self.get_migration_create_body(
            namespace, 
            name,
            plan_name
        )

        if my_output is not None:
            my_output.default(
                yaml.dump(body),
                before_newline=True, 
                wrap='~~~'
            )

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_migration_mo(body):
            if my_output is not None:
                my_output.error('Migration REST API failed')
            return False
                
        if my_output is not None:
            my_output.default('Migration created', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for migration...')

        if not self.wait_migration(namespace, name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        if my_output is not None:
            my_output.default('Wait for migration finished...')

        if not self.wait_migration_finished(namespace, name, my_output=my_output):
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    