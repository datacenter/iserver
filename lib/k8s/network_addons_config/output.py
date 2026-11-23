class K8sNetworkAddonsConfigOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_network_addons_configs(self, info):
        if info is None:
            return

        if len(info) == 0:
            self.my_output.default('No network addons config', before_newline=True)
            return 
                
        for item in info:
            self.print_network_addons_config(item)

    
    def print_network_addons_config(self, item):
        self.my_output.dictionary_ng(
            'Network Addons Config',
            item, 
            [
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['Ready', 'readyTick']
            ]
        )
