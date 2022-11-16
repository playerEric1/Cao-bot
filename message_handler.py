import re

def process_message(content):
    if '傻逼' in content:
        return '憋噴子了'
    if '中国人' in content:
        return '哔哔，你说中国人你冒犯到了我了你知道吗'
    if '集美' in content or 'zn' in content or '织女' in content:
        return '我求求你们别舔集美了可以吗？像个小学生一样，舔又舔不到，只能无能狂怒'
    if '大的' in content:
        return '《大的来了》是荒诞戏剧的代表作。以几个鼠人苦等“大的”，而“大的”不来的情节，' \
               '喻示人生是一场无尽无望的等待，表达了世界荒诞、人生痛苦的存在主义思想。它发生的' \
               '时间地点都是模糊的，布景也是一片荒凉，他们一边等，一边用各种无意义的手段打发时光。' \
               '他们经常显得头脑一片混乱，缺乏思维能力，尤其是极度地惧怕孤独。当有人询问“大的代表什么”时，' \
               '鼠人们说：“我要是知道，早就说出来了。 '
    if '书单' in content:
        return '我青年时代就读过：西游记，马可波罗游记，左丘明左传，我的故乡，纳楚克道尔基，吉檀迦利，园丁集，飞鸟集，' \
               '新月集，泰戈尔，三国演义，水浒传，老子，孔子，墨子，孟子，庄子，伏尔泰，孟德斯鸠，狄德罗，卢梭，圣西门，蒙田，傅立叶，拉封丹，' \
               '萨特，司汤达，莫里哀，大仲马，雨果，巴尔扎克，福楼拜，乔治桑，莫泊桑，小仲马，冉阿让，罗曼罗兰，羊脂球，卡西莫多，席勒，歌德，' \
               '海涅，莱布尼茨，黑格尔，康德，费尔巴哈，马克思，海德格尔，马尔库塞。我还读过托马斯潘恩联邦党人文集，常识，梭罗，惠特曼，' \
               '马克吐温，杰克伦敦，海明威老人与海，简奥斯丁，华滋华斯，狄更斯，猫，福尔摩斯，卡尔马克思，弗里德里希·恩格斯，拜伦，雪莱，' \
               '肖伯纳，培根，克伦威尔，约翰·洛克，托马斯·莫尔，亚当·斯密，李约瑟，阿诺德·汤因比，双城记，雾都孤儿，简爱' \
               '，鲁滨逊漂流记，汤显祖牧丹亭，南柯记，紫钗记，邯郸记，莎士比亚，威尼斯商人，仲夏夜之淫梦，罗密欧与朱丽叶，第十二夜，李尔王，' \
               '奥赛罗，麦克白，萨格尔王。'
    if '河南' in content:
        return '恁马列批，贺房伸圣？今儿个打的你乱窜靠恁娘！'
    if '海鲜批' in content:
        return "它有个海鲜批\n\当它去Lady M时，白带可以当吞拿酱\n\
  当它吃巧克力可颂时，可以拿牛角自慰 \n\当它吃火锅时，淫水可以当汤底  \n\
  老中医让它忌口，它却说不用忌批  \n\无论它是鲑鱼味批还是沙丁味批  \n\
  它可以发黑发霉，也可以是迪奭尼在逃鲱鱼批  \n\幸好，它有个海鲜批"
    if '荷兰' in content:
        return '靠恁娘，荷兰人没有好人坏人吗，我就是荷兰人，你真是马批活腻了我nèng死你个兔熊，你骂荷兰人，我逮住你，我逮住你马列批一jio踢恁娘肚里去马列批'
    if '中嘞' in content:
        return '这下忠咧！太忠咧！'
    if '广西' in content:
        return '贵州和广西相比⚡那我还是觉得我们广西牛批⚡'
    if '京人' in content:
        return '咱儿百儿京儿人儿可儿真儿是儿太儿高儿贵儿了儿您嘞！'
    if '猴' in content:
        return '有点像广西佬'
    if '看看' in content:
        return ' [看看牛牛](https://i.imgur.com/4b8eoDX.mp4)'
    if '原神' in content:
        return '老妈保佑，刚刚拿我妈支付宝冲了一发648，一发十连小保底中了钟离，我妈在昏迷中肯定也会开心的，相信她很快就会醒过来！'
    if '原批' in content:
        return '运气用完了，妈妈也走了。最后还是没抽到甘雨，一大遗憾。'
    if 'pc' in content:
        return '我有妹子送逼，我日过白的黄的黑的绿的红的蓝的紫的透明的'
    if '宇宙' in content:
        return '大海掀翻小池塘'
    if '神奈川' in content:
        return '神奈川冲浪里吧是我所见过最理智，最自由的地方。在这里，色欲被正视，失败也只是一种人生状态，' \
               '大家甚至尊重无良商贩，家徒四壁也不会成为交流障碍，每个人表现出如儿童般直白的索取欲。大家拒绝一切伪善，' \
               '相信伟大终究平凡，正视成功学的无用，大家知道奋斗和努力是比回避更低级的社会性遵从，是弱势者存活的借口。' \
               '而挣脱一切的第一步就是反其道而行之，' \
               '停留在时间与空间的夹缝，大家的不思进取是看透，大家的不学无术是反抗，毫无光彩的人生是沉默的接受，' \
               '下水道般的生活是为了更好的仰望星空。。。'
    if '开香槟' in content:
        return "\
         _*    *_       ||\n\
        |*|    |*|      ||\n\
        |_|    |_|     |  |\n\
        \*/    \*/     |__|\n\
         |      |      |  |\n\
        _|_    _|_     |__|"
    if '我叫王' in content:
        return '你好我叫王，我今年45岁，我是在美国出生和长大的华裔美国人，请你给我发一张你的照片吗？我想看看和谁聊天'
    if content.startswith('test'):
        return '理你一下'
    if 'good bot' in content:
        return 'bot麻了，bot需要牛牛，不是赞美'
    if 'bad bot' in content:
        return '确实挺尬的，终于有人说这一点了。 能看出来本sub想极力模仿隔壁bot的节目效果，可是mod又没混过抽象tv和' \
               '其他泛抽象圈，导致每次bot出现的地方都极其的尴尬，有一种东施效颦强行幽默的别扭感。还不如直接关了，真的不好笑！'
    if '叫啊' in content:
        return '來了來了'
    if '支' in content:
        return '一日为支，终生为支，世世代代为支，子子孙孙为支'
    return None

