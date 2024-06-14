import os
import re
import uuid
import time
import hashlib
import traceback
import json
import warnings
import yaml

warnings.filterwarnings(action='ignore', module='.*paramiko.*')

# pylint: disable=wrong-import-position
import paramiko
from paramiko import SSHClient

from lib import template
from lib import file_helper
from lib import log_helper


class Ssh():
    def __init__(self, ip_address, username, port=22, password=None, key_filename=None, load_system_host_keys=False, endpoint_type=None, verbose=False, debug=False, log_id=None, timeout=10):
        self.log_handler = log_helper.Log(log_id=log_id)
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.port = port
        self.key_filename = key_filename
        self.timeout = timeout
        self.load_system_host_keys = load_system_host_keys
        self.endpoint_type = endpoint_type
        if self.endpoint_type is None:
            self.endpoint_type = 'standard'

        self.template_handler = template.Template(verbose=verbose, debug=debug)

    def create_session(self, max_attempts=1):
        attempt = 1
        while True:
            try:
                success = True
                session = SSHClient()
                if self.load_system_host_keys:
                    session.load_system_host_keys()
                session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                if self.endpoint_type not in ['standard', 'cisco']:
                    self.log_handler.error(
                        'create_session',
                        'Unsupported endpoint type: %s' % (self.endpoint_type)
                    )
                    return None

                if self.endpoint_type == 'standard':
                    if self.password is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            password=self.password,
                            timeout=self.timeout
                        )

                    if self.key_filename is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            key_filename=self.key_filename,
                            timeout=self.timeout
                        )

                if self.endpoint_type == 'cisco':
                    session.connect(
                        self.ip_address,
                        port=self.port,
                        username=self.username,
                        password=self.password,
                        timeout=self.timeout,
                        allow_agent=False,
                        look_for_keys=False
                    )

            except BaseException:
                self.log_handler.error(
                    'create_session',
                    traceback.format_exc()
                )
                success = False
                if session is not None:
                    session.close()

            if success:
                self.log_handler.debug(
                    'create_session',
                    'Session created at %s' % (self.ip_address)
                )
                return session

            if attempt == max_attempts:
                return None

            time.sleep(1)
            attempt = attempt + 1

    def is_ssh(self):
        session = self.create_session(max_attempts=1)
        if session is None:
            return False

        session.close()
        return True

    def wait_ssh(self, timeout):
        start_time = int(time.time())
        while True:
            if self.is_ssh():
                return True

            if int(time.time()) - start_time > timeout:
                return False

            time.sleep(10)

    def scp_directory(self, source, destination, put=True, retry=1, path_fixup=True):
        try:
            if path_fixup:
                destination = self.path_fixup(destination)

            if not put:
                self.log_handler.error(
                    'scp_directory',
                    'download not implemented'
                )
                return False

            self.log_handler.debug(
                'scp_directory',
                '%s => %s' % (source, destination)
            )

            session = None
            loop = 0
            while True:
                try:
                    success = True

                    session = SSHClient()
                    if self.load_system_host_keys:
                        session.load_system_host_keys()
                    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                    if self.password is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            password=self.password,
                            timeout=self.timeout
                        )

                    if self.key_filename is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            key_filename=self.key_filename,
                            timeout=self.timeout
                        )

                    sftp = paramiko.SFTPClient.from_transport(session.get_transport())

                    for root, dirs, files in os.walk(source, topdown=False):
                        for name in dirs:
                            source_directory = os.path.join(root, name)
                            target_directory = self.path_fixup(
                                os.path.join(
                                    destination,
                                    self.path_fixup(source_directory[len(source):]).lstrip('/')
                                )
                            )

                            if not self.create_directory(target_directory):
                                self.log_handler.error(
                                    'scp_directory',
                                    'Create directory failed: %s' % (target_directory)
                                )
                                success = False
                                break

                            self.log_handler.debug(
                                'scp_directory',
                                'Directory created: %s' % (target_directory)
                            )

                        if not success:
                            break

                    for root, dirs, files in os.walk(source, topdown=False):
                        for name in files:
                            source_filename = os.path.join(root, name)
                            target_directory = os.path.dirname(source_filename)[len(source):]
                            if target_directory.startswith('/'):
                                target_directory = target_directory[1:]
                            if target_directory.startswith('\\'):
                                target_directory = target_directory[1:]

                            if len(target_directory) == 0:
                                destination_filename = os.path.join(
                                    destination,
                                    name
                                )

                            if len(target_directory) > 0:
                                destination_filename = os.path.join(
                                    destination,
                                    os.path.join(
                                        target_directory,
                                        name
                                    )
                                )

                            if put:
                                if os.path.isfile(source_filename):
                                    self.log_handler.debug(
                                        'scp_directory',
                                        'File %s => %s' % (
                                            source_filename,
                                            self.path_fixup(destination_filename)
                                        )
                                    )

                                    sftp.put(
                                        source_filename,
                                        self.path_fixup(destination_filename)
                                    )
                                else:
                                    self.log_handler.error(
                                        'scp_directory',
                                        'Source file not found %s' % (
                                            source_filename
                                        )
                                    )

                    sftp.close()

                    session.close()

                except paramiko.ssh_exception.AuthenticationException:
                    self.log_handler.error(
                        'scp_directory',
                        'Authentication failed at %s with username: %s, password: %s, key: %s' % (
                            self.ip_address,
                            self.username,
                            self.password,
                            self.key_filename
                        )
                    )
                    success = False
                except BaseException:
                    self.log_handler.error(
                        'scp_directory',
                        traceback.format_exc()
                    )
                    success = False
                finally:
                    if session is not None:
                        session.close()

                if success:
                    return True

                loop = loop + 1
                if loop > retry:
                    return False

                time.sleep(loop * 5)

        except BaseException:
            self.log_handler.error(
                'scp_directory',
                traceback.format_exc()
            )
            return False

    def scp_file(self, source, destination, put=True, retry=1, path_fixup=True):
        try:
            if path_fixup:
                destination = self.path_fixup(destination)

            session = None
            loop = 0
            while True:
                try:
                    success = True

                    session = SSHClient()
                    if self.load_system_host_keys:
                        session.load_system_host_keys()
                    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                    if self.password is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            password=self.password,
                            timeout=self.timeout
                        )

                    if self.key_filename is not None:
                        session.connect(
                            self.ip_address,
                            port=self.port,
                            username=self.username,
                            key_filename=self.key_filename,
                            timeout=self.timeout
                        )

                    sftp = paramiko.SFTPClient.from_transport(session.get_transport())
                    if put:
                        sftp.put(source, destination)
                        self.log_handler.debug(
                            'scp_file',
                            'put: %s => %s' % (
                                source,
                                destination
                            )
                        )
                    else:
                        sftp.get(source, destination)
                        self.log_handler.debug(
                            'scp_file',
                            'get: %s => %s' % (
                                source,
                                destination
                            )
                        )
                    sftp.close()

                    session.close()
                except paramiko.ssh_exception.AuthenticationException:
                    self.log_handler.error(
                        'scp_file',
                        'Authentication failed at %s with username: %s, password: %s, key: %s' % (
                            self.ip_address,
                            self.username,
                            self.password,
                            self.key_filename
                        )
                    )
                    success = False
                except BaseException:
                    self.log_handler.error(
                        'scp_file',
                        traceback.format_exc()
                    )
                    success = False
                finally:
                    if session is not None:
                        session.close()

                if success:
                    return True

                loop = loop + 1
                if loop > retry:
                    return False

                time.sleep(loop * 5)

        except BaseException:
            self.log_handler.error(
                'scp_file',
                traceback.format_exc()
            )
            return False

    def run_cmd(self, command, live_output=False, timeout=3600, max_attempts=1):
        session = None
        start_time = int(time.time())
        self.log_handler.debug(
            'run_cmd',
            'Command: %s' % (command)
        )

        try:
            success = True

            session = self.create_session(max_attempts=max_attempts)
            if session is None:
                success = False
                output = None
                error = 'SSH access failed'
                self.log_handler.error('run_cmd', 'IP: %s' % (self.ip_address))
                self.log_handler.error('run_cmd', 'Port: %s' % (self.port))
                self.log_handler.error('run_cmd', 'Username: %s' % (self.username))
                self.log_handler.error('run_cmd', 'Password: %s' % (self.password))
                self.log_handler.error('run_cmd', 'Key: %s' % (self.key_filename))
            else:
                stdin, stdout, stderr = session.exec_command(
                    command,
                    timeout=timeout,
                    get_pty=live_output
                )
                if live_output:
                    for line in iter(stdout.readline, ""):
                        print(line, end="")

                if stdout.channel.recv_exit_status() > 0:
                    success = False

                stdin.flush()
                output = stdout.read().decode('utf-8')
                error = stderr.read().decode('utf-8')

        except BaseException:
            success = False
            output = None
            error = traceback.format_exc()

        finally:
            if session is not None:
                session.close()
            end_time = int(time.time())
            self.log_handler.debug('run_cmd', 'Duration: %s seconds' % (end_time - start_time))

        return success, output, error

    def exec_cmd(self, command, timeout=30, max_attempts=1):
        session = None
        start_time = int(time.time())
        self.log_handler.debug('exec_cmd', 'Command: %s' % (command))
        try:
            success = True

            session = self.create_session(max_attempts=max_attempts)
            if session is None:
                success = False
            else:
                session.exec_command(
                    command,
                    timeout=timeout
                )

        except BaseException:
            success = False

        finally:
            if session is not None:
                session.close()
            end_time = int(time.time())
            self.log_handler.debug('exec_cmd', 'Duration: %s seconds' % (end_time - start_time))

        return success

    def path_fixup(self, name):
        return name.replace('\\', '/')

    def create_file(self, content, filename=None):
        source_filename = file_helper.set_tmp_file(content)
        if filename is None:
            destination_filename = source_filename
        else:
            destination_filename = filename

        if not self.scp_file(source_filename, destination_filename):
            return None

        return destination_filename

    def create_directory(self, directory_name, path_fixup=True):
        if path_fixup:
            directory_name = self.path_fixup(directory_name)

        cmd = 'mkdir -p %s' % (directory_name)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return False
        return True

    def delete_directory(self, directory_name, path_fixup=True):
        if path_fixup:
            directory_name = self.path_fixup(directory_name)

        if directory_name == '/':
            self.log_handler.error(
                'delete_directory',
                'Hell no on root directory delete'
            )
            return False

        cmd = 'rm -rf %s' % (directory_name)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return False
        return True

    def get_directories(self, path, path_fixup=True):
        if path_fixup:
            path = self.path_fixup(path)

        cmd = 'ls -la %s' % (path)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return None

        directory_names = []
        for line in output.split('\n'):
            line = re.sub(' +', ' ', line)
            if len(line.split(' ')) != 9:
                continue

            if not line.split(' ')[0].startswith('d'):
                continue

            directory_name = line.split(' ')[8]
            if directory_name not in ['.', '..']:
                directory_names.append(
                    directory_name
                )

        return directory_names

    def get_filenames(self, path, path_fixup=True, relative=False):
        if path_fixup:
            path = self.path_fixup(path)

        cmd = 'find %s -type f' % (path)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return None

        filenames = []
        for line in output.split('\n'):
            if line == path:
                continue

            if relative:
                line = line[len(path) + 1:]

            if len(line) > 0:
                filenames.append(line)

        return filenames

    def is_file(self, filename, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'file %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success or 'No such file or directory' in output:
            return False
        return True

    def touch_file(self, filename, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'touch %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return False
        return True

    def get_file(self, filename, convert_json=False, convert_yaml=False, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'cat %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success or 'No such file or directory' in output:
            return None

        if convert_json:
            try:
                output = json.loads(output)
            except BaseException:
                output = None

        if convert_yaml:
            try:
                output = yaml.safe_load(output)
            except BaseException:
                output = None

        return output

    def delete_file(self, filename, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'rm -f %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        return success

    def set_file_chmod(self, filename, chmod, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'chmod %s %s' % (chmod, filename)
        success, output, error = self.run_cmd(cmd)
        if success:
            return True
        return False

    def get_file_md5(self, filename, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        cmd = 'md5sum %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if success:
            return output.split(' ')[0]
        return None

    def get_local_file_md5(self, filename, path_fixup=True):
        if path_fixup:
            filename = self.path_fixup(filename)

        if not os.path.isfile(filename):
            return None
        hasher = hashlib.md5()
        blocksize = 65536
        with open(filename, 'rb') as file_handler:
            buf = file_handler.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = file_handler.read(blocksize)
        md5 = hasher.hexdigest()
        return md5

    def run_script(self, script_filename, variables={}, live_output=False, timeout=3600, path_fixup=True):
        if path_fixup:
            script_filename = self.path_fixup(script_filename)

        self.log_handler.debug('run_script', 'IP: %s' % (self.ip_address))
        self.log_handler.debug('run_script', 'Username: %s' % (self.username))
        self.log_handler.debug('run_script', 'Password: %s' % (self.password))
        self.log_handler.debug('run_script', 'Run script: %s' % (script_filename))

        content = self.template_handler.get_template(
            script_filename,
            variables
        )
        if content is None:
            return False

        self.log_handler.debug('run_script', '~~~ script content ~~~')
        self.log_handler.debug('run_script', content)
        self.log_handler.debug('run_script', '~~~~~~~~~~~~~~~~~~~~~~')

        source_filename = '/tmp/%s' % (str(uuid.uuid4()))
        try:
            with open(source_filename, 'wb') as file_handler:
                file_handler.write(content.encode('utf-8'))
        except BaseException:
            self.log_handler.error(
                'run_script',
                'Preparation of script file for upload failed'
            )
            self.log_handler.error(
                'run_script',
                traceback.format_exc()
            )
            return False

        self.log_handler.debug('run_script', 'Local script prepared: %s' % (source_filename))

        destination_filename = str(uuid.uuid4())
        if not self.scp_file(source_filename, destination_filename):
            self.log_handler.error(
                'run_script',
                'Script upload failed: %s => %s' % (
                    source_filename,
                    destination_filename
                )
            )
            return False
        self.log_handler.debug('run_script', 'Script uploaded: %s' % (destination_filename))

        if not self.set_file_chmod(destination_filename, '755'):
            self.log_handler.error(
                'run_script',
                'Script chmod failed: %s' % (
                    destination_filename
                )
            )
            return False
        self.log_handler.debug('run_script', 'Chmod set to 755')

        if live_output:
            self.log_handler.debug('run_script', 'Run script with live output...')
        else:
            self.log_handler.debug('run_script', 'Run script and wait for completion...')

        success, output, error = self.run_cmd(
            './%s' % (destination_filename),
            live_output=live_output,
            timeout=timeout
        )

        if success:
            self.log_handler.debug('run_script', 'Remote script execution finished')
            if not live_output:
                self.log_handler.debug('run_script', '~~~ script output ~~~')
                self.log_handler.debug('run_script', output)
                self.log_handler.debug('run_script', '~~~~~~~~~~~~~~~~~~~~~')

            if not self.delete_file(destination_filename):
                self.log_handler.error(
                    'run_script',
                    'Remote script delete failed: %s' % (
                        destination_filename
                    )
                )
                return False

            self.log_handler.debug('run_script', 'Remote script deleted')

        if not success:
            self.log_handler.error('run_script', 'Remote script execution failed')
            self.log_handler.error('run_script', '~~~ script error ~~~')
            self.log_handler.error('run_script', error)
            self.log_handler.error('run_script', '~~~~~~~~~~~~~~~~~~~~~')
            self.log_handler.error('run_script', 'Remote script not deleted for further troubleshooting: %s' % (destination_filename))

        return success

    def run_file_upload(self, source_filename, destination_filename, destination_chmod='644', is_template=False, variables={}, path_fixup=True):
        if path_fixup:
            source_filename = self.path_fixup(source_filename)
            destination_filename = self.path_fixup(destination_filename)

        if is_template:
            content = self.template_handler.get_template(
                source_filename,
                variables
            )
            if content is None:
                return False

            self.log_handler.debug('run_file_upload', content)

            source_filename = '/tmp/%s' % (str(uuid.uuid4()))
            try:
                with open(source_filename, 'wb') as file_handler:
                    file_handler.write(content.encode('utf-8'))

            except BaseException:
                self.log_handler.error(
                    'run_file_upload',
                    'Preparation of script file for upload failed'
                )
                self.log_handler.debug('run_file_upload', traceback.format_exc())
                return False

            self.log_handler.debug('run_file_upload', 'Local file prepared: %s' % (source_filename))

        self.log_handler.debug('run_file_upload', 'Copy file: %s => %s' % (source_filename, destination_filename))

        if not os.path.isfile(source_filename):
            self.log_handler.error('run_file_upload', 'File not found: %s' % (source_filename))
            return False
        self.log_handler.debug('run_file_upload', 'Local file found: %s' % (source_filename))

        source_md5 = self.get_local_file_md5(source_filename)
        destination_md5 = self.get_file_md5(destination_filename)
        if source_md5 == destination_md5:
            self.log_handler.debug('run_file_upload', 'Checksum (md5) match and upload skipped')
        else:
            temp_destination_filename = '/tmp/%s' % str((uuid.uuid4()))
            if not self.scp_file(source_filename, temp_destination_filename):
                self.log_handler.error('run_file_upload', 'File upload failed')
                return False

            if not self.exec_cmd('mv %s %s' % (temp_destination_filename, destination_filename)):
                self.log_handler.error('run_file_upload', 'File to move uploaded file to final destination')
                return False

        if not self.set_file_chmod(destination_filename, destination_chmod):
            self.log_handler.error('run_file_upload', 'File chmod failed: %s' % (destination_filename))
            return False

        return True
