from lib.workflow import ocp_common
from lib.workflow.k8s import nad_bridge_create
from lib.workflow.k8s import nad_ipvlan_create
from lib.workflow.k8s import nad_macvlan_create
from lib.workflow.k8s import nad_vlan_create


def validate(params):
    success, params['type'] = ocp_common.check_paramater(
        params,
        'type',
        expected_type='str',
        allowed_values=['bridge', 'ipvlan', 'macvlan', 'vlan']
    )
    if not success:
        return None, params['type']
    
    if params['type'] == 'bridge':
        return nad_bridge_create.validate(params)

    if params['type'] == 'ipvlan':
        return nad_ipvlan_create.validate(params)

    if params['type'] == 'macvlan':
        return nad_macvlan_create.validate(params)

    if params['type'] == 'vlan':
        return nad_vlan_create.validate(params)

    return None, 'Unexpected nad type: %s' % (params['type'])


def run(params, log_id=None):
    if params['type'] == 'bridge':
        return nad_bridge_create.run(params, log_id=log_id)

    if params['type'] == 'ipvlan':
        return nad_ipvlan_create.run(params, log_id=log_id)

    if params['type'] == 'macvlan':
        return nad_macvlan_create.run(params, log_id=log_id)

    if params['type'] == 'vlan':
        return nad_vlan_create.run(params, log_id=log_id)

    return False
