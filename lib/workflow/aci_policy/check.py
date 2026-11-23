import json
from progress.bar import Bar
from lib import ip_helper
from lib import output_helper
from lib.workflow.aci_interface import common as local_common


def validate_tenant(policy):
    if 'tenant' not in policy:
        policy['tenant'] = []

    if not isinstance(policy['tenant'], list):
        return None, 'tenant list required'
    
    for item in policy['tenant']:
        if not isinstance(item, dict):
            return None, 'tenant list of dict required'

        if 'name' not in item:
            return None, 'tenant.name required'
        
    return policy['tenant'], None

def validate(params):
    if 'apic' not in params:
        return None, 'APIC name required'

    params['tenant'], error = validate_tenant(params)
    if error is not None:
        return None, error
    
    return params, None


def check_tenants(handler, policy, my_output):
    success = True
    for tenant in policy['tenant']:
        if not handler.is_tenant(tenant['name']):
            my_output.error('Tenant [%s] not found' % (tenant['name']))
            success = False
        else:
            my_output.default('- Tenant [%s] found' % (tenant['name']))
    return success


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('ACI Workflow - Check policy configuration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    print(json.dumps(params, indent=4))

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    success = True

    if not check_tenants(params['apic_handler'], params, my_output):
        success = False

    return success
