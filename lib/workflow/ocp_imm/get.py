from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_imm import common as local_common


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
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Hardware - Get', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    nodes_info = params['k8s_handler'].get_nodes_info()
    if nodes_info is None:
        my_output.error(
            'Failed to get nodes info'
        )
        return False

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
