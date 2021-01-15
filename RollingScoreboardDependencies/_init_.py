"""
RollingScoreboard Plugin provides a large number of operations on the game scoreboard,including:
    1.Add automatic display scoreboard
    2.Custom scoreboard title (including title content, color and font style), statistical items, etc
    3.Filtering statistical items with WhitePaper's whitelist plugin or the build-in automatic filter
    4.Automatic start & stop rolling
    5.Automatic clean server log file
    etc
<<<<<<< HEAD
This project is open source on GitHub and Gitee, and complies with gpl-3.0 protocol. I accept all constructive PRs and
issues.
"""


class initPlugin():
    def __init__(self, server):
        from os import getcwd
        self.getcwd = getcwd()
        self.server = server

    def checker(self):
        path = self.getcwd
        self.server.logger.info(path)
