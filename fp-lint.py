#!/usr/bin/env python3

__license__ = 'MIT'

import argparse
import json
import os
import yaml

from manifest import Manifest
from linter import Linter

parser = argparse.ArgumentParser()
parser.add_argument('manifests', nargs='*')

opts = parser.parse_args()

def load_manifest_json(manifest):
    with open(manifest) as f:
        data = f.read()
        m = json.loads(data)
    return m

def load_manifest_yaml(manifest):
    with open(manifest) as f:
        try:
            m = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
        # YAML use "app-id"
        m["id"] = m["app-id"]
    return m

def lint_manifest(manifest):
    m = None
    _, ext = os.path.splitext(manifest)
    if ext == '.json':
        m = load_manifest_json(manifest)
    elif ext == ".yml" or ext == ".yaml":
        m = load_manifest_yaml(manifest)
    else:
        print("Extension not supported", ext)

    if m == None:
        print("Error loading manifest")
        return False

    mobj = Manifest(m)

    # Run the linter
    linter = Linter(mobj)
    lints = linter.lint()

    for l in lints:
        print(l)
    if len(lints) > 0:
        print("{} warnings".format(len(lints)))

    return True;

manifests = []
if opts.manifests:
    manifests = opts.manifests
else:
    exit('At least one manifest must be specified')


for manifest in manifests:
    lint_manifest(manifest)
