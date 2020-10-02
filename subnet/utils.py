
import ipaddress
import math

from random import randint


class SubnetUtils:

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

        for subnet in self.subnets(prefixlen_diff=subnet_diff):
            yield subnet

    def random_ip(self):
        """Returns a random IP from this subnet"""

        random_address = randint(
            int(self.network_address)+1,
            int(self.broadcast_address)-1)

        return ipaddress.ip_address(random_address)


class IPv4Subnet(ipaddress.IPv4Network, SubnetUtils):
    pass


class IPv6Subnet(ipaddress.IPv6Network, SubnetUtils):
    pass
