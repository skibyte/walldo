# Walldo - A wallpaper downloader
# Copyright (C) 2012  Fernando Castillo skibyte@gmail.com
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 
"""
Walldo: A wallpaer downloader
@summary: 
@author: Fernando Castillo
"""

import re
from walldo import util
class Parser():
    """
    It parses the presentation webpage from www.interfacelift.com, extracting 
    important information to download wallpapers.
    """
    def __init__(self):
        pass

    def parse(self, lines, resolution):
        """
        Extracts the id image , name of the image and its resolution
        """
        mylist = []
        for line in lines:
            matches = re.match( \
                r'.*onchange="javascript:imgload\(\'(\w+)\',.+,\'(\d+)\'\).*',\
                line, re.I)
            if matches:
                mylist.append(util.getpath(matches.group(2), matches.group(1), \
                        resolution))

        return mylist

