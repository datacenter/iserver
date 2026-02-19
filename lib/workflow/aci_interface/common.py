from lib.workflow import aci_common


def initialize(params, my_output, log_id):
    params = augment_params(params)
    params['apic_handler'] = aci_common.get_apic_handler(params['apic'], my_output, log_id)
    if params['apic_handler'] is None:
        return None
    
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
