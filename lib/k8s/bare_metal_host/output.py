class K8sBareMetalHostOutput():
    def __init__(self):
        pass

    def print_bare_metal_hosts_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Bare Metal Host', 'namespace_nameT'],
                ['Provisioning', 'provisioning_state'],
                ['Operational', 'operational_state'],
                ['Online', 'onlineT'],
                ['Power', 'powerT'],
                ['Server', 'serverT']
            ]
        )
