#version=DEVEL
# System authorization information
auth --useshadow --enablemd5
# Install OS instead of upgrade
cdrom
# Use graphical install
graphical
# Firewall configuration
firewall --disabled
firstboot --enable
ignoredisk --only-use=sda
# Keyboard layouts
keyboard --vckeymap=us --xlayouts='us'
# System language
lang en_US.UTF-8

# Network information
network --activate --bootproto=static --ip=10.58.29.76 --netmask=255.255.255.240 --gateway=10.58.29.78 --nameserver=144.254.71.184 --device=ens192
network --hostname=my-centos

# Root password
rootpw cisco123
# SELinux configuration (make things super secure...)
selinux --disabled
# System services
services --enabled="chronyd"
# System timezone
timezone US/Pacific
# System bootloader configuration
bootloader --append=" crashkernel=auto" --location=mbr --boot-drive=sda
autopart --type=lvm
# Clear the Master Boot Record
zerombr
# Partition clearing information
clearpart --all

%packages --default
%end

reboot