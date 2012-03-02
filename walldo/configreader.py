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

import os.path
import sys
import ConfigParser

from walldo import util


class ConfigReader():
    """
    Config reader object
    """
    def __init__(self):
        self.directories = {}

    def read(self, config_file):
        """
            Format
            ======
                A walldo configuration file is formed of several entries like \
                this:
                [<resolution>]
                directory = <path>

                Where:
                <resolution> is one of the supported resolutions
                <path> is the directory where the wallpapers for the

                Sample
                ------
                [1280x1024]
                directory = mywallpapers

            Reads a configuration file
            @type config_file : string
            @param config_file : A path to the confioguration file

        """
        if not os.path.isfile(config_file):
            print "Configuration file: " + config_file + " does not exist"
            sys.exit(0)

        else:
            cfg = ConfigParser.RawConfigParser()
            cfg.read(config_file)
            for resolution in cfg.sections():
                if util.isresolutionsupported(resolution):
                    try:
                        self.directories[resolution] = \
                                cfg.get(resolution, "directory")
                    except ConfigParser.NoOptionError , detail:
                        print detail
                        print "Please edit: " + config_file + \
                        " to fix this problem.\n"

                else:
                    print "Resolution " + resolution + " is not supported"

    def getdirectories(self):
        """
        @rtype: dictionary
        @return : A dictionary with the following form, \
                <resolution>:<directory>

        """
        return self.directories
