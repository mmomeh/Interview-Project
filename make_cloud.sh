#!/bin/bash
set -e
trap 'echo deactivate' EXIT 
python point_cloud.py 2>/dev/null
