__author__ = 'Mariosmsk'

import epanet as d
import numpy

#d.LoadLibrary('epanet2')
inpname = "Net1_Rossman2000.inp" # BWSN1_Ostfeld2008 , Net2_Rossman2000 , Net1_Rossman2000 , net1trace
d.LoadInpFile(inpname)


# get all functions
print d.getFunctionsImplement()

print d.getQualityInfo()

print d.getLinkPumpPower()
print 'Get Curves: %s'%d.getCurvesInfo()
print 'Get head curve idnex: %s'%d.getHeadCurveIndex()

print d.ENsimtime()
#hasattr
## Get version
print 'Get version: %s'%d.getVersion()

## Get type of the parameters
print 'Link Type Index: %s'%d.getLinkTypeIndex()
print 'Link Type: %s'%d.getLinkType()

print 'Node Type Index: %s'%d.getNodeTypeIndex()
print 'Node Type: %s'%d.getNodeType()

## Get all the countable network parameters
print 'Node Count: %s'%d.getNodeCount()
print 'Tank Reservoir Count: %s'%d.getNodeTankReservoirCount()
print 'Link Count: %s'%d.getLinkCount()
print 'Pattern Count: %s'%d.getPatternCount()
print 'Curve Count: %s'%d.getCurveCount()
print 'Control Rules Count: %s'%d.getControlRulesCount()

print 'Junction Count: %s'%d.getNodeJunctionsCount()
print 'Reservoir Count: %s'%d.getNodeReservoirCount()
print 'Tank Count: %s'%d.getNodeTankCount()

print 'Pipe Count: %s'%d.getLinkPipeCount()
print 'Pump Count: %s'%d.getLinkPumpCount()
print 'Valve Count: %s'%d.getLinkValveCount()

## Errors
a = (range(0,6),range(101,106),[110], [120], [200], range(202,207), range(223,224), range(240,241), range(250,251), range(301,309))
for i in range(0,len(a)):
    for e in range(0,len(a[i])):
        print d.getError(a[i][e])


## Retrieves the parameters of all control statements
# cindex:  control statement index
# ctype:   control type code EN_LOWLEVEL   (Low Level Control)
#                            EN_HILEVEL    (High Level Control)
#                            EN_TIMER      (Timer Control)
#                            EN_TIMEOFDAY  (Time-of-Day Control)
# lindex:  index of link being controlled
# setting: value of the control setting
# nindex:  index of controlling node
# level:   value of controlling water level or pressure for level controls
#          or of time of control action (in seconds) for time-based controls"""
#d.getControls() => TYPECONTROL[ctype.value] , ctype, lindex, nindex, setting, level
print 'Get Controls: %s'%d.getControls()


## Get the flow units
print 'Flow Units: %s'%d.getFlowUnits()
print 'Flow Units code: %s'%d.getFlowUnitsCode()


## Get all the link data
# Retrieves the ID label(s) of all links, or the IDs of an index set of links
print 'Link Name ID: %s'%d.getLinkNameID()
print 'Link Name ID for specific indices: %s'%d.getLinkNameID(2, 4, 5)
# Retrieves the indices of all links, or the indices of an ID set of links
print 'Link index: %s'%d.getLinkIndex()
print 'Link indices for specific ID:'
if inpname == 'Net1_Rossman2000.inp':
    print d.getLinkIndex('122', '113', '9')
elif inpname == 'Net2_Rossman2000.inp':
    print d.getLinkIndex('1', '10', '35')
elif inpname == 'BWSN1_Ostfeld2008.inp':
    print d.getLinkIndex('LINK-1', 'LINK-10', 'LINK-8')
