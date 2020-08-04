import wx


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.initui()

    def initui(self):
        panel = wx.Panel(self)

        button = wx.Button(panel, label='Button', pos=(20, 20))
        text = wx.CheckBox(panel, label='CheckBox', pos=(20, 90))
        combo = wx.ComboBox(panel, pos=(120, 22), choices=['Python', 'Ruby'])
        slider = wx.Slider(panel, 5, 6, 1, 10, (120, 90), (110, -1))

        panel.Bind(wx.EVT_ENTER_WINDOW, self.onwidgetenter)
        button.Bind(wx.EVT_ENTER_WINDOW, self.onwidgetenter)
        text.Bind(wx.EVT_ENTER_WINDOW, self.onwidgetenter)
        combo.Bind(wx.EVT_ENTER_WINDOW, self.onwidgetenter)
        slider.Bind(wx.EVT_ENTER_WINDOW, self.onwidgetenter)

        self.statusbar = self.CreateStatusBar()

        self.SetSize((250, 230))
        self.SetTitle('wx.StatusBar')
        self.Center()
        self.Show(True)

    def onwidgetenter(self, e):
        name = e.GetEventObject().GetClassName()
        self.statusbar.SetStatusText(name + 'widget')
        e.Skip()


if __name__ == '__main__':
    app = wx.App()
    Example(None)
    app.MainLoop()
