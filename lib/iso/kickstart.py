import os
import sys
import uuid
import shutil
import platform

from lib import file_helper
from lib import output_helper
from lib import ssh
from lib import template


class IsoKickstart():
    def __init__(self, debug=False):
        self.my_output = output_helper.OutputHelper(debug=debug)
        self.template_handler = template.Template(debug=debug)

    def get_make_iso_script_filename(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        script_filename = os.path.abspath(
            os.path.join(
                main_dir, 'templates/iso/make-iso.sh'
            )
        )

        return script_filename

    def make_iso_local(self, ks_filename, iso_filename):
        if os.path.isfile(iso_filename):
            os.remove(iso_filename)

        # Step 1: copy iso script
        script_filename = self.get_make_iso_script_filename()
        if script_filename is None:
            self.my_output.error('Make iso script not found')
            return False

        target_script_filename = '/tmp/%s' % (os.path.basename(script_filename))
        shutil.copyfile(script_filename, target_script_filename)
        self.my_output.debug('Copy make iso script file to local host: %s' % (target_script_filename))

        # Step 2: set script file settings
        cmd = 'chmod a+x %s' % (target_script_filename)
        os.system(cmd)

        # Step 3: execute script
        target_iso_filename = '%s.iso' % (str(uuid.uuid4()))
        cmd = '%s -s %s -d %s >/dev/null 2>&1' % (
            target_script_filename,
            ks_filename,
            iso_filename
        )
        os.system(cmd)

        return os.path.isfile(iso_filename)

    def make_iso_remote(self, ks_filename, iso_filename, jump):
        ssh_handler = ssh.Ssh(
            jump['ip'],
            jump['username'],
            port=22,
            password=jump['password']
        )

        # Step 1: copy kickstart file
        target_ks_filename = os.path.basename(ks_filename)
        success = ssh_handler.scp_file(ks_filename, target_ks_filename)
        if not success:
            self.my_output.error('Failed to copy kickstart file to remote host')
            return False

        self.my_output.debug('Copy kickstart file to remote host: %s' % (target_ks_filename))

        # Step 2: copy iso script
        script_filename = self.get_make_iso_script_filename()
        if script_filename is None:
            self.my_output.error('Make iso script not found')
            return False

        target_script_filename = os.path.basename(script_filename)
        success = ssh_handler.scp_file(script_filename, target_script_filename)
        if not success:
            self.my_output.error('Failed to copy make iso script file to remote host')
            return False
        self.my_output.debug('Copy make iso script file to remote host: %s' % (target_script_filename))

        # Step 3: set script file settings
        cmd = 'chmod a+x %s' % (target_script_filename)
        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to set make iso script file flags')
            return False
        self.my_output.debug('Script mode changed')

        # Step 4: execute script
        target_iso_filename = '%s.iso' % (str(uuid.uuid4()))
        cmd = './%s -s %s -d %s' % (
            target_script_filename,
            target_ks_filename,
            target_iso_filename
        )
        success, output, error = ssh_handler.run_cmd(cmd)
        if not success:
            self.my_output.error('Failed to generate iso')
            return False
        self.my_output.debug('ISO generated: %s' % (target_iso_filename))

        # Step 5: download generated iso
        success = ssh_handler.scp_file(target_iso_filename, iso_filename, put=False)
        if not success:
            self.my_output.error('Failed to copy iso file from remote host')
            return False
        self.my_output.debug('Copy iso file to local host: %s' % (iso_filename))

        # Step 6: delete uploaded files

        for filename in [target_iso_filename, target_ks_filename, target_script_filename]:
            if not ssh_handler.delete_file(filename):
                self.my_output.error('Failed to delete remote file: %s' % (filename))

        return True

    def generate_iso(self, ks_template_filename, ks_attributes, iso_filename, jump):
        ks_template = self.template_handler.get_template(ks_template_filename, ks_attributes)
        if ks_template is None:
            return False

        ks_filename = '/tmp/%s.ks' % (str(uuid.uuid4()))
        try:
            with open(ks_filename, 'w', encoding='utf-8', newline='\n') as file_handler:
                file_handler.write(ks_template)
        except BaseException:
            self.my_output.error('Failed to save generated kickstart file: %s' % (ks_filename))
            return False

        my_os = platform.system()
        if my_os == 'Linux':
            success = self.make_iso_local(ks_filename, iso_filename)
            if not success:
                self.my_output.error('ISO generation failed')
                return False

        if my_os != 'Linux':
            if not jump['enabled']:
                self.my_output.error('Kickstart iso generatation requires Linux')
                return False

            success = self.make_iso_remote(ks_filename, iso_filename, jump)
            if not success:
                self.my_output.error('ISO generation failed')
                return False

        return True
