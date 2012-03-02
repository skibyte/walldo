Walldo
======
Walldo is a program written in Python which downloads wallapapers from 
http://interfacelift.com .

Contact
-------
Fernando Castillo skibyte@gmail.com

Installation
------------
See INSTALL file for details

Usage
-----
* Execute walldo for first time and a .walldorc file will be created in your 
  $HOME directory.
* Edit .walldorc and uncomment the desired resolutions and their respectives
  directories where the wallpapers will be downloaded.
* Execute walldo again.
* A progress indicator will appear showing that walldo is downloading 
  wallpapers (10 by default).

Walldo options
--------------
* -d        Download web pages based on the date.
* -r        Download web pages based on the raiting.
* -D        Download web pages based on the downloads.
* -n        Specify number of wallpapers to download (default 10).
* -c <file> Specify configuration file to use.
* -s        Print supported resolutions of wallpapers.
* -h        help menu.

Walldo configuration file format
--------------------------------
If a configuration file is not provided in command line walldo will search in $HOME/.walldorc
This file consists of lines with the following format:

[<wallpaper_resolution>]
directory = <directory where wallpapers will be downloaded>
Where <wallpaper_resolution> is one of the supported resolutions, returned by 'walldo -s'

### Samples
This will download wallpaper with a resolution of 1280x1024 intothe directory mywallpapers
[1280x1024]
directory = mywallpapers

This will download wallpaper with a resolution of 1920x1200into the directory mywallpapers
[1920x1200]
directory = wallpapers

License
-------
See COPYING file for details.
