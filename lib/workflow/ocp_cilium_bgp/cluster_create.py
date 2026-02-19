from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_cilium_bgp import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate_cluster(params):
    if 'policy' not in params or params['policy'] is None:
        params['policy'] = 'cluster'

    if 'label' not in params or params['label'] is None:
        params['label'] = []

    if isinstance(params['label'], str):
        params['label'] = [params['label']]

    if not isinstance(params['label'], list):
        return None, 'label param must list'

    params['mlabel'] = {}
    for item in params['label']:
        if len(item.split(':')) != 2:
            return None, 'unsupported label value: %s' % (item)
        
        params['mlabel'][item.split(':')[0]] = item.split(':')[1]

    if 'asn' not in params:
        return None, 'Local asn required'

    if not isinstance(params['asn'], int):
        return None, 'Local asn int required'

    if params['asn'] <= 0:
        return None, 'Local asn int gt0 required'

    return params, None


def validate_peer(params):
    if 'peer' not in params or params['peer'] is None:
        return None, 'peer property required'
    
    if not isinstance(params['peer'], dict):
        return None, 'peer dict required'
    
    if 'policy' not in params['peer'] or params['peer']['policy'] is None:
        params['peer']['policy'] = 'peer'

    if 'asn' not in params['peer']:
        return None, 'Peer asn required'

    if not isinstance(params['peer']['asn'], int):
        return None, 'Peer asn int required'

    if params['peer']['asn'] <= 0:
        return None, 'Peer asn int gt0 required'
    
    if 'ip' not in params['peer']:
        return None, 'Peer ips required'

    if not isinstance(params['peer']['ip'], list):
        return None, 'Peer ips required'

    if len(params['peer']['ip']) == 0:
        return None, 'Peer ips required'

    for item in params['peer']['ip']:    
        if not ip_helper.is_valid_ipv4_address(item) and not ip_helper.is_valid_ipv6_address(item):
            return None, 'peer ips required'

    params['peer']['peer'] = []
    index = 1
    for peer_ip in params['peer']['ip']:
        peer = {}
        peer['ip'] = peer_ip
        peer['asn'] = params['peer']['asn']
        peer['config'] = 'peer'
        peer['name'] = 'tor%s' % (index)
        params['peer']['peer'].append(peer)
        index += 1
    
    if 'af' not in params['peer']:
        params['peer']['af'] = ['v4']

    if not isinstance(params['peer']['af'], list):
        return None, 'Peer af list required'

    if len(params['peer']['af']) == 0:
        return None, 'Peer af required'

    for item in params['peer']['af']:
        if item not in ['v4', 'v6', 'vpn']:
            return None, 'Unsupported af: %s' % (item)
        
    if 'multihop' not in params['peer']:
        params['peer']['multihop'] = 1
    
    if not isinstance(params['peer']['multihop'], int):
        return None, 'Peer multihop int required'

    if params['peer']['multihop'] <= 0:
        return None, 'Peer multihop int gt0 required'

    if 'port' not in params['peer']:
        params['peer']['port'] = 179
    
    if not isinstance(params['peer']['port'], int):
        return None, 'Peer port int required'

    if params['peer']['port'] <= 0:
        return None, 'Peer port int gt0 required'

    if 'secret' not in params['peer']:
        params['peer']['secret'] = None

    if 'bfd' not in params['peer']:
        params['peer']['bfd'] = None

    if 'timer' not in params['peer']:
        params['peer']['timer'] = {}
    
    if not isinstance(params['peer']['timer'], dict):
        return None, 'Peer timer dict required'

    if 'keepalive' not in params['peer']['timer']:
        params['peer']['timer']['keepalive'] = 30

    if not isinstance(params['peer']['timer']['keepalive'], int):
        return None, 'Peer timer keepalive int required'

    if 'hold' not in params['peer']['timer']:
        params['peer']['timer']['hold'] = 90

    if not isinstance(params['peer']['timer']['hold'], int):
        return None, 'Peer timer hold int required'

    if 'retry' not in params['peer']['timer']:
        params['peer']['timer']['retry'] = 120

    if not isinstance(params['peer']['timer']['retry'], int):
        return None, 'Peer timer retry int required'

    if 'graceful' not in params['peer']:
        params['peer']['graceful'] = {}
    
    if not isinstance(params['peer']['graceful'], dict):
        return None, 'Peer graceful dict required'

    if 'enabled' not in params['peer']['graceful']:
        params['peer']['graceful']['enabled'] = False

    if not isinstance(params['peer']['graceful']['enabled'], bool):
        return None, 'Peer graceful enabled bool required'

    if 'restart' not in params['peer']['graceful']:
        params['peer']['graceful']['restart'] = 120

    if not isinstance(params['peer']['graceful']['restart'], int):
        return None, 'Peer graceful restart int required'

    return params, None


