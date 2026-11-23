import os
from lib import output_helper
from lib.k8s import settings
from lib.k8s import main as k8s
from lib.workflow import helper as workflow_helper


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'verbose' not in params:
        params['verbose'] = False

    params['hide'] = workflow_helper.anonymize()
    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        return None, error

    settings_handler = settings.K8sSettings(log_id=log_id)
    cluster_settings = settings_handler.get_k8s_cluster(params['cluster'], strict_match=True)
    if cluster_settings is None:
        return None, 'Cluster not found: %s' % (params['cluster'])
    
    if params['verbose']:
        my_output.default('Kubernetes Cluster', before_newline=True, underline=True)
        my_output.default('- cluster: %s' % (my_output.add_color(params['cluster'], 'Blue')))
        my_output.default('- type: %s' % (cluster_settings['type']))
        if not params['hide']:
            my_output.default('- kubeconfig: %s' % (cluster_settings['kubeconfig']))


    if not os.path.isfile(cluster_settings['kubeconfig']):
        return params, 'Kubeconfig file not found: %s' % (cluster_settings['kubeconfig'])
    
    params['k8s_handler'] = k8s.K8s(
        kubeconfig_filename=cluster_settings['kubeconfig'], 
        cluster_type=cluster_settings['type'], 
        log_id=log_id, 
        cluster_name=cluster_settings['name']
    )

    if not params['k8s_handler'].check_api():
        if params['verbose']:
            my_output.default('- api: %s' % my_output.add_color('fails', 'Red'))
        return None, 'API fails'
    
    if params['verbose']:
        my_output.default('- api: %s' % my_output.add_color('working', 'Green'))

    return params, None
