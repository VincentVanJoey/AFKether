# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"AFKether"), pos = wx.DefaultPosition, size = wx.Size( 336,241 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        frame_sizer = wx.BoxSizer( wx.VERTICAL )

        self.frame_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.frame_notebook.SetFont( wx.Font( 7, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Small Fonts" ) )
        self.frame_notebook.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.main_panel = wx.Panel( self.frame_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.main_panel.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Small Fonts" ) )
        self.main_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
        self.main_panel.SetBackgroundColour( wx.Colour( 116, 80, 135 ) )

        main_sizer = wx.BoxSizer( wx.VERTICAL )

        self.title = wx.StaticText( self.main_panel, wx.ID_ANY, _(u"Rivals of AFKether"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.title.SetLabelMarkup( _(u"Rivals of AFKether") )
        self.title.Wrap( -1 )

        self.title.SetFont( wx.Font( 14, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Terminal" ) )
        self.title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        main_sizer.Add( self.title, 0, wx.ALL|wx.EXPAND, 15 )

        minute_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.minute_label = wx.StaticText( self.main_panel, wx.ID_ANY, _(u"Match Length:\n(minutes)"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.minute_label.SetLabelMarkup( _(u"Match Length:\n(minutes)") )
        self.minute_label.Wrap( -1 )

        self.minute_label.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )
        self.minute_label.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        minute_sizer.Add( self.minute_label, 2, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.minute_spin = wx.SpinCtrl( self.main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.SP_ARROW_KEYS, 0, 10, 4 )
        self.minute_spin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

        minute_sizer.Add( self.minute_spin, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


        main_sizer.Add( minute_sizer, 1, wx.ALIGN_CENTER, 5 )

        self.toggle_btn = wx.ToggleButton( self.main_panel, wx.ID_ANY, _(u"Start Loop"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.toggle_btn.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Fixedsys" ) )

        main_sizer.Add( self.toggle_btn, 1, wx.ALIGN_CENTER|wx.ALL, 10 )


        self.main_panel.SetSizer( main_sizer )
        self.main_panel.Layout()
        main_sizer.Fit( self.main_panel )
        self.frame_notebook.AddPage( self.main_panel, _(u"AFKether"), True )
        self.calc_panel = wx.Panel( self.frame_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.calc_panel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        self.calc_panel.SetBackgroundColour( wx.Colour( 116, 80, 135 ) )

        calc_sizer = wx.BoxSizer( wx.VERTICAL )

        calc_choice_sizer = wx.FlexGridSizer( 2, 3, 0, 0 )
        calc_choice_sizer.SetFlexibleDirection( wx.VERTICAL )
        calc_choice_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_NONE )

        self.item_type_label = wx.StaticText( self.calc_panel, wx.ID_ANY, _(u"Item Type:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.item_type_label.Wrap( -1 )

        self.item_type_label.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        calc_choice_sizer.Add( self.item_type_label, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        self.rarity_type_label = wx.StaticText( self.calc_panel, wx.ID_ANY, _(u"Rarity:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rarity_type_label.Wrap( -1 )

        self.rarity_type_label.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        calc_choice_sizer.Add( self.rarity_type_label, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.item_count_label = wx.StaticText( self.calc_panel, wx.ID_ANY, _(u"#:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.item_count_label.Wrap( -1 )

        self.item_count_label.SetFont( wx.Font( 9, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        calc_choice_sizer.Add( self.item_count_label, 2, wx.ALIGN_CENTER|wx.ALL, 5 )

        item_type_choiceChoices = [ wx.EmptyString, _(u"Icon"), _(u"Emote"), _(u"Pallet"), _(u"Skin"), _(u"Respawn Platform"), _(u"Death Effect"), _(u"Taunt") ]
        self.item_type_choice = wx.Choice( self.calc_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, item_type_choiceChoices, 0 )
        self.item_type_choice.SetSelection( 0 )
        calc_choice_sizer.Add( self.item_type_choice, 0, wx.ALL, 5 )

        rarity_type_choiceChoices = [ wx.EmptyString, _(u"Common"), _(u"Rare"), _(u"Epic") ]
        self.rarity_type_choice = wx.Choice( self.calc_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rarity_type_choiceChoices, 0 )
        self.rarity_type_choice.SetSelection( 0 )
        calc_choice_sizer.Add( self.rarity_type_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.item_count_spin = wx.SpinCtrl( self.calc_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 999, 0 )
        self.item_count_spin.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )
        self.item_count_spin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

        calc_choice_sizer.Add( self.item_count_spin, 0, wx.ALIGN_CENTER, 0 )


        calc_sizer.Add( calc_choice_sizer, 1, wx.ALL|wx.EXPAND, 5 )

        calc_op_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.calc_add_btn = wx.Button( self.calc_panel, wx.ID_ANY, _(u"Add Item(s)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        calc_op_sizer.Add( self.calc_add_btn, 0, wx.ALL, 5 )

        self.calc_undo_btn = wx.Button( self.calc_panel, wx.ID_ANY, _(u"Undo"), wx.DefaultPosition, wx.DefaultSize, 0 )
        calc_op_sizer.Add( self.calc_undo_btn, 0, wx.ALL, 5 )

        self.calc_clear_btn = wx.Button( self.calc_panel, wx.ID_ANY, _(u"Clear"), wx.DefaultPosition, wx.DefaultSize, 0 )
        calc_op_sizer.Add( self.calc_clear_btn, 0, wx.ALL, 5 )


        calc_sizer.Add( calc_op_sizer, 1, wx.ALIGN_CENTER, 5 )

        self.total_amount = wx.TextCtrl( self.calc_panel, wx.ID_ANY, _(u"Total Coins: 0\nTotal Bucks: 0\nUSD: 0"), wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_MULTILINE|wx.TE_READONLY )
        self.total_amount.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )
        self.total_amount.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
        self.total_amount.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

        calc_sizer.Add( self.total_amount, 2, wx.ALL|wx.EXPAND, 10 )


        self.calc_panel.SetSizer( calc_sizer )
        self.calc_panel.Layout()
        calc_sizer.Fit( self.calc_panel )
        self.frame_notebook.AddPage( self.calc_panel, _(u"Calculator"), False )
        self.help_panel = wx.Panel( self.frame_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.help_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        help_body_sizer = wx.BoxSizer( wx.VERTICAL )

        hyperlink_sizer = wx.BoxSizer( wx.VERTICAL )

        self.github_link = wx.adv.HyperlinkCtrl( self.help_panel, wx.ID_ANY, _(u"AFKether Github"), u"https://github.com/VincentVanJoey/AFKether", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.github_link.SetHoverColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.github_link.SetNormalColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.github_link.SetVisitedColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.github_link.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        hyperlink_sizer.Add( self.github_link, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.dragdown_link = wx.adv.HyperlinkCtrl( self.help_panel, wx.ID_ANY, _(u"Dragdown Wiki"), u"https://dragdown.wiki/wiki/Main_Page", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_CONTEXTMENU )
        self.dragdown_link.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        hyperlink_sizer.Add( self.dragdown_link, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.nolt_link = wx.adv.HyperlinkCtrl( self.help_panel, wx.ID_ANY, _(u"ROA2 Nolt Board"), u"http://rivals2.com/nolt", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_CONTEXTMENU )
        self.nolt_link.SetFont( wx.Font( 12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Terminal" ) )

        hyperlink_sizer.Add( self.nolt_link, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        help_body_sizer.Add( hyperlink_sizer, 1, wx.ALIGN_CENTER|wx.ALL, 15 )

        config_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.open_config_btn = wx.Button( self.help_panel, wx.ID_ANY, _(u"Open Config File"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.open_config_btn.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Fixedsys" ) )
        self.open_config_btn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
        self.open_config_btn.SetBackgroundColour( wx.Colour( 116, 80, 135 ) )

        config_sizer.Add( self.open_config_btn, 1, wx.ALL, 5 )

        self.m_colourPicker4 = wx.ColourPickerCtrl( self.help_panel, wx.ID_ANY, wx.Colour( 116, 80, 135 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL )
        config_sizer.Add( self.m_colourPicker4, 0, wx.ALL, 5 )


        help_body_sizer.Add( config_sizer, 1, wx.ALIGN_CENTER, 5 )


        self.help_panel.SetSizer( help_body_sizer )
        self.help_panel.Layout()
        help_body_sizer.Fit( self.help_panel )
        self.frame_notebook.AddPage( self.help_panel, _(u"Help/Info"), False )

        frame_sizer.Add( self.frame_notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( frame_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.toggle_btn.Bind( wx.EVT_TOGGLEBUTTON, self.on_toggle_press )
        self.calc_add_btn.Bind( wx.EVT_BUTTON, self.calc_add_item )
        self.calc_undo_btn.Bind( wx.EVT_BUTTON, self.calc_undo_item )
        self.calc_clear_btn.Bind( wx.EVT_BUTTON, self.calc_clear_item )
        self.open_config_btn.Bind( wx.EVT_BUTTON, self.help_open_config )
        self.m_colourPicker4.Bind( wx.EVT_COLOURPICKER_CHANGED, self.help_theme_color_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def on_toggle_press( self, event ):
        event.Skip()

    def calc_add_item( self, event ):
        event.Skip()

    def calc_undo_item( self, event ):
        event.Skip()

    def calc_clear_item( self, event ):
        event.Skip()

    def help_open_config( self, event ):
        event.Skip()

    def help_theme_color_change( self, event ):
        event.Skip()


