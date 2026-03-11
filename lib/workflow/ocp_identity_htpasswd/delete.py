import os
import copy
import base64
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_identity_htpasswd import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'provider' not in params:
        return None, 'Provider name required'

    if 'mode' not in params:
        params['mode'] = 'delete'

    if params['mode'] not in ['delete']:
        return None, 'Invalid mode'

    if 'filename' not in params:
        params['filename'] = []

    if 'userpass' not in params:
        params['userpass'] = []

    if 'admins' not in params:
        params['admins'] = []

    params['users'] = {}

    locations = []
    for item in params['filename']:
        try:
            if not os.path.isabs(item):
                item = os.path.join(
                    params['base_directory'],
                    item
                )
        except BaseException:
            return None, 'htpasswd file path detection failed'
        
        locations.append(item)

    for item in locations:
        keys = file_helper.get_files_text(item)
        if keys is not None:
            for key in keys:
                for line in keys[key].split('\n'):
                    if len(line) > 0:
                        if len(line.split(':')) != 2:
                            return None, 'Unexpected htpasswd file content: %s' % (key)

                        username, password = line.split(':')
                        if username in params['users']:
                            return None, 'Unexpected htpasswd file content, user [%s] not unique: %s' % (username, key)

                        params['users'][username] = password

    for entry in params['userpass']:
        params['users'][entry.split(':')[0]] = None

    if len(params['admins']) == 1 and params['admins'][0] == '__ALL__':
        params['admins'] = []
        for user in params['users']:
            params['admins'].append(user)
            
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
    
    return params, None


def validate_delete(params, my_output):
    my_output.default('htpasswd identity provider [%s]' % (params['provider']), before_newline=True)
    params['providerInfo'] = params['k8s_handler'].get_identity_provider_htpasswd(params['provider'])
    if params['providerInfo'] is None:
        return None, 'Provider not found'
        
    my_output.default('- found')

    params['userMap'] = params['k8s_handler'].get_identity_provider_htpasswd_user_map()
    if params['userMap'] is None:
        return None, 'Failed to get existing htpasswd users'

    params['secret_namespace'] = 'openshift-config'
    params['secret_name'] = params['providerInfo']['secret']

    # provider delete case
    if len(params['admins']) == 0 and len(params['users']) == 0:
        for username in params['userMap']:
            if params['userMap'][username] == params['provider']:
                params['users'][username] = None

    # remove users that are not defined
    already_gone = []
    for username in params['users']:
        if username not in params['userMap']:
            already_gone.append(username)

    if len(already_gone) > 0:
        users = []
        for username in params['users']:
            if username in already_gone:
                continue
            users.append(username)

        params['users'] = copy.deepcopy(users)

    # check if user is not in another provider
    for username in params['users']:
        if params['userMap'][username] != params['provider']:
            return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    # remove admins that are not defined
    already_gone = []
    for username in params['admins']:
        if username not in params['userMap']:
            already_gone.append(username)

    if len(already_gone) > 0:
        users = []
        for username in params['admins']:
            if username in already_gone:
                continue
            users.append(username)

        params['admins'] = copy.deepcopy(users)

    # check if adminuser is not in another provider
    for username in params['admins']:
        if params['userMap'][username] != params['provider']:
            return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Delete HTPasswd Identity Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    params, error = validate_delete(params, my_output)
    if error is not None:
        my_output.error(error)
        return False
            
    if len(params['users']) > 0:
        for user in params['users']:
            identity = '%s:%s' % (
                params['providerInfo']['name'],
                user
            )

            success = params['k8s_handler'].delete_user(
                user, 
                include_identity=True,
                identity=identity,
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
            success = params['k8s_handler'].del_user_subject_cluster_role_binding(
                'cluster-admin', 
                user, 
                confirmation=params['confirmation'], 
                my_output=my_output
            )
            if not success:
                return False

        users_left = []

        content = ''
        for user in params['userMap']:
            if params['userMap'][user] != params['provider']:
                continue

            if user in params['users']:
                continue

            users_left.append(user)
            content = '%s%s:%s\n' % (content, user, params['providerInfo']['password'][user])

        content = content.strip('\n')

        if len(users_left) > 0:
            my_output.default('Generated htpasswd', before_newline=True)
            my_output.default(content, wrap='~~~')

            encoded_content = base64.b64encode(
                content.encode('utf-8')
            ).decode('utf-8')

            kv = {}
            kv['htpasswd'] = encoded_content

            success = params['k8s_handler'].create_or_update_secret_kv(
                params['secret_namespace'],
                params['providerInfo']['secret'],
                kv,
                replace=True,
                confirmation=params['confirmation'],
                my_output=my_output,
                wait=True
            )
            if not success:
                return False

        if len(users_left) == 0:
            success = params['k8s_handler'].delete_secret(
                params['secret_namespace'], 
                params['secret_name'],
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False

            success = params['k8s_handler'].del_identity_provider_oauth(
                params['provider'],
                confirmation=params['confirmation'],
                my_output=my_output
            )
            if not success:
                return False

    if len(params['admins']) > 0:
        for admin in params['admins']:
            success = params['k8s_handler'].del_user_subject_cluster_role_binding(
                'cluster-admin', 
                admin, 
                confirmation=params['confirmation'], 
                my_output=my_output
            )
            if not success:
                return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- HTPasswd Identity Provider configured')
    return True
