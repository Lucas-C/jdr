#!/bin/bash
# INSTALL: npm install -g https://github.com/gpotter2/sketchviz#d977905
set -o pipefail -o errexit -o nounset
cd $(dirname ${BASH_SOURCE[0]})

# sketchviz scenario.dot scenario.svg
sketchviz scenario1.dot scenario1.svg
sketchviz scenario2.dot scenario2.svg
