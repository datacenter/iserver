class K8sServiceMonitorDelete():
    def __init__(self):
        pass

    def delete_service_monitor(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Service Monitor', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_service_monitor(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_service_monitor_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete service monitor')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no service monitor')

            if not self.wait_no_service_monitor(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True
