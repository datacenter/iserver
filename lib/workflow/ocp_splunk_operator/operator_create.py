from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['version', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def fixup(body, my_output, sc=None):
    for crd in body:
        if filter_helper.get(crd, 'kind') == 'Deployment':
            for env in crd['spec']['template']['spec']['containers'][0]['env']:
                if env['name'] == 'SPLUNK_GENERAL_TERMS':
                    if env['value'] != '--accept-sgt-current-at-splunk-com':
                        env['value'] = '--accept-sgt-current-at-splunk-com'
                        my_output.default('Set env SPLUNK_GENERAL_TERMS value to --accept-sgt-current-at-splunk-com')

        if sc is not None and filter_helper.get(crd, 'kind') == 'PersistentVolumeClaim':
            crd['spec']['storageClassName'] = sc
            my_output.default('Set pvc storage class to: %s' % (sc))

    return body


def get_deployment_sa(body, my_output):
    for crd in body:
        if filter_helper.get(crd, 'kind') == 'Deployment':
            name = crd['spec']['template']['spec']['serviceAccountName']
            my_output.default('Deployment service account name: %s' % (name))
            return name

    return None
            

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    sc_default = params['k8s_handler'].get_default_storage_class_name()
    sc_name = None
    if sc_default is None:
        sc = params['k8s_handler'].get_default_storage_class(
            fallback_to_single=True
        )
        if sc is None:
            my_output.error('No storage class found')
            return False

        sc_name = sc['name']

    body = local_common.get_body(params, my_output)
    if body is None:
        return False

    body = fixup(body, my_output, sc=sc_name)
    sa_name = get_deployment_sa(body, my_output)
    if sa_name is None:
        return False

    success = params['k8s_handler'].apply_bodies(body, my_output=my_output, wait=True, only=['Namespace', 'ServiceAccount'])
    if not success:
        return False

    success = params['k8s_handler'].create_service_account_role_binding(
        params['__default__']['namespace'],
        params['__default__']['role-binding-name'],
        params['__default__']['role-binding-name'], 
        params['__default__']['namespace'],
        sa_name,
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False
        
    success = params['k8s_handler'].apply_bodies(body, my_output=my_output, wait=True, skip=['Namespace', 'ServiceAccount'])
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Splunk Operator installed')
    return True
