from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, 'openshift-mtv', 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Storage Map')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    object_filter = []
    if params['namespace'] is not None:
        object_filter.append('namespace:%s' % (params['namespace']))
    if params['name'] is not None:
        object_filter.append('name:%s' % (params['name']))

    maps = params['k8s_handler'].get_storage_maps(
        object_filter=object_filter, 
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get storage maps')
        return False
    
    if len(maps) == 0:
        my_output.default('No storage map defined')
        return True
    
    k8s_output_handler.print_storage_maps_state(maps)

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    used = []
    for smap in maps:
        if len(smap['plan']) > 0:
            used.append(
                smap['namespace_name']
            )

    if len(used) > 0:
        my_output.my_list(
            used,
            title='Storage maps being used and not to be deleted',
            underline=False,
            before_newline=True,
            ending_newline=True
        )

    for smap in maps:
        if len(smap['plan']) > 0:
            continue

        success = params['k8s_handler'].delete_storage_map(
            smap['namespace'], 
            smap['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- selected storage maps deleted')
    if len(used) > 0:
        my_output.default('- storage maps used by migration plans not deleted')

    return True