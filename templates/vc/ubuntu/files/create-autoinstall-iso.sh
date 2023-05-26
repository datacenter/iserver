#!/bin/bash
set -Eeuo pipefail

function cleanup() {
        trap - SIGINT SIGTERM ERR EXIT
        rm -rf "$tmpdir"
        log "Deleted temporary working directory $tmpdir"
}

trap cleanup SIGINT SIGTERM ERR EXIT
today=$(date +"%Y-%m-%d")

function log() {
        echo >&2 -e "[$(date +"%Y-%m-%d %H:%M:%S")] ${1-}"
}

function die() {
        local msg=$1
        log "$msg"
        exit 1
}

function parse_params() {
        user_data_file=''

        while :; do
                case "${1-}" in
                -u | --user-data)
                        user_data_file="${2-}"
                        shift
                        ;;
                *) break ;;
                esac
                shift
        done

        log "Starting up..."

        [[ -z "${user_data_file}" ]] && die "user-data file was not specified."
        [[ ! -f "$user_data_file" ]] && die "user-data file could not be found."

        return 0
}

parse_params "$@"

tmpdir=$(mktemp -d)

if [[ ! "$tmpdir" || ! -d "$tmpdir" ]]; then
        die "Could not create temporary working directory."
else
        log "Created temporary working directory $tmpdir"
fi

log "Checking for required utilities..."
[[ ! -x "$(command -v xorriso)" ]] && die "xorriso is not installed. On Ubuntu, install  the 'xorriso' package."
[[ ! -x "$(command -v sed)" ]] && die "sed is not installed. On Ubuntu, install the 'sed' package."
[[ ! -x "$(command -v curl)" ]] && die "curl is not installed. On Ubuntu, install the 'curl' package."
[[ ! -f "/usr/lib/ISOLINUX/isohdpfx.bin" ]] && die "isolinux is not installed. On Ubuntu, install the 'isolinux' package."
log "All required utilities are installed."

log "Download iso from vcenter..."
source_iso=/tmp/`uuidgen`.iso
curl --insecure --silent --noproxy ${VCENTER_NAME} -u ${VCENTER_USERNAME}:'${VCENTER_PASSWORD}' -X GET -o $source_iso "https://${VCENTER_NAME}/folder${ISO_FILENAME}?dcPath=${VCENTER_DATACENTER}&dsName=${VCENTER_DATASTORE}"
log "Downloaded to $source_iso"

log "Extracting ISO image..."
xorriso -osirrox on -indev "${source_iso}" -extract / "$tmpdir" &>/dev/null
chmod -R u+w "$tmpdir"
rm -rf "$tmpdir/"'[BOOT]'
log "Extracted to $tmpdir"

log "Adding autoinstall parameter to kernel command line..."
sed -i -e 's/---/ autoinstall  ---/g' "$tmpdir/isolinux/txt.cfg"
sed -i -e 's/---/ autoinstall  ---/g' "$tmpdir/boot/grub/grub.cfg"
sed -i -e 's/---/ autoinstall  ---/g' "$tmpdir/boot/grub/loopback.cfg"
log "Added parameter to UEFI and BIOS kernel command lines."

log "Adding user-data files..."
mkdir "$tmpdir/nocloud"
cp "$user_data_file" "$tmpdir/nocloud/user-data"
touch "$tmpdir/nocloud/meta-data"
sed -i -e 's,---, ds=nocloud;s=/cdrom/nocloud/  ---,g' "$tmpdir/isolinux/txt.cfg"
sed -i -e 's,---, ds=nocloud\\\;s=/cdrom/nocloud/  ---,g' "$tmpdir/boot/grub/grub.cfg"
sed -i -e 's,---, ds=nocloud\\\;s=/cdrom/nocloud/  ---,g' "$tmpdir/boot/grub/loopback.cfg"
log "Added data and configured kernel command line."

log "Updating $tmpdir/md5sum.txt with hashes of modified files..."
md5=$(md5sum "$tmpdir/boot/grub/grub.cfg" | cut -f1 -d ' ')
sed -i -e 's,^.*[[:space:]] ./boot/grub/grub.cfg,'"$md5"'  ./boot/grub/grub.cfg,' "$tmpdir/md5sum.txt"
md5=$(md5sum "$tmpdir/boot/grub/loopback.cfg" | cut -f1 -d ' ')
sed -i -e 's,^.*[[:space:]] ./boot/grub/loopback.cfg,'"$md5"'  ./boot/grub/loopback.cfg,' "$tmpdir/md5sum.txt"
log "Updated hashes."

log "Repackaging extracted files into an ISO image..."
destination_iso=/tmp/`uuidgen`.iso
cd "$tmpdir"
xorriso -as mkisofs -r -V "ubuntu-autoinstall-$today" -J -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -isohybrid-mbr /usr/lib/ISOLINUX/isohdpfx.bin -boot-info-table -input-charset utf-8 -eltorito-alt-boot -e boot/grub/efi.img -no-emul-boot -isohybrid-gpt-basdat -o $destination_iso . &>/dev/null
cd "$OLDPWD"
log "Repackaged into $destination_iso"

log "Upload modified iso to vcenter..."
curl --insecure --silent --noproxy ${VCENTER_NAME} -u ${VCENTER_USERNAME}:'${VCENTER_PASSWORD}' -X PUT --data-binary @$destination_iso "https://${VCENTER_NAME}/folder${KS_FILENAME}?dcPath=${VCENTER_DATACENTER}&dsName=${VCENTER_DATASTORE}"
log "Uploaded to /ubuntu-custom.iso in datastore datastore1"

log "Delete iso file $source_iso"
rm -f $source_iso

log "Delete iso file $destination_iso"
rm -f $destination_iso

log "Completed."
exit 0