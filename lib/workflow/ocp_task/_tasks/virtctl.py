import json
from lib.workflow.ocp_virtctl_cli import main as virtctl


def run(task, user_settings, my_output, log_id):
    if not task['enabled']:
        return True

    my_output.default('Task cli virtctl', before_newline=True, underline=True)
    my_output.default(json.dumps(task, indent=4))

    params = {}
    params['cluster'] = user_settings['connector']
    params['url'] = task['download_url']

    success = virtctl.run(
        params,
        log_id=log_id
    )
    return success
