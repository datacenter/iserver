import json
from progress.bar import IncrementalBar

from lib.lcm_server.common import LcmServerCommon


class LcmServerTag(LcmServerCommon):
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

    def add_tags(self, tags, new_tags):
        for new_tag in new_tags:
            updated = False
            for tag in tags:
                if tag['Key'] == new_tag.split(':')[0]:
                    tag['Value'] = new_tag.split(':')[1]
                    updated = True

            if not updated:
                item = {}
                item['Key'] = new_tag.split(':')[0]
                item['Value'] = new_tag.split(':')[1]
                tags.append(
                    item
                )

        return tags

    def add(self, servers_mo, tags):
        commands = []
        for server_mo in servers_mo:
            target_tag = self.add_tags(
                server_mo['Tags'],
                tags
            )
            command = 'isctl update compute rackunit moid %s --Tags=\'%s\'' % (
                server_mo['Moid'],
                json.dumps(target_tag)
            )
            commands.append(command)
            if self.dry_run:
                self.my_output.default(command)

        if self.dry_run:
            return True

        bar_handler = IncrementalBar('Set tag request', max=len(commands))
        bar_handler.goto(0)
        for command in commands:
            if not self.isctl.update(command):
                self.my_output.error('Command failed: %s' % (command))
                return False
            bar_handler.next()
        bar_handler.finish()

        return True

    def delete_tags(self, tags, delete_tags):
        new_tags = []
        for tag in tags:
            if tag['Key'] == 'Intersight.LicenseTier':
                new_tags.append(tag)
                continue

            to_delete = False
            for delete_tag in delete_tags:
                if tag['Key'] == delete_tag.split(':')[0]:
                    to_delete = True
                    break

            if not to_delete:
                new_tags.append(
                    tag
                )

        return new_tags

    def delete(self, servers_mo, tags):
        commands = []
        for server_mo in servers_mo:
            target_tag = self.delete_tags(
                server_mo['Tags'],
                tags
            )
            command = 'isctl update compute rackunit moid %s --Tags=\'%s\'' % (
                server_mo['Moid'],
                json.dumps(target_tag)
            )
            commands.append(command)
            if self.dry_run:
                self.my_output.default(command)

        if self.dry_run:
            return True

        bar_handler = IncrementalBar('Set tag request', max=len(commands))
        bar_handler.goto(0)
        for command in commands:
            if not self.isctl.update(command):
                self.my_output.error('Command failed: %s' % (command))
                return False
            bar_handler.next()
        bar_handler.finish()

        return True
