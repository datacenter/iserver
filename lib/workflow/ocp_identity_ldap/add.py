from lib import file_helper
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_identity_ldap import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'filename' not in params:
        params['filename'] = None

    params['content'] = None
    if params['filename'] is not None:
        params['content'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['content'] is None:
            return None, 'Filename yaml read failed: %s' % (params['filename'])
    
        for key in ['type', 'name', 'method', 'ldap']:
            if key not in params['content']:
                return None, 'Filename with ldap provider definition required: key %s expected' % (key)

        bind_password = filter_helper.get(params['content'], 'ldap:bindPassword:name')
        if bind_password is None:
            if 'secret' not in params or params['secret'] is None:
                return None, 'secret required'
        else:
            params['secret'] = None

    if params['filename'] is None:
        if 'provider' not in params or params['provider'] is None:
            return None, 'Provider name required'

        if 'url' not in params or params['url'] is None:
            return None, 'url required'

        if 'bind' not in params or params['bind'] is None:
            return None, 'bind required'

        if 'secret' not in params or params['secret'] is None:
            return None, 'secret required'

        if 'mapping' not in params or params['mapping'] is None:
            params['mapping'] = 'claim'

        if params['mapping'] not in ['claim', 'add', 'lookup']:
            return None, 'mapping one of claim, add or lookup required'

        if 'id' not in params or params['id'] is None:
            params['id'] = ['dn']

        if not isinstance(params['id'], list):
            return None, 'id param must be list'

        if 'name' not in params or params['name'] is None:
            params['name'] = ['cn']

        if not isinstance(params['name'], list):
            return None, 'name param must be list'

        if 'email' not in params or params['email'] is None:
            params['email'] = ['mail']

        if not isinstance(params['email'], list):
            return None, 'email param must be list'

        if 'username' not in params or params['username'] is None:
            params['username'] = ['uid']

        if not isinstance(params['username'], list):
            return None, 'username param must be list'

        if 'insecure' not in params or params['insecure'] is None:
            params['insecure'] = True

        if not isinstance(params['insecure'], bool):
            return None, 'insecure param must be true or false'
    
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
        'filename',
        'content',
        'provider',
        'url',
        'bind',
        'secret',
        'id',
        'name',
        'username',
        'email',
        'mapping',
        'insecure',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - LDAP Identity Provider - Add', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh=True, optional=True)
    if params is None:
        return False

    if params['content'] is None:
        if params['ssh_handler'] is not None:
            if params['insecure']:
                command = 'curl -sS --insecure %s -u %s:%s' % (
                    params['url'],
                    params['bind'],
                    params['secret']
                )
            else:
                command = 'curl -sS %s -u %s:%s' % (
                    params['url'],
                    params['bind'],
                    params['secret']
                )

            my_output.default('Check LDAP access from clusters management host...', before_newline=True)
            success, output, error = params['ssh_handler'].run_cmd(command)
            if success:
                my_output.default('# %s\n%s' % (command, str(output)), wrap='~~~')
            else:
                if my_output is not None:
                    my_output.default('$ %s\n%s' % (command, str(error)), wrap='~~~')
                
                if params['confirmation']:
                    if not get_confirmation('Continue?'):
                        return False
                
        success = params['k8s_handler'].set_ldap_identity_provider_oauth_from_params(
            params['provider'],
            params['url'],
            params['bind'],
            params['secret'],
            params['id'],
            params['name'],
            params['username'],
            params['email'],
            insecure=params['insecure'], 
            mapping=params['mapping'], 
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False
    else:
        success = params['k8s_handler'].set_ldap_identity_provider_oauth_from_body(
            params['content'],
            secret=params['secret'],
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LDAP Identity Provider configured')
    return True
