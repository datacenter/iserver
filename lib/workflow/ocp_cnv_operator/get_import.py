from lib import filter_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cnv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Container Virtualization Operator - Get Data Import Cron', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    my_output.default('Operator', underline=True, before_newline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- channel: %s' % (subscription['channel']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))

    my_output.default('HyperConverged', underline=True, before_newline=True)
    hc_info = params['k8s_handler'].get_hyperconverged(cache_enabled=False)
    if hc_info is None:
        my_output.default('- %s' % (my_output.add_color('no instance', 'Red')))
    else:
        my_output.default('- instance: %s' % (hc_info['name']))
        import_enabled = filter_helper.get(hc_info, 'spec:featureGates:enableCommonBootImageImport', on_error=False, on_none=False)
        if import_enabled:
            my_output.default('- data import cron: %s' % (my_output.add_color('enabled', 'Green')))
        else:
            my_output.default('- data import cron: %s' % (my_output.add_color('disabled', 'Red')))

    data_sources = params['k8s_handler'].get_data_sources(
        dv_info=True,
        pvc_info=True,
        cron_info=True,
        cache_enabled=False
    )
    if data_sources is None:
        my_output.error('DataSource crd failed')

    k8s_output_handler.print_data_sources(data_sources)

    data_volumes = params['k8s_handler'].get_data_volumes(
        object_filter=['cron:true'],
        cache_enabled=False
    )
    if data_volumes is None:
        my_output.error('DataVolume crd failed')

    k8s_output_handler.print_data_volumes(data_volumes)

    pvcs = params['k8s_handler'].get_pvcs(
        object_filter=['cron:true'],
        cache_enabled=False
    )
    if pvcs is None:
        my_output.error('PersistentVolumeClaim crd failed')

    k8s_output_handler.print_pvcs(pvcs)

    return True
