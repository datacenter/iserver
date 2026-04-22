from lib import output_helper
from lib.workflow.ocp_bare_metal_host import common as local_common
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common


def validate(params):
    bmc_rules = [
        ['node', False, None, 'str', None, None, None, None],
        ['type', False, None, 'str', None, None, ['ucsc'], None],
        ['address', False, None, 'ip', None, None, None, None],
        ['username', False, None, 'str', None, None, None, None],
        ['password', False, None, 'str', None, None, None, None],
        ['cert', False, None, 'bool', None, None, None, None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['bmc', False, None, 'list-of-dict', 1, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, nested=dict(bmc=bmc_rules))
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Bare Metal Host - Enable (register)', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    # verify bmh node names
    bmhs = params['k8s_handler'].get_bare_metal_hosts(cache_enabled=False)
    if bmhs is None:
        my_output.error('Failed to get BareMetalHost crd')
        return False
    
    for bmc in params['bmc']:
        found = False
        for bmh in bmhs:
            if bmh['name'] == bmc['node']:
                if bmh['provisioning_state'] not in ['unmanaged', 'registering']:
                    if bmh['operational_state'] != 'detached':
                        my_output.error(
                            'Node [%s] unexpected state [provisioning:%s] [operational:%s]' % (
                                bmh['name'],
                                bmh['provisioning_state'],
                                bmh['operational_state']
                            )
                        )
                        return False
                
                found = True                
                break

        if not found:
            my_output.error('Node %s not found' % (bmc['node']))
            return False

    if params['k8s_handler'].is_proxy_configured():
        for bmc in params['bmc']:
            if not params['k8s_handler'].is_noproxy(bmc['address'], my_output=my_output):
                success = params['k8s_handler'].add_noproxy(
                    bmc['address'],
                    my_output=my_output,
                    confirmation=params['confirmation'],
                    wait=True
                )
                if not success:
                    return False

    target = []
    for bmc in params['bmc']:
        target.append(bmc['node'])
        success = params['k8s_handler'].set_bare_metal_host_secret(
            params['__default__']['namespace'],
            '%s-bmc-secret' % (bmc['node']),
            bmc['username'],
            bmc['password'],
            my_output=my_output,
            confirmation=params['confirmation'],
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].set_bare_metal_host_bmc(
            params['__default__']['namespace'],
            bmc['node'],
            bmc['type'],
            '%s-bmc-secret' % (bmc['node']),
            bmc['address'],
            bmc['cert'],
            my_output=my_output,
            confirmation=params['confirmation'],
            wait=params['wait']
        )
        if not success:
            return False

    bmhs = params['k8s_handler'].get_bare_metal_hosts(
        object_filter=['names:%s' % (','.join(target))], 
        cache_enabled=False
    )
    k8s_output_handler.print_bare_metal_hosts_state(bmhs)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- bare metal hosts configured')

    return True
