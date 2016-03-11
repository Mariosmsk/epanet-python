# Read Epanet File
import os

def LoadFile(inp):
    global inpname, mm
    getPathPlugin = os.path.dirname(os.path.realpath(__file__))+"\\"
    inpname = getPathPlugin + inp

def BinUpdateClass():
    global mm
    mm = getBinInfo()
    return mm

## get Info
def getBinNodeJunctionCount():
    global mm
    return mm[4]

def getBinNodeReservoirCount():
    global mm
    return mm[7]


def getBinNodeNameID():
    global mm
    ndNameID=mm[0]
    for i in range(len(mm[5])):
        ndNameID.append(mm[5][i])#reservoirs
    #for i in range(len(mm[6])): tanks
     #   nodeElevations.append(mm[6][i])
    return ndNameID

def getBinNodeJunctionNameID():
    global mm
    return mm[0]

def getBinReservoirNameID():
    global mm
    return mm[5]

# def getBinNodeElevations():
#     global mm
#     nodeElevations=getBinNodeJunctionElevations()
#     for i in range(len(mm[6])):
#         nodeElevations.append(mm[6][i])#reservoirs
#     for i in range(len(mm[6])):
#         nodeElevations.append(mm[9][i])
#     return nodeElevations

def getBinNodeJunctionElevations():
    global mm
    return mm[1]

def getBinNodeReservoirElevations():
    global mm
    return mm[6]

def getBinNodeBaseDemands():
    global mm
    return mm[2]

# Tanks Info
def getBinNodeTankNameID():
    global mm
    return mm[8]

def getBinNodeTankElevations():
    global mm
    return mm[9]

def getBinNodeTankInitLevel():
    global mm
    return mm[10]

def getBinNodeTankMinLevel():
    global mm
    return mm[11]

def getBinNodeTankMaxLevel():
    global mm
    return mm[12]

def getBinNodeTankDiameter():
    global mm
    return mm[13]

def getBinNodeTankMinVol():
    global mm
    return mm[14]

# Get Links Info
def getBinLinkPipeCount():
    return len(getBinLinkPipeNameID())

def getBinLinkPipeNameID():
    global mm
    return mm[15]

def getBinLinkFromNode():
    global mm
    return mm[16]

def getBinLinkToNode():
    global mm
    return mm[17]

def getBinLinkPipeLengths():
    global mm
    return mm[18]

def getBinLinkPipeDiameters():
    global mm
    return mm[19]

def getBinLinkPipeRoughness():
    global mm
    return mm[20]

def getBinLinkPipeMinorLoss():
    global mm
    return mm[21]

# Get Pumps Info
def getBinLinkPumpCount():
    return len(getBinLinkPumpNameID())

def getBinLinkPumpNameID():
    global mm
    return mm[22]

def getBinLinkPumpPatterns():
    global mm
    return mm[23]

def getBinLinkPumpCurveNameID():
    global mm
    return mm[24]

def getBinLinkPumpPower():
    global mm
    return mm[25]

def getBinLinkPumpNameIDPower():
    global mm
    return mm[26]

#Get Valves Info
def getBinLinkValveCount():
    return len(getBinLinkValveNameID())

def getBinLinkValveNameID():
    global mm
    return mm[27]

def getBinLinkValveDiameters():
    global mm
    return mm[28]

def getBinLinkValveType():
    global mm
    return mm[29]

def getBinLinkValveSetting():
    global mm
    return mm[30]

def getBinLinkValveMinorLoss():
    global mm
    return mm[31]


