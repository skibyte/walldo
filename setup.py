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
 
from distutils.core import setup

setup(name="walldo",
        description="A wallpaper downloader",
        version="1.0",
        author="Fernando Castillo",
        author_email="skibyte@gmail.com",
        packages=["walldo"],
        keywords=["wallpaper", "downloader"],
        scripts=["walldo/walldo"],
        )
