import json
import base64
from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_bm_install import common as ocp_bm_common


def verify(task):
    if 'power-management' not in task:
        task['power-management'] = {}
        task['power-management']['enabled'] = False
        task['power-management']['wait-registered'] = True
        task['power-management']['check-ssl'] = True

    if 'enabled' not in task['power-management']:
        task['power-management']['enabled'] = False

    if 'namespace' not in task['power-management']:
        task['power-management']['namespace'] = 'openshift-machine-api'

    if 'wait-registered' not in task['power-management']:
        task['power-management']['wait-registered'] = True

    if 'check-ssl' not in task['power-management']:
        task['power-management']['check-ssl'] = True

    if not isinstance(task['power-management']['enabled'], bool):
        return None, 'task.server.power-management.enabled must be true or false'

    return task, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    my_output.default('Power management', underline=True, before_newline=True)
    if not params['enabled']:
        my_output.default('Not enabled')
        return True

    params['k8s_handler'] = workflow_common.verify_cluster_name(params['cluster'], log_id=log_id)
    if params['k8s_handler'] is None:
        my_output.error('Cluster invalid: %s' % (params['cluster']))
        return None

    for server in params['server']:
        my_output.default('Cluster node annotion and secret: %s' % (server['hostname']))
        node_info = params['k8s_handler'].get_node(
            server['hostname']
        )
        if node_info is None:
            my_output.error('Cluster node %s not found' % (server['hostname']))
            return False

        if 'server-imc' not in node_info['annotations']:
            my_output.error('Cluster node annotation not found: server-imc')
            return False

        my_output.default('- annotation key [server-imc] value [%s]' % (node_info['annotations']['server-imc']))
        my_output.default('- redfish username: %s' % (server['redfish']['username']))
        my_output.default('- redfish password: %s' % (server['redfish']['password']))

        secret_namespace = params['namespace']
        secret_name = '%s-bmc-secret' % (server['hostname'])

        if params['k8s_handler'].is_secret(secret_namespace, secret_name, cache_enabled=False):
            my_output.default(
                '- secret already created: %s/%s' % (
                    secret_namespace,
                    secret_name
                )
            )
        else:
            my_output.default(
                '- secret needs to be created with redfish credentials: %s/%s' % (
                    secret_namespace,
                    secret_name
                )
            )
            kv = {}
            kv['username'] = base64.b64encode(
                server['redfish']['username'].encode('utf-8')
            ).decode('utf-8')
            kv['password'] = base64.b64encode(
                server['redfish']['password'].encode('utf-8')
            ).decode('utf-8')
            my_output.default('- encoded redfish username: %s' % (kv['username']))
            my_output.default('- encoded redfish password: %s' % (kv['password']))

            labels = {}
            labels['environment.metal3.io'] = 'baremetal'

            success = params['k8s_handler'].create_secret_kv_mo(
                secret_namespace,
                secret_name,
                kv,
                labels=labels
            )
            if not success:
                my_output.error('Failed to create kubernetes secret with redfish credentials')
                return False

            my_output.default(
                '- secret with redfish credentials created: %s/%s' % (
                    secret_namespace,
                    secret_name
                )
            )

        my_output.default('Bare metal host: %s' % (server['hostname']))

        bare_metal_host_mo = params['k8s_handler'].get_bare_metal_host(
            params['namespace'],
            server['hostname'],
            return_mo=True,
            cache_enabled=False
        )
        if bare_metal_host_mo is None:
            my_output.error('BareMetalHost object not found')
            return False

        if 'bmc' in bare_metal_host_mo['spec'] and len(bare_metal_host_mo['spec']['bmc']['address']) > 0:
            my_output.default('- bmc already configured')
            my_output.default('- address: %s' % (bare_metal_host_mo['spec']['bmc']['address']))
            my_output.default('- secret: %s' % (bare_metal_host_mo['spec']['bmc']['credentialsName']))
            my_output.default('- disable SSL: %s' % (bare_metal_host_mo['spec']['bmc']['disableCertificateVerification']))
            continue

        my_output.default('- bmc needs to be configured')
        bare_metal_host_mo['spec']['bmc'] = {}
        bare_metal_host_mo['spec']['bmc']['address'] = server['redfish']['endpoint_ip']
        bare_metal_host_mo['spec']['bmc']['credentialsName'] = secret_name
        bare_metal_host_mo['spec']['bmc']['disableCertificateVerification'] = params['check-ssl']
        my_output.default(json.dumps(bare_metal_host_mo['spec']['bmc'], indent=4))

        success = params['k8s_handler'].set_bare_metal_host_mo(bare_metal_host_mo)
        if not success:
            my_output.error('Failed to update BareMetalHost object')
            return False

        my_output.default('BareMetalHost object updated with bmc credentials for power management')

    return True
