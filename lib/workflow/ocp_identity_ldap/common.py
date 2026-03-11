import yaml
import copy
import json
from urllib.parse import urlsplit
from lib import ip_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common
from menu.common import get_confirmation


def initialize(params, my_output, log_id, ssh=False, optional=False):
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
    if ssh:
        params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id, optional=optional)
        if not optional and params['ssh_handler'] is None:
            my_output.error('cluster management node ssh failed')
            return None

    return params


def get_default_params():
    params = {}
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


def get_providers_details(params, providers):
    for provider in providers:
        provider['users'] = params['k8s_handler'].get_users(
            object_filter=['provider:%s' % (provider['name'])]
        )
        if provider['users'] is None:
            provider['users'] = []

        try:
            url_parsed = urlsplit(provider['url'])
            provider['groups'] = params['k8s_handler'].get_groups(object_filter=['ldap_host:%s' % (url_parsed.hostname)], user_info=True)
        except BaseException:
            provider['groups'] = []

        if provider['groups'] is None:
            provider['groups'] = []

        provider['usageT'] = []
        provider['usageT'].append('User:  %s' % (len(provider['users'])))
        provider['usageT'].append('Group: %s' % (len(provider['groups'])))

    return providers                    


def print_provider_details(my_output, k8s_output_handler, provider):
    k8s_output_handler.print_oauths_ldap([provider])
    my_output.default(
        yaml.dump(provider['mo']), 
        before_newline=True,
        wrap='~~~'
    )

    if len(provider['users']) > 0:
        k8s_output_handler.print_users_state(provider['users'])

    if len(provider['groups']) > 0:
        k8s_output_handler.print_groups_state(provider['groups'])


def get_provider(params, my_output, k8s_output_handler=None):
    providers = params['k8s_handler'].get_identity_providers_ldap(
        params['provider'],
        cache_enabled=False
    )
    if providers is None or len(providers) == 0:
        my_output.default('LDAP provider %s %s' % (params['provider'], my_output.add_color('not found', 'Red')))
        return None

    provider = get_providers_details(params, providers)[0]
    if k8s_output_handler is not None:
        k8s_output_handler.print_oauths_ldap([provider])
    return provider


def get_sync_body(params, provider, my_output):
    params['parsed_url'] = ip_helper.get_url_parse(provider['url'].replace('ldap://', 'http://'))

    body = {}
    body['apiVersion'] = 'v1'
    body['kind'] = 'LDAPSyncConfig'
    body['url'] = 'ldap://%s' % (params['parsed_url']['netloc'])
    body['insecure'] = provider['insecure']
    body['bindDN'] = provider['bind_dn']
    body['bindPassword'] = provider['password']
    body['rfc2307'] = {}
    body['rfc2307']['groupsQuery'] = {}
    body['rfc2307']['groupsQuery']['baseDN'] = params['group']
    body['rfc2307']['groupsQuery']['scope'] = 'sub'
    body['rfc2307']['groupsQuery']['filter'] = '(objectClass=group)'
    body['rfc2307']['groupsQuery']['derefAliases'] = 'never'
    body['rfc2307']['groupsQuery']['pageSize'] = 0
    body['rfc2307']['groupUIDAttribute'] = params['groupUIDAttribute']
    body['rfc2307']['groupNameAttributes'] = [params['groupNameAttributes']]
    body['rfc2307']['groupMembershipAttributes'] = [params['groupMembershipAttributes']]
    body['rfc2307']['usersQuery'] = {}
    if params['user'] is None:
        body['rfc2307']['usersQuery']['baseDN'] = params['parsed_url']['path']
    else:
        body['rfc2307']['usersQuery']['baseDN'] = params['user']
    body['rfc2307']['usersQuery']['scope'] = 'sub'
    body['rfc2307']['usersQuery']['derefAliases'] = 'never'
    body['rfc2307']['usersQuery']['pageSize'] = 0
    body['rfc2307']['userUIDAttribute'] = params['userUIDAttribute']
    body['rfc2307']['userNameAttributes'] = [params['userNameAttributes']]
    body['rfc2307']['tolerateMemberNotFoundErrors'] = params['tolerateMemberNotFoundErrors']
    body['rfc2307']['tolerateMemberOutOfScopeErrors'] = params['tolerateMemberOutOfScopeErrors']

    my_output.default(yaml.dump(body), wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return None
    
    return body


def to_upper(text):
    items = text.split(',')
    new_items = []
    for item in items:
        if len(item.split('=')) != 2:
            new_items.append(item)

        (item_a, item_b) = item.split('=')
        new_items.append(
            '%s=%s' % (item_a.upper(), item_b)
        )
    return ','.join(new_items)


def get_whitelist(params, my_output):
    content = []
    for item in params['whitelist']:
        if len(item.split(',')) == 1:
            content.append(to_upper('cn=%s,%s' % (item, params['group'])))
        else:
            content.append(to_upper(item))

    if len(content) == 0:
        return None
    
    body = '\n'.join(content)
    my_output.default('Whitelist', before_newline=True, after_newline=True)
    my_output.default(body, wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return None
    
    return body


def get_blacklist(params, my_output):
    content = []
    for item in params['blacklist']:
        if len(item.split(',')) == 1:
            content.append(to_upper('cn=%s,%s' % (item, params['group'])))
        else:
            content.append(to_upper(item))

    if len(content) == 0:
        return None
    
    body = '\n'.join(content)
    my_output.default('Blacklist', before_newline=True, after_newline=True)
    my_output.default(body, wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return None
    
    return body


def sync(mode, params, my_output):
    remote_config = params['ssh_handler'].create_file(yaml.dump(params['content']))
    if remote_config is None:
        my_output.error('Failed to create yaml file on the management node')
        return False
    my_output.default('LDAPSyncConfig uploaded: %s' % (remote_config))

    whitelist = get_whitelist(params, my_output)
    remote_whitelist = None
    if whitelist is not None:
        remote_whitelist = params['ssh_handler'].create_file(whitelist)
        if remote_whitelist is None:
            my_output.error('Failed to create whitelist file on the management node')
            return False
        my_output.default('whitelist uploaded: %s' % (remote_whitelist))

    blacklist = get_blacklist(params, my_output)
    remote_blacklist = None
    if blacklist is not None:
        remote_blacklist = params['ssh_handler'].create_file(blacklist)
        if remote_blacklist is None:
            my_output.error('Failed to create blacklist file on the management node')
            return False
        my_output.default('blacklist uploaded: %s' % (remote_blacklist))

    command = 'oc adm %s --sync-config=%s' % (mode, remote_config)
    if remote_whitelist is not None:
        command = '%s --whitelist=%s' % (command, remote_whitelist)
    if remote_blacklist is not None:
        command = '%s --blacklist=%s' % (command, remote_blacklist)

    my_output.default('Run: %s' % (command))
    success, output, error = params['ssh_handler'].run_cmd(command)
    if not success:
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False

    my_output.default(str(output), wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return False
        
    command = '%s --confirm' % (command)
    my_output.default('Run: %s' % (command))
    success, output, error = params['ssh_handler'].run_cmd(command)
    if not success:
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False

    return True