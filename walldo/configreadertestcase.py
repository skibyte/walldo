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
 
import unittest
from walldo.configreader import ConfigReader


class ConfigReaderTestCase(unittest.TestCase):
    def testRead(self):
        reader = ConfigReader()
        reader.read('walldo/test_file.txt')

        dictionary = reader.getdirectories()
        self.assertEquals('directory1', dictionary['1024x768'], 'Entry is incorrect')
        self.assertEquals('directory2', dictionary['1280x1024'], 'Entry is incorrect')
