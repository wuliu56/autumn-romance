label ch_x:
    call ch5_x from _call_ch5_x
    call ch6_x from _call_ch6_x
    if x2_flag:
        pass
    elif x1_flag:
        pass
    else:
        call ch7_x from _call_ch7_x
    return
