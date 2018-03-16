# Argos Scripts

scripts that are used with [Argos Extension for Gnome](https://extensions.gnome.org/extension/1176/argos/). 

>Argos is a GNOME Shell extension that turns executables' standard output into panel dropdown menus. It is inspired by, and fully compatible with, the BitBar app for macOS. Argos supports many BitBar plugins without modifications, giving you access to a large library of well-tested scripts in addition to being able to write your own.

##Tilix

This script will put a menu option in the topbar that will give you a list of all your tilix session .json files and launch tilix with that session when you click on it. 

![alt text](https://raw.githubusercontent.com/spectre013/argosscripts/master/tilix.png "Tilix in action")


#### Install

On a gnome enabled desktop

Install gnome tweak tool if you do not have it 

```
 $sudo apt install gnome-tweak-tool

```

Make sure you have gnome shell extensions installed 

```
 $ gnome-shell --version
 #if not run 
 $ sudo apt install gnome-shell-extensions
```
In your browser go to Argos Extensino page and click the button in the upper right to turn on the shell extenstion.

https://extensions.gnome.org/extension/1176/argos/

Place your tilix session .json files in ~/tilix-spaces/
grouping them by projects by placing them in folders like so ~/tilix-spaces/project/session.json

Copy the tilix.py script to ~/.config/argos and make it executable. 
```
$ chmod +x  tilix.py 

```



