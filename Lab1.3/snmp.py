from pysnmp.hlapi import *  # Импортировать только High-level API
def print_snmp(g):
    try:
        result = getCmd(SnmpEngine(),
               CommunityData('public', mpModel=0),
               UdpTransportTarget(('10.31.70.107', 161)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
        print(result)
        #n = nextCmd(SnmpEngine(),
                #CommunityData('public', mpModel=0),
                #UdpTransportTarget(('10.31.70.107', 161)),
                #ContextData(),
                #ObjectType(ObjectIdentity('1.3.6.1.2.1.22.1.2')),
        #print_snmp(result)
