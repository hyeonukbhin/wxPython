import wx
import wx.media
import rospy

import roslib

roslib.load_manifest('rospy')
roslib.load_manifest('sensor_msgs')
import rospy
from sensor_msgs.msg import Image

import wx
import sys


# class ImageViewApp(wx.App):
#     def OnInit(self):
#         self.frame = wx.Frame(None, title = "ROS Image View", size = (256, 256))
#         self.panel = ImageViewPanel(self.frame)
#         self.frame.Show(True)

class Example(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 500))

        self.initui()
        self.Show()

    def initui(self):
        self.panel_default = wx.Panel(self)
        main_horigontal_sizer = wx.BoxSizer(wx.HORIZONTAL)
        image_voice_sizer = wx.BoxSizer(wx.VERTICAL)
        txt_image_voice = wx.StaticText(self.panel_default, label='ROS Image Viewer', size=(500, 100))

        image_voice_sizer.Add(txt_image_voice, flag=wx.TOP | wx.ALIGN_RIGHT | wx.BOTTOM, border=5)
        button_ok = wx.Button(self.panel_default, label='OK', size=(90, 28))
        button_close = wx.Button(self.panel_default, label='Close', size=(90, 28))

        image_voice_sizer.Add(button_ok)
        image_voice_sizer.Add(button_close, flag=wx.RIGHT | wx.BOTTOM, border=5)

        img = wx.EmptyImage(240, 240)
        imageCtrl = wx.StaticBitmap(self.panel_default, id = wx.ID_ANY, wx.BitmapFromImage(img))
        image_voice_sizer.Add(imageCtrl, 0, wx.ALL, 5)

        # self.frame = wx.Frame(None, title = "ROS Image View", size = (256, 256))
        self.panel_ros = ImageViewPanel(self)

        main_horigontal_sizer.Add(self.panel_ros, 1, wx.EXPAND)

        # perception_sizer = wx.GridBagSizer(4, 4)
        # txt_dashboard = wx.StaticText(panel, label='ROS State Dashboard', size=(500, 100))
        # perception_sizer.Add(txt_image_voice, pos=(0, 0))
        #
        # txt_image_voice_1 = wx.StaticText(panel, label='Status 1-1')
        # txt_image_voice_2 = wx.StaticText(panel, label='Status 1-2')
        # # txt_image_voice_3 = wx.StaticText(panel, label='Status 2-1')
        # # txt_image_voice_4 = wx.StaticText(panel, label='Status 2-2')
        # # txt_image_voice_5 = wx.StaticText(panel, label='Status 3-1')
        # # txt_image_voice_6 = wx.StaticText(panel, label='Status 3-2')
        # perception_sizer.Add(txt_image_voice_1, pos=(1, 0))
        # perception_sizer.Add(txt_image_voice_2, pos=(1, 1))
        # # perception_sizer.Add(txt_image_voice_3, pos=(2, 0))
        # # perception_sizer.Add(txt_image_voice_4, pos=(2, 1))
        # # perception_sizer.Add(txt_image_voice_5, pos=(3, 0))
        # # perception_sizer.Add(txt_image_voice_6, pos=(3, 1))
        #
        # # perception_sizer.AddMany([txt_image_voice_1,txt_image_voice_2,txt_image_voice_3,txt_image_voice_4,txt_image_voice_5,txt_image_voice_6])
        # # perception_sizer.AddGrowableCol(1)
        # # perception_sizer.AddGrowableRow(2)
        #
        # main_horigontal_sizer.Add(image_voice_sizer, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        # main_horigontal_sizer.Add(perception_sizer, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        # # verticalbox.Add(self.display, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=4)
        #
        # # sizer = wx.GridBagSizer(hgap=5, vgap=-1)
        #
        # # sizer.Add(txt_rename, pos=(0, 0), flag=wx.TOP | wx.ALIGN_RIGHT | wx.BOTTOM, border=5)
        #
        # # txtctrl = wx.TextCtrl(panel)
        # # sizer.Add(txtctrl, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        # #
        # # button_ok = wx.Button(panel, label='OK', size=(90, 28))
        # # button_close = wx.Button(panel, label='Close', size=(90, 28))
        # # sizer.Add(button_ok, pos=(3, 3))
        # # sizer.Add(button_close, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)
        #
        # # sizer.AddGrowableCol(1)
        # # sizer.AddGrowableRow(2)

        self.SetSizer(main_horigontal_sizer)

    def update11(self, image):
        print(type(image))


class ImageViewPanel(wx.Panel):
    """ class ImageViewPanel creates a panel with an image on it, inherits wx.Panel """

    def update(self, image):
        # http://www.ros.org/doc/api/sensor_msgs/html/msg/Image.html
        if not hasattr(self, 'staticbmp'):
            self.staticbmp = wx.StaticBitmap(self)
            frame = self.GetParent()
            frame.SetSize((image.width, image.height))
        if image.encoding == 'rgba8':
            bmp = wx.BitmapFromBufferRGBA(image.width, image.height, image.data)
            self.staticbmp.SetBitmap(bmp)
        elif image.encoding == 'rgb8':
            bmp = wx.BitmapFromBuffer(image.width, image.height, image.data)
            self.staticbmp.SetBitmap(bmp)


# class ImageViewApp(wx.App):
#     def OnInit(self):
#         self.frame = wx.Frame(None, title = "ROS Image View", size = (256, 256))
#         self.panel = ImageViewPanel(self.frame)
#         self.frame.Show(True)
#
#         return True

def handle_image(image):
    # make sure we update in the UI thread
    # print(wx.update11, image)
    print(Frame.update11(image))
    # wx.CallAfter(wx.GetApp().panel.update, image)
    # http://wiki.wxpython.org/LongRunningTasks


if __name__ == '__main__':
    # app = wx.App()
    # Example(None, title='Rename')
    # app.MainLoop()
    app = wx.App()
    # app = ImageViewApp()

    Frame = Example(None, title='Rename')
    # Frame.Show()

    rospy.init_node('ImageView')
    rospy.Subscriber('/camera/color/image_raw', Image, handle_image)
    app.MainLoop()
