
# Import everything from builtin module, so this can be used as a complete drop-in replacement
from ipaddress import (
    IPv4Address,
    IPv6Address,
    IPv4Interface,
    IPv6Interface,
    IPv4Network as builtin_IPv4Network,
    IPv6Network as builtin_IPv6Network,
    ip_address,
    ip_interface,
    ip_network as builtin_ip_network,
    collapse_addresses,
    get_mixed_type_key,
    summarize_address_range,
    v4_int_to_packed,
    v6_int_to_packed,
    AddressValueError,
    NetmaskValueError,
)

from .utils import (
    IPv4Network,
    IPv6Network,
    SubnetUtilsMixin,
)


def ip_network(*args, **kwargs):

    net = builtin_ip_network(*args, **kwargs)

    if isinstance(net, builtin_IPv4Network):
        net.__class__ = IPv4Network

    elif isinstance(net, builtin_IPv6Network):
        net.__class__ = IPv6Network

    else:
        raise ValueError('Unhandled network type: %s' % type(net))

    return net
