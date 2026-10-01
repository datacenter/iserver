from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_gpu_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            continue

        subscription = params['k8s_handler'].get_subscription_by_package(
            params['__default__']['name'],
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            my_output.default('Operator not found: %s' % (params['__default__']['name']))
            continue
        
        my_output.default('Operator', underline=True, before_newline=True)
        my_output.default('- subscription: %s' % (subscription['namespace_name']))
        my_output.default('- channel: %s' % (subscription['channel']))
        my_output.default('- csv: %s' % (subscription['installed_csv']))
        
        policies = params['k8s_handler'].get_cluster_policies(ds_info=True, cache_enabled=False)
        if policies is None:
            my_output.error('Failed to get nvidia cluster policy')
            continue
        
        for policy in policies:
            k8s_output_handler.print_cluster_policy(policy)
            k8s_output_handler.my_table(
                policy['daemon_sets'],
                [
                    ['Daemon Set', 'name'],
                    ['Scheduled', 'scheduled_summary'],
                    ['Available', 'available_summary']
                ]
            )

        output = params['k8s_handler'].get_nvidia_smi()
        if output is not None:
            my_output.default(output, wrap='~~~', before_newline=True)

        my_output.default('Monitoring Dashboard', underline=True, before_newline=True)

        is_config_map = params['k8s_handler'].is_config_map(
            params['__default__']['monitoring']['dashboard_namespace'],
            params['__default__']['monitoring']['dashboard_name'],
            cache_enabled=False
        )
        if is_config_map:
            my_output.default(
                '- config map: %s/%s' % (
                    params['__default__']['monitoring']['dashboard_namespace'],
                    params['__default__']['monitoring']['dashboard_name']
                )
            )
        else:
            my_output.default('- disabled')

        daemon_set = params['k8s_handler'].get_daemon_set(
            params['__default__']['namespace'],
            params['__default__']['ds-dcgm']
        )
        if daemon_set is None:
            my_output.default('- dcgm: %s' % (my_output.add_color('not found', 'Red')))
        else:
            if daemon_set['ready']:
                my_output.default('- dcgm: %s' % (my_output.add_color('ready', 'Green')))
            else:
                my_output.default('- dcgm: %s' % (my_output.add_color('not ready', 'Red')))

        daemon_set = params['k8s_handler'].get_daemon_set(
            params['__default__']['namespace'],
            params['__default__']['ds-dcgm-exporter']
        )
        if daemon_set is None:
            my_output.default('- dcgm exporter: %s' % (my_output.add_color('not found', 'Red')))
        else:
            if daemon_set['ready']:
                my_output.default('- dcgm exporter: %s' % (my_output.add_color('ready', 'Green')))
            else:
                my_output.default('- dcgm exporter: %s' % (my_output.add_color('not ready', 'Red')))

    return True