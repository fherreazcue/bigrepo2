#!/usr/bin/env bash

remote_name='shared1'
remote_url='https://github.com/fherreazcue/sharedcode.git'
dirs_to_sync='./'

echo "Adding remote ${remote_url} as ${remote_name}"
git remote add ${remote_name} ${remote_url}
echo "Configuring as no-push"
git remote set-url --push ${remote_name} no-pushing
echo "Fetching ${remote_name}"
git fetch ${remote_name}
echo "Pulling content from ${remote_name}/main: ${dirs_to_sync}"
git checkout ${remote_name}/main -- ${dirs_to_sync}

remote_name='shared2'
remote_url='https://github.com/fherreazcue/shared2.git'
dirs_to_sync='d2 d3'

echo "Adding remote ${remote_url} as ${remote_name}"
git remote add ${remote_name} ${remote_url}
echo "Configuring as no-push"
git remote set-url --push ${remote_name} no-pushing
echo "Fetching ${remote_name}"
git fetch ${remote_name}
echo "Pulling content from ${remote_name}/main: ${dirs_to_sync}"
git checkout ${remote_name}/main -- ${dirs_to_sync}
