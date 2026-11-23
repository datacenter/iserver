class K8sVastDriverOutput():
    def __init__(self):
        pass

    def print_vast_drivers_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Vast Driver', 'namespace_nameT'],
                ['Init', 'initializedTick'],
                ['Dep', 'deployedTick'],
                ['Spec', 'spec'],
                ['Resource', 'resource.description'],
                ['Vast Storage', 'storage']
            ],
            cast_dict=True
        )

    def print_vast_drivers_manifest(self, info):
        if info is None or len(info) == 0:
            return
        
        for item in info:
            self.my_output.default('Vast Driver Manifest [%s]' % (item['namespace_name']), before_newline=True, underline=True)
            self.my_output.default(item['manifest'], wrap='~~~')
