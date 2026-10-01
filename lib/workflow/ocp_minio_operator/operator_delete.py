from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_minio_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['wipe', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is not None:
        params = local_common.collect_state_info(params, my_output)

        my_output.dictionary_ng(
            'MinIO Custom Resources',
            params['summary'],
            params['__default__']['resource_output']
        )

        if params['summary']['resources']:
            if not params['wipe']:
                my_output.error('Delete minio operator resources first')
                return False

            if params['wipe']:
                if not local_common.wipe(params, my_output):
                    return False
                
        success = params['k8s_handler'].delete_minio_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    success = ocp_common.delete_operator(
        params,
        my_output
    )
    if not success:
        return False
    
    return True