# Get all info
def getBinInfo():
    global inpname
    file = open(inpname,'r')
    sec=[0]*7

    nodeJunctionNameID=[]
    nodeJunctionElevations=[]
    nodeJunctionBaseDemands=[]
    nodeJunctionPatternNameID=[]
    nodeReservoirNameID=[]
    nodeReservoirElevations=[]

    BinNodeTankNameID=[]
    BinNodeTankElevation=[]
    BinNodeTankInitLevel=[]
    BinNodeTankMinLevel=[]
    BinNodeTankMaxLevel=[]
    BinNodeTankDiameter=[]
    BinNodeTankMinVol=[]

    BinLinkPipeNameID=[]
    BinLinkFromNode=[]
    BinLinkToNode=[]
    BinLinkPipeLengths=[]
    BinLinkPipeDiameters=[]
    BinLinkPipeRoughness=[]
    BinLinkPipeMinorLoss=[]

    BinLinkPumpPatterns=[]
    BinLinkPumpCurveNameID=[]
    BinLinkPumpPower=[]
    BinLinkPumpNameIDPower=[]
    BinLinkPumpNameID=[]

    BinLinkValveNameID=[]
    BinLinkValveDiameters=[]
    BinLinkValveType=[]
    BinLinkValveSetting=[]
    BinLinkValveMinorLoss=[]

    while True:
        s1=file.readline()
        if s1=="[END]\n":
            return [nodeJunctionNameID, nodeJunctionElevations, nodeJunctionBaseDemands, nodeJunctionPatternNameID, len(nodeJunctionNameID),#01234
                    nodeReservoirNameID, nodeReservoirElevations, len(nodeReservoirNameID),#567
                    BinNodeTankNameID, BinNodeTankElevation, BinNodeTankInitLevel, BinNodeTankMinLevel, BinNodeTankMaxLevel, BinNodeTankDiameter, BinNodeTankMinVol, #8#9#10#11#12#13#14
                    BinLinkPipeNameID, BinLinkFromNode, BinLinkToNode, BinLinkPipeLengths, BinLinkPipeDiameters, BinLinkPipeRoughness, BinLinkPipeMinorLoss, #15#16#17#18#19#20#21
                    BinLinkPumpNameID, BinLinkPumpPatterns, BinLinkPumpCurveNameID, BinLinkPumpPower, BinLinkPumpNameIDPower, #22#23#24#25#26
                    BinLinkValveNameID, BinLinkValveDiameters, BinLinkValveType, BinLinkValveSetting, BinLinkValveMinorLoss] #27#28#29#30#31

        elif s1=="[JUNCTIONS]\n":
            sec[0]=1; pass
        elif s1=="[RESERVOIRS]\n":
            sec[0]=0;sec[1]=1;s1=file.readline()
        elif s1=="[TANKS]\n":
            sec[0]=sec[1]=0;sec[2]=1;s1=file.readline()
        elif s1=="[PIPES]\n":
            sec[0]=sec[1]=sec[2]=0;sec[3]=1;s1=file.readline()
        elif s1=="[PUMPS]\n":
            sec[0]=sec[1]=sec[2]=sec[3]=0;sec[4]=1;s1=file.readline()
        elif s1=="[VALVES]\n":
            sec[0]=sec[1]=sec[2]=sec[3]=sec[4]=0;sec[5]=1;s1=file.readline()
        elif s1[0][0]=="[":
            sec[0]=sec[1]=sec[2]=sec[3]=sec[4]=sec[5]=0;sec[6]=1;s1=file.readline()
        if sec[0]==1: #JUNCTIONS
            mm=s1.split()
            if len(mm)>1:
                if mm[0][0]==';':
                    pass
                else:
                    nodeJunctionNameID.append(mm[0])
                    nodeJunctionElevations.append(float(mm[1]))
                    nodeJunctionBaseDemands.append(float(mm[2]))
                    if len(mm)>2:
                        if mm[3][0]!=';':
                            nodeJunctionPatternNameID.append(mm[3])
                        else:
                            nodeJunctionPatternNameID.append('')

        if sec[1]==1: #RESERVOIRS
            mm=s1.split()
            if len(mm)>0:
                if mm[0][0]==';':
                    pass
                else:
                    nodeReservoirNameID.append(mm[0])
                    nodeReservoirElevations.append(float(mm[1]))
                    if len(mm)>1:
                        if mm[2][0]!=';':
                            nodeJunctionPatternNameID.append(mm[2])
                        else:
                            nodeJunctionPatternNameID.append('')

        if sec[2]==1: #TANKS
            mm=s1.split()
            if len(mm)>0:
                if mm[0][0]==';':
                    pass
                else:
                    BinNodeTankNameID.append(mm[0])
                    BinNodeTankElevation.append(float(mm[1]))
                    BinNodeTankInitLevel.append(float(mm[2]))
                    BinNodeTankMinLevel.append(float(mm[3]))
                    BinNodeTankMaxLevel.append(float(mm[4]))
                    BinNodeTankDiameter.append(float(mm[5]))
                    BinNodeTankMinVol.append(float(mm[6]))

        if sec[3]==1: #PIPES
            mm=s1.split()
            if len(mm)>0:
                if mm[0][0]==';':
                    pass
                else:
                    BinLinkPipeNameID.append(mm[0])
                    BinLinkFromNode.append(mm[1])
                    BinLinkToNode.append(mm[2])
                    BinLinkPipeLengths.append(float(mm[3]))
                    BinLinkPipeDiameters.append(float(mm[4]))
                    BinLinkPipeRoughness.append(float(mm[5]))
                    BinLinkPipeMinorLoss.append(float(mm[6]))

        if sec[4]==1: #PUMPS
            mm=s1.split()
            if len(mm)>0:
                if mm[0][0]==';':
                    pass
                else:
                    BinLinkPumpNameID.append(mm[0])
                    BinLinkFromNode.append(mm[1])
                    BinLinkToNode.append(mm[2])
                    if len(mm)>5:
                        if mm[5][0]!=';':
                            BinLinkPumpPatterns.append(mm[5])
                    if mm[3]=='HEAD':
                        BinLinkPumpCurveNameID.append(mm[4])
                    elif mm[3]=='POWER':
                        BinLinkPumpPower.append(float(mm[4]))
                        BinLinkPumpNameIDPower.append(mm[0])

        if sec[5]==1: #VALVES
            mm=s1.split()
            if len(mm)>1:
                if mm[0][0]==';':
                    pass
                else:
                    BinLinkValveNameID.append(mm[0])
                    BinLinkFromNode.append(mm[1])
                    BinLinkToNode.append(mm[2])
                    BinLinkValveDiameters.append(float(mm[3]))
                    BinLinkValveType.append(mm[4])
                    BinLinkValveSetting.append(float(mm[5]))
                    if len(mm)>6:
                        if mm[6][0]!=';':
                            BinLinkValveMinorLoss.append(float(mm[6]))

