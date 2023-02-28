import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(500, 600))
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(15)
        panel.SetFont(font)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.txtCtrl = wx.ComboBox(panel)
        
        vbox.Add(self.txtCtrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        gbox = wx.GridSizer(5, 4, 5, 5)
        
        gbox.AddMany( [(wx.Button(panel, label='очистить'), wx.ID_ANY, wx.EXPAND),
                        (wx.StaticText(panel), wx.EXPAND),
                        (wx.StaticText(panel), wx.EXPAND),
                        (wx.Button(panel, label='выйти'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='7'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='8'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='9'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='/'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='4'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='5'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='6'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='*'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='1'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='2'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='3'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='-'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='0'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='.'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='ответ'), wx.ID_ANY, wx.EXPAND),
                        (wx.Button(panel, label='+'), wx.ID_ANY, wx.EXPAND)] )
        
        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.OnClicked)
    
    def OnClicked(self, evt):
        label = evt.GetEventObject().GetLabel()

        if label == 'ответ':
            compute = self.txtCtrl.GetValue()
            
            if not compute.strip():
                return
            
            result = eval(compute)
            self.txtCtrl.Insert(compute, 0)
            self.txtCtrl.SetValue(str(result))

        elif label == 'очистить':
            self.txtCtrl.SetValue("")
        
        elif label == 'выйти':
            frame.Destroy()

        else:
            self.txtCtrl.SetValue(self.txtCtrl.GetValue() + label)

app = wx.App()
frame = MyFrame(None, 'калькулятор')
frame.Show()
app.MainLoop()
