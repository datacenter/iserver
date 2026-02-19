import json
from lib import output_helper
from lib.workflow import ocp_common as workflow_common


def verify(task):
    if 'nfs' not in task:
        task['nfs'] = {}
        task['nfs']['enabled'] = False

    if 'enabled' not in task['nfs']:
        task['nfs']['enabled'] = True

    if 'helm_repo' not in task['nfs']:
        task['nfs']['helm_repo'] = 'https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts'

    if 'helm_namespace' not in task['nfs']:
        task['nfs']['helm_namespace'] = 'kube-system'

    if 'helm_name' not in task['nfs']:
        task['nfs']['helm_name'] = 'csi-driver-nfs'

    if 'helm_version' not in task['nfs']:
        task['nfs']['helm_version'] = '4.6.0'

    if 'server' not in task['nfs']:
        return None, 'task.server.nfs.server expected'

    if 'share' not in task['nfs']:
        return None, 'task.server.nfs.share expected'

    if 'dir' not in task['nfs']:
        return None, 'task.server.nfs.dir expected'

    if 'storage_class' not in task['nfs']:
        task['nfs']['storage_class'] = 'nfs'

    if not isinstance(task['nfs']['enabled'], bool):
        return None, 'task.server.nfs.enabled must be true or false'

    return task, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    my_output.default('Storage NFS (CSI)', underline=True, before_newline=True)
    my_output.default(json.dumps(params, indent=4))

    params['k8s_handler'] = workflow_common.verify_cluster_name(params['cluster'], log_id=log_id)
    if params['k8s_handler'] is None:
        my_output.error('Cluster invalid: %s' % (params['cluster']))
        return None

    is_class = params['k8s_handler'].is_storage_class(
        params['storage_class'],
        cache_enabled=False
    )
    if is_class:
        my_output.default('- storage class already defined: %s' % (params['storage_class']))
        return True

    my_output.default('- storage class will be created: %s' % (params['storage_class']), after_newline=True)

    if workflow_common.is_nfs(params['cluster'], params['helm_namespace'], params['helm_name'], log_id=log_id, my_output=my_output):
        my_output.default('- NFS helm chart already installed')
    else:
        ssh_handler = workflow_common.get_management_node_ssh_handler(
            params['cluster'],
            log_id=log_id
        )
        if ssh_handler is None:
            my_output.error('Failed to get ssh handler to management node')
            return False

        success, output, error = ssh_handler.run_cmd('helm ls -n %s' % (params['helm_namespace']))
        if not success:
            my_output.error('Failed to check nfs helm chart')
            return False

        my_output.default('- NFS helm chart will be installed')
        success, output, error = ssh_handler.run_cmd(
            'helm repo add %s %s' % (
                params['helm_name'],
                params['helm_repo']
            )
        )
        if not success:
            my_output.error('Failed to add nfs helm repo')
            my_output.default(str(output))
            my_output.default(str(error))
            return False

        my_output.default('- nfs helm repo added')

        success, output, error = ssh_handler.run_cmd(
            'helm upgrade -i %s %s/%s --version %s --namespace %s' % (
                params['helm_name'],
                params['helm_name'],
                params['helm_name'],
                params['helm_version'],
                params['helm_namespace']
            )
        )
        if not success:
            my_output.error('Failed to install nfs helm chart')
            my_output.default(str(output))
            my_output.default(str(error))
            return False

        my_output.default('- nfs helm chart installed')

        deployments = [
            {'namespace': params['helm_namespace'], 'name': 'csi-nfs-controller'}
        ]
        success = params['k8s_handler'].wait_deployments_ready_state(deployments, my_output=my_output, optional=False)
        if not success:
            return False

        daemon_sets = [
            {'namespace': params['helm_namespace'], 'name': 'csi-nfs-node'}
        ]
        success = params['k8s_handler'].wait_daemon_sets_ready_state(daemon_sets, my_output=my_output, optional=False)
        if not success:
            return False

    body = {}
    body['apiVersion'] = 'storage.k8s.io/v1'
    body['kind'] = 'StorageClass'
    body['metadata'] = {}
    body['metadata']['name'] = params['storage_class']
    if params['default']:
        body['metadata']['annotations'] = {}
        body['metadata']['annotations']['storageclass.kubernetes.io/is-default-class'] = 'true'
    body['parameters'] = {}
    body['parameters']['server'] = params['server']
    body['parameters']['share'] = params['share']
    body['parameters']['subDir'] = params['dir']
    body['provisioner'] = 'nfs.csi.k8s.io'
    body['reclaimPolicy'] = 'Delete'
    body['volumeBindingMode'] = 'WaitForFirstConsumer'
    body['allowVolumeExpansion'] = True
    my_output.default(json.dumps(body, indent=4))

    success = params['k8s_handler'].create_storage_class(body)
    if not success:
        my_output.error('Failed to create storage class')
        return False

    my_output.default('- storage class created successfully', before_newline=True)

    return True
