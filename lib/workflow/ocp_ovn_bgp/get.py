from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common


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
        
    return ocp_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OVNKubernetes - Get frr-k8s information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    frr_enabled = params['k8s_handler'].is_ovn_frr_enabled()
    ra_enabled = params['k8s_handler'].is_ovn_frr_ra_enabled()

    if 'state' in params['view']:
        info = params['k8s_handler'].get_cluster_network_operator(cache_enabled=False)
        k8s_output_handler.print_network_operators([info])

        my_output.default('Feature', before_newline=True)
        if frr_enabled:
            my_output.default('- frr-k8s:  %s' % (my_output.add_color('enabled', 'Green')))
        else:
            my_output.default('- frr-k8s: %s' % (my_output.add_color('disabled', 'Red')))

        if ra_enabled:
            my_output.default('- route advertisement: %s' % (my_output.add_color('enabled', 'Green')))
        else:
            my_output.default('- route advertisement: %s' % (my_output.add_color('disabled', 'Red')))

        if frr_enabled:
            my_output.default('Configuration')
            frr_summary = params['k8s_handler'].get_frr_configurations_summary(cache_enabled=False)
            my_output.default('- frr: %s' % my_output.add_color(frr_summary['summary'], frr_summary['color']))

            if ra_enabled:
                ra_summary = params['k8s_handler'].get_route_advertisements_summary(cache_enabled=False)
                my_output.default('- route advertisement: %s' % (my_output.add_color(ra_summary['summary'], ra_summary['color'])))

            configs = params['k8s_handler'].get_frr_node_states(cache_enabled=False)
            if configs is not None:
                for config in configs:
                    my_output.default('- node %s: %s, %s' % (config['name'], my_output.add_color_bool(config['converted'], 'converted'), my_output.add_color_bool(config['reloaded'], 'reloaded')))

        if frr_enabled:
            sessions = params['k8s_handler'].get_bgp_session_states_summary(cache_enabled=False)
            if sessions is not None:
                my_output.default('BGP sessions')
                my_output.default('- configured nodes: %s' % (sessions['nodes']))
                for node in sessions['node']:
                    my_output.default('- %s: %s' % (node, my_output.add_color(sessions['node'][node]['summary'], sessions['node'][node]['color'])))

    if 'cli' in params['view']:
        if not frr_enabled:
            my_output.default('FRR %s' % (my_output.add_color('not enabled', 'Red')))
            return False
        
        pods = params['k8s_handler'].get_ovn_frr_pods(cache_enabled=False)
        my_output.my_table_ng(
            pods,
            [
                ['Host', 'host_name'],
                ['Pod', 'namespace_name'],
                ['Ready', 'container_state_summary'],
                ['FRR cli ', 'frr_cli']
            ]
        )

    if 'config' in params['view']:
        if not frr_enabled:
            my_output.default('FRR %s' % (my_output.add_color('not enabled', 'Red')))
            return False
   
        configs = params['k8s_handler'].get_frr_configurations(cache_enabled=False)
        if configs is None:
            my_output.error('failed to get FRRConfiguration objects')
            return False
        
        k8s_output_handler.print_frr_configurations_state(configs)

    if 'frr' in params['view']:
        if not frr_enabled:
            my_output.default('FRR %s' % (my_output.add_color('not enabled', 'Red')))
            return False
        
        object_filter = None
        if len(params['node']) > 0:
            object_filter = ['names:%s' % (','.join(params['node']))]
        configs = params['k8s_handler'].get_frr_node_states(object_filter=object_filter, cache_enabled=False)
        if configs is None:
            my_output.error('failed to get FRRNodeState objects')
            return False
        
        k8s_output_handler.print_frr_node_states(configs)

    if 'ra' in params['view'] or 'ra-config' in params['view']:
        if not ra_enabled:
            my_output.default('Route advertisement %s' % (my_output.add_color('not enabled', 'Red')))
        else:
            frr_info = False
            if 'ra-config' in params['view']:
                frr_info = True
            configs = params['k8s_handler'].get_route_advertisements(frr_info=frr_info, cache_enabled=False)
            if configs is None:
                my_output.error('failed to get RouteAdvertisement objects')
                return False
            
            k8s_output_handler.print_route_advertisements_state(configs)

    if 'session' in params['view']:
        if not frr_enabled:
            my_output.default('FRR %s' % (my_output.add_color('not enabled', 'Red')))
            return False
        
        object_filter = []
        if len(params['node']) > 0:
            object_filter.append('nodes:%s' % (','.join(params['node'])))
        if len(params['peer']) > 0:
            object_filter.append('peers:%s' % (','.join(params['peer'])))

        sessions = params['k8s_handler'].get_bgp_session_states(object_filter=object_filter, cache_enabled=False)
        if sessions is None:
            my_output.error('failed to get BGPSessionState objects')
            return False
        
        k8s_output_handler.print_bgp_session_states_state(sessions)

    if 'exec' in params['view']:
        if params['cmd'] is None:
            my_output.error('define cmd in exec mode')
        else:
            output = params['k8s_handler'].get_ovn_frr_pods_exec(
                nodes=params['node'], 
                commands=[params['cmd']]
            )
            for node in output:
                my_output.default('FRR %s [%s]' % (node, output[node]['host']), before_newline=True, underline=True)
                my_output.default(output[node][params['cmd']])


    return True
