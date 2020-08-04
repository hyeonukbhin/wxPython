# -*- coding: utf-8 -*-

import wx.media
import roslib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import wx
import etc_functions as ef

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')


# VOICE_AMP_SCALE = "linear"

class ImageVoicePanel(wx.Panel):

    def __init__(self, parent, voice_scale="linear"):
        wx.Panel.__init__(self, parent)
        _sizer = wx.GridBagSizer(hgap=3, vgap=-1)


        self.SetBackgroundColour(wx.WHITE)

        panel_title_image = ef.BlockWindow(self, ID=-1, label="ROS Image Viewer", size=(630, 50), style=wx.ALL,
                                        label_color=wx.WHITE, bg_color='#363b41',
                                        font_set=[18, wx.NORMAL, wx.NORMAL, wx.BOLD])

        _sizer.Add(panel_title_image, pos=(0, 0), span=(1, 3), flag=wx.EXPAND)

        self.ros_image = ImageViewPanel(self, size=(630, 480), bg_color=wx.WHITE)
        _sizer.Add(self.ros_image, pos=(1, 0), span=(23, 3), flag=wx.EXPAND)

        panel_title_voice = ef.BlockWindow(self, ID=-1, label="ROS Voice Viewer", size=(500, 50), style=wx.ALL,
                                        label_color=wx.WHITE, bg_color='#363b41',
                                        font_set=[18, wx.NORMAL, wx.NORMAL, wx.BOLD])
        _sizer.Add(panel_title_voice, pos=(25, 0), span=(1, 3), flag=wx.EXPAND)

        self.ros_voice = VoiceViewPanel(self, scale=voice_scale)
        _sizer.Add(self.ros_voice, pos=(26, 0), span=(23, 3), flag=wx.EXPAND)


        _sizer.AddGrowableCol(0)
        self.SetSizer(_sizer)


class ImageViewPanel(wx.Panel):
    """ class ImageViewPanel creates a panel with an image on it, inherits wx.Panel """

    def __init__(self, parent, ID=-1, pos=wx.DefaultPosition, size=(640, 480), style=wx.ALL, bg_color=wx.WHITE):
        wx.Panel.__init__(self, parent, ID, pos, size, style=style)

        self.count = 0
        self.SetBackgroundColour(bg_color)

    def update(self, image):
        # http://www.ros.org/doc/api/sensor_msgs/html/msg/Image.html
        if not hasattr(self, 'staticbmp'):
            self.staticbmp = wx.StaticBitmap(self)
            # frame = self.GetParent()
            # panel = self
            self.SetSize((image.width, image.height))

        if image.encoding == 'rgba8':
            bmp = wx.BitmapFromBufferRGBA(image.width, image.height, image.data)
            self.staticbmp.SetBitmap(bmp)
        elif image.encoding == 'rgb8':
            bmp = wx.BitmapFromBuffer(image.width, image.height, image.data)
            self.staticbmp.SetBitmap(bmp)


class VoiceViewPanel(wx.Panel):
    def __init__(self, parent, scale="linear"):
        wx.Panel.__init__(self, parent)
        self.scale=scale
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        # self.SetBackgroundColour(wx.WHITE)
        # self.canvas.SetBackgroundColour(wx.WHITE)
        self.figure.patch.set_facecolor('white')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        x = range(0, 8000)
        y = [0] * len(x)
        self.set_ylim_graph(self.scale)
        self.axes.plot(x, y)

    def update(self, data):
        x = range(0, len(data))
        y = data
        self.axes.clear()
        self.set_ylim_graph(self.scale)
        self.axes.plot(x, y)
        self.canvas.draw()
        # self.canvas.flush_events()

    def set_ylim_graph(self, scale):
        if scale == "linear":
            self.axes.set_ylim([-2 ** 15, (2 ** 15) - 1])
        elif scale == "db":
            self.axes.set_ylim([-10, 100])
        else:
            print("ylim not set")



