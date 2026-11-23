import copy
from lib.k8s import output as k8s_output
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_cnv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'import', 'crd'], None]
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

        params = local_common.collect_state_info(params)

        if 'state' in params['view']:
            local_common.print_state_summary(params, my_output)

            crds = local_common.get_cnv_crd(
                params['k8s_handler'], 
                crd=['CDI', 'NetworkAddonsConfig']
            )
            local_common.print_cnv_crd(
                crds, 
                k8s_output_handler, 
                crd=['CDI', 'NetworkAddonsConfig'],
                only_non_zero=False
            )
            
        if 'import' in params['view']:
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

        if 'crd' in params['view']:
            crds = local_common.get_cnv_crd(
                params['k8s_handler'], 
                my_output=my_output, 
                cache_enabled=False, 
                message_on_error=True
            )
            
            local_common.print_cnv_crd(
                crds, 
                k8s_output_handler, 
                only_non_zero=True, 
                crd=['__all__']
            )

    return True
