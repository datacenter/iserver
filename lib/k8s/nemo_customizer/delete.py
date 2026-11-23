class K8sNemoCustomizerDelete():
    def __init__(self):
        self.nemo_customizer = None

    def delete_nemo_customizers(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete nim build', before_newline=True, underline=True)

        servings = self.get_nemo_customizers(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get nim build')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no nim build found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_nemo_customizer_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('nim build delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nim build')

                if not self.wait_no_nemo_customizer(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
