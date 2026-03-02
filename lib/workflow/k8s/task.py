from lib import filter_helper
from lib.workflow.k8s import lb_ip_pool_create
from lib.workflow.k8s import pod_create
from lib.workflow.k8s import service_create
from lib.workflow.k8s import lb_ip_pool_delete
from lib.workflow.k8s import pod_delete
from lib.workflow.k8s import service_delete


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task_id = filter_helper.get(task, '__id__')
    namespace = filter_helper.get(task, 'namespace')

    if 'items' in task:
        if not isinstance(task['items'], list):
            return None, 'k8s.items list required'

        for item in task['items']:
            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item['__id__'] = task_id
            if namespace is not None and 'namespace' not in item:
                item['namespace'] = namespace

            item_type = filter_helper.get(item, '__type__')
            error = 'Unsupported type: %s' % (item_type)

            if item_type == 'lb-ip-pool':
                item, error = lb_ip_pool_create.validate(item)
                if error is not None:
                    return None, error
        
            if item_type == 'pod':
                item, error = pod_create.validate(item)
                if error is not None:
                    return None, error
        
            if item_type == 'service':
                item, error = service_create.validate(item)
                if error is not None:
                    return None, error
        
            if error is not None:
                return None, error
            
    new_task = {}
    allowed_keys = [
        '__id__',
        'items'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for k8s task'
    
    return new_task, None


def run(params, log_id=None):
    if 'items' in params:
        for item in params['items']:
            item_type = filter_helper.get(item, '__type__')

            if item_type == 'lb-ip-pool':
                success = lb_ip_pool_create.run(item, log_id=log_id)
                if not success:
                    return False
        
            if item_type == 'pod':
                success = pod_create.run(item, log_id=log_id)
                if not success:
                    return False
        
            if item_type == 'service':
                success = service_create.run(item, log_id=log_id)
                if not success:
                    return False
                
    return True


def validate_delete(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task_id = filter_helper.get(task, '__id__')
    namespace = filter_helper.get(task, 'namespace')

    if 'items' in task:
        if not isinstance(task['items'], list):
            return None, 'k8s.items list required'

        for item in task['items']:
            item['cluster'] = cluster_name
            item['confirmation'] = confirmation
            item['base_directory'] = cluster_settings['directory']
            item['__id__'] = task_id
            if namespace is not None and 'namespace' not in item:
                item['namespace'] = namespace

            item_type = filter_helper.get(item, '__type__')
            error = 'Unsupported type: %s' % (item_type)

            if item_type == 'lb-ip-pool':
                item, error = lb_ip_pool_delete.validate(item)
                if error is not None:
                    return None, error
        
            if item_type == 'pod':
                item, error = pod_delete.validate(item)
                if error is not None:
                    return None, error
        
            if item_type == 'service':
                item, error = service_delete.validate(item)
                if error is not None:
                    return None, error
        
            if error is not None:
                return None, error
    
    new_task = {}
    allowed_keys = [
        '__id__',
        'items'
    ]
    for key in task:
        if key in allowed_keys:
            new_task[key] = task[key]

    if len(new_task) == 0:
        return None, 'No valid parameters defined for k8s task'
    
    return new_task, None


def delete(params, log_id=None):
    if 'items' in params:
        for item in params['items']:
            item_type = filter_helper.get(item, '__type__')

            if item_type == 'lb-ip-pool':
                success = lb_ip_pool_delete.run(item, log_id=log_id)
                if not success:
                    return False

            if item_type == 'pod':
                success = pod_delete.run(item, log_id=log_id)
                if not success:
                    return False
        
            if item_type == 'service':
                success = service_delete.run(item, log_id=log_id)
                if not success:
                    return False

    return True