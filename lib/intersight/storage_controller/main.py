from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.storage_controller.info import StorageControllerInfo


class StorageController(IntersightCommon, StorageControllerInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage controller'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        StorageControllerInfo.__init__(self)

    def get_board_storage_controllers(self, board_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        controllers = []

        for item in self.cache:
            if item['ComputeBoard'] is not None:
                if item['ComputeBoard']['Moid'] == board_id:
                    controllers.append(item)

        return controllers

    def get_blade_storage_controllers(self, blade_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        controllers = []

        for item in self.cache:
            if item['ComputeBlade'] is not None:
                if item['ComputeBlade']['Moid'] == blade_id:
                    controllers.append(item)
                    continue

            for ancestor in item['Ancestors']:
                if ancestor['ObjectType'] == 'compute.Blade' and ancestor['Moid'] == blade_id:
                    controllers.append(item)
                    continue

        return controllers
