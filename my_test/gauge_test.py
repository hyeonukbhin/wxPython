import wx

TASK_RANGE = 50


class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.initui()

    def initui(self):
        self.timer = wx.Timer(self, 1)
        self.count = 0

        self.Bind(wx.EVT_TIMER, self.ontimer, self.timer)

        panel = wx.Panel(self)
        verticalbox = wx.BoxSizer(wx.VERTICAL)
        horizontalbox1 = wx.BoxSizer(wx.HORIZONTAL)
        horizontalbox2 = wx.BoxSizer(wx.HORIZONTAL)
        horizontalbox3 = wx.BoxSizer(wx.HORIZONTAL)

        self.gauge = wx.Gauge(panel, range=TASK_RANGE, size=(250, 25))
        self.button1 = wx.Button(panel, wx.ID_OK)
        self.button2 = wx.Button(panel, wx.ID_STOP)
        self.text = wx.StaticText(panel, label='Task to be done')

        self.Bind(wx.EVT_BUTTON, self.onok, self.button1)
        self.Bind(wx.EVT_BUTTON, self.onstop, self.button2)

        horizontalbox1.Add(self.gauge, proportion=1, flag=wx.ALIGN_CENTER)
        horizontalbox2.Add(self.button1, proportion=1, flag=wx.RIGHT, border=10)
        horizontalbox2.Add(self.button2, proportion=1, flag=wx.RIGHT, border=10)
        horizontalbox3.Add(self.text, proportion=1)
        verticalbox.Add((0, 30))
        verticalbox.Add(horizontalbox1, flag=wx.ALIGN_CENTER)
        verticalbox.Add((0, 20))
        verticalbox.Add(horizontalbox2, proportion=1, flag=wx.ALIGN_CENTER)
        verticalbox.Add(horizontalbox3, proportion=1, flag=wx.ALIGN_CENTER)

        panel.SetSizer(verticalbox)

        self.SetSize((300, 200))
        self.SetTitle('wx.Gauge')
        self.Center()
        self.Show(True)

    def onok(self, e):
        if self.count >= TASK_RANGE:
            return

        self.timer.Start(100)
        self.text.SetLabel('Task in Progress')

    def onstop(self, e):
        if self.count == 0 or self.count >= TASK_RANGE or not self.timer.IsRunning():
            return

        self.timer.Stop()
        self.text.SetLabel('Task Interrupted')

    def ontimer(self, e):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)

        if self.count == TASK_RANGE:
            self.timer.Stop()
            self.text.SetLabel('Task Completed')


if __name__ == '__main__':
    app = wx.App()
    Example(None)
    app.MainLoop()
