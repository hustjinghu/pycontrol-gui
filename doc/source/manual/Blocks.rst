###################
Building components
###################
.. index:: single: Building components
******
Blocks
******

.. index:: single: Blocks

Blocks are symbolic representations of circuit modules. A block must contain a number
of standard elements like pins, but can also include optional elements like tooltip or
netlisting functions.


Parameters and properties
=========================
.. index:: single: Parameters and properties

Blocks can have both parameters and properties. They control the behaviour of the 
block, The difference is that a parameter can change the *interface* of the blocks:
pin names, or number of pins. Properties *can* change the symbol, but *not* the pins.
Both properties and parameters are passed to the netlist. A paramerized Block is a block containing
a non empty *parameters* variable

Creating Blocks with the GUI
============================
.. index:: single: Creating Blocks with the GUI

In the library viewer right-click somewhere in empty space and choose *Create block*.
You can choose an icon if you can re-use an existing icon (but most of the time you 
will create a new one later). You add inputs, outputs, parameters and properties. 
After clicking OK the block is created in the current library.

When you right click on a block you can choose:

*edit icon*  to edit the icon, or generate an empty svg drawing when it is not yet present. 

*Edit pins* to edit pin-names and pin-positions, or add/delete pins

*Change BBox* to edit the bounding box

*Views* will allow you to edit any of the other views


Creating Blocks from code
=========================
.. index:: single: Creating Blocks from code

Blocks are simple python files that are inside a 'library'. The blocks should *not* import 
Qt as the netlister must be able to import them, without a gui. If Qt is needed or modules that import Qt
the easiest solution is to import them in the function that needs them (but never in the main, or netlist
routines). An Example::
    # cell definition
    # name = 'myblock'
    # libname = 'mylibrary'
    
    tooltip = 'This is an empty block with inputs a and b and output z'

    inp  = [('a', -40, -20), ('b', -40, 20)]
    outp = [('z', 40, 0)]
    io   = []
    bbox = None

    parameters = {} # pcell if not empty
    properties = {} # netlist properties

    #view variables:
    views = {'icon':'myblock.svg'}

.. py:data:: inp
.. py:data:: outp
.. py:data:: inout

*inp, outp, inout* are lists of tuples (pinname, x, y). The pinname can start with a `'.'` to indicate that the label should not be displayed. Alternatively *inp, outp, inout* can be an integer, being the number if inputs/outputs or inouts. The actual pins will be named '.i_0', '.i_1' etc. for inputs, '.o_0', '.o_1' etc. 
for outputs, or '.io_0', '.io_1' etc. for inouts. Note: inouts are optional and not yet properly implemented.

.. py:data:: tooltip
*tooltip* is an optional string that will be displayed when the mouse hoovers on the block.

.. py:data:: views
*views* is a dictionary that contains all (other) views. If *views['icon']* is defined it looks for
an svg file in either the *resources/blocks* directory (when no extension is specified) or in the same directory (library) as the block code otherwise.

.. py:data:: bbox
*bbox* is either *None*, or a 4-tuple: *(left, top, width, height)*

.. py:function:: ports(param)
This (optional, but highly recommended) function must return a tuple (inp, outp, inout), 
based on the parameters in the dictionary 'param'. Each of inp, outp, inout is a list of tuples 
(pinname, x, y). The pinname can start with a `'.'` to indicate that the label should not be displayed

.. py:function:: getSymbol(param, properties,parent=None,scene=None)
This function returns a :class:`Block` object. It is mandatory for parametrized blocks.
The getSymbol function will probably start with importing the block class, and Qt

.. py:function:: toMyhdlInstance(instname, connectdict, param)
This function should return a properly indented string (4 leading space) containing the MyHDL code.
It is required for myhdl netlisting a parametrized blocks. The instance name is the name of 
the block in the diagram. Connectdict is a dictionary with connections and properties 
(connectdict[pinname] = nettname or connectdict[property_name] = property_value)

.. py:function:: toSystemVerilogInstance(instname, connectdict, param)
This function should return a properly indented string (4 leading space) containing the SystemVerilog code.
It is required for SystemVerilog netlisting a parametrized block. The instance name is the name of 
the block in the diagram. Connectdict is a dictionary with connections and properties 
(connectdict[pinname] = nettname or connectdict[property_name] = property_value)

After importing a block the following defaults are added:
---------------------------------------------------------

.. py:data:: blockname
This is the name of the module (without the .py extension)

.. py:data:: libname
This is the name of the directory of the module (without the `'library_'` prefix)

.. py:data:: views
views will be extended with all views that are found (including the block-source itself)