def validate_advertise_base(params, section):
    if section not in params['advertise']:
        params['advertise'][section] = {}
        params['advertise'][section]['enabled'] = False

    if not isinstance(params['advertise'][section], dict):
        return None, 'advertise.%s dict required' % (section)
    
    if 'enabled' not in params['advertise'][section]:
        params['advertise'][section]['enabled'] = True

    if not isinstance(params['advertise'][section]['enabled'], bool):
        return None, 'advertise.%s.enabled bool required' % (section)
    
    if 'community' not in params['advertise'][section]:
        params['advertise'][section]['community'] = []

    if not isinstance(params['advertise'][section]['community'], list):
        return None, 'advertise.%s.community list required' % (section)
    
    return params, None


def validate_advertise_selector(params, section):
    if 'selector' not in params['advertise'][section]:
        params['advertise'][section]['selector'] = []
        
    if not isinstance(params['advertise'][section]['selector'], list):
        return None, 'advertise.%s.selector list required' % (section)

    for item in params['advertise'][section]['selector']:
        if not isinstance(item, dict):
            return None, 'advertise.%s.selector list of dict required' % (section)
        
        for key in ['key', 'operator', 'values']:
            if key not in item:
                return None, 'advertise.%s.selector with key %s required' % (section, key)
            
        if not isinstance(item['values'], list):
            return None, 'advertise.%s.selector with values list required' % (section)

    if len(params['advertise'][section]['selector']) == 0:
        params['advertise'][section]['selector'].append(
            dict(
                key='dummy',
                operator='NotIn',
                values=['dummy']
            )
        )

    return params, None


def validate_advertise_aggregate(params, section):
    if 'aggregatev4' not in params['advertise'][section]:
        params['advertise'][section]['aggregatev4'] = None

    if params['advertise'][section]['aggregatev4'] is not None:
        if not isinstance(params['advertise'][section]['aggregatev4'], int):
            return None, 'aggregatev4 int required'
        
        if params['advertise'][section]['aggregatev4'] < 0 or params['advertise'][section]['aggregatev4'] > 32:
            return None, 'aggregatev4 int required (0, 32)'

    if 'aggregatev6' not in params['advertise'][section]:
        params['advertise'][section]['aggregatev6'] = None

    if params['advertise'][section]['aggregatev6'] is not None:
        if not isinstance(params['advertise'][section]['aggregatev6'], int):
            return None, 'aggregatev6 int required'
        
        if params['advertise'][section]['aggregatev6'] < 0 or params['advertise'][section]['aggregatev6'] > 128:
            return None, 'aggregatev6 int required (0, 128)'

    return params, None


def validate_advertise_pod(params):
    params, error = validate_advertise_base(params, 'pod')
    if params is None:
        return None, error
    
    return params, None


def validate_advertise_cluster(params):
    params, error = validate_advertise_base(params, 'cluster')
    if params is None:
        return None, error
    
    params, error = validate_advertise_selector(params, 'cluster')
    if params is None:
        return None, error

    params, error = validate_advertise_aggregate(params, 'cluster')
    if params is None:
        return None, error

    return params, None


