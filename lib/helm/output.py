from lib import output_helper

from lib.helm.chart.output import HelmChartOutput
from lib.helm.release.output import HelmReleaseOutput


class HelmOutput(
    HelmChartOutput,
    HelmReleaseOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        HelmChartOutput.__init__(self)
        HelmReleaseOutput.__init__(self)
