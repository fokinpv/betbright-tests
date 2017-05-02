#!/bin/bash
flake8 || exit 1
python3 -m unittest tests/test_*.py || exit 1
