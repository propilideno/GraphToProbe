import glob
import networkx as nx
import pandas as pd

import lib.overheadCalc as oc
import lib.toProbe as tpb
from lib.readTopologyZoo import GraphToMST


def toDataframe(df,topology,isBackBone,numberOfNodes,numberOfEdges):
    #Extracting Overheads
    overhead_DataPlane_MPINT,\
    overhead_ControlPlane_MPINT,\
    overhead_DataPlane_MPolkaCRC8,\
    overhead_ControlPlane_MPolkaCRC8,\
    overhead_DataPlane_MPolkaCRC16,\
    overhead_ControlPlane_MPolkaCRC16,\
    overhead_DataPlane_INTClassico,\
    overhead_ControlPlane_INTClassico = oc.extractOverheads()
    replication = oc.extractReplication()
    
    #Overhead por abordagem
    overheadDP_mPolkaCRC8 = sum(sum(overhead_DataPlane_MPolkaCRC8,[]))
    overheadDP_mPolkaCRC16 = sum(sum(overhead_DataPlane_MPolkaCRC16,[]))
    overheadDP_mPINT = sum(sum(overhead_DataPlane_MPINT,[]))
    overheadDP_INTClassico = sum(sum(overhead_DataPlane_INTClassico,[]))

    overheadCP_mPolkaCRC8 = sum(overhead_ControlPlane_MPolkaCRC8)
    overheadCP_mPolkaCRC16 = sum(overhead_ControlPlane_MPolkaCRC16)
    overheadCP_mPINT = sum(overhead_ControlPlane_MPINT)
    overheadCP_INTClassico = sum(overhead_ControlPlane_INTClassico)

    replicationPerNode = sum(replication)/numberOfNodes
    maxReplication = max(replication)
    stateOverhead = 0
    for n in replication:
        stateOverhead += (1 + 2*n)

    matrixOverhead = {}
    matrixOverhead['Topology'] = [topology,topology]
    matrixOverhead['IsBackBone'] = [isBackBone,isBackBone]
    matrixOverhead['Number of Nodes'] = [numberOfNodes,numberOfNodes]
    matrixOverhead['Number of Edges'] = [numberOfEdges,numberOfEdges]
    matrixOverhead['Replication Average per Node'] = [replicationPerNode,replicationPerNode]
    matrixOverhead['Max Replication'] = [maxReplication,maxReplication]
    matrixOverhead['State Overhead'] = [stateOverhead,stateOverhead]
    matrixOverhead['Where'] = ['DataPlane','ControlPlane']
    matrixOverhead['MPINT'] = [overheadDP_mPINT,overheadCP_mPINT]
    matrixOverhead['MPolka CRC8'] = [overheadDP_mPolkaCRC8,overheadCP_mPolkaCRC8]
    matrixOverhead['MPolka CRC16'] = [overheadDP_mPolkaCRC16,overheadCP_mPolkaCRC16]
    matrixOverhead['INT Clássico'] = [overheadDP_INTClassico,overheadCP_INTClassico]
    df2 = pd.DataFrame(data=matrixOverhead)
    result = pd.concat([df,df2],ignore_index=True)
    return result

def extractOptimalNodeSender(G,numberOfNodes): #Optimal on DP as tiebreaker, Optimal on MPOLKA CRC16
    optimalDPOverhead = 0
    optimalCPOverhead = 0
    optimalNodeSender = 0
    for nodeSender in range(numberOfNodes):
        sonda = tpb.dfs_init(G,nodeSender)
        overheadDP, overheadCP = oc.extractMPolkaOverhead()
        #print('Possivel Matriz de Sondas: ',sonda,'Overhead DP:',overheadDP,'| Overhead CP',overheadCP)

        if((overheadDP > optimalDPOverhead) and (overheadCP > optimalCPOverhead)):
            optimalDPOverhead = overheadDP
            optimalCPOverhead = overheadCP
            optimalNodeSender = nodeSender
        elif((overheadDP == optimalDPOverhead) and (overheadCP < optimalCPOverhead)):
            optimalDPOverhead = overheadDP
            optimalCPOverhead = overheadCP
            optimalNodeSender = nodeSender

    return optimalNodeSender

def appendGraphToDataFrame(df,G):
    G,topologyName,isBackBone,numberOfNodes,numberOfEdges = GraphToMST(G)
    optimalNodeSender = extractOptimalNodeSender(G,numberOfNodes)
    sondaAux = tpb.dfs_init(G,optimalNodeSender)
    print('<ESCOLHIDA> Matriz de Sondas',topologyName,' =',sondaAux,'\n')
    df = toDataframe(df,topologyName,isBackBone,numberOfNodes,numberOfEdges)
    return df

def appendAllTopologysToDataFrame(df):
    listTopology = glob.glob('topologyZoo/*.gml')
    for topology in listTopology:
        G = nx.read_gml(topology,destringizer=int,label='id')
        df = appendGraphToDataFrame(df,G)
    return df