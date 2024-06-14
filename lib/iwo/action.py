class IwoAction():
    def __init__(self):
        self.mo_action = {}

    def initialize_action(self, related_class):
        body = {}
        body['environmentType'] = 'HYBRID'
        body['detailLevel'] = 'EXECUTION'
        if related_class != 'all':
            body['relatedEntityTypes'] = [related_class]

        self.mo_action[related_class] = self.post(
            '/wo/api/v3/markets/Market/actions',
            body=body
        )
        if self.mo_action[related_class] is None:
            return False

        self.log.iwo_mo(
            'Action.%s.attributes' % (related_class),
            self.mo_action[related_class]
        )

        return True

    def get_action_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def match_action(self, action_info, match_rules):
        if match_rules is None or len(match_rules) == 0:
            return True

        match = False
        for match_rule in match_rules:
            if match_rule.startswith('target_id:'):
                if action_info['target']['uuid'] == match_rule[10:]:
                    match = True
                    break

        return match

    def get_actions(self, related_class='all', match_rules=None):
        if related_class not in self.mo_action:
            if not self.initialize_action(related_class):
                self.log.error(
                    'get_actions',
                    'Managed objects must be initialized first'
                )
                return None

        actions = []

        for managed_object in self.mo_action[related_class]:
            action_info = self.get_action_info(
                managed_object
            )
            if action_info is not None:
                if not self.match_action(action_info, match_rules):
                    continue

                actions.append(
                    action_info
                )

        self.log.iwo_mo(
            'Action.%s.info' % (related_class),
            actions
        )

        return actions

    def get_actions_summary(self, actions):
        action_types = {}
        for action_type in ['delete', 'move', 'provision', 'reconfigure', 'resize', 'scale', 'start', 'suspend']:
            action_types[action_type] = {}
            action_types[action_type]['count'] = 0

            action_types[action_type]['severity'] = {}
            action_types['severity'] = {}
            for severity in ['minor', 'major', 'critical']:
                action_types[action_type]['severity'][severity] = 0
                action_types['severity'][severity] = 0

            action_types[action_type]['category'] = {}
            action_types[action_type]['class'] = {}
            action_types[action_type]['mode'] = {}
            action_types[action_type]['environment'] = {}

        for action in actions:
            action_type = action['actionType'].lower()
            if action_type not in action_types:
                self.log.error(
                    'iwo.get_actions.summary',
                    'Unsupported action type: %s' % (action_type)
                )
                continue

            action_types[action_type]['count'] = action_types[action_type]['count'] + 1

            class_name = action['target']['className']
            if class_name not in action_types[action_type]['class']:
                action_types[action_type]['class'][class_name] = 0
            action_types[action_type]['class'][class_name] = action_types[action_type]['class'][class_name] + 1

            environment_name = action['target']['environmentType']
            if environment_name not in action_types[action_type]['environment']:
                action_types[action_type]['environment'][environment_name] = 0
            action_types[action_type]['environment'][environment_name] = action_types[action_type]['environment'][environment_name] + 1

            action_mode = action['actionMode']
            if action_mode not in action_types[action_type]['mode']:
                action_types[action_type]['mode'][action_mode] = 0
            action_types[action_type]['mode'][action_mode] = action_types[action_type]['mode'][action_mode] + 1

            severity = action['risk']['severity'].lower()
            action_types[action_type]['severity'][severity] = action_types[action_type]['severity'][severity] + 1
            action_types['severity'][severity] = action_types['severity'][severity] + 1

            category = action['risk']['subCategory']
            if category not in action_types[action_type]['category']:
                action_types[action_type]['category'][category] = 0
            action_types[action_type]['category'][category] = action_types[action_type]['category'][category] + 1

        return action_types

    def get_actions_summary_list(self, actions):
        action_types = self.get_actions_summary(
            actions
        )

        summary = []
        for action_name in action_types:
            if action_name in ['severity']:
                continue

            item = {}
            item['name'] = action_name
            item['count'] = action_types[action_name]['count']
            for key in ['severity', 'category', 'class', 'mode', 'environment']:
                item[key] = []
                for value in action_types[action_name][key]:
                    item[key].append(
                        '%s (%s)' % (
                            value,
                            action_types[action_name][key][value]
                        )
                    )
                if len(item[key]) == 0:
                    item[key].append('')
            summary.append(item)

        return summary

    def get_actions_severity_flag(self, actions):
        summary = self.get_actions_summary(actions)

        if summary['severity']['critical'] > 0:
            flag = 'Critical (%s)' % (summary['severity']['critical'])
            color = 'Red'
            return (flag, color)

        if summary['severity']['major'] > 0:
            flag = 'Major (%s)' % (summary['severity']['major'])
            color = 'Yellow'
            return (flag, color)

        if summary['severity']['minor'] > 0:
            flag = 'Minor (%s)' % (summary['severity']['minor'])
            color = 'Blue'
            return (flag, color)

        return ('Normal', 'Green')

    def get_action_severity_summary(self, managed_objects, empty_if_zero=True):
        if len(managed_objects) == 0:
            return ('-', '.')

        critical = 0
        major = 0
        minor = 0
        normal = 0
        for managed_object in managed_objects:
            if managed_object['risk']['severity'].lower() == 'critical':
                critical = critical + 1

            if managed_object['risk']['severity'].lower() == 'major':
                major = major + 1

            if managed_object['risk']['severity'].lower() == 'minor':
                minor = minor + 1

            if managed_object['risk']['severity'].lower() == 'normal':
                normal = normal + 1

        severity = '%s/%s/%s/%s' % (
            critical,
            major,
            minor,
            normal
        )

        color = ':'
        if critical == 0:
            color = '%s.' % (color)
        else:
            color = '%s%s' % (
                color,
                'R'.rjust(len(str(critical)), 'R')
            )
        color = '%s.' % (color)

        if major == 0:
            color = '%s.' % (color)
        else:
            color = '%s%s' % (
                color,
                'Y'.rjust(len(str(major)), 'Y')
            )
        color = '%s.' % (color)

        if minor == 0:
            color = '%s.' % (color)
        else:
            color = '%s%s' % (
                color,
                'B'.rjust(len(str(minor)), 'B')
            )
        color = '%s.' % (color)

        if normal == 0:
            color = '%s.' % (color)
        else:
            color = '%s%s' % (
                color,
                'G'.rjust(len(str(normal)), 'G')
            )

        return (severity, color)

    def get_actions_list(self, actions):
        actions_list = []
        for action in actions:
            info = {}
            info['__Output'] = {}
            info['severity'] = action['risk']['severity'].lower()
            info['__Output']['severity'] = self.map_severity_color(
                info['severity']
            )
            info['description'] = action['risk']['description']
            info['subCategory'] = action['risk']['subCategory']
            info['details'] = action['details']
            actions_list.append(info)
        return actions_list

    def print_actions_summary(self, actions):
        summary = self.get_actions_summary_list(
            actions
        )

        order = [
            'name',
            'count',
            'severity',
            'category',
            'class',
            'mode',
            'environment'
        ]

        headers = [
            'Name',
            'Count',
            'Severity',
            'Category',
            'Class',
            'Mode',
            'Environment'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                summary,
                order,
                ['severity', 'category', 'class', 'mode', 'environment']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )
