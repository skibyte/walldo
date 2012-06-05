#
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
Walldo: A wallpaper downloader
@summary: 
@author: Fernando Castillo
@contact: skibyte@gmail.com
"""

from walldo.sorting import Sort

class URLBuilder():
    """
    Creates urls to presentation webpages from interfacelift.com where the wallpapers
    are view as thmbnails
    """
    currentpage = 0
    sorting = Sort.DATE

    def __init__(self, sort):
        self.sorting = sort
        self.currentpage = 0

    def getnextpage(self):
        """
        Return the next page from interfacelift
        @rtype: string
        @return: the x intercept of the line
        """

        self.currentpage += 1
        if self.sorting == Sort.RATING:
            return "http://interfacelift.com/wallpaper/downloads/" + \
            "rating/any/index" + str(self.currentpage) + ".html"
        elif self.sorting == Sort.DOWNLOADS:
            return "http://interfacelift.com/wallpaper/downloads/" + \
            "downloads/any/index" + str(self.currentpage) + ".html"
        else:
            return "http://interfacelift.com/wallpaper/downloads/" + \
           "date/any/index" + str(self.currentpage) + ".html"

    
    def reset(self):
        """
        Restore the class to its initial state
        """
        self.currentpage = 0
