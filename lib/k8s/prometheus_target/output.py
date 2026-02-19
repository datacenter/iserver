class K8sPrometheusTargetOutput():
    def __init__(self):
        pass

    def print_prometheus_targets(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Type', 'type'],
                ['Endpoint', 'scrapeUrl'],
                ['Service Monitor', 'sm_namespace_nameT'],
                ['Service', 'serviceT'],
                ['Ready', 'readyTick'],
                ['Last Scrape', 'lastScrapeT'],
                ['Duration [ms]', 'lastScrapeDurationT'],
            ]
        )
        
        ready = 0
        for item in info:
            if item['ready']:
                ready += 1

        self.my_output.default('Readiness summary: %s/%s' % (ready, len(info)), before_newline=True)
        