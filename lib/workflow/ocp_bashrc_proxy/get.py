from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-fixup'] = True
    ocp_check_params['verbose'] = True
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    my_output.default('Download /var/home/core/.bashrc')
    filename = file_helper.get_tmp_filename()
    success = ocp_params['data']['management_handler'].scp_file(
        '/var/home/core/.bashrc',
        filename,
        put=False
    )
    if not success:
        my_output.error('Download failed')
        return False

    content = file_helper.get_file_text(filename)
    if content is None:
        my_output.error('Failed to read downloaded file: %s' % (filename))
        return False

    my_output.default(content)
    return True
