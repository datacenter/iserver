from progress.bar import IncrementalBar

from lib.intersight.lcm.common import LcmServerCommon


class LcmServerPower(LcmServerCommon):
    def __init__(self, iaccount, wait=True, dry_run=False, silent=False, verbose=False, debug=False, log_id=None):
        self.dry_run = dry_run
        self.silent = silent
        self.wait = wait
        self.max_start_time = 30
        self.max_complete_time = 60
        self.verbose = verbose
        LcmServerCommon.__init__(
            self,
            iaccount,
            silent=silent,
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

    def power_task(self, servers_mo, power_state, workflow_name, label):
        target_servers_mo = []
        for server_mo in servers_mo:
            if 'ServerSettingId' not in server_mo:
                server_mo['ServerSettingId'] = self.get_server_setting_id(
                    server_mo['DeviceMoId']
                )
                if server_mo['ServerSettingId'] is None:
                    continue

            server_mo['attributes'] = 'moid %s --AdminPowerState %s' % (
                server_mo['ServerSettingId'],
                power_state
            )
            command = 'isctl create compute updatecomputeserversetting %s' % (server_mo['attributes'].replace(' --', '\n\t--'))
            self.my_output.info(command)
            if self.dry_run:
                self.my_output.default(command)

            target_servers_mo.append(
                server_mo
            )

        if self.dry_run:
            return True

        if self.wait:
            self.my_output.default('Collect workflow information...')
            servers = self.get_server_workflow_info(servers_mo)

        if self.silent:
            for server_mo in target_servers_mo:
                if not self.server_setting_handler.set(server_mo['attributes']):
                    self.my_output.error('Request failed: %s' % (server_mo['attributes']))
                    return False

        if not self.silent:
            bar_handler = IncrementalBar('%s request' % (label), max=len(target_servers_mo))
            bar_handler.goto(0)
            for server_mo in target_servers_mo:
                if not self.server_setting_handler.set(server_mo['attributes']):
                    self.my_output.error('Request failed: %s' % (server_mo['attributes']))
                    return False
                bar_handler.next()
            bar_handler.finish()
            self.my_output.files_only('%s request: [#######################] %s/%s' % (label, len(target_servers_mo), len(target_servers_mo)))

        success = True
        if self.wait:
            success = self.wait_workflows(
                servers,
                workflow_name,
                max_start_time=self.max_start_time,
                max_complete_time=self.max_complete_time,
                summary=True,
                details=self.verbose
            )

        return success

    def power_on(self, servers_mo):
        return self.power_task(servers_mo, 'PowerOn', 'Power On', 'Power On')

    def power_off(self, servers_mo):
        return self.power_task(servers_mo, 'PowerOff', 'Power Off', 'Power Off')

    def power_cycle(self, servers_mo):
        return self.power_task(servers_mo, 'PowerCycle', 'Power Cycle', 'Power Cycle')

    def power_hard(self, servers_mo):
        return self.power_task(servers_mo, 'HardReset', 'Hard Reset', 'Hard Reset')

    def power_reboot(self, servers_mo):
        return self.power_task(servers_mo, 'Reboot', 'Reboot Management Controller', 'Reboot Management Controller')

    def power_shut(self, servers_mo):
        return self.power_task(servers_mo, 'Shutdown', 'Shut Down OS', 'OS Shutdown')
