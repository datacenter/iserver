import subprocess
import traceback
import json
import os
import time
import platform

from lib import log_helper
from lib import iaccount_helper


class Isctl():
    def __init__(self, iaccount, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.iaccount = iaccount

        self.ia_handler = iaccount_helper.IntersightAccount()
        self.configuration = self.ia_handler.get_iaccount_configuration_filename(iaccount)

    def command_fixup_windows(self, command):
        escape_create = False
        escape_update = False
        if command.startswith('isctl create'):
            escape_create = True

        if command.startswith('isctl update'):
            escape_update = True

        command = command.replace('isctl ', 'isctl --config %s ' % (self.configuration))

        if escape_create:
            if '"' in command:
                # isctl create ippool pool --Name aaa --Organization default --IpV4Blocks "[{\"From\": \"10.1.1.10\", \"To\": \"10.1.1.14\"}]"
                command = command.replace('"', '\\"')
                command = command.replace('\'', '"')
                self.log.debug('isctl_helper.command_fixup_windows', command)

        if escape_update:
            if '\'' in command:
                # isctl create ippool pool --Name aaa --Organization default --IpV4Blocks "[{\"From\": \"10.1.1.10\", \"To\": \"10.1.1.14\"}]"
                command = command.replace('"', '\\"')
                command = command.replace('\'', '"')
                self.log.debug('isctl_helper.command_fixup_windows', command)

        return command

    def isctl_exec_windows(self, command, json_conversion=False, retry=3):
        try:
            command = self.command_fixup_windows(command)
            for i in range(0, retry):
                start = int(time.time() * 1000)
                with subprocess.Popen(
                    args=command,
                    stderr=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    shell=True,
                    env=os.environ
                ) as process:

                    output, error = process.communicate()
                    duration = int(time.time() * 1000) - start
                    if process.returncode == 0:
                        if json_conversion:
                            try:
                                output = json.loads(output.decode('utf-8'))
                            except BaseException:
                                return False, traceback.format_exc(), duration

                        return True, output, duration

                    time.sleep(3)

            return False, error, duration

        except BaseException:
            self.log.error('isctl_helper.isctl_exec', traceback.format_exc())
            return False, 'Exception', 0

    def command_fixup_linux(self, command):
        if 'isctl --config' not in command:
            command = command.replace('isctl ', 'isctl --config %s ' % (self.configuration))
        return command

    def isctl_exec_linux(self, command, json_conversion=False, retry=3):
        try:
            command = self.command_fixup_linux(command)
            for i in range(0, retry):
                start = int(time.time() * 1000)
                with subprocess.Popen(
                    args=command,
                    stderr=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    shell=True,
                    env=os.environ
                ) as process:

                    output, error = process.communicate()
                    duration = int(time.time() * 1000) - start
                    if process.returncode == 0:
                        if json_conversion:
                            try:
                                output = json.loads(output.decode('utf-8'))
                            except BaseException:
                                return False, traceback.format_exc(), duration

                        return True, output, duration

                    time.sleep(3)

            return False, error, duration

        except BaseException:
            self.log.error('isctl_helper.isctl_exec', traceback.format_exc())
            return False, 'Exception', None

    def isctl_exec(self, command, json_conversion=False, retry=3):
        my_os = platform.system()
        if my_os == 'Windows':
            return self.isctl_exec_windows(command, json_conversion=json_conversion, retry=retry)
        return self.isctl_exec_linux(command, json_conversion=json_conversion, retry=retry)

    def get(self, command, json_conversion=True, api_debug=False):
        success, response, duration = self.isctl_exec(
            command,
            json_conversion=json_conversion
        )
        if not success:
            self.log.cli(command, False, duration)
            try:
                self.log.error('isctl_helper.get', command)
                self.log.error('isctl_helper.get', response)
            except BaseException:
                pass
            return None

        item_count = None
        if json_conversion:
            if isinstance(response, dict):
                item_count = 1

            if isinstance(response, list):
                item_count = len(response)

        self.log.cli(
            command,
            True,
            duration,
            item_count=item_count
        )

        if api_debug:
            self.log.api(
                command,
                response
            )

        return response

    def create(self, command, get_response=False, json_conversion=True):
        if json_conversion:
            command = '%s -o json' % (command)

        success, response, duration = self.isctl_exec(
            command,
            json_conversion=json_conversion
        )
        if not success:
            self.log.cli(command, False, duration)
            try:
                self.log.error('isctl_helper.create', command)
                self.log.error('isctl_helper.create', response)
            except BaseException:
                pass

            if get_response:
                return dict(success=False, response=response)

            return False

        self.log.cli(command, True, duration)
        if get_response:
            return dict(success=True, response=response)

        return True

    def update(self, command):
        success, response, duration = self.isctl_exec(
            command,
            json_conversion=False
        )
        if not success:
            self.log.cli(command, False, duration)
            try:
                self.log.error('isctl_helper.update', command)
                self.log.error('isctl_helper.update', response)
            except BaseException:
                pass
            return False

        self.log.cli(command, True, duration)
        return True

    def delete(self, command):
        success, response, duration = self.isctl_exec(
            command,
            json_conversion=False
        )
        if not success:
            self.log.cli(command, False, duration)
            try:
                self.log.error('isctl_helper.delete', command)
                self.log.error('isctl_helper.delete', response)
            except BaseException:
                pass
            return False

        self.log.cli(command, True, duration)
        return True
