label ch52_l2:
    #Scene1
    scene bg activity room2 with fade
    play music "audio/007.mp3" fadein 1.0 fadeout 1.0
    "今天是部门例会的日子。"
    show s summer normal medium with dissolve
    s "[m_name]..."
    "..."
    s "[m_name]？今天你一直在发呆啊。"
    m "啊。这样啊。"
    s "林小莫今天没有来呢。"
    m "你有联系过她吗？"
    s "我没有她的联系方式啊。"
    m "这样啊。"
    "这也并不奇怪。社团本质上还是同好会，也没有什么强制的规定。"
    "我沉默了。"
    show s summer surprised medium with dissolve
    s "你是不是知道林小莫今天会这样。"
    m "我不知道。"
    m "我虽然有她的联系方式，但是她没提到过这件事。"
    "......"
    "一阵沉默。这沉默似乎表示着我们都心知肚明。"
    m "我去找一找林小莫吧。"
    m "或许我知道她在哪儿。"
    show s summer normal medium with dissolve
    s "不用了。"
    s "今天的部门例会到这里就结束了。不用特地麻烦自己做额外的事情。"
    s "今天就先回去吧。"
    "我乖乖地按照舒子淇的话往活动室外走去，悄悄低头看了眼手机。"
    "上面显示的是与林小莫最后的聊天记录。"
    "昨天11：43P.M."
    $m_name = "阿酱"
    m "明天的部门例会，你去吗？"
    "......"
    $m_name = temp_name
    return
