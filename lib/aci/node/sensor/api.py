class NodeSensorApi():
    def __init__(self):
        self.nodes_sensor_mo = None

    def get_nodes_sensor_mo(self):
        if self.nodes_sensor_mo is not None:
            return self.nodes_sensor_mo

        managed_objects = self.get_class(
            'eqptSensor'
        )
        if managed_objects is None:
            self.log.error(
                'get_nodes_sensor_mo',
                'API failed'
            )
            return None

        self.nodes_sensor_mo = []
        for managed_object in managed_objects['imdata']:
            self.nodes_sensor_mo.append(
                managed_object['eqptSensor']['attributes']
            )

        self.log.apic_mo(
            'eqptSensor',
            self.nodes_sensor_mo
        )

        return self.nodes_sensor_mo
