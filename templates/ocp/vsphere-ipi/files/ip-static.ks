#version=DEVEL
# System authorization information
# auth --useshadow --enablemd5
# Install OS instead of upgrade
# cdrom
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
network --activate --bootproto=static --ip=${INTERFACE_0_IP} --netmask=${INTERFACE_0_NETMASK} --gateway=${INTERFACE_0_GATEWAY} --nameserver=${DNS_NAMESERVER} --device=${INTERFACE_0_NAME}
network --hostname=${HOSTNAME}

# Root password
rootpw ${PASSWORD}
# SELinux configuration (make things super secure...)
selinux --disabled
# System services
services --enabled="chronyd"
# System timezone
timezone ${TIMEZONE} --ntp ${NTP_SERVER}
# System bootloader configuration
bootloader --append=" crashkernel=auto" --location=mbr --boot-drive=sda
autopart --type=lvm
# Clear the Master Boot Record
zerombr
# Partition clearing information
clearpart --all

%post --log=/root/ks-post.log
{
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
}
%end

%packages
%end

reboot