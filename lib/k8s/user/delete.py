class K8sUserDelete():
    def __init__(self):
        pass

    def delete_user(
            self, 
            name, 
            include_identity=True,
            identity=None,
            my_output=None,
            wait=True
        ):
        if my_output is not None:
            my_output.default('Delete user', before_newline=True, underline=True)
            my_output.default('- user: %s' % (name))
            if include_identity:
                my_output.default('- with identities')
                if identity is not None:
                    my_output.default('- incl identity: %s' % (identity))

        info = self.get_user(name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')

            if include_identity and identity is not None:
                success = self.delete_identity(
                    identity,
                    my_output=my_output,
                    wait=wait
                )
                if not success:
                    return True
                
            return True

        success = self.delete_resource(
            'User', 
            'user.openshift.io/v1',
            name, 
            object_name='user',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_user(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        if info is None:
            return True

        if include_identity:
            if identity is not None:
                success = self.delete_identity(
                    identity,
                    my_output=my_output,
                    wait=wait
                )
                if not success:
                    return True

            for user_identity in info['identities']:
                if identity is not None and identity == user_identity:
                    continue

                success = self.delete_identity(
                    user_identity,
                    my_output=my_output,
                    wait=wait
                )
                if not success:
                    return True

        return True