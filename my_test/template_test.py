import wx
from blockwindow import BlockWindow

labels = "one two three four five six seven eight nine".split()


class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "StaticBoxSizer Test")
        self.panel = wx.Panel(self)

        # # make three static boxes with windows positioned inside them
        # box1 = self.MakeStaticBoxSizer("Box 1", labels[0:3])
        # box2 = self.MakeStaticBoxSizer("Box 2", labels[3:6])
        # box3 = self.MakeStaticBoxSizer("Box 3", labels[6:9])
        #
        # # We can also use a sizer to manage the placement of other
        # # sizers (and therefore the windows and sub-sizers that they
        # # manage as well.)
        # sizer = wx.BoxSizer(wx.HORIZONTAL)
        # sizer.Add(box1, 0, wx.ALL, 10)
        # sizer.Add(box2, 0, wx.ALL, 10)
        # sizer.Add(box3, 0, wx.ALL, 10)
        #
        # box = wx.StaticBox(self.panel, -1, boxlabel)
        # sizer = wx.StaticBoxSizer(box, wx.VERTICAL)
        # bw = BlockWindow(self.panel, label=label)

        # sizer.Add(bw, 0, wx.ALL, 2)
        # self._btn1 = wx.Button(self.panel, wx.ID_ANY, "Click me")
        # self._btn2 = wx.Button(self.panel, wx.ID_ANY, "Click you")

        box1 = wx.StaticBox(self.panel, -1, "Box 1",  size=(300,200))
        # box1_sizer = wx.StaticBoxSizer(box1, wx.HORIZONTAL)
        box1_sizer = wx.GridSizer(box1, wx.HORIZONTAL)

        # Add(self, item, int proportion=0, int flag=0, int border=0,
        #     PyObject userData=None)
        bw1 = BlockWindow(self.panel, label="Block Window 1")
        box1_sizer.Add(bw1, 0, wx.ALL, border=2, pos=(0,0))

        # Add(self, item, int proportion=0, int flag=0, int border=0,
        #     PyObject userData=None
        rtb = wx.ToggleButton(self.panel, label='red')
        box1_sizer.Add(rtb, 0, wx.ALL, border=2, pos=(0,1))


        box2 = wx.StaticBox(self.panel, -1, "Box 2", size=(300,200))
        box2_sizer = wx.StaticBoxSizer(box2, wx.HORIZONTAL)

        bw2 = BlockWindow(self.panel, label="Block Window 2")
        box2_sizer.Add(bw2, 0, wx.ALL, 2)

        # gb_sizer = wx.GridBagSizer(hgap=5, vgap=5)
        #
        # _btn1 = wx.Button(self, wx.ID_ANY, "Click me")
        # # self._btn2 = wx.Button(self, wx.ID_ANY, "Click you")
        # #
        # gb_sizer.Add(_btn1, pos=(0, 4))

        # bw1 = BlockWindow(self, label="span 3 rows")
        # gb_sizer.Add(bw1, pos=(0, 3), span=(3, 1), flag=wx.EXPAND)
        #
        # self._btn1 = wx.Button(self, wx.ID_ANY, "Click me")
        # self._btn2 = wx.Button(self, wx.ID_ANY, "Click you")
        #
        # gb_sizer.Add(self._btn1, pos=(0, 4))
        # gb_sizer.Add(self._btn2, pos=(1, 4))
        # self.self_test_txt = wx.StaticText(self, -1, "my Right Panel")
        # sizer.Add(self.self_test_txt, pos=(2, 4))


        gb_sizer = wx.GridBagSizer(hgap=5, vgap=5)
        gb_sizer.Add(box1_sizer, pos=(0, 1), span=(3, 1), flag=wx.EXPAND)
        gb_sizer.Add(box2_sizer, pos=(0, 2), span=(3, 1), flag=wx.EXPAND)
        # gb_sizer.Add(gb_sizer, pos=(0, 3), span=(3, 1), flag=wx.EXPAND)

        self.panel.SetSizer(gb_sizer)
        gb_sizer.Fit(self)

    def MakeStaticBoxSizer(self, boxlabel, itemlabels):
        # first the static box
        box = wx.StaticBox(self.panel, -1, boxlabel)

        # then the sizer
        sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        # then add items to it like normal
        for label in itemlabels:
            bw = BlockWindow(self.panel, label=label)
            sizer.Add(bw, 0, wx.ALL, 2)
            self._btn1 = wx.Button(self.panel, wx.ID_ANY, "Click me")
            self._btn2 = wx.Button(self.panel, wx.ID_ANY, "Click you")

            sizer.Add(self._btn1)
            sizer.Add(self._btn2)

        return sizer


app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()
