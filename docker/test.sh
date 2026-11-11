#!/bin/sh

set -e

PATH="/home/microblog/.venv/bin:$PATH"
export PATH
exec make test
