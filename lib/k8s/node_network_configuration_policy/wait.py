import time


class K8sNodeNetworkConfigurationPolicyWait():
    def __init__(self):
        pass

    def wait_node_network_configuration_policy(self, name, match_properties={}, break_properties={}, my_output=None, prompt='NodeNetworkConfigurationPolicy', max_time=360):
        return self.wait_managed_object(
            'node_network_configuration_policy',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_node_network_configuration_policy(self, name, my_output=None, prompt='NodeNetworkConfigurationPolicy', max_time=360):
        return self.wait_no_managed_object(
            'node_network_configuration_policy',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_node_network_configuration_policies_status(self, policy_names=None, max_time=1800, log_error_on_timeout=True, my_output=None):
        start_time = int(time.time())
        while True:
            policies = self.get_node_network_configuration_policies(cache_enabled=False)
            if policies is not None:
                pending = []
                for policy in policies:
                    if policy_names is None or policy['name'] in policy_names:
                        if policy['status'] not in ['Available', 'Degraded']:
                            pending.append(
                                policy['name']
                            )

                if len(pending) == 0:
                    return True

                if my_output is not None:
                    my_output.default(
                        'Waiting for [%s]: %s' % (
                            len(pending),
                            ', '.join(pending)
                        )
                    )

            duration = int(time.time()) - start_time
            if duration > max_time:
                if log_error_on_timeout:
                    self.log.error(
                        'k8s.wait_node_network_configuration_policy',
                        'Max time reached'
                    )
                return False

            time.sleep(10)
