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
Walldo: a wallpaper downloader 
@summary: 
@author: Fernando Castillo
@contact: skibyte@gmail.com
"""

def isresolutionsupported(resolution):
    """
    @rtype: bool
    @return: True if the resolution is supported
    """
    return resolution in getsupportedresolutions()


def getsupportedresolutions():
    """
    @return: The resolutions supported by walldo
    """
    supportedresolutions = [
     "2048x2048",
     "1024x1024",
     "640x960",
     "320x480",
     "360x480",
     "320x240",
     "3360x1050",
     "3200x1200",
     "2880x900",
     "2560x1024",
     "1600x1200",
     "1400x1050",
     "1280x960",
     "1024x768",
     "1280x1024",
     "1080x960",
     "960x854",
     "960x800",
     "640x480",
     "1920x1080",
     "1280x720",
     "1366x768",
     "1024x600",
     "800x480",
     "480x272",
     "320x400",
     "3072x768",
     "2560x1600",
     "1920x1200",
     "1680x1050",
     "1440x900",
     "1280x800",
     "2560x1440",
     "1600x900",
     "480x800"
     ]

    return supportedresolutions

# TODO: The magic number may change, a solution is parsing the file
# jscript.js
# which is the file where this number appear
def getpath(idimage, name, resolution):
    """
    Creates a valid url from interfacelift.com pointing to a wallpaper
    @param idimage: The id of the image to download
    @param name: The name of the image
    @param resolution: The resolution of the image
    @return: A path in the form /wallpaper/<number>/<id>/<name>/<resolution>.jpg
    """
    path = '/wallpaper/7yz4ma1/' + idimage + '_' + name + '_' + \
            resolution + '.jpg'
    return path
