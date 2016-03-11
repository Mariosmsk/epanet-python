
import readEpanetFile as d

d.LoadFile('Net1_Rossman2000.inp')

print 'Epanet File Info:'
print d.BinUpdateClass()

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
print d.getBinNodeElevations()

print 'Get Node Basedemands:'
print d.getBinNodeBaseDemands()

