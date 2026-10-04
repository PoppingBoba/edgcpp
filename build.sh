#!/bin/bash
export PATH=$PATH:/usr/lib/llvm-22/bin/

gn gen out/
ninja -C out/