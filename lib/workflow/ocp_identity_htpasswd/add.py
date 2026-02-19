import os
import re
import uuid
import base64
import bcrypt
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'provider' not in params:
        return None, 'Provider name required'

    if 'mode' not in params:
        params['mode'] = 'patch'

    if params['mode'] not in ['post', 'patch']:
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
        if len(entry.split(':')) != 2:
            return None, 'Unexecpted user input value: %s' % (entry)

        (username, password) = entry.split(':')
        encrypted_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=12)).decode("utf-8")
        encrypted_password = re.sub(r"\$2[^a]\$", "$2y$", encrypted_password)
        if username in params['users']:
            return None, 'User [%s] not unique' % (username)

        params['users'][username] = encrypted_password

    if len(params['admins']) == 1 and params['admins'][0] == '__ALL__':
        params['admins'] = []
        for user in params['users']:
            params['admins'].append(user)

    if len(params['users']) == 0 and len(params['admins']) == 0:
        return None, 'No user or admin information'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose params must be true or false'

    return params, None


def validate_add(params):
    params['providerInfo'] = params['k8s_handler'].get_identity_provider_htpasswd(params['provider'])
    params['userMap'] = params['k8s_handler'].get_identity_provider_htpasswd_user_map()
    if params['userMap'] is None:
        return None, 'Failed to get existing htpasswd users'

    if params['providerInfo'] is None:
        params['mode'] = 'post'

    params['secret_namespace'] = 'openshift-config'
    params['secret_name'] = params['provider'].replace('_', '-')

    for username in params['users']:
        if username in params['userMap'] and params['userMap'][username] != params['provider']:
            return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    for admin in params['admins']:
        if admin not in params['userMap']:
            if admin not in params['users']:
                return None, 'Admin user undefined: %s' % (admin)

        if admin in params['userMap']:
            if params['userMap'][admin] != params['provider']:
                return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    return params, None


def run_patch(params, my_output):
    users = {}

    data = base64.b64decode(
        params['providerInfo']['data']
    ).decode('utf-8')
    for line in data.split('\n'):
        if len(line) > 0:
            users[line.split(':')[0]] = line.split(':')[1]

    for user in params['users']:
        users[user] = params['users'][user]

    content = ''
    for user in users:
        content = '%s%s:%s\n' % (content, user, users[user])
    content = content.strip('\n')

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

    return True


def run_post(params, my_output):
    if params['providerInfo'] is None:
        secret_name = params['secret_name']
        if params['k8s_handler'].is_secret(params['secret_namespace'], params['provider']):
            secret_name = '%s-%s' % (params['provider'], str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])

        success = params['k8s_handler'].add_identity_provider_oauth(
            secret_name,
            provider_name=params['provider']
        )
        if not success:
            my_output.error(
                'OAuth update with htpasswd failed'
            )
            return False

        my_output.default(
            'OAuth updated with htpasswd [%s]' % (params['provider'])
        )

        users = {}

        for user in params['users']:
            users[user] = params['users'][user]

        content = ''
        for user in users:
            content = '%s%s:%s\n' % (content, user, users[user])
        content = content.strip('\n')

        encoded_content = base64.b64encode(
            content.encode('utf-8')
        ).decode('utf-8')

        kv = {}
        kv['htpasswd'] = encoded_content
        success = params['k8s_handler'].create_secret_kv_mo(
            params['secret_namespace'],
            secret_name,
            kv
        )
        if not success:
            my_output.error(
                'Secret create failed: %s/%s' % (
                    params['secret_namespace'],
                    secret_name
                )
            )
            return False

        my_output.default(
            'Secret %s/%s created' % (
                params['secret_namespace'],
                secret_name
            )
        )

        return True

    current = {}

    data = base64.b64decode(
        params['providerInfo']['data']
    ).decode('utf-8')
    for line in data.split('\n'):
        if len(line) > 0:
            current[line.split(':')[0]] = line.split(':')[1]

    users = {}

    for user in params['users']:
        users[user] = params['users'][user]

    content = ''
    for user in users:
        content = '%s%s:%s\n' % (content, user, users[user])
    content = content.strip('\n')

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

    success = True

    for current_user in current:
        if current_user not in users:
            identity = '%s:%s' % (
                params['providerInfo']['name'],
                current_user
            )
            my_output.default(
                'Deleting user [%s] and identity [%s]' % (
                    current_user,
                    identity
                )
            )
            user_mo = params['k8s_handler'].get_user(current_user, return_mo=True, cache_enabled=False)
            if user_mo is None:
                my_output.default('User already deleted, checking for identity leftover')
                if params['k8s_handler'].is_identity(identity, cache_enabled=False):
                    if not params['k8s_handler'].delete_identity_mo(identity):
                        my_output.error('REST API failed')
                        success = False

            if user_mo is not None:
                if len(user_mo['identities']) > 1:
                    my_output.default('User has multiple identities, deleting identity only')
                    if params['k8s_handler'].is_identity(identity, cache_enabled=False):
                        if not params['k8s_handler'].delete_identity_mo(identity):
                            my_output.error('REST API failed')
                            success = False
                else:
                    if not params['k8s_handler'].delete_user_mo(user_mo, include_identity=True):
                        my_output.error('REST API failed')
                        success = False

    return success


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Add HTPasswd Identity Provider', before_newline=True, after_newline=True, double_underline=True)

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

    params, error = validate_add(params)
    if error is not None:
        my_output.error(error)
        return False

    if len(params['users']) > 0:
        if params['mode'] == 'patch':
            if not run_patch(params, my_output):
                return False

        if params['mode'] == 'post':
            if not run_post(params, my_output):
                return False

    if len(params['admins']) > 0:
        current_admins = params['k8s_handler'].get_cluster_role_binding_users('cluster-admin')
        if current_admins is None:
            my_output.error(
                'Failed to get current admins'
            )
            return False

        for admin in params['admins']:
            if admin in current_admins:
                my_output.default(
                    'Username %s already in cluster admins group' % (
                        admin
                    )
                )
                continue

            my_output.default(
                'Add username %s to cluster admins group' % (
                    admin
                )
            )

            success = params['k8s_handler'].add_user_subject_cluster_role_binding(
                'cluster-admin',
                admin
            )
            if not success:
                my_output.default(
                    'Add username %s to cluster admins group failed' % (
                        admin
                    )
                )
                return False

    return True
