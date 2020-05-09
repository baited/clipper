from yapsy.PluginManager import PluginManager
from yapsy.IPlugin import IPlugin

from . import Singleton


class PluginLoader(metaclass=Singleton):
    def __init__(self, pathname):
        self.pathname = pathname
        self.plugin_manager = PluginManager(directories_list=(pathname, ))
        self.plugin_manager.collectPlugins()

    def load_all_plugins(self):
        plugins = self.plugin_manager.getAllPlugins()
        print(f'{len(plugins)} plugins to load')
        for plugin in plugins:
            print(plugin)
            attrs = {}
            for a in dir(plugin):
                attrs[a] = getattr(plugin, a)
            
            from pprint import PrettyPrinter
            pp = PrettyPrinter().pprint
            pp(attrs)


class SitePlugin(IPlugin):
    """
    Base class for plugins that define an interface to a website.
    More functionality will be added later
    """
    name='plugin'
