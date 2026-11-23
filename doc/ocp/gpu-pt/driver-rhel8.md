# RHEL8 Virtual Machine with NVIDIA GPU driver

Once the virtual machine is [created](./virtual-machine-rhel8.md) with GPU device in passthrough mode, it has [nouveau driver](https://nouveau.freedesktop.org/) which is the open-source driver for NVIDIA GPU. It has limited capabilities as compared to NVIDIA driver.

```
$ cat /etc/redhat-release
Red Hat Enterprise Linux release 8.10 (Ootpa)
$ uname -r
4.18.0-553.81.1.el8_10.x86_64
```

The goal of this guide is to show how to install NVIDIA driver inside the RHEL8 virtual machine

References
- [CUDA toolkit installation guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/) 
- [NVIDIA driver installation guide](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/introduction.html)
- [FAQ](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/frequently-asked-questions.html)
- [youtube video](https://www.youtube.com/watch?v=lud0C-K3ya0).

## Command cheat sheet

```
$ sudo -E subscription-manager register
$ sudo -E yum -y install gcc kernel-devel-$(uname -r) kernel-headers-$(uname -r) freeglut mesa-libGLU
$ sudo -E subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms --enable=rhel-8-for-x86_64-baseos-rpms --enable=codeready-builder-for-rhel-8-x86_64-rpms
$ sudo -E yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
$ sudo -E yum -y install https://developer.download.nvidia.com/compute/cuda/13.1.0/local_installers/cuda-repo-rhel8-13-1-local-13.1.0_590.44.01-1.x86_64.rpm
$ sudo -E yum -y module install nvidia-driver:open-dkms
$ sudo -E yum -y install nvidia-open
$ sudo -E dkms -m nvidia/590.44.01 -k 4.18.0-553.81.1.el8_10.x86_64 build
$ sudo -E dkms -m nvidia/590.44.01 -k 4.18.0-553.81.1.el8_10.x86_64 install
$ sudo -E yum -y install cuda
```

## Expected outcome

```
$ lspci -nn -k -d ::0302
09:00.0 3D controller [0302]: NVIDIA Corporation GA107GL [A2 / A16] [10de:25b6] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:14a9]
        Kernel driver in use: nvidia
        Kernel modules: nvidia_drm, nvidia
```

## Register with Red Hat Subscription Management

Note: set http proxy if required

```
$ sudo -E subscription-manager register
Registering to: subscription.rhsm.redhat.com:443/subscription
Username: your-username-at-redhat
Password: your-password
The system has been registered with ID: system-uuid-generated-by-redhat
The registered system name is: your-vm-hostname
```

```
$ sudo -E subscription-manager status
+-------------------------------------------+
   System Status Details
+-------------------------------------------+
Overall Status: Registered
```

## Install 3rd party libraries

```
$ sudo -E yum -y install gcc kernel-devel-$(uname -r) kernel-headers-$(uname -r) freeglut mesa-libGLU
...
Upgraded:
  glibc-2.28-251.el8_10.27.x86_64   glibc-all-langpacks-2.28-251.el8_10.27.x86_64   glibc-common-2.28-251.el8_10.27.x86_64   glibc-gconv-extra-2.28-251.el8_10.27.x86_64
Installed:
  binutils-2.30-128.el8_10.x86_64                                bison-3.0.4-10.el8.x86_64                  cpp-8.5.0-28.el8_10.x86_64
  elfutils-libelf-devel-0.190-2.el8.x86_64                       flex-2.6.1-9.el8.x86_64                    freeglut-3.0.0-9.el8.x86_64
  gcc-8.5.0-28.el8_10.x86_64                                     glibc-devel-2.28-251.el8_10.27.x86_64      glibc-headers-2.28-251.el8_10.27.x86_64
  isl-0.16.1-6.el8.x86_64                                        kernel-devel-4.18.0-553.81.1.el8_10.x86_64 kernel-headers-4.18.0-553.81.1.el8_10.x86_64
  keyutils-libs-devel-1.5.10-9.el8.x86_64                        krb5-devel-1.18.2-32.el8_10.x86_64         libICE-1.0.9-15.el8.x86_64
  libX11-xcb-1.6.8-9.el8_10.x86_64                               libXfixes-5.0.3-7.el8.x86_64               libXi-1.7.10-1.el8.x86_64
  libXxf86vm-1.1.4-9.el8.x86_64                                  libcom_err-devel-1.45.6-7.el8_10.x86_64    libdrm-2.4.115-2.el8.x86_64
  libglvnd-1:1.3.4-2.el8.x86_64                                  libglvnd-glx-1:1.3.4-2.el8.x86_64          libkadm5-1.18.2-32.el8_10.x86_64
  libmpc-1.1.0-9.1.el8.x86_64                                    libpciaccess-0.14-1.el8.x86_64             libselinux-devel-2.9-10.el8_10.x86_64
  libsepol-devel-2.9-3.el8.x86_64                                libverto-devel-0.3.2-2.el8.x86_64          libxcrypt-devel-4.1.1-6.el8.x86_64
  libxshmfence-1.3-2.el8.x86_64                                  libzstd-devel-1.4.4-1.el8.x86_64           m4-1.4.18-7.el8.x86_64
  make-1:4.2.1-11.el8.x86_64                                     mesa-libGL-23.1.4-4.el8_10.x86_64          mesa-libGLU-9.0.0-15.el8.x86_64
  mesa-libglapi-23.1.4-4.el8_10.x86_64                           openssl-devel-1:1.1.1k-14.el8_6.x86_64     pcre2-devel-10.32-3.el8_6.x86_64
  pcre2-utf16-10.32-3.el8_6.x86_64                               pcre2-utf32-10.32-3.el8_6.x86_64           perl-Carp-1.42-396.el8.noarch
  perl-Data-Dumper-2.167-399.el8.x86_64                          perl-Digest-1.17-395.el8.noarch            perl-Digest-MD5-2.55-396.el8.x86_64
  perl-Encode-4:2.97-3.el8.x86_64                                perl-Errno-1.28-423.el8_10.x86_64          perl-Exporter-5.72-396.el8.noarch
  perl-File-Path-2.15-2.el8.noarch                               perl-File-Temp-0.230.600-1.el8.noarch      perl-Getopt-Long-1:2.50-4.el8.noarch
  perl-HTTP-Tiny-0.074-3.el8.noarch                              perl-IO-1.38-423.el8_10.x86_64             perl-IO-Socket-IP-0.39-5.el8.noarch
  perl-IO-Socket-SSL-2.066-4.module+el8.3.0+6446+594cad75.noarch perl-MIME-Base64-3.15-396.el8.x86_64       perl-Mozilla-CA-20160104-7.module+el8.3.0+6498+9eecfe51.noarch
  perl-Net-SSLeay-1.88-2.module+el8.6.0+13392+f0897f98.x86_64    perl-PathTools-3.74-1.el8.x86_64           perl-Pod-Escapes-1:1.07-395.el8.noarch
  perl-Pod-Perldoc-3.28-396.el8.noarch                           perl-Pod-Simple-1:3.35-395.el8.noarch      perl-Pod-Usage-4:1.69-395.el8.noarch
  perl-Scalar-List-Utils-3:1.49-2.el8.x86_64                     perl-Socket-4:2.027-3.el8.x86_64           perl-Storable-1:3.11-3.el8.x86_64
  perl-Term-ANSIColor-4.06-396.el8.noarch                        perl-Term-Cap-1.17-395.el8.noarch          perl-Text-ParseWords-3.30-395.el8.noarch
  perl-Text-Tabs+Wrap-2013.0523-395.el8.noarch                   perl-Time-Local-1:1.280-1.el8.noarch       perl-URI-1.73-3.el8.noarch
  perl-Unicode-Normalize-1.25-396.el8.x86_64                     perl-constant-1.33-396.el8.noarch          perl-interpreter-4:5.26.3-423.el8_10.x86_64
  perl-libnet-3.11-3.el8.noarch                                  perl-libs-4:5.26.3-423.el8_10.x86_64       perl-macros-4:5.26.3-423.el8_10.x86_64
  perl-parent-1:0.237-1.el8.noarch                               perl-podlators-4.11-1.el8.noarch           perl-threads-1:2.21-2.el8.x86_64
  perl-threads-shared-1.58-2.el8.x86_64                          zlib-devel-1.2.11-25.el8.x86_64

Complete!
```

## Enable optional repositories

```
$ sudo -E subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms --enable=rhel-8-for-x86_64-baseos-rpms --enable=codeready-builder-for-rhel-8-x86_64-rpms
Repository 'rhel-8-for-x86_64-appstream-rpms' is enabled for this system.
Repository 'rhel-8-for-x86_64-baseos-rpms' is enabled for this system.
Repository 'codeready-builder-for-rhel-8-x86_64-rpms' is enabled for this system.
```

## Install packages from EPEL repositories

Note: based on youtube video

```
$ sudo -E yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
Updating Subscription Management repositories.

...

Installed:
  epel-release-8-22.el8.noarch

Complete!
```

## Install CUDA toolkit repository package

Installation instructions based on [cuda-downloads](https://developer.nvidia.com/cuda-downloads) and depend on operating system, architecture, distribution and version.

Example below is for Cuda 13.1, x86_64 architecture, RHEL8, rpm local.

```
$ sudo -E yum -y install https://developer.download.nvidia.com/compute/cuda/13.1.0/local_installers/cuda-repo-rhel8-13-1-local-13.1.0_590.44.01-1.x86_64.rpm

...

Installed:
  cuda-repo-rhel8-13-1-local-13.1.0_590.44.01-1.x86_64

Complete!
```

Notes: 
- it may take a while depending on download speed as the rpm package is 4.6GB
- the downloaded package is a repository package that informs the package manager where to find the actual installation packages, but will not install them.

## Driver installation

Options
- open kernel module with nvidia-driver:open-dkms
- proprietary kernel module with nvida-driver:latest-dkms

### Which option to choose

The choice between the open vs. proprietary is based on the GPU hardware. I could not find explicit guideline other than rule-of-the-thumb rule that older GPUs may need proprietary kernel module while newer hardware expects open one.

No error is raised depending for hw-to-driver-option compatibility when module is installed. You can learn the hard way in the next step when installing cuda e.g.,

```
$ sudo -E yum -y install cuda
Error:
 Problem: package cuda-13.1.0-1.x86_64 from cuda-rhel9-13-1-local requires nvidia-open >= 590.44.01, but none of the providers can be installed
  - conflicting requests
  - package nvidia-open-3:590.44.01-1.el9.noarch from cuda-rhel9-13-1-local is filtered out by modular filtering
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

In case of mismatch, uninstall driver first following the [documentation](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/removing-the-driver.html) or refer to outputs below for RHEL8.

### Install open

Module enablement

```
$ sudo -E yum -y module install nvidia-driver:open-dkms

...

Installed:
  adwaita-cursor-theme-3.28.0-3.el8.noarch                          adwaita-icon-theme-3.28.0-3.el8.noarch             at-spi2-atk-2.26.2-1.el8.x86_64
  at-spi2-core-2.28.0-1.el8.x86_64                                  atk-2.28.1-1.el8.x86_64                            avahi-libs-0.7-27.el8_10.1.x86_64
  colord-libs-1.4.2-1.el8.x86_64                                    cups-libs-1:2.2.6-64.el8_10.x86_64                 dconf-0.28.0-4.el8.x86_64
  dkms-3.3.0-1.el8.noarch                                           egl-gbm-2:1.1.2.1-1.el8.x86_64                     egl-wayland-1.1.20-1.el8.x86_64
  egl-x11-1.0.3-1.el8.x86_64                                        fribidi-1.0.4-9.el8.x86_64                         gcc-c++-8.5.0-28.el8_10.x86_64
  gdk-pixbuf2-modules-2.36.12-7.el8_10.x86_64                       graphite2-1.3.10-10.el8.x86_64                     gtk-update-icon-cache-3.22.30-12.el8_10.x86_64
  gtk3-3.22.30-12.el8_10.x86_64                                     harfbuzz-1.7.5-4.el8.x86_64                        hicolor-icon-theme-0.17-2.el8.noarch
  jasper-libs-2.0.14-6.el8_10.x86_64                                jbigkit-libs-2.1-14.el8.x86_64                     kmod-nvidia-open-dkms-3:590.44.01-1.el8.noarch
  lcms2-2.9-2.el8.x86_64                                            libX11-devel-1.6.8-9.el8_10.x86_64                 libXau-devel-1.0.9-3.el8.x86_64
  libXcomposite-0.4.4-14.el8.x86_64                                 libXcursor-1.1.15-3.el8.x86_64                     libXdamage-1.1.4-14.el8.x86_64
  libXdmcp-1.1.3-1.el8.x86_64                                       libXfont2-2.0.3-2.el8.x86_64                       libXft-2.3.3-1.el8.x86_64
  libXinerama-1.1.4-1.el8.x86_64                                    libXrandr-1.5.2-1.el8.x86_64                       libXtst-1.2.3-7.el8.x86_64
  libdatrie-0.2.9-7.el8.x86_64                                      libepoxy-1.5.8-1.el8.x86_64                        libevdev-1.10.0-1.el8.x86_64
  libfontenc-1.1.3-8.el8.x86_64                                     libglvnd-egl-1:1.3.4-2.el8.x86_64                  libglvnd-gles-1:1.3.4-2.el8.x86_64
  libglvnd-opengl-1:1.3.4-2.el8.x86_64                              libgudev-232-4.el8.x86_64                          libgusb-0.3.0-1.el8.x86_64
  libinput-1.16.3-3.el8_6.x86_64                                    libjpeg-turbo-1.5.3-14.el8_10.x86_64               libnvidia-cfg-3:590.44.01-1.el8.x86_64
  libnvidia-fbc-3:590.44.01-1.el8.x86_64                            libnvidia-gpucomp-3:590.44.01-1.el8.x86_64         libnvidia-ml-3:590.44.01-1.el8.x86_64
  libstdc++-devel-8.5.0-28.el8_10.x86_64                            libthai-0.1.27-2.el8.x86_64                        libtiff-4.0.9-36.el8_10.x86_64
  libvdpau-1.5-11.el8.x86_64                                        libwacom-1.6-3.el8.x86_64                          libwacom-data-1.6-3.el8.noarch
  libwayland-client-1.21.0-1.el8.x86_64                             libwayland-cursor-1.21.0-1.el8.x86_64              libwayland-egl-1.21.0-1.el8.x86_64
  libwayland-server-1.21.0-1.el8.x86_64                             libxcb-devel-1.13.1-1.el8.x86_64                   libxkbfile-1.1.0-1.el8.x86_64
  llvm-compat-libs-17.0.6-3.module+el8.10.0+22218+ed012fd4.x86_64   mesa-libEGL-23.1.4-4.el8_10.x86_64                 mesa-libgbm-23.1.4-4.el8_10.x86_64
  mesa-vulkan-drivers-23.1.4-4.el8_10.x86_64                        mtdev-1.1.5-12.el8.x86_64                          nvidia-driver-3:590.44.01-1.el8.x86_64
  nvidia-driver-cuda-3:590.44.01-1.el8.x86_64                       nvidia-driver-cuda-libs-3:590.44.01-1.el8.x86_64   nvidia-driver-libs-3:590.44.01-1.el8.x86_64
  nvidia-kmod-common-3:590.44.01-1.el8.noarch                       nvidia-libXNVCtrl-3:590.44.01-1.el8.x86_64         nvidia-libXNVCtrl-devel-3:590.44.01-1.el8.x86_64
  nvidia-modprobe-3:590.44.01-1.el8.x86_64                          nvidia-persistenced-3:590.44.01-1.el8.x86_64       nvidia-settings-3:590.44.01-1.el8.x86_64
  nvidia-xconfig-3:590.44.01-1.el8.x86_64                           ocl-icd-2.2.12-1.el8.x86_64                        opencl-filesystem-1.0-6.el8.noarch
  pango-1.42.4-8.el8.x86_64                                         patch-2.7.6-11.el8.x86_64                          rest-0.8.1-3.el8_10.x86_64
  vulkan-loader-1.3.283.0-1.el8_10.x86_64                           xorg-x11-drv-fbdev-0.5.0-2.el8.x86_64              xorg-x11-drv-libinput-0.29.0-1.el8.x86_64
  xorg-x11-drv-vesa-2.4.0-3.el8.x86_64                              xorg-x11-nvidia-3:590.44.01-1.el8.x86_64           xorg-x11-proto-devel-2020.1-3.el8.noarch
  xorg-x11-server-Xorg-1.20.11-27.el8_10.x86_64                     xorg-x11-server-common-1.20.11-27.el8_10.x86_64    xorg-x11-xkb-utils-7.7-28.el8.x86_64

Complete!
```

Driver installation

```
$ sudo -E yum -y install nvidia-open

...

Installed:
  nvidia-open-3:590.44.01-1.el8.noarch

Complete!
```

### Install proprietary

Module enablement (have not tried this one)

```
$ sudo -E yum -y module install nvidia-driver:latest-dkms
```

Driver installation (have not tried this one)

```
$ sudo -E yum -y install cuda-drivers
```

### Recompile driver

If the there is no nvidia driver in /lib/modules/ or you need to recompile the driver instead of relying on the pre-built driver

```
# dkms -m nvidia/590.44.01 -k 4.18.0-553.81.1.el8_10.x86_64 build
Sign command: /lib/modules/4.18.0-553.81.1.el8_10.x86_64/build/scripts/sign-file
Signing key: /var/lib/dkms/mok.key
Public certificate (MOK): /var/lib/dkms/mok.pub

Building module(s)................................................................................................................................................. done.
Signing module /var/lib/dkms/nvidia/590.44.01/build/kernel-open/nvidia.ko
Signing module /var/lib/dkms/nvidia/590.44.01/build/kernel-open/nvidia-modeset.ko
Signing module /var/lib/dkms/nvidia/590.44.01/build/kernel-open/nvidia-drm.ko
Signing module /var/lib/dkms/nvidia/590.44.01/build/kernel-open/nvidia-uvm.ko
Signing module /var/lib/dkms/nvidia/590.44.01/build/kernel-open/nvidia-peermem.ko
```

```
# dkms -m nvidia/590.44.01 -k 4.18.0-553.81.1.el8_10.x86_64 install
Installing /lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia.ko.xz
Installing /lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-modeset.ko.xz
Installing /lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-drm.ko.xz
Installing /lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-uvm.ko.xz
Installing /lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-peermem.ko.xz
Running depmod.... done.
Executing post-transaction command.............. done.
```

Note:
- check nvidia version with 'dkms status'
- check kernel version with 'uname -r'

Example

```
# dkms status
nvidia/590.44.01
# uname -r
4.18.0-553.81.1.el8_10.x86_64
```

Important: if you have not enough memory (e.g. 2GB), compile may fail with

```
# dkms -m nvidia/590.44.01 -k 4.18.0-553.81.1.el8_10.x86_64 build
Sign command: /lib/modules/4.18.0-553.81.1.el8_10.x86_64/build/scripts/sign-file
Signing key: /var/lib/dkms/mok.key
Public certificate (MOK): /var/lib/dkms/mok.pub

Building module(s).....(bad exit status: 2)
Failed command:
'make' -j1 KERNEL_UNAME=4.18.0-553.81.1.el8_10.x86_64 IGNORE_PREEMPT_RT_PRESENCE=1 IGNORE_XEN_PRESENCE=1 modules

Error! Bad return status for module build on kernel: 4.18.0-553.81.1.el8_10.x86_64 (x86_64)
Consult /var/lib/dkms/nvidia/590.44.01/build/make.log for more information.

# more /var/lib/dkms/nvidia/590.44.01/build/make.log
DKMS (dkms-3.3.0) make.log for nvidia/590.44.01 for kernel 4.18.0-553.81.1.el8_10.x86_64 (x86_64)
Sun Jan  4 13:46:04 EST 2026

Building module(s)
# command: 'make' -j1 KERNEL_UNAME=4.18.0-553.81.1.el8_10.x86_64 IGNORE_PREEMPT_RT_PRESENCE=1 IGNORE_XEN_PRESENCE=1 modules
make -C src/nvidia
make[1]: Entering directory '/var/lib/dkms/nvidia/590.44.01/build/src/nvidia'
 [ nvidia            ]  CC           generated/g_access_cntr_buffer_nvoc.c
 [ nvidia            ]  CC           generated/g_all_dcl_pb.c
 [ nvidia            ]  CC           generated/g_binary_api_nvoc.c
 [ nvidia            ]  CC           generated/g_bindata.c
virtual memory exhausted: Cannot allocate memory
make[1]: *** [Makefile:204: _out/Linux_x86_64/g_bindata.o] Error 1
make[1]: Leaving directory '/var/lib/dkms/nvidia/590.44.01/build/src/nvidia'
make: *** [Makefile:34: src/nvidia/_out/Linux_x86_64/nv-kernel.o] Error 2

# exit code: 2
# elapsed time: 00:00:09
----------------------------------------------------------------
```

Once memory has been increased to 8GB, compile was successful. Not sure what is the lower limit for this.

### Uninstall driver

The command is the same regardless of the installed driver. The output example below is for proprietary driver uninstallation.

```
$ sudo -E yum -y module remove --all nvidia-driver
```

```
$ sudo -E yum -y module reset nvidia-driver
```

```
$ sudo reboot
```

### Test

```
$ find /lib/modules -type f -name nvidia*
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-modeset.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-drm.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-uvm.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-peermem.ko.xz
```

## CUDA installation

```
$ sudo -E yum -y install cuda

...

Installed:
  alsa-lib-1.2.10-2.el8.x86_64                                                          copy-jdk-configs-4.0-2.el8.noarch
  cuda-13.1.0-1.x86_64                                                                  cuda-13-1-13.1.0-1.x86_64
  cuda-cccl-13-1-13.1.78-1.x86_64                                                       cuda-command-line-tools-13-1-13.1.0-1.x86_64
  cuda-compiler-13-1-13.1.0-1.x86_64                                                    cuda-crt-13-1-13.1.80-1.x86_64
  cuda-cudart-13-1-13.1.80-1.x86_64                                                     cuda-cudart-devel-13-1-13.1.80-1.x86_64
  cuda-culibos-devel-13-1-13.1.68-1.x86_64                                              cuda-cuobjdump-13-1-13.1.80-1.x86_64
  cuda-cupti-13-1-13.1.75-1.x86_64                                                      cuda-cuxxfilt-13-1-13.1.80-1.x86_64
  cuda-documentation-13-1-13.1.80-1.x86_64                                              cuda-driver-devel-13-1-13.1.80-1.x86_64
  cuda-gdb-13-1-13.1.68-1.x86_64                                                        cuda-libraries-13-1-13.1.0-1.x86_64
  cuda-libraries-devel-13-1-13.1.0-1.x86_64                                             cuda-nsight-13-1-13.1.68-1.x86_64
  cuda-nsight-compute-13-1-13.1.0-1.x86_64                                              cuda-nsight-systems-13-1-13.1.0-1.x86_64
  cuda-nvcc-13-1-13.1.80-1.x86_64                                                       cuda-nvdisasm-13-1-13.1.80-1.x86_64
  cuda-nvml-devel-13-1-13.1.68-1.x86_64                                                 cuda-nvprune-13-1-13.1.80-1.x86_64
  cuda-nvrtc-13-1-13.1.80-1.x86_64                                                      cuda-nvrtc-devel-13-1-13.1.80-1.x86_64
  cuda-nvtx-13-1-13.1.68-1.x86_64                                                       cuda-opencl-13-1-13.1.80-1.x86_64
  cuda-opencl-devel-13-1-13.1.80-1.x86_64                                               cuda-profiler-api-13-1-13.1.80-1.x86_64
  cuda-runtime-13-1-13.1.0-1.x86_64                                                     cuda-sandbox-devel-13-1-13.1.68-1.x86_64
  cuda-sanitizer-13-1-13.1.75-1.x86_64                                                  cuda-tileiras-13-1-13.1.80-1.x86_64
  cuda-toolkit-13-1-13.1.0-1.x86_64                                                     cuda-toolkit-13-1-config-common-13.1.80-1.noarch
  cuda-toolkit-13-config-common-13.1.80-1.noarch                                        cuda-toolkit-config-common-13.1.80-1.noarch
  cuda-tools-13-1-13.1.0-1.x86_64                                                       cuda-visual-tools-13-1-13.1.0-1.x86_64
  gds-tools-13-1-1.16.0.49-1.x86_64                                                     gtk2-2.24.32-5.el8.x86_64
  java-1.8.0-openjdk-1:1.8.0.472.b08-1.el8.x86_64                                       java-1.8.0-openjdk-headless-1:1.8.0.472.b08-1.el8.x86_64
  javapackages-filesystem-5.3.0-2.module+el8+2598+06babf2e.noarch                       libSM-1.2.3-1.el8.x86_64
  libatomic-8.5.0-28.el8_10.x86_64                                                      libcublas-13-1-13.2.0.9-1.x86_64
  libcublas-devel-13-1-13.2.0.9-1.x86_64                                                libcufft-13-1-12.1.0.31-1.x86_64
  libcufft-devel-13-1-12.1.0.31-1.x86_64                                                libcufile-13-1-1.16.0.49-1.x86_64
  libcufile-devel-13-1-1.16.0.49-1.x86_64                                               libcurand-13-1-10.4.1.34-1.x86_64
  libcurand-devel-13-1-10.4.1.34-1.x86_64                                               libcusolver-13-1-12.0.7.41-1.x86_64
  libcusolver-devel-13-1-12.0.7.41-1.x86_64                                             libcusparse-13-1-12.7.2.19-1.x86_64
  libcusparse-devel-13-1-12.7.2.19-1.x86_64                                             libnpp-13-1-13.0.2.21-1.x86_64
  libnpp-devel-13-1-13.0.2.21-1.x86_64                                                  libnvfatbin-13-1-13.1.80-1.x86_64
  libnvfatbin-devel-13-1-13.1.80-1.x86_64                                               libnvjitlink-13-1-13.1.80-1.x86_64
  libnvjitlink-devel-13-1-13.1.80-1.x86_64                                              libnvjpeg-13-1-13.0.2.28-1.x86_64
  libnvjpeg-devel-13-1-13.0.2.28-1.x86_64                                               libnvptxcompiler-13-1-13.1.80-1.x86_64
  libnvvm-13-1-13.1.80-1.x86_64                                                         libxkbcommon-x11-0.9.1-1.el8.x86_64
  lksctp-tools-1.0.18-3.el8.x86_64                                                      lua-5.3.4-12.el8.x86_64
  nsight-compute-2025.4.0-2025.4.0.12-1.x86_64                                          nsight-systems-2025.5.2-2025.5.2.266_255236693005v0-0.x86_64
  nspr-4.36.0-2.el8_10.x86_64                                                           nss-3.112.0-4.el8_10.x86_64
  nss-softokn-3.112.0-4.el8_10.x86_64                                                   nss-softokn-freebl-3.112.0-4.el8_10.x86_64
  nss-sysinit-3.112.0-4.el8_10.x86_64                                                   nss-util-3.112.0-4.el8_10.x86_64
  ttmkfdir-3.0.9-54.el8.x86_64                                                          tzdata-java-2025c-1.el8.noarch
  xcb-util-0.4.0-10.el8.x86_64                                                          xcb-util-image-0.4.0-9.el8.x86_64
  xcb-util-keysyms-0.4.0-7.el8.x86_64                                                   xcb-util-renderutil-0.3.9-10.el8.x86_64
  xcb-util-wm-0.4.1-12.el8.x86_64                                                       xorg-x11-font-utils-1:7.5-41.el8.x86_64
  xorg-x11-fonts-Type1-7.5-19.el8.noarch

Complete!
```

## System settings

PATH and LD_LIBRARY_PATH settings

```
$ cat /etc/profile.d/gpu.sh
PATH=/usr/local/cuda-13.1/bin${PATH:+:${PATH}}
export PATH

LD_LIBRARY_PATH=/usr/local/cuda-13.1/lib64 ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export LD_LIBRARY_PATH
```

Disable nouveau driver

```
$ cat /etc/modprobe.d/disable-nouveau.conf

blacklist nouveau
options nouveau modeset=0
```

Rebuild of initial ramdisk prevents the driver from being loaded upon boot

```
$ sudo dracut --force
```

System reload

```
$ sudo reboot
```

## Success criteria

```
$ lsmod  | grep nvidia
nvidia_uvm           1810432  0
nvidia_drm            114688  0
nvidia_modeset       1638400  1 nvidia_drm
nvidia              14577664  2 nvidia_uvm,nvidia_modeset
```

```
$ find /lib/modules -type f -name nvidia*
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-modeset.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-drm.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-uvm.ko.xz
/lib/modules/4.18.0-553.81.1.el8_10.x86_64/extra/nvidia-peermem.ko.xz
```

```
$ cat /proc/driver/nvidia/version
NVRM version: NVIDIA UNIX Open Kernel Module for x86_64  590.44.01  Release Build  (root@rhel8-azure-thrush-29)  Sun Jan  4 14:02:53 EST 2026
GCC version:  gcc version 8.5.0 20210514 (Red Hat 8.5.0-28) (GCC)
```

```
$ nvidia-smi
Sun Jan  4 14:14:50 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.44.01              Driver Version: 590.44.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA A16                     Off |   00000000:09:00.0 Off |                    0 |
|  0%   33C    P8             13W /   62W |       0MiB /  15356MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

[[Back]](./README.md)