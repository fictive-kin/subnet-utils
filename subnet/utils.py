
from ipaddress import (
    IPv4Network as builtin_IPv4Network,
    IPv6Network as builtin_IPv6Network,
    ip_address as builtin_ip_address,
)
import math

from random import randint


class SubnetUtilsMixin:

    def divide(self, parts):
        """ Generator to return the resulting subnets after dividing a main network """

        # Can't divide a subnet into less parts than 1, so guard against silliness
        if parts <= 1:
            subnet_diff = 0

        # Handle exact powers of 2 specifically
        elif (parts & (parts - 1)) == 0:
            subnet_diff = int(math.log2(parts))

        # And all other numbers fall here
        else:
            subnet_diff = int(math.log2(parts)) + 1

        if (subnet_diff+self.prefixlen) > self.max_prefixlen:
            raise ValueError('Unable to divide %s into %s subnets.' % (self, parts))

        yield from self.subnets(prefixlen_diff=subnet_diff)

    __truediv__ = divide

    def random_ip(self):
        """Returns a random IP from this subnet"""

        random_address = randint(
            int(self.network_address)+1,
            int(self.broadcast_address)-1)

        return builtin_ip_address(random_address)


class IPv4Network(builtin_IPv4Network, SubnetUtilsMixin):
    pass


class IPv6Network(builtin_IPv6Network, SubnetUtilsMixin):
    pass
