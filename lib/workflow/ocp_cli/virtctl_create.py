from lib import output_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_cli import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['url', True, None, 'str', None, None, None, None],
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

    ocp_common.print_title(params, my_output, 'Add virtctl')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_hyperconverged(cache_enabled=False):
        my_output.error('Cnv hyperconverged instance required')
        return False

    if params['url'] is None:
        config_info = params['k8s_handler'].get_ingress_config()
        if config_info is None or config_info['domain'] is None:
            my_output.error('Failed to get cluster ingress domain name')
            return False

        params['url'] = 'https://hyperconverged-cluster-cli-download-openshift-cnv.%s/amd64/linux/virtctl.tar.gz' % (
            config_info['domain']
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
        
    success = params['ssh_handler'].upload_binary_from_source(
        'virtctl', 
        params['url'], 
        format='tar.gz',
        target_path='/usr/local/bin', 
        chmod=True, 
        test='virtctl version',
        overwrite=params['overwrite'],
        verify=False,
        my_output=my_output
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- virtctl installed')
    return True