# Retrieves the link-type code for all links.
print 'Link Type Index: %s'%d.getLinkTypeIndex()
# Retrieves the pipe index
print 'Link Pipe Index: %s'%[d.getLinkPipeIndex()]
# Retrieves the pump index
print 'Link Pump Index: %s'%d.getLinkPumpIndex()
# Retrieves the valve index
print 'Link Valve Index: %s'%d.getLinkValveIndex()
# Retrieves the value of all link diameters
print 'Link Diameter: %s'%d.getLinkDiameter()
# Retrieves the value of all link lengths
print 'Link Length: %s'%d.getLinkLength()
print 'Link Roughness: %s'%d.getLinkRoughnessCoeff()
# Retrieves the value of all link minor loss coefficients
print 'Link Minor loss coefficients: %s'%d.getLinkMinorLossCoeff()
# Retrieves the value of all link initial status
print 'Link Initial Status: %s'%d.getLinkInitialStatus()
# Retrieves the value of all link roughness for pipes or initial speed for pumps or initial setting for valves
print 'Link roughness for pipes or initial speed for pumps or initial setting for valves: %s'%d.getLinkInitialSetting()
# Retrieves the value of all link bulk reaction coefficients
print 'Link Bulk reaction coefficients: %s'%d.getLinkBulkReactionCoeff()
# Retrieves the value of all link wall reaction coefficients
print 'Link Wall reaction coefficients: %s'%d.getLinkWallReactionCoeff()
print 'Link pipe name ID: %s'%d.getLinkPipeNameID()
print 'Link pump name ID: %s'%d.getLinkPumpNameID()
print 'Link valve name ID: %s'%d.getLinkValveNameID()
print 'Link pump pattern index: %s'%d.getLinkPumpPatternIndex() # epanet20013


## Get all the node data
# Retrieves the ID label(s) of all links, or the IDs of an index set of links
print 'Node Name ID: %s'%d.getNodeNameID()
print 'Node Name ID for specific indices: %s'%d.getNodeNameID(2, 4, 5)
# Retrieves the indices of all nodes, or the indices of an ID set of nodes
print 'Node index: %s'%d.getNodeIndex()
print 'Node indices for specific ID:'
if inpname == 'Net1_Rossman2000.inp':
    print d.getNodeIndex('10', '11', '2')
elif inpname == 'Net2_Rossman2000.inp':
    print d.getNodeIndex('1', '10', '35')
elif inpname == 'BWSN1_Ostfeld2008.inp':
    print d.getNodeIndex('JUNCTION-8', 'JUNCTION-10', 'JUNCTION-20')
# Retrieves the junction index
print 'Node Junction Index: %s'%d.getNodeJunctionIndex()
# Retrieves the reservoir index
print 'Node reservoir Index: %s'%d.getNodeReservoirIndex()
# Retrieves the tank index
print 'Node tank Index: %s'%d.getNodeTankIndex()
print 'Node junctions name ID: %s'%d.getNodeJunctionNameID()
print 'Node tanks name ID: %s'%d.getNodeTankNameID()
print 'Node reservoirs name ID: %s'%d.getNodeReservoirNameID()
# Retrieves the value of all node elevations
print 'Node Elevations: %s'%d.getNodeElevations()
# Retrieves the value of all node basedemands
print 'Node Basedemands: %s'%d.getNodeBaseDemands()
# Retrieves the value of all node demand pattern indices
print 'Node demand pattern indices: %s'%d.getNodeDemandPatternIndex()
# Retrieves the value of all node emmitter coefficients
print 'Node emmitter coefficients: %s'%d.getNodeEmitterCoeff()
# Retrieves the value of all node initial quality
print 'Node initial quality: %s'%d.getNodeInitialQuality()
# Retrieves the value of all nodes source quality
print 'Node source quality: %s'%d.getNodeSourceQuality()
# Retrieves the value of all node source pattern index
print 'Node pattern index: %s'%d.getNodeSourcePatternIndex()
# Retrieves the value of all node source type
print 'Node source type code: %s'%d.getNodeSourceTypeCode()
print 'Node source type: %s'%d.getNodeSourceType()
# Retrieves the indices of the from/to nodes of all links.
print 'Link nodes indices: %s'%d.getNodesConnectingLinksIndex(); l=d.getNodesConnectingLinksIndex(); print l[0]; print l[0][0]
# Retrieves the id of the from/to nodes of all links.
print 'Link nodes IDs: %s'%d.getNodesConnectingLinksID(); c=d.getNodesConnectingLinksID(); print c[0]; print c[0][0]

