import time
import json

from lib import log_helper


class RedfishTree():
    def __init__(self, endpoint_handler):
        self.endpoint_handler = endpoint_handler
        self.log = log_helper.Log()

        self.tree = {}
        self.tree_root = None
        self.tree_deep_search = False
        self.tree_max_execution_time = 0
        self.tree_start_time = None
        self.tree_max_execution_time_reached = False

    def initialize_tree(self, path, deep, max_time):
        self.log.debug(
            'initalize_tree',
            'Initialize tree: %s %s %s' % (path, deep, max_time)
        )

        self.tree = {}
        self.tree_root = self.endpoint_handler.path_fixup(path)
        self.tree_deep_search = deep
        self.tree_start_time = int(time.time())
        self.tree_max_execution_time = max_time
        self.tree_max_execution_time_reached = False

    def find_odata_id(self, data):
        # https://www.dmtf.org/sites/default/files/standards/documents/DSP2052_1.0.0.pdf
        # section 2.2.3
        #
        # odata.id may contain URI only e.g. /redfish/v1/Chassis/1/Power
        # odata.id may cotain URI and JSON fragment identifier e.g. /redfish/v1/Chassis/1/Power
        # the goal here is to find URI(s) only
        #
        items = []
        if data is None:
            return items

        json_nice_output = json.dumps(data, indent=4)
        for line in json_nice_output.split('\n'):
            # get rid of all whitespaces
            line = line.strip(' ').replace(' ', '')

            # search for "key":"value" lines
            if len(line.split(':')) == 2:
                # remove " from key and value"
                (key, value) = line.split(':')
                key = key.strip('"')
                value = value.rstrip(',').strip('"')

                if key == '@odata.id':
                    # Make sure to get URI value only
                    if '#' in value:
                        value = value.split('#')[0]

                    if value == '/redfish/v1':
                        value = '/redfish/v1/'

                    value = self.endpoint_handler.path_fixup(value)
                    if value not in items:
                        items.append(value)

        return items

    def get_branch(self, branch):
        self.log.debug(
            'get_branch',
            'Get branch: %s' % (branch)
        )

        # Make sure get_tree does not run for too long
        if self.tree_max_execution_time > 0:
            if int(time.time()) - self.tree_start_time > self.tree_max_execution_time:
                self.tree_max_execution_time_reached = True
                return

        # No need to duplicate
        if branch in self.tree:
            self.log.debug(
                'get_branch',
                'Branch already in the tree:%s' % (branch)
            )
            return

        # Get JSON properties of branch URI
        self.tree[branch] = self.endpoint_handler.get_properties(branch)
        if self.tree[branch] is None:
            self.log.debug(
                'get_branch',
                'Branch properties not found: %s' % (branch)
            )
            return

        # Find all odata.id references in JSON properties
        leaves = self.find_odata_id(
            self.tree[branch]
        )

        if not self.tree_deep_search:
            # If no deep search/walk in redfish api tree, just note the existence of leaves (children) and exit
            for leaf in leaves:
                self.log.debug(
                    'get_branch',
                    'No deep search: %s' % (leaf)
                )
                self.tree[leaf] = None

            return

        # Now the recursion...
        for leaf in leaves:
            # Make sure to only recurse withing the tree_root
            # For example if tree_root is 'Chassis/1' but odata.id reference is 'System/...' then we do not go there
            # just note the existence of such leaf and exit
            if not leaf.startswith(self.tree_root):
                self.log.debug(
                    'get_branch',
                    'No deep outside of root: %s' % (leaf)
                )
                self.tree[leaf] = None
                continue

            # Do not go deep on excluded branches
            if leaf in self.endpoint_handler.get_excluded_tree_uri():
                self.tree[leaf] = None
                self.log.debug(
                    'get_branch',
                    'No deep direct match: %s' % (leaf)
                )
                continue

            for excluded_tree_uri in self.endpoint_handler.get_excluded_tree_uri():
                if leaf.startswith(excluded_tree_uri):
                    self.tree[leaf] = None
                    self.log.debug(
                        'get_branch',
                        'No deep partial match: %s' % (leaf)
                    )
                    continue

            # Let's go deeper in the tree...
            self.get_branch(leaf)

    def get_tree(self):
        self.get_branch(
            self.tree_root
        )

        if self.tree_max_execution_time_reached:
            return False

        return True
