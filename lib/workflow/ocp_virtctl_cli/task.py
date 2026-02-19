from lib.workflow.ocp_virtctl_cli import install


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if not task['enabled']:
        return task, None

    if 'download_url' in task and task['download_url'] is not None:
         return task, None
    
    if k8s_handler is None and cluster_settings is None:
        return None, 'Cluster handler or settings required'

    if cluster_settings is not None:
        task['download_url'] = 'https://hyperconverged-cluster-cli-download-openshift-cnv.apps.%s.%s/amd64/linux/virtctl.tar.gz' % (
            cluster_settings['name'],
            cluster_settings['base_dns_domain']
        )
        return task, None

    dns_info = k8s_handler.get_dns()
    if dns_info is None:
        return None, 'Failed to get dns information'
    
    if dns_info['domain'] is None:
        return None, 'Failed to get dns information'

    task['download_url'] = 'https://hyperconverged-cluster-cli-download-openshift-cnv.apps.%s/amd64/linux/virtctl.tar.gz' % (
        dns_info['domain']
    )

    return task, None

def run(params, log_id=None):
    if params['enabled']:
        return install.run(params, log_id=log_id)
    
    return True