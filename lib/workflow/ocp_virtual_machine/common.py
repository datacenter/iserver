import json
import copy
from lib.workflow.ocp_access import check as ocp_check
from menu.common import get_confirmation
from lib.workflow import ocp_common


def initialize(params, my_output, log_id, virtctl=False):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-required'] = virtctl
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    if virtctl:
        params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id=log_id)
        
    return params

def get_default_params():
    params = {}
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


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
    
    k8s_output_handler.print_virtual_machines(virtual_machines)

    if params['confirmation']:
        if not get_confirmation():
            return False, None

    return True, virtual_machines
