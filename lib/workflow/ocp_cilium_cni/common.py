import json
import copy
from lib import filter_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common
from lib.workflow import helper as workflow_helper


def initialize(params, my_output, log_id, mgmt_required=False, api_check=True):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['kube-api-check'] = api_check
    ocp_check_params['mgmt-required'] = mgmt_required
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['kubeconfig_filename'] = ocp_params['data']['kubeconfig_filename']
    params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id)
    if mgmt_required:
        if params['ssh_handler'] is None:
            my_output.error('Management access required and fails')
            return None

    return params


def get_default_params():
    params = {}
    params['namespace'] = 'cilium'
    params['operator-name'] = 'cilium-operator'
    params['operator-lease'] = 'cilium-operator-resource-lock'
    params['agent-name'] = 'cilium'
    params['package'] = 'clife'
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def is_cilium(params, my_output, install_plan_enforced=False):
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['package'],
        csv_info=True,
        plan_info=True,
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Cilium operator %s' % (my_output.add_color('not found', 'Red')))
        return False

    if 'verbose' not in params:
        verbose = True
    else:
        verbose = params['verbose']

    if not verbose:
        my_output.default('Cilium cni %s' % (my_output.add_color('found', 'Green')))
        
    print_subscription(my_output, subscription, verbose=verbose)

    approved = filter_helper.get(subscription, 'installplan:approved')
    if approved is not None:
        if not approved:
            if install_plan_enforced:
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
    if workflow_helper.anonymize():
        csv['image'] = '*******'
        
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
    lease = params['k8s_handler'].get_lease_optimized(
        params['namespace'],
        params['operator-lease'],
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