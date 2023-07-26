from lib.intersight import compute_blade
from lib.intersight import equipment_chassis

from lib import filter_helper
from lib import output_helper


class ChassizInfo():
    """Class for intersight chassis objects
    """
    def __init__(self, iaccount, log_id=None):
        self.chassis_handler = equipment_chassis.EquipmentChassis(iaccount, log_id=log_id)
        self.chassis_handler.set_get_expand('RegisteredDevice')
        self.blade_handler = compute_blade.ComputeBlade(iaccount, log_id=log_id)

        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def add_chassis_info(self, info):
        info['__Output'] = {}
        info['BladeCount'] = len(info['Blades'])

        if info['AlarmSummary']['Warning'] == 0 and info['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Healthy'
            info['HealthSummary'] = 'Healthy'
            info['__Output']['Health'] = 'Green'
            info['__Output']['HealthSummary'] = 'Green'
        if info['AlarmSummary']['Warning'] > 0 and info['AlarmSummary']['Critical'] == 0:
            info['Health'] = 'Warnings'
            info['HealthSummary'] = 'Warnings (%s)' % (info['AlarmSummary']['Warning'])
            info['__Output']['Health'] = 'Yellow'
            info['__Output']['HealthSummary'] = 'Yellow'
        if info['AlarmSummary']['Critical'] > 0:
            info['Health'] = 'Critical'
            info['HealthSummary'] = 'Critical (%s)' % (info['AlarmSummary']['Critical'])
            info['__Output']['Health'] = 'Red'
            info['__Output']['HealthSummary'] = 'Red'

        info['UcsDomain'] = ''
        if 'DeviceHostname' in info['RegisteredDevice']:
            info['UcsDomain'] = info['RegisteredDevice']['DeviceHostname'][0]

        for blade in info['Blades']:
            if blade['ObjectType'] == 'compute.Blade':
                blade_info = self.blade_handler.get_info(
                    blade['Moid']
                )
                if blade_info is not None:
                    for key in blade_info:
                        blade[key] = blade_info[key]

                if blade['PowerOn']:
                    blade['powerOnTick'] = '\u2713'
                    blade['__Output']['powerOnTick'] = 'Green'
                else:
                    blade['powerOnTick'] = '\u2717'
                    blade['__Output']['powerOnTick'] = 'Red'

        info['Blades'] = sorted(
            info['Blades'],
            key=lambda i: i['SlotId']
        )

        return info

    def match_chassis_blade(self, blade_info, blade_filter):
        if 'bname' in blade_filter:
            if len(blade_filter['bname']) > 0:
                if not filter_helper.match_string(blade_filter['bname'], blade_info['Name']):
                    return False

        if 'bserial' in blade_filter:
            if len(blade_filter['bserial']) > 0:
                if not filter_helper.match_string(blade_filter['bserial'], blade_info['Serial']):
                    return False

        if 'bmodel' in blade_filter:
            if len(blade_filter['bmodel']) > 0:
                if not filter_helper.match_string(blade_filter['bmodel'], blade_info['Model']):
                    return False

        return True

    def match_chassis_blades(self, blades_info, blade_filter):
        matched = False
        for blade_info in blades_info:
            matched = matched or self.match_chassis_blade(blade_info, blade_filter)
        return matched

    def get(self, match_rules=None):
        if match_rules is None:
            all_chassiz = self.chassis_handler.get_all()
        else:
            all_chassiz = self.chassis_handler.filter(
                name_filter=match_rules['name'],
                serial_filter=match_rules['serial'],
                model_filter=match_rules['model']
            )

        chassiz = []
        for chassis in all_chassiz:
            chassis = self.add_chassis_info(
                chassis
            )

            if match_rules is None:
                chassiz.append(
                    chassis
                )

            if match_rules is not None and self.match_chassis_blades(chassis['Blades'], match_rules):
                chassiz.append(
                    chassis
                )

        chassiz = sorted(
            chassiz,
            key=lambda i: i['Name']
        )

        return chassiz

    def print(self, info, title=False):
        if title:
            self.my_output.default(
                'Chassis [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'Name',
            'HealthSummary',
            'Model',
            'Serial',
            'UcsDomain',
            'Blades.Name',
            'Blades.Health',
            'Blades.Model',
            'Blades.Serial',
            'Blades.SlotId',
            'Blades.powerOnTick'
        ]

        headers = [
            'Name',
            'Health',
            'Model',
            'Serial',
            'UCS Domain',
            'Blade',
            'Health',
            'Model',
            'Serial',
            'Slot',
            'Power'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['Blades']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
