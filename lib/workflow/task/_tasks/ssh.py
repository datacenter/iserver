import os
import json
from lib import file_helper
from lib.workflow.ocp_ssh import main as ocp_ssh


def verify(task, directory):
    local_keys = []
    ssh_directory = os.path.join(directory, 'ssh')
    if os.path.isdir(ssh_directory):
        for file_basename in os.listdir(ssh_directory):
            filename = os.path.join(
                ssh_directory,
                file_basename
            )
            content = file_helper.get_file_text(filename)
            if content is None:
                return None, 'ssh key read failed: %s' % (filename)

            local_keys.append(
                content.strip().split('\n')[0]
            )

    if 'keys' not in task and len(local_keys) == 0:
        return None, 'ssh task requires keys list'

    if 'keys' not in task:
        task['keys'] = []

    for key in local_keys:
        task['keys'].append(key)

    if len(task['keys']) == 0:
        return None, 'ssh task requires keys list'

    for item in task['keys']:
        if not isinstance(item, str):
            return None, 'ssh task requires keys list'

    return task, None


def run(task, user_settings, my_output, log_id):
    my_output.default('Task ssh', before_newline=True, underline=True)
    if user_settings['connector'] is None:
        my_output.error('Connector required')
        if task['break-on-error']:
            return False
    else:
        params = {}
        params['cluster'] = user_settings['connector']
        params['keys'] = task['keys']
        my_output.default(json.dumps(params, indent=4))
        success = ocp_ssh.run(
            params,
            log_id=log_id
        )
        if not success and task['break-on-error']:
            return False

    return True
