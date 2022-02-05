# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class fraMain
###########################################################################

class fraMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Winnipeg Weather Processor", pos = wx.DefaultPosition, size = wx.Size( 547,418 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 547,418 ), wx.Size( 547,418 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 54, 54, 54 ) )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Winnipeg Weather Processor", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 23, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_staticText30.SetForegroundColour( wx.Colour( 104, 130, 158 ) )
		self.m_staticText30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizer25.Add( self.m_staticText30, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Daily Avg Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText32.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer14.Add( self.m_staticText32, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.lbl_Daily_Month = wx.StaticText( self, wx.ID_ANY, u"Month (MM):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Daily_Month.Wrap( -1 )

		self.lbl_Daily_Month.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer30.Add( self.lbl_Daily_Month, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.lbl_Daily_Year = wx.StaticText( self, wx.ID_ANY, u"Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Daily_Year.Wrap( -1 )

		self.lbl_Daily_Year.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer30.Add( self.lbl_Daily_Year, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		gSizer16.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer31.SetMinSize( wx.Size( -1,111 ) )
		self.txt_Daily_Month_Input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Daily_Month_Input.SetMaxLength( 2 )
		self.txt_Daily_Month_Input.SetMinSize( wx.Size( 75,20 ) )

		bSizer31.Add( self.txt_Daily_Month_Input, 0, wx.ALL, 5 )

		self.txt_Daily_Year_Input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Daily_Year_Input.SetMaxLength( 4 )
		self.txt_Daily_Year_Input.SetMinSize( wx.Size( 75,20 ) )

		bSizer31.Add( self.txt_Daily_Year_Input, 0, wx.ALL, 5 )

		self.btn_Plot_Daily = wx.Button( self, wx.ID_ANY, u"Plot Daily", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.btn_Plot_Daily, 0, wx.ALL, 5 )


		gSizer16.Add( bSizer31, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		bSizer29.Add( gSizer16, 1, wx.EXPAND, 5 )


		gSizer14.Add( bSizer29, 1, wx.EXPAND, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Monthly Avg Temps", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( 16, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.m_staticText35.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer14.Add( self.m_staticText35, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.lbl_Monthly_Start_Year = wx.StaticText( self, wx.ID_ANY, u"Start Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Monthly_Start_Year.Wrap( -1 )

		self.lbl_Monthly_Start_Year.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32.Add( self.lbl_Monthly_Start_Year, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.lbl_Monthly_End_Year = wx.StaticText( self, wx.ID_ANY, u"End Year (YYYY):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_Monthly_End_Year.Wrap( -1 )

		self.lbl_Monthly_End_Year.SetForegroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer32.Add( self.lbl_Monthly_End_Year, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		gSizer17.Add( bSizer32, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		bSizer33.SetMinSize( wx.Size( -1,111 ) )
		self.txt_Monthly_Start_Year_Input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Monthly_Start_Year_Input.SetMaxLength( 4 )
		self.txt_Monthly_Start_Year_Input.SetMinSize( wx.Size( 75,20 ) )

		bSizer33.Add( self.txt_Monthly_Start_Year_Input, 0, wx.ALL, 5 )

		self.txt_Monthly_Start_End_Input = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_Monthly_Start_End_Input.SetMaxLength( 4 )
		self.txt_Monthly_Start_End_Input.SetMinSize( wx.Size( 75,20 ) )

		bSizer33.Add( self.txt_Monthly_Start_End_Input, 0, wx.ALL, 5 )

		self.btn_Plot_Monthly = wx.Button( self, wx.ID_ANY, u"Plot Monthly", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.btn_Plot_Monthly, 0, wx.ALL, 5 )


		gSizer17.Add( bSizer33, 1, wx.ALIGN_BOTTOM|wx.EXPAND, 5 )


		bSizer34.Add( gSizer17, 1, wx.EXPAND, 5 )


		gSizer14.Add( bSizer34, 1, wx.EXPAND, 5 )


		bSizer25.Add( gSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()
		self.m_menubar4 = wx.MenuBar( 0 )
		self.mnu_File = wx.Menu()
		self.mnu_File_Download = wx.Menu()
		self.mnu_File_Download_Update = wx.MenuItem( self.mnu_File_Download, wx.ID_ANY, u"Update Existing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_File_Download.Append( self.mnu_File_Download_Update )

		self.mnu_File_Download_Full = wx.MenuItem( self.mnu_File_Download, wx.ID_ANY, u"Full Download", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_File_Download.Append( self.mnu_File_Download_Full )

		self.mnu_File.AppendSubMenu( self.mnu_File_Download, u"Download Data" )

		self.mnu_File_Exit = wx.MenuItem( self.mnu_File, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_File.Append( self.mnu_File_Exit )

		self.m_menubar4.Append( self.mnu_File, u"File" )

		self.mnu_Help = wx.Menu()
		self.mnu_Help_About = wx.MenuItem( self.mnu_Help, wx.ID_ANY, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mnu_Help.Append( self.mnu_Help_About )

		self.m_menubar4.Append( self.mnu_Help, u"Help" )

		self.SetMenuBar( self.m_menubar4 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_Plot_Daily.Bind( wx.EVT_BUTTON, self.Btn_Plot_Daily_OnClick_Event )
		self.btn_Plot_Monthly.Bind( wx.EVT_BUTTON, self.Btn_Plot_Monthly_OnClick_Event )
		self.Bind( wx.EVT_MENU, self.mnu_File_Download_Update_OnClick_Event, id = self.mnu_File_Download_Update.GetId() )
		self.Bind( wx.EVT_MENU, self.mnu_File_Download_Full_OnClick_Event, id = self.mnu_File_Download_Full.GetId() )
		self.Bind( wx.EVT_MENU, self.mnu_File_Exit_OnClick_Event, id = self.mnu_File_Exit.GetId() )
		self.Bind( wx.EVT_MENU, self.mnu_Help_About_OnClick_Event, id = self.mnu_Help_About.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Btn_Plot_Daily_OnClick_Event( self, event ):
		event.Skip()

	def Btn_Plot_Monthly_OnClick_Event( self, event ):
		event.Skip()

	def mnu_File_Download_Update_OnClick_Event( self, event ):
		event.Skip()

	def mnu_File_Download_Full_OnClick_Event( self, event ):
		event.Skip()

	def mnu_File_Exit_OnClick_Event( self, event ):
		event.Skip()

	def mnu_Help_About_OnClick_Event( self, event ):
		event.Skip()


###########################################################################
## Class fraAbout
###########################################################################

class fraAbout ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 363,247 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 363,247 ), wx.Size( 363,247 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer8.Add( self.m_staticText22, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Winnipeg Weather Processor Application", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer8.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Version 1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer8.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Copyright © 2021", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer8.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Developed By: Derrick Phang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer8.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer8.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.btn_Close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_Close, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_Close.Bind( wx.EVT_BUTTON, self.btn_Close_OnClick_Event )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_Close_OnClick_Event( self, event ):
		event.Skip()


