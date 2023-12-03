import time

from lib import ssh


class ImcCommand():
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

    def run_commands(self, commands, max_attempts=1, prompt_sleep=10, command_sleep=10):
        success = True
        output = {}

        session = self.ssh_handler.create_session(max_attempts=max_attempts)
        if session is None:
            self.log.error(
                'run_commands',
                'Session create failed: %s@%s:%s pass:%s' % (
                    self.username,
                    self.endpoint_ip,
                    self.endpoint_port,
                    self.password
                )
            )

            return False, output

        chan = session.invoke_shell()

        chan.send('\n')
        chan.send('\n')
        time.sleep(prompt_sleep)
        response = chan.recv(9999)
        try:
            prompt = None
            lines = response.decode('utf-8').replace('\r\n', '\n').split('\n')
            for line in lines:
                if len(line) > 0:
                    prompt = line.strip().strip('\n')

            self.log.debug(
                'run_commands',
                'Prompt: %s' % (prompt)
            )
            if prompt is None:
                success = False
                self.log.error(
                    'run_commands',
                    'Prompt detection failed'
                )
                self.log.error(
                    'run_commands',
                    lines
                )

        except BaseException:
            success = False
            prompt = None
            self.log.error(
                'run_commands',
                'Prompt detection failed (traceback)'
            )

        if prompt is not None:
            for command in commands:
                chan.send(command)
                chan.send('\n')
                time.sleep(command_sleep)
                response = chan.recv(9999)
                try:
                    response = response.decode('utf-8').replace('\r\n', '\n')
                    command_output = []
                    for line in response.split('\n'):
                        line = line.strip()
                        if line == command:
                            continue
                        if line == prompt:
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

        session.close()

        return success, output
