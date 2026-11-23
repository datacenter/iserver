class K8sNimServiceDelete():
    def __init__(self):
        self.nim_service = None

    def delete_nim_services(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete nim service', before_newline=True, underline=True)

        servings = self.get_nim_services(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get nim service')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no nim service found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_nim_service_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('nim service delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no nim service')

                if not self.wait_no_nim_service(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
