from lib import ip_helper
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_butane_cli import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'url' not in params:
        params['url'] = None

    if params['url'] is None:
        params['url'] = 'https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-amd64'

    if 'overwrite' not in params:
        params['overwrite'] = False

    if not isinstance(params['overwrite'], bool):
        return None, 'overwrite param must be true or false'
    
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
        'overwrite',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Install butane cli', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['overwrite']:
        success = params['ssh_handler'].is_file('/usr/local/bin/butane')
        if success:
            my_output.default('/usr/local/bin/butane found and overwrite not enforced')
            return True
        
    my_output.default('Downloading butane binary from %s' % (params['url']))
    filename = ip_helper.download_url(
        params['url'],
        file_helper.get_tmp_filename()
    )
    if filename is None:
        my_output.error('Download failed')
        return False

    my_output.default('Uploading butane binary to cluster management node')
    success = params['ssh_handler'].scp_file(
        filename,
        filename
    )
    if not success:
        my_output.error('Upload failed')
        return False

    my_output.default('Copy butane to /usr/local/bin')
    success, output, error = params['ssh_handler'].run_cmd(
        'sudo sudo mv %s /usr/local/bin/butane' % (filename)
    )
    if not success:
        my_output.error('File copy failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default('Change file flags')
    success, output, error = params['ssh_handler'].run_cmd(
        'sudo chmod a+x /usr/local/bin/butane'
    )
    if not success:
        my_output.error('Command failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    success, output, error = params['ssh_handler'].run_cmd(
        'butane --version'
    )
    if not success:
        my_output.error('Command failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default(output, wrap='~~~', before_newline=True)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- butane installed')

    return True
