class K8sNamespaceDelete():
    def __init__(self):
        pass

    def check_namespace_usage_and_state(self, namespace, my_output=None, show_details=False, underline=False, before_newline=True):
        used = False

        if my_output is not None:
            my_output.default('Namespace [%s] resources' % (namespace), underline=underline, before_newline=before_newline)
        
        object_filter = ['namespace:%s' % (namespace)]

        pods = self.get_pods(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to check pod')

        if pods is not None:
            if len(pods) == 0:
                if my_output is not None:
                    my_output.default('- no pods')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- pod')
                        for pod in pods:
                            my_output.default(
                                '\t[%s] [%s] [%s]' % (
                                    pod['namespace_name'], 
                                    pod['container_state_summary'],
                                    my_output.add_color(pod['phaseT'], pod['__Output']['phaseT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- pods [%s]' % (len(pods)))

        deployments = self.get_deployments(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if deployments is None:
            if my_output is not None:
                my_output.error('Failed to check deployment')

        if deployments is not None:
            if len(deployments) == 0:
                if my_output is not None:
                    my_output.default('- no deployments')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- deployment')
                        for deployment in deployments:
                            my_output.default(
                                '\t[%s] [%s]' % (
                                    deployment['namespace_name'], 
                                    my_output.add_color(deployment['readyT'], deployment['__Output']['readyT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- deployments [%s]' % (len(deployments)))

        daemon_sets = self.get_daemon_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if daemon_sets is None:
            if my_output is not None:
                my_output.error('Failed to check daemon set')

        if daemon_sets is not None:
            if len(daemon_sets) == 0:
                if my_output is not None:
                    my_output.default('- no daemon sets')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- daemon set')
                        for daemon_set in daemon_sets:
                            my_output.default(
                                '\t[%s] Scheduled [%s] Available [%s]' % (
                                    daemon_set['namespace_name'], 
                                    my_output.add_color(daemon_set['scheduled_summary'], daemon_set['__Output']['scheduled_summary']),
                                    my_output.add_color(daemon_set['available_summary'], daemon_set['__Output']['available_summary'])
                                )
                            )

                    if not show_details:
                        my_output.default('- daemon sets [%s]' % (len(daemon_sets)))

        replica_sets = self.get_replica_sets(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if replica_sets is None:
            if my_output is not None:
                my_output.error('Failed to check replica set')

        if replica_sets is not None:
            if len(replica_sets) == 0:
                if my_output is not None:
                    my_output.default('- no replica sets')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- replica set')
                        for replica_set in replica_sets:
                            my_output.default(
                                '\t[%s] [%s]' % (
                                    replica_set['namespace_name'], 
                                    my_output.add_color(replica_set['replicasT'], replica_set['__Output']['replicasT'])
                                )
                            )

                    if not show_details:
                        my_output.default('- replica sets [%s]' % (len(replica_sets)))

        services = self.get_services(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if services is None:
            if my_output is not None:
                my_output.error('Failed to check service')

        if services is not None:
            if len(services) == 0:
                if my_output is not None:
                    my_output.default('- no services')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- service')
                        for service in services:
                            my_output.default(
                                '\t[%s] [%s] [%s]' % (
                                    service['namespace_name'], 
                                    service['type'], 
                                    service['ports']
                                )
                            )

                    if not show_details:
                        my_output.default('- services [%s]' % (len(services)))

        pvcs = self.get_pvcs(object_filter=object_filter, return_mo=False, cache_enabled=False)
        if pvcs is None:
            if my_output is not None:
                my_output.error('Failed to check pvc')

        if pvcs is not None:
            if len(pvcs) == 0:
                if my_output is not None:
                    my_output.default('- no pvcs')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- pvc')
                        for pvc in pvcs:
                            my_output.default(
                                '\t[%s]' % (
                                    pvc['namespace_name']
                                )
                            )

                    if not show_details:
                        my_output.default('- pvc [%s]' % (len(pvcs)))

        namespace_udns = self.get_namespace_udns(namespace, cache_enabled=False)
        if namespace_udns is not None:
            if len(namespace_udns) == 0:
                if my_output is not None:
                    my_output.default('- no user defined networks')
            else:
                used = True
                if my_output is not None:
                    if show_details:
                        my_output.default('- user defined network')
                        for namespace_udn in namespace_udns:
                            my_output.default(
                                '\t[%s]' % (
                                    namespace_udn
                                )
                            )

                    if not show_details:
                        my_output.default('- user defined network [%s]' % (len(namespace_udns)))

        return used
    
    def remove_namespace_finalizers(self, namespace):
        namespace_mo = self.get_namespace(namespace, return_mo=True, cache_enabled=False)
        if namespace_mo is None:
            return False
        
        if 'finalizers' not in namespace_mo['spec']:
            return True
        
        del namespace_mo['spec']['finalizers']
        return self.set_namespace_mo(namespace_mo)
    
    def delete_namespace(self, namespace, my_output=None, check_usage=True, wait=True, finalizers=False):
        if my_output is not None:
            my_output.default('Delete Namespace', before_newline=True, underline=True)
            my_output.default('- name: %s' % (namespace))

        if not self.is_namespace(namespace):
            if my_output is not None:
                my_output.default('- already deleted')
            return True
    
        if check_usage:
            used = self.check_namespace_usage_and_state(
                namespace, 
                my_output=my_output, 
                show_details=True,
                underline=False
            )
            if used:
                if my_output is not None:
                    my_output.error('Namespace used and cannot be deleted')

                return False
    
        success = self.delete_namespace_mo(namespace)
        if not success:
            if my_output is not None:
                my_output.error('Delete API failed')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no namespace')

            if not self.wait_no_namespace(namespace):
                if my_output is not None:
                    my_output.error('Timed out')

                if not finalizers:
                    return False
                
                if my_output is not None:
                    my_output.default('Remove finalizers')

                if not self.remove_namespace_finalizers(namespace):
                    if my_output is not None:
                        my_output.error('REST API failed')
                    return False
                
                if not self.wait_no_namespace(namespace):
                    if my_output is not None:
                        my_output.error('Giving up')

                    return False

        return True
