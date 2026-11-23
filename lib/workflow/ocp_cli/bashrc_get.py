import copy
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cli import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state'], None]
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

        ocp_common.print_title(params, my_output, 'Get .bashrc')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
        if params is None:
            return False
            
        my_output.default('Download /var/home/core/.bashrc')
        filename = file_helper.get_tmp_filename()
        success = params['ssh_handler'].scp_file(
            '/var/home/core/.bashrc',
            filename,
            put=False
        )
        if not success:
            my_output.error('Download failed')
            continue

        content = file_helper.get_file_text(filename)
        if content is None:
            my_output.error('Failed to read downloaded file: %s' % (filename))
            continue

        my_output.default(content, wrap='~~~')

    return True