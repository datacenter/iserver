class K8sClusterPolicyDelete():
    def __init__(self):
        pass

    def delete_cluster_policies(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Cluster Policy', before_newline=True, underline=True)

        policies = self.get_cluster_policies(ds_info=True, cache_enabled=False)
        if policies is None:
            if my_output is not None:
                my_output.error('Failed to get cluster policy information')
            return False
        
        if len(policies) == 0:
            if my_output is not None:
                my_output.default('No cluster policy found')
            return True
        
        for policy in policies:
            if my_output is not None:
                my_output.default('- name: %s' % (policy['name']))

            if not self.delete_cluster_policy_mo(policy['name']):
                if my_output is not None:
                    my_output.error('Failed to delete cluster policy')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no cluster policy')

                if not self.wait_no_cluster_policy(policy['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
                for daemon_set in policy['daemon_sets']:
                    if my_output is not None:
                        my_output.default('- wait for no daemon set %s/%s' % (daemon_set['namespace'], daemon_set['name']))
                    if not self.wait_no_daemon_set(daemon_set['namespace'], daemon_set['name']):
                        if my_output is not None:
                            my_output.error('Time out')
                        return False

        return True
