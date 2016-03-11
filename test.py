
import readEpanetFile as d

d.LoadFile('BWSN1_Ostfeld2008.inp') # BWSN1_Ostfeld2008 # Net1_Rossman2000

print 'Epanet File Info:'
print d.BinUpdateClass()

#print d.getBinNodeCoordinates()

print 'Get Junction Count:'
print d.getBinNodeJunctionCount()

print 'Get Reservoir Count:'
print d.getBinNodeReservoirCount()

print 'Get Junction Name ID:'
print d.getBinNodeJunctionNameID()

print 'Get Reservoir Name ID:'
print d.getBinReservoirNameID()

print 'Get Node Name ID:'
print d.getBinNodeNameID()

print 'Get Node Elevations:'
#print d.getBinNodeElevations()
print d.getBinNodeReservoirElevations()
print d.getBinNodeJunctionElevations()
print d.getBinNodeTankElevations()

print 'Get Node Basedemands:'
print d.getBinNodeBaseDemands()

print 'Tank Name IDs:'
print d.getBinNodeTankNameID()

print 'Get Node Tank Init Level:'
print d.getBinNodeTankInitLevel()

print 'Get Node Tank Min Level:'
print d.getBinNodeTankMinLevel()

print 'Get Node Tank Max Level:'
print d.getBinNodeTankMaxLevel()

print 'Get Node Tank Diameter:'
print d.getBinNodeTankDiameter()

print 'Get Node Tank Min Vol:'
print d.getBinNodeTankMinVol()

print 'Get Pipe Name ID:'
print d.getBinLinkPipeNameID()

print 'Pipe Count:'
print d.getBinLinkPipeCount()

print 'Link From Node ID:'
print d.getBinLinkFromNode()

print 'Link To Node ID:'
print d.getBinLinkToNode()

print 'Link Pipe Lengths:'
print d.getBinLinkPipeLengths()

print 'Link Pipe Diameters:'
print d.getBinLinkPipeDiameters()

print 'Link Pipe Roughness:'
print d.getBinLinkPipeRoughness()

print 'Link Pipe Minor Loss:'
print d.getBinLinkPipeMinorLoss()

print 'Link Pump Name ID:'
print d.getBinLinkPumpNameID()

print 'Pump Count:'
print d.getBinLinkPumpCount()

print 'Link Pump Patterns ID:'
print d.getBinLinkPumpPatterns()

print 'Link Pump Curve Name ID:'
print d.getBinLinkPumpCurveNameID()

print 'Link Pump Power:'
print d.getBinLinkPumpPower()

print 'Link Pump Name ID Power:'
print d.getBinLinkPumpNameIDPower()

#Get Valves Info
print 'Valve Count:'
print d.getBinLinkValveCount()

print 'Valve Name ID:'
print d.getBinLinkValveNameID()

print 'Valve Diameters:'
print d.getBinLinkValveDiameters()

print 'Valve Type:'
print d.getBinLinkValveType()

print 'Valve Setting:'
print d.getBinLinkValveSetting()

print 'Valve Minor Loss:'
print d.getBinLinkValveMinorLoss()
