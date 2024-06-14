from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.storage_physical_disk.info import StoragePhysicalDiskInfo


class StoragePhysicalDisk(IntersightCommon, StoragePhysicalDiskInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'storage physicaldisk'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        StoragePhysicalDiskInfo.__init__(self)

    def get_compute_disks(self, compute_id, cache=True, disk_type=None):
        if cache:
            self.prepare_cache()
        else:
            self.cache = self.get_all()

        if self.cache is None:
            return None

        disks = []

        for item in self.cache:
            if disk_type is not None and item['Type'] != disk_type:
                continue

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
