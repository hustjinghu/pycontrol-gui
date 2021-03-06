# cell definition
# name = 'LTI_continous'
# libname = 'common'

inp = 1
outp = 1

parameters = dict(inp=1,outp=1)
properties = {'Initial conditions': ' 0', 'name': 'cssBlk', 'System': ' sys'} #voor netlisten
#view variables:
iconSource = 'CSS'



import supsisim.block 

def getSymbol(param, properties,parent=None,scene=None,):
    attributes = dict()
    attributes['name'] = name
    attributes['libname'] = libname
    attributes['input'] = param['inp'] if 'inp' in param else inp
    attributes['output'] = param['outp'] if 'outp' in param else outp
    attributes['icon'] = iconSource
    
    
    return supsisim.block.Block(attributes,param,properties,name,libname,parent,scene)
    

views = {'icon':iconSource}
