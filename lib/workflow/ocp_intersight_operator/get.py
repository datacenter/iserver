import copy
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res'], None]
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


def collect_state_info(params, my_output):
    my_output.default('- instance')
    params['instances'] = params['k8s_handler'].get_intersights(cache_enabled=False)
    iconfiguration = params['k8s_handler'].get_secret(
        params['__default__']['namespace'],
        params['__default__']['secret'],
        cache_enabled=False
    )

    my_output.default('- operator console')
    params['console'] = params['k8s_handler'].get_operator_console('cluster', cache_enabled=False)
    if params['console'] is None:
        my_output.error('Failed to get operator console information')
        return False

    params['summary'] = get_instance_state(params['summary'], params['instances'], iconfiguration)
    params['summary'] = params['k8s_handler'].add_tick(
        params['summary'],
        'spec:plugins',
        'intersight-plugin',
        'consoleTick',
        managed_object=params['console']
    )

    return params


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

        params = ocp_common.get_operator(params, my_output)
        if params['subscription'] is None:
            return True

        params = collect_state_info(params, my_output)

        if 'state' in params['view']:
            my_output.dictionary_ng(
                'State',
                params['summary'],
                [
                    ['package', 'package'],
                    ['csv', 'csv'],
                    ['resources', 'readyTick'],
                    ['instance', 'instance'],
                    ['account registration', 'secret'],
                    ['console plugin', 'consoleTick']
                ]
            )

        if 'res' in params['view']:
            ocp_common.print_subscription(params['subscription'], my_output)
            ocp_common.print_resources(params, k8s_output_handler)

    return True
