from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if '__id__' not in params:
        params['__id__'] = None

    if 'namespace' not in params or params['namespace'] is None:
        return None, 'Namespace required'

    if 'name' not in params or params['name'] is None:
        return None, 'Name required'

    if params['name'].endswith('-') and params['__id__'] is not None:
        params['name'] = '%s%s' % (
            params['name'],
            params['__id__']
        )

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys = [
        'cluster',
        '__id__',
        'namespace',
        'name',
        'wait',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Service - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].delete_service(
        params['namespace'], 
        params['name'], 
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False

    return True
