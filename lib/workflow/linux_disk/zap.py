import copy
from lib import output_helper
from lib.workflow.linux_disk import common as local_common
from lib.workflow.linux_access import common as linux_common
from lib.linux import output as linux_output
from menu.common import get_confirmation


def validate(params):
    if 'server' not in params or params['server'] is None:
        return None, 'server list required'

    if not isinstance(params['server'], list):
        return None, 'server list required'
    
    if len(params['server']) == 0:
        return None, 'define at least one server'
    
    if 'device' not in params or params['device'] is None:
        params['device'] = []

    if not isinstance(params['device'], list):
        return None, 'device list required'
    
    new_devices = []
    for item in params['device']:
        if item.startswith('/dev/'):
            new_devices.append(item)
            continue

        item = '/dev/%s' % (item)
        new_devices.append(item)

    params['device'] = copy.deepcopy(new_devices)

    if 'break' not in params:
        params['break'] = True

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    allowed_keys = [
        'server',
        'device',
        'verbose',
        'break',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Linux - Disk - Zap', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False
    
    success, servers = linux_common.get_ssh_handlers(
        params['server'],
        log_id,
        my_output=my_output,
        check=True,
        add_linux=True
    )
    if not success:
        return False
    
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    for server in servers:
        my_output.default('Server: %s' % (server['name']), before_newline=True, underline=True)
        lsblks = server['linux_handler'].get_lsblks(
            device_names=params['device'],
            include_disk_paths=True,
            exclude_boot=True,
            cache_enabled=False
        )
        if lsblks is None:
            my_output.error('Failed to get lsblk')
            return False
        
        if len(lsblks) == 0:
            my_output.error('No matching device found')
            return False
        
        linux_output_handler.print_linux_lsblk(lsblks)

        if params['confirmation']:
            if not get_confirmation():
                return False
            
        for device in lsblks:
            my_output.default('Zap device: %s' % (device['path']), before_newline=True)

            command = 'sudo sgdisk --zap-all %s' % (device['path'])
            my_output.default('Command: %s' % (command))
            success, output, error = server['ssh_handler'].run_cmd(command)
            my_output.default('%s %s' % (str(output), str(error)), wrap='~~~')
            if not success:
                if 'Invalid partition data!' in str(output) or 'Invalid partition data!' in str(error):
                    command = 'sudo sgdisk --zap-all %s' % (device['path'])
                    my_output.default('Command: %s' % (command))
                    success, output, error = server['ssh_handler'].run_cmd(command)
                    my_output.default('%s %s' % (str(output), str(error)), wrap='~~~')
                    if not success:
                        my_output.error('Failed')
                        if params['break']:
                            return False
                else:
                    my_output.error('Failed')
                    if params['break']:
                        return False
            
            command = 'sudo blkdiscard -f  %s' % (device['path'])
            my_output.default('Command: %s' % (command))
            success, output, error = server['ssh_handler'].run_cmd(command)
            my_output.default('%s %s' % (str(output), str(error)), wrap='~~~')
            if not success:
                my_output.error('Failed')
                if params['break']:
                    return False

        lsblks = server['linux_handler'].get_lsblks(
            device_names=params['device'],
            include_disk_paths=True,
            exclude_boot=True,
            cache_enabled=False
        )
        if lsblks is None:
            my_output.error('Failed to get lsblk')
            return False
        
        if len(lsblks) == 0:
            my_output.error('No matching device found')
            return False
        
        linux_output_handler.print_linux_lsblk(lsblks)

    return True
