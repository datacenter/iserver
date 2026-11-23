from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, add_defaults=False, copy_handler=False), None


def run(params, log_id=None):
    return True
