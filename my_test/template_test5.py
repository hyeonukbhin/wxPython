import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 250))

        self.initui()
        self.Show()

    def initui(self):
        # menubar = wx.MenuBar()
        # menu_file = wx.Menu()
        # menubar.Append(menu_file, '&File')
        # self.SetMenuBar(menubar)

        verticalbox = wx.BoxSizer(wx.HORIZONTAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        verticalbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)

        self.statix_txt = wx.StaticText(self, label='Class', style=wx.ALIGN_CENTRE_HORIZONTAL, size=(100,30))
        self.right = wx.StaticText(self, -1, "align right", (100, 70), (160, -1), wx.ALIGN_RIGHT)
        self.right.SetBackgroundColour('black')
        self.right.SetForegroundColour('red')

        verticalbox.Add(self.right, flag=wx.TOP | wx.ALIGN_BOTTOM, border=4)

        # statictxt1 = wx.StaticText(panel, label='Class Name1111111111111111')
        self.btn1 = wx.Button(self, label='OK', size=(70, 30))

        # self.button = wx.TextCtrl(self, style=wx.TE_RIGHT)
        verticalbox.Add(self.btn1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        gridsizer = wx.GridSizer(5, 4, 5, 5)

        gridsizer.AddMany([
            (wx.Button(self, label='Cls'), 0, wx.EXPAND),
            (wx.Button(self, label='Bck'), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.Button(self, label='Close'), 0, wx.EXPAND),
            (wx.Button(self, label='7'), 0, wx.EXPAND),
            (wx.Button(self, label='8'), 0, wx.EXPAND),
            (wx.Button(self, label='9'), 0, wx.EXPAND),
            (wx.Button(self, label='/'), 0, wx.EXPAND),
            (wx.Button(self, label='4'), 0, wx.EXPAND),
            (wx.Button(self, label='5'), 0, wx.EXPAND),
            (wx.Button(self, label='6'), 0, wx.EXPAND),
            (wx.Button(self, label='*'), 0, wx.EXPAND),
            (wx.Button(self, label='1'), 0, wx.EXPAND),
            (wx.Button(self, label='2'), 0, wx.EXPAND),
            (wx.Button(self, label='3'), 0, wx.EXPAND),
            (wx.Button(self, label='-'), 0, wx.EXPAND),
            (wx.Button(self, label='0'), 0, wx.EXPAND),
            (wx.Button(self, label='.'), 0, wx.EXPAND),
            (wx.Button(self, label='='), 0, wx.EXPAND),
            (wx.Button(self, label='+'), 0, wx.EXPAND)
        ])
        verticalbox.Add(gridsizer, proportion=1, flag=wx.EXPAND)
        self.SetSizer(verticalbox)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title='Calc')
    app.MainLoop()
