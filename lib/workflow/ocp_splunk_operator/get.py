from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Splunk Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    subscription = global_common.get_subscription(
        params['k8s_handler'], 
        params['name'], 
        my_output=my_output
    )
    if subscription is None:
        return True
    
    standalones = params['k8s_handler'].get_splunk_standalones(
        pod_info=True,
        pvc_info=True,
        service_info=True,
        route_info=True,
        secret_info=True
    )
    if standalones is not None:
        k8s_output_handler.print_standalones(standalones)

    return True
