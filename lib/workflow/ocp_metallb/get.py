from lib import filter_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.ocp_metallb import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['node', True, [], 'list-of-str', None, None, None, None],
        ['peer', True, [], 'list-of-ip', None, None, None, None],
        ['cmd', True, None, 'str', None, None, None, None],
        ['view', False, None, 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OVNKubernetes - Get metallb information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        brief=True
    )
    if subscription is None:
        return True

    instance = params['k8s_handler'].get_any_metallb(cache_enabled=False)
    bgp_mode = None
    if instance is None:
        my_output.default(my_output.add_color('No metallb instance', 'Red'))
    else:
        bgp_mode = filter_helper.get(instance, 'spec:bgpBackend', on_error='', on_none='')
        if bgp_mode in ['native']:
            my_output.default('Metallb instance in %s' % (my_output.add_color('l2 mode', 'Blue')))
        else:
            my_output.default('Metallb instance in %s' % (my_output.add_color('l3 mode', 'Blue')))

    ready = params['k8s_handler'].is_subscription_metallb_ready(
        with_instance=instance, 
        details=True
    )
    if not ready:
        ready = params['k8s_handler'].is_subscription_metallb_ready(
            with_instance=instance, 
            my_output=my_output, 
            details=True,
            cache_enabled=True
        )
        my_output.default('Metallb operator %s' % (my_output.add_color('not ready', 'Red')))
        return True

    if 'state' in params['view']:
        if bgp_mode == 'native':
            pass
    
        if bgp_mode == '':
            my_output.default('bgpBackend undefined (ovn-bgp integrated mode)')
            my_output.default('Metallb configuration')
            my_output.default('- IPAddressPool: %s' % (len(params['k8s_handler'].get_ip_address_pools(cache_enabled=False))))
            my_output.default('- BGPPeer: %s' % (len(params['k8s_handler'].get_bgp_peers(cache_enabled=False))))
            my_output.default('- BFDProfile: %s' % (len(params['k8s_handler'].get_bfd_profiles(cache_enabled=False))))
            my_output.default('- BGPAdvertisement: %s' % (len(params['k8s_handler'].get_bgp_advertisements(cache_enabled=False))))
            my_output.default('- Community: %s' % (len(params['k8s_handler'].get_communitys(cache_enabled=False))))
            my_output.default('- FRRConfiguration: %s' % (len(params['k8s_handler'].get_frr_configurations(cache_enabled=False))))

        if bgp_mode == 'frr':
            my_output.default('bgpBackend frr')
            my_output.default('Metallb configuration')
            my_output.default('- IPAddressPool: %s' % (len(params['k8s_handler'].get_ip_address_pools(cache_enabled=False))))
            my_output.default('- BGPPeer: %s' % (len(params['k8s_handler'].get_bgp_peers(cache_enabled=False))))
            my_output.default('- BFDProfile: %s' % (len(params['k8s_handler'].get_bfd_profiles(cache_enabled=False))))
            my_output.default('- BGPAdvertisement: %s' % (len(params['k8s_handler'].get_bgp_advertisements(cache_enabled=False))))
            my_output.default('- Community: %s' % (len(params['k8s_handler'].get_communitys(cache_enabled=False))))

    if 'crd' in params['view']:
        info = params['k8s_handler'].get_ip_address_pools(cache_enabled=False)
        k8s_output_handler.print_ip_address_pools(info)

        info = params['k8s_handler'].get_bgp_peers(cache_enabled=False)
        k8s_output_handler.print_bgp_peers(info)

        info = params['k8s_handler'].get_bfd_profiles(cache_enabled=False)
        k8s_output_handler.print_bfd_profiles(info)

        info = params['k8s_handler'].get_bgp_advertisements(cache_enabled=False)
        k8s_output_handler.print_bgp_advertisements(info)

        info = params['k8s_handler'].get_communitys(cache_enabled=False)
        k8s_output_handler.print_communitys(info)

        info = params['k8s_handler'].get_frr_configurations(cache_enabled=False)
        k8s_output_handler.print_frr_configurations_state(info)

    if 'cli' in params['view']:
        if bgp_mode is None:
            my_output.default('Use "iserver get ocp ovn-bgp" command instead')

        if bgp_mode in ['frr']:
            pods = params['k8s_handler'].get_metallb_pods(component='speaker', cache_enabled=False)
            my_output.my_table_ng(
                pods,
                [
                    ['Host', 'host_name'],
                    ['Pod', 'namespace_name'],
                    ['Ready', 'container_state_summary'],
                    ['FRR cli ', 'frr_cli']
                ]
            )

    if 'frr' in params['view']:
        if bgp_mode is None:
            my_output.default('Use "iserver get ocp ovn-bgp" command instead')

        if bgp_mode in ['frr']:
            output = params['k8s_handler'].get_metallb_pods_exec(
                nodes=params['node'], 
                commands=['show run']
            )
            for node in output:
                my_output.default('FRR %s [%s]' % (node, output[node]['host']), before_newline=True, underline=True)
                my_output.default(output[node]['show run'])

    if 'exec' in params['view']:
        if bgp_mode is None:
            my_output.default('Use "iserver get ocp ovn-bgp" command instead')

        if bgp_mode in ['frr']:
            if params['cmd'] is None:
                my_output.error('define cmd in exec mode')
            else:
                output = params['k8s_handler'].get_metallb_pods_exec(
                    nodes=params['node'], 
                    commands=[params['cmd']]
                )
                for node in output:
                    my_output.default('FRR %s [%s]' % (node, output[node]['host']), before_newline=True, underline=True)
                    my_output.default(output[node][params['cmd']])

    return True
