import ipaddress
from define import ADDR_TYPE


class NeedMoreData(object):
    event_type = "NeedMoreData"

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "NeedMoreData"


class GreetingRequest(object):
    event_type = "GreetingRequest"

    def __init__(self, version, nmethod, methods):
        self.version = version
        self.nmethod = nmethod
        self.methods = methods

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "SOCKSv{0} Greeting Request: number of method: {1}, Auth Types : {2}".format(
            self.version, self.nmethod, self.methods)


class GreetingResponse(object):
    event_type = "GreetingResponse"

    def __init__(self, version, auth_type):
        self.version = version
        self.auth_type = auth_type

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "SOCKSv{0} Greeting Response: Auth Type : {1}".format(
            self.version, self.auth_type)


class AuthRequest(object):
    event_type = "AuthRequest"

    def __init__(self, version, username, password):
        self.version = version
        self.username = username
        self.password = password

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "SOCKSv{0} Auth Request: username: {1}, password: {2}".format(
            self.version, self.username, self.password)


class AuthResponse(object):
    event_type = "AuthResponse"

    def __init__(self, version, status):
        self.version = version
        self.status = status

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        return "SOCKSv{0} Auth Response: status: {1}".format(
            self.version, self.status)


class Request(object):
    event_type = "Request"

    def __init__(self, version, cmd, atyp, addr, port):
        self.version = version
        self.cmd = cmd
        self.atyp = atyp
        self.addr = addr
        self.port = port

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        if self.atyp == ADDR_TYPE["IPV4"]:
            return "SOCKSv{0} Request: Command : {1}, Addr : {2} Port : {3}".format(
                self.version, self.cmd,
                ipaddress.IPv4Address(self.addr), self.port)

        if self.atyp == ADDR_TYPE["IPV6"]:
            return "SOCKSv{0} Request: Command : {1}, Addr : {2} Port : {3}".format(
                self.version, self.cmd,
                ipaddress.IPv6Address(self.addr), self.port)

        if self.atyp == ADDR_TYPE["DOMAINNAME"]:
            return "SOCKSv{0} Request: Command : {1}, Addr : {2} Port : {3}".format(
                self.version, self.cmd,
                self.addr, self.port)


class Response(object):
    event_type = "Response"

    def __init__(self, version, status, atyp, addr, port):
        self.version = version
        self.status = status
        self.atyp = atyp
        self.addr = addr
        self.port = port

    def __eq__(self, value):
        return self.event_type == value

    def __ne__(self, value):
        return not self.__eq__(value)

    def __str__(self):
        if self.atyp == ADDR_TYPE["IPV4"]:
            return "SOCKSv{0} Response: Status : {1}, Addr : {2} Port : {3}".format(
                self.version, self.status,
                ipaddress.IPv4Address(self.addr), self.port)

        if self.atyp == ADDR_TYPE["IPV6"]:
            return "SOCKSv{0} Response: Status : {1}, Addr : {2} Port : {3}".format(
                self.version, self.status,
                ipaddress.IPv6Address(self.addr), self.port)

        if self.atyp == ADDR_TYPE["DOMAINNAME"]:
            return "SOCKSv{0} Response: Status : {1}, Addr : {2} Port : {3}".format(
                self.version, self.status,
                self.addr, self.port)
