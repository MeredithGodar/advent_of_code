#!/bin/bash

cd day_01
pytest inverse_captcha_test.py

cd ../day_02
pytest corruption_checksum_test.py

cd ../day_03
pytest spiral_memory_test.py

cd ../day_04
pytest high_entropy_passphrases_test.py

cd ../day_05
pytest twisty_trampolines_test.py
