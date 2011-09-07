from Globals import InitializeClass
# from AccessControl import ClassSecurityInfo

from Products.ZenRelations.RelSchema import *
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenUtils.Utils import convToUnits

from Products.ZenModel.ZenossSecurity import ZEN_VIEW, ZEN_CHANGE_SETTINGS

_kw = dict(mode='w')

class BladeServer(DeviceComponent, ManagedEntity):
    "Blade Server Information"
    
    portal_type = meta_type = 'BladeServer'

    bsDisplayName = ""
    bsId = ""
    bsPosition = -1
    bsHeight = -1
    bsWidth = -1
    bsDepth = -1
    bsSlotsUsed = -1
    bsSerialNum = ""
    bsProductId = ""
    bsPartNumber = ""
    bsSystemBoardPartNum = ""
    bsCPUType = ""
    bsCPUCount = 0
    bsNic1Mac = ""
    bsNic2Mac = ""
    bsIloIp = ""
    bsInstalledRam = -1
    bsIloFirmwareVersion = ""
    snmpindex = -1

    _properties = (
	dict(id='bsDisplayName', type='string',  **_kw),
	dict(id='bsId', type='string',  **_kw),
	dict(id='bsPosition', type='int',  **_kw),
	dict(id='bsHeight', type='int',  **_kw),
	dict(id='bsWidth',	type='int',  **_kw),
	dict(id='bsDepth',	type='int',  **_kw),
	dict(id='bsSlotsUsed',type='int',  **_kw),
	dict(id='bsSerialNum', type='string',	**_kw),
	dict(id='bsProductId', type='string',	**_kw),
	dict(id='bsPartNumber', type='string',	**_kw),
	dict(id='bsSystemBoardPartNum', type='string',	**_kw),
	dict(id='bsCPUType', type='string',	**_kw),
	dict(id='bsCPUCount', type='int',	**_kw),
	dict(id='bsNic1Mac', type='string',	**_kw),
	dict(id='bsNic2Mac', type='string',	**_kw),
	dict(id='bsIloIp', type='string',	**_kw),
	dict(id='bsIloFirmwareVersion', type='string',	**_kw),
	dict(id='bsInstalledRam', type='int',	**_kw)
    )

    _relations = (
	('bladechassis', ToOne(ToManyCont, 'ZenPacks.community.HPBladeChassis.BladeChassis', 'bladeservers')),
    )

    # Screen action bindings (and tab definitions)
    factory_type_information = (
	{
	    'id'             : 'BladeServer',
	    'meta_type'      : 'Blade Server',
	    'description'    : 'Blade Server Description',
	    'icon'           : 'Device_icon.gif',
	    'product'        : 'BladeServers',
	    'factory'        : 'manage_addBladeServer',
	    'immediate_view' : 'viewBladeDetail',
	    'actions'        :
	    (
		{ 'id'            : 'detail'
		, 'name'          : 'Blade Detail'
		, 'action'        : 'viewBladeDetail'
		, 'permissions'   : (ZEN_VIEW, )
		},
		{ 'id'            : 'templates'
		, 'name'          : 'Templates'
		, 'action'        : 'objTemplates'
		, 'permissions'   : (ZEN_CHANGE_SETTINGS, )
		},
	    )
	},
    )

    def device(self):
	return self.bladechassis()

    def managedDeviceLink(self):
	from Products.ZenModel.ZenModelRM import ZenModelRM
	d = self.getDmdRoot("Devices").findDevice(self.bsDisplayName)
	if d:
	    return ZenModelRM.urlLink(d, 'link')
	return None

    def snmpIgnore(self):
	return ManagedEntity.snmpIgnore(self) or self.snmpindex < 0
    

InitializeClass(BladeServer)
