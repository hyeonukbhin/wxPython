# -*- coding: utf-8 -*-

import wx.media
import time
import roslib
import rospy
import threading
import wx
import numpy as np

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')



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
        radius = int(min([sz.width, sz.height]) * 0.4)
        # print(radius)
        dc.DrawCircle(sz.width / 2, sz.height / 2, radius)

    def UpdateColor(self, color):
        self.color = color
        self.Refresh()


class BlockWindow(wx.Panel):
    # code on book "wxPython in action" Listing 11.1
    def __init__(self, parent, ID=-1, label="", pos=wx.DefaultPosition, size=(100, 35), style=wx.RAISED_BORDER,
                 label_color=wx.BLACK, bg_color='', font_set=[]):
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
            font = wx.Font(self.font_set[0], self.font_set[1], self.font_set[2], self.font_set[3])
            dc.SetFont(font)
            w, h = dc.GetTextExtent(self.label)
            sz = self.GetClientSize()

        dc.DrawText(self.label, (sz.width - w) / 2, (sz.height - h) / 2)

    def UpdateLabel(self, label):
        self.label = label
        self.Refresh()



def convert_db(data):
    np.seterr(divide='ignore')
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


def get_param(param_name="state1"):
    try:
        output_values = rospy.get_param(param_name)
    except KeyError as e:
        output_values = ""
        # print(colored("KeyError : {}".format(e), 'red'))
    if output_values == "None" or None:
        output_values = ""
    return output_values