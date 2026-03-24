class K8sVirtualMachineWait():
    def __init__(self):
        pass
           
    def wait_virtual_machine_up(
            self, 
            namespace, 
            name, 
            my_output=None, 
            max_time=60, 
            prompt='VirtualMachine', 
            log_error_on_timeout=True
        ):
        return self.wait_managed_object(
            'virtual_machine',
            name,
            namespace=namespace,
            match_properties=dict(status='Running'),
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            log_error_on_timeout=log_error_on_timeout
        )
    
    def wait_virtual_machine_down(
            self, 
            namespace, 
            name, 
            my_output=None, 
            max_time=60, 
            prompt='VirtualMachine', 
            log_error_on_timeout=True
        ):
        return self.wait_managed_object(
            'virtual_machine',
            name,
            namespace=namespace,
            match_properties=dict(status='Stopped'),
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            log_error_on_timeout=log_error_on_timeout
        )
    
    def wait_virtual_machine_paused(
            self, 
            namespace, 
            name, 
            my_output=None, 
            max_time=60, 
            prompt='VirtualMachine', 
            log_error_on_timeout=True
        ):
        return self.wait_managed_object(
            'virtual_machine',
            name,
            namespace=namespace,
            match_properties=dict(status='Paused'),
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time,
            log_error_on_timeout=log_error_on_timeout
        )

    def wait_virtual_machine(
            self, 
            namespace, 
            name, 
            match_properties={}, 
            break_properties={}, 
            my_output=None, 
            prompt='VirtualMachine', 
            max_time=60
        ):
        return self.wait_managed_object(
            'virtual_machine',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_virtual_machine(
            self, 
            namespace, 
            name, 
            max_time=60, 
            my_output=None, 
            prompt='VirtualMachine'
        ):
        return self.wait_no_managed_object(
            'virtual_machine',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )