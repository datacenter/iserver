import os
import uuid
import platform
import subprocess

from lib import input_validator
from lib import output_helper
from lib import ssh
from lib import template


class IsoAutoinstall():
    def __init__(self, template_name, log_id=None, verbose=False, debug=False):
        self.template_name = template_name
        self.my_output = output_helper.OutputHelper(verbose=verbose, debug=debug)
        self.input_validator_handler = input_validator.InputValidator(log_id=log_id)
        self.template_handler = template.Template(verbose=verbose, debug=debug)
        self.verbose = verbose
        self.debug = debug

    def get_script_filename(self):
        template_dir = self.input_validator_handler.get_template_dir(self.template_name, template_category='vc')
        if template_dir is None:
            self.my_output.error('Template dir not found for template: %s' % (self.template_name))
            return None

        template_definition = self.input_validator_handler.get_template_definition(self.template_name, template_category='vc')
        if template_definition is None:
            self.my_output.error('Template definition not found for template: %s' % (self.template_name))
            return None

        files_dir = os.path.join(template_dir, 'files')
        filename = os.path.join(
            files_dir,
            template_definition['main']['autoinstall_iso_create_script']
        )

        if not os.path.isfile(filename):
            self.my_output.error('Autoinstall iso create script not found: %s' % (filename))
            return None

        return filename

    def prepare_script(self, variables):
        script_filename = self.get_script_filename()
        if script_filename is None:
            self.my_output.error('Get script filename failed')
            return None

        content = self.template_handler.get_template(
            script_filename,
            variables,
            replace_variables_enabled=True,
            check_remaining_variables=False
        )
        if content is None:
            self.my_output.error('Script template failed')
            return None

        target_filename = '/tmp/%s' % (str(uuid.uuid4()))
        try:
            with open(target_filename, 'w', encoding='utf-8') as file_handler:
                file_handler.write(content)

        except BaseException:
            self.my_output.error('Failed to prepare local script')
            return None

        self.my_output.debug('Autoinstall preparation script')
        self.my_output.debug(content)

        return target_filename

    def prepare_user_data(self, user_data_filename, variables, replace_variables_enabled=True):
        user_data_content = self.template_handler.get_template(
            user_data_filename,
            variables,
            replace_variables_enabled=replace_variables_enabled
        )
        if user_data_content is None:
            self.my_output.error('User data preparation failed')
            return False

        user_data_filename = '/tmp/%s.user-data' % (str(uuid.uuid4()))
        try:
            with open(user_data_filename, 'w', encoding='utf-8', newline='\n') as file_handler:
                file_handler.write(user_data_content)

        except BaseException:
            self.my_output.error('Failed to save generated kickstart file: %s' % (user_data_filename))
            return None

        self.my_output.debug('User data')
        self.my_output.debug(user_data_content)

        return user_data_filename

    def make_iso_local(self, script_filename, user_data_filename):
        cmd = 'chmod a+x %s' % (script_filename)
        os.system(cmd)

        command = './%s -u %s' % (
            script_filename,
            user_data_filename
        )

        with subprocess.Popen(
            args=command.split(' '),
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True
        ) as process:
            output, error = process.communicate()

            if process.returncode > 0:
                self.my_output.error('Autoinstall preparation script failed')
                self.my_output.default(output.decode('utf-8'))
                self.my_output.default(error.decode('utf-8'))
                return False

            self.my_output.info('Autoinstall preparation script successful')
            self.my_output.debug(output.decode('utf-8'))

        return True

    def make_iso_remote(self, script_filename, user_data_filename, jump):
        ssh_handler = ssh.Ssh(
            jump['ip'],
            jump['username'],
            port=22,
            password=jump['password'],
            debug=self.debug
        )

        # Step 1: copy script

        success = ssh_handler.scp_file(script_filename, script_filename)
        if not success:
            self.my_output.error('Failed to copy autoinstall script file to remote host')
            return False
        self.my_output.debug('Copy autoinstall script file to remote host: %s' % (script_filename))

        cmd = 'dos2unix %s' % (script_filename)
        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to run dos2unix command: %s' % (cmd))
            return False

        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to run dos2unix command: %s' % (cmd))
            return False

        self.my_output.debug('Autoinstall script dos2unix changed')

        # Step 2: copy user data

        success = ssh_handler.scp_file(user_data_filename, user_data_filename)
        if not success:
            self.my_output.error('Failed to copy user data file to remote host')
            return False
        self.my_output.debug('Copy autoinstall user data file to remote host: %s' % (user_data_filename))

        cmd = 'dos2unix %s' % (user_data_filename)
        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to run dos2unix command: %s' % (cmd))
            return False

        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to run dos2unix command: %s' % (cmd))
            return False

        self.my_output.debug('User data dos2unix changed')

        # Step 3: execute script

        cmd = 'bash %s -u %s' % (
            script_filename,
            user_data_filename
        )
        success, output, error = ssh_handler.run_cmd(cmd, live_output=self.verbose)
        if not success:
            self.my_output.error('Autoinstall iso generation script failed: %s' % (cmd))
            return False

        self.my_output.debug('ISO generated and uploaded')
        return True

    def generate_iso(self, user_data_filename, variables, jump, replace_variables_enabled=True):
        user_data_filename = self.prepare_user_data(
            user_data_filename,
            variables,
            replace_variables_enabled=replace_variables_enabled
        )
        if user_data_filename is None:
            self.my_output.error('Iso generation failed on user data preparation')
            return False

        script_filename = self.prepare_script(variables)
        if script_filename is None:
            os.remove(user_data_filename)
            self.my_output.error('Iso generation failed on script preparation')
            return False

        my_os = platform.system()
        if my_os == 'Linux':
            if jump['enabled']:
                success = self.make_iso_remote(script_filename, user_data_filename, jump)

            if not jump['enabled']:
                success = self.make_iso_local(script_filename, user_data_filename)

        if my_os != 'Linux':
            if jump['enabled']:
                success = self.make_iso_remote(script_filename, user_data_filename, jump)

            if not jump['enabled']:
                self.my_output.error('Autoinstall iso generatation requires Linux')
                success = False

        os.remove(user_data_filename)
        os.remove(script_filename)

        return success