## Get all tank data
# Retrieves the value of all tank initial water levels
print 'Tank initial water levels: %s'%d.getNodeTankInitialLevel()
# Retrieves the tank initial volume
print 'Tank initial volume: %s'%d.getNodeTankInitialWaterVolume()
# Retrieves the tank mixing mode (mix1, mix2, fifo, lifo)
print 'Tank mixing model: %s'%d.getNodeTankMixiningModel()
print 'Tank mixing code: %s'%d.getNodeTankMixiningModelCode()
# Retrieves the tank mixing zone volume
print 'Tank mixing zone value: %s'%d.getNodeTankMixZoneVolume()
# Retrieves the tank diameters
print 'Tank diameters: %s'%d.getNodeTankDiameter()
# Retrieves the tank minimum volume
print 'Tank minimum volume: %s'%d.getNodeTankMinimumWaterVolume()
# Retrieves the tank volume curve index
print 'Tank volume curve index: %s'%d.getNodeTankVolumeCurveIndex()
# Retrieves the tank minimum water level
print 'Tank minimum water level: %s'%d.getNodeTankMinimumWaterLevel()
# Retrieves the tank maximum water level
print 'Tank maximum water level: %s'%d.getNodeTankMaximumWaterLevel()
# Retrieves the tank Fraction of total volume occupied by the inlet/outlet zone in a 2-compartment tank
print 'Tank fraction: %s'%d.getNodeTankFraction()
# Retrieves the tank bulk rate coefficient
print 'Tank bulk rate: %s'%d.getNodeTankBulkReactionCoeff()


## Get all options
print 'Options max trials: %s'%d.getOptionsMaxTrials()
print 'Options accurancy value: %s'%d.getOptionsAccuracyValue()
print 'Options quality tolerance: %s'%d.getOptionsQualityTolerance()
print 'Options emitter exponent: %s'%d.getOptionsEmitterExponent()
print 'Options pattern demand multiplier: %s'%d.getOptionsPatternDemandMultiplier()

## Get pattern data
# Retrieves the ID label of all or some time patterns indices
print 'Pattern name ID: %s'%d.getPatternNameID()
print 'Pattern name ID of index 1: %s'%d.getPatternNameID(1)
# Retrieves the index of all or some time patterns IDs
print 'Pattern index: %s'%d.getPatternIndex()
if inpname == 'Net1_Rossman2000.inp':
    print 'Pattern index of ID 1: %s'%d.getPatternIndex('1')
elif inpname == 'Net2_Rossman2000.inp':
    print 'Pattern index of ID 2: %s'%d.getPatternIndex('2')
elif inpname == 'BWSN1_Ostfeld2008.inp':
    print 'Pattern index of ID PATTERN-1, PATTERN-0: %s'%d.getPatternIndex('PATTERN-1', 'PATTERN-0')
# Retrieves the number of time periods in all or some patterns
print 'Pattern lengths: %s'%d.getPatternLengths()
print 'Pattern count: %s'%d.getPatternCount()
patternIndex=1
patternStep=8
print 'Pattern value: %s'%d.getPatternValue(patternIndex, patternStep) #0.8 for Net1_Rossman2000
#print d.getPattern()

## Get quality types
# Retrieves the type of water quality analysis type
print 'Quality type code: %s'%[d.getQualityTypeCode()]
print 'Quality type: %s'%d.getQualityType()
print 'Quality trace node index: %s'%d.getQualityTraceNodeIndex()


