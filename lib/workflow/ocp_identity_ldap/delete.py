from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_identity_ldap import common as local_common
from lib.workflow.ocp_oauth import group_delete
from lib.workflow.ocp_oauth import user_delete
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'provider' not in params:
        params['provider'] = None

    if 'dependencies' not in params:
        params['dependencies'] = True

    if not isinstance(params['dependencies'], bool):
        return None, 'dependencies param must be true or false'
            
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'    

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
    allowed_keys = [
        'cluster',
        'provider',
        'dependencies',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LDAP Identity Provider - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    if params['provider'] is None:
        providers = params['k8s_handler'].get_identity_providers_ldap(cache_enabled=False)
    else:
        providers = params['k8s_handler'].get_identity_providers_ldap(name=params['provider'], cache_enabled=False)

    if providers is None or len(providers) == 0:
        my_output.default(
            'Identity ldap %s' % (my_output.add_color('not defined', 'Green'))
        )
        return True

    if params['dependencies']:
        providers = local_common.get_providers_details(params, providers)

    for provider in providers:
        if params['dependencies']:
            local_common.print_provider_details(my_output, k8s_output_handler, provider)
        else:
            k8s_output_handler.print_oauths_ldap([provider])

        if params['confirmation']:
            if not get_confirmation():
                return False

        if params['dependencies']:
            if len(provider['users']) == 0:
                my_output.default('No users from identity provider', before_newline=True)

            for user in provider['users']:
                child_params = {}
                child_params['cluster'] = params['cluster']
                child_params['user'] = user['name']
                child_params['verbose'] = params['verbose']
                child_params['confirmation'] = False
                success = user_delete.run(child_params, log_id=log_id)
                if not success:
                    return False
                
            if len(provider['groups']) == 0:
                my_output.default('No groups from identity provider', before_newline=True)

            for group in provider['groups']:
                child_params = {}
                child_params['cluster'] = params['cluster']
                child_params['group'] = group['name']
                child_params['verbose'] = params['verbose']
                child_params['confirmation'] = False
                success = group_delete.run(child_params, log_id=log_id)
                if not success:
                    return False

        success = params['k8s_handler'].del_identity_provider_oauth(
            provider['name'],
            confirmation=False,
            my_output=my_output
        )
        if not success:
            return False

        if provider['isSecret']:
            success = params['k8s_handler'].delete_secret(
                'openshift-config', 
                provider['secret'], 
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
    my_output.default('')
    my_output.default('Completed tasks')
    if params['dependencies']:
        my_output.default('- LDAP Identity Provider deleted with dependencies')
    else:
        my_output.default('- LDAP Identity Provider deleted')
    return True
