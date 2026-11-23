# Testing RHEL9 Virtual Machine with NVIDIA GPU driver

Samples for CUDA Developers which demonstrates features in CUDA Toolkit in [git repo](https://github.com/NVIDIA/cuda-samples)

## Installation

```
$ sudo -E yum -y install git cmake
$ git clone https://github.com/NVIDIA/cuda-samples.git
$ cd cuda-samples/
$ mkdir build && cd build
$ cmake ..
...
-- Configuring done (13.2s)
-- Generating done (0.4s)
-- Build files have been written to: /home/cloud-user/cuda-samples/build
$ make -j$(nproc)
...
[100%] Linking C executable ptxgen
[100%] Built target ptxgen
[100%] Building C object Samples/7_libNVVM/uvmlite/CMakeFiles/uvmlite.dir/uvmlite.c.o
[100%] Linking C executable uvmlite
[100%] Built target uvmlite
```

## Run tests

```
$ pwd
/home/cloud-user/cuda-samples

$ python3 run_tests.py --output ./test --dir ./build/Samples --config test_args.json
...

Test Summary:
Ran 146 test runs for 147 executables.
All test runs passed!
```

During the tests you can check GPU usage e.g.

```
$ nvidia-smi
Mon Jan  5 11:03:01 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.44.01              Driver Version: 590.44.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A16                     Off |   00000000:09:00.0 Off |                    0 |
|  0%   43C    P0             34W /   62W |     164MiB /  15356MiB |     78%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A           17781      C   ./UnifiedMemoryPerf                     102MiB |
+-----------------------------------------------------------------------------------------+
```

[[Back]](./README.md)