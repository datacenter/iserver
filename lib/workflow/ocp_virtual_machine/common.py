from menu.common import get_confirmation


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow - Virtual Machine'
    return params


def select_virtual_machines(params, my_output, k8s_output_handler):
    object_filter = []
    if params['namespace'] is not None:
        object_filter.append('namespace:%s' % (params['namespace']))
    if params['name'] is not None:
        object_filter.append('name:%s' % (params['name']))

    virtual_machines = params['k8s_handler'].get_virtual_machines(
        object_filter=object_filter,
        cache_enabled=False
    )

    if virtual_machines is None:
        my_output.error('Failed to get virtual machines')
        return False, None
    
    if len(virtual_machines) == 0:
        my_output.default('No virtual machine found')
        return True, None
    
    k8s_output_handler.print_virtual_machines_state(virtual_machines)

    if params['confirmation']:
        if not get_confirmation():
            return False, None

    return True, virtual_machines


def get_virtual_machine(params, namespace, name, my_output, k8s_output_handler=None, instance=False):
    info = params['k8s_handler'].get_virtual_machine(
        namespace,
        name,
        cache_enabled=False
    )
    if info is None:
        my_output.error('VirtualMachine %s not found' % (params['name']))
        return None
    
    if k8s_output_handler is not None:
        k8s_output_handler.print_virtual_machines_state([info])

    if not instance:
        return info
    
    instance_info = params['k8s_handler'].get_virtual_machine_instance(
        namespace,
        name,
        cache_enabled=False
    )
    if instance_info is None:
        my_output.default('VirtualMachine not running')
        return info
    
    if k8s_output_handler is not None:
        k8s_output_handler.print_virtual_machine_instances_state([instance_info])

    return info