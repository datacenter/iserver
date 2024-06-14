class LinuxContainerPolicyCmd():
    def __init__(self):
        self.container_policy_config_cmd = None

    def get_container_policy_config_cmd(self):
        if self.container_policy_config_cmd is not None:
            return self.container_policy_config_cmd

        cache = self.get_cmd_cache(
            'container_policy.conf'
        )
        if cache is not None:
            self.container_policy_config_cmd = cache
            return self.container_policy_config_cmd

        filename = '/etc/containers/policy.json'
        container_policy_config = self.ssh_handler.get_file(
            filename
        )
        if container_policy_config is None:
            self.log.debug(
                'get_container_policy_config_cmd',
                'No container_policy configuration file: %s' % (filename)
            )
            return None

        self.container_policy_config_cmd = container_policy_config
        return self.container_policy_config_cmd