## Get time parameters
print 'Simulation duration: %s'%d.getTimeSimulationDuration()
print 'Hydraulic step: %s'%d.getTimeHydraulicStep()
print 'Quality step: %s'%d.getTimeQualityStep()
print 'Pattern step: %s'%d.getTimePatternStep()
print 'Pattern start: %s'%d.getTimePatternStart()
print 'Report step: %s'%d.getTimeReportingStep()
print 'Report start: %s'%d.getTimeReportingStart()
print 'Rule step: %s'%d.getTimeRuleControlStep()
print 'Number of reporting periods saved to the binary: %s'%d.getTimeReportingPeriods()
print 'Statistic type code: %s'%d.getTimeStatisticsCode()
print 'Statistic type: %s'%d.getTimeStatisticsType()


## Units: US Customary - SI metric
print 'Pressure units: %s'%d.getNodePressureUnits()
print 'Pattern demand units: %s'%d.getPatternDemandsUnits()
print 'Pipe diameter units: %s'%d.getLinkPipeDiameterUnits()
print 'Tank diameter units: %s'%d.getNodeTankDiameterUnits()
print 'Energy efficiency units: %s'%d.getEnergyEfficiencyUnits()
print 'Node elevation units: %s'%d.getNodeElevationUnits()
print 'Node emitter coefficient units: %s'%d.getNodeEmitterCoefficientUnits()
print 'Energy units: %s'%d.getEnergyUnits()
print 'Link friction factor units: %s'%d.getLinkFrictionFactorUnits()
print 'Node head units: %s'%d.getNodeHeadUnits()
print 'Link length units: %s'%d.getLinkLengthsUnits()
print 'Link minor loss coefficient units: %s'%d.getLinkMinorLossCoeffUnits()
print 'Link pump power units: %s'%d.getLinkPumpPowerUnits()
print 'Quality reaction coefficient bulk units: %s'%d.getQualityReactionCoeffBulkUnits()
print 'Quality reaction coefficient wall units: %s'%d.getQualityReactionCoeffWallUnits()
print 'Link pipe roughness coefficient units: %s'%d.getLinkPipeRoughnessCoeffUnits()
print 'Quality source mass injection units: %s'%d.getQualitySourceMassInjectionUnits()
print 'Link velocity units: %s'%d.getLinkVelocityUnits()
print 'Tank volume units: %s'%d.getNodeTankVolumeUnits()
print 'Quality water age units: %s'%d.getQualityWaterAgeUnits()


print 'Node Coordinates: %s'%[d.getNodeCoordinates()]
print 'Plot network...'; d.plot()

## Simulation Hydraulics
# Runs hydraulics Step-by-step
d.openHydraulicAnalysis()
d.initializeHydraulicAnalysis()
tstep=1; P=[];T=[]; D=[]; H=[];F=[];Dsensing=[]
TankVolume=[];Velocity=[];Status=[];Settings=[]
PumpEnergy=[];LinkQuality=[]
while (tstep>0):
    T.append(d.runHydraulicAnalysis())
    # node dynamics
    P.append(d.getNodePressure())
    D.append(d.getNodeActualDemand())
    Dsensing.append(d.getNodeActualDemandSensingNodes([1,2]))
    H.append(d.getNodeHydaulicHead())
    TankVolume.append(d.getNodeTankVolume())
    # link dynamics
    F.append(d.getLinkFlows())
    Velocity.append(d.getLinkVelocity())
    Status.append(d.getLinkStatus())
    Settings.append(d.getLinkSettings())
    PumpEnergy.append(d.getLinkPumpEnergy())
 #   LinkQuality.append(d.getLinkQuality()) # epanet20013
    tstep=d.nextHydraulicAnalysisStep()
d.closeHydraulicAnalysis()

print 'Time: %s'%T
print 'Pressure: %s'%P
print 'Demand: %s'%D
print 'DemandSensing: %s'%Dsensing
print 'Head: %s'%H
print 'Velocity: %s'%Velocity
print 'TankVolume: %s'%TankVolume
print 'Flows: %s'%F

import matplotlib.pyplot as plot
PressureNodeIndex=[]
nodeindex = 5
for i in range(0,len(P)):
    PressureNodeIndex.append(P[i][nodeindex-1])
