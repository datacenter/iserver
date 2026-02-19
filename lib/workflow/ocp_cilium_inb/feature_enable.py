import json
import yaml
import base64
from lib import ip_helper
from lib import file_helper
from lib import filter_helper
from lib import output_helper
from lib import ssh
from lib.linux import settings as linux_settings
from lib.k8s import settings as k8s_settings
from lib.k8s import main as k8s
from lib.workflow.ocp_cilium_inb import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow.ocp_cilium_mesh import cluster_create
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'ip' not in params or params['ip'] is None:
        return None, 'inb ip required'

    if not isinstance(params['ip'], str):
        return None, 'ip param must be ipv4 address'

    if not ip_helper.is_valid_ipv4_address(params['ip']):
        return None, 'inb ipv4 address expected'

    if 'username' not in params or params['username'] is None:
        return None, 'username required'

    if not isinstance(params['username'], str):
        return None, 'username param must be int'

    if len(params['username']) == 0:
        return None, 'username required'

    if 'password' not in params or params['password'] is None:
        return None, 'password required'

    if not isinstance(params['password'], str):
        return None, 'password param must be int'

    if len(params['password']) == 0:
        return None, 'password required'

    if 'mesh-id' not in params:
        return None, 'mesh-id required'

    if not isinstance(params['mesh-id'], int):
        return None, 'mesh-id param must be int'

    if  params['mesh-id'] < 1 or params['mesh-id'] > 255:
        return None, 'mesh-id param must be int in [1, 255] range'
    
    if 'mesh-name' not in params or params['mesh-name'] is None:
        return None, 'mesh-name required'

    if not isinstance(params['mesh-name'], str):
        return None, 'mesh-name param must be str'
    
    if len(params['mesh-name']) == 0:
        return None, 'mesh-name required'

    if 'mesh-port' not in params:
        return None, 'mesh-port required'

    if params['mesh-port'] is not None and not isinstance(params['mesh-port'], int):
        return None, 'mesh-port param must be int'

    if  params['mesh-port'] < 1 or params['mesh-port'] > 65535:
        return None, 'mesh-port param must be int in [1, 65535] range'
    
    if 'cidr' not in params or params['cidr'] is None:
        return None, 'cidr required'

    if not ip_helper.is_valid_ipv4_cidr(params['cidr']):
        return None, 'cidr param must be valid ipv4 cidr'

    if 'pnet' not in params or params['pnet'] is None:
        return None, 'pnet required'

    if not isinstance(params['pnet'], str):
        return None, 'pnet param must be int'

    if len(params['pnet']) == 0:
        return None, 'pnet required'

    if 'nic' not in params or params['nic'] is None:
        return None, 'nic required'

    if not isinstance(params['nic'], str):
        return None, 'nic param must be int'

    if len(params['nic']) == 0:
        return None, 'pnet required'

    if 'gateway' not in params or params['gateway'] is None:
        return None, 'gateway required'

    if not ip_helper.is_valid_ipv4_cidr(params['gateway']):
        return None, 'gateway param must be valid ipv4 cidr'
        
    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'ip',
        'username',
        'password',
        'mesh-id',
        'mesh-name',
        'mesh-port',
        'cidr',
        'pnet',
        'nic',
        'gateway',
        'verbose',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def validate_vm(params, my_output, log_id):
    params['ssh_handler'] = ssh.Ssh(
        params['ip'],
        params['username'],
        password=params['password'],
        log_id=log_id
    )
    if not params['ssh_handler'].is_ssh():
        my_output.error('SSH access to inb fails')
        return None

    my_output.default('SSH access to inb successful')

    success, output, error = params['ssh_handler'].run_cmd('ip -j address')
    if not success:
        my_output.error('ip address information failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return None
    
    my_output.default('Inb interface IP addresses collected')
    
    try:
        interfaces = json.loads(output)
    except BaseException:
        my_output.error('ip address information parse failed')
        my_output.default(str(interfaces), wrap='~~~')
        return None
    
    found = False
    for interface in interfaces:
        if interface['ifname'] == params['nic']:
            found = True
            my_output.default('nic %s found' % (params['nic']))
            for address in interface['addr_info']:
                if address['family'] == 'inet6' and address['local'].startswith('fe80::'):
                    continue

                my_output.error('unexpected ip address configured on vm interface')
                my_output.default(address, wrap='~~~')
                return None
            
            my_output.default('no ip address configured')

    if not found:
        my_output.error('interface %s not found' % (params['nic']))

    return params


def validate_cidr(params, my_output):
    cluster_network = params['k8s_handler'].get_cluster_network()
    if cluster_network is None:
        my_output.error('Failed to get cluster network information')
        return None
    
    if ip_helper.is_subnet_overlap(cluster_network['cluster_network'], params['cidr']):
        my_output.error('inb pod cidr overlaps with cluster pod cidr')
        return None
    
    my_output.default('inb pod cidr does not overlap with cluster pod cidr')
    return params


def validate_mesh(params, my_output):
    mesh_config = params['k8s_handler'].get_cilium_mesh_configured_clusters(cache_enabled=False)
    if mesh_config is None:
        my_output.error('Failed to get mesh config')
        return None
    
    params['cluster-reinit'] = False
    for item in mesh_config:
        if item['name'] == params['mesh-name']:
            params['cluster-reinit'] = True
            if params['ip'] not in item['ips']:
                my_output.error('Cluster mesh name already configured with different ip address')
                return None
        
            if params['mesh-port'] != item['port']:
                my_output.error('Cluster mesh name already configured with different port')
                return None
        
            my_output.default('Cluster reinit detected')
            break

        if params['ip'] in item['ips']:
            my_output.error('inb ip already configured in cluster mesh')
            return None

    if not params['cluster-reinit']:
        my_output.default('mesh-name not used in cluster mesh configuration')
        my_output.default('inb ip not used in cluster mesh configuration')

        if not params['k8s_handler'].is_cilium_mesh_id_available(params['mesh-id']):
            my_output.error('mesh-id already used')
            return None
        
        my_output.default('mesh-id not used')

    return params


def validate_runtime(params, my_output, log_id):
    my_output.default('Validate input parameters', before_newline=True, underline=True)
    params = validate_vm(params, my_output, log_id)
    if params is None:
        return None
    
    if params['k8s_handler'].is_clusterwide_private_network(params['pnet']):
        my_output.default('Private network already defined: %s' % (params['pnet']))
        params['is_private_network'] = True
    else:    
        my_output.default('Private network not defined: %s' % (params['pnet']))
        params['is_private_network'] = False

    params = validate_cidr(params, my_output)
    if params is None:
        return None

    params = validate_mesh(params, my_output)
    if params is None:
        return None

    return params


def generate_configuration(params, cilium_config, my_output):
    my_output.default('Generate inb config', before_newline=True, underline=True)
    body = {}
    body['cluster'] = {}
    body['cluster']['id'] = params['mesh-id']
    body['cluster']['name'] = params['mesh-name']
    
    node_ip = params['k8s_handler'].get_any_worker_node_ip()
    if node_ip is None:
        my_output.error('Failed to get worker node ip')
        return False

    my_output.default('remote cluster ip as any worker node ip')

    ocp_name = filter_helper.get(cilium_config, 'spec:cluster:name')
    if ocp_name is None:
        my_output.error('Cilium config spec:cluster:name required')
        return False
    
    my_output.default('remote cluster name from spec:cluster:name')

    node_port = filter_helper.get(cilium_config, 'spec:clustermesh:apiserver:nodePort')
    if node_port is None:
        my_output.error('Cilium config spec:clustermesh:apiserver:nodePort required')
        return False

    my_output.default('remote cluster port from spec:clustermesh:apiserver:nodePort')

    cluster = {}
    cluster['ips'] = [node_ip]
    cluster['name'] = ocp_name
    cluster['port'] = node_port
    body['remoteClusters'] = [cluster]

    tunnel_port = filter_helper.get(cilium_config, 'spec:tunnelPort')
    if node_port is None:
        my_output.error('Cilium config spec:tunnelPort required')
        return False
    
    my_output.default('tunnel port from spec:tunnelPort')

    health_port = filter_helper.get(cilium_config, 'spec:clusterHealthPort')
    if node_port is None:
        my_output.error('Cilium config spec:clusterHealthPort required')
        return False

    my_output.default('health port from spec:clusterHealthPort')

    body['tunnelPort'] = tunnel_port
    body['clusterHealthPort'] = health_port
    body['host'] = {}
    body['host']['ip'] = params['ip']
    body['ipam'] = {}
    body['ipam']['podCIDR'] = 'QUOTE%sQUOTE' % (params['cidr'])

    body['privateNetworks'] = []

    pnet = {}
    pnet['name'] = params['pnet']
    pnet['interface'] = {}
    pnet['interface']['name'] = params['nic']
    pnet['subnets'] = []
    pnet['subnets'].append(ip_helper.get_network_cidr_from_cidr(params['gateway']))
    route = {}
    route['destination'] = '0.0.0.0/0'
    route['gateway'] = params['gateway'].split('/')[0]
    pnet['routes'] = [route]

    body['privateNetworks'].append(pnet)

    if params['k8s_handler'].is_cilium_timescape_mesh_enabled(cache_enabled=False):
        body['hubble'] = {}
        body['hubble']['timescape'] = {}
        body['hubble']['timescape']['namespace'] = params['namespace']
        
    my_output.default(yaml.dump(body).replace('QUOTE', '"'), wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = params['ssh_handler'].scp_content(yaml.dump(body).replace('QUOTE', '"'), './config.yaml', path_fixup=False)
    if not success:
        my_output.error('config.yaml upload failed')
        return False
    
    my_output.default('config.yaml uploaded to inb')
    return True


def upload_ca_certificate(params, my_output):
    my_output.default('Upload CA certificate', before_newline=True, underline=True)
    my_output.default('Get cilium ca secret: %s/%s' % (params['namespace'], params['secret']))
    secret_mo = params['k8s_handler'].get_secret(params['namespace'], params['secret'], return_mo=True, cache_enabled=False)
    if secret_mo is None:
        my_output.error('Not found')
        return False
    
    crt = filter_helper.get(secret_mo, 'data:tls.crt')
    if crt is None:
        my_output.error('data:ca.crt not found')
        return False
    
    key = filter_helper.get(secret_mo, 'data:tls.key')
    if key is None:
        my_output.error('data:tls.key not found')
        return False
    
    body = base64.b64decode(crt.encode('utf-8')).decode('utf-8')
    my_output.default(body, wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = params['ssh_handler'].scp_content(body, './ca.crt', path_fixup=False)
    if not success:
        my_output.error('ca.crt upload failed')
        return False
    
    my_output.default('ca.crt uploaded to inb')

    body = base64.b64decode(key.encode('utf-8')).decode('utf-8')
    my_output.default(body, wrap='~~~')
    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = params['ssh_handler'].scp_content(body, './ca.key', path_fixup=False)
    if not success:
        my_output.error('ca.key upload failed')
        return False
    
    my_output.default('ca.key uploaded to inb')
    return True


def init_inb(params, my_output):
    my_output.default('Initialize inb', before_newline=True, underline=True)
    my_output.default('Sit tight...')
    
    success, output, error = params['ssh_handler'].run_cmd(
        '/opt/isovalent/inbadm init',
        paranoid=True,
        timeout=300
    )
    my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
    if not success:
        my_output.error('inb init failed')
        return False
    
    return True


def initialize_inb(params, my_output):
    cilium_config = params['k8s_handler'].get_cilium_config()
    if cilium_config is None:
        my_output.error('Failed to get cilium configuration')
        return False

    if not generate_configuration(params, cilium_config, my_output):
        return False

    if not upload_ca_certificate(params, my_output):
        return False

    if not init_inb(params, my_output):
        return False

    return True


def create_inb_linux_server(params, my_output, log_id):
    my_output.default('Create inb linux handler')
    params['inb_linux_name'] = '%s-%s' % (
        params['cluster'],
        params['mesh-name']
    )
    linux_settings_handler = linux_settings.LinuxSettings(log_id=log_id)
    success = linux_settings_handler.set_linux_server(
        params['inb_linux_name'], 
        params['ip'], 
        params['username'], 
        password=params['password']
    )
    if not success:
        my_output.error('Failed')
        return None

    my_output.default('Linux connector %s' % (params['inb_linux_name']))
    return params


def create_inb_k8s_connector(params, my_output, log_id):
    success, output, error = params['ssh_handler'].run_cmd('sudo cat /etc/kubernetes/super-admin.conf')
    if not success:
        my_output.error('inb kubeconfig not found: /etc/kubernetes/super-admin.conf')
        return None

    filename = file_helper.set_tmp_file(output)
    params['inb_k8s_name'] = '%s-%s' % (
        params['cluster'],
        params['mesh-name']
    )
    
    k8s_settings_handler = k8s_settings.K8sSettings(log_id=log_id)
    success = k8s_settings_handler.set_k8s_cluster(
        params['inb_k8s_name'], 
        filename, 
        cluster_type='standard', 
        cluster_source='user'
    )

    params['inb_k8s_handler'] = k8s.K8s(
        kubeconfig_filename=filename, 
        cluster_type='standard', 
        log_id=log_id
    )
    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Initialize Isovalent Network Bridge', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if not params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.error('Cluster mesh disabled')
        return False
    
    my_output.default('Cluster mesh enabled')
    
    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.error('Private network disabled')
        return True

    my_output.default('Private network enabled')

    params = validate_runtime(params, my_output, log_id)
    if params is None:
        return False

    params = create_inb_linux_server(params, my_output, log_id)
    if params is None:
        return False

    success = initialize_inb(params, my_output)
    if not success:
        return False
    
    params = create_inb_k8s_connector(params, my_output, log_id)
    if params is None:
        return False

    nodes = params['inb_k8s_handler'].get_nodes()
    if nodes is None:
        my_output.error('inb kubernetes api failed')
        return False
    
    my_output.default('inb kubernetes api successful')

    if not params['is_private_network']:
        success = params['k8s_handler'].create_clusterwide_private_network(
            params['pnet'], 
            cidrv4=ip_helper.get_network_cidr_from_cidr(params['gateway']), 
            cidrv6=None, 
            inb=[params['mesh-name']], 
            gatewayv4=params['gateway'].split('/')[0],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    if not params['cluster-reinit']:
        child_params = {}
        child_params['cluster'] = params['cluster']
        child_params['mesh-id'] = params['mesh-id']
        child_params['mesh-name'] = params['mesh-name']
        child_params['mesh-ip'] = params['ip']
        child_params['mesh-port'] = params['mesh-port']
        child_params['wait'] = True
        child_params['confirmation'] = params['confirmation']
        success = cluster_create.run(child_params, log_id=log_id)
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Isovalent network bridge initiated')
    my_output.default('- Cluster mesh established')
    my_output.default('- Isovalent network bridge k8s and linux connectors created')

    return True
