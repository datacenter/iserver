from lib import filter_helper
from lib import ip_helper
from lib import output_helper
from lib.linux import main as linux
from lib.linux import settings as linux_settings
from lib.linux import output as linux_output
from lib.k8s import settings as k8s_settings
from lib.k8s import output as k8s_output
from lib.k8s import main as k8s
from lib.vc import vcenter
from lib.workflow.ocp_cilium_inb import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'vcenter' not in params:
        params['vcenter'] = None

    if 'mesh-name' not in params:
        params['mesh-name'] = None

    if params['mesh-name'] is not None:
        if not isinstance(params['mesh-name'], str):
            return None, 'mesh-name param must be str'
        
        if len(params['mesh-name']) == 0:
            return None, 'mesh-name required'

    if 'view' not in params or params['view'] is None:
        params['view'] = ['ssh', 'vc', 'kube', 'pnet', 'mesh']

    if not isinstance(params['view'], list):
        return None, 'view param must be list'
    
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
        'vcenter',
        'mesh-name',
        'view',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_mesh_peers(params, my_output):
    configured = params['k8s_handler'].get_cilium_mesh_configured_clusters()
    if configured is None:
        my_output.error('Failed to get configured cluster mesh')
        return None
    
    if len(configured) == 0:
        my_output.default('No cluster mesh configured')
        return None
    
    peers = []
    for item in configured:
        if params['mesh-name'] is None:
            peers.append(item['name'])
            continue

        if item['name'] == params['mesh-name']:
            peers.append(item['name'])

    if len(peers) == 0:
        my_output.default('Cluster mesh %s not found' % (params['mesh-name']))
        return None
    
    return peers

    
def is_inb(peer_name, params, my_output, log_id):
    my_output.default('Checking cluster mesh: %s' % (peer_name))

    info = {}
    info['name'] = peer_name

    linux_handler = linux_settings.LinuxSettings(log_id)
    connector_name = '%s-%s' % (
        params['cluster'],
        peer_name
    )

    connector = linux_handler.get_linux_server(connector_name)
    if connector is None:
        my_output.default('- linux connector expected: %s' % (connector_name))
        return None
    
    info['linux_handler'] = linux.Linux(
        connector['address'],
        connector['username'],
        password=connector['password'],
        log_id=log_id
    )
    if not info['linux_handler'].ssh_handler.is_ssh():
        my_output.default('- ssh access fails: %s' % (connector_name))
        return  None

    my_output.default('- linux connector: %s' % (connector_name))

    k8s_handler = k8s_settings.K8sSettings(log_id)
    connector_name = '%s-%s' % (
        params['cluster'],
        peer_name
    )

    connector = k8s_handler.get_k8s_cluster(connector_name)
    if connector is None:
        my_output.default('- kubernetes connector expected: %s' % (connector_name))
        return None
    
    info['k8s_handler'] = k8s.K8s(
        kubeconfig_filename=connector['kubeconfig'], 
        cluster_type=connector['type'], 
        log_id=log_id
    )
    if not info['k8s_handler'].check_api():
        my_output.default('- kubernetes access fails: %s' % (connector_name))
        return  None

    my_output.default('- kubernetes connector: %s' % (connector_name))
    my_output.default('- cluster mesh peer detected as inb')
    return info


def get_linux(peer, params, my_output, log_id):
    if 'ssh' in params['view']:
        crictl = peer['linux_handler'].get_crictl_processes(cache_enabled=False)
        if crictl is None:
            my_output.default('- failed to get crictl processes')
            return
        
        if len(crictl) == 0:
            my_output.default('- no crictl processes running')
            return
        
        linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
        my_output.default('## Container', before_newline=True)
        linux_output_handler.print_linux_crictl_ps(crictl)

    if 'ssh' in params['view'] or 'vc' in params['view']:
        interfaces = peer['linux_handler'].get_interfaces(phys_only=True)
        my_output.default('## Interface', before_newline=True)
        linux_output_handler.print_interfaces(interfaces)

    if params['vcenter'] is None or 'vc' not in params['view']:
        return 
    
    my_output.default('## vCenter', before_newline=True)

    vc_handler = vcenter.Vcenter(
        params['vcenter']['ip'],
        params['vcenter']['username'],
        params['vcenter']['password'],
        port=params['vcenter']['port'],
        log_id=log_id
    )
    if not vc_handler.is_vc_connected():
        my_output.error('Failed to connect to vcenter')
        return

    vms = vc_handler.get_vms()
    if vms is None:
        my_output.error('Failed to get vm data')
        return

    inb_vm = None
    for vm in vms:
        vm_nics = filter_helper.get(vm, 'nic', on_error=[], on_none=[])
        for vm_nic in vm_nics:
            for inb_interface in interfaces:
                if ip_helper.is_mac_equal(inb_interface['mac'], vm_nic['macAddress']):
                    inb_vm = vm
                    break

            if inb_vm is not None:
                break

    if inb_vm is None:
        my_output.default('- failed to find vm by mac address')
        return 
    
    my_output.default('### inb', before_newline=True)

    vc_handler.print_vms([inb_vm])
    for nic in inb_vm['nic']:
        nic['interface'] = None
        for inb_interface in interfaces:
            if ip_helper.is_mac_equal(inb_interface['mac'], nic['macAddress']):
                nic['interface'] = inb_interface['name']

    order = [
        'label',
        'type',
        'networkName',
        'macAddress',
        'interface'
    ]

    headers = [
        'Label',
        'Type',
        'Network',
        'MAC',
        'Interface'
    ]

    my_output.my_table(
        inb_vm['nic'],
        order=order,
        headers=headers,
        underline=True,
        allow_order_subkeys=True,
        row_separator=True,
        table=True
    )    

    interface_id = 0
    for inb_nic in inb_vm['nic']:
        if interface_id > 0:
            my_output.default('### private network [%s] via [%s]' % (inb_nic['networkName'], inb_nic['interface']), before_newline=True)

            interface_vms = []
            for vm in vms:
                vm_nics = filter_helper.get(vm, 'nic', on_error=[], on_none=[])
                for vm_nic in vm_nics:
                    if vm_nic['networkName'] == inb_nic['networkName']:
                        interface_vms.append(vm)
                        break

            vc_handler.print_vms(interface_vms)

        interface_id += 1


