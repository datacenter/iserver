import json
import time
from lib import output_helper
from lib import file_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import agent_exec


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'filename' not in params:
        return None, 'Target configuration filename required'

    content = file_helper.get_file_yaml(params['filename'])
    if content is None:
        return None, 'Target yaml configuration filename not found'

    if file_helper.is_kube_kind(content, kind='CiliumConfig', namespace='cilium', spec=True):  
        params['content'] = content['spec']
    else:
        params['content'] = content

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'rollback' not in params:
        params['rollback'] = True

    if not isinstance(params['rollback'], bool):
        return None, 'rollback param must be true or false'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'filename',
        'content',
        'wait',
        'confirmation',
        'rollback',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Set configuration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].update_cilium_config(
        params['content'], 
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