plot.plot(T,PressureNodeIndex,'b')
nodeid = d.getNodeNameID(nodeindex)
str = 'Node ID ' + nodeid[0]
plot.title(str)
plot.xlabel('Time(sec)')
plot.ylabel(d.getNodePressureUnits())
plot.show()

# Simulation Quality analysis
d.openQualityAnalysis()
d.initializeQualityAnalysis()
tstep=1; Q=[];T=[]
while (tstep>0):
    T.append(d.runQualityAnalysis())
    Q.append(d.getNodeActualQuality())
    tstep=d.stepQualityAnalysisTimeLeft()
#getNodeMassFlowRate
d.closeQualityAnalysis()
import matplotlib.pyplot as plot
nodeindex=6
quality=[]
for i in range(0,len(Q)):
    quality.append(Q[i][nodeindex-1])

print T
plot.plot(T,quality,'b')
nodeid = d.getNodeNameID(nodeindex)
str = 'Node ID ' + nodeid[0]
plot.title(str)
plot.xlabel('Time(sec)')
plot.ylabel(d.getQualityWaterAgeUnits())
plot.show()

#epanet dev-2.1
print d.getNodeTankVolume()
print d.getNodeTankMaxVolume()

QualType = d.getQualityType()
print 'Get Qualtype: %s'%d.getQualityType()
print 'Set Qualtype NONE'
d.setQualityType(d.EN_NONE)
print 'Get Qualtype: %s'%d.getQualityType()
print 'Set Qualtype AGE'
d.setQualityType(d.EN_AGE)
print 'Get Qualtype: %s'%d.getQualityType()
nodeid = d.getNodeNameID(1)
print 'Set Qualtype TRACE, NODE %s' %nodeid
d.setQualityType(d.EN_TRACE,nodeid[0]) # Net1
print 'Get Qualtype: %s'%d.getQualityType()
d.setQualityType(QualType) # Net1


## Get, add, set pattern
print d.addPattern('NewPat1') #add pattern and return pattern index
print d.addPattern('NewPat2', [0.8, 1.1, 1.4, 1.1, 0.8, 0.7])
print 'Retrieves the multiplier factor for all patterns and all times: %s'%d.getPattern()
print 'Pattern name ID: %s'%d.getPatternNameID()

if d.getControlRulesCount():
    print 'Get Controls: %s'%d.getControls()#TYPECONTROL[ctype.value] , ctypeCode, lindex, nindex, setting, level
    d.setControl(1,d.EN_HILEVEL,13,1,11,150)#controlRuleIndex,controlTypeCode,linkIndex,controlSettingValue,nodeIndex,controlLevel
    print 'Get new Controls: %s'%d.getControls()

print 'Link Diameter: %s'%d.getLinkDiameter()
newDiameter = d.getLinkDiameter()#18 Net1
newDiameter[0]=newDiameter[0]+5 #23
d.setLinkDiameter(newDiameter)
print 'Link new Diameter: %s'%d.getLinkDiameter()

print 'Link Length: %s'%d.getLinkLength()
newLength = d.getLinkLength()
newLength[0]=newLength[0]+5
d.setLinkLength(newLength)
print 'Link new Length: %s'%d.getLinkLength()

print 'Link Roughness: %s'%d.getLinkRoughnessCoeff()
newRoughness = d.getLinkRoughnessCoeff()
newRoughness[0]=newRoughness[0]+5
d.setLinkRoughnessCoeff(newRoughness)
print 'Link new Roughness: %s'%d.getLinkRoughnessCoeff()

print 'Link Minor loss coefficients: %s'%d.getLinkMinorLossCoeff()
newMinorloss = d.getLinkMinorLossCoeff()
newMinorloss[0]=newMinorloss[0]+1.1
d.setLinkMinorLossCoeff(newMinorloss)
print 'Link new Minor loss coefficients: %s'%d.getLinkMinorLossCoeff()

