from lib import output_helper
from lib.workflow.ocp_helm_cli import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'view' not in params or params['view'] is None:
        params['view'] = ['list']

    if not isinstance(params['view'], list):
        return None, 'view must be list'

    if len(params['view']) == 0:
        params['view'] = ['list']

    for item in params['view']:
        if item not in ['list', 'ver']:
            return None, 'unsupported view %s' % (item)
        
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

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
        'url',
        'view',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Check helm cli', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if 'ver' in params['view']:
        success, output, error = params['ssh_handler'].run_cmd(
            'helm version'
        )
        if not success:
            my_output.error('Command failed')
            my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
            return False

        my_output.default(str(output), wrap='~~~')

    if 'list' in params['view']:
        success, output, error = params['ssh_handler'].run_cmd(
            'helm ls -A'
        )
        if not success:
            my_output.error('Command failed')
            my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
            return False

        my_output.default(str(output), wrap='~~~')
        
    return True
