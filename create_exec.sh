#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit
fi

if [ -f "/usr/local/bin/quicktask" ]; then
    rm /usr/local/bin/quicktask
fi

cp quicktask.py /usr/local/bin/quicktask
chmod 755 /usr/local/bin/quicktask

which quicktask
echo 'try running with `quicktask`'