import yaml
from menu.common import get_confirmation


class K8sDeploymentCreate():
    def __init__(self):
        pass

    def get_deployment_resources_body(self, rcpu, lcpu, rmem, lmem):
        body = {}
        body['requests'] = {}
        body['requests']['cpu'] = rcpu
        body['requests']['memory'] = rmem
        body['limits'] = {}
        body['limits']['cpu'] = lcpu
        body['limits']['memory'] = lmem
        return body

    def get_deployment_secontext_body(self, escalation=False, privileged=False, ro_rootfs=True, drop_all_caps=True):
        body = {}
        body['securityContext'] = {}
        body['securityContext']['allowPrivilegeEscalation'] = escalation
        body['securityContext']['privileged'] = privileged
        body['securityContext']['readOnlyRootFilesystem'] = ro_rootfs
        if drop_all_caps:
            body['securityContext']['capabilities'] = {}
            body['securityContext']['capabilities']['drop'] = ['all']
        return body

    def create_deployment(
            self, 
            namespace, 
            name, 
            body,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Create Deployment', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))            

        if self.is_deployment(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already exists')
            return True

        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False

        if not self.create_deployment_mo(body):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait until deployment found [timeout:60s]...')

        success = self.wait_deployment(namespace, name, max_time=60)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        if my_output is not None:
            my_output.default('Wait until deployment resources [timeout:60s]...')

        success = self.wait_deployment_ready_state(namespace, name)
        if not success:
            if my_output is not None:
                my_output.error('Timed out')                
            return False

        return True
