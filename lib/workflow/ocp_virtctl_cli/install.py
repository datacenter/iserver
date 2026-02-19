import json
from lib import ip_helper
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'url' not in params:
        params['url'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Install virtctl cli', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    my_output.default('Workflow Parameters', underline=True)
    my_output.default(json.dumps(params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-fixup'] = True
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['linux_handler'] = ocp_params['data']['management_handler']

    if not params['k8s_handler'].is_cnv_subscription('openshift-cnv', 'kubevirt-hyperconverged', cache_enabled=False):
        my_output.error('Cnv operator required')
        return False
    
    my_output.default('Cnv operator installed')

    if not params['k8s_handler'].is_hyperconverged(cache_enabled=False):
        my_output.error('Cnv hyperconverged instance required')
        return False
    
    my_output.default('Cnv hyperconverged instance created')

    if params['url'] is None:
        config_info = params['k8s_handler'].get_ingress_config()
        if config_info is None or config_info['info']['domain'] is None:
            my_output.error('Failed to get cluster ingress domain name')
            return False

        params['url'] = 'https://hyperconverged-cluster-cli-download-openshift-cnv.%s/amd64/linux/virtctl.tar.gz' % (
            config_info['info']['domain']
        )

    if 'hyperconverged-cluster-cli-download-openshift-cnv' in params['url']:
        my_output.default('Check for cluster endpoint to download virtctl binary from [timeout:30]...')
        success = params['k8s_handler'].wait_endpoint(
            'openshift-cnv',
            'hyperconverged-cluster-cli-download',
            my_output=my_output,
            max_time=30
        )
        if not success:
            my_output.error('endpoint not ready')
            return False

    my_output.default('Downloading virtctl binary from %s' % (params['url']))
    filename = ip_helper.download_url(
        params['url'],
        file_helper.get_tmp_filename(),
        verify=False
    )
    if filename is None:
        my_output.error('Download failed')
        return False

    my_output.default('Uploading virtctl binary to cluster management node')
    success = params['linux_handler'].scp_file(
        filename,
        filename
    )
    if not success:
        my_output.error('Upload failed')
        return False

    my_output.default('Unpack')
    success, output, error = params['linux_handler'].run_cmd(
        'sudo tar xzvfC %s /usr/local/bin' % (filename)
    )
    if not success:
        my_output.error('Unpack failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default('Change file flags')
    success, output, error = params['linux_handler'].run_cmd(
        'sudo chmod a+x /usr/local/bin/virtctl'
    )
    if not success:
        my_output.error('Command failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    success, output, error = params['linux_handler'].run_cmd(
        'virtctl version'
    )
    if not success:
        my_output.error('Command failed')
        my_output.default(str(output))
        my_output.default(str(error))
        return False

    my_output.default('Virtctl binary ready to be used')
    my_output.default(output)

    return True
