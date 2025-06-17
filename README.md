# pysros_cli

This is a project to have a CLI tool wrapper around the pySROS python library. The pySROS documentation is available [here](https://network.developer.nokia.com/static/sr/learn/pysros/latest/index.html).

## Usage

Currently tested is get and set functions. Available parameters are exposed and visible using help command.

## Examples:

```shell
pysros_cli get --host 10.0.1.135 -u admin -p admin --path /state/router[router-name=Base]/interface[interface-name=system] --no-hostkey-verify
```

```shell
/state/router/interface: {'interface-name': Leaf('system'), 'if-index': Leaf(1), 'system-if-index': 
Leaf(256), 'oper-state': Leaf('up'), 'protocol': Leaf('isis mpls rsvp'), 'oper-ip-mtu': Leaf(1500), 
'creation-origin': Leaf('manual'), 'last-oper-change': Leaf('2025-05-23T08:37:31.4Z'), 'statistics': 
Container({'ip': Container({'out-packets': Leaf(0), 'out-octets': Leaf(0), 'out-discard-packets': 
Leaf(0), 'out-discard-octets': Leaf(0), 'in-packets': Leaf(0), 'in-octets': Leaf(0), 
'urpf-check-fail-packets': Leaf(0), 'urpf-check-fail-octets': Leaf(0)}), 'mpls': 
Container({'out-packets': Leaf(0), 'out-octets': Leaf(0), 'in-packets': Leaf(0), 'in-octets': 
Leaf(0)})}), 'ipv4': Container({'oper-state': Leaf('up'), 'icmp': Container({'statistics': 
Container({'icmp-in-msgs': Leaf(1), 'icmp-in-errors': Leaf(1), 'icmp-in-dest-unreachables': Leaf(0), 
'icmp-in-redirects': Leaf(0), 'icmp-in-echos': Leaf(0), 'icmp-in-echo-replies': Leaf(0), 
'icmp-in-time-exceeds': Leaf(1), 'icmp-in-src-quenches': Leaf(0), 'icmp-in-timestamps': Leaf(0), 
'icmp-in-timestamp-replies': Leaf(0), 'icmp-in-address-masks': Leaf(0), 'icmp-in-address-mask-replies': 
Leaf(0), 'icmp-in-parm-problems': Leaf(0), 'icmp-out-msgs': Leaf(0), 'icmp-out-errors': Leaf(0), 
'icmp-out-dest-unreachables': Leaf(0), 'icmp-out-redirects': Leaf(0), 'icmp-out-echos': Leaf(0), 
'icmp-out-echo-replies': Leaf(0), 'icmp-out-time-exceeds': Leaf(0), 'icmp-out-src-quenches': Leaf(0), 
'icmp-out-timestamps': Leaf(0), 'icmp-out-timestamp-replies': Leaf(0), 'icmp-out-address-masks': Leaf(0),
'icmp-out-address-mask-replies': Leaf(0), 'icmp-out-parm-problems': Leaf(0), 'icmp-out-discards': 
Leaf(0)})}), 'dhcp': Container({'statistics': Container({'total-rx-packets': Container({'received': 
Leaf(0), 'malformed': Leaf(0), 'untrusted': Leaf(0)}), 'total-tx-packets': Container({'transmitted': 
Leaf(0)}), 'client-packets': Container({'dropped': Leaf(0), 'relayed': Leaf(0), 'snooped': Leaf(0)}), 
'server-packets': Container({'dropped': Leaf(12), 'relayed': Leaf(0), 'snooped': Leaf(0)})})}), 
'statistics': Container({'out-packets': Leaf(0), 'out-octets': Leaf(0), 'out-discard-packets': Leaf(0), 
'out-discard-octets': Leaf(0), 'in-packets': Leaf(0), 'in-octets': Leaf(0), 'urpf-check-fail-packets': 
Leaf(0), 'urpf-check-fail-octets': Leaf(0), 'out-discard-dbcast-packets': Leaf(0), 
'out-discard-dbcast-octets': Leaf(0), 'in-ip-helper-redirects-packets': Leaf(0), 
'in-ip-helper-redirects-octets': Leaf(0)}), 'primary': Container({'oper-address': Leaf('192.0.0.135'), 
'creation-origin': Leaf('manual')})}), 'ipv6': Container({'oper-state': Leaf('down'), 'down-reason': 
Leaf('protocol-down'), 'icmp6': Container({'statistics': Container({'icmp6-in-msgs': Leaf(0), 
'icmp6-in-errors': Leaf(0), 'icmp6-in-dest-unreachables': Leaf(0), 'icmp6-in-admin-prohibs': Leaf(0), 
'icmp6-in-time-exceeds': Leaf(0), 'icmp6-in-parm-problems': Leaf(0), 'icmp6-in-pkt-too-bigs': Leaf(0), 
'icmp6-in-echos': Leaf(0), 'icmp6-in-echo-replies': Leaf(0), 'icmp6-in-rtr-solicits': Leaf(0), 
'icmp6-in-rtr-advertisements': Leaf(0), 'icmp6-in-nbr-solicits': Leaf(0), 'icmp6-in-nbr-advertisements': 
Leaf(0), 'icmp6-in-redirects': Leaf(0), 'icmp6-in-grp-memb-queries': Leaf(0), 
'icmp6-in-grp-memb-repsonses': Leaf(0), 'icmp6-in-grp-memb-reductions': Leaf(0), 'icmp6-out-msgs': 
Leaf(0), 'icmp6-out-errors': Leaf(0), 'icmp6-out-dest-unreachables': Leaf(0), 'icmp6-out-admin-prohibs': 
Leaf(0), 'icmp6-out-time-exceeds': Leaf(0), 'icmp6-out-parm-problems': Leaf(0), 'icmp6-out-pkt-too-bigs':
Leaf(0), 'icmp6-out-echos': Leaf(0), 'icmp6-out-echo-replies': Leaf(0), 'icmp6-out-rtr-solicits': 
Leaf(0), 'icmp6-out-rtr-advertisements': Leaf(0), 'icmp6-out-nbr-solicits': Leaf(0), 
'icmp6-out-nbr-advertisements': Leaf(0), 'icmp6-out-redirects': Leaf(0), 'icmp6-out-grp-memb-queries': 
Leaf(0), 'icmp6-out-grp-memb-responses': Leaf(0), 'icmp6-out-grp-memb-reductions': Leaf(0), 
'icmp6-out-discards': Leaf(0)})}), 'statistics': Container({'out-packets': Leaf(0), 'out-octets': 
Leaf(0), 'out-discard-packets': Leaf(0), 'out-discard-octets': Leaf(0), 'in-packets': Leaf(0), 
'in-octets': Leaf(0), 'urpf-check-fail-packets': Leaf(0), 'urpf-check-fail-octets': Leaf(0)})})}
```

Similar command with json output formatting:

```shell
pysros_cli get --host 10.0.1.135 -u admin -p admin --path /state/router[router-name=Base]/interface[interface-name=system] --no-hostkey-verify --format json
```

```json
{
  "nokia-state:if-index": 1,
  "nokia-state:system-if-index": 256,
  "nokia-state:oper-state": "up",
  "nokia-state:protocol": "isis mpls rsvp",
  "nokia-state:oper-ip-mtu": 1500,
  "nokia-state:creation-origin": "manual",
  "nokia-state:last-oper-change": "2025-05-23T08:37:31.4Z",
  "nokia-state:statistics": {
    "ip": {
      "out-packets": "0",
      "out-octets": "0",
      "out-discard-packets": "0",
{....}
  },
  "nokia-state:ipv6": {
    "statistics": {
      "bgp": {
        "tunnel-count": 0
      },
      "bgp-epe": {
        "tunnel-count": 0
      },
      "isis": {
        "tunnel-count": 0
      },
      "ldp": {
        "tunnel-count": 0
      },
      "mpls-fwd-policy": {
        "tunnel-count": 0
      },
      "ospfv3": {
        "tunnel-count": 0
      },
      "rib-api": {
        "tunnel-count": 0
      },
      "sdp": {
        "tunnel-count": 0
      },
      "sr-policy": {
        "tunnel-count": 0
      },
      "sr-te": {
        "tunnel-count": 0
      },
      "srv6-isis": {
        "tunnel-count": 0
      },
      "srv6-policy": {
        "tunnel-count": 0
      }
    }
  }
}
```