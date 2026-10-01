
import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common
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
    
        params = local_common.collect_state_info(params, my_output)

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
                'Splunk Custom Resources',
                params['summary'],
                params['__default__']['resource_output']
            )

        if 'res' in params['view']:
            my_output.dictionary_ng(
                'Splunk Custom Resources',
                params['summary'],
                params['__default__']['resource_output']
            )

            for key in params['__default__']['resource_keys']:
                if params[key] is None:
                    continue

                if len(params[key]) == 0:
                    continue

                getattr(k8s_output_handler, 'print_splunk_%ss_state' % (key))(params[key])

    return True