import wx #For graphics' interface
import os #For operating system compatibility

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



class TextPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.WHITE)

        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE) #Text area with multiline

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.control, 1, wx.EXPAND)
        self.SetSizer(sizer)

class GraphicsPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.BLACK)


class ImagePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.BLACK)
        _sizer = wx.BoxSizer(wx.VERTICAL)
        txt_image_voice = wx.StaticText(self, label='ROS Image Viewer', size=(640, 50))
        _sizer.Add(txt_image_voice, flag=wx.TOP | wx.ALIGN_RIGHT | wx.BOTTOM, border=5)

        self.ros_image = ImageViewPanel(self)
        _sizer.Add(self.ros_image, 1, wx.EXPAND)

        self.SetSizer(_sizer)



class StatePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour(wx.WHITE)
        _sizer = wx.GridBagSizer(5,5)

        # sizer = wx.GridBagSizer(hgap=5, vgap=-1)
        bw = BlockWindow(self, label="State 1")
        # txt_image_voice = wx.StaticText(self, label='state1', size=(50, 30))

        # _sizer.Add(bw, pos=(0,0), span=(3,1), flag=wx.EXPAND)
        for i in range(3):
            for j in range(5):
                _sizer.Add(BlockWindow(self, label="State {}-{}".format(i,j)), pos=(i, j), flag=wx.EXPAND)

        _sizer.Add(BlockWindow(self, label="State {}-{}".format(4,0)), pos=(4, 0), span=(1,5), flag=wx.EXPAND)

        self.bw_9 = BlockWindow(self, ID=wx.ID_ANY, label="State {}-{}".format(9,0))


        _sizer.Add(self.bw_9, pos=(9, 0),span=(1,5),  flag=wx.EXPAND)

        # _sizer.Add(BlockWindow(self, label="State 1-1"), pos=(1,1), flag=wx.EXPAND)

        self.SetSizer(_sizer)



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



class MainWindow(wx.Frame):
    def __init__(self, parent, id, title):

        #SETUP
        wx.Frame.__init__(self, parent, wx.ID_ANY, title = "MyTitle", size = (1800,500))
        self.dirname=''

        self.top_panel = TopPanel(self)

        #CREATE
        # self.create_status_bar()
        # self.create_menu_bar()


# FUNCTIONS
# ------------------------------------------------------------------------------
    def create_status_bar(self):
        self.CreateStatusBar() #A Statusbar at the bottom of the window


    def create_menu_bar(self):

    # File Menu
        filemenu= wx.Menu()

        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open file to edit")
        filemenu.AppendSeparator()
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save the file")
        menuSaveAs = filemenu.Append(wx.ID_SAVEAS, "Save &As", "Save the file with a new name")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate communication and close window")

    #The Menu Bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") #Adding the "File" menu to the 'menuBar'
        self.SetMenuBar(menuBar)  #Adding the 'menuBar' to the Frame content

    #Event binding
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, menuSaveAs)

# EVENTS
# ------------------------------------------------------------------------------
    def OnExit(self, event):
        self.Close(True) #Close the frame


    def OnOpen(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)

        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.panelA.control.SetValue(f.read())
            f.close()
        dlg.Destroy()


    def OnSave(self, event):
        f = open(os.path.join(self.dirname, self.filename), 'w')
        f.write(self.panelA.control.GetValue())
        f.close()


    def OnSaveAs(self, event):
        file_choices = "TXT (*.txt)|*.txt"
        dlg = wx.FileDialog(self, message = "Save file as...", defaultDir = os.getcwd(), defaultFile = self.filename, wildcard = file_choices, style = wx.SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            f = open(os.path.join(dlg.GetDirectory(), dlg.GetFilename()), 'w')
            f.write(self.panelA.control.GetValue())
            f.close()


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


class BlockWindow(wx.Panel):
    # code on book "wxPython in action" Listing 11.1
    def __init__(self, parent, ID=-1, label="",
                 pos = wx.DefaultPosition, size = (100, 25)):
        wx.Panel.__init__(self, parent, ID, pos, size,
                          wx.RAISED_BORDER, label)
        self.label = label

        self.SetMinSize(size)
        # self.SetBackgroundColour('black')
        # self.SetForegroundColour('black')
        self.Bind(wx.EVT_PAINT, self.OnPaint)
    def OnPaint(self, evt):
        sz = self.GetClientSize()
        dc = wx.PaintDC(self)
        w,h = dc.GetTextExtent(self.label)
        dc.SetFont(self.GetFont())

        dc.DrawText(self.label, (sz.width-w)/2, (sz.height-h)/2)
        dc.DrawText(self.label, )

    def UpdateLabel(self, label):
        self.label = label
        self.Refresh()

def handle_image(image):
    # make sure we update in the UI thread
    # print(app.frame.top_panel.ros_image.update, image)

    wx.CallAfter(app.frame.top_panel.image_panel.ros_image.update, image)
    import time

    # wx.CallAfter(app.frame.top_panel.state_panel.bw_9.UpdateLabel, time.time())
    # wx.CallAfter(app.frame.top_panel.state_panel.bw_9.UpdateLabel(str(time.time())))
    app.frame.top_panel.state_panel.bw_9.UpdateLabel(str(time.time()))


    # http://wiki.wxpython.org/LongRunningTasks

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

    app.frame = MainWindow(None, wx.ID_ANY, "tSock - Adaptation Technologies")
    app.frame.Show()
    app.MainLoop()