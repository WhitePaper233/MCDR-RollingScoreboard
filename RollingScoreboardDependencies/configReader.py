# coding: utf8
"""
Some basic functions to read the config file
"""
import ruamel.yaml as yml
import os


def readAll():
    """
    读取Config设置中的所有选项的值
    :return: 所有选项的字典或'error'为键，错误信息为值的字典
    """
    path = os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml')
    try:
        with open(path, encoding='utf8') as f:
            return yml.safe_load(f)
    except BaseException as reason:
        returnDict = {'error': reason}
        return returnDict


def readLanguage():
    """
    读取Config设置中的language选项的值
    :return: language选项的值或错误信息
    """
    path = os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml')
    try:
        with open(path, encoding='utf8') as f:
            return yml.safe_load(f)['language']
    except BaseException as reason:
        return reason


def readFilter():
    """
    读取Config设置中的filter选项的值
    :return: language选项的值或错误信息
    """
    path = os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml')
    try:
        with open(path, encoding='utf8') as f:
            return yml.safe_load(f)['filter']
    except BaseException as reason:
        return reason


def readDefaultScoreboardInterval():
    """
    读取Config设置中的default_scoreboard_interval选项的值
    :return: default_scoreboard_interval选项的值(float)或错误信息
    """
    path = os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml')
    try:
        with open(path, encoding='utf8') as f:
            return float(yml.safe_load(f)['default_scoreboard_interval'])
    except BaseException as reason:
        return reason


def readPreventScoreboardConfusion():
    """
    读取Config设置中的prevent_scoreboard_confusion选项的值
    :return: prevent_scoreboard_confusion选项的值(bool)或错误信息
    """
    path = os.path.join(os.getcwd(), 'config', 'RollingScoreboard', 'config.yml')
    path = r'F:\SourceCodes\MCDR-RollingScoreboard\config\RollingScoreboard\config.yml'
    try:
        with open(path, encoding='utf8') as f:
            print(yml.safe_load(f)['prevent_scoreboard_confusion'])
            # if yml.safe_load(f)['prevent_scoreboard_confusion'] == 'true':
            #     return True
            # elif yml.safe_load(f)['prevent_scoreboard_confusion'] == 'false':
            #     return False
            # else:
            #     return f'''[Error]The "prevent_scoreboard_confusion" value can only be "true" or "false", value "{yml.
            #         safe_load(f)['prevent_scoreboard_confusion']}" is invalid'''
    except BaseException as reason:
        return reason


print(readPreventScoreboardConfusion())