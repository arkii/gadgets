---
layout: post
title: BitBar plugin icinga2 overview
date: 2016.01.25 10:42 +08:00
---
#MacBitBar Plugin icinga2-api-overview.py

Plugin to show icinga2 tactical overview, developed by python, in order to use this plugin, you should enable icinga2-api first.

##Screenshot
![](/icinga2-api-overview.png)

##Install MacBitBar
Download the latest package from site below
[https://github.com/matryer/bitbar/releases](https://github.com/matryer/bitbar/releases)
Or install it by brew cask
`brew cask install bitbar`

##Get plugin
[https://github.com/arkii/gadgets/blob/master/Utility/BitBar/icinga2-api-overview.py](https://github.com/arkii/gadgets/blob/master/Utility/BitBar/icinga2-api-overview.py)

##Install Plugin
Just download the plugin of your choice into your BitBar plugins directory and choose Refresh from one of the BitBar menu.

``` bash
chmod +x icinga2-api-overview.py
cd Plugins/Enabled
# Enable uptime plugin and change update interval to 30 seconds
ln -s ../Utility/icinga2-api-overview.py icinga.30s.py
```

##Other plugins built by me
[https://github.com/arkii/gadgets/Utility/BitBar/](https://github.com/arkii/gadgets/blob/master/Utility/BitBar/)

##MacBitBar

Homepage:
[https://getbitbar.com](https://getbitbar.com)
Projects:
[BitBar](https://github.com/matryer/bitbar)
[BitBar-Plugins](https://github.com/matryer/bitbar-plugins)


