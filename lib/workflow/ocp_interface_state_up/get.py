from lib import output_helper
from lib.workflow import netshoot_helper
from lib.workflow import ocp_common as workflow_common


def validate(params, log_id=None):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['silent', True, True, 'bool', None, None, None, None],        
        ['always-delete', True, True, 'bool', None, None, None, None], 
        ['view', True, ['up'], 'view', None, None, ['up'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = None
    if not params['silent']:
        my_output = output_helper.OutputHelper(log_id=log_id)

    params = validate(params, log_id=log_id)
    if params is None:
        return None

    params = ocp_common.workflow_init(params, my_output, log_id)

    params = netshoot_helper.create_netshoots(params, my_output=my_output)
    if params is None:
        return None
    
    response = {}

    if 'up' in params['view']:
        commands = []
        commands.append(dict(key='ip', cmd='ip link show'))

        output = netshoot_helper.run_netshoot_cli(
            params, 
            commands, 
            my_output=my_output, 
            always_delete=False
        )
        if output is not None:
            return None

        response['up'] = {}
        for node_name in output:
            response['up'][node_name] = {}
            for interface in output[node_name]:
                response['up'][node_name][interface['name']] = interface['up']

    if params['netshoot_created'] and not params['always_delete'] or params['always_delete']:
        netshoot_helper.delete_netshoots(params, my_output=my_output)
        del params['netshoot']
        del params['netshoot_created']

    return response