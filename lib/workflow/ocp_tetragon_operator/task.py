from lib.workflow.ocp_tetragon_operator import operator_create
from lib.workflow.ocp_prometheus import monitoring_enable
from lib.workflow.ocp_tetragon_operator import prometheus_enable
from lib.workflow.ocp_tetragon_operator import crd_create
from lib.workflow.ocp_tetragon_operator import operator_delete
from lib.workflow.ocp_tetragon_operator import prometheus_disable
from lib.workflow.ocp_tetragon_operator import crd_delete
from lib.workflow.ocp_tetragon_operator import wipe

def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'tetragon.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator']['confirmation'] = confirmation
        task['operator'], error = operator_create.validate(task['operator'])
        if error is not None:
            return None, error

    if 'prometheus' in task:
        if not isinstance(task['prometheus'], dict):
            return None, 'tetragon.prometheus dict required'

        task['prometheus']['cluster'] = cluster_name
        task['prometheus']['confirmation'] = confirmation
        task['prometheus'], error = prometheus_enable.validate(task['prometheus'])
        if error is not None:
            return None, error

    if 'crd' in task:
        if not isinstance(task['crd'], dict):
            return None, 'tetragon.crd dict required'

        task['crd']['cluster'] = cluster_name
        task['crd']['confirmation'] = confirmation
        task['crd']['base_directory'] = cluster_settings['directory']
        task['crd'], error = crd_create.validate(task['crd'])
        if error is not None:
            return None, error

    if 'wipe' in task:
        if not isinstance(task['wipe'], dict):
            return None, 'tetragon.wipe dict required'

        task['wipe']['cluster'] = cluster_name
        task['wipe'], error = wipe.validate(task['wipe'])
        if error is not None:
            return None, error
                
    new_task = {}
    allowed_keys = [
        'operator',
        'prometheus',
        'crd',
        'wipe'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for tetragon task'
    
    return new_task, None


def run(params, log_id=None):
    if 'operator' in params:
        success = operator_create.run(params['operator'], log_id=log_id)
        if not success:
            return False

    if 'prometheus' in params:
        success = monitoring_enable.run(params['prometheus'], log_id=log_id)
        if not success:
            return False

        success = prometheus_enable.run(params['prometheus'], log_id=log_id)
        if not success:
            return False

    if 'wipe' in params:
        success = wipe.run(params['wipe'], log_id=log_id)
        if not success:
            return False  
        
    if 'crd' in params:
        success = crd_create.run(params['crd'], log_id=log_id)
        if not success:
            return False             

    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    if 'operator' in task:
        if not isinstance(task['operator'], dict):
            return None, 'tetragon.operator dict required'

        task['operator']['cluster'] = cluster_name
        task['operator'], error = operator_delete.validate(task['operator'])
        if error is not None:
            return None, error

        if 'wipe' not in task:
            task['wipe'] = {}
            task['wipe']['cluster'] = cluster_name
            task['wipe'], error = wipe.validate(task['operator'])
            if error is not None:
                return None, error

    if 'prometheus' in task:
        if not isinstance(task['prometheus'], dict):
            return None, 'tetragon.prometheus dict required'

        task['prometheus']['cluster'] = cluster_name
        task['prometheus'], error = prometheus_disable.validate(task['prometheus'])
        if error is not None:
            return None, error

    if 'wipe' in task:
        if not isinstance(task['wipe'], dict):
            return None, 'tetragon.wipe dict required'

        task['wipe']['cluster'] = cluster_name
        task['wipe'], error = wipe.validate(task['wipe'])
        if error is not None:
            return None, error
        
    if 'crd' in task:
        if not isinstance(task['crd'], dict):
            return None, 'tetragon.crd dict required'

        task['crd']['cluster'] = cluster_name
        task['crd']['base_directory'] = cluster_settings['directory']
        task['crd'], error = crd_delete.validate(task['crd'])
        if error is not None:
            return None, error
            
    new_task = {}
    allowed_keys = [
        'operator',
        'prometheus',
        'crd',
        'wipe'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for tetragon task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'wipe' in params or 'operator' in params:
        success = wipe.run(params['operator'], log_id=log_id)
        if not success:
            return False
        
    if 'crd' in params and 'operator' not in params:
        success = crd_delete.run(params['crd'], log_id=log_id)
        if not success:
            return False

    if 'prometheus' in params and 'operator' not in params:
        success = prometheus_disable.run(params['crd'], log_id=log_id)
        if not success:
            return False

    if 'operator' in params:
        success = operator_delete.run(params['operator'], log_id=log_id)
        if not success:
            return False

    return True