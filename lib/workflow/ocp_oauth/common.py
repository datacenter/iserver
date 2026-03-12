import copy
import json
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    return params


def get_default_params():
    params = {}
    params['default'] = {}
    params['default']['auth-namespace'] = 'openshift-authentication'
    params['default']['operator-namespace'] = 'openshift-authentication-operator'
    params['default']['apiserver-namespace'] = 'openshift-oauth-apiserver'
    params['default']['co'] = 'authentication'
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def get_state(params, my_output, scope=None, cache_enabled=False):
    if scope is None:
        scope = ['co', 'group', 'user', 'pod', 'deployment', 'authentication', 'oauth', 'ldap', 'htpasswd']

    if 'state' not in params:
        params['state'] = {}

    if 'deployment' in scope:
        params['state']['operator_deployment'] = params['k8s_handler'].get_oauth_operator_deployments(cache_enabled=cache_enabled)
        if params['state']['operator_deployment'] is None:
            my_output.error('Failed to get operator deployments')
            params['state']['operator_deployment'] = []

        params['state']['oauth_deployment'] = params['k8s_handler'].get_oauth_deployments(cache_enabled=cache_enabled)
        if params['state']['oauth_deployment'] is None:
            my_output.error('Failed to get authentication deployments')
            params['state']['oauth_deployment'] = []

        params['state']['deployment'] = params['state']['operator_deployment'] + params['state']['oauth_deployment']

    if 'pod' in scope:
        params['state']['operator_pod'] = params['k8s_handler'].get_oauth_operator_pods(cache_enabled=cache_enabled)
        if params['state']['operator_pod'] is None:
            my_output.error('Failed to get operator pods')
            params['state']['operator_pod'] = []

        params['state']['oauth_pod'] = params['k8s_handler'].get_oauth_pods(cache_enabled=cache_enabled)
        if params['state']['oauth_pod'] is None:
            my_output.error('Failed to get authentication pods')
            params['state']['oauth_pod'] = []

        params['state']['pod'] = params['state']['operator_pod'] + params['state']['oauth_pod']

    if 'co' in scope:
        params['state']['co'] = params['k8s_handler'].get_cluster_operator(
            params['default']['co'],
            cache_enabled=cache_enabled
        )
        if params['state']['co'] is None:
            my_output.error('Failed to get cluster operator')

    if 'group' in scope:
        params['state']['group'] = params['k8s_handler'].get_groups(user_info=True, cache_enabled=cache_enabled)
        if params['state']['group'] is None:
            my_output.error('Failed to get groups')
            params['state']['group'] = []

        params['state']['ldap_groups'] = 0
        for group in params['state']['group']:
            if group['isLdap']:
                params['state']['ldap_groups'] += 1

    if 'user' in scope:
        params['state']['user'] = params['k8s_handler'].get_users(cache_enabled=cache_enabled)
        if params['state']['user'] is None:
            my_output.error('Failed to get users')
            params['state']['user'] = []

    if 'authentication' in scope:
        params['state']['authentication'] = params['k8s_handler'].get_authentications(cache_enabled=cache_enabled)
        if params['state']['authentication'] is None:
            my_output.error('Failed to get authentication crd')
            params['state']['authentication'] = []

    if 'oauth' in scope:
        params['state']['oauth'] = params['k8s_handler'].get_oauths(user_info=True, cache_enabled=cache_enabled)
        if params['state']['oauth'] is None:
            my_output.error('Failed to get oauth crd')
            params['state']['oauth'] = []
    
    if 'ldap' in scope:
        params['state']['ldap'] = params['k8s_handler'].get_identity_providers_ldap(cache_enabled=cache_enabled)
        if params['state']['ldap'] is None:
            my_output.error('Failed to get ldap providers')
            params['state']['ldap'] = []

    if 'htpasswd' in scope:
        params['state']['htpasswd'] = params['k8s_handler'].get_identity_providers_htpasswd(cache_enabled=cache_enabled)
        if params['state']['htpasswd'] is None:
            my_output.error('Failed to get htpasswd providers')
            params['state']['htpasswd'] = []

    return params


def print_state(params, my_output, k8s_output_handler, scope=None):
    print_map = {}
    print_map['co'] = 'print_cluster_operator'
    print_map['authentication'] = 'print_authentications_state'
    print_map['pod'] = 'print_pods_state'
    print_map['oauth'] = 'print_oauths'
    print_map['ldap'] = 'print_oauths_ldap'
    print_map['htpasswd'] = 'print_oauths_htpasswd'
    print_map['user'] = 'print_users_state'
    print_map['group'] = 'print_groups_state'

    if scope is None:
        scope = list(print_map.keys())

    for item in scope:
        if item not in params['state']:
            my_output.error('Exception: %s not collected' % (item))
            continue

        if params['state'][item] is None:
            my_output.error('%s get failed' % (item))
            continue

        getattr(k8s_output_handler, print_map[item])(params['state'][item])


def print_state_summary(params, my_output, k8s_output_handler):
    k8s_output_handler.print_cluster_operator(params['state']['co'], table=False)
    k8s_output_handler.print_authentications_state(params['state']['authentication'][0], table=False)

    my_output.default('Pod', before_newline=True, underline=True)
    info = params['k8s_handler'].get_pods_summary(params['state']['operator_pod'])
    my_output.default('- operator: %s' % (my_output.add_color(info['summary'], info['__Output']['summary'])))
    info = params['k8s_handler'].get_pods_summary(params['state']['oauth_pod'])
    my_output.default('- authentication: %s' % (my_output.add_color(info['summary'], info['__Output']['summary'])))

    my_output.default('Authentication and Authorization', before_newline=True, underline=True)
    for item in params['state']['htpasswd']:
        my_output.default(
            '- identity provider htpasswd [%s] with [%s/%s] active users' % (
                item['name'],
                item['userCount'],
                len(item['users'])
            )
        )

    for item in params['state']['ldap']:
        my_output.default(
            '- identity provider ldap [%s] with [%s] active users' % (
                item['name'],
                item['userCount']
            )
        )

    my_output.default('- users: %s' % (len(params['state']['user'])))
    my_output.default('- group: %s with %s from ldap' % (len(params['state']['group']), params['state']['ldap_groups']))

    my_output.default('Command hints', before_newline=True, underline=True)
    my_output.default('iserver get k8s pod --namespace openshift-authentication-operator -v logs')
    my_output.default('iserver get k8s pod --namespace openshift-authentication -v logs')
    my_output.default('iserver get ocp htpasswd')
    my_output.default('iserver get ocp ldap')
    my_output.default('iserver get k8s user')
    my_output.default('iserver get k8s group')
