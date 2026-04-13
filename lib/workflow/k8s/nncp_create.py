from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common
from lib.workflow.k8s import nncp_generate


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['node', True, '__all__', 'str', None, None, None, None],
        ['policy', True, 'my-policy', 'str', None, None, None, None],
        ['delete', True, True, 'bool', None, None, None, None],
        ['check', True, True, 'bool', None, None, None, None],
        ['timeout', True, 360, 'int', None, None, None, None],
        ['interfaces', True, [], 'list-of-dict', None, None, None, None],
        ['routes', True, [], 'list-of-dict', None, None, None, None],
        ['ovn', True, [], 'list-of-dict', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params
        
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Kubernetes Workflow - Node Network Configuration Policy (NNCP) - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    body = nncp_generate.run(params, my_output)
    if body is None:
        return False

    success = params['k8s_handler'].create_node_network_configuration_policy(
        body['nncp'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True,
        max_time=params['timeout']
    )
    if not success:
        return False
    
    if params['delete']:
        success = params['k8s_handler'].delete_node_network_configuration_policy_mo(
            body['nncp']['metadata']['name']
        )
        if not success:
            my_output.error('Delete rest api failed')
            return False
        
        my_output.default('NNCP %s deleted' % (body['nncp']['metadata']['name']))

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- node network configuration policy created')
    return True
