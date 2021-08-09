label ch5_main:

    if l_flag:
        jump ch_l
    else:
        "这是共通线第五章的内容"
        call ch51_main
        call ch52_main
        call ch53_main
    return
