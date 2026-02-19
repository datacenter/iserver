from lib import output_helper
from lib.linux import settings as linux_settings
from lib.k8s import settings as k8s_settings
from lib.workflow.ocp_cilium_inb import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow.ocp_cilium_mesh import cluster_delete


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'mesh-name' not in params:
        params['mesh-name'] = None

    if params['mesh-name'] is not None:
        if not isinstance(params['mesh-name'], str):
            return None, 'mesh-name param must be str'
        
        if len(params['mesh-name']) == 0:
            return None, 'mesh-name required'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'mesh-name',
        'verbose',
        'confirmation',
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
    
    my_output.default('- linux connector: %s' % (connector_name))
    info['linux_connector'] = connector_name

    k8s_handler = k8s_settings.K8sSettings(log_id)
    connector_name = '%s-%s' % (
        params['cluster'],
        peer_name
    )

    connector = k8s_handler.get_k8s_cluster(connector_name)
    if connector is None:
        my_output.default('- kubernetes connector expected: %s' % (connector_name))
        return None
    
    my_output.default('- kubernetes connector: %s' % (connector_name))
    info['linux_connector'] = connector_name

    my_output.default('- cluster mesh peer detected as inb')
    return info


def delete_linux_connector(connector, my_output, log_id):
    linux_handler = linux_settings.LinuxSettings(log_id)
    if linux_handler.get_linux_server(connector) is None:
        my_output.default('Linux connector already deleted: %s' % (connector))
        return True
    
    success = linux_handler.delete_linux_server(connector)
    if not success:
        my_output.error('Failed to delete linux connector: %s' % (connector))
        return False
    
    my_output.default('Linux connector deleted: %s' % (connector))        
    return True


def delete_k8s_connector(connector, my_output, log_id):
    k8s_handler = k8s_settings.K8sSettings(log_id)
    if k8s_handler.get_k8s_cluster(connector) is None:
        my_output.default('Kubernetes connector already deleted: %s' % (connector))
        return True
    
    success = k8s_handler.delete_k8s_cluster(connector)
    if not success:
        my_output.error('Failed to delete kubernetes connector: %s' % (connector))
        return False
    
    my_output.default('Kubernetes connector deleted: %s' % (connector))        
    return True


def delete_cluster_mesh(params, name, log_id):
    child_params = {}
    child_params['cluster'] = params['cluster']
    child_params['mesh-name'] = name
    child_params['verbose'] = params['verbose']
    child_params['confirmation'] = params['confirmation']
    
    success = cluster_delete.run(
        child_params,
        log_id=log_id
    )
    return success


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Unconfigure Isovalent Network Bridge', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.default('Cluster mesh disabled')

        if params['mesh-name'] is not None:
            linux_connector = '%s-%s' % (params['cluster'], params['mesh-name'])
            k8s_connector = '%s-%s' % (params['cluster'], params['mesh-name'])
            if not delete_linux_connector(linux_connector, my_output, log_id):
                return False
            
            if not delete_k8s_connector(k8s_connector, my_output, log_id):
                return False

        return True
    
    my_output.default('Cluster mesh enabled')
    
    # if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
    #     my_output.default('Private network disabled')
    #     return True

    # my_output.default('Private network enabled')

    peers = get_mesh_peers(params, my_output)
    if peers is None:
        return True

    inbs = []

    if params['mesh-name'] is None:
        for peer in peers:
            peer_info = is_inb(peer, params, my_output, log_id)
            if peer_info is not None:
                inbs.append(peer_info)
    else:
        info = {}
        info['name'] = peers[0]
        info['linux_connector'] = '%s-%s' % (params['cluster'], info['name'])
        info['k8s_connector'] = '%s-%s' % (params['cluster'], info['name'])
        inbs.append(info)

    for inb in inbs:
        my_output.default('inb: %s' % (inb['name']), before_newline=True, underline=True)

        if not delete_linux_connector(info['linux_connector'], my_output, log_id):
            return False
        
        if not delete_k8s_connector(info['k8s_connector'], my_output, log_id):
            return False

        if not delete_cluster_mesh(params, inb['name'], log_id):
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster mesh deleted')
    my_output.default('- Isovalent network bridge k8s and linux connectors deleted')

    return True
