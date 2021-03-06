import maya.cmds as cmds
import cPickle, os, imp, types
import pymel.core as pm

def pyToAttr(objAttr, data):
	"""
	Write (pickle) Python data to the given Maya obj.attr.  This data can
	later be read back (unpickled) via attrToPy().

	Arguments:
	objAttr : string : a valid object.attribute name in the scene.  If the
		object exists, but the attribute doesn't, the attribute will be added.
		The if the attribute already exists, it must be of type 'string', so
		the Python data can be written to it.
	data : some Python data :  Data that will be pickled to the attribute
		in question.
	"""
	obj, attr = objAttr.split('.')
	# Add the attr if it doesn't exist:
	if not cmds.objExists(objAttr):
		cmds.addAttr(obj, longName=attr, dataType='string')
	# Make sure it is the correct type before modifing:
	if cmds.getAttr(objAttr, type=True) != 'string':
		raise Exception("Object '%s' already has an attribute called '%s', but it isn't type 'string'"%(obj,attr))

	# Pickle the data and return the coresponding string value:
	stringData = cPickle.dumps(data)
	# Make sure attr is unlocked before edit:
	cmds.setAttr(objAttr, edit=True, lock=False)
	# Set attr to string value:
	cmds.setAttr(objAttr, stringData, type='string')
	# And lock it for safety:
	cmds.setAttr(objAttr, edit=True, lock=True)

def attrToPy(objAttr):
	"""
	Take previously stored (pickled) data on a Maya attribute (put there via
	pyToAttr() ) and read it back (unpickle) to valid Python values.

	Arguments:
	objAttr : string : A valid object.attribute name in the scene.  And of course,
		it must have already had valid Python data pickled to it.

	Return : some Python data :  The reconstituted, unpickled Python data.
	"""
	# Get the string representation of the pickled data.  Maya attrs return
	# unicode vals, and cPickle wants string, so we convert:
	stringAttrData = str(cmds.getAttr(objAttr))
	# Un-pickle the string data:
	loadedData = cPickle.loads(stringAttrData)

	return loadedData

# Compile Py from Ui
def compileUI():
	print "COMPILE"
	from pyside2uic import compileUi
	
	moduleName = __name__.split('.')[0]
	print moduleName
	modulePath = os.path.abspath(imp.find_module(moduleName)[1])
	
	pyfile = open(modulePath+'\\matchRig_mainWindow.py', 'w')
	compileUi(modulePath+"\\matchRig_mainWindow.ui", pyfile, False, 4,False)
	pyfile.close()

	pyfile2 = open(modulePath+'\\matchRig_bakeWindow.py', 'w')
	compileUi(modulePath+"\\matchRig_bakeWindow.ui", pyfile2, False, 4,False)
	pyfile2.close()
	
def fixName(name):
	i = 1
	initName = name
	while cmds.objExists(name):
		name = initName + str(i)
		i += 1
	return name	

def fixShapeName(name):
	shape = cmds.listRelatives(name)[0]
	cmds.rename(shape, name+"Shape")
	return shape

def getShape(name):
	shape = cmds.listRelatives(name)[0]
	return shape

def resetAttrs(o):
	cmds.setAttr(o+".tx", 0)
	cmds.setAttr(o+".ty", 0)
	cmds.setAttr(o+".tz", 0)
	cmds.setAttr(o+".rx", 0)
	cmds.setAttr(o+".ry", 0)
	cmds.setAttr(o+".rz", 0)	
	
def setColor(o, color):
	cmds.setAttr(o+".overrideEnabled", 1)
	cmds.setAttr(o+".overrideColor", color)
	
def getSetObjects(set):
	objects = []
	if type(cmds.sets(set, q=1)) is types.NoneType:
		return []
	#print pm.sets(set, q=1)
	for o in pm.sets(set, q=1):
		#print pm.objectType(o)
		if pm.objectType(o) == 'objectSet':
			innerObjects = getSetObjects(o.name())
			objects += innerObjects
		else:
			objects.append(o)
	return objects

def setUserAttr(obj, attrName, value, type="string"):

	# create attribute if not exists
	if not cmds.attributeQuery(attrName, n=obj, exists=True ):

		if type == "string":
			cmds.addAttr(obj, longName=attrName, dt=type, keyable=False)

		elif type == "bool":
			cmds.addAttr(obj, longName=attrName, at=type, keyable=False)

		elif type == "data":
			pyToAttr(obj+'.'+attrName, value)

	# set attribute value
	cmds.setAttr(obj+"."+attrName, e=1, l=0)

	if type == "string":
		cmds.setAttr(obj+"."+attrName, value, type="string")
	elif type == "bool":
		cmds.setAttr(obj+"."+attrName, value)
	elif type == "data":
		pyToAttr(obj+'.'+attrName, value)		

	cmds.setAttr(obj+"."+attrName, e=1, l=True )