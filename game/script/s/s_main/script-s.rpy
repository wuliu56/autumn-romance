label ch_s:
    call ch6_s from _call_ch6_s
    if s2:
        pass
    else:
        call ch7_s from _call_ch7_s
        if s1:
            pass
        else:
            call ch8_s from _call_ch8_s
    return