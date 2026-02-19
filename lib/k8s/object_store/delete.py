class K8sObjectStoreDelete():
    def __init__(self):
        self.object_store = None

    def delete_object_stores(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete object store', before_newline=True, underline=True)

        servings = self.get_object_stores(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get object store')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no object store found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_object_store_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('object store delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no object store')

                if not self.wait_no_object_store(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
