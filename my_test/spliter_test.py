import  wx

class MyFrame(wx.Frame):
       def __init__(self, parent):
           wx.Frame.__init__(self, parent)
           self.splitter = wx.SplitterWindow(self)

           pan1 = wx.Window(self.splitter, style=wx.BORDER_SUNKEN)
           pan1.SetBackgroundColour("yellow")
           wx.StaticText(pan1, -1, "My Left Panel")

           pan2 = wx.Window(self.splitter, style=wx.BORDER_SUNKEN)
           pan2.SetBackgroundColour("orange")
           wx.StaticText(pan2, -1, "my Right Panel")

           self.splitter.SplitVertically(pan1, pan2, -100)


if __name__ == '__main__':
       app = wx.PySimpleApp()
       frame = MyFrame(None)
       frame.Show()
       app.MainLoop()