class K8sKnativeServingDelete():
    def __init__(self):
        self.knative_serving = None

    def delete_knative_servings(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Knative Serving', before_newline=True, underline=True)

        servings = self.get_knative_servings(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get knative serving')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no knative serving found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_knative_serving_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('knative serving delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no knative serving')

                if not self.wait_no_knative_serving(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
