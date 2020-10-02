
import ipaddress

from .utils import (
    IPv4Subnet,
    IPv6Subnet,
    SubnetUtils,
)


def ip_network(*args, **kwargs):

    net = ipaddress.ip_network(*args, **kwargs)

    if isinstance(net, ipaddress.IPv4Network):
        net.__class__ = IPv4Subnet

    elif isinstance(net, ipaddress.IPv6Network):
        net.__class__ = IPv6Subnet

    else:
        raise ValueError('Unhandled network type: %s' % type(net))

    return net
