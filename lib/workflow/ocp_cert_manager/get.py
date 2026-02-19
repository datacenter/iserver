from lib import output_helper
from lib.workflow.ocp_cert_manager import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Certificate Manager - Get', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    local_common.is_repo(params, my_output)
    local_common.is_helm(params, my_output)
    crds = local_common.get_crds(params)
    if not crds['ready']:
        my_output.default('Crds not installed')
    else:
        my_output.default('Issuer CRD [#%s]' % (len(crds['issuer'])))
        my_output.default('Certificate CRD [#%s]' % (len(crds['certificate'])))        

    return True
