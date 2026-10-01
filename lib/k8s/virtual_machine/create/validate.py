class K8sVirtualMachineCreateValidate():
    def __init__(self):
        pass

    def virtual_machine_body_validate(self, body, my_output=None):
        kind = self.get(body, 'kind')
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        if kind is None or kind != 'VirtualMachine':
            if my_output is not None:
                my_output.error('kind VirtualMachine required')
            return False
        
        if namespace is None:
            if my_output is not None:
                my_output.error('metadata:namespace required')
            return False
        
        if name is None:
            if my_output is not None:
                my_output.error('metadata:name required')
            return False

        return True