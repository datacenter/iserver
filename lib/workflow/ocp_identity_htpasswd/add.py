import os
import re
import uuid
import base64
import bcrypt
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_identity_htpasswd import common as local_common


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


def validate_add(params, my_output):
    my_output.default('htpasswd identity provider [%s]' % (params['provider']), before_newline=True)
    params['providerInfo'] = params['k8s_handler'].get_identity_provider_htpasswd(params['provider'])
    if params['providerInfo'] is None:
        params['mode'] = 'post'
        my_output.default('- not found')
    else:
        my_output.default('- found')

    my_output.default('- %s mode' % (params['mode']))

    params['userMap'] = params['k8s_handler'].get_identity_provider_htpasswd_user_map()
    if params['userMap'] is None:
        return None, 'Failed to get existing htpasswd users'

    params['secret_namespace'] = 'openshift-config'
    params['secret_name'] = params['provider'].replace('_', '-')
    my_output.default('- secret %s/%s' % (params['secret_namespace'], params['secret_name']))
    for username in params['users']:
        my_output.default('- check user %s' % (username))
        if username in params['userMap'] and params['userMap'][username] != params['provider']:
            return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    for admin in params['admins']:
        my_output.default('- check admin %s' % (admin))
        if admin not in params['userMap']:
            if admin not in params['users']:
                return None, 'Admin user undefined: %s' % (admin)

        if admin in params['userMap']:
            if params['userMap'][admin] != params['provider']:
                return None, 'User [%s] defined in another provider [%s]' % (username, params['userMap'][username])

    return params, None


def run_patch(params, my_output):
    users = {}

    if params['providerInfo']['data'] is None:
        data = ''
    else:
        try:
            data = base64.b64decode(
                params['providerInfo']['data']
            ).decode('utf-8')
        except BaseException:
            my_output.error('Failed to base64 decode data')
            return False
        
    for line in data.split('\n'):
        if len(line) > 0:
            users[line.split(':')[0]] = line.split(':')[1]

    for user in params['users']:
        users[user] = params['users'][user]

    content = ''
    for user in users:
        content = '%s%s:%s\n' % (content, user, users[user])
    content = content.strip('\n')

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
        replace=False,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )

    return success


def run_post(params, my_output):
    if params['providerInfo'] is None:
        secret_name = params['secret_name']
        if params['k8s_handler'].is_secret(params['secret_namespace'], params['provider']):
            secret_name = '%s-%s' % (params['provider'], str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])

        success = params['k8s_handler'].add_htpasswd_identity_provider_oauth(
            secret_name,
            params['provider'],
            confirmation=params['confirmation'],
            my_output=my_output
        )
        if not success:
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

        my_output.default('Generated htpasswd', before_newline=True)
        my_output.default(content, wrap='~~~')

        encoded_content = base64.b64encode(
            content.encode('utf-8')
        ).decode('utf-8')

        kv = {}
        kv['htpasswd'] = encoded_content

        success = params['k8s_handler'].create_secret_kv(
            params['secret_namespace'],
            secret_name,
            kv,
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        return success

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

    for current_user in current:
        if current_user not in users:
            identity = '%s:%s' % (
                params['providerInfo']['name'],
                current_user
            )

            success = params['k8s_handler'].delete_user(
                current_user, 
                include_identity=True,
                identity=identity,
                my_output=my_output,
                wait=True
            )
            if not success:
                return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Add HTPasswd Identity Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    params, error = validate_add(params, my_output)
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

            success = params['k8s_handler'].add_user_subject_cluster_role_binding(
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
