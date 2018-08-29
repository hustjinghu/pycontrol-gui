name = 'Gain' #zelfde als bestand naam 
libname = 'common' #zelfde als map naam

inp = 1
outp = 1

parameters = dict(inp=1,outp=1)
properties = {'name': 'matmultBlk', 'Gains': ' 1'} #voor netlisten
#view variables:
iconSource = 'MULT'
textSource = 'libraries/library_common/Gain.py'



import supsisim.block 

def getSymbol(param,parent=None,scene=None,):
    attributes = dict()
    attributes['name'] = name
    attributes['libname'] = libname
    attributes['input'] = param['inp'] if 'inp' in param else inp
    attributes['output'] = param['outp'] if 'outp' in param else outp
    attributes['icon'] = iconSource
    
    
    return supsisim.block.Block(attributes,param,properties,name,libname,parent,scene)
    

views = {'icon':iconSource,'text':textSource}