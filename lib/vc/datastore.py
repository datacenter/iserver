import os
import traceback
import requests

# pylint: disable=no-name-in-module
from pyVmomi import vim

# mypy: ignore-errors
requests.packages.urllib3.disable_warnings()


class VcDatastore():
    def __init__(self):
        self.datastore_info_cache = {}

    def is_datastore(self, datacenter_name, datastore_name):
        datastores = self.get_datastores()
        if datastores is None:
            return False

        for datastore in datastores:
            if datastore['dc'] == datacenter_name:
                if datastore['name'] == datastore_name:
                    return True

        return False

    def get_datastore_info(self, datastore_obj):
        if datastore_obj in self.datastore_info_cache:
            return self.datastore_info_cache[datastore_obj]

        info = {}
        try:
            info['name'] = datastore_obj.name
            if getattr(datastore_obj.info, 'nas', None) is not None:
                info['type'] = datastore_obj.info.nas.type
                info['capacity'] = datastore_obj.info.nas.capacity
                info['capacity_unit'] = self.convert_storage(datastore_obj.info.nas.capacity)
            if getattr(datastore_obj.info, 'vmfs', None) is not None:
                info['type'] = datastore_obj.info.vmfs.type
                info['capacity'] = datastore_obj.info.vmfs.capacity
                info['capacity_unit'] = self.convert_storage(datastore_obj.info.vmfs.capacity)
            info['free'] = datastore_obj.info.freeSpace
            info['free_unit'] = self.convert_storage(datastore_obj.info.freeSpace)
            info['used'] = info['capacity'] - info['free']
            info['usage_pct'] = round(
                info['used'] * 100 / info['capacity'],
                2
            )
            info['usage_unit'] = self.convert_pct(info['usage_pct'])
        except BaseException:
            info = None

        self.datastore_info_cache[datastore_obj] = info
        return info

    def get_datastore_object(self, datacenter_name, datastore_name):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        datacenters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Datacenter],
            True
        )

        for dc_obj in datacenters_object_view.view:
            if dc_obj.name == datacenter_name:
                datastores_object_view = content.viewManager.CreateContainerView(
                    dc_obj,
                    [vim.Datastore],
                    True
                )

                for ds_obj in datastores_object_view.view:
                    if ds_obj.info.name == datastore_name:
                        datacenters_object_view.Destroy()
                        datastores_object_view.Destroy()
                        return ds_obj

                datastores_object_view.Destroy()

        datacenters_object_view.Destroy()

        return None

    def get_datastores(self, datacenter_name=None):
        if not self.vc_connect():
            return None

        datastores = []
        content = self.vc_service_instance.RetrieveContent()

        # Get the list of all datacenters we have available to us
        datacenters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Datacenter],
            True
        )

        for dc_obj in datacenters_object_view.view:
            if datacenter_name is not None and dc_obj.name != datacenter_name:
                continue

            datastores_object_view = content.viewManager.CreateContainerView(
                dc_obj,
                [vim.Datastore],
                True
            )

            for ds_obj in datastores_object_view.view:
                datastore = self.get_datastore_info(ds_obj)
                datastore['dc'] = dc_obj.name
                datastores.append(datastore)

            datastores_object_view.Destroy()

        datacenters_object_view.Destroy()

        return datastores

    def print_datastores(self, datastores):
        if datastores is None or len(datastores) == 0:
            self.my_output.default('No datastores found')
            return

        self.my_output.my_table(
            datastores,
            order=[
                'dc',
                'name',
                'type',
                'capacity_unit',
                'free_unit',
                'usage_unit'
            ],
            headers=[
                'Datacenter',
                'Datastore',
                'Type',
                'Capacity',
                'Free',
                'Usage'
            ],
            table=True
        )

    def get_datastore_folders(self, datacenter_name, datastore_name, folder_name):
        ds_obj = self.get_datastore_object(datacenter_name, datastore_name)
        if ds_obj is None:
            return None

        spec = vim.host.DatastoreBrowser.SearchSpec(query=[vim.host.DatastoreBrowser.FolderQuery()])
        spec.details = vim.host.DatastoreBrowser.FileInfo.Details(
            fileOwner=True, fileSize=True, fileType=True, modification=True
        )
        search_path = '[%s] %s' % (datastore_name, folder_name)

        task = ds_obj.browser.SearchDatastoreSubFolders_Task(
            search_path,
            spec
        )
        self.wait_for_tasks([task])
        search_results = task.info.result

        folders = []
        for search_result in search_results:
            folder_path = self.fixup_datastore_path(
                search_result.folderPath
            )
            if folder_path != search_path:
                continue

            for folder_info in search_result.file:
                folder_details = {}
                folder_details['type'] = 'Folder'
                folder_details['datastore'] = datastore_name
                folder_details['folder'] = folder_name
                folder_details['filename'] = folder_info.path
                folder_details['path'] = '[%s] %s%s' % (
                    datastore_name,
                    folder_name,
                    folder_details['filename']
                )
                folder_details['size'] = folder_info.fileSize
                folder_details['size_unit'] = self.convert_storage(folder_details['size'])
                folder_details['owner'] = folder_info.owner
                folder_details['modification'] = folder_info.modification
                folders.append(folder_details)

        return folders

    def get_datastore_folder(self, datacenter_name, datastore_name, folder_name):
        folders = self.get_datastore_folders(datacenter_name, datastore_name, folder_name)
        if folders is None:
            return None

        files = self.get_datastore_files(datacenter_name, datastore_name, folder_name)
        if files is None:
            return None

        result = folders
        for file in files:
            found = False
            for folder in folders:
                if file['path'] == folder['path']:
                    found = True
                    break

            if found:
                continue

            result.append(file)

        return result

    def print_datastore_files(self, files):
        self.my_output.my_table(
            files,
            order=[
                'path',
                'type',
                'size_unit',
                'owner',
                'modification'
            ],
            headers=[
                'Path',
                'Type',
                'Size',
                'Owner',
                'Modification'
            ],
            table=True
        )

    def is_datastore_folder(self, datacenter_name, datastore_name, folder_name):
        ds_obj = self.get_datastore_object(datacenter_name, datastore_name)
        if ds_obj is None:
            return False

        spec = vim.host.DatastoreBrowser.SearchSpec(query=[vim.host.DatastoreBrowser.FolderQuery()])
        search_path = '[%s] %s' % (datastore_name, folder_name)
        task = ds_obj.browser.SearchDatastoreSubFolders_Task(
            search_path,
            spec
        )
        self.wait_for_tasks([task], exception_on_task_failure=False)
        if task.info.state == 'error':
            return False

        return True

    def create_datastore_folder(self, datacenter_name, datastore_name, folder_name, nested=True):
        if not self.vc_connect():
            print('[ERROR] Failed to connect to virtual center')
            return False

        # https://vdc-download.vmware.com/vmwb-repository/dcr-public/fa5d1ee7-fad5-4ebf-b150-bdcef1d38d35/a5e46da1-9b96-4f0c-a1d0-7b8f3ebfd4f5/doc/vim.FileManager.html
        dc_obj = self.get_datacenter_object(datacenter_name)

        file_manager_handler = self.get_filemanager_handler()
        if file_manager_handler is None:
            print('[ERROR] Failed to get file manager handler')
            return False

        name = '[%s] %s' % (datastore_name, folder_name)
        try:
            file_manager_handler.MakeDirectory(
                name=name,
                datacenter=dc_obj,
                createParentDirectories=nested
            )
        except BaseException:
            print(traceback.format_exc())
            return False

        return self.is_datastore_folder(datacenter_name, datastore_name, folder_name)

    def delete_datastore_folder(self, datacenter_name, datastore_name, folder_name, nested=True):
        if not self.vc_connect():
            print('[ERROR] Failed to connect to virtual center')
            return False

        # https://vdc-download.vmware.com/vmwb-repository/dcr-public/fa5d1ee7-fad5-4ebf-b150-bdcef1d38d35/a5e46da1-9b96-4f0c-a1d0-7b8f3ebfd4f5/doc/vim.FileManager.html
        dc_obj = self.get_datacenter_object(datacenter_name)

        file_manager_handler = self.get_filemanager_handler()
        if file_manager_handler is None:
            print('[ERROR] Failed to get file manager handler')
            return False

        name = '[%s] %s' % (datastore_name, folder_name)
        try:
            file_manager_handler.DeleteFile(
                name=name,
                datacenter=dc_obj
            )
        except BaseException:
            print(traceback.format_exc())
            return False

        return True

    def get_datastore_files(self, datacenter_name, datastore_name, folder_name):
        ds_obj = self.get_datastore_object(datacenter_name, datastore_name)
        if ds_obj is None:
            return None

        spec = vim.host.DatastoreBrowser.SearchSpec(query=[vim.host.DatastoreBrowser.Query()])
        spec.details = vim.host.DatastoreBrowser.FileInfo.Details(
            fileOwner=True, fileSize=True, fileType=True, modification=True
        )
        search_path = '[%s] %s' % (datastore_name, folder_name)
        task = ds_obj.browser.SearchDatastoreSubFolders_Task(
            search_path,
            spec
        )
        self.wait_for_tasks([task])
        search_results = task.info.result

        files = []
        for search_result in search_results:
            # <class 'pyVmomi.VmomiSupport.vim.host.DatastoreBrowser.SearchResults'>

            # dynamicType = <unset>,
            # dynamicProperty = (vmodl.DynamicProperty) [],
            # datastore = 'vim.Datastore:datastore-1013',
            # folderPath = '[datastore1] catalog/tidy/',
            # file = (vim.host.DatastoreBrowser.FileInfo) [
            #     (vim.host.DatastoreBrowser.FolderInfo) {
            #         dynamicType = <unset>,
            #         dynamicProperty = (vmodl.DynamicProperty) [],
            #         path = 'v1',
            #         friendlyName = <unset>,
            #         fileSize = <unset>,
            #         modification = <unset>,
            #         owner = <unset>
            #     }
            # ]
            for file_info in search_result.file:
                file_folder = self.fixup_datastore_path(
                    search_result.folderPath
                )
                if file_folder != search_path:
                    continue

                file_details = {}
                file_details['type'] = 'File'
                file_details['datastore'] = datastore_name
                file_details['folder'] = folder_name
                file_details['filename'] = file_info.path
                file_details['path'] = '[%s] %s%s' % (
                    datastore_name,
                    folder_name,
                    file_details['filename']
                )
                file_details['size'] = file_info.fileSize
                file_details['size_unit'] = self.convert_storage(file_details['size'])
                file_details['owner'] = file_info.owner
                file_details['modification'] = file_info.modification
                files.append(file_details)

        return files

    def is_datastore_file(self, datacenter_name, datastore_name, folder_name, file_name):
        if not self.is_datastore_folder(datacenter_name, datastore_name, folder_name):
            return False

        files = self.get_datastore_files(datacenter_name, datastore_name, folder_name)
        if files is None:
            return False

        for folder_file_info in files:
            if folder_file_info['filename'] == file_name:
                return True

        return False

    def create_datastore_file(self, datacenter_name, datastore_name, source_filename, target_folder_name, target_filename):
        if not os.path.isfile(source_filename):
            self.my_output.error('File not found: %s' % (source_filename))
            return False

        if not self.vc_connect():
            return None

        target_filename = '/folder%s%s' % (target_folder_name, target_filename)
        params = {}
        params["dsName"] = datastore_name
        params["dcPath"] = datacenter_name
        http_url = "https://%s:%s%s" % (
            self.vcenter_ip,
            self.vcenter_port,
            target_filename
        )

        # Get the cookie built from the current session

        # pylint: disable=protected-access
        client_cookie = self.vc_service_instance._stub.cookie

        # Break apart the cookie into it's component parts - This is more than
        # is needed, but a good example of how to break apart the cookie
        # anyways. The verbosity makes it clear what is happening.
        cookie_name = client_cookie.split("=", 1)[0]
        cookie_value = client_cookie.split("=", 1)[1].split(";", 1)[0]
        cookie_path = client_cookie.split("=", 1)[1].split(";", 1)[1].split(
            ";", 1)[0].lstrip()
        cookie_text = " " + cookie_value + "; $" + cookie_path

        # Make a cookie
        cookie = {}
        cookie[cookie_name] = cookie_text

        # Get the request headers set up
        headers = {'Content-Type': 'application/octet-stream'}

        try:
            self.my_output.debug(http_url)

            with open(source_filename, "rb") as file_data:
                # Connect and upload the file
                response = requests.put(
                    http_url,
                    params=params,
                    data=file_data,
                    headers=headers,
                    cookies=cookie,
                    verify=False,
                    timeout=3600
                )

            response_code = response.status_code
            self.my_output.debug('Reponse code: %s' % (response_code))
            if response_code >= 300:
                self.my_output.error('File upload failed with response code %s' % (response_code))
                try:
                    self.my_output.default(response.content)
                except BaseException:
                    pass

                return False

        except BaseException:
            self.my_output.error('Exception in file upload')
            self.my_output.default(traceback.format_exc())
            return False

        return True

    def delete_datastore_file(self, datacenter_name, datastore_name, file_path):
        if not self.vc_connect():
            print('[ERROR] Failed to connect to virtual center')
            return False

        # https://vdc-download.vmware.com/vmwb-repository/dcr-public/fa5d1ee7-fad5-4ebf-b150-bdcef1d38d35/a5e46da1-9b96-4f0c-a1d0-7b8f3ebfd4f5/doc/vim.FileManager.html
        dc_obj = self.get_datacenter_object(datacenter_name)

        file_manager_handler = self.get_filemanager_handler()
        if file_manager_handler is None:
            print('[ERROR] Failed to get file manager handler')
            return False

        name = '[%s] %s' % (datastore_name, file_path)
        try:
            file_manager_handler.DeleteFile(
                name=name,
                datacenter=dc_obj
            )
        except BaseException:
            print(traceback.format_exc())
            return False

        return True
