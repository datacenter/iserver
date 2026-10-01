import copy
from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_imm import common as local_common
from lib.workflow import ocp_common


def get_ips(param):
    cluster_name = None
    node_name = None

    if len(param.split(':')) == 1:
        cluster_name = param

    if len(param.split(':')) == 2:
        cluster_name, node_name = param.split(':')

    if cluster_name is None:
        return None, 'Wrong parameter'

    k8s_handler = workflow_common.verify_cluster_name(cluster_name)
    if k8s_handler is None:
        return None, 'Wrong cluster name'

    nodes_info = k8s_handler.get_nodes_info()
    if nodes_info is None:
        return None, 'Failed to get nodes info'

    ips = []
    for node_info in nodes_info:
        if node_name is not None and node_info['info']['name'] != node_name:
            continue

        for key in node_info['info']['annotations']:
            if key == 'server-imc':
                ips.append(node_info['info']['annotations'][key])

    return ips, None


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


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

        nodes_info = params['k8s_handler'].get_nodes_info()
        if nodes_info is None:
            my_output.error(
                'Failed to get nodes info'
            )
            continue

        nodes = []
        for node_info in nodes_info:
            item = {}
            item['node'] = node_info['info']['name']
            item['imc'] = '--'
            item['moid'] = '--'
            item['deviceid'] = '--'
            item['name'] = '--'
            item['model'] = '--'
            item['serial'] = '--'

            for key in node_info['info']['annotations']:
                if key == 'server-imc':
                    item['imc'] = node_info['info']['annotations'][key]
                if key == 'server-name':
                    item['name'] = node_info['info']['annotations'][key]
                if key == 'server-model':
                    item['model'] = node_info['info']['annotations'][key]
                if key == 'server-serial':
                    item['serial'] = node_info['info']['annotations'][key]
                if len(key.split('intersight-')) > 1:
                    if len(key.split('intersight-dev-')) > 1:
                        item['deviceid'] = node_info['info']['annotations'][key]
                    else:
                        item['moid'] = node_info['info']['annotations'][key]

            nodes.append(
                item
            )

        order = [
            'node',
            'imc',
            'moid',
            'deviceid',
            'name',
            'model',
            'serial'
        ]

        headers = [
            'Mode',
            'Management IP',
            'Intersight Moid',
            'Registered Device',
            'Name',
            'Model',
            'Serial'
        ]

        my_output.my_table(
            nodes,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    return True