def get_kubernetes(peer, params, my_output, log_id):
    if 'kube' not in params['view'] and 'mesh' not in params['view'] and 'pnet' not in params['view']:
        return 
    
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    if 'kube' in params['view']:
        nodes = peer['k8s_handler'].get_nodes()
        if nodes is None:
            my_output.error('k8s nodes api failed')
        else:
            my_output.default('## Node', before_newline=True)
            k8s_output_handler.print_nodes_state(nodes)

        pods = peer['k8s_handler'].get_pods()
        if pods is None:
            my_output.error('k8s pods api failed')
        else:
            my_output.default('## POD', before_newline=True)
            k8s_output_handler.print_pods_state(pods)

    if 'mesh' in params['view']:
        agents = peer['k8s_handler'].get_cilium_agent_status()
        if agents is None or len(agents) == 0:
            my_output.error('agent status info failed')
        else:
            for agent in agents:
                my_output.default('## Cilium Agent', before_newline=True, after_newline=True)
                my_output.default('- agent: %s' % (agent['agent']))
                my_output.default('- state: %s' % (agent['cilium']['state']))
                my_output.default('- image: %s' % (agent['cilium']['msg']))

        status = params['k8s_handler'].get_cilium_mesh_status()
        my_output.default('## Cilium Mesh', before_newline=True)
        k8s_output_handler.print_cilium_mesh_status(status)

    if 'pnet' in params['view']:
        dbs = params['k8s_handler'].get_cilium_private_network_dbs(cache_enabled=False)

        pnets = None
        peps = None

        if dbs['privnet-endpoints'] is None:
            my_output.error('Failed to get private network endpoints')
        else:
            peps = params['k8s_handler'].get_clusterwide_private_network_endpoints_db_info(dbs['privnet-endpoints'])
            if peps is None:
                my_output.error('Failed to parse private networks endpoints cilium db content')

        if dbs['private-networks'] is None:
            my_output.error('Failed to get private networks')
        else:
            pnets = params['k8s_handler'].get_clusterwide_private_networks_db_info(
                dbs['private-networks'],
                peps
            )
            if pnets is None:
                my_output.error('Failed to parse private networks cilium db content')

        if pnets is not None:
            my_output.default('## Private Network', before_newline=True)
            k8s_output_handler.print_clusterwide_private_networks(pnets)

        if peps is not None:
            my_output.default('## Private Network Endpoints', before_newline=True)
            k8s_output_handler.print_clusterwide_private_network_endpoints_db(peps)


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get Isovalent Network Bridge', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    success = True

    if params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network %s' % (my_output.add_color('enabled', 'Green')))
    else:
        my_output.default('Private network %s' % (my_output.add_color('disabled', 'Red')))
        success = False    

    if params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.default('Cluster mesh %s' % (my_output.add_color('enabled', 'Green')))
    else:
        my_output.default('Cluster mesh %s' % (my_output.add_color('disabled', 'Red')))
        success = False    
    
    if not success:
        return False
    
    peers = get_mesh_peers(params, my_output)
    if peers is None:
        return True

    inbs = []
    for peer in peers:
        peer_info = is_inb(peer, params, my_output, log_id)
        if peer_info is not None:
            inbs.append(peer_info)

    for inb in inbs:
        my_output.default('inb: %s' % (inb['name']), before_newline=True, underline=True)
        get_linux(inb, params, my_output, log_id)
        get_kubernetes(inb, params, my_output, log_id)

    return True
