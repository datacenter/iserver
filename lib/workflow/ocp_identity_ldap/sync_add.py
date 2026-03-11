import yaml
from lib import file_helper
from lib import filter_helper
from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_identity_ldap import common as local_common


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

    if 'schedule' not in params:
        params['schedule'] = '*/30'

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
        'schedule',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - LDAP Group - Sync Add', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh=True, optional=False)
    if params is None:
        return False

    if params['content'] is None:
        provider = local_common.get_provider(params, my_output, k8s_output_handler=k8s_output_handler)
        if provider is None:
            return False
        
        params['content'] = local_common.get_sync_body(params, provider, my_output)
        if params['content'] is None:
            return False
    
    success = local_common.sync('groups sync', params, my_output)
    if not success:
        return False

    if params['filename'] is None:
        parsed_url = ip_helper.get_url_parse(provider['url'].replace('ldap://', 'http://'))
        provider['groups'] = params['k8s_handler'].get_groups(
            object_filter=['ldap_host:%s' % (parsed_url['hostname'])], 
            user_info=True,
            cache_enabled=False
        )
        k8s_output_handler.print_groups_state(provider['groups'])

    if params['job'] is not None:
        provider = local_common.get_provider(params, my_output)
        if provider is None:
            return False

        success = params['k8s_handler'].create_namespace(
            params['job'],
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].create_service_account(
            params['job'],
            '%s-group-syncer' % (params['provider']),
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
                
        success = params['k8s_handler'].create_or_update_cluster_role(
            '%s-group-syncer' % (params['provider']), 
            api_groups=['', 'user.openshift.io'], 
            resources=['groups'], 
            verbs=['get', 'list', 'create', 'update'],
            replace=True,
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True            
        )
        if not success:
            return False

        success = params['k8s_handler'].create_or_update_service_account_cluster_role_binding(
            '%s-group-syncer' % (params['provider']), 
            '%s-group-syncer' % (params['provider']), 
            '%s-group-syncer' % (params['provider']), 
            params['job'],
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True            
        )
        if not success:
            return False
        
        data = {}
        data['sync.yaml'] = yaml.dump(params['content'])

        success = params['k8s_handler'].create_or_update_config_map(
            params['job'], 
            '%s-group-syncer' % (params['provider']),
            data, 
            labels=None,
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        whitelist = local_common.get_whitelist(params, my_output)
        if whitelist is not None:
            data = {}
            data['whitelist.txt'] = whitelist

            success = params['k8s_handler'].create_or_update_config_map(
                params['job'], 
                '%s-whitelist-group-syncer' % (params['provider']),
                data, 
                labels=None,
                confirmation=params['confirmation'],
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
        blacklist = local_common.get_blacklist(params, my_output)
        if blacklist is not None:
            data = {}
            data['blacklist.txt'] = blacklist

            success = params['k8s_handler'].create_or_update_config_map(
                params['job'], 
                '%s-blacklist-group-syncer' % (params['provider']),
                data, 
                labels=None,
                confirmation=params['confirmation'],
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
        job = {}
        container_mo = {}
        container_mo['name'] = '%s-group-syncer' % (params['provider'])
        container_mo['image'] = 'registry.redhat.io/openshift4/ose-cli:latest'
        command = 'oc adm groups sync --sync-config=/etc/config/sync.yaml'
        if whitelist is not None:
            command = '%s --whitelist=/etc/whitelist/whitelist.txt' % (command)
        if blacklist is not None:
            command = '%s --blacklist=/etc/blacklist/blacklist.txt' % (command)
        command = '%s --confirm' % (command)
        container_mo['command'] = [
            '/bin/bash',
            '-c',
            command
        ]
        mount_mo = {}
        mount_mo['mountPath'] = '/etc/config'
        mount_mo['name'] = 'ldap-sync-volume'
        container_mo['volumeMounts'] = [mount_mo]

        if whitelist is not None:
            mount_mo = {}
            mount_mo['mountPath'] = '/etc/whitelist'
            mount_mo['name'] = 'ldap-sync-whitelist'
            container_mo['volumeMounts'].append(mount_mo)

        if blacklist is not None:
            mount_mo = {}
            mount_mo['mountPath'] = '/etc/blacklist'
            mount_mo['name'] = 'ldap-sync-blacklist'
            container_mo['volumeMounts'].append(mount_mo)

        job['containers'] = [container_mo]
        
        volume_mo = {}
        volume_mo['name'] = 'ldap-sync-volume'
        volume_mo['configMap'] = dict(name='%s-group-syncer' % (params['provider']))
        job['volumes'] = [volume_mo]

        if whitelist is not None:
            volume_mo = {}
            volume_mo['name'] = 'ldap-sync-whitelist'
            volume_mo['configMap'] = dict(name='%s-whitelist-group-syncer' % (params['provider']))
            job['volumes'].append(volume_mo)

        if blacklist is not None:
            volume_mo = {}
            volume_mo['name'] = 'ldap-sync-blacklist'
            volume_mo['configMap'] = dict(name='%s-blacklist-group-syncer' % (params['provider']))
            job['volumes'].append(volume_mo)

        job['restartPolicy'] = 'Never'
        job['terminationGracePeriodSeconds'] = 30
        job['activeDeadlineSeconds'] = 500
        job['dnsPolicy'] = 'ClusterFirst'
        job['serviceAccountName'] = '%s-group-syncer' % (params['provider'])

        success = params['k8s_handler'].create_or_update_cron_job(
            params['job'], 
            '%s-group-syncer' % (params['provider']),
            '%s * * * *' % (params['schedule']), 
            job,
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- LDAP groups configured')
    return True
