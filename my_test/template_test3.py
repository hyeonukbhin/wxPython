import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(390, 350))

        self.initui()
        self.Show()

    def initui(self):
        panel = wx.Panel(self)
        # panel.SetBackgroundColour('BLACK')
        font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)


        verticalbox = wx.BoxSizer(wx.VERTICAL)

        horizontalbox1 = wx.BoxSizer(wx.HORIZONTAL)
        # horizontalbox1

        statictxt1 = wx.StaticText(panel, label='Class Name1111111111111111')
        statictxt1.SetFont(font)
        statictxt1.SetForegroundColour('blue')
        statictxt1.SetBackgroundColour('green')
        # statictxt1.SetBackgroundColour('white')

        # statictxt1 = wx.StaticText(panel, label='Class Name', style=wx.wx.ALIGN_CENTER_HORIZONTAL)
        # center = wx.StaticText(panel, -1, "align center", (100, 50), (160, -1), wx.ALIGN_CENTRE)


        # __init__(self, Window parent, int id=-1, String label=EmptyString,
        #     Point pos=DefaultPosition, Size size=DefaultSize,
        #     long style=0, String name=StaticTextNameStr) -> StaticText

        horizontalbox1.Add(statictxt1, proportion=1, flag=wx.CENTER, border=8)

        statictxt2 = wx.StaticText(panel, label='Class 222222222222222')
        statictxt2.SetFont(font)
        statictxt2.SetForegroundColour('blue')
        statictxt2.SetBackgroundColour('black')

        horizontalbox1.Add(statictxt2, proportion=1, flag=wx.RIGHT, border=8)

        # txtctrl1 = wx.TextCtrl(panel)
        # horizontalbox1.Add(txtctrl1, proportion=1)
        verticalbox.Add(horizontalbox1, flag=wx.EXPAND | wx.ALIGN_CENTER, border=10)
        #
        # verticalbox.Add((-1, 10))
        #
        # horizontalbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # statictxt2 = wx.StaticText(panel, label='Matching Classes')
        # statictxt2.SetFont(font)
        # horizontalbox2.Add(statictxt2)
        # verticalbox.Add(horizontalbox2, flag=wx.LEFT | wx.TOP, border=10)
        #
        # verticalbox.Add((-1, 10))
        #
        # horizontalbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # txtctrl2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        # horizontalbox3.Add(txtctrl2, proportion=1, flag=wx.EXPAND)
        # verticalbox.Add(horizontalbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        #
        # verticalbox.Add((-1, 25))
        #
        # horizontalbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # checkbox1 = wx.CheckBox(panel, label='Case Sensitive')
        # checkbox1.SetFont(font)
        # horizontalbox4.Add(checkbox1)
        # checkbox2 = wx.CheckBox(panel, label='Nested Classes')
        # checkbox2.SetFont(font)
        # horizontalbox4.Add(checkbox2, flag=wx.LEFT, border=10)
        # checkbox3 = wx.CheckBox(panel, label='Non-Project Classes')
        # checkbox3.SetFont(font)
        # horizontalbox4.Add(checkbox3, flag=wx.LEFT, border=10)
        # verticalbox.Add(horizontalbox4, flag=wx.LEFT, border=10)
        #
        # verticalbox.Add((-1, 15))
        #
        # horizontalbox5 = wx.BoxSizer(wx.HORIZONTAL)
        # btn1 = wx.Button(panel, label='OK', size=(70, 30))
        # horizontalbox5.Add(btn1)
        # btn2 = wx.Button(panel, label='Close', size=(70, 30))
        # horizontalbox5.Add(btn2, flag=wx.LEFT | wx.Bottom, border=5)
        # verticalbox.Add(horizontalbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
        #
        # verticalbox.Add((-1, 50))
        #
        # # panel.SetSizer(verticalbox)
        #
        # main_horizontalbox.Add(verticalbox)
        # verticalbox = wx.BoxSizer(wx.VERTICAL)
        #
        # horizontalbox1 = wx.BoxSizer(wx.HORIZONTAL)
        #
        # statictxt1 = wx.StaticText(panel, label='Class Name')
        # statictxt1.SetFont(font)
        #
        # horizontalbox1.Add(statictxt1, flag=wx.RIGHT, border=8)
        # txtctrl1 = wx.TextCtrl(panel)
        # horizontalbox1.Add(txtctrl1, proportion=1)
        # verticalbox.Add(horizontalbox1, flag=wx.EXPAND | wx.TOP, border=10)
        #
        # verticalbox.Add((-1, 10))
        #
        # horizontalbox2 = wx.BoxSizer(wx.HORIZONTAL)
        # statictxt2 = wx.StaticText(panel, label='Matching Classes')
        # statictxt2.SetFont(font)
        # horizontalbox2.Add(statictxt2)
        # verticalbox.Add(horizontalbox2, flag=wx.LEFT | wx.TOP, border=10)
        #
        # verticalbox.Add((-1, 10))
        #
        # horizontalbox3 = wx.BoxSizer(wx.HORIZONTAL)
        # txtctrl2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        # horizontalbox3.Add(txtctrl2, proportion=1, flag=wx.EXPAND)
        # verticalbox.Add(horizontalbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        #
        # verticalbox.Add((-1, 25))
        #
        # horizontalbox4 = wx.BoxSizer(wx.HORIZONTAL)
        # checkbox1 = wx.CheckBox(panel, label='Case Sensitive')
        # checkbox1.SetFont(font)
        # horizontalbox4.Add(checkbox1)
        # checkbox2 = wx.CheckBox(panel, label='Nested Classes')
        # checkbox2.SetFont(font)
        # horizontalbox4.Add(checkbox2, flag=wx.LEFT, border=10)
        # checkbox3 = wx.CheckBox(panel, label='Non-Project Classes')
        # checkbox3.SetFont(font)
        # horizontalbox4.Add(checkbox3, flag=wx.LEFT, border=10)
        # verticalbox.Add(horizontalbox4, flag=wx.LEFT, border=10)
        #
        # verticalbox.Add((-1, 15))
        #
        # horizontalbox5 = wx.BoxSizer(wx.HORIZONTAL)
        # btn1 = wx.Button(panel, label='OK', size=(70, 30))
        # horizontalbox5.Add(btn1)
        # btn2 = wx.Button(panel, label='Close', size=(70, 30))
        # horizontalbox5.Add(btn2, flag=wx.LEFT | wx.Bottom, border=5)
        # verticalbox.Add(horizontalbox5, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)
        #
        # verticalbox.Add((-1, 50))
        # main_horizontalbox.Add(verticalbox)
        panel.SetSizer(verticalbox)


def main():
    app = wx.App()
    Example(None, title='Go to Class')
    app.MainLoop()


if __name__ == '__main__':
    main()

