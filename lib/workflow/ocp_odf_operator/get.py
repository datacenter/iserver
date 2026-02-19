import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_odf_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'view',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.augment_params(params)

    my_output.default('Workflow Parameters', underline=True)
    my_output.default(json.dumps(params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = True
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    if 'state' in params['view']:
        my_output.default('Operator', underline=True)
        my_output.default('- subscription: %s' % (subscription['namespace_name']))
        my_output.default('- channel: %s' % (subscription['channel']))
        my_output.default('- csv: %s' % (subscription['installed_csv']))
        
        csv = params['k8s_handler'].get_cluster_service_version(
            subscription['namespace'],
            subscription['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv is None:
            my_output.debug('[WARNING] CSV not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))

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
