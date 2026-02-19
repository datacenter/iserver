from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose params must be true or false'
    
    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Get HTPasswd Identity Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    providers = params['k8s_handler'].get_identity_providers_htpasswd(cache_enabled=False)
    if providers is None or len(providers) == 0:
        my_output.default(
            'Identity htpasswd not defined'
        )
        return True

    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    k8s_output_handler.print_oauths_htpasswd(providers)

    return True
