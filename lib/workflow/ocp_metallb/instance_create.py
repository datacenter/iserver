from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_metallb import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, None, None],
        ['bgp', True, None, 'str', None, None, ['', 'native', 'frr', 'frr-k8s'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - MetalLB Operator - Create instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )
    if subscription is None:
        return False

    ready = params['k8s_handler'].is_subscription_metallb_ready(with_instance=False, my_output=my_output, details=True)
    if not ready:
        return False

    if params['k8s_handler'].is_any_metallb(cache_enabled=False):
        my_output.default('Metallb instance already defined', before_newline=True, after_newline=True)
        return True

    my_output.default('No metallb instance currently defined', before_newline=True, after_newline=True)

    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get metallb instance: %s' % (params['filename']))
            return False

    if instance_body is None:
        instance_body = params['k8s_handler'].get_metallb_body()
        if len(params['bgp']) > 0:
            if 'spec' not in instance_body:
                instance_body['spec'] = {}
                instance_body['spec']['bgpBackend'] = params['bgp']

    success = params['k8s_handler'].create_metallb(
        instance_body, 
        my_output=my_output, 
        confirmation=params['confirmation'], 
        wait=params['wait']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- MetalLB instance created')

    return True