## Node Coordinates
def getBinNodeCoordinates():
    global inpname
    coord=[]
    file = open(inpname,'r')
    u=0
    while True:
        s1=file.readline()
        u+=1
        if s1=="[END]\n":
            break

    file = open(inpname,'r')
    a=0;k=0
    x=[]
    y=[]
    # Create a list.
    vertx=[];verty=[]
    # Append empty lists in first two indexes.
    nlink = getBinLinkPipeCount()+getBinLinkPumpCount()+getBinLinkValveCount()
    for i in range(0,nlink):
        vertx.append([])
        verty.append([])
    node=getBinNodesConnectingLinksIndex()
    for i in range(0, u):
        if a==0:
            s=file.readline()
            ss=";Node            \tX-Coord         \tY-Coord\n"
        if s == ss or a==1:
            s=file.readline()
            coord.append(s)
            a=1;m=0
            if s=="[VERTICES]\n":
                s=file.readline()
                ss=";Link               \tX-Coord           \tY-Coord\n"
                a=2
            if s!="\n" and a!=2:
                pp = s.split()
                x.append(float(pp[1]))
                y.append(float(pp[2]))
                k+=1
        if s == ss or a==2:
            s=file.readline()
            if s=="[LABELS]\n":
                break
            if s!="\n":
                pp = s.split()
                linkIndex = getLinkIndex(pp[0])
                # Add elements to empty lists.
                vertx[linkIndex[0]-1].append(float(pp[1]))
                verty[linkIndex[0]-1].append(float(pp[2]))
                k+=1


    x1 = []
    y1 = []
    x2 = []; ToNode = []
    y2 = []; FromNode = []
    for i in range(0,nlink):
        fr = node[i][0]
        FromNode.append(fr)
        t0 = node[i][1]
        ToNode.append(t0)
        x1.append(x[FromNode[i]-1])
        y1.append(y[FromNode[i]-1])
        x2.append(x[ToNode[i]-1])
        y2.append(y[ToNode[i]-1])
    return x,y,x1,y1,x2,y2,vertx,verty

