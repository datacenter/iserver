from lib.workflow.ocp_ovn_bgp import feature_enable
from lib.workflow.ocp_ovn_bgp import ra_enable
from lib.workflow.ocp_ovn_bgp import feature_disable
from lib.workflow.ocp_ovn_bgp import ra_disable


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'ovn-bgp.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature']['base_directory'] = cluster_settings['directory']
        task['feature'], error = feature_enable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'ra' in task:
        if not isinstance(task['ra'], dict):
            return None, 'ovn-bgp.ra dict required'

        task['ra']['cluster'] = cluster_name
        task['ra']['confirmation'] = confirmation
        task['ra']['base_directory'] = cluster_settings['directory']
        task['ra'], error = ra_enable.validate(task['ra'])
        if error is not None:
            return None, error
            
    new_task = {}
    allowed_keys = [
        'feature',
        'ra'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for ovn-bgp task'
    
    return new_task, None


def run(params, log_id=None):
    if 'feature' in params:
        success = feature_enable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    if 'ra' in params:
        success = ra_enable.run(params['ra'], log_id=log_id)
        if not success:
            return False
        
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'ovn-bgp.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_disable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'ra' in task:
        if not isinstance(task['ra'], dict):
            return None, 'ovn-bgp.ra dict required'

        task['ra']['cluster'] = cluster_name
        task['ra']['confirmation'] = confirmation
        task['ra'], error = ra_disable.validate(task['ra'])
        if error is not None:
            return None, error
            
    new_task = {}
    allowed_keys = [
        'feature',
        'ra'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for ovn-bgp task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'ra' in params:
        success = ra_disable.run(params['ra'], log_id=log_id)
        if not success:
            return False

    if 'feature' in params:
        success = feature_disable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    return True