import copy
import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow import ocp_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'config'], None]
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

        if not cilium_common.is_cilium(params, my_output):
            continue
        
        if not params['k8s_handler'].is_cilium_mesh_enabled():
            my_output.default('Cluster mesh %s' % (my_output.add_color('not enabled', 'Red')))
            continue
        
        my_output.default('Cluster mesh %s' % (my_output.add_color('enabled', 'Green')))

        if 'config' in params['view']:
            mesh_config = params['k8s_handler'].get_cilium_mesh_configuration()
            my_output.default('Cluster mesh configuration', after_newline=True)
            my_output.default(yaml.dump(mesh_config), wrap='~~~')

        if 'state' in params['view']:
            status = params['k8s_handler'].get_cilium_mesh_status()
            k8s_output_handler.print_cilium_mesh_status(status)

    return True