def getLinkPumpPower():
    global inpname
    file = open(inpname,'r')
    value=[]
    while True:
        s1=file.readline()
        pp = s1.split()
        if s1=="[END]\n":
            return value
        elif len(pp)>3:
            if pp[3]=='POWER' or pp[3]=='power':
                append((pp[0],pp[4])) #return pump id with Power value
        elif s1=="[VALVES]\n":
            return value

EN_ELEVATION     = 0      # /* Node parameters */
EN_BASEDEMAND    = 1
EN_PATTERN       = 2
EN_EMITTER       = 3
EN_INITQUAL      = 4
EN_SOURCEQUAL    = 5
EN_SOURCEPAT     = 6
EN_SOURCETYPE    = 7
EN_TANKLEVEL     = 8
EN_DEMAND        = 9
EN_HEAD          = 10
EN_PRESSURE      = 11
EN_QUALITY       = 12
EN_SOURCEMASS    = 13
EN_INITVOLUME    = 14
EN_MIXMODEL      = 15
EN_MIXZONEVOL    = 16

EN_TANKDIAM      = 17
EN_MINVOLUME     = 18
EN_VOLCURVE      = 19
EN_MINLEVEL      = 20
EN_MAXLEVEL      = 21
EN_MIXFRACTION   = 22
EN_TANK_KBULK    = 23

EN_DIAMETER      = 0      # /* Link parameters */
EN_LENGTH        = 1
EN_ROUGHNESS     = 2
EN_MINORLOSS     = 3
EN_INITSTATUS    = 4
EN_INITSETTING   = 5
EN_KBULK         = 6
EN_KWALL         = 7
EN_FLOW          = 8
EN_VELOCITY      = 9
EN_HEADLOSS      = 10
EN_STATUS        = 11
EN_SETTING       = 12
EN_ENERGY        = 13

EN_DURATION      = 0      # /* Time parameters */
EN_HYDSTEP       = 1
EN_QUALSTEP      = 2
EN_PATTERNSTEP   = 3
EN_PATTERNSTART  = 4
EN_REPORTSTEP    = 5
EN_REPORTSTART   = 6
EN_RULESTEP      = 7
EN_STATISTIC     = 8
EN_PERIODS       = 9

EN_NODECOUNT     = 0      # /* Component counts */
EN_TANKCOUNT     = 1
EN_LINKCOUNT     = 2
EN_PATCOUNT      = 3
EN_CURVECOUNT    = 4
EN_CONTROLCOUNT  = 5

EN_JUNCTION      = 0      # /* Node types */
EN_RESERVOIR     = 1
EN_TANK          = 2

EN_CVPIPE        = 0      # /* Link types */
EN_PIPE          = 1
EN_PUMP          = 2
EN_PRV           = 3
EN_PSV           = 4
EN_PBV           = 5
EN_FCV           = 6
EN_TCV           = 7
EN_GPV           = 8

