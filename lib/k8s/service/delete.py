class K8sServiceDelete():
    def __init__(self):
        pass

    def delete_service(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Service', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_service(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_service_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete service')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no service')

            if not self.wait_no_service(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False
            
        return True

    def delete_services(self, object_filter=None, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete services', before_newline=True, underline=True)

        services = self.get_services(
            object_filter=object_filter
        )
        if services is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False

        if len(services) == 0:
            if my_output is not None:
                my_output.default('- no service found')
            return True

        for service in services:
            my_output.default('- %s/%s' % (service['namespace'], service['name']))
            success = self.delete_service_mo(service['namespace'], service['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')

                if wait:
                    if my_output is not None:
                        my_output.default('- wait for no service...')

                    if not self.wait_no_service(service['namespace'], service['name']):
                        if my_output is not None:
                            my_output.error('Timed out')
                        return False
                    
        return True
