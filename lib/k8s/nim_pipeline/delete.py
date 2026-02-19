class K8sNimPipelineDelete():
    def __init__(self):
        self.nim_pipeline = None

    def delete_nim_pipelines(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete nim pipeline', before_newline=True, underline=True)

        servings = self.get_nim_pipelines(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get nim pipeline')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no nim pipeline found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_nim_pipeline_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('nim pipeline delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nim pipeline')

                if not self.wait_no_nim_pipeline(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
