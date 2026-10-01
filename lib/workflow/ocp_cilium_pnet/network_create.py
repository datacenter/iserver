from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow import ocp_common


def validate(params):
    subnet_rules = [
        ['name', False, None, 'str', None, None, None, None],
        ['cidrv4', True, None, 'ipv4-subnet', None, None, None, None],
        ['cidrv6', True, None, 'ipv6-subnet', None, None, None, None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['name', False, None, 'k8s-name', None, None, None, None],
        ['cidrv4', True, [], 'list-of-cidrv4', None, None, None, None],
        ['cidrv6', True, [], 'list-of-cidrv6', None, None, None, None],
        ['subnet', True, [], 'list-of-dict', None, None, None, None],
        ['nad', True, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(
        params, 
        rules, 
        nested=dict(subnet=subnet_rules)
    )
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def validate_subnet(cidrv4, cidrv6, subnet, my_output):
    if len(cidrv4) > 0 and len(cidrv6) > 0 and len(cidrv4) != len(cidrv6):
        my_output.error('cidrv4 and cidrv6 count must be equal')
        return None
    
    cidr_len = max(len(cidrv4), len(cidrv6))
    if cidr_len > 0 and len(subnet) > 0:
        my_output.error('Defined cidr or subnet parameter')
        return None

    if cidr_len == 0 and len(subnet) == 0:
        my_output.error('Defined cidr or subnet parameter')
        return None

    if cidr_len > 0:
        subnets = []
        for index in range(0, cidr_len):
            subnet_mo = {}
            subnet_mo['name'] = 'subnet-%s' % (index)
            if index < len(cidrv4):
                value = '%s/%s' % (ip_helper.get_network_ipv4_in_cidr(cidrv4[index]), cidrv4[index].split('/')[1])
                subnet_mo['cidrv4'] = value
                if value != cidrv4[index]:
                    subnet_mo['routes'] = []
                    route_mo = {}
                    route_mo['destination'] = '0.0.0.0/0'
                    route_mo['gateway'] = cidrv4[index].split('/')[0]
                    subnet_mo['routes'].append(route_mo)

            if index < len(cidrv6):
                subnet_mo['cidrv6'] = cidrv6[index]

            subnets.append(subnet_mo)

        return subnets

    new_subnets = []
    subnet_names = []
    for item in subnet:
        if item['name'] in subnet_names:
            my_output.error('Subnet name must be unique')
            return None

        subnet_names.append(item['name'])

        if item['cidrv4'] is None and item['cidrv6'] is None:
            my_output.error('Define cidrv4 and/or cidrv6 for subnet')
            return None
        
        if item['cidrv4'] is None:
            del item['cidrv4']

        if item['cidrv6'] is None:
            del item['cidrv6']

        new_subnets.append(item)

    return new_subnets


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    subnet = validate_subnet(params['cidrv4'], params['cidrv6'], params['subnet'], my_output)
    if subnet is None:
        return False

    params = local_common.initialize(params, my_output, 'Create', log_id)
    if params is None:
        return False

    if len(params['nad']) > 0 and not params['state']['multus']['enabled']:
        my_output.error('Enable multus for private network first')
        return False
    
    success = params['k8s_handler'].create_clusterwide_private_network(
        params['name'], 
        subnet, 
        nad=params['nad'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    network_info = local_common.get_private_network(
        params,
        params['name'],
        my_output=my_output,
        k8s_output_handler=k8s_output_handler
    )
    if network_info is None:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network created')
    return True