import traceback


class NfvoApi():
    def __init__(self, nfvo_etsi=True, nfvo_version='4.x'):
        self.nfvo_etsi = nfvo_etsi
        self.nfvo_version = nfvo_version

    def adhoc_get(self, path, params=None, output_format='xml', trace=None):
        resource_type = 'running'
        header = 'Accept'
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type=resource_type,
            header=header,
            media_type='application/vnd.yang.data',
            path=path,
            params=params,
            trace=trace
        )

        return success, response

    def adhoc_post(self, path, data, output_format='xml', timeout=None, trace=None):
        resource_type = 'running'
        header = 'Accept'
        success, response = self.rest_handler.post_rest(
            output_format=output_format,
            resource_type=resource_type,
            header=header,
            media_type='application/vnd.yang.data',
            path=path,
            data=data,
            params=None,
            timeout=timeout,
            trace=trace
        )

        return success, response

    def adhoc_patch(self, path, data, output_format='xml', timeout=None, trace=None):
        resource_type = 'running'
        header = 'Accept'
        success, response = self.rest_handler.patch_rest(
            output_format=output_format,
            resource_type=resource_type,
            header=header,
            media_type='application/vnd.yang.data',
            path=path,
            data=data,
            params=None,
            timeout=timeout,
            trace=trace
        )

        return success, response

    def adhoc_put(self, path, data, output_format='xml', timeout=None, trace=None):
        resource_type = 'running'
        header = 'Accept'
        success, response = self.rest_handler.put_rest(
            output_format=output_format,
            resource_type=resource_type,
            header=header,
            media_type='application/vnd.yang.data',
            path=path,
            data=data,
            params=None,
            timeout=timeout,
            trace=trace
        )

        return success, response

    def adhoc_delete(self, path, params=None, output_format='xml', trace=None):
        resource_type = 'running'
        header = 'Accept'
        success, response = self.rest_handler.delete_rest(
            output_format=output_format,
            resource_type=resource_type,
            header=header,
            media_type='application/vnd.yang.data',
            path=path,
            params=params,
            trace=trace
        )

        return success, response

    def get_rest_api_info(self, output_format='json'):
        """
        Returns API information
        """
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type=None,
            media_type='application/vnd.yang.api',
            header='Accept',
            path=None
        )

        if success:
            try:
                response = response['api']
            except BaseException:
                self.log.error(
                    'nso.get_rest_api_info',
                    traceback.format_exc()
                )

    def get_data(self, output_format, datastore, data_path, header=None, media_type=None, params=None, trace=None):
        """
        Get a data entry in a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`

        :param data_path: The list of paths
        :type  data_path: ``list`` of ``str`` or ``tuple``

        :param header: Header name, mostly "Accept" or "Content-Type"
        :type header: 'str'
        """
        data_path = '/'.join(data_path)
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type=media_type,
            path=data_path,
            params=params,
            trace=trace
        )

        return success, response

    def get_datastore(self, output_format, datastore, header=None, params=None, trace=None):
        """
        Get the details of a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`
        """
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type='application/vnd.yang.data',
            path=None,
            params=params,
            trace=trace
        )

        return success, response

    def create_data_value(self, output_format, datastore, data_path, data, header=None, params=None, trace=None):
        """
        Create (PUT) a data entry in a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`

        :param data_path: The list of paths
        :type  data_path: ``list`` of ``str`` or ``tuple``

        :param data: The new value at the given path
        :type  data: ``dict``

        :param header: Header name, mostly "Accept" or "Content-Type"
        :type header: 'str'

        :rtype: ``bool``
        :return: ``True`` if successful, otherwise error.
        """
        data_path = '/'.join(data_path)
        success, response = self.rest_handler.put_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type='application/vnd.yang.data',
            path=data_path,
            data=data,
            params=params,
            trace=trace
        )

        return success, response

    def patch_data_value(self, output_format, datastore, data_path, data, header=None, params=None, timeout=None, trace=None):
        """
        Update (POST) a data entry in a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`

        :param data_path: The list of paths
        :type  data_path: ``list`` of ``str`` or ``tuple``

        :param data: The new value at the given path
        :type  data: ``dict``

        :param header: Header name, mostly "Accept" or "Content-Type"
        :type header: 'str'

        :rtype: ``bool``
        :return: ``True`` if successful, otherwise error.
        """
        data_path = '/'.join(data_path)
        success, response = self.rest_handler.patch_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type='application/vnd.yang.data',
            data=data,
            path=data_path,
            params=params,
            timeout=timeout,
            trace=trace
        )

        return success, response

    def set_data_value(self, output_format, datastore, data_path, data, header=None, params=None, timeout=None, trace=None):
        data_path = '/'.join(data_path)
        success, response = self.rest_handler.post_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type='application/vnd.yang.data',
            path=data_path,
            data=data,
            params=params,
            timeout=timeout,
            trace=trace
        )

        return success, response

    def delete_path(self, output_format, datastore, data_path, header=None, params=None, trace=None):
        """
        Delete a data entry in a datastore

        :param datastore: The target datastore
        :type  datastore: :class:`DatastoreType`

        :param data_path: The list of paths
        :type  data_path: ``list`` of ``str`` or ``tuple``

        :param header: Header name, mostly "Accept" or "Content-Type"
        :type header: 'str'

        :rtype: ``bool``
        :return: ``True`` if successful, otherwise error.
        """
        data_path = '/'.join(data_path)
        success, response = self.rest_handler.delete_rest(
            output_format=output_format,
            resource_type=datastore,
            header=header,
            media_type='application/vnd.yang.data',
            path=data_path,
            params=params,
            trace=trace
        )

        return success, response

    def get_rollbacks(self, output_format='xml', trace=None):
        """
        Get a list of stored rollbacks
        """
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type='rollbacks',
            header='Accept',
            media_type='application/vnd.yang.api',
            trace=trace
        )

        return success, response

    def get_rollback(self, name, output_format='xml', trace=None):
        """
        Get a list of stored rollbacks
        """
        success, response = self.rest_handler.get_rest(
            output_format=output_format,
            resource_type='rollbacks',
            header='Accept',
            media_type='application/vnd.yang.api',
            path=name,
            trace=trace
        )

        return success, response

    def apply_rollback(self, datastore, name, output_format='xml', trace=None):
        """
        Apply a system rollback
        """
        header = 'Accept'
        success, response = self.rest_handler.post_rest(
            output_format=output_format,
            resource_type=datastore,
            media_type='application/vnd.yang.data',
            header=header,
            path='rollback',
            data={'file': name},
            trace=trace
        )

        return success, response

    def is_nfvo_rest_api(self, output_format='json'):
        success = False
        if self.nfvo_version == '3.x':
            if self.restconf_enabled:
                success, response = self.get_data(
                    output_format,
                    'running',
                    ('tailf-etsi-rel2-nfvo:nfvo', 'vnfd'),
                    header='Accept',
                    media_type='application/vnd.yang.collection',
                    params=None
                )
            else:
                success, response = self.get_data(
                    output_format,
                    'running',
                    ('nfvo', 'vnfd'),
                    header='Accept',
                    media_type='application/vnd.yang.collection',
                    params='deep'
                )

        if self.nfvo_version == '4.x':
            if self.restconf_enabled:
                success, response = self.get_data(
                    output_format,
                    'running',
                    ('etsi-nfv-descriptors:nfv', 'vnfd'),
                    header='Accept',
                    media_type='application/vnd.yang.collection',
                    params=None
                )
            else:
                success, response = self.get_data(
                    output_format,
                    'running',
                    ('nfv', 'vnfd'),
                    header='Accept',
                    media_type='application/vnd.yang.collection',
                    params='deep'
                )

        return success
