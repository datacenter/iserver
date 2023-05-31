from lib.aci.policy.troubleshooting.span.source import PolicyTroubleshootingSpanSource
from lib.aci.policy.troubleshooting.span.destination import PolicyTroubleshootingSpanDestination


class PolicyTroubleshootingSpan(PolicyTroubleshootingSpanSource, PolicyTroubleshootingSpanDestination):
    def __init__(self):
        PolicyTroubleshootingSpanSource.__init__(self)
        PolicyTroubleshootingSpanDestination.__init__(self)
