#init python:
#    style.default.font = "simfang.ttf"
#    style.default.language = "simfang"
#    style.default.layout = "greedy"
image hbar:
    "gui/slider/horizontal_idle_mbar.png"
    size(300,29)

image mthumb:
    "gui/slider/horizontal_[prefix_]mthumb.png"
    ypos -1
    zoom 0.8

image line:
    "gui/button/gallery/line.png"
    zoom 0.3

image bg idle:
    "gui/button/gallery/music_idle.png"
    xpos -0.6
    ypos -0.6
    size(55,55)

image bg hover:
    "gui/button/gallery/music_hover.png"
    xpos -0.6
    ypos -0.6
    size(55,55)

image bg selected:
    "gui/button/gallery/music_selected.png"
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

image 1-1_cg :
    "gallery/1-1_cg.png"
    size (1280 ,720) ## 原图尺寸：1920*1080，改为：1280*720


image 1-2_cg :
    "gallery/1-2_cg.png"
    size (1280 ,720)

image 1-3_cg :
    "gallery/1-3_cg.png"
    size (1280 ,720)

image 2-1_cg:
    "gallery/2-1_cg.png"
    size (1280 ,720)

image 2-2_cg :
    "gallery/2-2_cg.png"
    size (1280 ,720)

image 2-3_cg :
    "gallery/2-3_cg.png"
    size (1280 ,720)

image 3-1_cg:
    "gallery/3-1_cg.jpg"
    size (1280 ,720)

image 3-2_cg :
    "gallery/3-2_cg.jpg"
    size (1280 ,720)

image 3-3_cg :
    "gallery/3-3_cg.png"
    size (1280 ,720)

image 4-1_cg :
    "gallery/4-1_cg.jpg"
    size (1280 ,720)

image 4-2_cg :
    "gallery/4-2_cg.jpg"
    size (1280 ,720)

image 4-3_cg :
    "gallery/4-3_cg.jpg"
    size (1280 ,720)

image 5-1_cg :
    "gallery/5-1_cg.jpg"
    size (1280 ,720)

image 5-2_cg :
    "gallery/5-2_cg.jpg"
    size (1280 ,720)

image 5-3_cg :
    "gallery/5-3_cg.jpg"
    size (1280 ,720)

image 6-1_cg :
    "gallery/6-1_cg.jpg"
    size (1280 ,720)

image 6-2_cg :
    "gallery/6-2_cg.jpg"
    size (1280 ,720)

image 6-3_cg :
    "gallery/6-3_cg.jpg"
    size (1280 ,720)

image 7-1_cg :
    "gallery/7-1_cg.jpg"
    size (1280 ,720)

image 7-2_cg :
    "gallery/7-2_cg.jpg"
    size (1280 ,720)

image 7-3_cg :
    "gallery/7-3_cg.jpg"
    size (1280 ,720)

image 8-1_cg :
    "gallery/8-1_cg.jpg"
    size (1280 ,720)

image 8-2_cg :
    "gallery/8-2_cg.jpg"
    size (1280 ,720)

image 8-3_cg :
    "gallery/8-3_cg.jpg"
    size (1280 ,720)

image 9-1_cg :
    "gallery/9-1_cg.jpg"
    size (1280 ,720)

image 9-2_cg :
    "gallery/9-2_cg.jpg"
    size (1280 ,720)

image 9-3_cg :
    "gallery/9-3_cg.jpg"
    size (1280 ,720)

image 10-1_cg :
    "gallery/10-1_cg.jpg"
    size (1280 ,720)

image 10-2_cg :
    "gallery/10-2_cg.jpg"
    size (1280 ,720)

image 10-4_cg :
    "gallery/10-3_cg.jpg"
    size (1280 ,720)

image 11-1_cg :
    "gallery/11-1_cg.jpg"
    size (1280 ,720)

image 11-2_cg :
    "gallery/11-2_cg.jpg"
    size (1280 ,720)

image 11-3_cg :
    "gallery/11-3_cg.jpg"
    size (1280 ,720)

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
    ## 列出画廊解锁后的CG图片，可以继续添加，图片应该在初始化阶段就预先定义好。
    gallery_cg_items = ["1-1_cg", "1-2_cg", "1-3_cg", "2-1_cg", "2-2_cg", "2-3_cg", "3-1_cg", "3-2_cg", "3-3_cg",
     "4-1_cg", "4-2_cg", "4-3_cg", "5-1_cg", "5-2_cg", "5-3_cg", "6-1_cg", "6-2_cg", "6-3_cg",
     "7-1_cg", "7-2_cg", "7-3_cg", "8-1_cg", "8-2_cg", "8-3_cg", "9-1_cg", "9-2_cg", "9-3_cg",
     "10-1_cg", "10-2_cg", "10-3_cg", "11-1_cg", "11-2_cg", "11-3_cg"]

    ## 有多少行和列？
    gal_rows = 3
    gal_cols = 3

    ## CG缩略图大小（像素）注意图的比例。
    thumbnail_x = 140
    thumbnail_y = 87

    gal_cells = gal_rows * gal_cols

## 创建Gallery对象。
    g_cg = Gallery()

    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + "mark") # 按钮的标识。+ "mark"
        g_cg.image(gal_item) # 将一个新的图像添加至当前按钮。该图像由一个或多个可视组件构成。
        g_cg.unlock(gal_item) # 一个条件函数，使用一个或多个图片名作为入参，当所有入参的图像都被用户看过时表示条件满足。图片名称应该是字符串。

    g_cg.transition = fade # 0.5秒时间画面逐渐暗淡至全黑，然后0.5秒时间画面从全黑逐渐变亮成新界面。一个 Fade() 转场类的实例。
    cg_page=0

#init +1 python:
    ## 在这里，我们创建缩略图。 我们为BG创建了一个灰度缩略图，但我们使用一个特殊的“锁定(locked)”图像来防止剧透。
    # for gal_item in gallery_cg_items:
    #     renpy.image (gal_item + "mark", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))

################################################################################################################

#############################################################################################
##音乐空间
init python:

    #  步骤1，创建一个MusicRoom实例。
    mr = MusicRoom(fadeout=1.0)

    # Step 2. 添加音乐文件。
    mr.add("audio/kami.mp3", always_unlocked=True)
    mr.add("audio/kokochiqu.mp3")
    mr.add("audio/kokochifa.mp3", always_unlocked=True)

label start:
    call ch1_main from _call_ch1_main
    call ch2_main from _call_ch2_main
    call ch3_main from _call_ch3_main
    return
