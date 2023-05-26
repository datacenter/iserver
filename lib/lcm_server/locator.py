from progress.bar import IncrementalBar

from lib.lcm_server.common import LcmServerCommon


class LcmServerLocator(LcmServerCommon):
    def __init__(self, iaccount, wait=True, dry_run=False, silent=False, verbose=False, debug=False, log_id=None):
        self.dry_run = dry_run
        self.wait = wait
        self.max_start_time = 30
        self.max_complete_time = 60
        LcmServerCommon.__init__(
            self,
            iaccount,
            silent=silent,
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

    def locator_task(self, servers, admin_state, workflow_name, label):
        for server in servers:
            server['attributes'] = 'moid %s --AdminLocatorLedState %s' % (
                server['ServerSettingId'],
                admin_state
            )
            command = 'isctl create compute updatecomputeserversetting %s' % (server['attributes'].replace(' --', '\n\t--'))
            self.my_output.info(command)
            if self.dry_run:
                self.my_output.default(command)

        if self.dry_run:
            return True

        bar_handler = IncrementalBar('%s request' % (label), max=len(servers))
        bar_handler.goto(0)
        for server in servers:
            if not self.server_setting_handler.set(server['attributes']):
                self.my_output.error('Request failed: %s' % (server['attributes']))
                return False
            bar_handler.next()
        bar_handler.finish()
        self.my_output.files_only('%s request: [#######################] %s/%s' % (label, len(servers), len(servers)))

        success = True
        if self.wait:
            success = self.wait_workflows(
                servers,
                workflow_name,
                max_start_time=self.max_start_time,
                max_complete_time=self.max_complete_time,
                summary=True
            )

        return success

    def locator_on(self, servers):
        return self.locator_task(servers, 'On', 'Turn On Locator', 'Locator On')

    def locator_off(self, servers):
        return self.locator_task(servers, 'Off', 'Turn Off Locator', 'Locator Off')