EN_NONE          = 0      # /* Quality analysis types */
EN_CHEM          = 1
EN_AGE           = 2
EN_TRACE         = 3

EN_CONCEN        = 0      # /* Source quality types */
EN_MASS          = 1
EN_SETPOINT      = 2
EN_FLOWPACED     = 3

EN_CFS           = 0      # /* Flow units types */
EN_GPM           = 1
EN_MGD           = 2
EN_IMGD          = 3
EN_AFD           = 4
EN_LPS           = 5
EN_LPM           = 6
EN_MLD           = 7
EN_CMH           = 8
EN_CMD           = 9

EN_TRIALS        = 0      # /* Misc. options */
EN_ACCURACY      = 1
EN_TOLERANCE     = 2
EN_EMITEXPON     = 3
EN_DEMANDMULT    = 4

EN_LOWLEVEL      = 0      # /* Control types */
EN_HILEVEL       = 1
EN_TIMER         = 2
EN_TIMEOFDAY     = 3

EN_AVERAGE       = 1      # /* Time statistic types.    */
EN_MINIMUM       = 2
EN_MAXIMUM       = 3
EN_RANGE         = 4

EN_MIX1          = 0      # /* Tank mixing models */
EN_MIX2          = 1
EN_FIFO          = 2
EN_LIFO          = 3

EN_NOSAVE        = 0      # /* Save-results-to-file flag */
EN_SAVE          = 1
EN_INITFLOW      = 10     # /* Re-initialize flow flag   */

Open             = 1
Closed           = 0

# Constants for units
FlowUnits= { EN_CFS :"cfs"   ,
             EN_GPM :"gpm"   ,
             EN_MGD :"a-f/d" ,
             EN_IMGD:"mgd"   ,
             EN_AFD :"Imgd"  ,
             EN_LPS :"L/s"   ,
             EN_LPM :"Lpm"   ,
             EN_MLD :"m3/h"  ,
             EN_CMH :"m3/d"  ,
             EN_CMD :"ML/d"  }

# Constants for links
TYPELINK= {  EN_CVPIPE :"CV" ,
             EN_PIPE :"PIPE" ,
             EN_PUMP :"PUMP" ,
             EN_PRV:"PRV"    ,
             EN_PSV :"PSV"   ,
             EN_PBV :"PBV"   ,
             EN_FCV :"FCV"   ,
             EN_TCV :"TCV"   ,
             EN_GPV :"GPV"   }

# Constants for nodes
TYPENODE= {  EN_JUNCTION :"JUNCTION"  ,
             EN_RESERVOIR :"RESERVOIR",
             EN_TANK :"TANK"      }

# Constants for controls
TYPECONTROL= {  EN_LOWLEVEL :"LOWLEVEL"  ,
                EN_HILEVEL :"HIGHLEVEL"  ,
                EN_TIMER :"TIMER"        ,
                EN_TIMEOFDAY :"TIMEOFDAY"}

# Constants for mixing models
TYPEMIXMODEL= { EN_MIX1 :"MIX1" ,
                EN_MIX2 :"MIX2" ,
                EN_FIFO :"FIFO" ,
                EN_LIFO :"LIFO" }

# Constants for quality
TYPEQUALITY= { EN_NONE :"NONE"  ,
               EN_CHEM :"CHEM"  ,
               EN_AGE :"AGE"    ,
               EN_TRACE :"TRACE"}

# Constants for sources
TYPESOURCE= { EN_CONCEN :"CONCEN"      ,
              EN_MASS :"MASS"          ,
              EN_SETPOINT :"SETPOINT"  ,
              EN_FLOWPACED :"FLOWPACED"}

# Constants for statistics
TYPESTATS= { EN_NONE :"NONE"      ,
             EN_AVERAGE :"AVERAGE",
             EN_MINIMUM :"MINIMUM",
             EN_MAXIMUM :"MAXIMUM",
             EN_RANGE :"RANGE"    }