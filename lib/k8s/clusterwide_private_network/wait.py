class K8sClusterwidePrivateNetworkWait():
    def __init__(self):
        pass

    def wait_clusterwide_private_network_webhook(self, max_time=60):
        return self.wait_mutating_webhook(self.pnet_webhook_name, max_time=max_time)

    def wait_no_clusterwide_private_network_webhook(self, max_time=60):
        return self.wait_no_mutating_webhook(self.pnet_webhook_name, max_time=max_time)

    def wait_clusterwide_private_network(self, name, my_output=None, prompt='ClusterwidePrivateNetwork', max_time=60):
        return self.wait_managed_object(
            'clusterwide_private_network',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_clusterwide_private_network(self, name, my_output=None, prompt='ClusterwidePrivateNetwork', max_time=60):
        return self.wait_no_managed_object(
            'clusterwide_private_network',
            name,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
        