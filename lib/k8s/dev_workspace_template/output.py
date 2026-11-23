class K8sDevWorkspaceTemplateOutput():
    def __init__(self):
        pass

    def print_dev_workspace_templates(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Dev Workspace Template', 'namespace_nameT']
            ]
        )