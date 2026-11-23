import copy
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_nfd_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res', 'annotation'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def collect_state_info(params, my_output):
    my_output.debug('- instance')
    params['instance'] = None
    params['summary']['instanceReady'] = False
    instances = params['k8s_handler'].get_node_feature_discoverys(cache_enabled=False)
    if instances is not None and len(instances) == 1:
        params['instance'] = instances[0]
        params['summary']['instanceReady'] = params['instance']['ready']

    params['summary'] = params['k8s_handler'].add_tick(
        params['summary'],
        'instanceReady',
        True,
        'instanceReadyTick'
    )

    my_output.debug('- nodes')

    params['nodes'] = params['k8s_handler'].get_nodes(cache_enabled=False)
    if params['nodes'] is None:
        my_output.error('Failed to get kubernetes nodes')
        return params
    
    node_count = 0
    node_with_annotation = []
    node_without_annotation = []
    for node in params['nodes']:
        if 'nfd.node.kubernetes.io/feature-labels' in node['annotation']:
            node_count +=1
            node_with_annotation.append(node['name'])

    for node in params['nodes']:
        if node['name'] not in node_with_annotation:
            node_without_annotation.append(node['name'])

    params['summary']['nodes_summary'] = '%s/%s' % (
        node_count,
        len(params['nodes'])
    )
    if node_count == len(params['nodes']):
        params['summary']['__Output']['nodes_summary'] = 'Green'
        params['summary']['nodes_without_annotation'] = '---'
    else:
        params['summary']['__Output']['nodes_summary'] = 'Red'
        params['summary']['nodes_without_annotation'] = ', '.join(node_without_annotation)

    return params


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

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            continue

        params = ocp_common.get_operator(params, my_output)
        if params['subscription'] is None:
            continue

        params = collect_state_info(params, my_output)

        if 'state' in params['view']:
            my_output.dictionary_ng(
                'State',
                params['summary'],
                [
                    ['package', 'package'],
                    ['csv', 'csv'],
                    ['resources', 'readyTick'],
                    ['instance', 'instanceReadyTick'],
                    ['node annotations', 'nodes_summary'],
                    ['no annotation', 'nodes_without_annotation']
                ]
            )

        if 'res' in params['view']:
            ocp_common.print_subscription(params['subscription'], my_output)
            ocp_common.print_resources(params, k8s_output_handler)
            if params['instance'] is not None:
                k8s_output_handler.print_node_feature_discoverys([params['instance']])

        if 'annotation' in params['view']:
            if params['nodes'] is not None:
                for node in params['nodes']:
                    my_output.default('Node [%s]' % (node['name']), before_newline=True)
                    for annotation in node['annotation']['nfd.node.kubernetes.io/feature-labels'].split(','):
                        my_output.default('\t%s' % (annotation))

    return True
