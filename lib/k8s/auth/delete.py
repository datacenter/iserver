class K8sAuthDelete():
    def __init__(self):
        pass

    def delete_auths(self, my_output=None, wait=True):
        clusters = self.get_auths(
            cache_enabled=False
        )
        if clusters is None:
            if my_output is not None:
                my_output.default('Delete Auth', before_newline=True, underline=True)
                my_output.error('Failed to get auths')
            return False

        if len(clusters) == 0:
            if my_output is not None:
                my_output.default('Delete Auth', before_newline=True, underline=True)
                my_output.default('- no record found')
            return True
        
        for cluster in clusters:
            success = self.delete_auth(cluster['name'])
            if not success:
                return False
            
        return True

    def delete_auth(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Auth', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        if not self.is_auth(name, cache_enabled=False):
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        success = self.delete_auth_mo(
            name
        )
        if not success:
            if my_output is not None:
                my_output.error('Auth delete failed')

            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no auth')

            if not self.wait_no_auth(name):
                if my_output is not None:
                    my_output.error('Time out')
                return False
            
        return True
    