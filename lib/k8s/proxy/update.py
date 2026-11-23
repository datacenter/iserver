class K8sProxyUpdate():
    def __init__(self):
        pass
    
    def set_proxy(
            self, 
            http_proxy=None,
            https_proxy=None,
            no_proxy=None,
            confirmation=False, 
            my_output=None,
            wait=True
        ):
        if my_output is None:
            confirmation = False

        if my_output is not None:
            my_output.default('Configure proxy settings', before_newline=True, underline=True)
            if http_proxy is not None:
                my_output.default('- http proxy: %s' % (http_proxy))
            if https_proxy is not None:
                my_output.default('- https proxy: %s' % (https_proxy))
            if no_proxy is not None:
                my_output.default('- no proxy: %s' % (no_proxy))
            
        proxy_mo = self.get_proxy('cluster', return_mo=True, cache_enabled=False)
        if proxy_mo is None:
            if my_output is not None:
                my_output.error('Proxy settings not found')
            return False

        proxy_mo = self.cleanup_managed_object(proxy_mo, exclude=['resourceVersion'])

        if http_proxy is not None:
            proxy_mo['spec']['httpProxy'] = http_proxy

        if https_proxy is not None:
            proxy_mo['spec']['httpsProxy'] = https_proxy

        if no_proxy is not None:
            proxy_mo['spec']['noProxy'] = no_proxy

        success = self.replace_resource(proxy_mo, object_name='proxy', my_output=my_output, confirmation=confirmation)
        if not success:
            return False

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for desired proxy status...', before_newline=True)

        success = self.wait_proxy_status(
            http_proxy=http_proxy,
            https_proxy=https_proxy,
            no_proxy=no_proxy,
            my_output=my_output,
            max_time=360,
            log_error_on_timeout=True
        )
        return success
