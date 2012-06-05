#
# Walldo - A wallpaper downloader
# Copyright (C) 2012  Fernando Castillo 
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

from walldo.urlbuilder import URLBuilder
from walldo.sorting import Sort

import unittest

class URLBuilderTestCase(unittest.TestCase):
    def testGetNextPage_Rating(self):
        builder = URLBuilder(Sort.RATING)
        self.assertEquals(
                'http://interfacelift.com/wallpaper/downloads/rating/any/index1.html',
                builder.getnextpage(), 'url is incorrect')

    def testGetNextPage_Date(self):
        builder = URLBuilder(Sort.DATE)
        self.assertEquals(
                'http://interfacelift.com/wallpaper/downloads/date/any/index1.html',
                builder.getnextpage(), 'url is incorrect')

    def testGetNextPage_Downloads(self):
        builder = URLBuilder(Sort.DOWNLOADS)
        self.assertEquals(
                'http://interfacelift.com/wallpaper/downloads/downloads/any/index1.html',
                builder.getnextpage(), 'url is incorrect')

