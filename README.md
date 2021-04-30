# microkeeper-automation

Microkeeper is a shift tracking tool that requires employees to clock on and clock off.\
For anyone with a full time position, this is very annoying, so I've automated it.\
\
Systemd service files assume clockon.py and clockoff.py are in ~/bin in the users home directory\
Modify clockon.py and clockoff.py to fill your unsername and password\

Copy .service and .timer files into ~/.config/systemd/user/
```
$ systemctl --user enable clocko*
```
