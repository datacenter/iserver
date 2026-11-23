class K8sCdiConfigOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_cdi_configs(self, info):
        if info is None:
            return

        if len(info) == 0:
            self.my_output.default('No cdi config', before_newline=True)
            return 
                
        for item in info:
            self.print_cdi_config(item)

    
    def print_cdi_config(self, item):
        self.my_output.dictionary_ng(
            'Containerized Data Importer (CDI) Config',
            item, 
            [
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['HTTP Proxy', 'status.importProxy.HTTPProxy'],
                ['HTTPs Proxy', 'status.importProxy.HTTPSProxy'],
                ['No Proxy', 'status.importProxy.noProxy'],
                ['Upload Proxy URL', 'status.uploadProxyURL'],
                ['POD CPU Limits (Default)', 'status.defaultPodResourceRequirements.limits.cpu'],
                ['POD Memory Limits (Default)', 'status.defaultPodResourceRequirements.limits.memory'],
                ['POD CPU Requests (Default)', 'status.defaultPodResourceRequirements.requests.cpu'],
                ['POD Memory Requests (Default)', 'status.defaultPodResourceRequirements.requests.memory']
            ]
        )
