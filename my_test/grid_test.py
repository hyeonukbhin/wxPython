import wx
from blockwindow import BlockWindow

labels = "one two three four five six seven eight nine".split()


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "GridBagSizer Test")
        self.panel = wx.Panel(self)

        sizer = wx.GridBagSizer(hgap=5, vgap=5)
        for col in range(3):
            for row in range(3):
                bw = BlockWindow(self, label=labels[row * 3 + col])
                sizer.Add(bw, pos=(row, col))

        # add a window that spans several rows
        bw = BlockWindow(self, label="span 3 rows")
        sizer.Add(bw, pos=(0, 3), span=(3, 1), flag=wx.EXPAND)

        self._btn1 = wx.Button(self, wx.ID_ANY, "Click me")
        self._btn2 = wx.Button(self, wx.ID_ANY, "Click you")

        sizer.Add(self._btn1, pos=(0, 4))
        sizer.Add(self._btn2, pos=(1, 4))
        self.self_test_txt = wx.StaticText(self, -1, "my Right Panel")
        sizer.Add(self.self_test_txt, pos=(2, 4))

        # self.button = wx.Button(self, -1, "Hello", pos=(50, 20))
        # self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        # self.button.SetDefault()

        # add a window that spans all columns
        bw = BlockWindow(self, label="span all columns")
        sizer.Add(bw, pos=(3, 0), span=(1, 4), flag=wx.EXPAND)

        # make the last row and col be stretchable
        sizer.AddGrowableCol(3)
        sizer.AddGrowableRow(3)

#         # make three static boxes with windows positioned inside them
#         box1 = self.MakeStaticBoxSizer("Box 1", labels[0:3])
#         box2 = self.MakeStaticBoxSizer("Box 2", labels[3:6])
#         box3 = self.MakeStaticBoxSizer("Box 3", labels[6:9])
#
#         # We can also use a sizer to manage the placement of other
#         # sizers (and therefore the windows and sub-sizers that they
#         # manage as well.)
#         sizer = wx.BoxSizer(wx.HORIZONTAL)
#         sizer.Add(box1, 0, wx.ALL, 10)
#         sizer.Add(box2, 0, wx.ALL, 10)
#         sizer.Add(box3, 0, wx.ALL, 10)
#
#         self.panel.SetSizer(sizer)
#         sizer.Fit(self)


        self.SetSizer(sizer)
        self.Fit()


    def MakeStaticBoxSizer(self, boxlabel, itemlabels):
        # first the static box
        box = wx.StaticBox(self.panel, -1, boxlabel)

        # then the sizer
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        # then add items to it like normal
        for label in itemlabels:
            bw = BlockWindow(self.panel, label=label)
            sizer.Add(bw, 0, wx.ALL, 2)

        return sizer


# class TestFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, -1, "StaticBoxSizer Test")
#         self.panel = wx.Panel(self)
#
#         # make three static boxes with windows positioned inside them
#         box1 = self.MakeStaticBoxSizer("Box 1", labels[0:3])
#         box2 = self.MakeStaticBoxSizer("Box 2", labels[3:6])
#         box3 = self.MakeStaticBoxSizer("Box 3", labels[6:9])
#
#         # We can also use a sizer to manage the placement of other
#         # sizers (and therefore the windows and sub-sizers that they
#         # manage as well.)
#         sizer = wx.BoxSizer(wx.HORIZONTAL)
#         sizer.Add(box1, 0, wx.ALL, 10)
#         sizer.Add(box2, 0, wx.ALL, 10)
#         sizer.Add(box3, 0, wx.ALL, 10)
#
#         self.panel.SetSizer(sizer)
#         sizer.Fit(self)
#
#     def MakeStaticBoxSizer(self, boxlabel, itemlabels):
#         # first the static box
#         box = wx.StaticBox(self.panel, -1, boxlabel)
#
#         # then the sizer
#         sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
#
#         # then add items to it like normal
#         for label in itemlabels:
#             bw = BlockWindow(self.panel, label=label)
#             sizer.Add(bw, 0, wx.ALL, 2)
#
#         return sizer

app = wx.PySimpleApp()
TestFrame().Show()

app.MainLoop()
