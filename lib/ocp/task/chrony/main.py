class OcpTaskChrony():
    def __init__(self):
        pass

    def get_ocp_chrony_mc(self):
        info = []

        machine_configs = self.k8s_handler.get_machine_configs(
            object_filter=['path:/etc/chrony.conf']
        )
        for machine_config in machine_configs:
            if len(machine_config['file']) == 0:
                continue

            if machine_config['name'].startswith('rendered-'):
                continue

            info.append(
                machine_config
            )

        return info

    def get_ocp_chrony_config(self, handlers):
        info = []

        for handler in handlers:
            item = {}
            item['name'] = handler['name']
            item['ip'] = handler['ip']

            chrony_config = handler['handler'].get_chrony_config_info()
            if chrony_config is None:
                continue

            item['config'] = chrony_config['configuration']
            info.append(item)

        return info

    def get_ocp_chrony_state(self, handlers):
        info = []

        for handler in handlers:
            item = {}
            item['name'] = handler['name']
            item['ip'] = handler['ip']

            chrony_state = handler['handler'].get_chrony_tracking_info()
            if chrony_state is None:
                continue

            for key in chrony_state:
                item[key] = chrony_state[key]

            info.append(item)

        return info

    def get_ocp_chrony_info(self, mcp=False, config=False, state=False):
        info = {}

        handlers = self.get_ocp_nodes_linux_handlers()
        if handlers is None:
            return None

        if mcp:
            info['mc'] = self.get_ocp_chrony_mc()

        if config:
            info['config'] = self.get_ocp_chrony_config(handlers)

        if state:
            info['state'] = self.get_ocp_chrony_state(handlers)

        return info
