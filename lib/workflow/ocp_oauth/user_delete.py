from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['user', True, None, 'str', None, None, None, None],
        ['group', True, None, 'str', None, None, None, None],
        ['provider', True, None, 'str', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Delete User')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    object_filter = []
    if params['user'] is not None:
        object_filter.append('name:%s' % (params['user']))

    if params['group'] is not None:
        object_filter.append('group:%s' % (params['group']))

    if params['provider'] is not None:
        object_filter.append('provider:%s' % (params['provider']))

    users = params['k8s_handler'].get_users(object_filter=object_filter, cache_enabled=False)
    if users is None:
        my_output.error('rest api failed')
        return False
    
    if len(users) == 0:
        my_output.default('No users found')
        return True
    
    k8s_output_handler.print_users_state(users)

    if params['confirmation']:
        if not get_confirmation():
            return True
    
    for user in users:
        success = params['k8s_handler'].delete_user(
            user['name'], 
            my_output=my_output,
            include_identity=True,
            wait=True
        )
        if not success:
            return False
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Selected users deleted')
    
    return True