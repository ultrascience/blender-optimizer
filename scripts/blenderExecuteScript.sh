#!/bin/bash

find . -name '*.blend' -exec blender {} --background --python $1 \;
