class K8sForkliftControllerOutput():
    def __init__(self):
        pass

    def print_forklift_controllers(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['ForkliftController', 'namespace_nameT']
            ]
        )