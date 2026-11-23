import copy
import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_odf_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res', 'ocs'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def collect_state_info(params, my_output):
    my_output.debug('- odf')

    params['odf_installed'] = params['k8s_handler'].check_odf_subscription(
        params['__default__']['name'], 
        my_output=my_output,
        check_ready=False
    )

    if params['odf_installed']:
        params['odf_ready'] = params['k8s_handler'].is_subscription_odf_ready(my_output=my_output)

    if 'state' in params['view']:
        params['crd'] = local_common.get_odf_crd(
            params['k8s_handler'], 
            my_output=my_output,
            crd=['StorageCluster', 'CephCluster', 'PersistentVolume', 'PersistentVolumeClaim']
        )

    if 'res' in params['view']:
        params['crd'] = local_common.get_odf_crd(
            params['k8s_handler'], 
            my_output=my_output
        )

    if 'ocs' in params['view']:
        params['ocs'] = params['k8s_handler'].get_ocs_operator_subscription(
            csv_info=True,
            deployment_info=True,
            replica_set_info=True,
            cache_enabled=False
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
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_optional=True)
        if params is None:
            continue

        params = ocp_common.get_operator(params, my_output, csv=True)
        if params['subscription'] is None:
            continue

        params = collect_state_info(params, my_output)

        if 'state' in params['view']:
            local_common.print_odf_crd(
                params['crd'], 
                k8s_output_handler, 
                crd=['StorageCluster', 'CephCluster', 'PersistentVolume', 'PersistentVolumeClaim'],
                only_non_zero=False
            )

        if 'res' in params['view']:
            local_common.print_odf_crd(
                params['crd'], 
                k8s_output_handler
            )

        if 'ocs' in params['view']:
            if params['ocs'] is None:
                my_output.default('Operator ocs-operator not found')
                continue

            k8s_output_handler.print_subscription(params['ocs'])
            k8s_output_handler.print_cluster_service_version(params['ocs']['csv'])
            k8s_output_handler.print_deployment(params['ocs']['deployment'])
            k8s_output_handler.print_replica_sets([params['ocs']['replica_set']])

    return True
