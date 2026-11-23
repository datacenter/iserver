from lib import output_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_cli import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['url', True, None, 'str', None, None, None, None],
        ['version', True, None, 'str', None, None, None, None],
        ['overwrite', False, False, 'bool', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Add tridentctl')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    if params['url'] is None:
        if params['version'] is None:
            my_output.error('Define url or version for tridentctl download: https://github.com/NetApp/trident/releases')
            return False
        
        params['url'] = 'https://github.com/NetApp/trident/releases/download/v%s/trident-installer-%s.tar.gz' % (
            params['version'],
            params['version'],
        )        

    success = params['ssh_handler'].upload_binary_from_source(
        'tridentctl', 
        params['url'], 
        format='tar.gz',
        package_binary='trident-installer/tridentctl',
        target_path='/usr/local/bin', 
        chmod=True, 
        test='tridentctl --help',
        overwrite=params['overwrite'],
        my_output=my_output
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- tridentctl installed')
    return True