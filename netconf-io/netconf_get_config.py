import sys, os
from netconf import netconf_connect, netconf_load_config, netconf_terminate, netconf_xget_leaf_value, netconf_xget_config_container_value, netconf_xget_container_value
import time

def main():
    gatewayip="192.168.209.1"
    port=830
    user="root"
    password="hadm1_123"

    if len(sys.argv)!=2 and len(sys.argv)!=3 and len(sys.argv)!=4:
        print "Usage: netconf_get_config.py host [xpath]"
        return -1
    host=sys.argv[1]
    if len(sys.argv)>=3:
        xpath=sys.argv[2]
    else:
        xpath="/"

    netconf_host = netconf_connect(host, port, user, password)
    if netconf_host == None:
        print "[FAILED] Connecting to ip=%(ip)s:" % {'ip':host}
        return(-1)

    if len(sys.argv)==4 and sys.argv[3] == "status":
        (ret, config_container_value) = netconf_xget_container_value(netconf_host, xpath)
        if ret==0:
            print "  "+str(config_container_value)
        else:
            print "FAILED"
            return(-1)
    else:
        (ret, config_container_value) = netconf_xget_config_container_value(netconf_host, xpath)
        if ret==0:
            print "  "+str(config_container_value)
        else:
            print "FAILED"
            return(-1)

    netconf_terminate(netconf_host)

    return 0

exit(main())

