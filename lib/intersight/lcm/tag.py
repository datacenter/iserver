import json
from progress.bar import IncrementalBar

from lib.intersight.lcm.common import LcmServerCommon
from lib import filter_helper


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

    def is_equal(self, tags_a, tags_b):
        if len(tags_a) != len(tags_b):
            return False

        for tag_a in tags_a:
            tag_match = False
            for tag_b in tags_b:
                if tag_a['Key'] == tag_b['Key']:
                    if tag_a['Value'] == tag_b['Value']:
                        tag_match = True
                        break

            if not tag_match:
                return False

        return True

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

            if server_mo['ObjectType'] == 'compute.RackUnit':
                command = 'isctl update compute rackunit moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tag)
                )

            if server_mo['ObjectType'] == 'compute.Blade':
                command = 'isctl update compute blade moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tag)
                )

            commands.append(command)
            if self.dry_run:
                self.my_output.default(command)

        if self.dry_run:
            return True

        bar_handler = IncrementalBar('Add tag request', max=len(commands))
        bar_handler.goto(0)
        for command in commands:
            if not self.isctl.update(command):
                self.my_output.error('Command failed: %s' % (command))
                return False
            bar_handler.next()
        bar_handler.finish()

        return True

    def delete_tags(self, tags, delete_tags, except_tags=None):
        new_tags = []
        for tag in tags:
            if tag['Key'] == 'Intersight.LicenseTier':
                new_tags.append(tag)
                continue

            if except_tags is not None:
                to_delete = True
                for except_tag in except_tags:
                    if filter_helper.match_string(except_tag.split(':')[0], tag['Key']):
                        if filter_helper.match_string(except_tag.split(':')[1], tag['Value']):
                            to_delete = False
                            new_tags.append(tag)

                if not to_delete:
                    continue

            to_delete = False
            for delete_tag in delete_tags:
                if filter_helper.match_string(delete_tag.split(':')[0], tag['Key']):
                    if filter_helper.match_string(delete_tag.split(':')[1], tag['Value']):
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

            if self.is_equal(server_mo['Tags'], target_tag):
                continue

            if server_mo['ObjectType'] == 'compute.RackUnit':
                command = 'isctl update compute rackunit moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tag)
                )

            if server_mo['ObjectType'] == 'compute.Blade':
                command = 'isctl update compute blade moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tag)
                )

            commands.append(command)
            if self.dry_run:
                self.my_output.default(command)

        if self.dry_run:
            return True

        bar_handler = IncrementalBar('Delete tag request', max=len(commands))
        bar_handler.goto(0)
        for command in commands:
            if not self.isctl.update(command):
                self.my_output.error('Command failed: %s' % (command))
                return False
            bar_handler.next()
        bar_handler.finish()

        return True

    def set(self, servers_mo, add_tags, delete_tags, except_tags):
        commands = []
        for server_mo in servers_mo:
            target_tags = self.delete_tags(
                server_mo['Tags'],
                delete_tags,
                except_tags=except_tags
            )

            target_tags = self.add_tags(
                target_tags,
                add_tags
            )

            if self.is_equal(server_mo['Tags'], target_tags):
                continue

            if server_mo['ObjectType'] == 'compute.RackUnit':
                command = 'isctl update compute rackunit moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tags)
                )

            if server_mo['ObjectType'] == 'compute.Blade':
                command = 'isctl update compute blade moid %s --Tags=\'%s\'' % (
                    server_mo['Moid'],
                    json.dumps(target_tags)
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
