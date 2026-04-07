from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_nfd_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['annotation', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Node Feature Discover Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
        my_output=my_output
    )
    if subscription is None:
        return True
    
    my_output.default('Instance', underline=True)
    nfds = params['k8s_handler'].get_node_feature_discoverys(
        cache_enabled=False
    )
    if nfds is None:
        my_output.error('failed to get nfd instances')
        return False

    if len(nfds) == 0:
        my_output.default('- no instance found')
        with_instance=False
    else:
        with_instance=True
        names = filter_helper.get(nfds, 'name')
        if names is None:
            my_output.error('failed to get nfd instances')
            return False

        my_output.default('- name: %s' % (','.join(names)))

    ready = params['k8s_handler'].is_subscription_nfd_ready(with_instance=with_instance, my_output=my_output, details=True)
    if ready:
        nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
        if nodes is None:
            my_output.error('Failed to get kubernetes nodes')
            return False
        
        my_output.default('NFD node annotations', underline=True, before_newline=True)
        for node in nodes:
            if 'nfd.node.kubernetes.io/feature-labels' not in node['annotations']:
                my_output.error('No nfd annotations on node [%s]' % (node['name']))
            else:
                if not params['annotation']:
                    my_output.default('- found in node %s' % (node['name']))

                if params['annotation']:
                    my_output.default('- node [%s]' % (node['name']))
                    for annotation in node['annotations']['nfd.node.kubernetes.io/feature-labels'].split(','):
                        my_output.default('\t%s' % (annotation))

    return True
