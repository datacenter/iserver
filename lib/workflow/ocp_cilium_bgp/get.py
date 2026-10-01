import copy
import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_bgp import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res', 'cli'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


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


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ssh_required = False
        if 'cli' in params['view']:
            ssh_required = True

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=ssh_required)
        if params is None:
            continue

        if 'state' in params['view']:
            get_state(params, my_output, k8s_output_handler)
        
        if 'res' in params['view']:
            get_crds(params, my_output)

        if 'cli' in params['view']:
            get_cli(params, my_output)

    return True