from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_nfd_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Create Instance')
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
            
    if params['k8s_handler'].is_any_node_feature_discovery(cache_enabled=False):
        my_output.default('Node Feature Discovery instance %s' % (my_output.add_color('already defined', 'Green')))
        return True

    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get nfd instance: %s' % (params['filename']))
            return False

    if instance_body is None:
        instance_body = params['k8s_handler'].get_package_channel_example(
            params['__default__']['name'], 
            params['__default__']['catalog'],
            subscription['channel'],
            'NodeFeatureDiscovery'
        )        
        if instance_body is None:
            my_output.error('Failed to get NodeFeatureDiscovery reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_node_feature_discovery(
        instance_body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Node feature discovery instance created')
    my_output.default('- Note annotations found')
    return True
