import os
import uuid
import time
import hashlib
import traceback
import json

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

# pylint: disable=wrong-import-position
import paramiko
from paramiko import SSHClient

from lib import output_helper
from lib import template


class Ssh():
    def __init__(self, ip_address, username, port=22, password=None, key_filename=None, load_system_host_keys=False, endpoint_type=None, verbose=False, debug=False):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.port = port
        self.key_filename = key_filename
        self.timeout = 10
        self.load_system_host_keys = load_system_host_keys
        self.endpoint_type = endpoint_type
        if self.endpoint_type is None:
            self.endpoint_type = 'standard'

        self.template_handler = template.Template(verbose=verbose, debug=debug)
        self.my_output = output_helper.OutputHelper(verbose=verbose, debug=debug)

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
                success = False
                if session is not None:
                    session.close()

            if success:
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

    def scp_file(self, source, destination, put=True, retry=3):
        try:
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
                    else:
                        sftp.get(source, destination)
                    sftp.close()

                    session.close()
                except paramiko.ssh_exception.AuthenticationException:
                    self.my_output.error(
                        'Authentication failed at %s with username: %s, password: %s, key: %s' % (
                            self.ip_address,
                            self.username,
                            self.password,
                            self.key_filename
                        )
                    )
                    success = False
                except BaseException:
                    self.my_output.error(
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
            self.myoutput.error(
                traceback.format_exc()
            )
            return False

    def run_cmd(self, command, live_output=False, timeout=3600, max_attempts=1):
        session = None
        start_time = int(time.time())
        self.my_output.debug('Command: %s' % (command))

        try:
            success = True

            session = self.create_session(max_attempts=max_attempts)
            if session is None:
                success = False
                output = None
                error = 'SSH access failed'
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
            self.my_output.debug('Duration: %s seconds' % (end_time - start_time))

        return success, output, error

    def exec_cmd(self, command, timeout=30, max_attempts=1):
        session = None
        start_time = int(time.time())
        self.my_output.debug('Command: %s' % (command))
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
            self.my_output.debug('Duration: %s seconds' % (end_time - start_time))

        return success

    def create_directory(self, directory_name):
        cmd = 'mkdir -p %s' % (directory_name)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return False
        return True

    def is_file(self, filename):
        cmd = 'file %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success or 'No such file or directory' in output:
            return False
        return True

    def touch_file(self, filename):
        cmd = 'touch %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success:
            return False
        return True

    def get_file(self, filename, convert_json=False):
        cmd = 'cat %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if not success or 'No such file or directory' in output:
            return None

        if convert_json:
            try:
                output = json.loads(output)
            except BaseException:
                output = None

        return output

    def delete_file(self, filename):
        cmd = 'rm -f %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        return success

    def set_file_chmod(self, filename, chmod):
        cmd = 'chmod %s %s' % (chmod, filename)
        success, output, error = self.run_cmd(cmd)
        if success:
            return True
        return False

    def get_file_md5(self, filename):
        cmd = 'md5sum %s' % (filename)
        success, output, error = self.run_cmd(cmd)
        if success:
            return output.split(' ')[0]
        return None

    def get_local_file_md5(self, filename):
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

    def run_script(self, script_filename, variables={}, live_output=False, timeout=3600):
        self.my_output.debug('IP: %s' % (self.ip_address))
        self.my_output.debug('Username: %s' % (self.username))
        self.my_output.debug('Password: %s' % (self.password))
        self.my_output.default('Run script: %s' % (script_filename))

        content = self.template_handler.get_template(
            script_filename,
            variables
        )
        if content is None:
            return False

        self.my_output.debug('~~~ script content ~~~')
        self.my_output.debug(content)
        self.my_output.debug('~~~~~~~~~~~~~~~~~~~~~~')

        source_filename = '/tmp/%s' % (str(uuid.uuid4()))
        try:
            with open(source_filename, 'wb') as file_handler:
                file_handler.write(content.encode('utf-8'))
        except BaseException:
            self.my_output.error(
                'Preparation of script file for upload failed'
            )
            self.my_output.default(traceback.format_exc())
            return False

        self.my_output.debug('Local script prepared: %s' % (source_filename))

        destination_filename = str(uuid.uuid4())
        if not self.scp_file(source_filename, destination_filename):
            self.my_output.error(
                'Script upload failed: %s => %s' % (
                    source_filename,
                    destination_filename
                )
            )
            return False
        self.my_output.debug('Script uploaded: %s' % (destination_filename))

        if not self.set_file_chmod(destination_filename, '755'):
            self.my_output.error(
                'Script chmod failed: %s' % (
                    destination_filename
                )
            )
            return False
        self.my_output.debug('Chmod set to 755')

        if live_output:
            self.my_output.debug('Run script with live output...')
        else:
            self.my_output.debug('Run script and wait for completion...')

        success, output, error = self.run_cmd(
            './%s' % (destination_filename),
            live_output=live_output,
            timeout=timeout
        )

        if success:
            self.my_output.debug('Remote script execution finished')
            if not live_output:
                self.my_output.debug('~~~ script output ~~~')
                self.my_output.debug(output)
                self.my_output.debug('~~~~~~~~~~~~~~~~~~~~~')

            if not self.delete_file(destination_filename):
                self.my_output.error(
                    'Remote script delete failed: %s' % (
                        destination_filename
                    )
                )
                return False

            self.my_output.debug('Remote script deleted')

        if not success:
            self.my_output.error('Remote script execution failed')
            self.my_output.default('~~~ script error ~~~')
            self.my_output.default(error)
            self.my_output.default('~~~~~~~~~~~~~~~~~~~~~')
            self.my_output.default('Remote script not deleted for further troubleshooting: %s' % (destination_filename))

        return success

    def run_file_upload(self, source_filename, destination_filename, destination_chmod, is_template=False, variables={}):
        if is_template:
            content = self.template_handler.get_template(
                source_filename,
                variables
            )
            if content is None:
                return False

            self.my_output.debug(content)

            source_filename = '/tmp/%s' % (str(uuid.uuid4()))
            try:
                with open(source_filename, 'wb') as file_handler:
                    file_handler.write(content.encode('utf-8'))

            except BaseException:
                self.my_output.error(
                    'Preparation of script file for upload failed'
                )
                self.my_output.default(traceback.format_exc())
                return False

            self.my_output.debug('Local file prepared: %s' % (source_filename))

        self.my_output.info('Copy file: %s => %s' % (source_filename, destination_filename))

        if not os.path.isfile(source_filename):
            self.my_output.error('File not found: %s' % (source_filename))
            return False
        self.my_output.info('Local file found: %s' % (source_filename))

        source_md5 = self.get_local_file_md5(source_filename)
        destination_md5 = self.get_file_md5(destination_filename)
        if source_md5 == destination_md5:
            self.my_output.default('Checksum (md5) match and upload skipped')
        else:
            if not self.scp_file(source_filename, destination_filename):
                self.my_output.error('File upload failed')
                return False

        if not self.set_file_chmod(destination_filename, destination_chmod):
            self.my_output.error('File chmod failed: %s' % (destination_filename))
            return False

        return True
