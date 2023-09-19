#!/usr/bin/env python3

import subprocess

class remote:
    def __init__(self,remote_name,remote_url,dirs_to_sync="./",run_after_sync=None):
        self.remote_name = remote_name
        self.remote_url = remote_url
        self.dirs_to_sync = dirs_to_sync
        self.run_after_sync = run_after_sync

remotes = [
    remote(
        remote_name = "shared1",
        remote_url = "https://github.com/fherreazcue/sharedcode.git",
        dirs_to_sync = "./",
        run_after_sync = "python -c 'pp(\'hello\')'",
    ),
    remote(
        remote_name = "shared2",
        remote_url = "https://github.com/fherreazcue/shared2.git",
        dirs_to_sync = "d2 d3",
        run_after_sync = "",
    ),
]

for R in remotes:
    print(f"Adding remote {R.remote_url} as {R.remote_name}")
    subprocess.run(["git","remote","add",R.remote_name,R.remote_url])

    print(f"Configuring as no-push")
    subprocess.run(["git","remote","set-url","--push",R.remote_name,"no-pushing"])
    
    print(f"Fetching {R.remote_name}")
    subprocess.run(["git","fetch",R.remote_name])

    print(f"Pulling content from {R.remote_name}/main: {R.dirs_to_sync}")
    # subprocess.run(["git","checkout",f"{R.remote_name}/main","--",R.dirs_to_sync])
    subprocess.run(f"git checkout {R.remote_name}/main -- {R.dirs_to_sync}",shell=True)

