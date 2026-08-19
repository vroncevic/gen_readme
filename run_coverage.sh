#!/bin/bash
#
# @brief   gen_readme
# @version 1.1.7
# @date    Sat Aug 08 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_readme
pylint gen_readme > gen_readme.report
echo "Done"
