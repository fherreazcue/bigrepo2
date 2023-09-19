#!/usr/bin/env python3

import argparse
import subprocess

parser = argparse.ArgumentParser(description="Script to configure and/or sync git remotes used in this repo.",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--no-config", action="store_true", help="Skip remote configuration, sync only")
parser.add_argument("--no-sync", action="store_true", help="Skip remote synchronization, config only")
parser.add_argument("--no-after", action="store_true", help="Skip run_after_sync commands")
args = parser.parse_args()

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
        run_after_sync = "python3 -c 'print(\"Hello form run_after_sync!!!\")'",
    ),
    remote(
        remote_name = "shared2",
        remote_url = "https://github.com/fherreazcue/shared2.git",
        dirs_to_sync = "d2 d3",
        run_after_sync = "",
    ),
]

existing=subprocess.run(["git","remote","show"],capture_output=True,text=True).stdout.splitlines()

for R in remotes:
    print("")
    if not args.no_config:
        if R.remote_name in existing:
            print(f"    Remote {R.remote_name} already exists, skipping config...")
        else:
            print(f"    Adding remote {R.remote_url} as {R.remote_name}")
            subprocess.run(["git","remote","add",R.remote_name,R.remote_url])

            print(f"    Configuring as no-push")
            subprocess.run(["git","remote","set-url","--push",R.remote_name,"no-pushing"])
    
    if not args.no_sync:
        if args.no_config and not R.remote_name in existing:
            print(f"    Remote {R.remote_name} is not configured, skipping sync...")
        else:
            print(f"    Fetching {R.remote_name}")
            subprocess.run(["git","fetch",R.remote_name])

            print(f"    Pulling content from {R.remote_name}/main: {R.dirs_to_sync}")
            subprocess.run(f"git checkout {R.remote_name}/main -- {R.dirs_to_sync}",shell=True)

            if R.run_after_sync and not args.no_after:
                print(f"    Running after-sync command: {R.run_after_sync}")
                subprocess.run(f"{R.run_after_sync}",shell=True)

print("")
