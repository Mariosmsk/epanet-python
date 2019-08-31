import readEpanetFile as d
#from Epa2Shp import epaShp

#epaShp('BWSN1_Ostfeld2008.inp')

d.LoadFile('Net1_Rossman2000.inp') # BWSN1_Ostfeld2008 # Net1_Rossman2000 example_temp test

print('Epanet File Info:')
print(d.BinUpdateClass())

print(d.getBinCurvesNameID())
print(d.getBinCurveCount())
print(d.getBinCurvesXY())

print(d.getBinLinkInitialStatus())
print(d.getBinLinkInitialStatusNameID())


print(d.getBinNodeCoordinates())
print(d.getBinNodesConnectingLinksID())
print(d.getBinNodesConnectingLinksIndex())

print(d.getBinLinkLength())
print(d.getBinLinkDiameter())
print(d.getBinLinkRoughnessCoeff())
print(d.getBinLinkMinorLossCoeff())

print('Get Reservoir Index')
print(d.getBinNodeReservoirIndex())

print('Get Tank Index')
print(d.getBinNodeTankIndex())

print('Get Pumps index:')
print(d.getBinLinkPumpIndex())

print('Get Valves index:')
print(d.getBinLinkValveIndex())

print('Get Node Demand Pattern ID:')
print(d.getBinNodeDemandPatternID())

print('Get Junction Count:')
print(d.getBinNodeJunctionCount())

print('Get Reservoir Count:')
print(d.getBinNodeReservoirCount())

print('Get Junction Name ID:')
print(d.getBinNodeJunctionNameID())

print('Get Reservoir Name ID:')
print(d.getBinReservoirNameID())

print('Get Node Name ID:')
print(d.getBinNodeNameID())

print('Get Node Elevations:')
#print(d.getBinNodeElevations())
print(d.getBinNodeReservoirElevations())
print(d.getBinNodeJunctionElevations())
print(d.getBinNodeTankElevations())

print('Get Node Basedemands:')
print(d.getBinNodeBaseDemands())

print('Tank Name IDs:')
print(d.getBinNodeTankNameID())

print('Get Node Tank Init Level:')
print(d.getBinNodeTankInitialLevel())

print('Get Node Tank Min Level:')
print(d.getBinNodeTankMinimumWaterLevel())

print('Get Node Tank Max Level:')
print(d.getBinNodeTankMaximumWaterLevel())

print('Get Node Tank Diameter:')
print(d.getBinNodeTankDiameter())

print('Get Node Tank Min Vol:')
print(d.getBinNodeTankMinimumWaterVolume())

print('Get Pipe Name ID:')
print(d.getBinLinkPipeNameID())

print('Pipe Count:')
print(d.getBinLinkPipeCount())

print('Link From Node ID:')
print(d.getBinLinkFromNode())

print('Link To Node ID:')
print(d.getBinLinkToNode())

print('Link Pipe Lengths:')
print(d.getBinLinkPipeLengths())

print('Link Pipe Diameters:')
print(d.getBinLinkPipeDiameters())

print('Link Pipe Roughness:')
print(d.getBinLinkPipeRoughness())

print('Link Pipe Minor Loss:')
print(d.getBinLinkPipeMinorLoss())

print('Link Pump Name ID:')
print(d.getBinLinkPumpNameID())

print('Pump Count:')
print(d.getBinLinkPumpCount())

print('Link Pump Patterns ID:')
print(d.getBinLinkPumpPatterns())

print('Link Pump Curve Name ID:')
print(d.getBinLinkPumpCurveNameID())

print('Link Pump Power:')
print(d.getBinLinkPumpPower())

print('Link Pump Name ID Power:')
print(d.getBinLinkPumpNameIDPower())

#Get Valves Info
print('Valve Count:')
print(d.getBinLinkValveCount())

print('Valve Name ID:')
print(d.getBinLinkValveNameID())

print('Valve Diameters:')
print(d.getBinLinkValveDiameters())

print('Valve Type:')
print(d.getBinLinkValveType())

print('Valve Setting:')
print(d.getBinLinkValveSetting())

print('Valve Minor Loss:')
print(d.getBinLinkValveMinorLoss())
