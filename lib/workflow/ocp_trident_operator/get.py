import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_trident_operator import common as local_common
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


def collect_state_info(params, my_output):
    my_output.debug('- instance')
    params['instance'] = None
    params['summary']['instanceReady'] = False
    instances = params['k8s_handler'].get_trident_orchestrators(cache_enabled=False)
    if instances is not None and len(instances) == 1:
        params['instance'] = instances[0]
        params['summary']['instanceInstalled'] = params['instance']['installed']

    params['summary'] = params['k8s_handler'].add_tick(
        params['summary'],
        'instanceInstalled',
        True,
        'instanceTick'
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
            continue

        params = collect_state_info(params, my_output)

        if 'state' in params['view']:
            my_output.dictionary_ng(
                'State',
                params['summary'],
                [
                    ['package', 'package'],
                    ['csv', 'csv'],
                    ['resources', 'readyTick'],
                    ['instance', 'instanceTick']
                ]
            )

        if 'res' in params['view']:
            pass

    return True