
Subnet Utilities
================

This is a Python module for manipulating subnet information. It adds useful
utilities to the built-in Python `ipaddress` library. It requires Python 3+
and supports both IPv4 and IPv6 subnets.


Example usage
-------------

Create a subnet object::

    from subnet import ip_network, IPv4Network, IPv6Network

    # The simple way takes either IPv4 or IPv6 CIDR notation
    my_subnet = ip_network('10.10.0.0/16')

    # The specific type way
    my_ipv4_subnet = IPv4Network('10.10.0.0/16')
    my_ipv6_subnet = IPv6Network('fd3e:48fe:59b2:43ca::/64')


Divide a subnet into useful chunks (as evenly as plausible)::

    for subnet in my_ipv4_subnet.divide(6):
        print(subnet)

    for subnet in my_ipv6_subnet.divide(2):
        print(subnet)


Get a random ip from a subnet::

    print(my_subnet.random_ip())


Command line usage
------------------

It is also possible to perform various tasks from the command line directly::

    $ network-divide 10.0.0.0/8 4
    $ network-random-ip fd3e:48fe:59b2:43ca::/64
    $ network-info 192.168.0.0/24
