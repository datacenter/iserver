class NodeSensorApi():
    def __init__(self):
        self.node_sensor_mo = None

    def get_node_sensor_mo(self):
        if self.node_sensor_mo is not None:
            return self.node_sensor_mo

        cache = self.get_object_cache(
            'eqptSensor'
        )
        if cache is not None:
            self.node_sensor_mo = cache
            self.log.apic_mo(
                'eqptSensor',
                self.node_sensor_mo
            )
            return self.node_sensor_mo

        managed_objects = self.get_class(
            'eqptSensor'
        )
        if managed_objects is None:
            self.log.error(
                'get_node_sensor_mo',
                'API failed'
            )
            return None

        self.node_sensor_mo = []
        for managed_object in managed_objects['imdata']:
            self.node_sensor_mo.append(
                managed_object['eqptSensor']['attributes']
            )

        self.log.apic_mo(
            'eqptSensor',
            self.node_sensor_mo
        )

        self.set_object_cache(
            'eqptSensor',
            self.node_sensor_mo
        )

        return self.node_sensor_mo