print 'Link Initial Status: %s'%d.getLinkInitialStatus()
newInitStatus = d.getLinkInitialStatus()
newInitStatus[0]=d.Closed
d.setLinkInitialStatus(newInitStatus)
print 'Link new Initial Status: %s'%d.getLinkInitialStatus()

print 'Link roughness for pipes or initial speed for pumps or initial setting for valves: %s'%d.getLinkInitialSetting()
newLinkSetting=d.getLinkInitialSetting()
newLinkSetting=list(numpy.array(newLinkSetting)+numpy.array([10] * d.getLinkCount()))
d.setLinkInitialSetting(newLinkSetting)
print 'New - Link roughness for pipes or initial speed for pumps or initial setting for valves: %s'%d.getLinkInitialSetting()

print 'Link Bulk reaction coefficients: %s'%d.getLinkBulkReactionCoeff()
newLinkBulkCoeff=d.getLinkBulkReactionCoeff()
newLinkBulkCoeff=list(numpy.array(newLinkBulkCoeff)-numpy.array([-0.55] * d.getLinkCount()))
d.setLinkBulkReactionCoeff(newLinkBulkCoeff)
print 'Link new Bulk reaction coefficients: %s'%d.getLinkBulkReactionCoeff()

print 'Link Wall reaction coefficients: %s'%d.getLinkWallReactionCoeff()
newLinkWallCoeff=d.getLinkBulkReactionCoeff()
newLinkWallCoeff=list(numpy.array(newLinkWallCoeff)-numpy.array([-1.1] * d.getLinkCount()))
d.setLinkWallReactionCoeff(newLinkWallCoeff)
print 'Link new Wall reaction coefficients: %s'%d.getLinkWallReactionCoeff()


print 'Link Status: %s'%d.getLinkStatus()
newLinkStatus=d.getLinkStatus()
newLinkStatus=numpy.array([d.Closed] * d.getLinkCount())
d.setLinkStatus(newLinkStatus)
print 'Link new Status: %s'%d.getLinkStatus()

print 'Link Settings: %s'%d.getLinkSettings()
newLinkSettings=d.getLinkSettings()
newLinkSettings=numpy.array([111] * d.getLinkCount())
d.setLinkSettings(newLinkSettings)
print 'Link new Settings: %s'%d.getLinkSettings()

print 'Node Elevations: %s'%d.getNodeElevations()
values=d.getNodeElevations()
values[0]=values[0]+50
d.setNodeElevations(values)
print 'Node new Elevations: %s'%d.getNodeElevations()

print 'Node Basedemands: %s'%d.getNodeBaseDemands()
values=d.getNodeBaseDemands()
values[0]=values[0]+50
d.setNodeBaseDemands(values)
print 'Node new Basedemands: %s'%d.getNodeBaseDemands()

print 'Node demand pattern indices: %s'%d.getNodeDemandPatternIndex()
values=d.getNodeDemandPatternIndex()
values[1]=0
d.setNodeDemandPatternIndex(values)
print 'Node new demand pattern indices: %s'%d.getNodeDemandPatternIndex()

print 'Node emmitter coefficients: %s'%d.getNodeEmitterCoeff()
values=d.getNodeEmitterCoeff()
values[1]=0.5
d.setNodeEmitterCoeff(values)
print 'Node new emmitter coefficients: %s'%d.getNodeEmitterCoeff()

print 'Node initial quality: %s'%d.getNodeInitialQuality()
values=d.getNodeInitialQuality()
values[1]=0.6
d.setNodeInitialQuality(values)
print 'Node new initial quality: %s'%d.getNodeInitialQuality()

