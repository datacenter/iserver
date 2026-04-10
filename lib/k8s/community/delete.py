class K8sCommunityDelete():
    def __init__(self):
        pass

    def delete_community(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'Community', 
            'metallb.io/v1beta1',
            name, 
            namespace=namespace, 
            object_name='community',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True

        success = self.wait_no_community(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def delete_communitys(self, my_output=None, wait=True):
        communities = self.get_communitys(
            cache_enabled=False
        )
        if communities is None:
            if my_output is not None:
                my_output.error('Failed to get communities')
            return False

        if len(communities) == 0:
            if my_output is not None:
                my_output.default('Metallb communities %s' % (my_output.add_color('not found', 'Green')))
            return True
        
        all_gone = True
        for community in communities:
            success = self.delete_community(
                community['namespace'],
                community['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                all_gone = False
            
        return all_gone