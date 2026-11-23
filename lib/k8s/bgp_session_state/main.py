from lib.k8s.bgp_session_state.api import K8sBgpSessionStateApi
from lib.k8s.bgp_session_state.info import K8sBgpSessionStateInfo
from lib.k8s.bgp_session_state.match import K8sBgpSessionStateMatch


class K8sBgpSessionState(
        K8sBgpSessionStateApi,
        K8sBgpSessionStateInfo,
        K8sBgpSessionStateMatch
        ):
    def __init__(self):
        K8sBgpSessionStateApi.__init__(self)
        K8sBgpSessionStateInfo.__init__(self)
        K8sBgpSessionStateMatch.__init__(self)
