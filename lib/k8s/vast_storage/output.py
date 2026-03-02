class K8sVastStorageOutput():
    def __init__(self):
        pass

    def print_vast_storages_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Vast Storage', 'namespace_nameT'],
                ['Init', 'initializedTick'],
                ['Dep', 'deployedTick'],
                ['Spec', 'spec'],
                ['Resource', 'resource.description']
            ],
            cast_dict=True
        )

    def print_vast_storages_manifest(self, info):
        if info is None or len(info) == 0:
            return
        
        for item in info:
            self.my_output.default('Vast Storage Manifest [%s]' % (item['namespace_name']), before_newline=True, underline=True)
            self.my_output.default(item['manifest'], wrap='~~~')
