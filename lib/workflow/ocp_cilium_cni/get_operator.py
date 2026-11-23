import copy
import yaml
from lib.k8s import output as k8s_output
from lib import output_helper
from lib import filter_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['pod'], 'view', None, None, ['pod', 'config', 'logs'], None]
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

        ocp_common.print_title(params, my_output, 'Get operator')
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            continue

        if 'config' in params['view']:
            cilium_config = params['k8s_handler'].get_cilium_config()
            if cilium_config is None:
                my_output.error('Failed to get cilium configuration')
            else:
                operator_config = filter_helper.get(cilium_config, 'spec:operator')
                if operator_config is None:
                    my_output.error('Failed to get operator spec in cilium configuration')
                else:
                    my_output.default('Operator Configuration', underline=True, before_newline=True)
                    my_output.default(
                        yaml.safe_dump(dict(operator=operator_config)),
                        wrap='~~~'
                    )

        if 'pod' in params['view']:
            local_common.show_operators(params, my_output, k8s_output_handler)

        if 'logs' in params['view']:
            lease = params['k8s_handler'].get_lease(
                params['namespace'],
                params['operator-lease'],
                cache_enabled=False
            )

            success, namespace, name, logs = params['k8s_handler'].get_cilium_operator_leader_logs(
                lease, 
                cache_enabled=False
            )
            if not success:
                my_output.error('Failed to get cilium operator leader logs')
            else:
                my_output.default('Cilium Operator Leader [%s/%s]' % (namespace, name), underline=True, before_newline=True)
                my_output.default(logs, wrap='~~~')

    return True
