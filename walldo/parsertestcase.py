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
from walldo.parser import Parser;

class ParserTestCase(unittest.TestCase):
    lines = ['<select class="select" style="margin: 0 2px 0 0; margin-top: 4px; float: left; width: 145px; max-width: 145px;" name="resolution" onChange="javascript:imgload(\'ithilien\', this,\'2949\')">']
    expected = ['/wallpaper/7yz4ma1/2949_ithilien_1024x768.jpg']

    def setUp(self):
        self.parser = Parser()

    def testParse(self):
        current = self.parser.parse(self.lines, '1024x768')
        for i in range(len(current)):
            self.assertEquals(self.expected[i], current[i], 'Entry incorrect')
