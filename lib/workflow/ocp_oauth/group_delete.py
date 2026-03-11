from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'group' not in params:
        params['group'] = None

    if 'ldap_host' not in params:
        params['ldap_host'] = None

    if 'ldap' not in params:
        params['ldap'] = False

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
        'group',
        'ldap_host',
        'ldap',
        'confirmation',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OAuth - Delete Group', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
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
