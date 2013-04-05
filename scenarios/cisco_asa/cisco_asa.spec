{
    "fields" : [
        { "templateCount" : {"count":43} },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%b %d %Y" } },
        { "ip" : {"type": "random", "generate_type":"IPv4" } },
        { "ip2" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } },
        { "port2" : {"type": "random", "generate_type":"integer", "min":1, "max":5000 } },
        { "number" : {"type": "random", "generate_type":"integer", "min":0, "max":100 } }
    ],
    "template" : [
          "%ASA-session-6-302016: Teardown UDP connection 105683967 for Merkez_Wan_Int:${ip}/${port} to Sube_Mpls:${ip2}/${port2} duration 0:00:15 bytes ${number}",
          "%ASA-session-6-305011: Built dynamic TCP translation from any:${ip2}/${port2} to Merkez_Wan_Int:${ip}/${port}",
          "%ASA-session-6-302013: Built outbound TCP connection 105683971 for Merkez_Wan_Int:${ip}/${port} (${ip}/${port}) to Sube_Mpls:${ip2}/${port2} (${ip2}/${port2})",
          "%ASA-session-6-302014: Teardown TCP connection 105683877 for Merkez_Wan_Int:{ip}/${port} to Merkez_Mpls:{ip2}/${port2} duration 0:00:17 bytes ${number} TCP FINs",
          "%ASA-session-6-305012: Teardown dynamic UDP translation from any:{ip}/${port} to Merkez_Wan_Int:{ip2}/${port2} duration 0:00:32",
          "%ASA-session-6-302015: Built inbound UDP connection 105683972 for Merkez_Wan_Int:${ip}/${port} (${ip}/${port}) to Merkez_Mpls:${ip2}/${port2} (${ip2}/${port2})",
          "%ASA--4-410001: Dropped UDP DNS reply from Sube_Mpls:${ip}/${port} to Merkez_Wan_Int:${ip2}/${port2}; packet length ${port2} bytes exceeds configured limit of ${number} bytes",
          "%ASA-session-6-302017: Built inbound GRE connection 105683971 from Merkez_Wan_Int:${ip} (${ip}/${port}) to Sube_Mpls:${ip2}/${port2} (${ip2}/${port2})",
          "%ASA-session-5-304001: ${ip} Accessed URL ${ip2}:${url}",
          "%ASA-4-106023: Deny tcp src inside:${ip}/${port} dst outside1:${ip2}/${port2} by access-group \"inside_access_in_1\" [0x87d926c5, 0x0]",
          "%ASA-session-6-302013: Built outbound TCP connection 106070115 for Merkez_Wan_Int:${ip}/${port} (${ip}/${port}) to Sube_Mpls:${ip2}/${port2} (${ip2}/${port2})",
          "%ASA-session-6-302014: Teardown TCP connection 106070008 for Merkez_Wan_Int:${ip}/${port} to Sube_Mpls:${ip2}/${port2} duration 0:00:43 bytes ${port2} TCP FINs",
          "%ASA-session-6-302015: Built inbound UDP connection 106070121 for Merkez_Wan_Int:${ip}/${port} (${ip}/${port}) to Sube_Mpls:${ip2}/${port2} (${ip2}/${port2})",
          "%ASA-session-6-302016: Teardown UDP connection 106070116 for Merkez_Wan_Int:${ip}/${port} to Sube_Mpls:${ip2}/${port2} duration 0:01:09 bytes ${port2}",
          "%ASA-6-106015: Deny TCP (no connection) from ${ip}/${port} to ${ip2}/${port2} flags RST on interface inside",
          "%ASA-3-710003: TCP access denied by ACL from ${ip}/${port} to wan:${ip2}/${port2}",
          "%ASA-vpn-7-715047: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, processing hash payload",
          "%ASA-vpn-7-715046: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, constructing blank hash payload",
          "%ASA-vpn-7-713236: IP = ${ip}, IKE_DECODE SENDING Message (msgid=28258478) with payloads : HDR + HASH (8) + NOTIFY (11) + NONE (0) total length : ${number}",
          "%ASA-vpn-7-715036: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Sending keep-alive of type DPD R-U-THERE-ACK (seq number 0xedc7c9ff)",
          "%ASA-vpn-7-715075: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Received keep-alive of type DPD R-U-THERE (seq number 0xedc7ca0e)",
          "%ASA-vpn-7-713906: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, sending delete/delete with reason message",
          "%ASA-vpn-7-715053: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, MODE_CFG: Received request for Split DNS!",
          "%ASA-vpn-7-715001: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, constructing proxy ID",
          "%ASA-vpn-7-715019: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, IKEGetUserAttributes: primary DNS = ${ip2}",
          "%ASA-vpn-7-715049: IP = ${ip}, Received xauth V6 VID",
          "%ASA-vpn-7-715077: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Pitcher: received KEY_UPDATE, spi 0xe4b34fed",
          "%ASA-vpn-7-715076: Group = LocalUsers, IP = ${ip}, Computing hash for ISAKMP",
          "%ASA-vpn-7-714011: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, ID_IPV4_ADDR ID received",
          "%ASA-vpn-6-602303: IPSEC: An outbound remote access SA (SPI= 0xB3CB70E7) between ${ip} and ${ip2} (user= XXXYYYZZZ) has been created.",
          "%ASA-vpn-7-715055: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Send Client Browser Proxy Attributes!",
          "%ASA-vpn-7-715059: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Selecting only UDP-Encapsulated-Tunnel and  UDP-Encapsulated-Transport modes defined by NAT-Traversal",
          "%ASA-vpn-6-602304: IPSEC: An outbound remote access SA (SPI= 0xB3CB70E7) between ${ip} and ${ip2} (user= XXXYYYZZZ) has been deleted.",
          "%ASA-vpn-7-715064: IP = ${ip}, IKE Peer included IKE fragmentation capability flags:  Main Mode:        True  Aggressive Mode:  False",
          "%ASA-vpn-7-715038: Group = LocalUsers, IP = ${ip}, Processing IOS/PIX Vendor ID payload (version: 1.0.0, capabilities: 00000408)",
          "%ASA-vpn-7-715028: Group = LocalUsers, IP = ${ip}, IKE SA Proposal # 1, Transform # 1 acceptable  Matches global IKE entry # 2",
          "%ASA-vpn-7-715048: Group = LocalUsers, IP = ${ip}, Send Altiga/Cisco VPN3000/Cisco ASA GW VID",
          "%ASA-vpn-6-713172: Group = LocalUsers, IP = ${ip}, Automatic NAT Detection Status:     Remote end   IS   behind a NAT device     This   end is NOT behind a NAT device",
          "%ASA-vpn-7-715022: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Resume Quick Mode processing, Cert/Trans Exch/RM DSID completed",
          "%ASA-vpn-7-715021: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, Delay Quick Mode processing, Cert/Trans Exch/RM DSID in progress",
          "%ASA-vpn-5-713119: Group = LocalUsers, Username = XXXYYYZZZ, IP = ${ip}, PHASE 1 COMPLETED",
          "%ASA-session-6-3016: Teardown UDP connection 10568xXX3967 for Merkez_Wan_Int:${ip}/${port} to Sube_Mpls:${ip}/${port} duration 0:01:08 bytes ${number}",
          "${date}: %ASA--4-410001: Dropped UDP DNS reply from Sube_Mpls:${ip}/${port} to Merkez_Wan_Int:${ip}/${port}; packet length ${port2} bytes exceeds configured limit of ${number} bytes"
    ]
}
