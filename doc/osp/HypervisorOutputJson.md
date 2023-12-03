# Hypervisor

## Default output

```
# iserver get osp hv --cluster pod1 -o json

Cluster: pod1
[
    {
        "id": 13,
        "hypervisor_hostname": "AIO-server-1",
        "state": "up",
        "status": "enabled",
        "vcpus": 80,
        "memory_mb": 257397,
        "local_gb": 825,
        "vcpus_used": 22,
        "memory_mb_used": 111616,
        "local_gb_used": 100,
        "hypervisor_type": "QEMU",
        "hypervisor_version": 4002000,
        "free_ram_mb": 145781,
        "free_disk_gb": 725,
        "current_workload": 0,
        "running_vms": 5,
        "disk_available_least": 575,
        "host_ip": "192.168.100.13",
        "service": {
            "id": 31,
            "host": "AIO-server-1",
            "disabled_reason": null
        },
        "cpu_info": "{\"arch\": \"x86_64\", \"model\": \"Skylake-Server-IBRS\", \"vendor\": \"Intel\", \"topology\": {\"cells\": 2, \"sockets\": 1, \"cores\": 22, \"threads\": 2}, \"features\": [\"tm\", \"3dnowprefetch\", \"mtrr\", \"fxsr\", \"nx\", \"monitor\", \"pni\", \"mpx\", \"abm\", \"xsave\", \"sse4.2\", \"ht\", \"avx512bw\", \"pse36\", \"ds\", \"tsc\", \"invpcid\", \"intel-pt\", \"f16c\", \"avx512dq\", \"est\", \"ss\", \"sse4.1\", \"vmx\", \"pcid\", \"fma\", \"arch-capabilities\", \"acpi\", \"tsc-deadline\", \"sep\", \"fpu\", \"pdpe1gb\", \"dca\", \"stibp\", \"smx\", \"mce\", \"pae\", \"aes\", \"sse\", \"smep\", \"fsgsbase\", \"adx\", \"lm\", \"tm2\", \"x2apic\", \"avx2\", \"xtpr\", \"clwb\", \"xsaves\", \"popcnt\", \"tsc_adjust\", \"pdcm\", \"rtm\", \"pge\", \"syscall\", \"msr\", \"smap\", \"vme\", \"spec-ctrl\", \"invtsc\", \"rdrand\", \"sse2\", \"avx\", \"ssbd\", \"avx512f\", \"clflushopt\", \"apic\", \"erms\", \"lahf_lm\", \"ds_cpl\", \"pse\", \"avx512vl\", \"cx8\", \"avx512cd\", \"movbe\", \"de\", \"rsba\", \"rdseed\", \"cmov\", \"pku\", \"pbe\", \"ssse3\", \"cx16\", \"bmi2\", \"dtes64\", \"xsaveopt\", \"pclmuldq\", \"xgetbv1\", \"mmx\", \"rdtscp\", \"md-clear\", \"hle\", \"clflush\", \"mca\", \"xsavec\", \"arat\", \"pat\", \"bmi1\"]}",
        "__Output": {
            "state": "Green",
            "status": "Green"
        },
        "cpu_summary": "22/80",
        "memory_summary": "111,616/257,397 [MB] (43%)",
        "disk_summary": "100/825 [GB] (12%)"
    },
    {
        "id": 7,
        "hypervisor_hostname": "AIO-server-2",
        "state": "up",
        "status": "enabled",
        "vcpus": 48,
        "memory_mb": 257405,
        "local_gb": 825,
        "vcpus_used": 14,
        "memory_mb_used": 89088,
        "local_gb_used": 62,
        "hypervisor_type": "QEMU",
        "hypervisor_version": 4002000,
        "free_ram_mb": 168317,
        "free_disk_gb": 763,
        "current_workload": 0,
        "running_vms": 2,
        "disk_available_least": 740,
        "host_ip": "192.168.100.12",
        "service": {
            "id": 25,
            "host": "AIO-server-2",
            "disabled_reason": null
        },
        "cpu_info": "{\"arch\": \"x86_64\", \"model\": \"Skylake-Server-IBRS\", \"vendor\": \"Intel\", \"topology\": {\"cells\": 2, \"sockets\": 1, \"cores\": 14, \"threads\": 2}, \"features\": [\"mca\", \"de\", \"xsaves\", \"ds_cpl\", \"x2apic\", \"xgetbv1\", \"avx512f\", \"cmov\", \"mpx\", \"pat\", \"bmi2\", \"pcid\", \"vmx\", \"arat\", \"mce\", \"rdseed\", \"clwb\", \"arch-capabilities\", \"clflushopt\", \"fpu\", \"pclmuldq\", \"xtpr\", \"tm\", \"xsaveopt\", \"aes\", \"cx16\", \"adx\", \"dca\", \"erms\", \"pge\", \"sse4.2\", \"ss\", \"mmx\", \"movbe\", \"sse2\", \"avx\", \"rdtscp\", \"syscall\", \"tm2\", \"rtm\", \"ssse3\", \"avx512cd\", \"fsgsbase\", \"ssbd\", \"tsc\", \"spec-ctrl\", \"msr\", \"acpi\", \"invpcid\", \"ht\", \"lahf_lm\", \"md-clear\", \"tsc-deadline\", \"sse4.1\", \"dtes64\", \"fma\", \"hle\", \"monitor\", \"rsba\", \"avx2\", \"avx512dq\", \"smx\", \"est\", \"mtrr\", \"apic\", \"invtsc\", \"smep\", \"sep\", \"pku\", \"cx8\", \"fxsr\", \"abm\", \"pse\", \"pbe\", \"f16c\", \"rdrand\", \"xsavec\", \"intel-pt\", \"avx512vl\", \"stibp\", \"pni\", \"bmi1\", \"smap\", \"sse\", \"tsc_adjust\", \"ds\", \"vme\", \"avx512bw\", \"pdpe1gb\", \"popcnt\", \"pse36\", \"lm\", \"clflush\", \"pae\", \"pdcm\", \"xsave\", \"3dnowprefetch\", \"nx\"]}",
        "__Output": {
            "state": "Green",
            "status": "Green"
        },
        "cpu_summary": "14/48",
        "memory_summary": "89,088/257,405 [MB] (34%)",
        "disk_summary": "62/825 [GB] (7%)"
    },
    {
        "id": 10,
        "hypervisor_hostname": "AIO-server-3",
        "state": "up",
        "status": "enabled",
        "vcpus": 80,
        "memory_mb": 257398,
        "local_gb": 825,
        "vcpus_used": 30,
        "memory_mb_used": 115712,
        "local_gb_used": 44,
        "hypervisor_type": "QEMU",
        "hypervisor_version": 4002000,
        "free_ram_mb": 141686,
        "free_disk_gb": 781,
        "current_workload": 0,
        "running_vms": 2,
        "disk_available_least": 760,
        "host_ip": "192.168.100.14",
        "service": {
            "id": 28,
            "host": "AIO-server-3",
            "disabled_reason": null
        },
        "cpu_info": "{\"arch\": \"x86_64\", \"model\": \"Skylake-Server-IBRS\", \"vendor\": \"Intel\", \"topology\": {\"cells\": 2, \"sockets\": 1, \"cores\": 22, \"threads\": 2}, \"features\": [\"xgetbv1\", \"est\", \"msr\", \"pdpe1gb\", \"ssbd\", \"xsaves\", \"sse4.2\", \"avx2\", \"spec-ctrl\", \"apic\", \"lm\", \"erms\", \"clflushopt\", \"stibp\", \"tm2\", \"pni\", \"rtm\", \"pcid\", \"ds\", \"pdcm\", \"de\", \"f16c\", \"avx512f\", \"clwb\", \"arch-capabilities\", \"monitor\", \"cx8\", \"movbe\", \"ssse3\", \"acpi\", \"xsaveopt\", \"xtpr\", \"smep\", \"fsgsbase\", \"rsba\", \"lahf_lm\", \"cmov\", \"adx\", \"clflush\", \"fma\", \"x2apic\", \"invpcid\", \"xsavec\", \"avx512bw\", \"pae\", \"smx\", \"avx512cd\", \"avx512vl\", \"bmi2\", \"tsc-deadline\", \"avx\", \"ds_cpl\", \"ht\", \"mce\", \"tsc_adjust\", \"pclmuldq\", \"pku\", \"hle\", \"arat\", \"pse\", \"nx\", \"xsave\", \"sep\", \"dtes64\", \"pat\", \"popcnt\", \"3dnowprefetch\", \"rdseed\", \"invtsc\", \"fpu\", \"vme\", \"md-clear\", \"aes\", \"avx512dq\", \"pbe\", \"pse36\", \"rdrand\", \"bmi1\", \"mca\", \"fxsr\", \"sse\", \"cx16\", \"rdtscp\", \"pge\", \"tsc\", \"syscall\", \"tm\", \"smap\", \"sse2\", \"vmx\", \"sse4.1\", \"intel-pt\", \"mpx\", \"dca\", \"abm\", \"mtrr\", \"mmx\", \"ss\"]}",
        "__Output": {
            "state": "Green",
            "status": "Green"
        },
        "cpu_summary": "30/80",
        "memory_summary": "115,712/257,398 [MB] (44%)",
        "disk_summary": "44/825 [GB] (5%)"
    },
    {
        "id": 1,
        "hypervisor_hostname": "compute-server-1",
        "state": "up",
        "status": "enabled",
        "vcpus": 92,
        "memory_mb": 257396,
        "local_gb": 852,
        "vcpus_used": 22,
        "memory_mb_used": 66560,
        "local_gb_used": 102,
        "hypervisor_type": "QEMU",
        "hypervisor_version": 4002000,
        "free_ram_mb": 190836,
        "free_disk_gb": 750,
        "current_workload": 0,
        "running_vms": 3,
        "disk_available_least": 738,
        "host_ip": "192.168.100.11",
        "service": {
            "id": 19,
            "host": "compute-server-1",
            "disabled_reason": null
        },
        "cpu_info": "{\"arch\": \"x86_64\", \"model\": \"Skylake-Server-IBRS\", \"vendor\": \"Intel\", \"topology\": {\"cells\": 2, \"sockets\": 1, \"cores\": 24, \"threads\": 2}, \"features\": [\"ssbd\", \"pat\", \"mca\", \"invtsc\", \"sse4.1\", \"xsave\", \"fxsr\", \"popcnt\", \"spec-ctrl\", \"pdpe1gb\", \"tm2\", \"abm\", \"est\", \"x2apic\", \"xgetbv1\", \"avx512vl\", \"vme\", \"fsgsbase\", \"lm\", \"pni\", \"clflush\", \"xsaves\", \"avx512dq\", \"bmi1\", \"de\", \"lahf_lm\", \"movbe\", \"aes\", \"rtm\", \"tsc_adjust\", \"nx\", \"cmov\", \"cx8\", \"mpx\", \"stibp\", \"pge\", \"msr\", \"pae\", \"clwb\", \"ht\", \"avx512cd\", \"avx\", \"syscall\", \"arat\", \"monitor\", \"fma\", \"hle\", \"md-clear\", \"dca\", \"xsavec\", \"pdcm\", \"pku\", \"cx16\", \"rdtscp\", \"vmx\", \"erms\", \"pclmuldq\", \"arch-capabilities\", \"avx2\", \"sse2\", \"clflushopt\", \"smap\", \"smx\", \"tm\", \"rdseed\", \"sse4.2\", \"avx512f\", \"rdrand\", \"tsc-deadline\", \"pse36\", \"avx512bw\", \"ds\", \"xsaveopt\", \"ssse3\", \"ss\", \"bmi2\", \"pbe\", \"pse\", \"mce\", \"sep\", \"sse\", \"tsc\", \"invpcid\", \"f16c\", \"adx\", \"dtes64\", \"acpi\", \"mtrr\", \"3dnowprefetch\", \"xtpr\", \"apic\", \"pcid\", \"fpu\", \"mmx\", \"smep\", \"intel-pt\", \"rsba\", \"ds_cpl\"]}",
        "__Output": {
            "state": "Green",
            "status": "Green"
        },
        "cpu_summary": "22/92",
        "memory_summary": "66,560/257,396 [MB] (25%)",
        "disk_summary": "102/852 [GB] (11%)"
    },
    {
        "id": 4,
        "hypervisor_hostname": "compute-server-2",
        "state": "up",
        "status": "enabled",
        "vcpus": 92,
        "memory_mb": 385412,
        "local_gb": 852,
        "vcpus_used": 35,
        "memory_mb_used": 101376,
        "local_gb_used": 142,
        "hypervisor_type": "QEMU",
        "hypervisor_version": 4002000,
        "free_ram_mb": 284036,
        "free_disk_gb": 710,
        "current_workload": 0,
        "running_vms": 5,
        "disk_available_least": 659,
        "host_ip": "192.168.100.10",
        "service": {
            "id": 22,
            "host": "compute-server-2",
            "disabled_reason": null
        },
        "cpu_info": "{\"arch\": \"x86_64\", \"model\": \"Skylake-Server-IBRS\", \"vendor\": \"Intel\", \"topology\": {\"cells\": 2, \"sockets\": 1, \"cores\": 24, \"threads\": 2}, \"features\": [\"avx512cd\", \"sep\", \"pse36\", \"avx2\", \"md-clear\", \"vmx\", \"pku\", \"bmi1\", \"pcid\", \"abm\", \"monitor\", \"fma\", \"x2apic\", \"pat\", \"sse2\", \"invtsc\", \"arat\", \"erms\", \"msr\", \"mmx\", \"hle\", \"rtm\", \"cx8\", \"3dnowprefetch\", \"fpu\", \"nx\", \"intel-pt\", \"arch-capabilities\", \"xsavec\", \"avx512bw\", \"cx16\", \"avx512f\", \"ht\", \"tm2\", \"smap\", \"acpi\", \"bmi2\", \"popcnt\", \"pdcm\", \"lahf_lm\", \"pse\", \"rdtscp\", \"xsaves\", \"tsc_adjust\", \"mce\", \"xgetbv1\", \"aes\", \"f16c\", \"clflushopt\", \"movbe\", \"ds\", \"clflush\", \"xsaveopt\", \"cmov\", \"avx\", \"stibp\", \"rsba\", \"ds_cpl\", \"vme\", \"fxsr\", \"est\", \"pclmuldq\", \"mpx\", \"pdpe1gb\", \"avx512vl\", \"ssse3\", \"lm\", \"tsc-deadline\", \"fsgsbase\", \"mca\", \"apic\", \"ss\", \"smx\", \"dtes64\", \"pge\", \"sse4.1\", \"mtrr\", \"rdseed\", \"invpcid\", \"sse4.2\", \"syscall\", \"tm\", \"dca\", \"sse\", \"avx512dq\", \"ssbd\", \"rdrand\", \"pni\", \"tsc\", \"smep\", \"xsave\", \"de\", \"clwb\", \"pbe\", \"pae\", \"adx\", \"spec-ctrl\", \"xtpr\"]}",
        "__Output": {
            "state": "Green",
            "status": "Green"
        },
        "cpu_summary": "35/92",
        "memory_summary": "101,376/385,412 [MB] (26%)",
        "disk_summary": "142/852 [GB] (16%)"
    }
]
```

Developer

```
# iserver get osp hv --cluster pod1 -o json

{
    "duration": 3532,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 3074,
        "total_time": 3074
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 2
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 09:55:40.518058	True	3074	get	hypervisors
```

[[Back]](./HypervisorGet.md)