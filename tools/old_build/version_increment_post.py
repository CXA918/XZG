""" Remove version increment guard file if present """

import os

if os.path.exists("tools/.no_version_increment"):
    os.remove("tools/.no_version_increment")

#  Copyright (C) 2020  Davide Perini
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of
#  this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  You should have received a copy of the MIT License along with this program.
#  If not, see <https://opensource.org/licenses/MIT/>.
#
