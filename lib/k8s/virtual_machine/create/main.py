from lib.k8s.virtual_machine.create.template import K8sVirtualMachineCreateTemplate
from lib.k8s.virtual_machine.create.validate import K8sVirtualMachineCreateValidate


class K8sVirtualMachineCreate(K8sVirtualMachineCreateTemplate, K8sVirtualMachineCreateValidate):
    def __init__(self):
        K8sVirtualMachineCreateTemplate.__init__(self)
        K8sVirtualMachineCreateValidate.__init__(self)

    def create_virtual_machine(
            self, 
            body,
            metadata=None,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if not self.virtual_machine_body_validate(body, my_output=my_output):
            return False
        
        success, created = self.create_resource(body, object_name='virtual_machine', my_output=my_output, confirmation=confirmation)
        if not success:
            return False
        
        if not created:
            return True
        
        if not wait:
            return True
        
        namespace = self.get(body, 'metadata:namespace')
        name = self.get(body, 'metadata:name')

        if metadata is not None:
            if 'dv' in metadata:
                success = self.wait_data_volume_uploaded(
                    metadata['dv']['namespace'],
                    metadata['dv']['name'],
                    max_time=600,
                    my_output=my_output
                )
                if not success:
                    return False

        success = self.wait_virtual_machine(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        info = self.get_virtual_machine(namespace, name, cache_enabled=False)
        if not info['running_expected']:
            return True

        success = self.wait_virtual_machine_up(
            namespace,
            name,
            max_time=360,
            my_output=my_output
        )
        if not success:
            return False
        
        return True