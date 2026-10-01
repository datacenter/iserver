import copy
import time
import importlib
import json
from lib import log_helper
from lib import filter_helper
from lib import ip_helper
from lib import output_helper
from lib.workflow.task import common


def validate(tasks):
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
            rules = getattr(fmodule, 'get_rules')()

            for supported_task_name in rules['create']:
                if supported_task_name in task[task_name]:
                    task_module = importlib.import_module(
                        'lib.workflow.%s.%s' % (
                            fmap[task_name], 
                            rules['create'][supported_task_name]
                        )
                    )

                    task_params = copy.deepcopy(task[task_name][supported_task_name])
                    if isinstance(task_params, list):
                        for itask_param in task_params:
                            if '__cluster__' in task[task_name]:
                                itask_param['cluster'] = task[task_name]['__cluster__']

                            itask_param['confirmation'] = filter_helper.get(task[task_name], '__confirmation__', on_error=True, on_none=True)
                            itask_param['__break_on_error__'] = filter_helper.get(task[task_name], '__break_on_error__', on_error=True, on_none=True)
                            itask_param['base_directory'] = filter_helper.get(task[task_name], '__directory__')

                            task_def = {}
                            task_def[task_name] = {}
                            task_def[task_name][supported_task_name], error = getattr(task_module, 'validate')(
                                itask_param
                            )                            
                            if error is not None:
                                return None, error

                            new_tasks.append(
                                task_def
                            )

                    if isinstance(task_params, dict):
                        if '__cluster__' in task[task_name]:
                            task_params['cluster'] = task[task_name]['__cluster__']

                        task_params['confirmation'] = filter_helper.get(task[task_name], '__confirmation__', on_error=True, on_none=True)
                        task_params['__break_on_error__'] = filter_helper.get(task[task_name], '__break_on_error__', on_error=True, on_none=True)
                        task_params['base_directory'] = filter_helper.get(task[task_name], '__directory__')

                        task_def = {}
                        task_def[task_name] = {}
                        task_def[task_name][supported_task_name], error = getattr(task_module, 'validate')(
                            task_params
                        )                            
                        if error is not None:
                            return None, error

                        new_tasks.append(
                            task_def
                        )

    return new_tasks, None


def run(tasks, validate_only=False, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    log_handler = log_helper.Log(log_id=log_id)
    resolved_tasks, error = validate(
        tasks
    )
    if resolved_tasks is None:
        my_output.error(error)    
        return False
    
    if validate_only:
        my_output.default(json.dumps(resolved_tasks, indent=4))
        return True

    success = True
    results = []

    fmap = common.get_task_map()
    for task in resolved_tasks:
        for task_name in task:
            if task_name not in fmap:
                return None, 'Unsupported task: %s' % (task_name)

            if not filter_helper.get(task[task_name], '__enabled__', on_error=True, on_none=True):
                continue

            if filter_helper.get(task[task_name], '__no_create__', on_error=False, on_none=False):
                continue

            fmodule = importlib.import_module('lib.workflow.%s.task' % (fmap[task_name]))
            rules = getattr(fmodule, 'get_rules')()

            for supported_task_name in rules['create']:
                if supported_task_name in task[task_name]:
                    task_module = importlib.import_module(
                        'lib.workflow.%s.%s' % (
                            fmap[task_name], 
                            rules['create'][supported_task_name]
                        )
                    )

                    result = {}
                    result['__Output'] = {}
                    result['target'] = common.get_task_target(task[task_name][supported_task_name])
                    result['task'] = task_name
                    result['oper'] = 'create %s' % (supported_task_name)
                    result['workflow_id'] = ip_helper.get_short_uuid()

                    start_time = int(time.time())
                    task[task_name][supported_task_name]['__workflow_id__'] = result['workflow_id']
                    task_success = getattr(task_module, 'run')(
                        task[task_name][supported_task_name],
                        log_id=log_id
                    )

                    result['changes'] = log_handler.get_log('workflow_%s' % (result['workflow_id']))
                    result['success'] = task_success
                    if result['success']:
                        result['successTick'] = '\u2713'
                        result['__Output']['successTick'] = 'Green'
                    else:
                        result['successTick'] = '\u2717'
                        result['__Output']['successTick'] = 'Red'

                    result['duration'] = int(time.time()) - start_time
                    results.append(result)

                    if task[task_name][supported_task_name]['__break_on_error__'] and not task_success:
                        return False
                    
                    success = success and task_success

    my_output.my_table_ng(
        results,
        [
            ['Target', 'target'],
            ['Scope', 'task'],
            ['Workflow', 'oper'],
            ['Changes', 'changes'],
            ['Success', 'successTick'],
            ['Duration [s]', 'duration']
        ]
    )
    return success