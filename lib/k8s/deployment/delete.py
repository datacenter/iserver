class K8sDeploymentDelete():
    def __init__(self):
        pass

    def delete_deployment(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Deployment', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_deployment(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        replica_sets = self.get_replica_set_deployments(namespace, name)
        pods = []
        if replica_sets is None:
            my_output.error('replica set rest api failed')
            return False
        
        if len(replica_sets) == 0:
            my_output.default('- no associated replica set')
        else:
            for replica_set in replica_sets:
                my_output.default('- replica set: %s' % (replica_set['name']))
                pods = self.get_pods_replica_set(namespace, replica_set['name'])
                if pods is None:
                    my_output.error('pod rest api failed')
                    return False        

                for pod in pods:
                    my_output.default('- pod: %s' % (pod['name']))

        if not self.delete_deployment_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to deployment service')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no deployment')

            if not self.wait_no_deployment(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

            for replica_set in replica_sets:
                if my_output is not None:
                    my_output.default('- wait for no replica set %s/%s' % (replica_set['namespace'], replica_set['name']))

                if not self.wait_no_replica_set(replica_set['namespace'], replica_set['name']):
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False

            for pod in pods:
                if my_output is not None:
                    my_output.default('- wait for no pod: %s' % (pod['name']))

                if not self.wait_no_pod(pod['namespace'], pod['name']):
                    if my_output is not None:
                        my_output.error('Timed out')
                    return False

        return True
