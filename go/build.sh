#!/usr/bin/env bash

mkdir build --parents

for BINARY in ./src/*.go; do
  go build  -o ./build "$BINARY"
done
