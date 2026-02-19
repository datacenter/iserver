from lib.workflow.ocp_bashrc_proxy import task as task_bashrc
from lib.workflow.ocp_cilium_cli import task as task_cilium_cli
from lib.workflow.ocp_helm_cli import task as task_helm_cli
from lib.workflow.ocp_hubble_cli import task as task_hubble_cli
from lib.workflow.ocp_tridentctl_cli import task as task_tridentctl_cli
from lib.workflow.ocp_virtctl_cli import task as task_virtctl_cli
from lib.workflow.ocp_web_terminal_operator import task as task_web_terminal
from lib.workflow.ocp_cli import task_apply
from lib.workflow.ocp_cli import install

def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name

    if 'exec' not in task:
        task['exec'] = []

    for item in task['exec']:
        if not isinstance(item, str):
            return None, 'exec command must be string'

    for item in ['bashrc', 'cilium', 'helm', 'hubble', 'tridentctl', 'virtctl', 'web', 'file']:
        if item not in task:
            continue

        if isinstance(task[item], bool):
            enabled = task[item]
            task[item] = {}
            task[item]['enabled'] = enabled

        if isinstance(task[item], dict):
            if 'enabled' not in task[item]:
                task[item]['enabled'] = True

    if 'virtctl' in task and 'bashrc' not in task:
        task['bashrc'] = dict(enabled=True)

    if 'bashrc' in task:
        task['bashrc'], error = task_bashrc.validate_create(
            task['bashrc'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'cilium' in task:
        task['cilium'], error = task_cilium_cli.validate_create(
            task['cilium'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'helm' in task:
        task['helm'], error = task_helm_cli.validate_create(
            task['helm'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'hubble' in task:
        task['hubble'], error = task_hubble_cli.validate_create(
            task['hubble'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error
        
    if 'tridentctl' in task:
        task['tridentctl'], error = task_tridentctl_cli.validate_create(
            task['tridentctl'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'virtctl' in task:
        task['virtctl'], error = task_virtctl_cli.validate_create(
            task['virtctl'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'web' in task:
        task['web'], error = task_web_terminal.validate_create(
            task['web'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error

    if 'file' in task:
        task['file'], error = task_apply.validate_create(
            task['file'], 
            cluster_name,
            confirmation,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler
        )
        if error is not None:
            return None, error
                    
    return task, None

def run(params, log_id=None):
    return install.run(params, log_id=log_id)
