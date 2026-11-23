from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.storage_virtual_drive.info import StorageVirtualDriveInfo


class StorageVirtualDrive(IntersightCommon, StorageVirtualDriveInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage virtualdrive'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        StorageVirtualDriveInfo.__init__(self)

    def get_virtual_drives(self, compute_id, cache=True):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            match = False
            for ancestor in item['Ancestors']:
                if ancestor['ObjectType'] == 'compute.Board' and ancestor['Moid'] == compute_id:
                    match = True
                    break

                if ancestor['ObjectType'] == 'compute.Blade' and ancestor['Moid'] == compute_id:
                    match = True
                    break

            if match:
                disks.append(item)

        return disks
