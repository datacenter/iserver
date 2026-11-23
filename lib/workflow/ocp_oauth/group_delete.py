from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['group', True, None, 'str', None, None, None, None],
        ['ldap_host', True, None, 'str', None, None, None, None],
        ['ldap', True, False, 'bool', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Delete Group')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    object_filter = []
    if params['group'] is not None:
        object_filter.append('name:%s' % (params['group']))
    if params['ldap']:
        object_filter.append('ldap:true')
    if params['ldap_host'] is not None:
        object_filter.append('ldap_host:%s' % (params['ldap_host']))

    groups = params['k8s_handler'].get_groups(object_filter=object_filter, cache_enabled=False)
    if groups is None:
        my_output.error('rest api failed')
        return False
    
    if len(groups) == 0:
        my_output.default('No groups found')
        return True
    
    k8s_output_handler.print_groups_state(groups)

    if params['confirmation']:
        if not get_confirmation():
            return True
    
    for group in groups:
        success = params['k8s_handler'].delete_group(
            group['name'], 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Selected groups deleted')
    
    return True
