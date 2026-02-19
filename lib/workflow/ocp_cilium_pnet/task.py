from lib.workflow.ocp_cilium_pnet import feature_enable
from lib.workflow.ocp_cilium_pnet import webhook_enable
from lib.workflow.ocp_cilium_pnet import test
from lib.workflow.ocp_cilium_pnet import feature_disable
from lib.workflow.ocp_cilium_pnet import webhook_disable
from lib.workflow.ocp_cilium_pnet import wipe


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_pnet.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_enable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'webhook' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_pnet.feature dict required'

        task['webhook']['cluster'] = cluster_name
        task['webhook']['confirmation'] = confirmation
        task['webhook'], error = webhook_enable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'test' in task:
        if not isinstance(task['test'], dict):
            return None, 'cilium_pnet.test dict required'

        task['test']['cluster'] = cluster_name
        task['test']['confirmation'] = confirmation
        task['test'], error = test.validate(task['test'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'feature',
        'webhook',
        'test'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_pnet task'
    
    return new_task, None


def run(params, log_id=None):
    if 'feature' in params:
        success = feature_enable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    if 'webhook' in params:
        success = webhook_enable.run(params['webhook'], log_id=log_id)
        if not success:
            return False
        
    if 'test' in params:
        success = test.run(params['test'], log_id=log_id)
        if not success:
            return False

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'feature' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_pnet.feature dict required'

        task['feature']['cluster'] = cluster_name
        task['feature']['confirmation'] = confirmation
        task['feature'], error = feature_disable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'webhook' in task:
        if not isinstance(task['feature'], dict):
            return None, 'cilium_pnet.feature dict required'

        task['webhook']['cluster'] = cluster_name
        task['webhook']['confirmation'] = confirmation
        task['webhook'], error = webhook_disable.validate(task['feature'])
        if error is not None:
            return None, error

    if 'wipe' in task:
        if not isinstance(task['wipe'], dict):
            return None, 'cilium_pnet.wipe dict required'

        task['wipe']['cluster'] = cluster_name
        task['wipe']['confirmation'] = confirmation
        task['wipe'], error = wipe.validate(task['wipe'])
        if error is not None:
            return None, error

    new_task = {}
    allowed_keys = [
        'feature',
        'webhook',
        'wipe'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for cilium_pnet task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'wipe' in params:
        success = wipe.run(params['wipe'], log_id=log_id)
        if not success:
            return False

    if 'webhook' in params and 'feature' not in params:
        success = webhook_disable.run(params['webhook'], log_id=log_id)
        if not success:
            return False
        
    if 'feature' in params:
        success = feature_disable.run(params['feature'], log_id=log_id)
        if not success:
            return False

    return True