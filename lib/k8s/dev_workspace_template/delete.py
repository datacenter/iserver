class K8sDevWorkspaceTemplateDelete():
    def __init__(self):
        pass

    def delete_dev_workspace_templates(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete workspace templates', before_newline=True, underline=True)

        servings = self.get_dev_workspace_templates(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.default('- failed to get workspace template <=> CRD not installed')
            return True

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no workspace template found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_dev_workspace_template_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('workspace template delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no workspace template')

                if not self.wait_no_dev_workspace_template(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
