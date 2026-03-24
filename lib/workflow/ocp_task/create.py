import importlib
import json
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_task import common


def validate(tasks, cluster_name, cluster_settings=None, k8s_handler=None, confirmation=True):
    if not isinstance(tasks, list):
        return None, 'tasks list required'
    
    for task in tasks:
        if not isinstance(task, dict):
            return None, 'tasks list of dict required'

    fmap = common.get_task_map()
    new_tasks = []
    for task in tasks:
        for task_name in task:
            if task_name not in fmap:
                return None, 'Unsupported task: %s' % (task_name)

            if not filter_helper.get(task[task_name], '__enabled__', on_error=True, on_none=True):
                continue

            if filter_helper.get(task[task_name], '__no_create__', on_error=False, on_none=False):
                continue

            fmodule = importlib.import_module('lib.workflow.%s.task' % (fmap[task_name]))
            task_def = {}
            task_def[task_name], error = getattr(fmodule, 'validate_create')(
                    task[task_name],
                    cluster_name,
                    confirmation,
                    cluster_settings=cluster_settings,
                    k8s_handler=k8s_handler
            )                            
            if error is not None:
                return None, error

            new_tasks.append(
                task_def
            )

    return new_tasks, None


def run(tasks, cluster_name, confirmation=True, cluster_settings=None, k8s_handler=None, validate_only=False, break_on_error=True, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    resolved_tasks, error = validate(
        tasks,
        cluster_name,
        cluster_settings=cluster_settings,
        k8s_handler=k8s_handler,
        confirmation=confirmation
    )
    if resolved_tasks is None:
        my_output.error(error)    
        return False
    
    if validate_only:
        my_output.default(json.dumps(resolved_tasks, indent=4))
        return True

    success = True
    fmap = common.get_task_map()
    for task in tasks:
        for task_name in task:
            if task_name not in fmap:
                return None, 'Unsupported task: %s' % (task_name)

            if not filter_helper.get(task[task_name], '__enabled__', on_error=True, on_none=True):
                continue

            if filter_helper.get(task[task_name], '__no_create__', on_error=False, on_none=False):
                continue

            fmodule = importlib.import_module('lib.workflow.%s.task' % (fmap[task_name]))
            task_success = getattr(fmodule, 'run')(
                task[task_name],
                log_id=log_id
            )
            if not task_success and break_on_error:
                return False
            
            success = success and task_success

    return success