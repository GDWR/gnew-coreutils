#!/usr/bin/env bash

for BINARY in ./cmd/*.go; do
  go build  -o ./build "$BINARY"
done
