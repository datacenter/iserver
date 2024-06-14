import time

from lib import filter_helper
from lib import ssh


class ImcCliCommand():
    def __init__(self, endpoint_ip, endpoint_port, username, password, log_id):
        self.ssh_handler = ssh.Ssh(
            endpoint_ip,
            username,
            port=endpoint_port,
            password=password,
            endpoint_type='cisco',
            timeout=30,
            log_id=log_id
        )

        self.session = None
        self.shell = None
        self.prompt = None

    def __del__(self):
        if self.session is not None:
            self.session.close()

    def is_cli_ready(self):
        session = self.ssh_handler.create_session(max_attempts=1)
        if session is None:
            return False

        try:
            chan = session.invoke_shell()
        except BaseException:
            return False

        session.close()
        return True

    def create_session(self, max_attempts=1):
        if self.session is not None:
            return True

        self.session = self.ssh_handler.create_session(max_attempts=max_attempts)
        if self.session is None:
            self.log.error(
                'create_session',
                'Session create failed: %s@%s:%s pass:%s' % (
                    self.username,
                    self.endpoint_ip,
                    self.endpoint_port,
                    self.password
                )
            )

            return False

        return True

    def set_prompt(self, prompt_sleep=10):
        if self.prompt is not None:
            return True

        success = True
        self.shell = self.session.invoke_shell(
            height=1000
        )

        response = ''
        for index in range(0, prompt_sleep):
            time.sleep(1)
            response = response + self.shell.recv(9999).decode('utf-8')
            response = response.strip()
            if response.endswith('#'):
                break

        try:
            self.prompt = None
            lines = response.replace('\r\n', '\n').split('\n')
            for line in lines:
                if len(line) > 0:
                    self.prompt = line.strip().strip('\n')

            if self.prompt is None:
                success = False
                self.log.error(
                    'set_prompt',
                    'Prompt detection failed'
                )

            self.prompt = self.prompt.split('#')[0]

            self.log.debug(
                'set_prompt',
                'Prompt: %s' % (self.prompt)
            )
        except BaseException:
            success = False
            self.prompt = None
            self.log.error(
                'set_prompt',
                'Prompt detection failed (traceback)'
            )

        return success

    def run_commands(self, commands, max_attempts=1, prompt_sleep=10, command_sleep=10, continue_prompt=False):
        success = True
        output = {}

        if not self.create_session(max_attempts=max_attempts):
            return False, output

        if not self.set_prompt(prompt_sleep=prompt_sleep):
            return False, output

        for command in commands:
            self.shell.send(command)
            self.shell.send('\n')

            response = ''
            for index in range(0, command_sleep):
                time.sleep(1)
                command_response = self.shell.recv(9999)
                if command_response is None:
                    continue

                response = response + command_response.decode('utf-8').replace('\r\n', '\n')
                last_line = response.split('\n')[-1].strip()
                if last_line.startswith(self.prompt) and last_line.endswith('#'):
                    break

                if 'Do you want to continue?[y|N]' in last_line:
                    self.log.debug(
                        'run_commands',
                        'Detected confirmation requst: %s' % (last_line)
                    )
                    if continue_prompt:
                        self.shell.send('y')
                        self.shell.send('\n')
                        self.log.debug(
                            'run_commands',
                            'Confirmation: y'
                        )
                    else:
                        self.shell.send('N')
                        self.shell.send('\n')
                        self.log.debug(
                            'run_commands',
                            'Confirmation: N'
                        )
                    break

            try:
                command_output = []
                for line in response.split('\n'):
                    line = line.strip()
                    if line == command:
                        continue
                    if line.startswith(self.prompt) and line.endswith('#'):
                        continue

                    command_output.append(line)

                output[command] = '\n'.join(command_output)

                self.log.debug(
                    'run_commands',
                    'Command successful: %s' % (command)
                )
                self.log.debug(
                    'run_commands',
                    output[command]
                )

            except BaseException:
                output[command] = None
                self.log.error(
                    'run_commands',
                    'Command failed: %s' % (command)
                )

        return success, output

    def goto_top(self):
        self.run_commands(['top'])

    def set_scope(self, scope):
        commands = []
        commands.append('top')
        for item in scope.split(','):
            commands.append('scope %s' % (item))
        self.run_commands(commands)

    def parse_list(self, output, delimiter, item_key, method='all'):
        items = []
        item = None
        for line in output.split('\n'):
            new_section = False
            if line.startswith(delimiter):
                new_section = True
            else:
                if '__INDEX__' in delimiter:
                    (before_index, after_index) = delimiter.split('__INDEX__')
                    if line.startswith(before_index) and line.endswith(after_index):
                        try:
                            middle = int(line[len(before_index):][:-len(after_index)])
                            new_section = True
                        except BaseException:
                            middle = None

            if new_section:
                if item is not None:
                    items.append(
                        item
                    )

                item = {}
                if item_key is not None:
                    if method == 'all':
                        item[item_key] = line
                    if method == 'last word':
                        item[item_key] = line.split(':')[0].split(' ')[-1]

                continue

            if len(line.split(':')) == 2:
                key = line.split(':')[0].strip()
                value = line.split(':')[1].strip()
                if item is not None:
                    item[key] = value

        if item is not None:
            items.append(
                item
            )

        return items

    def parse_dict(self, output, start=None, ignore_keys=None, ignore_start=None):
        started = False
        if start is None:
            started = True

        items = {}
        for line in output.split('\n'):
            if not started:
                if not filter_helper.match_string('%s*' % (start), line.strip()):
                    continue
                started = True
                continue

            if len(line.split(':')) == 2:
                key = line.split(':')[0].strip()
                value = line.split(':')[1].strip()

                if ignore_keys is not None:
                    ignore = False
                    for ignore_key in ignore_keys:
                        if filter_helper.match_string('%s*' % (ignore_key), key):
                            ignore = True
                            break

                    if ignore:
                        continue

                if ignore_start is not None:
                    if filter_helper.match_string('%s*' % (ignore_start), key):
                        break

                items[key] = value

        return items

    def show_dict(self, command, scope=None, start=None, top=True, ignore_keys=None, ignore_start=None):
        commands = []
        if top:
            commands.append('top')

        if scope is not None:
            for item in scope.split(','):
                commands.append('scope %s' % (item))

        commands.append(
            command
        )

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        response = self.parse_dict(
            output[command],
            start=start,
            ignore_keys=ignore_keys,
            ignore_start=ignore_start
        )

        return response

    def show_list(self, command, delimiter, key, method='all', scope=None, top=True):
        commands = []
        if top:
            commands.append('top')

        if scope is not None:
            commands.append('scope %s' % (scope))

        commands.append(
            command
        )

        success, output = self.run_commands(
            commands
        )

        if not success:
            return None

        response = self.parse_list(
            output[command],
            delimiter,
            key,
            method=method
        )

        return response
