from lib.workflow.ocp_tridentctl_cli import install


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if 'download_url' in task or 'version' in task:
        task['enabled'] = True

    if not task['enabled']:
        return task, None

    if 'download_url' not in task:
        task['download_url'] = None

    if 'version' not in task:
        task['version'] = None

    if task['download_url'] is None and task['version'] is None:
        return None, 'tridentctl: download url or version required'

    if task['download_url'] is None:
        task['download_url'] = 'https://github.com/NetApp/trident/releases/download/v%s/trident-installer-%s.tar.gz' % (
            task['version'],
            task['version']
        )

    return task, None

def run(params, log_id=None):
    if params['enabled']:
        return install.run(params, log_id=log_id)
    
    return True