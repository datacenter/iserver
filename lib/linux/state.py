import time
import json
import re
import traceback

from progress.bar import IncrementalBar


class LinuxState():
    def __init__(self):
        pass

    def convert_pct(self, pct):
        try:
            value = '%s%%' % (round(pct, 2))
        except BaseException:
            self.log.error('iwe_cluster_info.convert_cpu_capacity', pct)
            return None
        return value

    def convert_memory(self, value):
        try:
            unit = ['KiB', 'MiB', 'GiB', 'TiB']
            for index in range(0, 4):
                value = value / 1024
                if value < 1000:
                    break

            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

        except BaseException:
            self.my_output.traceback(traceback.format_exc())
            return None

        return value

    def convert_storage(self, value):
        try:
            unit = ['KB', 'MB', 'GB', 'TB']
            for index in range(0, 4):
                value = value / 1000
                if value < 1000:
                    break

            value = '%s [%s]' % (
                round(value, 2),
                unit[index]
            )

        except BaseException:
            self.log.error('iwe_cluster_info.convert_storage', value)
            return None

        return value

    def get_cpu_load(self, output):
        try:
            load = {}
            for line in output.split('\n'):
                if 'load average:' in line:
                    value = line.split('load average:')[1]
                    if ',' in value:
                        load_list = value.split(',')
                    else:
                        load_list = value.split(' ')

                    load['cpu_load_1min'] = float(load_list[0].strip())
                    load['cpu_load_5min'] = float(load_list[1].strip())
                    load['cpu_load_15min'] = float(load_list[2].strip())

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return load

    def get_memory_utilization(self, output):
        try:
            memory_utilization = {}
            for line in output.split('\n'):
                line = line.rstrip('\n')
                if line.startswith('Mem:'):
                    values = line.split('Mem:')[1].strip()
                    mem_string = re.sub(' +', ' ', values).split(' ')
                    memory_utilization['memory_total'] = int(mem_string[0])
                    memory_utilization['memory_total_unit'] = self.convert_memory(
                        memory_utilization['memory_total']
                    )
                    memory_utilization['memory_used'] = int(mem_string[1])
                    memory_utilization['memory_used_unit'] = self.convert_memory(
                        memory_utilization['memory_used']
                    )
                    memory_utilization['memory_free'] = int(mem_string[2])
                    memory_utilization['memory_free_unit'] = self.convert_memory(
                        memory_utilization['memory_free']
                    )
                    memory_utilization['memory_shared'] = int(mem_string[3])
                    memory_utilization['memory_shared_unit'] = self.convert_memory(
                        memory_utilization['memory_shared']
                    )
                    memory_utilization['memory_cache'] = int(mem_string[4])
                    memory_utilization['memory_cache_unit'] = self.convert_memory(
                        memory_utilization['memory_cache']
                    )
                    memory_utilization['memory_available'] = int(mem_string[5])
                    memory_utilization['memory_available_unit'] = self.convert_memory(
                        memory_utilization['memory_available']
                    )
                    memory_utilization['memory_used_pct'] = int(memory_utilization['memory_used'] * 100 / memory_utilization['memory_total'])
                    memory_utilization['memory_used_pct_unit'] = self.convert_pct(
                        memory_utilization['memory_used_pct']
                    )

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return memory_utilization

    def get_disk_utilization(self, output):
        try:
            disk_info = {}
            disk_info['disk_count'] = 0
            disk_info['disk_total_capacity'] = 0
            disk_info['disk_total_used'] = 0
            disk_info['disk_max_used_pct'] = 0
            for line in output.split('\n'):
                if line.startswith('/dev/'):
                    disk_info['disk_count'] = disk_info['disk_count'] + 1
                    values = re.sub(' +', ' ', line).split(' ')
                    disk_info['disk_total_capacity'] = disk_info['disk_total_capacity'] + int(values[1]) * 1024
                    disk_info['disk_total_used'] = disk_info['disk_total_used'] + int(values[2]) * 1024
                    disk_info['disk_max_used_pct'] = max(
                        disk_info['disk_max_used_pct'],
                        int(int(values[2]) * 100 / int(values[1]))
                    )

            disk_info['disk_total_used_pct'] = int(disk_info['disk_total_used'] * 100 / disk_info['disk_total_capacity'])
            disk_info['disk_total_used_pct_unit'] = self.convert_pct(disk_info['disk_total_used_pct'])
            disk_info['disk_total_capacity_unit'] = self.convert_storage(disk_info['disk_total_capacity'])
            disk_info['disk_total_used_unit'] = self.convert_storage(disk_info['disk_total_used'])
            disk_info['disk_max_used_pct_unit'] = self.convert_pct(disk_info['disk_max_used_pct'])

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return disk_info

    def get_cpu_info(self, output):
        try:
            # Architecture:          x86_64
            # CPU op-mode(s):        32-bit, 64-bit
            # Byte Order:            Little Endian
            # CPU(s):                28
            # On-line CPU(s) list:   0-27
            # Thread(s) per core:    1
            # Core(s) per socket:    14
            # Socket(s):             2
            # NUMA node(s):          2
            # Vendor ID:             GenuineIntel
            # CPU family:            6
            # Model:                 79
            # Model name:            Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
            # Stepping:              1
            # CPU MHz:               2600.158
            # CPU max MHz:           2600.0000
            # CPU min MHz:           1200.0000
            # BogoMIPS:              5187.67
            # Virtualization:        VT-x
            # L1d cache:             32K
            # L1i cache:             32K
            # L2 cache:              256K
            # L3 cache:              35840K
            # NUMA node0 CPU(s):     0-13
            # NUMA node1 CPU(s):     14-27
            info = {}
            info['numa_count'] = None
            info['numa_nodes'] = []
            for line in output.split('\n'):
                if line.startswith('Model name:'):
                    line = re.sub(' +', ' ', line)
                    info['cpu_model'] = line.split('Model name:')[1].strip()
                if line.startswith('CPU(s):'):
                    line = re.sub(' +', ' ', line)
                    info['cpu_count'] = int(line.split('CPU(s):')[1])
                if line.startswith('Core(s) per socket:'):
                    line = re.sub(' +', ' ', line)
                    info['cpu_per_socket'] = int(line.split('Core(s) per socket:')[1])
                if line.startswith('Socket(s):'):
                    line = re.sub(' +', ' ', line)
                    info['socket_count'] = int(line.split('Socket(s):')[1])
                if line.startswith('NUMA node(s):'):
                    line = re.sub(' +', ' ', line)
                    info['numa_count'] = int(line.split('NUMA node(s):')[1])
                if line.startswith('Thread(s) per core:'):
                    line = re.sub(' +', ' ', line)
                    info['threads_count'] = int(line.split('Thread(s) per core:')[1])

            info['hyperthreading'] = False
            if info['cpu_per_socket'] * info['socket_count'] < info['cpu_count']:
                info['hyperthreading'] = True

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return info

    def is_hypervisor(self, output):
        try:
            hypervisor = False
            for line in output.split('\n'):
                if line.startswith('Hypervisor vendor:'):
                    hypervisor = True

                if line.startswith('Flags:'):
                    if 'hypervisor' in line:
                        hypervisor = True

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return hypervisor

    def get_release_info(self, output):
        try:
            # NAME="Ubuntu"
            # VERSION="18.04.4 LTS (Bionic Beaver)"
            # ID=ubuntu
            # ID_LIKE=debian
            # PRETTY_NAME="Ubuntu 18.04.4 LTS"
            # VERSION_ID="18.04"
            # HOME_URL="https://www.ubuntu.com/"
            # SUPPORT_URL="https://help.ubuntu.com/"
            # BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
            # PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
            # VERSION_CODENAME=bionic
            # UBUNTU_CODENAME=bionic
            info = {}
            for line in output.split('\n'):
                if line.startswith('NAME='):
                    line = re.sub(' +', ' ', line)
                    info['release_name'] = line.split('=')[1].strip('"')
                if line.startswith('VERSION='):
                    line = re.sub(' +', ' ', line)
                    info['release_version'] = line.split('=')[1].strip('"')

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return info

    def get_uptime(self, output):
        try:
            # cat /proc/uptime
            # 3864040.37 102139784.03
            epoch = round(float(output.split(' ')[0]))
            days = 0
            while True:
                if epoch < 24 * 60 * 60:
                    break

                epoch = epoch - 24 * 60 * 60
                days = days + 1

            if days == 0:
                uptime = time.strftime('%H:%M:%S', time.gmtime(epoch))
            else:
                uptime = '%s (%s days)' % (time.strftime('%H:%M:%S', time.gmtime(epoch)), days)

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return uptime

    def get_state_commands(self, settings):
        commands = []
        commands.append('cat /etc/hostname')
        commands.append('cat /proc/uptime')
        commands.append('cat /etc/os-release')

        if settings['cpu']:
            commands.append('uptime')
            commands.append('lscpu')

        if settings['memory']:
            commands.append('free -b')

        if settings['disk']:
            commands.append('df -k')

        return commands

    def get_state(self, settings, progress_bar=False):
        try:
            commands = self.get_state_commands(settings)
            outputs = self.run_commands(commands, progress_bar=progress_bar)
            if outputs is None:
                self.my_output.error('Commands output collection failed')
                return None

            state = {}
            state['management_ip'] = self.management_ip
            state['ssh_username'] = self.username
            state['ssh_password'] = self.password

            state['hostname'] = outputs['cat /etc/hostname'].rstrip('\n')
            state['uptime'] = self.get_uptime(outputs['cat /proc/uptime'])
            release_info = self.get_release_info(outputs['cat /etc/os-release'])
            if release_info is not None:
                for key in release_info:
                    state[key] = release_info[key]

            if settings['cpu']:
                cpu_load = self.get_cpu_load(outputs['uptime'])
                if cpu_load is not None:
                    for key in cpu_load:
                        state[key] = cpu_load[key]

                cpu_info = self.get_cpu_info(outputs['lscpu'])
                if cpu_info is not None:
                    for key in cpu_info:
                        state[key] = cpu_info[key]

                state['hypervisor'] = self.is_hypervisor(outputs['lscpu'])

            if settings['memory']:
                memory_info = self.get_memory_utilization(outputs['free -b'])
                if memory_info is not None:
                    for key in memory_info:
                        state[key] = memory_info[key]

            if settings['disk']:
                disk_info = self.get_disk_utilization(outputs['df -k'])
                if disk_info is not None:
                    for key in disk_info:
                        state[key] = disk_info[key]

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return state

    def print_state(self, state):
        self.my_output.dictionary(
            state,
            title='Linux State Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=[
                'management_ip',
                'ssh_username',
                'ssh_password',
                'hostname',
                'uptime',
                'release_name',
                'release_version',
                'cpu_count',
                'hyperthreading',
                'cpu_load_1min',
                'memory_total_unit',
                'memory_used_pct_unit',
                'disk_total_capacity_unit',
                'disk_total_used_pct_unit',
                'disk_max_used_pct_unit'
            ],
            title_keys=[
                'IP Address',
                'Username',
                'Password',
                'Hostname',
                'Uptime',
                'Release name',
                'Release version',
                'CPU count',
                'Hyperthreading',
                'CPU load (1 minute)',
                'Memory',
                'Memory usage',
                'Disk total capacity',
                'Disk total usage',
                'Max disk usage'
            ]
        )
