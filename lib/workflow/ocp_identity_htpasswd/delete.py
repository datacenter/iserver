import os
import copy
import base64
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check


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
            

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose params must be true or false'
        
    return params, None


def validate_delete(params):
    params['providerInfo'] = params['k8s_handler'].get_identity_provider_htpasswd(params['provider'])
    if params['providerInfo'] is None:
        return None, 'Provider not found'

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

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    params, error = validate_delete(params)
    if error is not None:
        my_output.error(error)
        return False
            
    if len(params['users']) > 0:
        for user in params['users']:
            identity = '%s:%s' % (
                params['providerInfo']['name'],
                user
            )

            my_output.default(
                'Deleting user [%s] and identity [%s]' % (
                    user,
                    identity
                )
            )

            user_mo = params['k8s_handler'].get_user(user, return_mo=True, cache_enabled=False)
            if user_mo is None:
                my_output.default('User already deleted, checking for identity leftover')
                if params['k8s_handler'].is_identity(identity, cache_enabled=False):
                    if not params['k8s_handler'].delete_identity_mo(identity):
                        my_output.error('REST API failed')
                        return False

            if user_mo is not None:
                if len(user_mo['identities']) > 1:
                    my_output.default('User has multiple identities, deleting identity only')
                    if params['k8s_handler'].is_identity(identity, cache_enabled=False):
                        if not params['k8s_handler'].delete_identity_mo(identity):
                            my_output.error('REST API failed')
                            return False
                else:
                    if not params['k8s_handler'].delete_user_mo(user_mo, include_identity=True):
                        my_output.error('REST API failed')
                        return False

            my_output.default(
                'Deleting user [%s] from cluster-admin group' % (
                    user
                )
            )

            if not params['k8s_handler'].del_user_subject_cluster_role_binding('cluster-admin', user):
                my_output.error('REST API failed')
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
            encoded_content = base64.b64encode(
                content.encode('utf-8')
            ).decode('utf-8')

            kv = {}
            kv['htpasswd'] = encoded_content
            success = params['k8s_handler'].update_secret_kv_mo(
                params['secret_namespace'],
                params['providerInfo']['secret'],
                kv
            )
            if not success:
                my_output.error(
                    'Secret update failed: %s/%s' % (
                        params['secret_namespace'],
                        params['providerInfo']['secret']
                    )
                )
                return False

            my_output.default(
                'Secret %s/%s updated' % (
                    params['secret_namespace'],
                    params['providerInfo']['secret']
                )
            )

        if len(users_left) == 0:
            my_output.default(
                'Deleting secret [%s/%s]' % (
                    params['secret_namespace'],
                    params['secret_name']
                )
            )
            if params['k8s_handler'].is_secret(params['secret_namespace'], params['secret_name'], cache_enabled=False):
                if not params['k8s_handler'].delete_secret_mo(params['secret_namespace'], params['secret_name']):
                    my_output.error('REST API failed')
                    return False

            my_output.default(
                'Deleting htpasswd identity provider [%s]' % (
                    params['provider']
                )
            )
            if not params['k8s_handler'].del_identity_provider_oauth(params['provider']):
                my_output.error('REST API failed')
                return False

    if len(params['admins']) > 0:
        for admin in params['admins']:
            my_output.default('Removing user [%s] from cluster-admin group' % (admin))
            if not params['k8s_handler'].del_user_subject_cluster_role_binding('cluster-admin', admin):
                my_output.error('REST API failed')
                return False

    return True