if d.getNodeTankCount():
    print 'Tank initial water levels: %s'%d.getNodeTankInitialLevel()
    values=d.getNodeTankInitialLevel()
    tankIndex1 = d.getNodeTankIndex()[0]-1
    values[tankIndex1]=100
    d.setNodeTankInitialLevel(values)
    print 'Tank new initial water levels: %s'%d.getNodeTankInitialLevel()

    print 'Tank mixing model: %s'%d.getNodeTankMixiningModel()
    print 'Tank mixing code: %s'%d.getNodeTankMixiningModelCode()
    values=d.getNodeTankMixiningModelCode()
    values[tankIndex1]=d.EN_MIX2
    d.setNodeTankMixingModel(values)
    print 'Tank mixing model: %s'%d.getNodeTankMixiningModel()
    print 'Tank mixing code: %s'%d.getNodeTankMixiningModelCode()
    values[tankIndex1]=d.EN_FIFO
    d.setNodeTankMixingModel(values)
    print 'Tank mixing model: %s'%d.getNodeTankMixiningModel()
    values[tankIndex1]=d.EN_LIFO
    d.setNodeTankMixingModel(values)
    print 'Tank mixing model: %s'%d.getNodeTankMixiningModel()

    print 'Tank diameters: %s'%d.getNodeTankDiameter()
    values=d.getNodeTankDiameter()
    values[tankIndex1]=values[tankIndex1]+10
    d.setNodeTankDiameter(values)
    print 'Tank new diameters: %s'%d.getNodeTankDiameter()

    # print 'Tank minimum water level: %s'%d.getNodeTankMinimumWaterLevel()
    # values=d.getNodeTankMinimumWaterLevel()
    # values[tankIndex1]=values[tankIndex1]+10
    # values[:-1]=[nan]
    # d.setNodeTankMinimumWaterLevel(values)                                             #  BUG
    # print 'Tank new minimum water level: %s'%d.getNodeTankMinimumWaterLevel()

    print 'Tank minimum volume: %s'%d.getNodeTankMinimumWaterVolume()
    values=d.getNodeTankMinimumWaterVolume()
    values[tankIndex1]=values[tankIndex1]+10
    d.setNodeTankMinimumWaterVolume(values)
    print 'Tank minimum volume: %s'%d.getNodeTankMinimumWaterVolume()

    print 'Tank maximum water level: %s'%d.getNodeTankMaximumWaterLevel()
    values=d.getNodeTankMaximumWaterLevel()
    values[tankIndex1]=values[tankIndex1]+20
    d.setNodeTankMaximumWaterLevel(values)
    print 'Tank new maximum water level: %s'%d.getNodeTankMaximumWaterLevel()

    print 'Tank fraction: %s'%d.getNodeTankFraction()
    values=d.getNodeTankFraction()
    values[tankIndex1]=0.5
    d.setNodeTankFraction(values)
    print 'Tank new fraction: %s'%d.getNodeTankFraction()

    print 'Tank bulk rate: %s'%d.getNodeTankBulkReactionCoeff()
    values=d.getNodeTankFraction()
    values[tankIndex1]=1
    d.setNodeTankBulkReactionCoeff(values)
    print 'Tank new bulk rate: %s'%d.getNodeTankBulkReactionCoeff()

## Get, set sources
print 'Node source type code: %s'%d.getNodeSourceTypeCode()
values=d.getNodeSourceTypeCode()
values[2]=d.EN_MASS
d.setNodeSourceTypeCode(values)
print 'Node new source type code: %s'%d.getNodeSourceTypeCode()
print 'Node new source type: %s'%d.getNodeSourceType()
values[2]=d.EN_CONCEN
d.setNodeSourceTypeCode(values)
print 'Node new source type: %s'%d.getNodeSourceType()
values[2]=d.EN_SETPOINT
d.setNodeSourceTypeCode(values)
print 'Node new source type: %s'%d.getNodeSourceType()
values[2]=d.EN_FLOWPACED
d.setNodeSourceTypeCode(values)
print 'Node new source type: %s'%d.getNodeSourceType()

print 'Node source quality: %s'%d.getNodeSourceQuality()
values=d.getNodeSourceTypeCode()
values[2]=0.5
d.setNodeSourceQuality(values)
print 'Node new source quality: %s'%d.getNodeSourceQuality()

