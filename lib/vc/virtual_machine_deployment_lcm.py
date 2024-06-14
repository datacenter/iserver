import os
import time
import json
import traceback
import uuid

from lib import ssh
from lib import ip_helper
from lib import template
from lib.iso import kickstart
from lib.iso import autoinstall


class VcVirtualMachineDeploymentLcm():
    def __init__(self, log_id=None, verbose=False, debug=False):
        self.template_handler = template.Template(verbose=verbose, debug=debug)
        self.iso_kickstart_handler = kickstart.IsoKickstart()
        self.iso_autoinstall_handler = autoinstall.IsoAutoinstall(
            'ubuntu',
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        self.vm_parameters = None
        self.dry_run = False

    def set_vm_parameters(self, vm_parameters):
        self.vm_parameters = vm_parameters

    def is_iso_preparation_required(self):
        self.my_output.debug(
            'ISO parameters: %s' % (
                json.dumps(self.vm_parameters['iso'], indent=4)
            )
        )

        if not self.vm_parameters['iso']['enabled']:
            return False

        if self.vm_parameters['iso']['is_file'] and not self.vm_parameters['iso']['overwrite']:
            return False

        return True

    def prepare_iso(self):
        if not self.is_iso_preparation_required():
            self.my_output.info('ISO preparation not required')
            return True

        if not self.vm_parameters['iso']['is_folder']:
            self.my_output.default('Create data store folder: %s' % (self.vm_parameters['iso']['folder_name']))
            success = self.create_datastore_folder(
                self.vm_parameters['vcenter']['datacenter'],
                self.vm_parameters['vcenter']['datastore'],
                self.vm_parameters['iso']['folder_name']
            )
            if not success:
                self.my_output.error('Folder %s create failed' % (self.vm_parameters['iso']['folder_name']))
                return False
            self.my_output.default('Folder created: %s' % (self.vm_parameters['iso']['folder_name']))

        self.my_output.default('Upload iso: %s => [%s] %s/%s' % (
            self.vm_parameters['iso']['source'],
            self.vm_parameters['vcenter']['datastore'],
            self.vm_parameters['iso']['folder_name'],
            self.vm_parameters['iso']['file_name']
        ))
        success = self.create_datastore_file(
            self.vm_parameters['vcenter']['datacenter'],
            self.vm_parameters['vcenter']['datastore'],
            self.vm_parameters['iso']['source'],
            self.vm_parameters['iso']['folder_name'],
            self.vm_parameters['iso']['file_name']
        )
        if not success:
            self.my_output.error('Failed to create file: %s' % (self.vm_parameters['iso']['destination']))
            return False

        self.my_output.default('ISO ready: %s' % (self.vm_parameters['iso']['destination']))

        return True

    def is_ks_preparation_required(self):
        self.my_output.debug(
            'Kickstart parameters: %s' % (
                json.dumps(self.vm_parameters['ks'], indent=4)
            )
        )

        if not self.vm_parameters['ks']['enabled']:
            return False

        if self.vm_parameters['ks']['is_file'] and not self.vm_parameters['ks']['overwrite']:
            return False

        return True

    def prepare_kickstart(self):
        if self.vm_parameters['vm']['distribution'] not in ['centos', 'fedora', 'rhel']:
            return True

        if not self.is_ks_preparation_required():
            self.my_output.info('Kickstart iso preparation not required')
            return True

        if self.vm_parameters['ks']['generate']:
            success = self.iso_kickstart_handler.generate_iso(
                self.vm_parameters['ks']['template'],
                self.vm_parameters['variables'],
                self.vm_parameters['ks']['source'],
                self.vm_parameters['jump']
            )
            if not success:
                self.my_output.error('Kickstart iso generation failed')
                return None
            self.my_output.info('Kickstart iso generated: %s' % (self.vm_parameters['ks']['source']))

        if not self.vm_parameters['ks']['is_folder']:
            success = self.create_datastore_folder(
                self.vm_parameters['vcenter']['datacenter'],
                self.vm_parameters['vcenter']['datastore'],
                self.vm_parameters['ks']['folder_name']
            )
            if not success:
                self.my_output.error('Folder %s create failed' % (self.vm_parameters['ks']['folder_name']))
                return False
            self.my_output.default('Folder created: %s' % (self.vm_parameters['ks']['folder_name']))

        success = self.create_datastore_file(
            self.vm_parameters['vcenter']['datacenter'],
            self.vm_parameters['vcenter']['datastore'],
            self.vm_parameters['ks']['source'],
            self.vm_parameters['ks']['folder_name'],
            self.vm_parameters['ks']['file_name']
        )
        if not success:
            self.my_output.error('Failed to create file: %s' % (self.vm_parameters['ks']['destination']))
            return False

        self.my_output.default('Kickstart ready: %s' % (self.vm_parameters['ks']['destination']))

        return True

    def is_autoinstall_preparation_required(self):
        self.my_output.debug(
            'Kickstart parameters: %s' % (
                json.dumps(self.vm_parameters['ks'], indent=4)
            )
        )

        if not self.vm_parameters['ks']['enabled']:
            return False

        return True

    def prepare_autoinstall(self):
        if self.vm_parameters['vm']['distribution'] not in ['ubuntu']:
            return True

        if not self.is_autoinstall_preparation_required():
            self.my_output.info('Autoinstall iso preparation not required')
            return True

        if self.vm_parameters['ks']['is_file']:
            self.my_output.error('Autoinstall iso already exists...')
            return False

        self.my_output.default('Prepare autoinstall iso...')

        if not self.vm_parameters['ks']['is_folder']:
            success = self.create_datastore_folder(
                self.vm_parameters['vcenter']['datacenter'],
                self.vm_parameters['vcenter']['datastore'],
                self.vm_parameters['ks']['folder_name']
            )
            if not success:
                self.my_output.error('Folder %s create failed' % (self.vm_parameters['ks']['folder_name']))
                return False
            self.my_output.default('Folder created: %s' % (self.vm_parameters['ks']['folder_name']))

        success = self.iso_autoinstall_handler.generate_iso(
            self.vm_parameters['ks']['template'],
            self.vm_parameters['variables'],
            self.vm_parameters['jump'],
            replace_variables_enabled=self.vm_parameters['settings']['kickstart_template_variable_replacement_enabled']
        )
        if not success:
            self.my_output.error('Autoinstall iso generation failed')
            return False

        self.my_output.default('Autoinstall iso prepared: %s' % (self.vm_parameters['ks']['destination']))
        self.vm_parameters['ks']['is_file'] = True

        return True

    def create_vm_deployment(self, vm_parameters, screen_base_directory=None, dry_run=False):
        self.vm_parameters = vm_parameters
        self.dry_run = dry_run

        vm_name = self.vm_parameters['vm']['name']
        if self.is_vm(vm_name):
            self.my_output.info('VM already created: %s' % (vm_name))
        else:
            if not self.prepare_iso():
                return False

            if not self.prepare_kickstart():
                return False

            if not self.prepare_autoinstall():
                return False

            success = self.create_vm(self.vm_parameters['vm'], dry_run=self.dry_run)
            if not success:
                return False

        if self.dry_run:
            return True

        if self.is_vm_powered_on(vm_name):
            self.my_output.default('Virtual machine already powered on')
        else:
            success = self.power_on_vm(vm_name)
            if not success:
                return False

        if screen_base_directory is not None:
            self.my_output.default('Get initial screenshot...')
            screen_filename = '%s/initial.png' % (screen_base_directory)
            self.get_state(
                vm_name,
                screen_filename=screen_filename
            )

        if 'settings' in self.vm_parameters:
            if self.vm_parameters['settings']['sleep_after_vm_connected'] > 0:
                self.my_output.default('Extra wait time after connected state reached of %s seconds...' % (self.vm_parameters['settings']['sleep_after_vm_connected']))
                time.sleep(
                    self.vm_parameters['settings']['sleep_after_vm_connected']
                )

                if screen_base_directory is not None:
                    self.my_output.default('Get installation screenshot...')
                    screen_filename = '%s/install.png' % (screen_base_directory)
                    self.get_state(
                        vm_name,
                        screen_filename=screen_filename
                    )

        if self.vm_parameters['vm']['ssh']['enabled']:
            if not self.wait_ssh():
                return False

        if not self.run_tasks():
            return False

        if screen_base_directory is not None:
            self.my_output.default('Get final screenshot...')
            screen_filename = '%s/final.png' % (screen_base_directory)

            vm_state = self.get_state(
                vm_name,
                screen_filename=screen_filename
            )

        return True

    def wait_ssh(self, timeout=3600):
        self.my_output.default(
            'Wait for SSH access %s using (%s, %s) credentials with %s seconds timeout' % (
                self.vm_parameters['vm']['ssh']['ip'],
                self.vm_parameters['vm']['ssh']['username'],
                self.vm_parameters['vm']['ssh']['password'],
                timeout
            )
        )

        ssh_handler = ssh.Ssh(
            self.vm_parameters['vm']['ssh']['ip'],
            self.vm_parameters['vm']['ssh']['username'],
            password=self.vm_parameters['vm']['ssh']['password']
        )

        if not ssh_handler.wait_ssh(timeout):
            self.my_output.error('SSH timed out')
            return False

        return True

    def wait_connected(self, timeout=120, extra_wait=30):
        if self.vm_parameters['settings']['wait_vm_connected']:
            self.my_output.default('Wait for VM connected state with %s seconds timeout...' % (timeout))
            start_time = int(time.time())
            while True:
                vm_state = self.get_state(self.vm_parameters['vm']['name'])
                if vm_state['connectionState'] == 'connected':
                    break

                if int(time.time()) - start_time > timeout:
                    self.my_output.error('VM connection state did not reach connected in time')
                    return False

                time.sleep(5)

        time.sleep(extra_wait)
        return True

    def run_task_script(self, script_filename, live_output=False):
        ssh_handler = ssh.Ssh(
            self.vm_parameters['vm']['ssh']['ip'],
            self.vm_parameters['vm']['ssh']['username'],
            password=self.vm_parameters['vm']['ssh']['password']
        )

        self.my_output.default('Run script', underline=True, before_newline=True, after_newline=True)
        self.my_output.default('Script filename: %s\n' % (script_filename))

        content = self.template_handler.get_template(
            script_filename,
            self.vm_parameters['variables']
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
        if not ssh_handler.scp_file(source_filename, destination_filename):
            self.my_output.error(
                'Script upload failed: %s => %s' % (
                    source_filename,
                    destination_filename
                )
            )
            return False
        self.my_output.debug('Script uploaded: %s' % (destination_filename))

        if not ssh_handler.set_file_chmod(destination_filename, '755'):
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

        success, output, error = ssh_handler.run_cmd(
            './%s' % (destination_filename),
            live_output=live_output
        )

        if success:
            self.my_output.debug('Remote script execution finished')

            if not live_output:
                self.my_output.debug('~~~ script output ~~~')
                self.my_output.debug(output)
                self.my_output.debug('~~~~~~~~~~~~~~~~~~~~~')

            if not ssh_handler.delete_file(destination_filename):
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

    def run_task_file(self, file_info, create_directory=False):
        ssh_handler = ssh.Ssh(
            self.vm_parameters['vm']['ssh']['ip'],
            self.vm_parameters['vm']['ssh']['username'],
            password=self.vm_parameters['vm']['ssh']['password']
        )

        self.my_output.default('Copy file', underline=True, before_newline=True, after_newline=True)
        source_filename = file_info['source']
        destination_filename = file_info['destination']
        destination_directory = os.path.dirname(destination_filename)
        destination_chmod = file_info['chmod']
        self.my_output.debug('Source: %s' % (source_filename))
        self.my_output.debug('Destination: %s' % (destination_filename))
        self.my_output.debug('Template: %s' % (file_info['template']))
        self.my_output.debug('Target chmod: %s\n' % (destination_chmod))

        if file_info['template']:
            content = self.template_handler.get_template(
                source_filename,
                self.vm_parameters['variables']
            )
            if content is None:
                return False

            self.my_output.debug('~~~ file content ~~~')
            self.my_output.debug(content)
            self.my_output.debug('~~~~~~~~~~~~~~~~~~~~')

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

            self.my_output.debug('Local file prepared with variables replaced: %s' % (source_filename))

        self.my_output.default('Copy file: %s => %s' % (source_filename, destination_filename))

        if not os.path.isfile(source_filename):
            self.my_output.error('Local file not found: %s' % (source_filename))
            return False
        self.my_output.info('Local file found: %s' % (source_filename))

        source_md5 = ip_helper.get_file_md5(source_filename)
        self.my_output.debug('Local file checksum: %s' % (source_md5))
        destination_md5 = ssh_handler.get_file_md5(destination_filename)
        self.my_output.debug('Remote file checksum: %s' % (destination_md5))
        if source_md5 == destination_md5:
            self.my_output.default('Checksum (md5) match and upload skipped')
        else:
            if create_directory:
                if not ssh_handler.create_directory(destination_directory):
                    self.my_output.error('Directory create failed: %s' % (destination_directory))
                    return False
            self.my_output.debug('File upload...')
            if not ssh_handler.scp_file(source_filename, destination_filename):
                self.my_output.error('File upload failed')
                return False
            self.my_output.debug('File upload completed')

        if not ssh_handler.set_file_chmod(destination_filename, destination_chmod):
            self.my_output.error('File chmod failed: %s' % (destination_filename))
            return False

        self.my_output.debug('File chmod set to %s' % (destination_chmod))
        self.my_output.debug('Task file copy completed')

        return True

    def run_task_command(self, command):
        self.my_output.default('Run command', underline=True, before_newline=True)
        self.my_output.default('Command: %s' % (command))

        ssh_handler = ssh.Ssh(
            self.vm_parameters['vm']['ssh']['ip'],
            self.vm_parameters['vm']['ssh']['username'],
            password=self.vm_parameters['vm']['ssh']['password']
        )

        success, output, error = ssh_handler.run_cmd(command)
        if success:
            self.my_output.default('Command successful')
            if output is not None and len(output) > 0:
                self.my_output.debug('~~~ command output ~~~')
                self.my_output.debug(output)
                self.my_output.debug('~~~~~~~~~~~~~~~~~~~~~')

        if not success:
            self.my_output.error('Command failed')
            self.my_output.default('~~~ command output ~~~')
            self.my_output.default(error)
            self.my_output.default('~~~~~~~~~~~~~~~~~~~~~')

        return success

    def run_task(self, task_filename):
        self.my_output.default('Task: %s' % (task_filename), underline=True)

        task_definition = self.template_handler.get_template(
            task_filename,
            self.vm_parameters['variables'],
            yaml_conversion=True
        )

        if task_definition is None:
            return False

        for task in task_definition['tasks']:
            for key in task:
                if key == 'scripts':
                    for script_name in task[key]:
                        script_filename = os.path.join(
                            os.path.dirname(task_filename),
                            script_name
                        )
                        if not self.run_task_script(script_filename):
                            return False

                if key == 'files':
                    for file_info in task[key]:
                        if '/' in file_info['source'] or '\\' in file_info['source']:
                            pass
                        else:
                            file_info['source'] = os.path.join(
                                os.path.dirname(task_filename),
                                file_info['source']
                            )
                        if not self.run_task_file(file_info):
                            return False

                if key == 'commands':
                    for item in task[key]:
                        if not self.run_task_command(item):
                            return False

        return True

    def run_tasks(self):
        if 'tasks' not in self.vm_parameters or len(self.vm_parameters['tasks']) == 0:
            return True

        if not self.vm_parameters['vm']['ssh']['enabled']:
            self.my_output.error('Tasks configured but ssh not enabled')
            return False

        for task_filename in self.vm_parameters['tasks']:
            if not self.run_task(task_filename):
                return False

        return True

    def check_vm_network_devices(self):
        vm_name = self.vm_parameters['vm']['name']
        network_devices = self.get_network_devices_info(vm_name)
        if network_devices is None:
            self.my_output.error('No network device found')
            return False

        if not self.is_network_devices_connected(vm_name):
            network_devices = self.get_network_devices_info(vm_name)
            self.print_network_devices(network_devices)

        return True

    def delete_vm_deployment(self, parameters):
        name = parameters['vm']['name']

        if not self.is_vm(name):
            self.my_output.default('Virtual machine does not exist: %s' % (name))
        else:
            if not self.power_off_vm(name):
                return False

            if not self.destroy_vm(name):
                return False

        if 'ks' in parameters and parameters['ks']['enabled']:
            datacenter_name = parameters['vcenter']['datacenter']
            datastore_name = parameters['vcenter']['datastore']
            kickstart_folder = parameters['ks']['folder_name']
            kickstart_filename = parameters['ks']['file_name']
            kickstart_path = parameters['ks']['destination']
            if not self.is_datastore_file(datacenter_name, datastore_name, kickstart_folder, kickstart_filename):
                self.my_output.default('Kickstart does not exist: %s @ %s' % (kickstart_path, datastore_name))
            else:
                if not self.delete_datastore_file(datacenter_name, datastore_name, kickstart_path):
                    self.my_output.error('Kickstart delete failed: %s' % (kickstart_path))
                    return False

                self.my_output.default('Kickstart deleted: %s' % (kickstart_path))

        return True
