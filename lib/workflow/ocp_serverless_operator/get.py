import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_serverless_operator import common as local_common
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
    my_output.debug('- knative eventing')
    params['eventing'] = params['k8s_handler'].get_knative_eventings(cache_enabled=False)
    params['summary']['eventing'] = '---'
    if params['eventing'] is not None:
        params['summary']['eventing'] = len(params['eventing'])

    my_output.debug('- knative serving')
    params['serving'] = params['k8s_handler'].get_knative_servings(deployment_info=True, cache_enabled=False)
    params['summary']['serving'] = '---'
    if params['serving'] is not None:
        params['summary']['serving'] = len(params['serving'])
    
    my_output.debug('- knative kafka')
    params['kafka'] = params['k8s_handler'].get_knative_kafkas(cache_enabled=False)
    params['summary']['kafka'] = '---'
    if params['kafka'] is not None:
        params['summary']['kafka'] = len(params['kafka'])

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
                    ['resources', 'readyTick']
                ]
            )

            my_output.dictionary_ng(
                'Serverless Custom Resources',
                params['summary'],
                [
                    ['eventing', 'eventing'],
                    ['serving', 'serving'],
                    ['kafka', 'kafka']
                ]
            )

        if 'res' in params['view']:
            k8s_output_handler.print_knative_eventings(params['eventing'])
            k8s_output_handler.print_knative_servings(params['serving'])
            k8s_output_handler.print_knative_kafkas(params['kafka'])

    return True