from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'user' not in params:
        params['user'] = None

    if 'group' not in params:
        params['group'] = None

    if 'provider' not in params:
        params['provider'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'user',
        'group',
        'provider',
        'confirmation',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OAuth - Delete User', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
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
