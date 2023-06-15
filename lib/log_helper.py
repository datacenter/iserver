import datetime
import os
import time
import json
import shutil

from lib import output_helper
from lib import ssh


class Log():
    def __init__(self, log_id=None):
        self.logs_directory = '/tmp/iserver'
        if log_id is not None:
            self.logs_directory = os.path.join(self.logs_directory, log_id)
        self.log_id = log_id

        self.command_filename = os.path.join(self.logs_directory, 'command')
        self.error_filename = os.path.join(self.logs_directory, 'iserver.error')
        self.info_filename = os.path.join(self.logs_directory, 'iserver.info')
        self.debug_filename = os.path.join(self.logs_directory, 'iserver.debug')
        self.isctl_filename = os.path.join(self.logs_directory, 'isctl.debug')
        self.api_filename = os.path.join(self.logs_directory, 'api.debug')
        self.redfish_filename = os.path.join(self.logs_directory, 'redfish.debug')
        self.odata_filename = os.path.join(self.logs_directory, 'odata.debug')
        self.ucsm_filename = os.path.join(self.logs_directory, 'ucsm.debug')
        self.k8s_filename = os.path.join(self.logs_directory, 'k8s.debug')
        self.ocapi_filename = os.path.join(self.logs_directory, 'ocapi.debug')
        self.ocp_filename = os.path.join(self.logs_directory, 'ocp.debug')
        self.kubevirt_filename = os.path.join(self.logs_directory, 'kubevirt.debug')
        self.vcenter_filename = os.path.join(self.logs_directory, 'vcenter.debug')
        self.nexus_filename = os.path.join(self.logs_directory, 'nexus.debug')
        self.apic_filename = os.path.join(self.logs_directory, 'apic.debug')
        self.iwo_filename = os.path.join(self.logs_directory, 'iwo.debug')
        self.ssh_filename = os.path.join(self.logs_directory, 'ssh.debug')
        self.devel_filename = os.path.join(self.logs_directory, 'devel.debug')
        self.lcm_report_filename = os.path.join(self.logs_directory, 'lcm.report')
        self.cache_filename = os.path.join(self.logs_directory, 'cache')
        self.trace_filename = os.path.join(self.logs_directory, 'trace')

        self.mapping = {}
        self.mapping['command'] = self.command_filename
        self.mapping['error'] = self.error_filename
        self.mapping['info'] = self.info_filename
        self.mapping['debug'] = self.debug_filename
        self.mapping['isctl'] = self.isctl_filename
        self.mapping['api'] = self.api_filename
        self.mapping['odata'] = self.odata_filename
        self.mapping['redfish'] = self.redfish_filename
        self.mapping['ucsm'] = self.ucsm_filename
        self.mapping['k8s'] = self.k8s_filename
        self.mapping['ocapi'] = self.ocapi_filename
        self.mapping['ocp'] = self.ocp_filename
        self.mapping['kubevirt'] = self.kubevirt_filename
        self.mapping['vcenter'] = self.vcenter_filename
        self.mapping['nexus'] = self.nexus_filename
        self.mapping['apic'] = self.apic_filename
        self.mapping['iwo'] = self.iwo_filename
        self.mapping['ssh'] = self.ssh_filename

    def initialize(self, max_dirs=100):
        try:
            if self.log_id is not None:
                if not os.path.isdir(self.logs_directory):
                    os.makedirs(self.logs_directory, exist_ok=True)

                logs_base_directory = os.path.dirname(self.logs_directory)
                my_dirs = []
                for name in os.listdir(logs_base_directory):
                    directory = os.path.join(logs_base_directory, name)
                    if os.path.isdir(directory):
                        my_dirs.append(
                            dict(
                                directory=directory,
                                create_time=int(os.path.getmtime(directory))
                            )
                        )

                if len(my_dirs) > max_dirs:
                    my_dirs = sorted(my_dirs, key=lambda i: i['create_time'])
                    my_max = len(my_dirs) - max_dirs
                    for index in range(0, my_max):
                        directory = my_dirs[index]['directory']
                        if directory.startswith(logs_base_directory):
                            if directory != self.logs_directory:
                                shutil.rmtree(directory)

        except BaseException:
            pass

    def clean(self):
        if self.log_id is not None:
            shutil.rmtree(self.logs_directory)

    def trace(self, name, start_time):
        log_filename = os.path.join(self.logs_directory, self.trace_filename)
        try:
            self.safe_append(
                log_filename,
                '%s\t%s\n' % (
                    int(time.time() * 1000) - start_time,
                    name
                )
            )
        except BaseException:
            pass

    def analyze_isctl(self):
        result = {}
        result['read'] = False
        result['calls'] = 0
        result['success'] = 0
        result['failed'] = 0
        result['total_time'] = 0

        content = self.get_file(self.isctl_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                result['calls'] = result['calls'] + 1
                (when, success, duration, count, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

        return result

    def analyze_ucsm(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['mo'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.ucsm_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                if 'disconnect ' in command:
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)
                    continue

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_apic(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['mo'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.apic_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                if len(line.split('\t')) != 4:
                    print(line)

                (success, duration, count, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                if 'disconnect ' in command:
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)
                    continue

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_iwo(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['mo'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.iwo_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, count, command, url, body) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                if 'disconnect ' in command:
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)
                    continue

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_k8s(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['mo'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.k8s_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, scope, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_ocp(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['mo'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.ocp_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                try:
                    (when, success, duration, scope, command) = line.split('\t')
                    if success == 'True':
                        result['success'] = result['success'] + 1
                    else:
                        result['failed'] = result['failed'] + 1

                    result['total_time'] = result['total_time'] + int(duration)

                    result['mo'] = result['mo'] + 1
                    result['mo_time'] = result['mo_time'] + int(duration)
                except BaseException:
                    pass

        return result

    def analyze_kubevirt(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['mo'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.kubevirt_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, scope, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_vcenter(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['connect_time'] = 0
        result['mo'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.vcenter_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, scope, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_nexus(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['mo'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['mo_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.nexus_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                (when, success, duration, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                if 'disconnect ' in command:
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)
                    continue

                result['mo'] = result['mo'] + 1
                result['mo_time'] = result['mo_time'] + int(duration)

        return result

    def analyze_redfish(self):
        result = {}
        result['read'] = False
        result['success'] = 0
        result['failed'] = 0
        result['connect'] = 0
        result['disconnect'] = 0
        result['path'] = 0
        result['connect_time'] = 0
        result['disconnect_time'] = 0
        result['path_time'] = 0
        result['total_time'] = 0

        content = self.get_file(self.redfish_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                if len(line.split('\t')) != 4:
                    continue

                (when, success, duration, command) = line.split('\t')
                if success == 'True':
                    result['success'] = result['success'] + 1
                else:
                    result['failed'] = result['failed'] + 1

                result['total_time'] = result['total_time'] + int(duration)

                if 'connect ' in command:
                    result['connect'] = result['connect'] + 1
                    result['connect_time'] = result['connect_time'] + int(duration)
                    continue

                if 'disconnect ' in command:
                    result['disconnect'] = result['disconnect'] + 1
                    result['disconnect_time'] = result['disconnect_time'] + int(duration)
                    continue

                result['path'] = result['path'] + 1
                result['path_time'] = result['path_time'] + int(duration)

        return result

    def analyze_ssh(self):
        result = {}
        result['read'] = False
        result['calls'] = 0
        result['total_time'] = 0

        content = self.get_file(self.ssh_filename)
        if content is None:
            return result

        result['read'] = True
        for line in content.split('\n'):
            if len(line) > 0:
                result['calls'] = result['calls'] + 1
                (when, success, duration, ip_address, command) = line.split('\t')
                result['total_time'] = result['total_time'] + int(duration)

        return result

    def analyze_log(self, filename):
        result = {}
        result['read'] = False
        result['lines'] = 0

        content = self.get_file(filename)
        if content is None:
            return result

        result['read'] = True
        result['lines'] = len(content.split('\n'))
        return result

    def analyze(self, duration):
        result = {}
        result['duration'] = duration
        info = self.analyze_isctl()
        if info['read']:
            result['isctl'] = info

        info = self.analyze_redfish()
        if info['read']:
            result['redfish'] = info

        info = self.analyze_ucsm()
        if info['read']:
            result['ucsm'] = info

        info = self.analyze_nexus()
        if info['read']:
            result['nexus'] = info

        info = self.analyze_k8s()
        if info['read']:
            result['k8s'] = info

        info = self.analyze_ocp()
        if info['read']:
            result['ocp'] = info

        info = self.analyze_kubevirt()
        if info['read']:
            result['kubevirt'] = info

        info = self.analyze_vcenter()
        if info['read']:
            result['vcenter'] = info

        info = self.analyze_apic()
        if info['read']:
            result['apic'] = info

        info = self.analyze_iwo()
        if info['read']:
            result['iwo'] = info

        info = self.analyze_ssh()
        if info['read']:
            result['ssh'] = info

        result['error'] = self.analyze_log(self.error_filename)
        result['info'] = self.analyze_log(self.info_filename)
        result['debug'] = self.analyze_log(self.debug_filename)
        result['cache_hits'] = self.analyze_cache_hit()

        return result

    def get_file(self, filename):
        if os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file_handler:
                    return file_handler.read()
            except BaseException:
                pass
        return None

    def get_log(self, log_name, json_conversion=False):
        filename = os.path.join(
            self.logs_directory,
            log_name
        )

        content = None
        if os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file_handler:
                    content = file_handler.read()

                if json_conversion:
                    content = json.loads(content)

            except BaseException:
                return None

        return content

    def set_log(self, log_name, content, json_conversion=False):
        filename = os.path.join(
            self.logs_directory,
            log_name
        )

        try:
            with open(filename, 'w', encoding='utf-8') as file_handler:
                if json_conversion:
                    file_handler.write(json.dumps(content, indent=4))
                else:
                    file_handler.write(content)

        except BaseException:
            return False

        return True

    def get_log_filename(self, log_name):
        if log_name in self.mapping:
            return self.mapping[log_name]
        return None

    def is_log(self, log_name):
        if log_name in self.mapping:
            return os.path.isfile(self.mapping[log_name])
        return False

    def get_logs(self, files=None):
        if files is None:
            files = ['debug', 'info', 'error', 'isctl', 'ssh', 'redfish', 'ucsm', 'nexus', 'k8s', 'ocapi', 'ocp', 'kubevirt', 'vcenter', 'apic', 'iwo']

        content = {}
        for filename in files:
            if filename in self.mapping:
                content[filename] = self.get_file(self.mapping[filename])

        return content

    def analyze_cache_hit(self):
        content = self.get_file(self.cache_filename)
        if content is None:
            return 0
        return len(content.split('\n'))

    def cache_hit(self, object_type, object_scope, object_name, filename, ttl, age):
        msg = "%s\t%s\t%s\t%s\t%s\t%s\n" % (
            ttl,
            age,
            object_type,
            object_scope,
            object_name,
            filename
        )

        success = self.safe_append(
            self.cache_filename,
            msg
        )
        if not success:
            print('SSH log failed...')

    def is_cache(self, key):
        filename = '%s.%s' % (
            self.cache_filename,
            key
        )
        return os.path.isfile(filename)

    def get_cache(self, key):
        try:
            filename = '%s.%s' % (
                self.cache_filename,
                key
            )
            if not os.path.isfile(filename):
                return None

            content = json.loads(
                self.get_file(
                    filename
                )
            )

        except BaseException:
            return None

        return content

    def set_cache(self, key, cache):
        try:
            filename = '%s.%s' % (
                self.cache_filename,
                key
            )
            success = self.safe_write(
                filename,
                json.dumps(
                    cache,
                    indent=4
                )
            )

        except BaseException:
            return False

        return success

    def wait_for_no_file(self, filename, max_wait_ms=1000, gap=0.1):
        try:
            start = int(time.time() * 1000)
            while True:
                if not os.path.isfile(filename):
                    return True
                time.sleep(0.1)
                if int(time.time() * 1000) - start > max_wait_ms:
                    return False
        except BaseException:
            return False

    def safe_write(self, filename, content, force=True):
        success = True
        try:
            lock = '%s.lock' % (filename)
            if not self.wait_for_no_file(lock):
                if not force:
                    return False

            loop = 0
            while True:
                try:
                    with open(lock, 'w', encoding='utf-8') as file_handler:
                        file_handler.write('lock')
                    file_handler.close()

                    with open(filename, 'w', encoding='utf-8') as file_handler:
                        file_handler.write(content)

                    if os.path.isfile(lock):
                        os.remove(lock)

                    break

                except BaseException:
                    if os.path.isfile(lock):
                        os.remove(lock)

                time.sleep(0.01)
                loop = loop + 1
                if loop > 3:
                    success = False
                    break

            if os.path.isfile(lock):
                os.remove(lock)

        except BaseException:
            return False

        return success

    def safe_append(self, filename, content, force=True):
        success = True
        try:
            lock = '%s.lock' % (filename)
            if not self.wait_for_no_file(lock):
                if not force:
                    return False

            loop = 0
            while True:
                try:
                    with open(lock, 'w', encoding='utf-8') as file_handler:
                        file_handler.write('lock')
                    file_handler.close()

                    with open(filename, 'a', encoding='utf-8') as file_handler:
                        file_handler.write(content)

                    if os.path.isfile(lock):
                        os.remove(lock)

                    break

                except BaseException:
                    if os.path.isfile(lock):
                        os.remove(lock)

                time.sleep(0.01)
                loop = loop + 1
                if loop > 3:
                    success = False
                    break

            if os.path.isfile(lock):
                os.remove(lock)

        except BaseException:
            return False

        return success

    def ssh(self, ip_address, cmd, success, duration):
        try:
            current_time = datetime.datetime.now()
            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time, success, duration, ip_address, cmd)

            success = self.safe_append(
                self.ssh_filename,
                msg
            )
            if not success:
                print('SSH log failed...')

        except BaseException:
            pass

    def ucsm(self, command, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command
            )

            success = self.safe_append(
                self.ucsm_filename,
                msg
            )
            if not success:
                print('Ucsm log failed...')

        except BaseException:
            pass

    def apic(self, command, success, duration, item_count=None):
        try:
            count = '-'
            if item_count is not None:
                count = int(item_count)

            msg = "%s\t%s\t%s\t%s\n" % (
                success,
                duration,
                count,
                command
            )

            success = self.safe_append(
                self.apic_filename,
                msg
            )
            if not success:
                print('Apic log failed...')

        except BaseException:
            pass

    def get_apic_mo(self, name):
        filename = os.path.join(
            self.logs_directory,
            'apic.mo.%s' % (name)
        )

        content = self.get_file(filename)
        if content is not None:
            content = json.loads(content)

        return content

    def apic_mo(self, name, managed_object):
        try:
            name = name.replace('/', '_')
            filename = os.path.join(
                self.logs_directory,
                'apic.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def iwo(self, command, url, body, success, duration, item_count=None):
        try:
            current_time = datetime.datetime.now()

            count = '-'
            if item_count is not None:
                count = int(item_count)

            msg = "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                count,
                command,
                url,
                body
            )

            success = self.safe_append(
                self.iwo_filename,
                msg
            )
            if not success:
                print('Iwo log failed...')

        except BaseException:
            pass

    def get_iwo_mo(self, name):
        filename = os.path.join(
            self.logs_directory,
            'iwo.mo.%s' % (name)
        )

        content = self.get_file(filename)
        if content is not None:
            content = json.loads(content)

        return content

    def iwo_mo(self, name, managed_object):
        try:
            filename = os.path.join(
                self.logs_directory,
                'iwo.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def k8s_mo(self, name, managed_object):
        try:
            filename = os.path.join(
                self.logs_directory,
                'k8s.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def k8s(self, command, scope, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command,
                scope
            )

            success = self.safe_append(
                self.k8s_filename,
                msg
            )
            if not success:
                print('K8s log failed...')

        except BaseException:
            pass

    def ocp_mo(self, name, managed_object):
        try:
            filename = os.path.join(
                self.logs_directory,
                'ocp.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def ocp(self, command, scope, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command,
                scope
            )

            success = self.safe_append(
                self.ocp_filename,
                msg
            )
            if not success:
                print('ocp log failed...')

        except BaseException:
            pass

    def ocapi_mo(self, name, managed_object):
        try:
            filename = os.path.join(
                self.logs_directory,
                'ocapi.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def ocapi(self, command, scope, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command,
                scope
            )

            success = self.safe_append(
                self.ocapi_filename,
                msg
            )
            if not success:
                print('ocapi log failed...')

        except BaseException:
            pass

    def kubevirt_mo(self, name, managed_object):
        try:
            filename = os.path.join(
                self.logs_directory,
                'kubevirt.mo.%s' % (name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        managed_object,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def kubevirt(self, command, scope, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command,
                scope
            )

            success = self.safe_append(
                self.kubevirt_filename,
                msg
            )
            if not success:
                print('K8s log failed...')

        except BaseException:
            pass

    def vcenter(self, command, scope, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command,
                scope
            )

            success = self.safe_append(
                self.vcenter_filename,
                msg
            )
            if not success:
                print('vcenter log failed...')

        except BaseException:
            pass

    def nexus_cli(self, nexus_ip, name, output):
        try:
            filename = os.path.join(
                self.logs_directory,
                'nexus.%s.%s' % (nexus_ip, name)
            )

            if not os.path.isfile(filename):
                self.safe_write(
                    filename,
                    json.dumps(
                        output,
                        indent=4
                    )
                )

        except BaseException:
            pass

    def nexus(self, command, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command
            )

            success = self.safe_append(
                self.nexus_filename,
                msg
            )
            if not success:
                print('Nexus log failed...')

        except BaseException:
            pass

    def redfish(self, command, success, duration):
        try:
            current_time = datetime.datetime.now()

            msg = "%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                command
            )

            success = self.safe_append(
                self.redfish_filename,
                msg
            )
            if not success:
                print('Redfish log failed...')

        except BaseException:
            pass

    def get_api(self):
        content = self.get_file(self.api_filename)
        if content is None:
            return {}
        return json.loads(content)

    def api(self, command, content):
        try:
            apis = self.get_api()
            apis[command] = content

            success = self.safe_write(
                self.api_filename,
                json.dumps(apis, indent=4)
            )
            if not success:
                print('Api log failed...')

        except BaseException:
            pass

    def get_odata(self):
        content = self.get_file(self.odata_filename)
        if content is None:
            return {}
        return json.loads(content)

    def odata(self, path, content):
        try:
            odatas = self.get_odata()
            odatas[path] = content

            success = self.safe_write(
                self.odata_filename,
                json.dumps(odatas, indent=4)
            )
            if not success:
                print('Odata log failed...')

        except BaseException:
            pass

    def cli(self, command, success, duration, item_count=None):
        try:
            current_time = datetime.datetime.now()

            count = '-'
            if item_count is not None:
                count = int(item_count)

            msg = "%s\t%s\t%s\t%s\t%s\n" % (
                current_time,
                success,
                duration,
                count,
                command
            )

            success = self.safe_append(
                self.isctl_filename,
                msg
            )
            if not success:
                print('Isctl log failed...')

        except BaseException:
            pass

    def adhoc(self, filename, info):
        log_filename = os.path.join(self.logs_directory, filename)
        try:
            success = self.safe_append(
                log_filename,
                info
            )
        except BaseException:
            pass
        return log_filename

    def error(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)

            success = self.safe_append(
                self.error_filename,
                msg
            )
            if not success:
                print('Error log failed (%s): %s' % (self.error_filename, msg))

            self.info(location, message)

        except BaseException:
            pass

    def info(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)

            success = self.safe_append(
                self.info_filename,
                msg
            )
            if not success:
                print('Info log failed...')

            self.debug(location, message)

        except BaseException:
            pass

    def debug(self, location, message):
        try:
            current_time = datetime.datetime.now()
            msg = "[%s]\t[%s]\t%s\n" % (
                current_time, location, message)

            success = self.safe_append(
                self.debug_filename,
                msg
            )
            if not success:
                print('Debug log failed...')

        except BaseException:
            pass

    def get_lcm_report(self):
        if os.path.isfile(self.lcm_report_filename):
            try:
                with open(self.lcm_report_filename, 'r', encoding='utf-8') as file_handler:
                    return json.loads(file_handler.read())

            except BaseException:
                pass

        return None

    def set_lcm_report(self, report):
        try:
            with open(self.lcm_report_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(json.dumps(report, indent=4))

        except BaseException:
            return False

        return True

    def set_command(self, command):
        try:
            with open(self.command_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(command)
        except BaseException:
            pass

    def get_command(self):
        try:
            if os.path.isfile(self.command_filename):
                with open(self.command_filename, 'r', encoding='utf-8') as file_handler:
                    return file_handler.read()

        except BaseException:
            pass

        return None

    def show_last_logs(self):
        my_dirs = []
        logs_directory = os.path.dirname(self.logs_directory)
        for name in os.listdir(logs_directory):
            directory = os.path.join(logs_directory, name)
            if os.path.isdir(directory):
                directory_info = {}
                directory_info['name'] = name
                directory_info['directory'] = directory
                directory_info['create_time'] = int(os.path.getmtime(directory))
                directory_info['time'] = datetime.datetime.fromtimestamp(directory_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')

                command_filename = os.path.join(directory, 'command')
                command = self.get_file(command_filename)
                if command is not None:
                    directory_info['command'] = command
                    my_dirs.append(directory_info)

        my_dirs = sorted(my_dirs, key=lambda i: i['create_time'], reverse=True)

        my_output = output_helper.OutputHelper(log_id=self.log_id)
        my_output.my_table(
            my_dirs,
            order=['name', 'command', 'directory', 'time'],
            headers=['Name', 'Command', 'Directory', 'Time']
        )

    def get_command_directory(self, search_command, debug=False):
        my_dirs = []
        logs_directory = self.logs_directory
        if self.log_id is not None:
            logs_directory = os.path.dirname(self.logs_directory)

        for name in os.listdir(logs_directory):
            directory = os.path.join(logs_directory, name)
            if os.path.isdir(directory):
                directory_info = {}
                directory_info['name'] = name
                directory_info['directory'] = directory
                directory_info['create_time'] = int(os.path.getmtime(directory))
                directory_info['time'] = datetime.datetime.fromtimestamp(directory_info['create_time']).strftime('%Y-%m-%d %H:%M:%S')

                command_filename = os.path.join(directory, 'command')
                command = self.get_file(command_filename)
                if command is not None:
                    directory_info['command'] = command
                    my_dirs.append(directory_info)

                if debug:
                    print(json.dumps(directory_info, indent=4))

        my_dirs = sorted(my_dirs, key=lambda i: i['create_time'], reverse=True)

        for my_dir in my_dirs:
            if my_dir['command'] == search_command:
                return my_dir['directory']

        if '"' in search_command:
            search_command = search_command.replace('"', '')
            for my_dir in my_dirs:
                if my_dir['command'] == search_command:
                    return my_dir['directory']

        return None

    def bug_report(self, name):
        logs_directory = os.path.dirname(self.logs_directory)
        directory = os.path.join(logs_directory, name)
        if not os.path.isdir(directory):
            print('Directory not found: %s' % (directory))
            return

        ssh_handler = ssh.Ssh('10.58.25.162', 'root', password='!Cisc0_123')
        for filename in os.listdir(directory):
            source = os.path.join(directory, filename)
            destination = os.path.join('/tmp/iserver-bug-reports', '%s.%s' % (name, filename))
            if not ssh_handler.scp_file(source, destination):
                print('Log upload failed: %s' % (source))
                return
            print('Log file uploaded: %s' % (source))
