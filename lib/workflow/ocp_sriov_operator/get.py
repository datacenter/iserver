import copy
import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_sriov_operator import common as local_common
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

        subscription = params['k8s_handler'].get_subscription_by_package(
            params['__default__']['name'],
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            my_output.default('Operator not found: %s' % (params['__default__']['name']))
            continue
        
        my_output.default('Operator', underline=True)
        my_output.default('- subscription: %s' % (subscription['namespace_name']))
        my_output.default('- channel: %s' % (subscription['channel']))
        my_output.default('- csv: %s' % (subscription['installed_csv']))
        
        config = params['k8s_handler'].get_sriov_operator_config(cache_enabled=False)
        if config is None:
            my_output.default('SRIOV operator configuration (instance) not defined', before_newline=True)
            continue
        
        my_output.default('SRIOV operator configuration', before_newline=True, underline=True)
        my_output.default('- namespace: %s' % (config['namespace']))
        my_output.default('- name: %s' % (config['name']))
        
        my_output.default(json.dumps(config['spec'], indent=4), wrap='~~~', before_newline=True)

    return True
