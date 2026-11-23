import json
from lib import filter_helper
from lib import output_helper

from lib.redfish.dell.output import RedfishEndpointDellOutput
from lib.redfish.fi.output import RedfishEndpointFabricInterconnectOutput
from lib.redfish.hpe.output import RedfishEndpointHpeOutput
from lib.redfish.ucs_rack.output import RedfishEndpointUcsRackOutput


class RedfishOutput(
        RedfishEndpointDellOutput,
        RedfishEndpointFabricInterconnectOutput,
        RedfishEndpointHpeOutput,
        RedfishEndpointUcsRackOutput
        ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        RedfishEndpointDellOutput.__init__(self)
        RedfishEndpointFabricInterconnectOutput.__init__(self)
        RedfishEndpointHpeOutput.__init__(self)
        RedfishEndpointUcsRackOutput.__init__(self)

    def print_children(self, path, children, deep, output):
        if output == 'default':
            self.my_output.default('')
            if deep:
                self.my_output.default('Redfish resource references (recursively): %s' % (path), underline=True)
            else:
                self.my_output.default('Redfish resource references: %s' % (path), underline=True)

            for child in children:
                if child != path:
                    self.my_output.default(child)

        if output == 'json':
            self.my_output.default(json.dumps(children, indent=4))

    def print_tree(self, data, output):
        if data is None:
            return

        if output == 'json':
            self.my_output.default(
                json.dumps(
                    data,
                    indent=4
                )
            )

        if output == 'default':
            self.my_output.default('')
            for uri in data:
                self.my_output.default(uri, underline=True)
                if data[uri] is None:
                    self.my_output.default('No properties')
                    continue

                self.my_output.default(
                    json.dumps(
                        data[uri],
                        indent=4
                    )
                )

                self.my_output.default('')
