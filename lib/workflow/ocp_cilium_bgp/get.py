import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_bgp import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'cli' not in params:
        params['cli'] = False

    if not isinstance(params['cli'], bool):
        return None, 'cli param must be true or false'

    if 'crd' not in params:
        params['crd'] = False

    if not isinstance(params['crd'], bool):
        return None, 'crd param must be true or false'

    if 'state' not in params:
        params['state'] = False

    if not isinstance(params['state'], bool):
        return None, 'state param must be true or false'
    
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
        'cli',
        'crd',
        'state',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def cleanup(managed_object):
    for key in ['creationTimestamp', 'managedFields', 'generation', 'resourceVersion', 'uid']:
        if key in managed_object['metadata']:
            del managed_object['metadata'][key]

    if 'status' in managed_object:
        del managed_object['status']

    return managed_object


def get_crds(params, my_output):
    content = []
    crds = params['k8s_handler'].get_isovalent_bgp_cluster_configs(
        return_mo=True,
        cache_enabled=False
    )
    if crds is None:
        my_output.error('Failed to get IsovalentBGPClusterConfig CRD')
    else:
        for crd in crds:
            content.append(yaml.safe_dump(cleanup(crd)))

    crds = params['k8s_handler'].get_isovalent_bgp_peer_configs(
        return_mo=True,
        cache_enabled=False
    )
    if crds is None:
        my_output.error('Failed to get IsovalentBGPPeerConfig CRD')
    else:
        for crd in crds:
            content.append(yaml.safe_dump(cleanup(crd)))

    crds = params['k8s_handler'].get_isovalent_bgp_advertisements(
        return_mo=True,
        cache_enabled=False
    )
    if crds is None:
        my_output.error('Failed to get IsovalentBGPAdvertisement CRD')
    else:
        for crd in crds:
            content.append(yaml.safe_dump(cleanup(crd)))

    my_output.default(
        '---\n'.join(content),
        before_newline=True,
        wrap='~~~'
    )


def get_cli(params, my_output):
    if params['ssh_handler'] is None:
        my_output.error('No ssh access to cluster management node')
        return
    
    success, output, error = params['ssh_handler'].run_cmd('cilium bgp peers -n cilium')
    if not success:
        my_output.error('Failed to run cilium cli command')
        return 

    my_output.default('# cilium bgp peers -n cilium\n%s' % (str(output)), wrap='~~~', before_newline=True)

    success, output, error = params['ssh_handler'].run_cmd('cilium bgp routes advertised ipv4 unicast -n cilium')
    if success:
        my_output.default('# cilium bgp routes advertised ipv4 unicast -n cilium\n%s' % (str(output)), wrap='~~~', before_newline=True)

    success, output, error = params['ssh_handler'].run_cmd('cilium bgp routes advertised ipv4 mpls_vpn -n cilium')
    if success:
        my_output.default('# cilium bgp routes advertised ipv4 mpls_vpn -n cilium\n%s' % (str(output)), wrap='~~~', before_newline=True)

    success, output, error = params['ssh_handler'].run_cmd('cilium bgp routes advertised ipv6 unicast -n cilium')
    if success:
        my_output.default('# cilium bgp routes advertised ipv6 unicast -n cilium\n%s' % (str(output)), wrap='~~~', before_newline=True)


def get_state(params, my_output, k8s_output_handler):
    if not cilium_common.is_cilium(params, my_output):
        return

    if not params['k8s_handler'].is_cilium_bgp_enabled(cache_enabled=False):
        my_output.default('BGP control plane %s' % (my_output.add_color('disabled', 'Red')))
        return

    my_output.default('BGP control plane %s' % (my_output.add_color('enabled', 'Green')))

    info = params['k8s_handler'].get_isovalent_bgp_node_configs(cache_enabled=False)
    if info is None:
        my_output.error('Failed to get IsovalentBGPNodeConfig CRD')
        return
    
    k8s_output_handler.print_isovalent_bgp_node_configs(info)

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium BGP Control Plane - Get', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['state']:
        get_state(params, my_output, k8s_output_handler)
        
    if params['crd']:
        get_crds(params, my_output)

    if params['cli']:
        get_cli(params, my_output)

    return True
