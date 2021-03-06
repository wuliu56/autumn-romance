label ch43_main:
    "这是第4.3章内容"
    #Scene1
    "动漫社活动室里。"
    s "明天我门院学生会外宣部要去陪领导慰问军训的新生。"
    s "但是这学年的负责人下午有课，我把这件事揽下来了。"
    m "所以这跟我有什么关系？"
    s "你忘了我跟你说过林小莫是我的直系学妹了？"
    m "啊，记得记得。所以呢？"
    s "明天，来帮我搬饮料。"
    s "我们趁这个机会接触一下林小莫。"
    m "可是我明明不是你们院的啊..."
    m "而且，要接触的话你一个人难道不是绰绰有余吗？再随便找一个院里的男劳动力干活就行了。"
    s "饮料要等院领导讲完话之后再发下去，哪个人愿意空出时间在太阳下站这么久。"
    m "林小莫不是女生排吗...肯定会有男生愿意去慰问学妹的吧..."
    "舒子淇瞪了我一眼。"
    s "好的，out。那种人会造成妨碍的。你该不会就这么想吧？"
    m "啊哈哈..."
    "我大概是属于有贼心没贼胆的那种吧。"
    s "总之，明天下午3:00在操场外面集会。"
    s "放心，饮料会被送到操场外面的，你只要搬进去就行了，不会太累。"
    m "...你不问问我明天下午有没有课吗？"
    s "那你有课吗？"
    m "...没有。不过..."
    "舒子淇好像猜到了我要说的话。"
    s "好吧，那我在最后确认一下你的意愿。"
    s "我打算去接触林小莫，劝诱她进入社团。"

    menu:
        s "明天下午能不能空出时间来协助我？"

        "「好吧」":
            $l_appeal+=1
            $s_appeal+=1
            call choice_8a
        "「也不是不行」":
            call choice_8b

    s "好，那就这么决定了。"
    s "明天下午你一定要到啊。"
    m "哦。"
    m "话说舒子淇..."
    m "你看过素晴世界吗？"
    s "嗯？什么？"
    m "就是有一个很有名蓝毛女神的番。"
    s "异世界？好像是男性向后宫吧。"
    m "嗯。"
    s "有机会的话，再说吧。"
    s "我不是说对后宫番有什么偏见哦，我只是不怎么看这类的罢了。"
    "一般来讲，女生吃到这种安利应该是不感兴趣的反应吧..."
    "我又想起几天前的林小莫。这家伙，是有点奇怪吧？"

    #Scene2
    "今天的阳光也很毒辣，舒子淇他们院的领导正站在操场上的树荫下给军训的新生们讲话慰问。"
    "我和舒子淇则在一旁的空地上守着整箱的饮料。"
    "某院领导" "「巴拉巴拉巴拉巴拉...」"
    "某院领导" "「那么，今天我要说的就这么多。」"
    "某院领导" "「你们的学长学姐们也带来了饮料慰问一下大家，希望大家鼓鼓劲，继续积极参加接下来的训练。」"
    "稀稀落落的鼓掌声响起。"
    "解散的队伍三三两两地走到操场边的树荫下拿饮料休息，舒子淇趁机和林小莫搭话。"
    s "嗨，小莫。"
    l "嗯？"
    s "是我啊，还记得我吗？动漫社的。"
    s "我们还是一个学院的呢。好巧啊。"
    l "..."
    "哦吼，完蛋。林小莫一副不解的样子，显然是没认出舒子淇来。"
    "舒子淇的笑脸僵硬了几分。"
    s "哈哈，是一下没认出来吗？"
    s "我是星辉动漫社那天负责招新的舒子淇。创绘比赛的时候我们应该见过。"
    s "拿到的奖品手办，还喜欢吗？"
    l "嗯。很喜欢。"
    s "我们社团的办公室还有很多前辈留下来的和部员带来的藏品，有兴趣要不要去看一看？"
    l "嗯，有机会的话。"
    s "小莫的绘画水平很高呢，是学过什么吗？"
    l "就普通的...水粉，还有素描吧。"
    s "怪不得画出来的画那么棒呢。我们社团的宣传部一定很适合你。"
    s "招新那天来到我们社团，觉得我们星辉漫研社怎么样？"
    l "嗯..."
    l "挺不错的？"
    "为什么是疑问语气啊..."
    s "那，有没有兴趣加入我们社？"
    l "......"
    "林小莫明显一脸为难的样子。我正想上去开解一下，教官突然就吹起了集合的口哨。"
    s "那么今天就这样吧，要是有入社的意愿，随时来找我们的人哦？"
    s "就在社团活动室那边经常有人在的。"
    "林小莫向舒子淇点了点头，正准备转身回去的时候看见了我。"
    "我俩的目光一下子对上了。林小莫的表情似乎舒缓了一些。"
    l "啊，[m_name]学长。"
    m "嗯。你好啊。"
    l "学长好。"
    "说完，林小莫就小跑着回到队伍里去了。"
    "舒子淇一脸狐疑地看着我。"
    s "你们两的关系似乎很好嘛？"
    m "嗯？一般般啊，也就认识而已。"
    s "小莫明明连我的脸和名字都没记住...是我的问题吗？"
    s "不过，既然这样。那么劝诱林小莫的工作交给你来负责可以吗？"
    m "我？"
    m "我们平时有没有什么交集，怎么劝诱？"
    s "找个机会加上QX或者X信，多接触接触聊聊天。"
    s "小莫对你的印象看上去不差，感觉交给你来更靠谱些。"
    "我拂了拂额上的汗。"
    m "这话说的怎么感觉有些怪怪的呢？"
    s "总之你尽力去试试看吧。这件事就全权交给你了。"
    m "哦....."
    m "好吧......"
    "我回头看了看队伍中的林小莫，一瞬间眼睛似乎对上了，但小莫的视线又很快移开了。"
    "刚才林小莫是在往我和舒子淇这边看吗？"
    "算了，不管它了。今天真热，回宿舍歇会。"
    return

label choice_8a:
    "都已经说到这个份上了，再拒绝下去也不太好吧。"
    m "那好吧。"
    m "毕竟也算是对社团做一点贡献，吧？"
    s "至少作为宣传部的部长我就很感激你。"
    m "受不起，受不起。"
    s "[m_name]，你讲话的感觉，有的时候会变得很奇怪呢。"
    "这是在损我吗..."
    return

label choice_8b:
    "有点麻烦啊。不过，也没办法啊。"
    m "也行吧。"
    m "如果真的找不到别人。"
    m "诶，话说社团里没有别人可以来帮忙吗？"
    s "你不是和林小莫接触得最多吗？"
    s "招新那天一直到在一起，创绘比赛也是你为林小莫想出来的。"
    m "啊，也是呢..."
    return
