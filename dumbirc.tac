from twisted.application import internet, service
from dumbbot import DumbIRCFactory

application = service.Application("DumbIRC")
internet.TCPClient("irc.desertbus.org", 6667, DumbIRCFactory("#desertbus", "DumbBot")).setServiceParent(application)
internet.TCPClient("irc.desertbus.org", 6667, DumbIRCFactory("#desertbus", "DumberBot")).setServiceParent(application)
