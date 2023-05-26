#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

getent passwd kni
exit_code=$?

if [ $exit_code -eq 0 ]; then
    echo User kni already exists
    exit 0
fi

echo User kni does not exist yet
useradd kni
exit_on_error $?
echo User kni created

usermod --password $(echo kni | openssl passwd -1 -stdin) kni
exit_on_error $?
echo User kni password set to kni

echo "kni ALL=(root) NOPASSWD:ALL" | tee -a /etc/sudoers.d/kni
exit_on_error $?
echo User kni added to sudoers

chmod 0440 /etc/sudoers.d/kni
exit_on_error $?
echo sudoers chmod 0440

su - kni -c "ssh-keygen -t ed25519 -f /home/kni/.ssh/id_rsa -N ''"
exit_on_error $?
echo User kni ssh key ed25519 created

exit 0