from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    subnet_rules = [
        ['name', True, None, 'str', None, None, None, None],
        ['cidr', False, None, 'list-of-cidr', 1, None, None, None],
        ['route', True, None, 'list-of-dict', None, None, None, None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['subnet', False, None, 'list-of-dict', 1, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(
        params, 
        rules, 
        extras=['__type__'], 
        nested=dict(subnet=subnet_rules)
    )
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, add_defaults=False, copy_handler=False), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - Cilium Private Network - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False

    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network %s' % (my_output.add_color('must be enabled first', 'Red')))
        return False
    
    my_output.default('Cilium private network feature %s' % (my_output.add_color('enabled', 'Green')))

    success = params['k8s_handler'].create_clusterwide_private_network(
        params['network'], 
        params['subnet'], 
        inb=params['inb'], 
        gatewayv4=params['gateway'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- cilium private network created')
    return True
