from lib.nexus.feature.api import FeatureApi
from lib.nexus.feature.info import FeatureInfo


class Feature(
        FeatureApi,
        FeatureInfo
        ):
    def __init__(self):
        FeatureApi.__init__(self)
        FeatureInfo.__init__(self)