def validate_advertise_ext(params):
    params, error = validate_advertise_base(params, 'ext')
    if params is None:
        return None, error
    
    params, error = validate_advertise_selector(params, 'ext')
    if params is None:
        return None, error

    params, error = validate_advertise_aggregate(params, 'ext')
    if params is None:
        return None, error

    return params, None


def validate_advertise_lb(params):
    params, error = validate_advertise_base(params, 'lb')
    if params is None:
        return None, error
    
    params, error = validate_advertise_selector(params, 'lb')
    if params is None:
        return None, error

    params, error = validate_advertise_aggregate(params, 'lb')
    if params is None:
        return None, error

    return params, None


def validate_advertise_egw(params):
    params, error = validate_advertise_base(params, 'egw')
    if params is None:
        return None, error
    
    params, error = validate_advertise_selector(params, 'egw')
    if params is None:
        return None, error

    params, error = validate_advertise_aggregate(params, 'egw')
    if params is None:
        return None, error

    return params, None


def validate_advertise(params):
    if 'advertise' not in params or params['advertise'] is None:
        return None, 'advertise property required'
    
    if not isinstance(params['advertise'], dict):
        return None, 'advertise dict required'
    
    if 'policy' not in params['advertise'] or params['advertise']['policy'] is None:
        params['advertise']['policy'] = 'advertise'

    params, error = validate_advertise_pod(params)
    if params is None:
        return None, error

    params, error = validate_advertise_cluster(params)
    if params is None:
        return None, error

    params, error = validate_advertise_ext(params)
    if params is None:
        return None, error

    params, error = validate_advertise_lb(params)
    if params is None:
        return None, error

    params, error = validate_advertise_egw(params)
    if params is None:
        return None, error
                
    return params, None


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    params, error = validate_cluster(params)
    if params is None:
        return None, error
    
    params, error = validate_peer(params)
    if params is None:
        return None, error

    params, error = validate_advertise(params)
    if params is None:
        return None, error

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'policy',
        'label',
        'mlabel',
        'asn',
        'peer',
        'advertise',
        'confirmation',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium BGP Control Plane - Cluster Configuration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if not params['k8s_handler'].is_cilium_bgp_enabled(cache_enabled=False):
        my_output.default('BGP control plane %s' % (my_output.add_color('disabled', 'Red')))
        return False

    my_output.default('BGP control plane %s' % (my_output.add_color('enabled', 'Green')))

    if params['k8s_handler'].get_isovalent_bgp_peer_configs(cache_enabled=False) is None:
        my_output.default('IsovalentBGPPeerConfig CRD %s' % (my_output.add_color('not found', 'Red')))
        return False
    
    my_output.default('IsovalentBGPPeerConfig CRD %s' % (my_output.add_color('found', 'Green')))

    success = params['k8s_handler'].create_isovalent_bgp_cluster_config(
        params['policy'],
        params['asn'],
        params['peer']['peer'],
        label=params['mlabel'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_isovalent_bgp_peer_config(
        params['peer']['policy'],
        dict(advertise='bgp'),
        params['peer']['af'],
        params['peer']['timer']['retry'],
        params['peer']['timer']['hold'],
        params['peer']['timer']['keepalive'],
        params['peer']['multihop'],
        params['peer']['graceful']['enabled'],
        params['peer']['graceful']['restart'],
        params['peer']['port'],
        params['peer']['secret'],
        params['peer']['bfd'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_isovalent_bgp_advertisement(
        params['advertise']['policy'],
        dict(advertise='bgp'),
        params['advertise']['pod'],
        params['advertise']['cluster'],
        params['advertise']['lb'],
        params['advertise']['ext'],
        params['advertise']['egw'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- BGP control plane configuration defined')

    return True
