name = 'Prod' #zelfde als bestand naam 
libname = 'math' #zelfde als map naam

inp = 2
outp = 1

parameters = dict(inp=2,outp=1)
properties = {'name': 'prodBlk'} #voor netlisten
#view variables:
iconSource = 'PROD'
textSource = 'libraries/library_math/Prod.py'



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