import copy
from lib import output_helper
from lib.workflow.ocp_cli import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['list'], 'view', None, None, ['list', 'ver'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get helm')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
        if params is None:
            return False

        if 'ver' in params['view']:
            success, output, error = params['ssh_handler'].run_cmd(
                'helm version'
            )
            if not success:
                my_output.error('Command failed')
                my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
                continue

            my_output.default(str(output), wrap='~~~')

        if 'list' in params['view']:
            success, output, error = params['ssh_handler'].run_cmd(
                'helm ls -A'
            )
            if not success:
                my_output.error('Command failed')
                my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
                continue

            my_output.default(str(output), wrap='~~~')

    return True