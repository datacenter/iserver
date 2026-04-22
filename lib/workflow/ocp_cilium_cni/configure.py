from lib import output_helper
from lib import file_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', False, None, 'file-k8s', None, None, None, None],
        ['rollback', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Set configuration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    content = file_helper.get_file_yaml(params['filename'])
    if file_helper.is_kube_kind(content, kind='CiliumConfig', namespace='cilium', spec=True):  
        config_content = content['spec']
    else:
        config_content = content

    success = params['k8s_handler'].update_cilium_config(
        config_content, 
        my_output=my_output, 
        rollback=params['rollback'], 
        wait=params['wait'], 
        confirmation=params['confirmation']
    )

    if success:
        my_output.default('Configuration updated %s' % (my_output.add_color('successfully', 'Green')), before_newline=True, after_newline=True)
    else:
        my_output.default('Configuration update %s' % (my_output.add_color('failed', 'Red')), before_newline=True, after_newline=True)
        
    return success
