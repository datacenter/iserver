import json
from lib import filter_helper
from lib.workflow import ocp_common


def get_default_params():
    params = {}
    params['namespace'] = 'cilium'
    params['operator-name'] = 'cilium-operator'
    params['operator-lease'] = 'cilium-operator-resource-lock'
    params['agent-name'] = 'cilium'
    params['package'] = 'clife'
    return params


def get_subscription(params, my_output, verbose, cache_enabled=True):
    namespace = filter_helper.get(params, '__default__:namespace')
    if namespace is None:
        namespace = 'cilium'

    name = filter_helper.get(params, '__default__:package')
    if name is None:
        name = 'clife'

    subscription = params['k8s_handler'].get_subscription(
        namespace,
        name,
        csv_info=True,
        plan_info=True,
        return_mo=False,
        cache_enabled=cache_enabled
    )
    if subscription is None:
        my_output.default('Cilium operator %s' % (my_output.add_color('not found', 'Red')))
        return None

    if not verbose:
        my_output.default('Cilium cni %s' % (my_output.add_color('found', 'Green')))
        
    print_subscription(my_output, subscription, verbose=verbose)
    return subscription


def is_cilium(params, my_output, install_plan_enforced=False):
    subscription = get_subscription(params, my_output, params['verbose'])
    if subscription is None:
        return False

    if install_plan_enforced:
        approved = filter_helper.get(subscription, 'installplan:approved')
        if approved is not None:
            if not approved:            
                my_output.error('Install plan needs to be approved first')
                return False

    return True


def print_subscription(my_output, subscription, verbose=True):
    try:
        subscription['__Output']['installplan.approvedTick'] = subscription['installplan']['__Output']['approvedTick']
    except BaseException:
        pass
    
    ocp_common.dictionary(
        my_output, 
        'Operator',
        subscription,
        [
            ['subscription', 'namespace_name'],
            ['package', 'packageT'],
            ['channel', 'channel'],
            ['install plan', 'install_planT'],
            ['install plan approved', 'installplan.approvedTick'],
            ['installed csv', 'csvT'],
            ['latest_csv', 'csvTick']
        ],
        verbose=verbose
    )


def print_csv(my_output, csv):
    ocp_common.dictionary(
        my_output, 
        'Cluster Service Version',
        csv,
        [
            ['namespace', 'namespace'],
            ['name', 'name'],
            ['provider', 'provider_name'],
            ['description', 'display_name'],
            ['maturity', 'maturityT'],
            ['version', 'version'],
            ['image', 'image']
        ]
    )

def show_operators(params, my_output, k8s_output_handler):
    lease = params['k8s_handler'].get_lease(
        params['__default__']['namespace'],
        params['__default__']['operator-lease'],
        cache_enabled=False
    )
    pods = params['k8s_handler'].get_cilium_operator_pods(
        lease=lease,
        cache_enabled=False
    )

    if pods is None:
        my_output.error('Failed to get cilium operator pods')
    else:
        k8s_output_handler.print_pods_state(
            pods,
            skip=['Net', 'Restart']
        )

def show_agents(params, my_output, k8s_output_handler):
    pods = params['k8s_handler'].get_cilium_agent_pods(
        cache_enabled=False
    )

    if pods is None:
        my_output.error('Failed to get cilium agent pods')
    else:
        k8s_output_handler.print_pods_state(
            pods,
            skip=['Net', 'Restart']
        )

def show_agents_version(params, my_output, versions):
    pods = params['k8s_handler'].get_cilium_agent_pods(
        cache_enabled=False
    )

    if pods is None:
        my_output.error('Failed to get cilium agent pods')
        return

    for pod in pods:
        for key in versions:
            if key == pod['name']:
                try:
                    pod['version'] = json.loads(versions[key].replace("'", '"'))['Client']['Version']
                except BaseException:
                    pod['version'] = '---'

    pods = sorted(
        pods,
        key=lambda i: i['host_name']
    )

    my_output.my_table_ng(
        pods,
        [
            ['Pod', 'namespace_nameT'],
            ['Ready', 'container_state_summary'],
            ['Label', 'phaseT'],
            ['Node', 'host_name'],
            ['IP', 'pod_ip'],
            ['Cilium Agent Version', 'version'],
            ['Age', 'age']
        ]
    )