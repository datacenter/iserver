import copy
import json
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res', 'webhook', 'db', 'ep'], None]
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
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            continue
        
        if 'state' in params['view']:
            params = local_common.collect_state_info(params)
            params = local_common.collect_db_state_info(params)
            local_common.print_state(params, my_output)
            if params['state']['enabled']:
                local_common.print_resource_summary(params, my_output)     
                local_common.print_db_summary(params, my_output)       

        if 'webhook' in params['view']:
            pass

        if 'res' in params['view']:
            params = local_common.collect_state_info(params)
            local_common.print_resource_summary(params, my_output)
            local_common.print_resources(params, k8s_output_handler)

        if 'db' in params['view']:
            params = local_common.collect_db_state_info(params)
            local_common.print_db_summary(params, my_output)
            local_common.print_dbs(params, k8s_output_handler)

        if 'ep' in params['view']:
            params = local_common.collect_db_state_info(params, db_name='privnet-endpoints')
            local_common.print_dbs(params, k8s_output_handler)            

    return True