#!/bin/bash

# https://docs.centos.org/en-US/8-docs/advanced-install/assembly_making-kickstart-files-available-to-the-installation-program/

usage()
{
  echo "$(basename "$0") [-h] [-s] [-r] -- Centos kickstart iso"
  echo "-h - help message"
  echo "-s - source kickstart file (ks.cfg)"
  echo "-d - target iso file (ks.iso)"
}

cd "$(dirname "$0")"

SOURCE=ks.cfg
DESTINATION=ks.iso

while getopts ':hs:d:' option; do
  case "$option" in
    s) SOURCE=$OPTARG
       ;;
    d) DESTINATION=$OPTARG
       ;;
    h) usage
       exit 1
       ;;
    :) echo "Option -$OPTARG requires an argument." >&2
       exit 1
       ;;
    \?)
       echo "Invalid option: -$OPTARG" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND-1))

echo Source kickstart file: $SOURCE
if [ ! -f $SOURCE ]; then
  echo Error: not found
  exit 1
fi

echo Destination iso file: $DESTINATION
if [ ! -f $DESTINATION ]; then
  rm -f $DESTINATION
fi

fallocate -l 1M $DESTINATION
dd if=/dev/zero of=$DESTINATION bs=1M count=1
mkfs -t ext2 -b 4096 $DESTINATION
if [ ! -d mnt ]; then
  mkdir -p mnt
fi
mount -o loop $DESTINATION mnt
cp $SOURCE mnt/ks.cfg
umount mnt
rmdir mnt
e2label $DESTINATION OEMDRV
blkid $DESTINATION

echo "Done"
exit 0

