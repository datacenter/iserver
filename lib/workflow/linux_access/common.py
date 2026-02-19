from lib import ssh
from lib.linux import main as linux


def get_default_params():
    params = {}
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def get_ssh_handlers(items, log_id, my_output=None, check=False, add_linux=False):
    if my_output is not None:
        my_output.default('Check ssh access', underline=True)

    success = True

    for item in items:
        item['ssh_handler'] = ssh.Ssh(
            item['address'], 
            item['username'], 
            password=item['password'],
            key_filename=item['key_filename'], 
            log_id=log_id
        )

        if add_linux:
            item['linux_handler'] = linux.Linux(
                item['address'],
                item['username'],
                password=item['password'],
                key_filename=item['key_filename'],
                server_name=item['name'],
                no_cache=True,
                log_id=log_id
            )

        if not check:
            if my_output is not None:
                my_output.default('- %s' % (item['name']))
            
            continue

        ssh_success = item['ssh_handler'].is_ssh()
        if ssh_success:
            if my_output is not None:
                my_output.default('- %s: %s' % (item['name'], my_output.add_color('ok', 'Green')))
            
            continue

        success = False
        if my_output is not None:
            my_output.default('- %s: %s' % (item['name'], my_output.add_color('nok', 'Red')))

    return success, items
