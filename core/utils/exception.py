"""
  @ Author:   Mr.Hat
  @ Date:     2024/3/30 14:05
  @ Description:
  @ History:
"""

class WebsocketClosedException(Exception):
    pass


class LowProxyScoreException(Exception):
    pass


class ProxyScoreNotFoundException(Exception):
    pass


class ProxyForbiddenException(Exception):
    pass
