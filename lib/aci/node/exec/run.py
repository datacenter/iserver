from lib import ssh


class NodeExecRun():
    def __init__(self):
        pass

    def node_run_show_command(self, node_id, command, debug=False, paranoid=False, attempts=3, ip_type='oob'):
        node_ip = self.get_node_mgmt_ip(node_id, ip_type=ip_type)
        if node_ip is None:
            self.log.error(
                'node_run_show_command',
                'Failed to get node mgmt ip: %s' % (node_id)
            )
            return None

        ssh_handler = ssh.Ssh(
            node_ip,
            self.apic_username,
            password = self.apic_password
        )

        attempt = 1
        while True:
            success, output, error = ssh_handler.run_cmd(
                command,
                timeout=60,
                debug=debug,
                paranoid=paranoid
            )

            if success:
                return output

            if attempt > attempts:
                self.log.error(
                    'node_run_show_command',
                    'Failed to rin command at %s: %s' % (node_id, command)
                )
                return None

            attempt += 1
