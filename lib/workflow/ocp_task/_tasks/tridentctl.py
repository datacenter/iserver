import json
from lib.workflow.ocp_tridentctl_cli import main as tridentctl


def run(task, user_settings, my_output, log_id):
    if not task['enabled']:
        return True

    my_output.default('Task cli tridentctl', before_newline=True, underline=True)
    my_output.default(json.dumps(task, indent=4))

    params = {}
    params['cluster'] = user_settings['connector']
    params['url'] = task['download_url']
    params['version'] = None
    if 'version' in task:
        params['version'] = task['version']

    success = tridentctl.run(
        params,
        log_id=log_id
    )

    return success
