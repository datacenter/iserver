class ComputeServerSettingInfo():
    def __init__(self):
        pass

    def get_by_device_moid(self, device_moid, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        for item in self.cache:
            if item['DeviceMoId'] == device_moid:
                return item

        return None

    def get_id_by_device_moid(self, device_moid, cache=True):
        item = self.get_by_device_moid(device_moid, cache=cache)
        if item is not None:
            return item['Moid']
        return None
