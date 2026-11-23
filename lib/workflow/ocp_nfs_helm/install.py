from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'helm_repo' not in params or params['helm_repo'] is None:
        params['helm_repo'] = 'https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts'

    if 'helm_namespace' not in params or params['helm_namespace'] is None:
        params['helm_namespace'] = 'kube-system'

    if 'helm_name' not in params or params['helm_name'] is None:
        params['helm_name'] = 'csi-driver-nfs'

    if 'helm_version' not in params or params['helm_version'] is None:
        params['helm_version'] = '4.6.0'

    return params, None


def add(params, my_output, log_id):
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

    my_output.default('- adding nfs helm repo')
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

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-fixup'] = True
    ocp_check_params['cli-helm-required'] = True
    ocp_check_params['verbose'] = True
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    my_output.default('NFS helm chart', before_newline=True)
    my_output.default('- Repo: %s' % (params['helm_repo']))
    my_output.default('- Namespace: %s' % (params['helm_namespace']))
    my_output.default('- Name: %s' % (params['helm_name']))
    my_output.default('- Version: %s' % (params['helm_version']), after_newline=True)

    if workflow_common.is_helm(params['cluster'], params['helm_namespace'], params['helm_name'], log_id=log_id, my_output=my_output):
        my_output.default('Helm chart already installed')
    else:
        my_output.default('Helm chart will be installed')
        if not add(params, my_output, log_id):
            return False

    return True
