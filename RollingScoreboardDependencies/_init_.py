# coding: utf8
"""
RollingScoreboard Plugin provides a large number of operations on the game scoreboard,including:
    1.Add automatic display scoreboard
    2.Custom scoreboard title (including title content, color and font style), statistical items, etc
    3.Filtering statistical items with WhitePaper's whitelist plugin or the build-in automatic filter
    4.Automatic start & stop rolling
    5.Automatic clean server log file
    etc
This project is open source on GitHub and Gitee, and complies with GPL-3.0 LICENSE. I accept all constructive PRs and
issues.
"""

import os

class initPlugin:
    """
    用于初始化插件的类
    """
    def __init__(self, server):
        """
        类初始化
        """
        self.server = server

    def configChecker(self):
        """
        检查插件配置文件是否正确
        :return: 0：全部初始化完成；1：未初始化config.yml；2：未初始化scoreboards.json；3：全部未初始化完成
        """
        path = os.getcwd()
        self.server.logger.info(path)
        if os.path.exists(os.path.join(path, 'config', 'RollingScoreboard', 'config.yml')) \
                and os.path.exists(os.path.join(path, 'config', 'RollingScoreboard', 'scoreboards.json')):
            return 0
        elif os.path.exists(os.path.join(path, 'config', 'RollingScoreboard', 'config.yml')):
            return 1
        elif os.path.exists(os.path.join(path, 'config', 'RollingScoreboard', 'scoreboards.json')):
            return 2
        else:
            return 3

    def configInitializer(self, mode):
        """
        执行初始化
        :param mode: 初始化模式：0：无需初始化；1：初始化config.yml；2：初始化scoreboards.json；3：全部初始化
        :return: 'normal'：初始化正常完成；否则输出错误信息
        """
        if mode == 0:
            return 'normal'
        elif mode == 1:
            with open(os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml'), encoding='utf8') as f:
                f.write('hello')
        else:
            pass