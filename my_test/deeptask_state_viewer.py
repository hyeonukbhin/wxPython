# -*- coding: utf-8 -*-

import wx  # For graphics' interface
import os  # For operating system compatibility

import wx
import wx.media
import rospy
import time

import roslib

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')
import rospy
from sensor_msgs.msg import Image

import wx
import sys
import rospy
from audio_msgs.msg import AudioData, FeatureData
import numpy as np
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, id, title):
        # SETUP
        wx.Frame.__init__(self, parent, -1, title="MyTitle", size=(1800, 1000))
        self.dirname = ''

        self.top_panel = TopPanel(self)


class VoicePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.draw()

    def draw(self):
        x = range(0, 8000)
        y = [0] * len(x)
        self.axes.set_ylim([-10, 100])
        self.axes.plot(x, y)

    def update(self, data):
        x = range(0, len(data))
        y = data
        self.axes.clear()
        # self.axes.set_ylim([-2 ** 15, (2 ** 15) - 1])
        self.axes.set_ylim([-10, 100])
        self.axes.plot(x, y)
        self.canvas.draw()
        self.canvas.flush_events()



class ImagePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # self.SetBackgroundColour(wx.BLACK)
        # _sizer = wx.BoxSizer(wx.VERTICAL)
        _sizer = wx.GridBagSizer(hgap=3, vgap=-1)
        self.SetBackgroundColour(wx.WHITE)


        panel_title_image = BlockWindow(self, ID=-1, label="ROS Image Viewer",size=(630,50), style=wx.ALL, label_color=wx.WHITE, bg_color='#363b41', font_set=[18,wx.NORMAL,wx.NORMAL,wx.BOLD])

        _sizer.Add(panel_title_image, pos=(0, 0), span=(1, 3), flag=wx.EXPAND)
        #
        # _sizer.Add(panel_title_image, flag=wx.TOP | wx.BOTTOM, border=5)

        self.ros_image = ImageViewPanel(self, size=(630,480))
        # _sizer.Add(self.ros_image, proportion=1, flag=wx.EXPAND)
        _sizer.Add(self.ros_image, pos=(1, 0), span=(23, 3), flag=wx.EXPAND)
        # _sizer.Add(self.ros_image, pos=(1, 0), span=(24, 3), flag=wx.EXPAND)

        panel_title_voice = BlockWindow(self, ID=-1, label="ROS Voice Viewer",size=(500,50), style=wx.ALL, label_color=wx.WHITE, bg_color='#363b41', font_set=[18,wx.NORMAL,wx.NORMAL,wx.BOLD])
        _sizer.Add(panel_title_voice, pos=(25, 0), span=(1, 3), flag=wx.EXPAND)

        self.ros_voice = VoicePanel(self)
        _sizer.Add(self.ros_voice, pos=(26, 0), span=(23, 3), flag=wx.EXPAND)


        # _sizer.Add(panel_title_voice, proportion=0, flag=wx.EXPAND)


        # title_pi = BlockWindow(self, ID=-1, label="Personal Information", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        #
        # _sizer.Add(title_pi, pos=(25, 0), span=(1, 3), flag=wx.EXPAND)
        # title_pi = BlockWindow(self, ID=-1, label="Voice Signal Viewer", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])


        _sizer.AddGrowableCol(0)
        self.SetSizer(_sizer)


class StatePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # self.SetBackgroundColour(wx.NullColour)
        self.SetBackgroundColour(wx.WHITE)
        _sizer = wx.GridBagSizer(hgap=5, vgap=-1)

        panel_title = BlockWindow(self, ID=-1, label="Perception Status",size=(640,50), style=wx.ALL, label_color=wx.WHITE, bg_color='#363b41', font_set=[18,wx.NORMAL,wx.NORMAL,wx.BOLD])

        _sizer.Add(panel_title, pos=(0, 0), span=(1, 5), flag=wx.EXPAND)

        title_pi = BlockWindow(self, ID=-1, label="Personal Information", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        _sizer.Add(title_pi, pos=(2, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_pi_label = wx.BoxSizer(wx.HORIZONTAL)

        labels_pi = ["Name", "Age", "Gender"]
        for idx, val in enumerate(labels_pi):
            box_sizer_pi_label.Add(BlockWindow(self, label="{}".format(val), label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)
        _sizer.Add(box_sizer_pi_label, pos=(3, 0), span=(1, 5), flag=wx.EXPAND)


        box_sizer_pi_value = wx.BoxSizer(wx.HORIZONTAL)
        self.pi_name=BlockWindow(self, label="{}".format(""), style=wx.ALL, size=(100,50),label_color=wx.BLACK, bg_color=wx.WHITE)
        box_sizer_pi_value.Add(self.pi_name, proportion=1,flag=wx.EXPAND)

        self.pi_age=BlockWindow(self, label="{}".format(""), style=wx.ALL, size=(100,50), label_color=wx.BLACK, bg_color=wx.WHITE)
        box_sizer_pi_value.Add(self.pi_age, proportion=1,flag=wx.EXPAND)

        self.pi_gender=BlockWindow(self, label="{}".format(""),style=wx.ALL, size=(100,50), label_color=wx.BLACK, bg_color=wx.WHITE)
        box_sizer_pi_value.Add(self.pi_gender, proportion=1,flag=wx.EXPAND)

        _sizer.Add(box_sizer_pi_value, pos=(4, 0), span=(1, 5), flag=wx.EXPAND)


        title_mot= BlockWindow(self, ID=-1, label="Motion", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        _sizer.Add(title_mot, pos=(5, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_motion_label = wx.BoxSizer(wx.HORIZONTAL)

        labels_pi = ["attention", "encouragement", "greeting"]
        for idx, val in enumerate(labels_pi):
            box_sizer_motion_label.Add(BlockWindow(self, label="{}".format(val),label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        _sizer.Add(box_sizer_motion_label, pos=(6, 0),span=(1, 5), flag=wx.EXPAND)

        box_sizer_motion_led = wx.BoxSizer(wx.HORIZONTAL)
        self.led_attention = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_motion_led.Add(self.led_attention, proportion=1,flag=wx.EXPAND)

        self.led_encouragement = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_motion_led.Add(self.led_encouragement, proportion=1, flag=wx.EXPAND)

        self.led_greeting = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_motion_led.Add(self.led_greeting, proportion=1, flag=wx.EXPAND)
        _sizer.Add(box_sizer_motion_led, pos=(7, 0), span=(1, 5), flag=wx.EXPAND)

        title_rl= BlockWindow(self, ID=-1, label="Relative Location", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        _sizer.Add(title_rl, pos=(8, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_rl = wx.BoxSizer(wx.HORIZONTAL)

        labels_rl = ["near_robot", "near_signboard", "near_restroom"]
        for idx, val in enumerate(labels_rl):
            box_sizer_rl.Add(BlockWindow(self, label="{}".format(val),label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        _sizer.Add(box_sizer_rl, pos=(9, 0),span=(1, 5), flag=wx.EXPAND)


        box_sizer_rl_led = wx.BoxSizer(wx.HORIZONTAL)
        self.led_near_robot = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_rl_led.Add(self.led_near_robot, proportion=1,flag=wx.EXPAND)

        self.led_near_signboard = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_rl_led.Add(self.led_near_signboard, proportion=1, flag=wx.EXPAND)

        self.led_near_restroom = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_rl_led.Add(self.led_near_restroom, proportion=1, flag=wx.EXPAND)
        _sizer.Add(box_sizer_rl_led, pos=(10, 0), span=(1, 5), flag=wx.EXPAND)

        title_sd= BlockWindow(self, ID=-1, label="Social Distance", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        _sizer.Add(title_sd, pos=(11, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_sd = wx.BoxSizer(wx.HORIZONTAL)

        labels_sd = ["public_space", "social_space", "personal_space", "intimate_space"]
        for idx, val in enumerate(labels_sd):
            box_sizer_sd.Add(BlockWindow(self, label="{}".format(val),label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        _sizer.Add(box_sizer_sd, pos=(12, 0),span=(1, 5), flag=wx.EXPAND)


        box_sizer_sd_led = wx.BoxSizer(wx.HORIZONTAL)
        self.led_public_space = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_sd_led.Add(self.led_public_space, proportion=1,flag=wx.EXPAND)

        self.led_social_space = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_sd_led.Add(self.led_social_space, proportion=1, flag=wx.EXPAND)

        self.led_personal_space = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_sd_led.Add(self.led_personal_space, proportion=1, flag=wx.EXPAND)

        self.led_intimate_space = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_sd_led.Add(self.led_intimate_space, proportion=1, flag=wx.EXPAND)


        _sizer.Add(box_sizer_sd_led, pos=(13, 0), span=(1, 5), flag=wx.EXPAND)


        title_int= BlockWindow(self, ID=-1, label="isSpeaking", style=wx.ALL,label_color=wx.WHITE, bg_color='#696c70', font_set=[14,wx.DEFAULT,wx.NORMAL,wx.NORMAL])
        _sizer.Add(title_int, pos=(14, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_issp = wx.BoxSizer(wx.HORIZONTAL)

        labels_issp = ["Human", "Robot", "Reply to Robot"]
        for idx, val in enumerate(labels_issp):
            box_sizer_issp.Add(BlockWindow(self, label="{}".format(val),label_color=wx.BLACK, bg_color=wx.WHITE), proportion=1, flag=wx.EXPAND)

        _sizer.Add(box_sizer_issp, pos=(15, 0),span=(1, 5), flag=wx.EXPAND)


        box_sizer_issp = wx.BoxSizer(wx.HORIZONTAL)
        self.led_issp_human = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_issp.Add(self.led_issp_human, proportion=1,flag=wx.EXPAND)

        self.led_issp_robot = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_issp.Add(self.led_issp_robot, proportion=1, flag=wx.EXPAND)

        self.led_issp_reply = CircleWindow(self, ID=-1, color='#df0a4b')
        box_sizer_issp.Add(self.led_issp_reply, proportion=1, flag=wx.EXPAND)


        _sizer.Add(box_sizer_issp, pos=(16, 0), span=(1, 5), flag=wx.EXPAND)



        title_per = BlockWindow(self, ID=-1, label="User Personality", style=wx.ALL, label_color=wx.WHITE, bg_color='#696c70',
                                font_set=[14, wx.DEFAULT, wx.NORMAL, wx.NORMAL])
        _sizer.Add(title_per, pos=(17, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_per = wx.BoxSizer(wx.HORIZONTAL)

        labels_per = ["O", "C", "E", "A", "N"]
        for idx, val in enumerate(labels_per):
            box_sizer_per.Add(BlockWindow(self, label="{}".format(val), label_color=wx.BLACK, bg_color=wx.WHITE),
                               proportion=1, flag=wx.EXPAND)

        _sizer.Add(box_sizer_per, pos=(18, 0), span=(1, 5), flag=wx.EXPAND)

        box_sizer_per = wx.BoxSizer(wx.HORIZONTAL)
        self.gauge1 = wx.Gauge(self, range=3, size=(100, 50), style=wx.GA_VERTICAL)
        self.gauge1.SetValue(1)
        self.gauge1.SetBackgroundColour(wx.WHITE)
        box_sizer_per.Add(self.gauge1, proportion=1, flag=wx.EXPAND)

        self.gauge2 = wx.Gauge(self, range=3, size=(100, 50), style=wx.GA_VERTICAL)
        self.gauge2.SetValue(2)
        self.gauge2.SetBackgroundColour(wx.WHITE)
        box_sizer_per.Add(self.gauge2, proportion=1, flag=wx.EXPAND)

        self.gauge3 = wx.Gauge(self, range=3, size=(100, 50), style=wx.GA_VERTICAL)
        self.gauge3.SetValue(3)
        self.gauge3.SetBackgroundColour(wx.WHITE)

        box_sizer_per.Add(self.gauge3, proportion=1, flag=wx.EXPAND)

        self.gauge4 = wx.Gauge(self, range=3, size=(100, 50), style=wx.GA_VERTICAL)
        self.gauge4.SetValue(1)
        self.gauge4.SetBackgroundColour(wx.WHITE)
        box_sizer_per.Add(self.gauge4, proportion=1, flag=wx.EXPAND)

        self.gauge5 = wx.Gauge(self, range=3, size=(100, 50), style=wx.GA_VERTICAL)
        self.gauge5.SetValue(2)
        self.gauge5.SetBackgroundColour(wx.WHITE)
        box_sizer_per.Add(self.gauge5, proportion=1, flag=wx.EXPAND)


        _sizer.Add(box_sizer_per, pos=(19, 0), span=(1, 5), flag=wx.EXPAND)

        # self.led_ = CircleWindow(self, ID=-1, color='#df0a4b')
        # box_sizer_per.Add(self.led_issp_robot, proportion=1, flag=wx.EXPAND)
        #
        # self.led_issp_reply = CircleWindow(self, ID=-1, color='#df0a4b')
        # box_sizer_per.Add(self.led_issp_reply, proportion=1, flag=wx.EXPAND)
        #
        # _sizer.Add(box_sizer_issp, pos=(16, 0), span=(1, 5), flag=wx.EXPAND)


        # _sizer.AddGrowableRow(0)
        _sizer.AddGrowableCol(0)

        self.SetSizer(_sizer)
        self.Fit()


class DialogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.BLACK)


class TopPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.image_panel = ImagePanel(self)
        main_sizer.Add(self.image_panel, 1, wx.EXPAND)

        self.state_panel = StatePanel(self)
        main_sizer.Add(self.state_panel, 1, wx.EXPAND)

        self.dialog_panel = DialogPanel(self)
        main_sizer.Add(self.dialog_panel, 1, wx.EXPAND)

        # text = TextPanel(self)
        # main_sizer.Add(text, 1, wx.EXPAND)
        #
        # graphics = GraphicsPanel(self)
        # main_sizer.Add(graphics, 1, wx.EXPAND)


        self.SetSizer(main_sizer)

    def update(self, image):
        print("image socket")



        # CREATE
        # self.create_status_bar()
        # self.create_menu_bar()


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


class CircleWindow(wx.Panel):
    def __init__(self, parent, ID=-1, color=wx.GREEN, size=(100, 50)):
        wx.Panel.__init__(self, parent, id=ID, size=size)

        self.count = 0
        self.parent = parent
        # self.SetBackgroundColour('#000000')
        self.SetBackgroundColour('white')
        self.color = color
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBrush(wx.Brush(self.color))
        sz = self.GetClientSize()
        dc.DrawCircle(sz.width/2, sz.height/2, 10)

    def UpdateColor(self, color):
        self.color = color
        self.Refresh()



class BlockWindow(wx.Panel):
    # code on book "wxPython in action" Listing 11.1

    def __init__(self, parent, ID=-1, label="", pos=wx.DefaultPosition, size=(100, 25), style=wx.RAISED_BORDER, label_color=wx.BLACK, bg_color='', font_set=[]):
        wx.Panel.__init__(self, parent, ID, pos, size, style=style)

        self.label = label
        self.font_set = font_set
        self.SetBackgroundColour(bg_color)
        self.size = size
        self.SetMinSize(size)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.label_color = label_color


    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.SetTextForeground(self.label_color)
        if self.font_set == []:
            dc.SetFont(self.GetFont())
            w, h = dc.GetTextExtent(self.label)
            sz = self.GetClientSize()
        else:
            font = wx.Font(self.font_set[0],self.font_set[1],self.font_set[2],self.font_set[3])
            dc.SetFont(font)
            w, h = dc.GetTextExtent(self.label)
            sz = self.GetClientSize()

        dc.DrawText(self.label, (sz.width - w) / 2, (sz.height - h) / 2)

    def UpdateLabel(self, label):
        self.label = label
        self.Refresh()


def handle_image(image):
    # make sure we update in the UI thread
    # print(app.frame.top_panel.ros_image.update, image)

    wx.CallAfter(app.frame.top_panel.image_panel.ros_image.update, image)

    # wx.CallAfter(app.frame.top_panel.state_panel.bw_9.UpdateLabel, time.time())
    # wx.CallAfter(app.frame.top_panel.state_panel.bw_9.UpdateLabel(str(time.time())))
    # app.frame.top_panel.state_panel.bw_9.UpdateLabel(str(time.time()))

    if int(time.time()) % 2 == 0:
        wx.CallAfter(app.frame.top_panel.state_panel.led_attention.UpdateColor, '#df0a4b')
        wx.CallAfter(app.frame.top_panel.state_panel.pi_name.UpdateLabel, '홀수')

        # app.frame.top_panel.state_panel.led_attention.UpdateColor('#df0a4b')
        # app.frame.top_panel.state_panel.pi_name.UpdateLabel("홀수")
    else:
        wx.CallAfter(app.frame.top_panel.state_panel.led_attention.UpdateColor, '#2aaa67')
        wx.CallAfter(app.frame.top_panel.state_panel.pi_name.UpdateLabel, '짝수')
        # app.frame.top_panel.state_panel.led_attention.UpdateColor('#2aaa67')
        # app.frame.top_panel.state_panel.pi_name.UpdateLabel("짝수")


    # http://wiki.wxpython.org/LongRunningTasks

import threading

class ParameterGetter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # self.url = url

    def run(self):
        while True:

            sd_data = rospy.get_param("/perception/social_distance")
            # time.sleep
            time.sleep(1)
            # print(sd_data)
            try:
                if int(time.time()) % 2 == 0:
                    wx.CallAfter(app.frame.top_panel.state_panel.led_attention.UpdateColor, '#df0a4b')
                    wx.CallAfter(app.frame.top_panel.state_panel.pi_name.UpdateLabel, '홀수')
                    # app.frame.top_panel.state_panel.led_attention.UpdateColor('#df0a4b')
                    # app.frame.top_panel.state_panel.pi_name.UpdateLabel("홀수")
                else:
                    wx.CallAfter(app.frame.top_panel.state_panel.led_attention.UpdateColor, '#2aaa67')
                    wx.CallAfter(app.frame.top_panel.state_panel.pi_name.UpdateLabel, '짝수')
                    # app.frame.top_panel.state_panel.led_attention.UpdateColor('#2aaa67')
                    # app.frame.top_panel.state_panel.pi_name.UpdateLabel("짝수")
            except AttributeError as e:
                print(e)
                break


def callback_packet(topic):
    audio_stream = topic.data
    msg_sequence = topic.header.seq
    byte_str = make_byte_str(audio_stream)
    wav_raw = make_wav_raw(byte_str)  #Integer (-32768 to 32767)

    wx.CallAfter(app.frame.top_panel.image_panel.ros_voice.update, convert_db(wav_raw))


def convert_db(data):
    data_abs = np.abs(data)
    output = 20 * np.log10(data_abs)
    return output

def make_byte_str(int16Array):
    byte_str = "".join(map(chr, int16Array))
    return byte_str

def make_wav_raw(byte_str):
    # wav_raw = np.fromstring(byte_str, dtype=np.int16).astype(np.float64) / 32768
    wav_raw = np.fromstring(byte_str, dtype=np.int16)
    return wav_raw


# t = HtmlGetter('http://google.com')
# t.start()

#


# def main(argv):
#     app = ImageViewApp()
#     rospy.init_node('ImageView')
#     rospy.Subscriber('/camera/color/image_raw', Image, handle_image)

# RUN!
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app = wx.App()
    rospy.init_node('ImageView')
    rospy.Subscriber('/camera/color/image_raw', Image, handle_image)
    rospy.Subscriber("audio_stream", AudioData, callback_packet, queue_size=50)
    param_thread = ParameterGetter()
    param_thread.start()

    app.frame = MainWindow(None, -1, "DeepTask Perception Viewer")
    app.frame.Show()
    app.MainLoop()
