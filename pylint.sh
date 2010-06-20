#!/bin/bash

# E1102: _ is not callable
# E1121: Too many positional arguments for function call
# C0103: Invalid name
# C0111: Missing docstring
# C0301: Line too long
# C0302: Too many lines in module
# R0903: Too few public method
# R0904: Too many public methods
# R0912: Too many branches
# R0913: Too many arguments
# R0914: Too many local variables
# R0915: Too many statements
# R0201: Method could be a function
# W0142: Used * or ** magic
# W0612: Unused variable
# W0614: Unused import
# W0231: __init__ method from base class is not called
# W0232: Class has no __init__ method
# W0212: Access to a protected member _meta of a client class

pylint --include-ids=y \
    --ignore=migrations \
    --disable=C0103 \
    --disable=C0111 \
    --disable=C0301 \
    --disable=C0302 \
    --disable=R0201 \
    --disable=R0903 \
    --disable=R0904 \
    --disable=R0912 \
    --disable=R0913 \
    --disable=R0914 \
    --disable=R0915 \
    --disable=W0212 \
    --disable=W0231 \
    --disable=W0232 \
    --disable=W0142 \
    --disable=W0612 \
    --disable=W0614 \
    --disable=E1102 \
    --disable=E1121 \
    setup.py docs/conf.py flickrsets flickrsets_example
   