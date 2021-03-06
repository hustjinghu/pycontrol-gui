Spyce, Simple python circuit editor
=============
A simulink like editor with netlist support. Heavily borrowed from a similar project for pycontrol by Roberto Bucher
http://robertobucher.dti.supsi.ch/python/ for the SUPSI university. You will find many references to supsi :) and also
some remaining packages that we did not yet update or remove

The following packages should be installed on your PC

* Python 2.7+ or Python 3.5+
* Qt (see https://github.com/mottosso/Qt.py)
* PySide, PySide2, PyQt4 or PyQt5
* MyHDL (best with fixbv extension, see https://github.com/imec-myhdl/myhdl)
* LateX if you want to build the pdf documentation

* our setup is based on anaconda python 2.7 and PyQt4 


Installing as normal user:
--------------------------
1) Install Spyce (checkout with git)
```
   git clone https://github.com/imec-myhdl/pycontrol-gui.git
```
2) install the  dependencies with pip:
```
   pip install Qt.py
   pip install --user git+https://github.com/imec-myhdl/myhdl.git
```

Workspace preparation
---------------------
```
   mkdir workdir
   cd workdir
   
   # create settings.py this file to make local modifications to the defaults in supsisim/const.py
   
   # link common libraries
   mkdir libraries
   ln -s ~/pycontrol-gui/BlockEditor/libraries/* libraries
```

Editor (standalone)
-------------------
To start the editor you do not need a setup/make step. You can run it can directly without installing.
```
cd workdir
python ~/pycontrol-gui/BlockEditor/spyce.py
```
Documentation (standalone)
--------------------------
```
cd ~/pycontrol-gui/doc
make latexpdf # or make html whatever you prefer and is supported by sphinx
```
manual will be in build/latex/spyce.pdf

Warning:
--------
Dangerous software, do not run as superuser, and be aware that there are bugs that could cause lost work (save as wrong filename for example). UNDO function is not implemented.

22.11.2018 imec-nl
