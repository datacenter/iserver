class K8sHyperConvergedOutput():
    def __init__(self):
        pass

    # Note: one object expected
    def print_hyperconvergeds(self, info):
        if info is None:
            return

        if len(info) == 0:
            self.my_output.default('No hyperconverged', before_newline=True)
            return 
                
        for item in info:
            self.print_hyperconverged(item)

    
    def print_hyperconverged(self, item):
        self.my_output.dictionary_ng(
            'HyperConverged',
            item, 
            [
                ['Namespace', 'namespace'],
                ['Name', 'name'],
                ['Owner', 'owner'],
                ['Healthy', 'healthyTick'],
                ['HA', 'haTick'],
                ['Errors', 'error']
            ]
        )

        self.my_output.dictionary_ng(
            'Feature Gates',
            item, 
            [
                ['alignCPUs', 'spec.featureGates.alignCPUs'],
                ['autoResourceLimits', 'spec.featureGates.autoResourceLimits'],
                ['deployKubeSecondaryDNS', 'spec.featureGates.deployKubeSecondaryDNS'],
                ['deployVmConsoleProxy', 'spec.featureGates.deployVmConsoleProxy'],
                ['disableMDevConfiguration', 'spec.featureGates.disableMDevConfiguration'],
                ['downwardMetrics', 'spec.featureGates.downwardMetrics'],
                ['enableApplicationAwareQuota', 'spec.featureGates.enableApplicationAwareQuota'],
                ['enableCommonBootImageImport', 'spec.featureGates.enableCommonBootImageImport'],
                ['persistentReservation', 'spec.featureGates.persistentReservation']
            ],
            underline=False,
            start=''
        )

        self.my_output.dictionary_ng(
            'Live Migration',
            item, 
            [
                ['allowAutoConverge', 'spec.liveMigrationConfig.allowAutoConverge'],
                ['allowPostCopy', 'spec.liveMigrationConfig.allowPostCopy'],
                ['completionTimeoutPerGiB', 'spec.liveMigrationConfig.completionTimeoutPerGiB'],
                ['completionTimeoutPerGiB', 'spec.liveMigrationConfig.completionTimeoutPerGiB'],
                ['parallelMigrationsPerCluster', 'spec.liveMigrationConfig.parallelMigrationsPerCluster'],
                ['parallelOutboundMigrationsPerNode', 'spec.liveMigrationConfig.parallelOutboundMigrationsPerNode'],
                ['progressTimeout', 'spec.liveMigrationConfig.progressTimeout']
            ],
            underline=False,
            start=''
        )

        self.my_output.dictionary_ng(
            'Workload Update Strategy',
            item, 
            [
                ['batchEvictionInterval', 'spec.workloadUpdateStrategy.batchEvictionInterval'],
                ['batchEvictionSize', 'spec.workloadUpdateStrategy.batchEvictionSize'],
                ['workloadUpdateMethods', 'spec.workloadUpdateStrategy.workloadUpdateMethods']
            ],
            underline=False,
            start=''
        )

        self.my_output.dictionary_ng(
            'Virtual Machine Options',
            item, 
            [
                ['disableFreePageReporting', 'spec.virtualMachineOptions.disableFreePageReporting'],
                ['disableSerialConsoleLog', 'spec.virtualMachineOptions.disableSerialConsoleLog']
            ],
            underline=False,
            start=''
        )

        self.my_output.dictionary_ng(
            'Other Settings',
            item, 
            [
                ['evictionStrategy', 'spec.evictionStrategy'],
                ['memoryOvercommitPercentage', 'spec.higherWorkloadDensity.memoryOvercommitPercentage'],
                ['vmiCPUAllocationRatio', 'spec.resourceRequirements.vmiCPUAllocationRatio'],
                ['uninstallStrategy', 'spec.uninstallStrategy'],
            ],
            underline=False,
            start=''
        )