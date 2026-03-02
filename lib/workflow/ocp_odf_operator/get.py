import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_odf_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'view' not in params or params['view'] is None:
        params['view'] = ['state']

    if not isinstance(params['view'], list):
        return None, 'view must be list'

    if len(params['view']) == 0:
        params['view'] = ['state']

    for item in params['view']:
        if item not in ['state', 'crd', 'ocs']:
            return None, 'unsupported view %s' % (item)
        
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'    
        
    allowed_keys = [
        'cluster',
        'view',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if not state['installed']:
        return True

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    if 'state' in params['view']:
        crds = local_common.get_odf_crd(
            params['k8s_handler'], 
            my_output=my_output,
            crd=['StorageCluster', 'CephCluster', 'PersistentVolume', 'PersistentVolumeClaim']
        )
        local_common.print_odf_crd(
            crds, 
            k8s_output_handler, 
            crd=['StorageCluster', 'CephCluster', 'PersistentVolume', 'PersistentVolumeClaim'],
            only_non_zero=False
        )

    if 'crd' in params['view']:
        crds = local_common.get_odf_crd(
            params['k8s_handler'], 
            my_output=my_output
        )
        local_common.print_odf_crd(
            crds, 
            k8s_output_handler
        )

    if 'ocs' in params['view']:
        subscription = params['k8s_handler'].get_ocs_operator_subscription(
            csv_info=True,
            deployment_info=True,
            replica_set_info=True,
            cache_enabled=False
        )
        if subscription is None:
            my_output.default('Operator ocs-operator not found')
            return True

        k8s_output_handler.print_subscription(subscription)
        k8s_output_handler.print_cluster_service_version(subscription['csv'])
        k8s_output_handler.print_deployment(subscription['deployment'])
        k8s_output_handler.print_replica_sets([subscription['replica_set']])

    return True
