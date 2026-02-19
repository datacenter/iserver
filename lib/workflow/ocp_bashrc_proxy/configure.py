import json
from lib import file_helper
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_bashrc_proxy import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'http_proxy' not in params:
        params['http_proxy'] = None

    if 'https_proxy' not in params:
        params['https_proxy'] = None

    if 'no_proxy' not in params:
        params['no_proxy'] = None

    if 'inherit' not in params:
        params['inherit'] = False

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'http_proxy',
        'https_proxy',
        'no_proxy',
        'inherit',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - .bashrc proxy settings', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['inherit']:
        proxy_mo = params['k8s_handler'].get_proxy(return_mo=True)
        if proxy_mo is None:
            my_output.error('Failed to cluster proxy settings')
            return False
        
        params['http_proxy'] = proxy_mo['status']['httpProxy']
        params['https_proxy'] = proxy_mo['status']['httpsProxy']
        params['no_proxy'] = proxy_mo['status']['noProxy']

        my_output.default('Proxy settings inherited from cluster proxy')
        my_output.default('http_proxy: %s' % (params['http_proxy']))
        my_output.default('https_proxy: %s' % (params['https_proxy']))
        my_output.default('no_proxy: %s' % (params['no_proxy']))

    my_output.default('Download /var/home/core/.bashrc')
    filename = file_helper.get_tmp_filename()
    success =  params['ssh_handler'].scp_file(
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

    if params['http_proxy'] is None:
        my_output.default('http proxy settings will be removed')
        new_lines = []
        for line in content.split('\n'):
            if filter_helper.match_string('export http_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            if filter_helper.match_string('export https_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            if filter_helper.match_string('export no_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            new_lines.append(line)

        content = '\n'.join(new_lines)
    else:
        my_output.default('http proxy settings will be added/replaced')

        new_lines = []
        for line in content.split('\n'):
            if filter_helper.match_string('export http_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            if filter_helper.match_string('export https_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            if filter_helper.match_string('export no_proxy=*', line.lower()):
                my_output.default('removed line [%s]' % (line))
                continue

            new_lines.append(line)

        new_lines.append('')

        line = 'export HTTP_PROXY=%s' % (params['http_proxy'])
        my_output.default('added line [%s]' % (line))
        new_lines.append(line)

        line = 'export HTTPS_PROXY=%s' % (params['https_proxy'])
        my_output.default('added line [%s]' % (line))
        new_lines.append(line)

        line = 'export NO_PROXY=%s' % (params['no_proxy'])
        my_output.default('added line [%s]' % (line))
        new_lines.append(line)

        new_lines.append('')

        content = '\n'.join(new_lines)

    success = file_helper.set_file(filename, content)
    if not success:
        my_output.error('Failed to set local file: %s' % (filename))
        return False

    my_output.default('Upload /var/home/core/.bashrc')
    success = params['ssh_handler'].scp_file(
        filename,
        '/var/home/core/.bashrc'
    )
    if not success:
        my_output.error('Upload failed')
        return False

    my_output.default('.bashrc uploaded with proxy settings')

    success, output, error = params['ssh_handler'].run_cmd("sed -i 's/\r$//' /var/home/core/.bashrc")
    if not success:
        my_output.error('Failed to remove carriage returns')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    return True
