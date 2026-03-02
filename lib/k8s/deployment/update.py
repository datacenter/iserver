import yaml
import datetime
from menu.common import get_confirmation


class K8sDeploymentUpdate():
    def __init__(self):
        pass

    def restart_deployment(self, namespace, name, my_output=None):
        if not self.is_deployment(namespace, name, cache_enabled=False):
            if my_output is not None:
                my_output.error('Deployment [%s/%s] not found' % (namespace, name))
            return False

        now = datetime.datetime.utcnow()
        now = str(now.isoformat("T") + "Z")
        body = {
            'spec': {
                'template':{
                    'metadata': {
                        'annotations': {
                            'kubectl.kubernetes.io/restartedAt': now
                        }
                    }
                }
            }
        }

        if not self.path_resource(body):
            if my_output is not None:
                my_output.error('Deployment [%s/%s] patch failed' % (namespace, name))
            return False

        if my_output is not None:
            my_output.default('Deployment [%s/%s] patch successful' % (namespace, name))

        return True

    def get_deployment_replica_patch_body(self, namespace, name, replicas):
        body = {}
        body['apiVersion'] = 'apps/v1'
        body['kind'] = 'Deployment'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['replicas'] = replicas
        return body
    
    def set_deployment_replicas(
            self, 
            namespace,
            name,
            replicas,
            confirmation=False, 
            my_output=None,
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Configure deployment replicas', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))
            my_output.default('- replicas: %s' % (replicas))
            
        deployment_mo = self.get_deployment(namespace, name, return_mo=True)
        if deployment_mo is None:
            if my_output is not None:
                my_output.error('Deployment not found')
            return False

        replica_set = self.get_replica_set_deployment(namespace, name)
        if replica_set is None:
            if my_output is not None:
                my_output.error('Network operator replica set not found')
            return False

        body = self.get_deployment_replica_patch_body(namespace, name, replicas)
        if my_output is not None:
            my_output.default(yaml.dump(body), before_newline=True, wrap='~~~')

        if confirmation:
            if not get_confirmation():
                return False     

        success = self.patch_resource(body)
        if not success:
            if my_output is not None:
                my_output.error('patch failed')
            return False
        
        if my_output is not None:
            my_output.default('Patch successful')

        if wait:
            if my_output is not None:
                my_output.default('Wait for desired replica pods...', before_newline=True)
            
            object_filter = []
            object_filter.append('namespace:%s' % (namespace))
            object_filter.append('owner:ReplicaSet/%s' % (replica_set['name']))
            success = self.wait_pods_count(
                object_filter,
                replicas
            )
            if not success:
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True    
