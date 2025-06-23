from __future__ import annotations
import typing as t
from ipaddress import (
    IPv4Address,
    IPv6Address,
    IPv4Network as builtin_IPv4Network,
    IPv6Network as builtin_IPv6Network,
    ip_address as builtin_ip_address,
    ip_network as builtin_ip_network,
)
import math

from random import randint


class SubnetUtilsMixin:
    """
    Mixin class to add useful utilities to IPv4Network and IPv6Network.
    """

    def divide(
        self, parts: int
    ) -> t.Generator[t.Union[IPv4Network, IPv6Network], None, None]:
        """Generator to return the resulting subnets after dividing a main network"""

        # Can't divide a subnet into less parts than 1, so guard against silliness
        if parts <= 1:
            subnet_diff = 0

        # Handle exact powers of 2 specifically
        elif (parts & (parts - 1)) == 0:
            subnet_diff = int(math.log2(parts))

        # And all other numbers fall here
        else:
            subnet_diff = int(math.log2(parts)) + 1

        if (subnet_diff + self.prefixlen) > self.max_prefixlen:
            raise ValueError(f"Unable to divide {self} into {parts} subnets.")

        yield from self.subnets(prefixlen_diff=subnet_diff)

    __truediv__ = divide

    def random_ip(self) -> t.Union[IPv4Address, IPv6Address]:
        """Returns a random IP from this subnet"""

        random_address = randint(
            int(self.network_address) + 1, int(self.broadcast_address) - 1
        )

        return builtin_ip_address(random_address)


class IPv4Network(builtin_IPv4Network, SubnetUtilsMixin):
    """
    This class represents and manipulates 32-bit IPv4 network + addresses..

    Attributes: [examples for IPv4Network('192.0.2.0/27')]
        .network_address: IPv4Address('192.0.2.0')
        .hostmask: IPv4Address('0.0.0.31')
        .broadcast_address: IPv4Address('192.0.2.32')
        .netmask: IPv4Address('255.255.255.224')
        .prefixlen: 27
    """

    pass  # pylint: disable=unnecessary-pass


class IPv6Network(builtin_IPv6Network, SubnetUtilsMixin):
    """
    This class represents and manipulates 128-bit IPv6 networks.

    Attributes: [examples for IPv6('2001:db8::1000/124')]
        .network_address: IPv6Address('2001:db8::1000')
        .hostmask: IPv6Address('::f')
        .broadcast_address: IPv6Address('2001:db8::100f')
        .netmask: IPv6Address('ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff0')
        .prefixlen: 124
    """

    pass  # pylint: disable=unnecessary-pass


def ip_network(*args, **kwargs) -> t.Union[IPv4Network, IPv6Network]:
    """Create an IPv4 or IPv6 network object."""

    net = builtin_ip_network(*args, **kwargs)

    if isinstance(net, builtin_IPv4Network):
        net.__class__ = IPv4Network

    elif isinstance(net, builtin_IPv6Network):
        net.__class__ = IPv6Network

    else:
        raise ValueError(f"Unhandled network type: {type(net)}")

    return net
