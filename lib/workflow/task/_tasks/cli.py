from lib.workflow.ocp_bm_install.tasks import bashrc
from lib.workflow.ocp_bm_install.tasks import cilium
from lib.workflow.ocp_bm_install.tasks import helm
from lib.workflow.ocp_bm_install.tasks import hubble
from lib.workflow.ocp_bm_install.tasks import tridentctl
from lib.workflow.ocp_bm_install.tasks import virtctl


def verify(task, user_settings):
    if 'exec' not in task:
        task['exec'] = []

    for item in task['exec']:
        if not isinstance(item, str):
            return None, 'exec command must be string'

    for item in ['bashrc', 'cilium', 'helm', 'hubble', 'tridentctl', 'virtctl']:
        if item not in task:
            task[item] = {}
            task[item]['enabled'] = False

        if isinstance(task[item], bool):
            enabled = task[item]
            task[item] = {}
            task[item]['enabled'] = enabled

        if isinstance(task[item], dict):
            if 'enabled' not in task[item]:
                task[item]['enabled'] = True

    task['tridentctl'], error = tridentctl.verify(task['tridentctl'])
    if error is not None:
        return None, error

    task['cilium'], error = cilium.verify(task['cilium'], user_settings)
    if error is not None:
        return None, error

    task['hubble'], error = hubble.verify(task['hubble'], user_settings)
    if error is not None:
        return None, error

    task['helm'], error = helm.verify(task['helm'])
    if error is not None:
        return None, error

    task['virtctl'], error = virtctl.verify(task['virtctl'], user_settings)
    if error is not None:
        return None, error

    if task['virtctl']['enabled']:
        task['bashrc']['enabled'] = True

    task['bashrc'], error = bashrc.verify(task['bashrc'], user_settings)
    if error is not None:
        return None, error

    return task, None


def run(task, user_settings, my_output, ssh_handler, log_id):
    if 'exec' in task:
        for command in task['exec']:
            my_output.default('Run command: %s' % command, before_newline=True, underline=True)
            success, output, error = ssh_handler.run_cmd(command)
            if not success:
                my_output.error('Failed')
                my_output.error(error)

                if task['break-on-error']:
                    return False
            else:
                my_output.default(output)

    if 'bashrc' in task:
        bashrc.run(task['bashrc'], user_settings, my_output, ssh_handler, log_id)

    if 'cilium' in task:
        cilium.run(task['cilium'], user_settings, my_output, log_id)

    if 'hubble' in task:
        hubble.run(task['hubble'], user_settings, my_output, log_id)

    if 'helm' in task:
        helm.run(task['helm'], user_settings, my_output, log_id)

    if 'virtctl' in task:
        virtctl.run(task['virtctl'], user_settings, my_output, log_id)

    return True
