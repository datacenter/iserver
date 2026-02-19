from lib import output_helper
from lib import ssh
from lib.linux import main as linux
from lib.linux import settings
from lib.workflow.linux_access import common as local_common


def validate(params):
    if 'server' not in params or params['server'] is None:
        return None, 'Server name required'

    if 'ssh-handler' not in params:
        params['ssh-handler'] = False

    if 'linux-handler' not in params:
        params['linux-handler'] = False

    if 'verbose' not in params:
        params['verbose'] = False

    allowed_keys = [
        'server',
        'ssh-handler',
        'linux-handler',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        return None, error

    settings_handler = settings.LinuxSettings(log_id=log_id)

    server = settings_handler.get_linux_server(params['server'], strict_match=True)
    if server is None:
        return None, 'Server not found: %s' % (params['server'])
    
    if params['verbose']:
        my_output.default('Linux Server', before_newline=True, underline=True)
        my_output.default('- ip: %s' % (server['address']))
        my_output.default('- username: %s' % (server['username']))

    params['data'] = {}
    params['data']['ssh_handler'] = ssh.Ssh(
        server['address'], 
        server['username'], 
        password=server['password'],
        key_filename=server['key'], 
        log_id=log_id
    )
    if not params['data']['ssh_handler'].is_ssh():
        if params['verbose']:
            my_output.default('- ssh: %s' % (my_output.add_color('nok', 'Red')))
        return None, 'Server access failed: %s@%s' % (server['username'], server['address'])

    if params['verbose']:
        my_output.default('- ssh: %s' % (my_output.add_color('ok', 'Green')))

    if params['linux-handler']:
        params['data']['linux_handler'] = linux.Linux(
            server['address'],
            server['username'],
            password=server['password'],
            key_filename=server['key'],
            server_name=server['name'],
            no_cache=True
        )

    return params, None
