from lib.k8s import output as k8s_output
from lib import output_helper
from lib import filter_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['view', False, None, 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_instance_state(info, instances, iconfiguration):
    info['__Output']['instance'] = 'Red'
    info['__Output']['secret'] = 'Red'
    info['secret'] = '---'

    if instances is None or len(instances) != 1:
        info['instance'] = '---'
        return info
    
    info['instance'] = instances[0]['namespace_name']
    if instances[0]['ready']:
        info['__Output']['instance'] = 'Green'

    if iconfiguration is not None:
        info['secret'] = '\u2713'
        info['__Output']['secret'] = 'Green'

    return info


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False
    
    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            return False

    my_output.default('Collecting state', before_newline=True)
    my_output.default('- subscription')

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name']
    )
    if subscription is None:
        my_output.default('Subscription %s: %s' % (my_output.add_color('not found', 'Red'), params['__default__']['name']), before_newline=True)
        return True

    my_output.default('- instance')
    instances = params['k8s_handler'].get_intersights(cache_enabled=False)
    iconfiguration = params['k8s_handler'].get_secret(
        params['__default__']['namespace'],
        params['__default__']['secret'],
        cache_enabled=False
    )

    my_output.default('- pods')
    pods = params['k8s_handler'].get_pods(
        namespace=params['__default__']['namespace']
    )
    if pods is None:
        my_output.error('Failed to get cisco intersight pods information')
        return False

    my_output.default('- deployments')
    deployments = params['k8s_handler'].get_deployments(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if deployments is None:
        my_output.error('Failed to get cisco intersight deployments information')
        return False

    my_output.default('- daemon sets')
    daemon_sets = params['k8s_handler'].get_daemon_sets(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if daemon_sets is None:
        my_output.error('Failed to get cisco intersight deployments information')
        return False

    my_output.default('- operator console')
    console = params['k8s_handler'].get_operator_console('cluster', cache_enabled=False)
    if console is None:
        my_output.error('Failed to get operator console information')
        return False

    if 'state' in params['view']:
        info = {}
        info['__Output'] = {}
        
        info['package'] = subscription['packageT']
        info['csv'] = subscription['csvT']
        info['ready'] = params['k8s_handler'].get_ready_resources(
            pods=pods, 
            deployments=deployments, 
            daemon_sets=daemon_sets
        )
        info = params['k8s_handler'].add_tick(
            info,
            'ready',
            True,
            'readyTick'
        )
        info = get_instance_state(info, instances, iconfiguration)

        info = params['k8s_handler'].add_tick(
            info,
            'spec:plugins',
            'intersight-plugin',
            'consoleTick',
            managed_object=console
        )

        my_output.dictionary_ng(
            'State',
            info,
            [
                ['package', 'package'],
                ['csv', 'csv'],
                ['resources', 'readyTick'],
                ['instance', 'instance'],
                ['account registration', 'secret'],
                ['console plugin', 'consoleTick']
            ]
        )

    if 'details' in params['view']:
        ocp_common.print_subscription(subscription, my_output)
        if deployments is not None:
            k8s_output_handler.print_deployments_state(
                deployments
            )
        if daemon_sets is not None:
            k8s_output_handler.print_daemon_sets_state(
                daemon_sets
            )
        if pods is not None:
            k8s_output_handler.print_pods_state(
                pods, 
                skip=['Net', 'Restart', 'Svc']
            )

    return True
