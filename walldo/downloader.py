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
"""

import urllib2
import os.path

class Downloader():
    """
    This class handles the process of downloading wallpapers.
    """

    def __init__(self, total):
        self.total = total
        self.counter = 0

    def download(self, resource):
        """
        Creates an url request pointing to a certain resource.
        """
        headers = {'User-Agent': \
                'Mozilla/5.0 (X11; Linux x86_64; rv:5.0) \
                        Gecko/20100101 Firefox/5.0'}
        req = urllib2.Request(resource, None, headers)
        return urllib2.urlopen(req)

    def downloadandsave(self, resource, directory, filename):
        """
        Downloads the wallpaper 
        """
        self.counter += 1
        percent = (self.counter * 100) / self.total
        path = directory + os.sep + filename
        if os.path.isfile(path):
            print "[%3d%%] - %s already exists." % (percent, filename)

        else:
            myfile = self.download(resource)
            print "[%3d%%] - Downloading %s" % (percent, resource)
            local = open(path, 'w')
            local.write(myfile.read())
            local.close()
