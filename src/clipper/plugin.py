from yapsy.PluginManager import PluginManager
from yapsy.IPlugin import IPlugin

from . import Singleton

# remove later
from pprint import PrettyPrinter
pp = PrettyPrinter().pprint



class PluginLoader(metaclass=Singleton):
    def __init__(self, pathname):
        self.pathname = pathname
        self.plugin_manager = PluginManager(directories_list=(pathname, ))
        self.plugin_manager.collectPlugins()

    def load_all_plugins(self):
        plugins = self.plugin_manager.getAllPlugins()
        for plugin in plugins:
            self.plugin_manager.activatePluginByName(plugin.name)


class SitePlugin(IPlugin):
    """
    Base class for plugins that define an interface to a website.
    More functionality will be added later
    """
    name='plugin'
    def __init__(self):
        # super().__init__()
        self._indexes = {}

    def get_indexes(self):
        """
        return a dictionary of site indexes available. The key will be
        displayed in the list view. The value is the method that will be
        invoked when the index is opened.
        """
        return self._indexes
    
    def add_index(self, site_name, method):
        """
        adds an index to the plugin
        """
        self._indexes[site_name] = method
