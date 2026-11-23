class K8sOAuthDelete():
    def __init__(self):
        pass

    def del_identity_provider_oauth(self, provider_name, name='cluster', confirmation=False, my_output=None):
        if my_output is not None:
            my_output.default('Delete identity provider from oauth', before_newline=True, underline=True)
            my_output.default('- oauth: %s' % (name))
            my_output.default('- provider: %s' % (provider_name))

        oauth_mo = self.get_oauth(name, return_mo=True, cache_enabled=False)
        if oauth_mo is None:
            if my_output is not None:
                my_output.error('oauth not found')

            self.log.error(
                'del_identity_provider_oauth',
                'OAuth not found: %s' % (name)
            )
            return False

        if 'identityProviders' not in oauth_mo['spec']:
            if my_output is not None:
                my_output.error('unexpected oauth spec')

            self.log.error(
                'del_identity_provider_oauth',
                'Unexpected oauth: %s' % (name)
            )
            return False

        new_identity_providers = []
        for provider_mo in oauth_mo['spec']['identityProviders']:
            if provider_mo['name'] == provider_name:
                continue
            new_identity_providers.append(
                provider_mo
            )

        oauth_mo = self.cleanup_managed_object(oauth_mo, exclude=['resourceVersion'])
        oauth_mo['spec']['identityProviders'] = new_identity_providers

        oauth_pods = self.get_oauth_pods(cache_enabled=False)
        success = self.replace_resource(oauth_mo, object_name='oauth', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        success = self.wait_oauth_pods_restart(oauth_pods, my_output=my_output)
        return success
