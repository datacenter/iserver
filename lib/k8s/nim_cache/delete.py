class K8sNimCacheDelete():
    def __init__(self):
        self.nim_cache = None

    def delete_nim_caches(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete nim cache', before_newline=True, underline=True)

        servings = self.get_nim_caches(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get nim cache')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no nim cache found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_nim_cache_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('nim cache delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nim cache')

                if not self.wait_no_nim_cache(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
