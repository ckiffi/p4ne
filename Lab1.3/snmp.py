# Подключаем часть библиотеки 'pysnmp'. 'hlapi' означает high-level API
from pysnmp.hlapi import *
    snmp_object = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
    snmp_object2 = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")
    result = getCmd(SnmpEngine(),
                    CommunityData
