class OcpTaskContainerPolicy():
    def __init__(self):
        pass

    def get_ocp_container_policy_mc(self):
        info = []

        machine_configs = self.k8s_handler.get_machine_configs(
            object_filter=['path:/etc/containers/policy.json']
        )
        for machine_config in machine_configs:
            if len(machine_config['file']) == 0:
                continue

            if machine_config['name'].startswith('rendered-'):
                continue

            if machine_config['name'].endswith('-generated-registries'):
                continue

            info.append(
                machine_config
            )

        return info

    def get_ocp_container_policy_config(self, handlers):
        info = []

        for handler in handlers:
            item = {}
            item['name'] = handler['name']
            item['ip'] = handler['ip']

            container_policy_config = handler['handler'].get_container_policy_config_info()
            if container_policy_config is None:
                continue

            item['config'] = container_policy_config
            info.append(item)

        return info

    def get_ocp_container_policy_info(self, mcp=False, config=False, state=False):
        info = {}

        handlers = self.get_ocp_nodes_linux_handlers()
        if handlers is None:
            return None

        if mcp:
            info['mc'] = self.get_ocp_container_policy_mc()

        if config:
            info['config'] = self.get_ocp_container_policy_config(handlers)

        return info
