################################################################################
## 初始化
################################################################################

init offset = -1
################################################################################
## 样式
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)


style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内屏幕
################################################################################


## Say 屏幕 ######################################################################
##
## Say 屏幕用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此屏幕必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    imagebutton:
        xpos 0.94
        ypos 0.895
        idle "gui/button/quick_quit_idle_background.png"
        hover "gui/button/quick_quit_hover_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        action MainMenu(True)


    imagebutton:
        hover "gui/button/quick_skip_hover_background.png"
        idle "gui/button/quick_skip_idle_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        xpos 826
        ypos 520
        action Skip() alternate Skip(fast=True, confirm=True)

    imagebutton:
         hover "gui/button/quick_history_hover_background.png"
         idle "gui/button/quick_history_idle_background.png"
         hover_sound "audio/button/hover.wav"
         activate_sound "audio/button/selected.wav"
         xpos 881
         ypos 518
         action ShowMenu('history')

    imagebutton:
        hover "gui/button/quick_hide_hover_background.png"
        idle "gui/button/quick_hide_idle_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        xpos 939
        ypos 518
        action HideInterface()

    imagebutton:
        hover "gui/button/quick_save_hover_background.png"
        idle "gui/button/quick_save_idle_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        xpos 1000
        ypos 516
        action ShowMenu('save')

    imagebutton:
        hover "gui/button/quick_preferences_hover_background.png"
        idle "gui/button/quick_preferences_idle_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        xpos 1055
        ypos 518
        action ShowMenu('preferences')

    ## 如果有侧边图像，会将其显示在文本之上。请不要在手机界面下显示这个，因为没
    ## 有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## 输入屏幕 ########################################################################
##
## 此屏幕用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此屏幕必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择屏幕 ########################################################################
##
## 此屏幕用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## 若为True，菜单内的叙述会使用旁白 (narrator) 角色。否则，叙述会显示为菜单内的
## 文字说明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## 快捷菜单屏幕 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():

    # 确保该菜单出现在其他屏幕之上，
    zorder 100

    # if quick_menu:
    #     imagebutton:
    #         xpos 0.94
    #         ypos 0.895
    #         idle "gui/button/quick_quit_idle_background.png"
    #         hover "gui/button/quick_quit_hover_background.png"
    #         hover_sound "audio/button/hover.wav"
    #         activate_sound "audio/button/selected.wav"
    #         action MainMenu(True)


## 此代码确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”屏幕。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## 标题和游戏菜单屏幕
################################################################################

## 导航屏幕 ########################################################################
##
## 该屏幕包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("New Game") action Start()

        else:

#            textbutton _("History") action ShowMenu("history")

            textbutton _("Save Game") action ShowMenu("save")

        textbutton _("Load Game") action ShowMenu("load")

        textbutton _("Gallery") action ShowMenu("gallery")

        textbutton _("Music Room") action ShowMenu("music_room")

        textbutton _("Settings") action ShowMenu("preferences")
#        if _in_replay:
#
#            textbutton _("结束回放") action EndReplay(confirm=True)

#        elif not main_menu:

#            textbutton _("标题界面") action MainMenu()

        #textbutton _("About") action ShowMenu("about")

        #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## “帮助”对移动设备来说并非必须或相关。
            #textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Exit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单屏幕 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## 此代码可确保替换掉任何其他菜单屏幕。
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    add "gui/logo2.png"

    ## 此空框可使标题菜单变暗。
    frame:
        pass

    ## “use”语句将其他的屏幕包含进此屏幕。标题屏幕的实际内容在导航屏幕中。
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 258
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## 游戏菜单屏幕 ######################################################################
##
## 此屏幕列出了游戏菜单的基本共同结构。此屏幕需使用屏幕标题（title）调用，并显示
## 背景、标题和导航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此屏幕与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, icon=None, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    hbox:
        label title
        null width 80
        if icon:
            add icon yoffset 20

    imagebutton:
        xpos 0.94
        ypos 0.895
        idle "gui/button/quick_quit_idle_background.png"
        hover "gui/button/quick_quit_hover_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## 关于屏幕 ########################################################################
