# pylint: disable=no-name-in-module
from pyVmomi import vim


class VcVmFolder():
    def __init__(self):
        pass

    def is_vm_folder(self, folder_name):
        folders = self.get_folders()
        if folders is None:
            return False

        for folder in folders:
            if folder['name'] == folder_name:
                return True

        return False

    def get_folders(self):
        if not self.vc_connect():
            return None

        folders = []
        content = self.vc_service_instance.RetrieveContent()

        # Get the list of all datacenters we have available to us
        folders_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Folder],
            True
        )

        for folder_obj in folders_object_view.view:
            folder = {}
            folder['name'] = folder_obj.name
            folders.append(folder)

        return folders

    def get_folder_object(self, folder_name):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        folders_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Folder],
            True
        )

        for folder_obj in folders_object_view.view:
            if folder_obj.name == folder_name:
                folders_object_view.Destroy()
                return folder_obj

        folders_object_view.Destroy()

        return None
