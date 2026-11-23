import copy
from lib import output_helper
from lib.workflow.linux_disk import common as local_common
from lib.workflow.linux_access import common as linux_common
from lib.linux import output as linux_output
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['server', True, None, 'list-of-dict', 1, None, None, None],
        ['device', False, [], 'list-of-str', None, None, None, None],
        ['fstype', False, [], 'list-of-str', None, None, ['LVM2', 'Ceph'], None],
        ['break', True, True, 'bool', None, None, None, None],
        ['break-blkdiscard', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Linux - Disk - Zap', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    new_devices = []
    for item in params['device']:
        if item.startswith('/dev/'):
            new_devices.append(item)
            continue

        item = '/dev/%s' % (item)
        new_devices.append(item)

    params['device'] = copy.deepcopy(new_devices)

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
            fstypes=params['fstype'],
            include_disk_paths=True,
            exclude_boot=True,
            cache_enabled=False
        )
        if lsblks is None:
            my_output.error('Failed to get lsblk')
            continue
        
        if len(lsblks) == 0:
            my_output.default('No matching device found')
            continue
        
        linux_output_handler.print_linux_lsblk(lsblks)

        if params['confirmation']:
            if not get_confirmation():
                continue
        
        zapped = []
        for device in lsblks:
            if device['path'] in ['/dev/loop0']:
                continue
            
            my_output.default('Zap device: %s' % (device['path']), before_newline=True)
            zapped.append(device['path'])

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
            
            if device['trim']:
                command = 'sudo blkdiscard -f  %s' % (device['path'])
                my_output.default('Command: %s' % (command))
                success, output, error = server['ssh_handler'].run_cmd(command)
                my_output.default('%s %s' % (str(output), str(error)), wrap='~~~')
                if not success:
                    if params['break-blkdiscard']:
                        my_output.error('Failed')
                        return False
                    
                    my_output.default('Continue')

        lsblks = server['linux_handler'].get_lsblks(
            device_names=zapped,
            include_disk_paths=True,
            exclude_boot=True,
            cache_enabled=False
        )
        if lsblks is None:
            my_output.error('Failed to get lsblk')
            continue
        
        if len(lsblks) == 0:
            my_output.error('No matching device found')
            continue
        
        linux_output_handler.print_linux_lsblk(lsblks)

    return True