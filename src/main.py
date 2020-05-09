import wx
import sys
import os
from clipper.plugin import PluginLoader


def main():
    # get the data directories
    directory = {}
    if getattr(sys, 'frozen', False):
        directory['current'] = os.path.normpath(os.path.dirname(sys.executable))
    else:
        directory['current'] = os.path.normpath(os.path.dirname(__file__))

    directory['data'] = os.path.join(directory['current'], 'data')
    directory['plugin'] = os.path.join(directory['current'], 'plugins')

    # load plugins
    loader = PluginLoader(directory['plugin'])
    loader.load_all_plugins()

    # build gui
    app = wx.App()
    frame = wx.Frame(None)
    MainFrame(frame)
    frame.Show()
    app.MainLoop()


class MainFrame(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.list = wx.ListCtrl(self)
        sizer.Add(self.list, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()


if __name__ == '__main__':
    main()