print 'Node pattern index: %s'%d.getNodeSourcePatternIndex()
values=d.getNodeSourcePatternIndex()
values[5]=1
d.setNodeSourcePatternIndex(values)
print 'Node new pattern index: %s'%d.getNodeSourcePatternIndex()

## Get, set options
print 'Options max trials: %s'%d.getOptionsMaxTrials()
d.setOptionsMaxTrials(45)
print 'Options new max trials: %s'%d.getOptionsMaxTrials()

print 'Options accurancy value: %s'%d.getOptionsAccuracyValue()
d.setOptionsAccuracyValue(0.015)
print 'Options new accurancy value: %s'%d.getOptionsAccuracyValue()

print 'Options quality tolerance: %s'%d.getOptionsQualityTolerance()
d.setOptionsQualityTolerance(0.02)
print 'Options new uality tolerance: %s'%d.getOptionsQualityTolerance()

print 'Options emitter exponent: %s'%d.getOptionsEmitterExponent()
d.setOptionsEmitterExponent(0.55)
print 'Options new emitter exponent: %s'%d.getOptionsEmitterExponent()

print 'Options pattern demand multiplier: %s'%d.getOptionsPatternDemandMultiplier()
d.setOptionsPatternDemandMultiplier(1.1)
print 'Options new pattern demand multiplier: %s'%d.getOptionsPatternDemandMultiplier()


## Get, Set Time parameters
print 'Simulation duration: %s'%d.getTimeSimulationDuration()
d.setTimeSimulationDuration(86500)
print 'New Simulation duration: %s'%d.getTimeSimulationDuration()

print 'Hydraulic step: %s'%d.getTimeHydraulicStep()
d.setTimeHydraulicStep(3500)
print 'New Hydraulic step: %s'%d.getTimeHydraulicStep()

print 'Quality step: %s'%d.getTimeQualityStep()
d.setTimeQualityStep(250)
print 'New Quality step: %s'%d.getTimeQualityStep()


print 'Pattern step: %s'%d.getTimePatternStep()
d.setTimePatternStep(7000)
print 'New Pattern step: %s'%d.getTimePatternStep()


print 'Pattern start: %s'%d.getTimePatternStart()
d.setTimePatternStart(100)
print 'New Pattern start: %s'%d.getTimePatternStart()


print 'Report step: %s'%d.getTimeReportingStep()
d.setTimeReportingStep(3500)
print 'New Report step: %s'%d.getTimeReportingStep()


print 'Report start: %s'%d.getTimeReportingStart()
d.setTimeReportingStart(200)
print 'New Report start: %s'%d.getTimeReportingStart()


print 'Rule step: %s'%d.getTimeRuleControlStep()
d.setTimeRuleControlStep(100)
print 'New Rule step: %s'%d.getTimeRuleControlStep()

print 'Statistic type code: %s'%d.getTimeStatisticsCode()
print 'Statistic type: %s'%d.getTimeStatisticsType()
d.setTimeStatisticsType(d.EN_AVERAGE)
print 'Statistic type: %s'%d.getTimeStatisticsType()
d.setTimeStatisticsType(d.EN_MINIMUM)
print 'Statistic type: %s'%d.getTimeStatisticsType()
d.setTimeStatisticsType(d.EN_MAXIMUM)
print 'Statistic type: %s'%d.getTimeStatisticsType()
d.setTimeStatisticsType(d.EN_RANGE)
print 'Statistic type: %s'%d.getTimeStatisticsType()

## Get, Set pattern
print 'Retrieves the multiplier factor for all patterns and all times: %s'%d.getPattern()
value = []
for i in [float(j) / 10 for j in range(0, 10, 1)]:
    value.append(i)


d.setPattern(1, value)
print 'Retrieves the multiplier factor for all patterns and all times: %s'%d.getPattern()

print 'ENgetcoord_dev2.1'
print d.getNodesCoords()

print d.getNodeCoordinates()

d.unload()

