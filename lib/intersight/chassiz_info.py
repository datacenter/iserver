from lib.intersight import equipment_chassis

from lib import output_helper


class ChassizInfo():
    """Class for intersight chassis objects
    """
    def __init__(self, iaccount, log_id=None):
        self.chassis_handler = equipment_chassis.EquipmentChassis(iaccount, log_id=log_id)
        self.chassis_handler.set_get_expand('RegisteredDevice')
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def get(self, match_rules=None):
        if match_rules is None:
            chassiz = self.chassis_handler.get_all()
        else:
            chassiz = self.chassis_handler.filter(
                name_filter=match_rules['name'],
                serial_filter=match_rules['serial'],
                model_filter=match_rules['model']
            )

        return chassiz

    def print(self, chassiz, legend_on=True, base_output=False):
        chassiz = sorted(chassiz, key=lambda i: i['Name'])

        summary = []
        for chassis in chassiz:
            summary.append(self.chassis_handler.get_summary(chassis))

        order = [
            'Name',
            'HealthSummary',
            'Model',
            'Serial',
            'UcsDomain',
            'Blades'
        ]

        headers = [
            'Name',
            'Health',
            'Model',
            'Serial',
            'UCS Domain',
            'Blades'
        ]

        self.my_output.my_table(
            summary,
            order=order,
            headers=headers,
            table=True
        )
