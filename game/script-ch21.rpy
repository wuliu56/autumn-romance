label ch21_main:
    "这是第2.1章内容"

    #Scene1(招新大会)
    "社员A" "「快点把要上展台手办摆好，昨天我们不是排过一遍了了吗？」"
    "社员B" "「诶，诶诶诶，小心点！很贵的，这些东西除了社团的还有社员私人的呢！」"
    "社员B" "「要是弄坏了我找你赔！那个ELL酱的手办弄坏了我打死你！」"
    "社员C" "「哦哦！对不起！我错了我错了！」"
    "社员C" "「诶，我这不摆的好好的嘛？我还以为真弄坏了呢！」"
    "社员A" "「别光看着了，没人会蠢到把这么贵的手办给弄掉。」"
    "社员A" "「倒是你，快点来来把周边摆上桌，桌上太乱了！」"
    "社员B" "「哦，来了！不过舒子淇部长...」"
    "社员B" "「啊，舒子淇已经在看摊子了，帮不了忙了，不然我还想问问她这情况该怎么办呢...」"
    "社员C" "「新生们都陆陆续续入场了，我们去年也是这么迫不及待的吗...」"

    "......"

    m "..."
    s "嗯，是的。请收一下我们的传单吧。这上面的二维码和那边海报的二维码是一样的，扫了就能进入我们的新生群。"
    m "...海报在那边。"
    s "嗯嗯，进社团本身是没有门槛的，要进部门的话在这之后我们会开全社大会拉人的。"
    m "..."
    s "没关系，只要你有热情，面试什么的都是小意思。不管是宅艺还是舞台剧，每年都有零基础的进入部门。"
    "说的可能就是我了。话说我待的那个宣传部也是需要门槛的吗？"
    s "就算进了我们社团，每天只是水水群也没关系。你一定能在这里找到兴趣相投的同伴。"
    "我把已经填了数个新生名字报名表递给舒子淇。"
    s "行，那么麻烦在这里填一下姓名，学号和联系方式。"
    s "好，谢谢，“星辉动漫研究社”欢迎你的加入！"
    m "热烈欢迎！"

    "舒子淇和我目送报完了名的新生。"
    "知道刚才还在排队报着名的新生出现了暂时的断档。"
    "社团里表演部两个出cos的家伙正对着新生的人流大声吆喝拉客。"
    s "..."
    m "..."
    s "看你做起事情来也不含糊，在社团里跟人交流也没什么问题。"
    s "怎么现在变得这么胆小，跟块木头似的。热情一点啊！"
    m "嗯。可能有点不太习惯吧。"
    m "毕竟...再怎么说我也还只是社团里的新人啊。"
    s "真是的，说话而已哪有什么不习惯的。"
    s "看，又来人了。你，上！"

    """
    停在社团面前的是个个子不高，戴着眼镜的女生。

    刚才一直来的都是各种宅男，原来也会有一些宅女啊。

    话说舒子淇也算是个宅女？又或者，动漫社的人真的都像我这样是个死宅吗？

    不管了，先把眼前的新生招呼好。
    """

    m "欢迎光临！"
    "我的胳膊肘被轻轻掐了一下。好吧，我说的话好像有点不合时宜。"
    m "你好，这里是“星辉动漫研究社”。"
    "新生（女）" "那个...动漫社的报名有什么要求吗？"
    m "我们社的话...入社是没有门槛的。"
    "新生（女）" "是吗..."
    "对话一下中断了。我感觉到舒子淇正拼命瞪着我。"
    m "啊...那个，想要了解更多的话可以扫一下这两个二维码，分别是我们的社团群和公众号的二维码。"
    m "请拿一下这个传单，在报名表上填下信息吧。这张传单上有关于我们漫研社各个部门的具体介绍。"
    m "想要了解更多的社团信息，还有进入部门的话都可以在不久后的社团大会上进行哦。"
    "新生（女）" "哦，好的。"
    "新生（女）" "谢谢学长！"
    "说完，小女生踏着小碎步离开了。"
    "我窃喜，嚯嚯，学长啊。嘿嘿。"
    m "感觉不错。"

    #选项4
    menu:
        s "还感觉不错呢，看到人家小学妹叫你学长就色眯眯地笑。"

        "「我就是萝莉控」":
            $l_appeal+=1
            m "小学妹有什么不好的？谁不喜欢娇小可爱的女孩子呢？"

        "「我才不是萝莉控」":
            $x_appeal+=1
            m "比起小学妹，我更喜欢色气的大姐姐哦！"

        "沉默":
            $s_appeal+=1
            m "..."
            m "要行使缄默权来保护自己的尊严。"

    s "好了好了别辩解了，谁管你啊。"
    s "还有，介绍的时候自然一点，积极一点啊。声音太小了，含糊不清的。"
    m "哦，哦。"
    s "看嘛，人又来了。不要害怕大声说话，热情地去吆喝啊。"
    m "明白了。"
    "我偷偷瞥了舒子淇一眼。只见她依然盯着前方，一副等待着下一位顾客的样子。"
    "我也不能太散漫了。打起精神来，今天可有的忙活呢。"

    "......"

    "社员A" "部长，还有[m_name]。换班了，下一个小时是我们来着。你们先去休息吧。"
    "社员B" "是啊，舒子淇部长还真是辛苦，负责最早和最晚的班。"
    s "哪有，大家都为迎新做了不少贡献。"
    s "还有，不用叫我部长，跟大家一样都直接喊名字吧。"
    "社员B" "诶，好嘞。话说，我们到现在已经招了多少人了？"
    s "已经五十几个了，今年报名的人肯定能突破去年的吧。"
    s "希望今年的新生能活跃一些。"
    "社员A" "毕竟每年都有近一半的人从来不参加活动啊。"
    "社员B" "还有创绘部啊，大半人都是大三大四的，要是再找不到新生可就没人了..."
    "在舒子淇和其他社员谈话的中途，我跑到了展柜面前，欣赏起了一排排手办。"
    "准备的时候我不是负责这个的，还没有机会仔细看。"
    "不过这数量还真多啊，Fade，点猫...哇，连MA的角色都有！这都是社团的吗，还是说哪些是社员私人的..."
    s "这么喜欢手办啊。看你在这盯了好长时间。"
    m "还行吧。自己买了的不多，所以看到这么多还挺稀奇的。"
    s "诶~这么说来，我们社的宅研那群人经常会搞什么鉴赏会，趁活动室没人的时候聚在那边，把自己的手办啊，周边啊，还有涩..."
    "舒子淇脸一红，顿了一下，突然变得有点结巴。"
    s "反，正...就这些东西拿出来互相展示分享。"
    s "你，你要，要是感兴趣的话，去玩玩也不是不行..."
    "真是好懂的反应。让人有点想捉弄她。"
    m "舒子淇有去参加过鉴赏会吗？"
    s "我才没有！谁会去看那种涩X的东西啊。"
    s "啊。"
    m "啊。"
    "舒子淇的脸一下子涨的通红，双眼一下怒瞪着我，一下又别开。"
    "好像做了什么坏事，内心充满了罪恶感。"
    m "哎呀，这个小百合的手办真是棒呢，特别是头发，还有眼睛的质感。"
    m "舒子淇有没有买过手办？有特别喜欢的角色吗？"
    """
    舒子淇瞪着我，又气又羞，不愿搭理我的样子。

    没办法，就这么逃走似乎也不太好，还是待在摊位这边吧。

    看看这里还有什么让我感兴趣的展品。

    哦，摊位门口又排起队了。
    """

    "......"

    "社员A" "「你看那个学妹，好可爱啊。」"
    "社员B" "「可爱关你什么事，看那样子，绝对不是二刺螈。」"
    "社员B" "「怎么，你难道有什么现充的手段去勾搭人家小学妹？」"
    "社员A" "「不说这个，她是不是在向我们这边过来啊。」"

    """
    我和舒子淇心不在焉地守着展柜，不由得被两人的对话吸引了注意。

    在人群中，一个显眼的存在朝着我们的方向走来。

    那是一个身材娇小的女孩子，身上可爱的打扮与周围的死宅们格格不入。

    明明是穿着日常的衣服，却给人一种从二次元中走出来的角色一般的感觉。

    我的注意完全被她抓住了。

    整个人群有如为凸显出她的存在一般。想必不管是男性还是女性，都不由得地去望向她吧。

    她径直走到我们旁边，站在展物柜前，指着最上层那个瓦娘的手办。
    """

    "可爱的女孩子" "我想要这个。"
    "？"
    "可爱的女孩子" "多少钱？"
    "？？？"
    "这是什么脑回路？"
    "不止是我和其它社员，连在场参观的新生都一个个愣在了原地。"
    "奇怪的女孩子" "这个要多少钱？"
    "在场的大部分人都还不知所措时，舒子淇最先反应过来。"
    s "不好意思同学，我们这里的展品都是社员的个人物品或者社团的公有物品。"
    s "这些展品不是用来贩卖的。"
    "奇怪的女孩子" "没关系，我可以出钱买。"
    "奇怪的女孩子" "我想要这个，很可爱。"
    "舒子淇依旧保持着彬彬有礼的笑容，用温和的态度解释着。"
    s "对不起，我们这个是非卖品。"
    s "如果你实在是想要的话，不妨先加入我们漫研社。"
    s "我们可能会在其他的活动上发放类似的手办作为奖品。"
    "奇怪的女孩子" "可我对漫研社没有兴趣。我只想要这个小人偶。"
    "周围开始传来窃窃私语，这里的骚动无疑是附近的焦点。"
    "舒子淇仍然维持着一个良好的态度。"
    "但可以看出，她已经在费很大力气忍耐了。"
    s "可以问一下你的名字吗，同学？"
    "奇怪的女孩子" "林小莫。"

    """
    不好，气氛开始变得险恶了。

    现在已的情况经对招新的宣传造成些许妨碍了，要是事态还得不到平息的话，可能还会受到更大的影响。

    然而这位名叫林小莫的女孩子仍一副懵懵懂懂，什么都没注意到的样子。

    周围的社员们推推搡搡，没有一个人站出来。

    真麻烦，我忍不住这样想。

    咬一咬牙，我赶紧站了出来吧舒子淇拉到一边。
    """

    s "干什么，你难道还想真的把手办卖给她不成？"
    s "我们这里是招新的展位，不是卖东西的小摊。"
    "少有地，舒子淇的语气比平时冲了不少。"
    m "我怎么会这么想呢？我可不可以问一下刚才那个手办是私有的还是社团的，还有就是它的价格大概是多少？"
    s "是社团的前辈留下的，以前制作的社团看板娘的角色手办。"
    s "虽然一半是手工的，但是价格还是能达到这个（比划）三位数。"
    "一个点子闪过，我头脑里很快过了一下社团投入到这次迎新活动中的经费规模。"
    "这个想法或许可行。"
    s "你在打什么鬼主意？不要想一些不可能的事情。"
    m "也没有啦..."
    "犹豫了一下，我还是决定把这个想法说出来。"
    m "虽然把手办卖给某个人肯定不可能，但是我们如果把它用作整个迎新中所使用的道具的话应该不会有什么问题吧？"
    s "这是什么意思？你打算怎么用？"
    m "我听你们说这一年创绘部会少很多老社员，有些青黄不接。我们不妨..."

    """
    我提出我们可以在今天临时举行一个创绘比赛，以手办为优胜的奖品吸引新生，特别是有绘画技能的新生。

    这样一来既能吸引更多人加入漫研社，特别是我们的创绘部；二来可以选拔对社团有用的人才，直接填补创绘部老人失活造成的战力不足。

    现在刚过12点，现在正是人流量渐渐增多的时候，迎新活动还有四五个小时才结束，如果现在就开始的话，应该能在结束前收到一些参赛作品。

    手办价格的话，算进活动经费里大概会拉高三四成左右，不是无法完全容许的情况。
    """

    s "比赛的地点呢？总不可能现在让新生回宿舍画张画回来吧，现场也没有专门的工具。"
    m "社团活动室就在迎新会场后面的活动中心里，安排两三个人来回领路应该就可以了，那里有足够的空间，还有桌椅。"
    s "那么我们应该用纸绘还是板绘的形式呢？两种都有不好处理的地方。"
    m "还是纸绘更可行一些。到时候并不是所有参加者都能上手软件或者携带了自己的设备，况且能够板绘的人肯定是有一定的纸绘基础的。"
    s "你说的方法或许可行，我现在就去联系社长。"
    s "这个活动人手估计会不够，组织就交由[m_name]你来负责了，赶紧去摇人。"
    s "A，你先一个人看摊位，暂时先辛苦你了；B你过来协助[m_name]。"
    "社员A" "「不辛苦。我会让我们社的摊位吸引到更多新生的！」"
    "社员B" "「[m_name]，不错啊，一下子就想到一个这么好的方法。舒子淇部长全交给你负责，看来你比看上去可靠的多啊！」"
    "我好像揽下一个不得了的活。"
    m "诶，诶。诶————"

    "......"

    m "这个展台上的东西都是非卖品。"
    l "..."
    m "如果你真的想要这个手办的话，可以参加我们举办的创绘大赛。"
    l "..."
    m "如果拿到优胜，就会以奖品的形式免费送给你。"
    l "..."
    m "现在就可以报名，我们社团一会儿就会有人来把你带到比赛场地。"
    "林小莫几乎一直盯着刚才看中的，那个瓦娘的手办。偶尔把头转过来瞟我几眼，不说话。"
    "她真的在认真听吗？和不认识的比自己小的女生讲话好难啊..."
    m "所以...同学你愿不愿意来参加这个活动呢？"
    l "要。"
    "她的语气之果决，与刚才懵懵懂懂的氛围判若两人。"
    m "诶，诶？"
    l "带我去。"
    m "好，好，我明白了。还请等一下我们的工作人员..."
    "我四处看了看，舒子淇联系完社长就去赶制临时决定的创绘比赛的海报了，其它社员不是忙着看摊子就是在打电话发消息叫人去了。"
    "不会吧，我还得负责这个创绘比赛的组织和运营。要是在我离开的时候再来新生又有谁能来说明？临时联系的帮手也都还没到..."
    "真是的，快来啊..."
    "？？？" "[m_name]！"
    "身后不远处有人在喊我名字。我回过头去。"
    m "嗯？夏何？"
    x "呼，呼~赶过来累死了。"
    x "舒子淇部长让我来给你帮忙。什么创绘比赛啊...为什么你一个新人来看摊子能搞出这么多事情..."

    menu:
        x "本来我一个小时之后才会需要来看摊位的。哼。"

        "能不能赶紧来帮忙啊":
            $x_appeal+=1
            call choice_5a from _call_choice_5a
        "谢谢你过来帮忙":
            call choice_5b from _call_choice_5b

    x "哦，知道了。"
    x "这位同学，请跟我走一下哦。"
    x "呜~！"
    "林小莫听到了夏何的话，一下子凑到了夏何身边非常近的地方。"
    "从边上看来，就像要贴上去一样。"
    x "卡哇伊..."
    x "你是个好孩子呢。来，手给我，学姐带你到活动室去咯。"
    "林小莫点点头，非常顺从地把手递给夏何。"
    "夏何就这么牵着林小莫的手走了！？"
    "社团摊位上的众人" "哦~——"
    "而我则是张大嘴目瞪口呆地看着这一幕。夏何是个这么亲切的家伙嘛？"
    "社员A" "「这就是传说中的百合吗。爱了爱了。」"
    "社员B" "「不愧是我们漫研社，就是与众不同。」"
    "好吧，先不管他们。接下来还有搞这个什么创绘大赛的一堆工作要忙呢。"
    m "好了，注意回到面前的事情上来。B，你先和夏何轮流负责把人带到活动室去，一会C来了会替你，你就和我一起在这里负责活动的介绍和说明。"
    m "诶，舒子淇的消息...哦，刚好C你来了，你先去活动室找舒子淇把新的海报带过去打印吧，速去速回，回来了再去找B，他会告诉你要干什么的。"
    m "诶哆，接下来还有哪些人回来，我看看群里的回复..."
    m "..."
    m "啊↗↘→，忙死啦！"

    "......"

label choice_5a:
    "夏何的样子让我不禁有些傻眼。我们这边不也是事出有因吗啊喂！"
    m "真麻烦...一来就抱怨..."
    "我自认为很小声地在念叨她，可夏何似乎还是听见了。"
    x "你说什么？"
    "她的眉毛一下子竖了起来。听她那语气，似乎有点生气了。"
    m "嗯...呵，呵呵..."
    "我只得尴尬的笑了笑。"
    m "不不不，没什么，非常感谢你来帮忙！"
    m "那个，麻烦先把这位林小莫同学带到活动室去好吗？舒子淇和社长应该都在那里。"
    x "哼！"
    return

label choice_5b:
    m "那个十分感谢你过来帮忙。"
    m "那个，麻烦先把这位林小莫同学带到活动室去好吗？舒子淇和社长应该都在那里。"
    return
