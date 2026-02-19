from lib.workflow.ocp_cilium_bgp import feature_enable
from lib.workflow.ocp_cilium_bgp import cluster_create
from lib.workflow.ocp_cilium_bgp import feature_disable
from lib.workflow.ocp_cilium_bgp import wipe


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium-bgp.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_enable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'cluster' in task:
        if not isinstance(task['cluster'], dict):
            return None, 'cilium-bgp.cluster dict required'

        task['cluster']['cluster'] = cluster_name
        task['cluster']['confirmation'] = confirmation
        task['cluster'], error = cluster_create.validate(task['cluster'])
        if error is not None:
            return None, error
           
    new_task = {}
    allowed_keys = [
        'feature',
        'cluster'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium-bgp task'
    
    return new_task, None


def run(params, log_id=None):
    if 'feature' in params:
        success = feature_enable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    if 'cluster' in params:
        success = cluster_create.run(params['cluster'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium-bgp.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_disable.validate(task['feature'])
        if error is not None:
            return None, error
            
    if 'wipe' in task:
        if not isinstance(task['wipe'], dict):
            return None, 'cilium-bgp.wipe dict required'

        task['wipe']['cluster'] = cluster_name
        task['wipe']['confirmation'] = confirmation
        task['wipe'], error = wipe.validate(task['wipe'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'feature',
        'wipe'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium-bgp task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'wipe' in params:
        success = wipe.run(params['wipe'], log_id=log_id)
        if not success:
            return False
        
    if 'feature' in params:
        success = feature_disable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    return True