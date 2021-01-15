# coding: utf8
PLUGIN_METADATA = {
    'id': 'rollingscoreboard',
    'version': '1.1.1-Alpha1',
    'name': 'RollingScoreboard',
    'description': 'Highly customized rolling scoreboard plugin based on MCDR',
    'author': 'WhitePaper',
    'link': 'https://github.com/AngelicaRoot/MCDR-RollingScoreboard',
    'dependencies': {
        'mcdreforged': '>=1.0.2'
    }
}


def test(server):
    from RollingScoreboardDependencies import _init_
    init = _init_.initPlugin(server)
    init.configInitializer(1)


def on_load(server, prev):
    server.register_event_listener('RollingScoreboard.test', test)
    test(server)