#     if message.content.startswith('支'):
#         await asyncio.sleep(1)
#         await message.channel.send('一日为支，终生为支，世世代代为支，子子孙孙为支。')
#         await asyncio.sleep(2.5)
#         await message.channel.send('支性是洗不掉的，哪怕1%的基因你也是一支。  '
#                                    '无论内支外支，近支远支，华支台支，和支韩支，你一使用方块字，或曾经使用，便支性难逃。  凡人皆有一死，支人何须生存。  '
#                                    '旧瓦雷利亚的后裔、安达尔人先民的女王、维斯特洛的统治者暨全境守护者、大草原多斯拉克人卡丽熙、不焚者、'
#                                    '弥林的女王、镣拷打破者、龙之母、阿斯塔波的解放者、罗伊拿人和先民的女王、龙石岛公主、屠城者、焦土女王、风暴'
#                                    '降生之丹妮莉絲·坦格利安，将君临这片黑暗的支性大陆、和支列岛、台支诸岛。  正义的大龙喷出烈焰， “看哪，”  '
#                                    '支性大陆、和支列岛、台支诸岛的女王、屠城者、焦土女王、风暴降生之丹妮莉絲·坦格利安高声道： “赏罚在我，我'
#                                    '必照各人的支性报应他屠灭他。我是阿拉法，我是俄梅戛；我是首先的，我是末后的；我是初，我是终。”')
#     if message.content.startswith('叫啊'):
#         await message.channel.send('來了來了')
#     if message.content.startswith('沒用'):
#         await message.channel.send('傻逼')
#     if message.content.startswith('nll'):
#         await message.channel.send('hzs')
#     if message.content.startswith('nxl'):
#         await message.channel.send('nbyx')
#     if message.content.startswith('bur'):
#         await message.channel.send('burr')
#     if message.content.startswith('gs'):
#         await message.channel.send('狗屎')
#     if message.content.startswith('x'):
#         await message.channel.send('mbyl')
#     if message.content.startswith('wsm'):
#         await message.channel.send('你問我 我倒要問問你')
#     if message.content.startswith('good bot'):
#         await message.channel.send('還真是')
#     elif message.content.startswith('bad bot'):
#         await message.channel.send('@' + message.author.name + ' 我去年買了個表')

#     if message.content.startswith('jnmj'):
#         await message.channel.send('就叫')
#     if message.content.startswith('m'):
#         await message.channel.send('mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
