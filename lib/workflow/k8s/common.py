import json
import copy
from lib import ip_helper
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    if '__id__' in params and params['__id__'] is not None:
        my_output.default('ID: %s' % (params['__id__']), after_newline=True)

    return params

def get_default_params():
    params = {}
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def get_pvcs(k8s_handler, namespace=None, name=None, unused=False):
    object_filter = []
    if namespace is not None:
        object_filter.append(
            'namespace:%s' % (namespace)
        )

    if name is not None:
        object_filter.append(
            'name:%s' % (name)
        )

    if unused:
        object_filter.append(
            'used:false'
        )

    pvcs = k8s_handler.get_pvcs(
        object_filter=object_filter,
        usage_info=True,
        cache_enabled=False
    )

    return pvcs


def get_dvs(k8s_handler, namespace=None, name=None, unused=False):
    object_filter = []
    if namespace is not None:
        object_filter.append(
            'namespace:%s' % (namespace)
        )

    if name is not None:
        object_filter.append(
            'name:%s' % (name)
        )

    if unused:
        object_filter.append(
            'used:false'
        )

    dvs = k8s_handler.get_data_volumes(
        object_filter=object_filter,
        cache_enabled=False
    )

    return dvs


def get_nads(k8s_handler, namespace=None, name=None, unused=False):
    object_filter = []
    if namespace is not None:
        object_filter.append(
            'namespace:%s' % (namespace)
        )

    if name is not None:
        object_filter.append(
            'name:%s' % (name)
        )

    nads = k8s_handler.get_nads(
        object_filter=object_filter,
        cache_enabled=False
    )

    return nads


def validate_vlan(value):
    if not isinstance(value, int):
        return False, 'vlan param must be int <1, 4096>'

    if value < 1 or value > 4096:
        return False, 'vlan param must be int <1, 4096>'
    
    return True, None


def validate_nad_ipam(params, modes=['dhcp', 'static', 'local']):
    if 'ipam' not in params:
        return None, 'ipam required: dhcp, static, local'
    
    if params['ipam'] not in modes:
        return None, 'ipam required: %s' % (', '.join(modes))
    
    if params['ipam'] == 'dhcp':
        params['address'] = None
        params['gateway'] = None

    if params['ipam'] == 'static':
        if 'address' not in params or params['address'] is None:
            return None, 'address required for ipam:static'
        
        if not ip_helper.is_valid_ipv4_address(params['address']):
            return None, 'address required for ipam:static'
        
        if 'gateway' not in params or params['gateway'] is None:
            return None, 'gateway required for ipam:static'
        
        if not ip_helper.is_valid_ipv4_cidr(params['gateway']):
            return None, 'gateway cidr required for ipam:static'

        if not ip_helper.is_ipv4_in_cidr(params['address'], params['gateway']):
            return None, 'address and gateway cidr mismatch'
        
    if params['ipam'] == 'local':
        if 'address' not in params or params['address'] is None:
            return None, 'address required for ipam:static'
        
        if len(params['address'].split('-')) != 2:
            return None, 'address_start-address_end required for ipam:local'

        address_start, address_end = params['address'].split('-')

        if not ip_helper.is_valid_ipv4_address(address_start):
            return None, 'address_start required for ipam:local'
        
        if not ip_helper.is_valid_ipv4_address(address_end):
            return None, 'address_end required for ipam:local'

        if ip_helper.get_ipv4_address_count(address_start, address_end) is None:
            return None, 'invalid address range for ipam:local'
        
        if 'gateway' not in params or params['gateway'] is None:
            return None, 'gateway required for ipam:local'
        
        if not ip_helper.is_valid_ipv4_cidr(params['gateway']):
            return None, 'gateway cidr required for ipam:local'

        if not ip_helper.is_ipv4_in_cidr(address_start, params['gateway']):
            return None, 'address and gateway cidr mismatch'

        if not ip_helper.is_ipv4_in_cidr(address_end, params['gateway']):
            return None, 'address and gateway cidr mismatch'
    
    if 'route' in params:
        if not isinstance(params['route'], list):
            return None, 'route list required'
        
        for route in params['route']:
            if not ip_helper.is_valid_ipv4_cidr(route):
                return None, 'route with subnets required'

    return params, None
