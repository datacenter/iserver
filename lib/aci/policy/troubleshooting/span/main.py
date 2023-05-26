from lib.aci.policy.troubleshooting.span.source import PolicyTroubleshootingSpanSource
from lib.aci.policy.troubleshooting.span.destination import PolicyTroubleshootingSpanDestination


class PolicyTroubleshootingSpan(PolicyTroubleshootingSpanSource, PolicyTroubleshootingSpanDestination):
    def __init__(self, log_id=None):
        PolicyTroubleshootingSpanSource.__init__(self, log_id=log_id)
        PolicyTroubleshootingSpanDestination.__init__(self, log_id=log_id)
