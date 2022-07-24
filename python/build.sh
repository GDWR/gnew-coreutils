#!/usr/bin/env bash

mkdir build/ --parents

for SCRIPT_PATH in ./src/*.py; do
  cp "$SCRIPT_PATH" "build/$(basename "$SCRIPT_PATH" .py)"
done
