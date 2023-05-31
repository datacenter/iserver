#!/bin/bash

KEYFILE=/root/.ssh/id_ed25519
if [ -f "$KEYFILE" ]; then
    exit 0
fi

ssh-keygen -t ed25519 -N "" -f $KEYFILE