#!/usr/bin/python2.7
# -*- coding: utf-8 -*-




import wx.media
import time
import roslib
from sensor_msgs.msg import Image
import rospy
from audio_msgs.msg import AudioData, FeatureData
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import threading
import wx
import etc_functions as ef

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# class DialogPanel(wx.Panel):
#     def __init__(self, parent):
#         wx.Panel.__init__(self, parent)
#         self.SetBackgroundColour(wx.BLACK)


roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')

VOICE_SCALE = "linear" # or "db"

CUSTOM_COLOR_RED = '#df0a4b'
CUSTOM_COLOR_GREEN = '#2aaa67'
CUSTOM_COLOR_DARK_GRAY = '#363b41'
CUSTOM_COLOR_LIGHT_GRAY = '#696c70'
CUSTOM_COLOR_VERY_LIGHT_GRAY = '#f0f0f0'
CUSTOM_COLOR_BLUE = '#385cf4'



class DialogPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # self.SetBackgroundColour(wx.NullColour)
        self.SetBackgroundColour(wx.WHITE)
        main_sizer = wx.GridBagSizer(hgap=5, vgap=-1)

        title_panel = ef.BlockWindow(self, ID=-1, label="Dialog", size=(630, 50), style=wx.ALL, label_color=wx.WHITE, bg_color=CUSTOM_COLOR_DARK_GRAY, font_set=[18, wx.NORMAL, wx.NORMAL, wx.BOLD])

        main_sizer.Add(title_panel, pos=(0, 0), span=(1, 5), flag=wx.EXPAND)

        t1_text = ""
        # t1 = wx.TextCtrl(self, -1, t1_text, style=wx.TE_MULTILINE | wx.HSCROLL | wx.ALIGN_RIGHT)
        # self.dialog_window = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.HSCROLL | wx.ALIGN_CENTER_HORIZONTAL, size=(430, 950))
        # self.dialog_window.SetFont(wx.Font(18, wx.NORMAL, wx.NORMAL, wx.BOLD))
        # main_sizer.Add(self.dialog_window, pos=(1, 1), span=(10, 3), flag=wx.EXPAND)


        self.dialog_window = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.HSCROLL | wx.ALIGN_CENTER_HORIZONTAL, size=(430, 950))
        self.dialog_window.SetFont(wx.Font(16, wx.NORMAL, wx.NORMAL, wx.BOLD))
        # self.dialog_window.AppendText("안뇽")

        main_sizer.Add(self.dialog_window, pos=(1, 1), span=(7, 3), flag=wx.EXPAND)

        # sizer_image = wx.BoxSizer(wx.HORIZONTAL)
        bmp_human = wx.BitmapFromImage(wx.Image("Human.png", wx.BITMAP_TYPE_ANY))
        bmp_robot = wx.BitmapFromImage(wx.Image("Robot.png", wx.BITMAP_TYPE_ANY))
        bmp_human = scale_bitmap(bmp_human, 100, 100)
        bmp_robot = scale_bitmap(bmp_robot, 100, 100)

        bmp_human = wx.StaticBitmap(self, -1, bmp_human, size=(100,100))
        bmp_robot = wx.StaticBitmap(self, -1, bmp_robot, size=(100,100))
        # sizer_image.Add(bmp_human, proportion=1, flag=wx.EXPAND)
        # sizer_image.Add(bmp_robot, proportion=1, flag=wx.EXPAND)
        main_sizer.Add(bmp_human, pos=(4, 0), flag=wx.EXPAND)
        main_sizer.Add(bmp_robot, pos=(4, 4), flag=wx.EXPAND)


        main_sizer.AddGrowableCol(0)

        self.SetSizer(main_sizer)
        self.Fit()

    def AppendData(self, data):
        self.dialog_window.AppendText("{}\n".format(data))

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        # SETUP
        wx.Frame.__init__(self, parent, id, title=title, size=(650, 1000))
        self.top_panel = TopPanel(self)


class TopPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        _sizer = wx.BoxSizer(wx.HORIZONTAL)
        # voice_scale = "linear"

        self.dialog_panel = DialogPanel(self)
        _sizer.Add(self.dialog_panel, proportion=1, flag=wx.EXPAND)

        self.SetSizer(_sizer)

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

def main():
    app = wx.App()
    frame = MainFrame(None, -1, "DeepTask GUI")


    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
