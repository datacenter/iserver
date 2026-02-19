from lib import ip_helper
from lib.workflow.ocp_helm_cli import install


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if not task['enabled']:
        return task, None

    # Potential improvement is checking Cilium CNI

    if 'download_url' in task and task['download_url'] is not None:
        return task, None
    
    if 'version_url' not in task or task['version_url'] is None:
        task['version_url'] = 'https://raw.githubusercontent.com/cilium/hubble/main/stable.txt'

    if 'version' not in task or task['version'] is None:
        task['version'] = ip_helper.get_url(
            task['version_url']
        ).strip('\n')
        if task['version'] is None:
            return None, 'Failed to get hubble version from %s' % (task['version_url'])

    task['download_url'] = 'https://github.com/cilium/hubble/releases/download/%s/hubble-linux-amd64.tar.gz' % (task['version'])

    return task, None

def run(params, log_id=None):
    if params['enabled']:
        return install.run(params, log_id=log_id)
    
    return True