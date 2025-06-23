# Import everything from builtin module, so this can be used as a complete drop-in replacement
from ipaddress import (
    IPv4Address,
    IPv6Address,
    IPv4Interface,
    IPv6Interface,
    ip_address,
    ip_interface,
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
    ip_network,
)

__all__ = [
    "AddressValueError",
    "IPv4Address",
    "IPv6Address",
    "IPv4Interface",
    "IPv6Interface",
    "IPv4Network",
    "IPv6Network",
    "NetmaskValueError",
    "SubnetUtilsMixin",
    "ip_address",
    "ip_interface",
    "ip_network",
    "collapse_addresses",
    "get_mixed_type_key",
    "summarize_address_range",
    "v4_int_to_packed",
    "v6_int_to_packed",
]
