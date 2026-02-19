class K8sPolicyBindingDelete():
    def __init__(self):
        self.policy_binding = None

    def delete_policy_bindings(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete policy binding', before_newline=True, underline=True)

        servings = self.get_policy_bindings(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get policy binding')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no policy binding found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_policy_binding_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('policy binding delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no policy binding')

                if not self.wait_no_policy_binding(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
