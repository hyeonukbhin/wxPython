import wx
import time

def ReadData():
    with open('RealTime.txt') as f:
        for line in f:
            data = line.split()
    results = map(float, data)
    return results

class BlockWindow(wx.Panel):
    # code on book "wxPython in action" Listing 11.1
    def __init__(self, parent, ID=-1, label="",
                 pos = wx.DefaultPosition, size = (100, 25)):
        wx.Panel.__init__(self, parent, ID, pos, size,
                          wx.RAISED_BORDER, label)
        self.label = label

        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    def OnPaint(self, evt):
        sz = self.GetClientSize()
        dc = wx.PaintDC(self)
        w,h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())
        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)

    def UpdateLabel(self, label):
        self.label = label
        self.Refresh()

class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(0,0))

        sizer = wx.GridBagSizer(hgap=5, vgap=-1)
        bw = BlockWindow(self, label="Item 1" )
        sizer.Add(bw, pos=(4, 2))

        self.block = BlockWindow(self, label="")
        sizer.Add(self.block, pos=(5, 2))

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(sizer, 0, wx.EXPAND|wx.ALL, 10)

        self.SetSizer(mainSizer)
        self.Fit()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(3000)

    def OnTimer(self, evt):
        # Data = ReadData()
        Data = [1,2,3,4,5,6]
        self.block.UpdateLabel("Updated : %.3f" % Data[0])

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title=' Frame Title')
        mypanel = MyPanel(self)
        self.SetSize(wx.Size(800,600))
        self.Centre()

app = wx.App(False)
MyFrame().Show()
app.MainLoop()