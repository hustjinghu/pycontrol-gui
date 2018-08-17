#!/usr/bin/python
# aim for python 2/3 compatibility
from __future__ import (division, print_function, absolute_import,
                        unicode_literals)

from  Qt import QtGui, QtWidgets, QtCore # see https://github.com/mottosso/Qt.py


#if sys.version_info>(3,0):
#    import sip
#    sip.setapi('QString', 1)

from supsisim.const import PW

class Port(QtWidgets.QGraphicsPathItem):
    """A block holds ports that can be connected to."""
    def __init__(self, parent, scene, name = ''):
        if QtCore.qVersion().startswith('5'):
            super(Port, self).__init__(parent)
        else:
            super(Port, self).__init__(parent, scene)
        self.block = None
        self.name = ''
        self.line_color = QtCore.Qt.black
        self.fill_color = QtCore.Qt.black
        self.p = QtGui.QPainterPath()
        self.connections = []
        self.nodeID = '0'
        self.parent = parent
        self.pinlabel = None

    def setup(self):
        pass

    def itemChange(self, change, value):
        if change == self.ItemScenePositionHasChanged:
            for conn in self.connections:
                try:
                    conn.update_pos_from_ports()
                    conn.update_path()
                except AttributeError:
                    self.connections.remove(conn)
        return value

    def is_connected(self, other_port):
        for conn in self.connections:
            if conn.port1 == other_port or conn.port2 == other_port:
                return True
        return False

    def remove(self):
        for conn in self.connections:
            try:
                conn.remove()
            except:
                pass
        try:
            self.scene().removeItem(self)
        except AttributeError:
            pass

            try:
                self.scene().removeItem(self)
            except AttributeError:
                pass

class InPort(Port):
    def __init__(self, parent, scene, name=''):
        super(InPort, self).__init__(parent, scene)
        self.name = name
        self.setup()

    def __str__(self):
        txt  = 'InPort \n'
        txt += 'Parent : ' + self.parent.name + '\n'
        txt += 'Node ID :' + self.nodeID + '\n'
        txt += 'Connections: ' + (len(self.connections)).__str__() + '\n'
        return txt
    
    def setup(self):
        self.setPen(self.line_color)
        self.setBrush(self.fill_color)
        self.p.addRect(-PW/2, -PW/2, PW, PW)
        self.setPath(self.p)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

class OutPort(Port):
    def __init__(self, parent, scene, name=''):
        super(OutPort, self).__init__(parent, scene)
        self.name = name
        self.setup()

    def __str__(self):
        txt  = 'OutPort \n'
        txt += 'Parent : ' + self.parent.name + '\n'
        txt += 'Node ID :' + self.nodeID + '\n'
        txt += 'Connections: ' + (len(self.connections)).__str__() + '\n'
        return txt
    
    def setup(self):
        self.setPen(self.line_color)
        self.setBrush(self.fill_color)
        self.p.addEllipse(-PW/2, -PW/2, PW, PW)
        self.setPath(self.p)
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)
         
class InNodePort(Port):
    def __init__(self, parent, scene):
        super(InNodePort, self).__init__(parent, scene)
        self.setup()

    def __str__(self):
        txt  = 'Node In \n'
        txt += 'Connections: ' + (len(self.connections)).__str__() + '\n'
        return txt

    def setup(self):
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

class OutNodePort(Port):
    def __init__(self, parent, scene):
        super(OutNodePort, self).__init__(parent, scene)
        self.setup()

    def __str__(self):
        txt  = 'Node Out \n'
        txt += 'Connections: ' + (len(self.connections)).__str__() + '\n'
        return txt

    def setup(self):
        self.setFlag(QtWidgets.QGraphicsItem.ItemSendsScenePositionChanges)

