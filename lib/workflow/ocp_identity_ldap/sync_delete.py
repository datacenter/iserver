from urllib.parse import urlsplit
from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_identity_ldap import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'method' not in params or params['method'] is None:
        params['method'] = 'oc'
    
    if params['method'] not in ['oc', 'api']:
        return None, 'Unsupported method [%s], oc or api value expected' % (params['method'])
    
    if 'filename' not in params:
        params['filename'] = None

    params['content'] = None
    if params['filename'] is not None:
        if params['method'] == 'api':
            return None, 'Method api unsupported with filename input'
        
        params['content'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['content'] is None:
            return None, 'Filename yaml read failed: %s' % (params['filename'])
    
        kind = filter_helper.get(params['content'], 'kind')
        if kind != 'LDAPSyncConfig':
            return None, 'File with LDAPSyncConfig required'

    if params['filename'] is None:
        if 'provider' not in params or params['provider'] is None:
            return None, 'Provider name required'

        if 'group' not in params or params['group'] is None:
            return None, 'group required'

        if 'whitelist' not in params or params['whitelist'] is None:
            params['whitelist'] = []

        if 'blacklist' not in params or params['blacklist'] is None:
            params['blacklist'] = []

        if 'groupUIDAttribute' not in params or params['groupUIDAttribute'] is None:
            return None, 'groupUIDAttribute required'

        if 'groupNameAttributes' not in params or params['groupNameAttributes'] is None:
            return None, 'groupNameAttributes required'

        if 'groupMembershipAttributes' not in params or params['groupMembershipAttributes'] is None:
            return None, 'groupMembershipAttributes required'

        if 'user' not in params:
            params['user'] = None

        if 'userUIDAttribute' not in params or params['userUIDAttribute'] is None:
            return None, 'userUIDAttribute required'

        if 'userNameAttributes' not in params or params['userNameAttributes'] is None:
            return None, 'userNameAttributes required'
        
        if 'tolerateMemberNotFoundErrors' not in params:
            params['tolerateMemberNotFoundErrors'] = False

        if 'tolerateMemberOutOfScopeErrors' not in params:
            params['tolerateMemberOutOfScopeErrors'] = False

    if 'job' not in params:
        params['job'] = None

    if params['job'] is not None:
        if 'provider' not in params or params['provider'] is None:
            return None, 'Provider name required when job is defined'
            
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
        'method',
        'filename',
        'content',
        'provider',
        'group',
        'whitelist',
        'blacklist',
        'groupUIDAttribute',
        'groupNameAttributes',
        'groupMembershipAttributes',
        'user',
        'userUIDAttribute',
        'userNameAttributes',
        'tolerateMemberNotFoundErrors',
        'tolerateMemberOutOfScopeErrors',
        'job',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LDAP Group - Sync Prune', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh=True, optional=False)
    if params is None:
        return False

    if params['job'] is not None:
        success = params['k8s_handler'].delete_cron_job(
            params['job'], 
            '%s-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True
        )
        if not success:
            return False        

        success = params['k8s_handler'].delete_config_map(
            params['job'], 
            '%s-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True
        )
        if not success:
            return False        
        
        success = params['k8s_handler'].delete_config_map(
            params['job'], 
            '%s-whitelist-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True
        )
        if not success:
            return False        
        
        success = params['k8s_handler'].delete_config_map(
            params['job'], 
            '%s-blacklist-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True
        )
        if not success:
            return False        
        
        success = params['k8s_handler'].delete_cluster_role_binding(
            '%s-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True            
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_cluster_role(
            '%s-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True            
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_service_account(
            params['job'],
            '%s-group-syncer' % (params['provider']),
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_namespace(
            params['job'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
    if params['method'] == 'api':
        provider = local_common.get_provider(params, my_output, k8s_output_handler=k8s_output_handler)
        if provider is None:
            return False

        try:
            url_parsed = urlsplit(provider['url'])
            groups = params['k8s_handler'].get_groups(object_filter=['ldap_host:%s' % (url_parsed.hostname)], user_info=True)
        except BaseException:
            my_output.error('Provider url parsing error')
            return False

        k8s_output_handler.print_groups_state(groups)

        if params['confirmation']:
            if not get_confirmation():
                return False
        
        for group in groups:
            success = params['k8s_handler'].delete_group(
                group['name'], 
                my_output=my_output,
                wait=True
            )
            if not success:
                return False

    if params['method'] == 'oc':
        if params['content'] is None:
            provider = local_common.get_provider(params, my_output, k8s_output_handler=k8s_output_handler)
            if provider is None:
                return False
            
            params['whitelist'] = []
            params['blacklist'] = []
            params['content'] = local_common.get_sync_body(params, provider, my_output)
            if params['content'] is None:
                return False
        
        if params['filename'] is None:
            parsed_url = ip_helper.get_url_parse(provider['url'].replace('ldap://', 'http://'))
        else:
            parsed_url = ip_helper.get_url_parse(params['content']['url'].replace('ldap://', 'http://'))
            
        if params['method'] == 'oc':
            success = local_common.sync('prune groups', params, my_output)
            if not success:
                return False

        provider['groups'] = params['k8s_handler'].get_groups(
            object_filter=['ldap_host:%s' % (parsed_url['hostname'])], 
            user_info=True,
            cache_enabled=False
        )
        k8s_output_handler.print_groups_state(provider['groups'])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LDAP groups deleted')
    return True
