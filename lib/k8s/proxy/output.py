class K8sProxyOutput():
    def __init__(self):
        pass

    def print_proxy(self, info):
        self.my_output.default('Http Proxy: %s' % (info['http_proxy']))
        self.my_output.default('Htps Proxy: %s' % (info['https_proxy']))
        self.my_output.default('No Proxy: %s' % (info['no_proxy']))
        