from lib import file_helper
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', False, None, 'list-of-str', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Create Policy')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_tetragon_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.default('Tetragon Operator %s' % (my_output.add_color('not installed', 'Red')))
        return True

    contents = file_helper.get_k8s_files(
        params['filename'],
        base_directory=params['base_directory'],
        kind=local_common.get_tetragon_crds()
    )
    
    for content in contents:
        my_output.default('File: %s' % (content['filename']))
        if content['yaml']['kind'] == 'AlertRule':
            success = params['k8s_handler'].create_alert_rule(
                content['yaml'],
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if content['yaml']['kind'] == 'SandboxPolicy':
            success = params['k8s_handler'].create_sandbox_policy(
                content['yaml'],
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if content['yaml']['kind'] == 'SandboxPolicyNamespaced':
            if filter_helper.get(content['yaml'], 'metadata:namespace') is None:
                my_output.error('Namespace metadata required')
                return False
            
            success = params['k8s_handler'].create_sandbox_policy_namespaced(
                content['yaml'],
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if content['yaml']['kind'] == 'TracingPolicy':
            success = params['k8s_handler'].create_tracing_policy(
                content['yaml'],
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

        if content['yaml']['kind'] == 'TracingPolicyNamespaced':
            if filter_helper.get(content['yaml'], 'metadata:namespace') is None:
                my_output.error('Namespace metadata required')
                return False

            success = params['k8s_handler'].create_tracing_policy_namespaced(
                content['yaml'],
                my_output=my_output,
                confirmation=params['confirmation'],
                wait=True
            )
            if not success:
                return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- CRDs applied')
    return True