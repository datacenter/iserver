from lib import ip_helper
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_bashrc_proxy import configure
from lib.workflow.ocp_helm_cli import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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

    success, output, error = params['ssh_handler'].run_cmd(
        'helm version'
    )
    if not success:
        my_output.error('Command failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False

    my_output.default('Helm found and ready')
    my_output.default(str(output), wrap='~~~')
    return True
