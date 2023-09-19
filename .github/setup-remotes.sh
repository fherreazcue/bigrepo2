#!/usr/bin/env bash

# remote_name='python-release-workflow'
# remote_url='https://github.com/hpcflow/python-release-workflow.git'
# dirs_to_sync='.github/'

remote_name='shared1'
remote_url='https://github.com/fherreazcue/sharedcode.git'
dirs_to_sync='./'

git remote add ${remote_name} ${remote_url}
git remote set-url --push ${remote_name} no-pushing

# git fetch --all
# git checkout ${remote_name} -- ${dirs_to_sync}