import json
from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_bm_install import common as ocp_bm_common


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    my_output.default('Node annotation', underline=True, before_newline=True)
    params['k8s_handler'] = workflow_common.verify_cluster_name(params['cluster'], log_id=log_id)
    if params['k8s_handler'] is None:
        my_output.error('Cluster invalid: %s' % (params['cluster']))
        return None

    for server in params['server']:
        redfish_handler = ocp_bm_common.get_server_redfish_handler(
            server['redfish'],
            log_id
        )

        if not redfish_handler.is_connected():
            my_output.error('Redfish connection to server failed: %s' % (server['redfish']['endpoint_ip']))
            return False

        chassis_uri = redfish_handler.endpoint_handler.get_chassis_uri()
        if chassis_uri is None:
            my_output.error('Getting redfish chassis uri failed: %s' % (server['redfish']['endpoint_ip']))
            return False

        my_output.default('Redfish endpoint: %s' % (server['redfish']['endpoint_ip']))
        values = redfish_handler.get_properties(chassis_uri)
        if values is not None:
            keys = [
                'ChassisType',
                'Model',
                'SerialNumber',
                'PowerState'
            ]
            for key in keys:
                if key in values:
                    my_output.default('- %s: %s' % (key, values[key]))
                    server['redfish'][key] = values[key]

        node_info = params['k8s_handler'].get_node(
            server['hostname']
        )
        if node_info is None:
            my_output.error('Cluster node %s not found' % (server['hostname']))
            return False

        my_output.default('Cluster node: %s' % (server['hostname']))

        annotation_key = 'server-imc'
        annotation_value = server['redfish']['endpoint_ip']

        if not params['k8s_handler'].add_node_annotation(server['hostname'], annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (server['hostname']))
            return False

        my_output.default('- annotation key [%s] value [%s]' % (annotation_key, annotation_value))

        annotation_key = 'server-serial'
        annotation_value = server['redfish']['SerialNumber']

        if not params['k8s_handler'].add_node_annotation(server['hostname'], annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (server['hostname']))
            return False

        my_output.default('- annotation key [%s] value [%s]' % (annotation_key, annotation_value))

        annotation_key = 'server-model'
        annotation_value = server['redfish']['Model']

        if not params['k8s_handler'].add_node_annotation(server['hostname'], annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (server['hostname']))
            return False

        my_output.default('- annotation key [%s] value [%s]' % (annotation_key, annotation_value))

    return True
