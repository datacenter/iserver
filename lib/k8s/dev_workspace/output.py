class K8sDevWorkspaceOutput():
    def __init__(self):
        pass

    def print_dev_workspaces(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Dev Workspace', 'namespace_nameT'],
                ['Ready', 'readyTick']
            ]
        )