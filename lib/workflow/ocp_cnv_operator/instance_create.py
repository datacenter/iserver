from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cnv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create HyperConverged Instance')
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
            
    if not params['k8s_handler'].is_subscription_cnv_ready():
        my_output.error('Cnv Operator not ready')
        return False
        
    my_output.default('Cnv operator ready', before_newline=True)
    
    if params['k8s_handler'].is_hyperconverged(cache_enabled=False):
        my_output.default('HyperConverged instance already defined')

        if not params['k8s_handler'].is_instance_cnv_ready():
            my_output.error('HyperConverged not ready')
            return False
            
        my_output.default('HyperConverged instance ready', before_newline=True)
        return True

    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get cnv instance: %s' % (params['filename']))
            return False
        
    if params['filename'] is None:
        instance_body = params['k8s_handler'].get_package_channel_example(
            params['__default__']['name'], 
            params['__default__']['catalog'],
            subscription['channel'],
            'HyperConverged'
        )   
        if instance_body is None:
            my_output.error('Failed to get HyperConverged reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_hyperconverged(
        instance_body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- HyperConverged instance created and ready')
    return True