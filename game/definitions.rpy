image ctc:
    pause 0.5
    "gui/ctc.png"
    block:
        alpha 1.0
        ease 1.0 alpha 0.0
        pause 0.5
        repeat

image bg playground = "bg/playground.png"
image bg campus = "bg/campus.png"

define narrator = Character(ctc = "ctc", ctc_position = "nestled")
define m = DynamicCharacter("m_name", what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")
define f = Character("枫",what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")
define l = Character("林小莫", what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")
define s = DynamicCharacter("s_name", what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")
define x = Character("夏何", what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")
define w = Character("乌拉", what_prefix = "「", what_suffix = "」", ctc = "ctc", ctc_position = "nestled")

default m_name = None
default s_name = "???"
default x_name = "看起来像宅的女生"
default w_name = "???"
default l_appeal = 0
default s_appeal = 0
default x_appeal = 0