##
## 此屏幕提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 这个屏幕没有什么特别之处，因此它也是如何制作自定义屏幕的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”屏幕到此处。子级“vbox”将包含在“game_menu”屏幕
    ## 的“viewport”内。
    use game_menu(_("ABOUT"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("Based on {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## 此变量在 options.rpy 中重新定义，来添加文本到关于屏幕。
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存屏幕 #####################################################################
##
## 这些屏幕负责允许玩家保存游戏并将其重新读取。由于它们几乎完全一样，因此它们都
## 是以第三方屏幕“file_slots”来实现的。
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("SAVE GAME"))


screen load():

    tag menu

    use file_slots(_("LOAD GAME"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto Save"), quick=_("Quick Save"))

    use game_menu(title, _("gui/icon/load.png")):

        fixed:

            ## 此代码确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    hbox:
                        button:
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5 size(179,127) yoffset 3

                            null height 20

                            text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("Empty Slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5
                xpos 520
                ypos 250

                xspacing 225
                yspacing 130
                xoffset 80
                yoffset 25

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    vbox:
                        spacing 24
                        imagebutton:
                            idle "gui/button/delete_idle.png"
                            hover "gui/button/delete_hover.png"
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action FileDelete(slot)
                            xoffset 3

                        imagebutton:
                            idle "gui/button/read_idle.png"
                            hover "gui/button/read_hover.png"
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action FileAction(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                imagebutton:
                    idle "gui/button/backward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    action FilePagePrevious(5,True)

                if config.has_autosave:
                    textbutton _("{#auto_page}A"):
                        hover_sound "audio/button/hover.wav"
                        activate_sound "audio/button/selected.wav"
                        action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q"):
                        hover_sound "audio/button/hover.wav"
                        activate_sound "audio/button/selected.wav"
                        action FilePage("quick")

                ## “range(1, 10)”给出1到9之间的数字。
                for page in range(1, 6):
                    textbutton "[page]":
                        hover_sound "audio/button/hover.wav"
                        activate_sound "audio/button/selected.wav"
                        action FilePage(page)

                imagebutton:
                    idle "gui/button/forward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    action FilePageNext(5,True)

            # imagebutton:
            #     xpos 0.94
            #     ypos 0.92
            #     idle "gui/button/quick_quit_idle_background.png"
            #     hover "gui/button/quick_quit_hover_background.png"
            #     action Return(True)

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## 画廊屏幕 ######################################
screen gallery:
    $ next_cg_page = cg_page + 1
    $ prev_cg_page = cg_page - 1
## # 确保任何其他菜单界面都会被替换。
    tag menu
## 背景图。
    #add "images/gallery/background.png"
    use game_menu(_("GALLERY")):
        hbox:
            add "gui/button/gallery_title.png" xpos -80 ypos -100

        hbox:
            text _("Character"):
                xpos 110
                ypos 60
                size 42
                style "gallery_text"

    ## 创建hbox，用于放置切换页面按钮。
        hbox:
            style_prefix "page"

            xalign 0.48
            yalign 1.0

            spacing gui.page_spacing

            if cg_page > 0:
                imagebutton:
                    idle "gui/button/backward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    xpos -270
                    ypos -70
                    action SetVariable('cg_page', prev_cg_page)
            else:
                imagebutton:
                    idle "gui/button/backward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    xpos -270
                    ypos -70
                    action SetVariable('cg_page', 0)

            for page in range(1, 4):
                textbutton "[page]":
                    xpos -270
                    ypos -65
                    action SetVariable('cg_page', page-1)

            if cg_page < 2:
                imagebutton:
                    idle "gui/button/forward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    xpos -270
                    ypos -70
                    action SetVariable('cg_page', next_cg_page)
            else:
                imagebutton:
                    idle "gui/button/forward_idle.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    xpos -270
                    ypos -70
                    action SetVariable('cg_page', 2)

        hbox:
            xpos 80
            ypos 140
            style_prefix "cha"

            textbutton _("舒子淇"):
                style "cha_button"

                xpos 40 yalign 0.1
                action SetVariable('cg_page', 0)

            textbutton _("夏何"):
                style "cha_button"

                xpos -90 yalign 0.22
                action SetVariable('cg_page', 1)

            textbutton _("林小莫"):
                style "cha_button"

                xpos -220 yalign 0.34
                action SetVariable('cg_page', 2)

            #textbutton "2" action SetVariable('cg_page', 1) , ShowMenu("gallery")
            #textbutton "3" action SetVariable('cg_page', 2) , ShowMenu("gallery")
            #textbutton "4" action SetVariable('cg_page', 3) , ShowMenu("gallery")
            ## 按照CG图数量和结构布局，可以继续增加，但相关参数（页面数量判断）也要调整。

        #frame background None :
            #pos (650 ,160) ## 可以调整位置，比如画廊左侧有菜单的话，那样其他参数也要调整了。

    ## 用于显示CG图的 grid 可视组件：[url=https://www.renpy.cn/doc/displayables.html?highlight=grid#Grid]https://www.renpy.cn/doc/displayables.html?highlight=grid#Grid[/url]
            # grid gal_rows gal_cols:
            #
            #     pos (-190,-160) # align (0.2,0.3)
            #
            #     ## 调整框体大小。
            #     xsize 650
            #     ysize 360
            #
            #     spacing 110
            #
            #     $ i = 0
            #     $ next_cg_page = cg_page + 1
            #
            #     if next_cg_page > int(len(gallery_cg_items)/gal_cells):
            #         $ next_cg_page = 0
            #     for gal_item in gallery_cg_items:
            #         $ i += 1
            #         if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
            #
            #             add g_cg.make_button(gal_item + "mark",
            #                 "locked",
            #                 "locked",#未解锁的专用“锁图”。
            #                 hover_border=gal_item+" small",
            #                 idle_border=gal_item+" small",
            #                 background="locked",
            #                 hover_background="unlocked_hover"
            #                 )
            #
            #     ## 应对CG数量有零头，用来填满grid，不然出错。
            #     for j in range(i, (cg_page+1)*gal_cells):
            #         null
            $cg_cells = [0,4,7,11]
            grid gal_rows gal_cols:

                pos (-100,-50) # align (0.2,0.3)

                ## 调整框体大小。
                xsize 650
                ysize 360

                spacing 110

                $ i = 0
                $ next_cg_page = cg_page + 1

                if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                    $ next_cg_page = 0
                for gal_item in gallery_cg_items:
                    $ i += 1
                    if i <= cg_cells[cg_page+1] and i>cg_cells[cg_page]:

                        add g_cg.make_button(gal_item + "mark",
                            "locked",
                            "locked",#未解锁的专用“锁图”。
                            hover_border=gal_item+" small",
                            idle_border=gal_item+" small",
                            background="locked",
                            hover_background="unlocked_hover"
                            )

                ## 应对CG数量有零头，用来填满grid，不然出错。
                for j in range(cg_cells[cg_page+1]-cg_cells[cg_page], gal_cells):
                    null
        #use music_room

        #label _("Extra Mode"):
            #style "game_menu_label"

        # imagebutton:
        #     xpos 0.94
        #     ypos 0.92
        #     idle "gui/button/quick_quit_idle_background.png"
        #     hover "gui/button/quick_quit_hover_background.png"
        #     action Return(True)

style cha_button:
    properties gui.button_properties("cha_button")
    activate_sound "audio/button/selected.wav"
    hover_sound "audio/button/hover.wav"

style cha_button_text:
    properties gui.button_text_properties("cha_button")
## 设置屏幕 ########################################################################
##
## 设置屏幕允许玩家配置游戏以更好地适应自己。
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen music_room:
    tag menu
    use game_menu(_("MUSIC ROOM")):
        hbox:
            add "gui/icon/music_room.png" xpos 0 ypos -115
        hbox:
            xpos 200
            ypos 140
            vbox:
                # 每条音轨的播放按钮。
                textbutton "寄一片枫叶写的信（piano ver）" action mr.Play("audio/001.mp3") style "cha_button"
                textbutton "今天，明天的日常" action mr.Play("audio/002.mp3") style "cha_button"
                textbutton "你周围的空气" action mr.Play("audio/003.mp3") style "cha_button"
                textbutton "天气不错" action mr.Play("audio/004.mp3") style "cha_button"
                textbutton "与某个坏蛋的孽缘" action mr.Play("audio/005.mp3") style "cha_button"
                textbutton "青空流云" action mr.Play("audio/006.mp3") style "cha_button"
                textbutton "公主晚安" action mr.Play("audio/007.mp3") style "cha_button"
                null height 40
                textbutton "下一首" action mr.Next() style "cha_button"

            vbox:
                xpos 200
                textbutton "怎么办" action mr.Play("audio/008.mp3") style "cha_button"
                textbutton "哦~吼！" action mr.Play("audio/009.mp3") style "cha_button"
                textbutton "晴夜" action mr.Play("audio/010.mp3") style "cha_button"
                textbutton "黄昏只剩一刻钟" action mr.Play("audio/011.mp3") style "cha_button"
                textbutton "步履不停" action mr.Play("audio/012.mp3") style "cha_button"
                textbutton "雨有点冷" action mr.Play("audio/013.mp3") style "cha_button"
                null height 80
                textbutton "上一首" action mr.Previous() style "cha_button"

screen preferences():

    tag menu

    use game_menu(_("SETTINGS"),_("gui/icon/settings.png")):

        # imagebutton:
        #     xpos 0.94
        #     ypos 0.92
        #     idle "gui/button/quick_quit_idle_background.png"
        #     hover "gui/button/quick_quit_hover_background.png"
        #     action Return(True)

        vbox:
            hbox:
                box_wrap True
                style_prefix "slider"

                vbox:

                    label "Volume":
                        xalign 0.3
                    if config.has_music:

                        null height 60

                        hbox:
                            yalign 1.0
                            add "gui/icon/music.png"
                            null width 22
                            text "Music Volume"
                            null width 36
                            bar value Preference("music volume") style "preferences_bar"

                        null height 36

                    if config.has_sound:

                        hbox:
                            add "gui/icon/sound.png"
                            null width 15
                            text "Sound Volume"
                            null width 32
                            bar value Preference("sound volume") style "preferences_bar"

                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)

                        null height 36

                    if config.has_voice:

                        hbox:
                            add "gui/icon/voice.png"
                            null width 35
                            text "Voice Volume"
                            null width 36
                            bar value Preference("voice volume") style "preferences_bar"

                vbox:
                    #style_prefix "check"
                    label "Skip":
                        xalign 0.25

                    null height 60

                    hbox:
                        text "Unseen text"
                        null width 36
                        imagebutton:
                            idle "gui/button/skip_idle.png"
                            hover "gui/button/skip_idle.png"
                            selected_idle "gui/button/skip_selected.png"
                            selected_hover "gui/button/skip_selected.png"
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action Preference("skip", "toggle")

                    null height 40

                    hbox:
                        text "After Choices"
                        null width 23
                        imagebutton:
                            idle "gui/button/skip_idle.png"
                            hover "gui/button/skip_idle.png"
                            selected_idle "gui/button/skip_selected.png"
                            selected_hover "gui/button/skip_selected.png"
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action Preference("after choices", "toggle")

                    null height 40

                    hbox:
                        text "Translations"
                        null width 36
                        imagebutton:
                            idle "gui/button/skip_idle.png"
                            hover "gui/button/skip_idle.png"
                            selected_idle "gui/button/skip_selected.png"
                            selected_hover "gui/button/skip_selected.png"
                            hover_sound "audio/button/hover.wav"
                            activate_sound "audio/button/selected.wav"
                            action InvertSelected(Preference("transitions", "toggle"))

                ## 可以在此处添加类型为“radio_pref”或“check_pref”的其他“vbox”，
                ## 以添加其他创建者定义的首选项设置。

            null height (4 * gui.pref_spacing)

            hbox:
                yalign 0.5

                box_wrap True

                label "Text Speed"

                null width 37

                bar value Preference("text speed") style "preferences_bar"

                null width 120

                label "Display"

                null width 53

                imagebutton:
                    idle "gui/button/smallscreen_idle_background.png"
                    hover "gui/button/smallscreen_selected_background.png"
                    selected_idle "gui/button/smallscreen_selected_background.png"
                    selected_hover "gui/button/smallscreen_selected_background.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    action Preference("display", "window")

                null width 36

                imagebutton:
                    idle "gui/button/fullscreen_idle_background.png"
                    hover "gui/button/fullscreen_selected_background.png"
                    selected_idle "gui/button/fullscreen_selected_background.png"
                    selected_hover "gui/button/fullscreen_selected_background.png"
                    hover_sound "audio/button/hover.wav"
                    activate_sound "audio/button/selected.wav"
                    action Preference("display", "fullscreen")

            # 这里开始是新的hbox
            null height (4 * gui.pref_spacing)
            # hbox:
            #     textbutton "Reset":
            #         text_color "#fa1515"
            #         text_size 42
            #         hover_sound "audio/button/hover.wav"
            #         activate_sound "audio/button/selected.wav"
            #         action Show("reset_check")
            #
            #     null width 728


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

style preferences_bar is bar:
    base_bar "gui/scrollbar/preferences_bar.png"
    thumb "gui/scrollbar/preferences_bar_thumb.png"
    thumb_shadow "gui/scrollbar/preferences_bar_thumb_shadow.png"
    thumb_offset 3
    xsize 128

init python:
    #重置设置的函数Reset
    def Reset():
        preferences.text_cps = 100
        # Preference("music volume", 0.5)         #设置音乐音量
        # Preference("sound volume", 0.5)         #设置音效音量
        # Preference("voice volume", 0.5)         #设置语音音量
        # Preference("skip", "seen")              #只跳过看过的信息
        # Preference("after choices", "stop")     #在选项后停止跳过
        # Preference("transitions", "all")        #显示所有转场(transition)效果
        # Preference("text speed", 25)            #设置文本显示速度为每秒25字符
        renpy.hide_screen("reset_check")                     #关闭确认界面

screen reset_check:
    use confirm("Are you sure you want to {color=#fa1515}Reset{/color} ?",Reset(),Hide("reset_check"))

## 历史屏幕 ########################################################################
##
## 这是一个向玩家显示对话历史的屏幕。虽然此屏幕没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## 避免预缓存此屏幕，因为它可能非常大。
    predict False

    # use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

    style_prefix "history"

    imagebutton:
        xpos 0.94
        ypos 0.895
        idle "gui/button/quick_quit_idle_background.png"
        hover "gui/button/quick_quit_hover_background.png"
        hover_sound "audio/button/hover.wav"
        activate_sound "audio/button/selected.wav"
        action Return()

    frame:
        background "gui/history_frame.png"
        margin (180,20)

        viewport:
            area(64,22,800,600)
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            yinitial 1.0
            side_yfill True

            vbox:
                spacing 50

                for h in _history_list:

                    if h.who:

                        label h.who:
                            style "history_name"
                            substitute False

                            ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                            ## 人文本中。
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    # $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text h.what:
                        substitute False

                if not _history_list:
                    label _("对话历史记录为空。")

                vbox:
                    null height 20

## 此代码决定了允许在历史记录屏幕上显示哪些标签。

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    background Frame("gui/history_frame.png")
    xfill True
    yfill True

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    ysize 30
    xfill True

style history_label_text:
    size 28
    xalign 0.5


## 帮助屏幕 ########################################################################
##
## 提供有关键盘和鼠标映射信息的屏幕。它使用其它屏幕
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("键盘") action SetScreenVariable("device", "keyboard")
                textbutton _("鼠标") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("手柄") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("回车")
        text _("推进对话并激活界面。")

    hbox:
        label _("空格")
        text _("推进对话但不选择选项。")

    hbox:
        label _("方向键")
        text _("导航界面。")

    hbox:
        label _("Esc")
        text _("访问游戏菜单。")

    hbox:
        label _("Ctrl")
        text _("按住时快进对话。")

    hbox:
        label _("Tab")
        text _("切换对话快进。")

    hbox:
        label _("Page Up")
        text _("回退至先前的对话。")

    hbox:
        label _("Page Down")
        text _("向前至之后的对话。")

    hbox:
        label "H"
        text _("隐藏用户界面。")

    hbox:
        label "S"
        text _("截图。")

    hbox:
        label "V"
        text _("切换辅助{a=https://www.renpy.org/l/voicing}自动朗读{/a}。")


screen mouse_help():

    hbox:
        label _("左键点击")
        text _("推进对话并激活界面。")

    hbox:
        label _("中键点击")
        text _("隐藏用户界面。")

    hbox:
        label _("右键点击")
        text _("访问游戏菜单。")

    hbox:
        label _("鼠标滚轮上\n点击回退控制区")
        text _("回退至先前的对话。")

    hbox:
        label _("鼠标滚轮下")
        text _("向前至之后的对话。")


screen gamepad_help():

    hbox:
        label _("右扳机键\nA/底键")
        text _("推进对话并激活界面。")

    hbox:
        label _("左扳机键\n左肩键")
        text _("回退至先前的对话。")

    hbox:
        label _("右肩键")
        text _("向前至之后的对话。")


    hbox:
        label _("十字键，摇杆")
        text _("导航界面。")

    hbox:
        label _("开始，向导")
        text _("访问游戏菜单。")

    hbox:
        label _("Y/顶键")
        text _("隐藏用户界面。")

    textbutton _("校准") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他屏幕
################################################################################


## 确认屏幕 ########################################################################
##
## 当 Ren'Py 需要询问玩家是非问题时，会调用确认屏幕。
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## 显示此屏幕时，确保其他屏幕无法输入。
    modal True

    zorder 200

    add "gui/overlay/confirm.png"

    frame:

        # vbox:
        #     xalign .5
        #     yalign .5
        #     spacing 35
        xalign 0.5
        yalign 0.5
        xysize (477,265)
        background "#000000"
        add "gui/confirm_frame.png" pos(0,0)

        text _(message):
            xalign 0.5
            yalign 0.3
            # hbox:
            #     xalign 0.5
            #     spacing 126

        imagebutton:
            idle "gui/button/confirm_no_idle_background.png"
            hover "gui/button/confirm_no_hover_background.png"
            hover_sound "audio/button/hover.wav"
            activate_sound "audio/button/selected.wav"
            xalign 0.3 ypos 165
            action no_action

        imagebutton:
            idle "gui/button/confirm_yes_idle_background.png"
            hover "gui/button/confirm_yes_hover_background.png"
            hover_sound "audio/button/hover.wav"
            activate_sound "audio/button/selected.wav"
            xalign 0.7 ypos 165
            action yes_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")




## 快进指示屏幕 ######################################################################
##
## “skip_indicator”屏幕用于指示快进正在进行中。
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知屏幕 ########################################################################
##
## 通知屏幕用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL 模式屏幕 ####################################################################
##
## 此屏幕用于 NVL 模式的对话和菜单。
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## 在“vpgrid”或“vbox”中显示对话框。
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## 如果给定，则显示“menu”。 如果“config.narrator_menu”设置为“True”，
        ## 则“menu”可能显示不正确，如前述。
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## 此代码控制一次可以显示的最大 NVL 模式条目数。
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


################################################################################
## 移动设备界面
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## 由于鼠标可能不存在，我们将快捷菜单替换为更容易触摸且按钮更少更大的版本。
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("回退") action Rollback()
            textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("菜单") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
