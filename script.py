#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getpass
import subprocess


def whereis(app):
    result = None

    try:
        result = subprocess.check_output(["whereis", app])
    except:
        print("Flutter not found")

    if result is None:
        print("Flutter not found")
        return []

    result = result.decode().splitlines()
    return [line for line in result if len(line)][0].split(" ")[1:][0]


path = f"/home/{getpass.getuser()}/snap/flutter/common/flutter/packages/flutter_tools/lib/src/web/chrome.dart"

# Read in the file
with open(path, "r") as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace("--disable-extensions", "--disable-web-security")

# Write the file out again
with open(path, "w") as file:
    file.write(filedata)


print("Done!")
