from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.python import log

class DumbBot(irc.IRCClient):
    """A bot that does a thing."""

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        log.msg("connectionMade")
        self.nickname = self.factory.nickname
        self.setNick(self.nickname)

    def signedOn(self):
        log.msg("signed on; joining channel {}".format(self.factory.channel))
        self.join(self.factory.channel)

    def joined(self, channel):
        log.msg("joined channel {}".format(channel))

    def privmsg(self, user, channel, msg):
        if msg.startswith(self.nickname + ":"):
            self.msg(channel, "I don't really do much.")
    
class DumbIRCFactory(protocol.ClientFactory):
    protocol = DumbBot

    def __init__(self, channel, nickname="ThisIsANickname"):
        self.nickname = nickname
        self.channel = channel

