import json


class K8sNamespaceDelete():
    def __init__(self):
        self.namespace_resource_keys = ['deployment', 'daemon_set', 'replica_set', 'pod', 'service', 'pvc', 'job']

    def get_namespace_usage(self, namespace, keys):
        usage = {}

        object_filter=['namespace:%s' % (namespace)]
        if 'pod' in keys:
            usage['pod'] = self.get_pods(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'deployment' in keys:
            usage['deployment'] = self.get_deployments(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'daemon_set' in keys:
            usage['daemon_set'] = self.get_daemon_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'replica_set' in keys:
            usage['replica_set'] = self.get_replica_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'service' in keys:
            usage['service'] = self.get_services(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'pvc' in keys:
            usage['pvc'] = self.get_pvcs(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'job' in keys:
            usage['job'] = self.get_jobs(object_filter=object_filter, return_mo=False, cache_enabled=False)

        if 'user_defined_networks' in keys:
            usage['user_defined_networks'] = self.get_namespace_udns(namespace, cache_enabled=False)

        if 'cluster_user_defined_networks' in keys:
            usage['cluster_user_defined_networks'] = self.get_namespace_cudns(namespace, cache_enabled=False)

        return usage
    
    def check_namespace_usage(self, namespace, my_output=None, k8s_output_handler=None, show_details=False, underline=False, before_newline=True, extras=[]):
        if my_output is not None:
            my_output.default('Namespace [%s] resources' % (namespace), underline=underline, before_newline=before_newline)
        
        keys = self.namespace_resource_keys + extras
        usage = self.get_namespace_usage(namespace, keys)
        used = False

        for key in keys:
            if usage[key] is None:
                my_output.default('- %s get %s' % (key, my_output.add_color('failed', 'Red')))
                continue

            if len(usage[key]) == 0:
                my_output.default('- no %ss' % (key))
                continue

            my_output.default('- %ss [%s]' % (key, len(usage[key])))
            used = True

        if show_details:
            for key in keys:
                if usage[key] is None:
                    continue

                if len(usage[key]) == 0:
                    continue
            
                getattr(k8s_output_handler, 'print_%ss_state' % (key))(usage[key])

        return used
    
    def wipe_namespace_resources(self, namespace, keys=None, extras=[], my_output=None, confirmation=False):
        if keys is None:
            keys = self.namespace_resource_keys

        keys = keys + extras

        usage = self.get_namespace_usage(namespace, keys)
        for key in usage:
            if usage[key] is None:
                continue

            if len(usage[key]) == 0:
                continue

            for item in usage[key]:
                success = getattr(self, 'delete_%s' % (key))(namespace, item['name'], my_output=my_output)
                if not success:
                    return False
                
        return True
    
    def remove_namespace_finalizers(self, namespace, my_output=None):
        if my_output is not None:
            my_output.default('Remove namespace finalizers')

        namespace_mo = self.get_namespace(namespace, return_mo=True, cache_enabled=False)
        if namespace_mo is None:
            if my_output is not None:
                my_output.error('Failed to get namespace')
            return False
        
        if 'finalizers' not in namespace_mo['spec']:
            if my_output is not None:
                my_output.default('No finalizers found')
            return True
        
        del namespace_mo['spec']['finalizers']
        success = self.finalize_namespace_mo(namespace_mo)
        if success:
            if my_output is not None:
                my_output.default('Namespace replace %s' % (my_output.add_color('successful', 'Green')))
        else:
            if my_output is not None:
                my_output.default('Namespace replace %s' % (my_output.add_color('failed', 'Red')))
    
        return success

    def delete_namespace(self, namespace, my_output=None, check_usage=True, wait=True, finalizers=False):
        if my_output is not None:
            my_output.default('Delete Namespace', before_newline=True, underline=True)
            my_output.default('- name: %s' % (namespace))

        info = self.get_namespace(namespace)
        if info is None:
            if my_output is not None:
                my_output.default('Namespace %s' % (my_output.add_color('already deleted', 'Green')), before_newline=True)
            return True
    
        if check_usage:
            used = self.check_namespace_usage(
                namespace, 
                my_output=my_output, 
                show_details=False,
                underline=False
            )
            if used:
                if my_output is not None:
                    my_output.error('Namespace used and cannot be deleted')

                return False

        if info['phase'] == 'Terminating':
            my_output.default('Namespace is already being deleted (phase:Terminating)...')
        else:
            success = self.delete_namespace_mo(namespace)
            if not success:
                if my_output is not None:
                    my_output.error('Delete API failed')
                return False

        if not wait:
            return True
        
        if self.wait_no_namespace(namespace, my_output=my_output):
            return True
        
        problem_mo = {}
        finalizers_mo = self.get(info, 'spec:finalizers')
        if finalizers_mo is not None:
            problem_mo['spec'] = {}
            problem_mo['spec']['finalizers'] = finalizers_mo

        if len(info['faults']) > 0:
            problem_mo['status'] = {}
            problem_mo['status']['conditions'] = info['faults']

        if my_output is not None and len(problem_mo) > 0:
            my_output.default(json.dumps(problem_mo, indent=4), wrap='~~~')

        if finalizers_mo is None:
            return False
        
        if not finalizers:
            if my_output is not None:
                my_output.default('Finalizers auto removal disabled')

            return False

        if not self.remove_namespace_finalizers(namespace, my_output=my_output):
            return False
        
        if not self.wait_no_namespace(namespace, my_output=my_output):
            if my_output is not None:
                my_output.error('Giving up')

            return False

        return True