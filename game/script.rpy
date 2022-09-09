#init python:
#    style.default.font = "simfang.ttf"
#    style.default.language = "simfang"
#    style.default.layout = "greedy"
########################################################################################################
## 定义图片
## image语句:[url=https://www.renpy.cn/doc/quickstart.html?highlight=image#image]https://www.renpy.cn/doc/quickstart.html?highlight=image#image[/url]
## 注意文件格式 png 与 jpg
init:
    $ config.keymap['self_voicing'] = []
    $ config.keymap['performance'] = []
    $ config.keymap['accessibility'] = []
    $ config.keymap['help'] = []
image cg_icon:
    "gallery/cg_icon.png"
    size(60,60)

image returnback:
    "gallery/return.png"
    size(60,60)

image previous:
    "gallery/previous.png"
    size(40,40)

image next:
    "gallery/next.png"
    size(40,40)

image hbar:
    "gui/slider/horizontal_idle_mbar.png"
    size(300,29)

image mthumb:
    "gui/slider/horizontal_[prefix_]mthumb.png"
    ypos -1
    zoom 0.8

image line:
    "gui/button/line.png"
    zoom 0.3

image bg idle:
    "gui/button/music_idle.png"
    xpos -0.6
    ypos -0.6
    size(55,55)

image bg hover:
    "gui/button/music_hover.png"
    xpos -0.6
    ypos -0.6
    size(55,55)

image bg selected:
    "gui/button/music_selected.png"
    xpos -0.6
    ypos -0.6
    size(55,55)

image musicbg:
    "gallery/musicbg.png"
    xpos 820
    ypos 130
    zoom 0.7

    size (531,710)

image bar:
    "gallery/bar.png"
    size (660,26)

## 定义 未解锁缩略图
image locked :
    "gallery/locked.png"
    xpos -20
    ypos -5
    size (179, 99) # 调整原图尺寸。

image unlocked_hover:
    xpos -20
    ypos -5
    "gallery/unlocked_hover.png"
    size (179, 99)

init python:
    #############################
    #画廊
    # 列出画廊解锁后的CG图片，可以继续添加，图片应该在初始化阶段就预先定义好。
    gallery_cg_items = ["CG s 1", "CG s 2", "CG s 3", "CG s 4", "CG x 1", "CG x 2", "CG x 5", "CG l 1", "CG l 2", "CG l 3", "CG l 4"]
    gallery_cg_items_s = ["CG s 1", "CG s 2", "CG s 3", "CG s 4", "CG s 5"]
    gallery_cg_items_x = ["CG x 1", "CG x 2", "CG x 3", "CG x 4", "CG x 5"]
    gallery_cg_items_l = ["CG l 1", "CG l 2", "CG l 3", "CG l 4"]

    ## 有多少行和列？
    gal_rows = 2
    gal_cols = 3

    ## CG缩略图大小（像素）注意图的比例。
    thumbnail_x = 140
    thumbnail_y = 87

    gal_cells = gal_rows * gal_cols

## 创建Gallery对象。
    g_cg = Gallery()

    g_cg.button("CG s 1"+"mark")
    g_cg.image("CG s 1")
    g_cg.unlock("CG s 1")

    g_cg.button("CG s 2"+"mark")
    g_cg.image("CG s 2")
    g_cg.unlock("CG s 2")

    g_cg.button("CG s 3"+"mark")
    g_cg.image("CG s 3")
    g_cg.unlock("CG s 3")

    g_cg.button("CG s 4"+"mark")
    g_cg.unlock_image("CG s 4")
    g_cg.unlock_image("CG s 5")

    g_cg.button("CG x 1"+"mark")
    g_cg.image("CG x 1")
    g_cg.unlock("CG x 1")

    g_cg.button("CG x 2"+"mark")
    g_cg.unlock_image("CG x 2")
    g_cg.unlock_image("CG x 3")
    g_cg.unlock_image("CG x 4")

    g_cg.button("CG x 5"+"mark")
    g_cg.image("CG x 5")
    g_cg.unlock("CG x 5")

    for gal_item in gallery_cg_items_l:
        g_cg.button(gal_item + "mark") # 按钮的标识。+ "mark"
        g_cg.image(gal_item) # 将一个新的图像添加至当前按钮。该图像由一个或多个可视组件构成。
        g_cg.unlock(gal_item) # 一个条件函数，使用一个或多个图片名作为入参，当所有入参的图像都被用户看过时表示条件满足。图片名称应该是字符串。

    g_cg.transition = fade # 0.5秒时间画面逐渐暗淡至全黑，然后0.5秒时间画面从全黑逐渐变亮成新界面。一个 Fade() 转场类的实例。
    cg_page=0

    #############################
    #音乐空间
    #  步骤1，创建一个MusicRoom实例。
    mr = MusicRoom(fadeout=1.0,single_track=True)

    # Step 2. 添加音乐文件。
    mr.add("audio/001.mp3")
    mr.add("audio/002.mp3")
    mr.add("audio/003.mp3")
    mr.add("audio/004.mp3")
    mr.add("audio/005.mp3")
    mr.add("audio/006.mp3")
    mr.add("audio/007.mp3")
    mr.add("audio/008.mp3")
    mr.add("audio/009.mp3")
    mr.add("audio/010.mp3")
    mr.add("audio/011.mp3")
    mr.add("audio/012.mp3")
    mr.add("audio/013.mp3")

default l_flag = False
default s_flag = False
default x_flag = False

label start:
    stop music fadeout 1.0
    #提示输入主角名称

    python:
        m_name = renpy.input("你的名字是？", length=10)
        m_name = m_name.strip()

        if not m_name:
             m_name = "主人公"
    #四章共通线
    call ch1_main from _call_ch1_main
    call ch2_main from _call_ch2_main
    call ch3_main from _call_ch3_main
    if l_appeal == 5:
        call ch4_main from _call_ch4_main
    else:
        call ch_l2 from _call_ch_l2
        call ch5_main from _call_ch5_main
    #call ch5_main
    #call ch_s
    return
