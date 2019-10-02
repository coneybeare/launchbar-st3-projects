#!/usr/bin/env python
#
# LaunchBar Action Script
#
# Based on https://github.com/vqv/launchbar-st3-projects
# 
import sys
import os.path
import json

path = '~/Library/Application Support/Sublime Text 3/Local/Session.sublime_session'

# try:
with open(os.path.expanduser(path)) as json_data:
	session = json.load(json_data)

	try:
		folders	= session["folder_history"]
	except:
		folders = []

	try:
		files	= session["settings"]["new_window_settings"]["file_history"]
	except:
		files = []

items = [dict(title = os.path.basename(path),
							subtitle = path, 
              path = path,
              icon = "com.sublimetext.3",
              action = "actionURL.sh",
              actionArgument = path) 
          for path in  folders + files]

# items = files
print json.dumps(items)
