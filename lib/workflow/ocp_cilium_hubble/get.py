import copy
import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_hubble import common as cilium_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'config', 'res'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=cilium_common.get_default_params()), None


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
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            continue

        cinfo = params['k8s_handler'].get_cilium_timescape_config_info(my_output=my_output)
        if cinfo is None or not cinfo['summary']['timescape']:
            my_output.default('Hubble/timescape ui %s' % (my_output.add_color('not enabled', 'Red')))
            continue

        rinfo = params['k8s_handler'].get_cilium_timescape_resources_info(my_output=my_output)

        if 'config' in params['view']:
            my_output.default('Cilium configuration', before_newline=True, after_newline=True, underline=True)
            my_output.default(yaml.dump(cinfo['config']), wrap='~~~')

        if 'res' in params['view']:
            if rinfo['pod'] is not None:
                k8s_output_handler.print_pods_state(rinfo['pod'])
            if rinfo['service'] is not None:
                k8s_output_handler.print_services(rinfo['service'])
            if rinfo['endpoint'] is not None:
                k8s_output_handler.print_endpoints(rinfo['endpoint'])

    return True