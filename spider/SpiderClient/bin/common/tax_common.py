#coding:utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

tax_dict = {
"万荣":0.191,
"万象":0.207,
"万隆":0.203,
"三泽":0.08,
"上海":0.162,
"上特劳恩":0.13,
"下关":0.158,
"下龙湾":0.152,
"不伦瑞克":0.07,
"不来梅":0.07,
"东京":0.08,
"严岛":0.134,
"丹佛":0.123,
"丹吉尔":0.101,
"丽江":0.166,
"丽贝岛":0.177,
"乌得勒支":0.063,
"乌斯怀亚":0.023,
"乌斯马尔":0.197,
"乌普萨拉":0.12,
"乌镇":0.169,
"乌鲁瓦图":0.21,
"乐山":0.166,
"九寨沟":0.166,
"乞力马扎罗山国家公园":0.197,
"二世古":0.188,
"于尔维克":0.09,
"云顶高原":0.114,
"亚历山大港":0.249,
"亚喀巴":0.177,
"亚庇":0.133,
"亚拉山谷":0.1,
"亚特兰大":0.206,
"亚琛":0.066,
"亚眠":0.1,
"亚萨瓦":0.406,
"京畿道":0.145,
"京都":0.08,
"仁川":0.155,
"仙台":0.08,
"仙女港镇":0.1,
"仙本那":0.085,
"代尔夫特":0.06,
"以弗所":0.08,
"伊丘卡":0.1,
"伊东":0.189,
"伊丽莎白港":0.134,
"伊兹密尔":0.08,
"伊拉克利翁":0.135,
"伊斯坦布尔":0.08,
"伊柳塞拉岛":0.184,
"伊瓜苏市":0.06,
"伊瓜苏港":0.06,
"伊瓦尔":0.079,
"伊维萨岛":0.1,
"伊豆":0.189,
"伊豆大岛":0.181,
"伍珀塔尔":0.07,
"休斯敦":0.165,
"优胜美地国家公园":0.111,
"会安":0.15,
"会晒":0.177,
"伦敦":0.202,
"伦敦(加拿大)":0.131,
"伯尔尼":0.038,
"伯尼":0.1,
"伯明翰":0.2,
"但尼丁":0.15,
"佐渡岛":0.188,
"佐贺":0.173,
"佛朗茨约瑟夫":0.15,
"佛罗伦萨":0.1,
"佛里曼特尔岛":0.1,
"佩吉":0.141,
"佩特拉":0.163,
"俄克拉荷马城":0.135,
"停泊岛":0.102,
"克伦威尔":0.15,
"克利夫兰":0.156,
"克朗克里":0.1,
"克莱蒙费朗":0.1,
"克雷塔罗":0.195,
"克鲁姆洛夫":0.155,
"全州":0.122,
"八丹拜":0.21,
"兰斯":0.1,
"兰达岛":0.161,
"关岛":0.11,
"内夫谢希尔":0.08,
"内皮尔":0.15,
"内罗毕":0.188,
"冈山":0.149,
"冲绳":0.08,
"凤凰城":0.132,
"凯库拉":0.15,
"凯恩斯":0.1,
"凯瑟琳":0.1,
"凯鲁万":0.06,
"函馆":0.08,
"切什梅":0.08,
"列日":0.06,
"利兹":0.2,
"利物浦":0.193,
"别府":0.08,
"前桥":0.08,
"剑桥":0.189,
"加斯佩":0.181,
"加来":0.1,
"加特林堡":0.152,
"加的斯":0.1,
"加米施-帕腾基兴":0.08,
"加那利群岛":0.07,
"努沙岬":0.1,
"努沙杜瓦":0.207,
"劳托卡":0.254,
"劳特布龙嫩":0.038,
"勒物库森":0.072,
"勒芒":0.1,
"勒阿弗尔":0.1,
"北九州":0.163,
"北京":0.148,
"北碧":0.177,
"北雪平":0.12,
"匹兹堡":0.132,
"千叶":0.178,
"华欣":0.177,
"华沙":0.08,
"华盛顿":0.137,
"卑尔根":0.096,
"南京":0.166,
"南安普敦":0.2,
"南投":0.15,
"南锡":0.1,
"博德鲁姆":0.08,
"博洛尼亚":0.1,
"博讷":0.1,
"卡什":0.08,
"卡塔":0.184,
"卡尔加里":0.104,
"卡尔卡松":0.1,
"卡尔巴里":0.1,
"卡帕帕村":0.15,
"卡斯凯什":0.06,
"卡昂":0.1,
"卡梅尔":0.131,
"卡罗维发利":0.146,
"卡萨布兰卡":0.101,
"卡通巴":0.1,
"卡那封":0.1,
"卡门海滩":0.184,
"卢克索":0.244,
"卢加诺":0.042,
"卢塞恩":0.038,
"卢森堡":0.03,
"卧龙岗":0.1,
"印第安纳波利斯":0.152,
"古尔本":0.1,
"可爱岛":0.134,
"台东":0.15,
"台中":0.135,
"台北":0.15,
"台南":0.158,
"合艾":0.177,
"吉利群岛":0.209,
"吉拉尔顿":0.1,
"吉隆":0.1,
"吉隆坡":0.112,
"同里":0.155,
"名古屋":0.08,
"名护":0.181,
"吕瑟峡湾":0.098,
"和歌山":0.08,
"哈利法克斯":0.175,
"哈勒姆":0.063,
"哈尔施塔特":0.13,
"哈尼阿":0.135,
"哈斯特":0.15,
"哈马马特":0.06,
"哥伦布":0.175,
"哥德堡":0.12,
"哥本哈根":0.25,
"嘉义":0.15,
"因弗卡吉尔":0.15,
"因斯布鲁克":0.13,
"因特拉肯":0.038,
"图卢兹":0.1,
"图卢姆":0.188,
"图尔":0.1,
"图恩":0.039,
"图森":0.157,
"图莱亚尔":0.2,
"土伦":0.1,
"圣但尼":0.022,
"圣何塞":0.13,
"圣保罗":0.047,
"圣保罗·德·旺斯":0.103,
"圣克里斯托瓦尔-德拉斯卡萨斯":0.182,
"圣勒":0.022,
"圣吉尔莱班":0.022,
"圣地亚哥":0.123,
"圣地亚哥-德孔波斯特拉":0.1,
"圣埃蒂安":0.101,
"圣塔菲":0.154,
"圣塞瓦斯蒂安":0.1,
"圣安东尼奥":0.166,
"圣巴巴拉":0.135,
"圣沃尔夫冈":0.135,
"圣灵群岛":0.118,
"圣米格尔-德阿连德":0.186,
"圣约翰斯":0.179,
"圣荷西":0.142,
"圣诞岛":0.1,
"圣路易斯":0.154,
"圣路易斯奥比斯波":0.147,
"圣马力诺":0.03,
"圣马洛":0.1,
"坎卢普斯":0.15,
"坎帕拉":0.193,
"坎昆":0.188,
"坎莫尔":0.116,
"坦帕":0.116,
"坦恩":0.1,
"垦丁":0.15,
"埃佩尔奈":0.106,
"埃克斯茅斯":0.1,
"埃克苏马岛":0.17,
"埃兹":0.11,
"埃因霍温":0.063,
"埃尔恰尔顿":0.21,
"埃德峡湾":0.1,
"埃德蒙顿":0.1,
"埃斯佩兰斯":0.1,
"埃武拉":0.06,
"埃特勒塔":0.1,
"埃维昂莱班":0.105,
"基律纳":0.12,
"基洛纳":0.158,
"基督城":0.15,
"基隆":0.151,
"埼玉":0.08,
"堪培拉":0.1,
"堪萨斯城":0.167,
"塔拉戈纳":0.1,
"塔斯马尼亚岛":0.1,
"塔里法":0.091,
"塔韦乌尼":0.223,
"塔马兰":0.15,
"塞伦盖蒂国家公园":0.192,
"塞多纳":0.119,
"塞尔":0.1,
"塞戈维亚":0.1,
"塞班岛":0.15,
"塞维利亚":0.1,
"塞萨洛尼基":0.135,
"墨尔本":0.1,
"墨西哥城":0.192,
"夏威夷大岛":0.202,
"夏洛特":0.159,
"夏洛特敦":0.186,
"夕张":0.08,
"多伦多":0.214,
"多特蒙德":0.072,
"多瑙河畔克雷姆斯":0.13,
"多维尔":0.1,
"夜丰颂":0.174,
"夜功":0.177,
"大分":0.157,
"大加那利岛":0.07,
"大叻":0.152,
"大城":0.177,
"大峡谷国家公园":0.139,
"大峡谷村":0.103,
"大巴哈马岛":0.204,
"大津":0.08,
"大湾":0.15,
"大溪地":0.134,
"大烟山国家公园":0.127,
"大理":0.216,
"大田":0.165,
"大邱":0.153,
"大阪":0.08,
"奄美大岛":0.188,
"奇琴伊察":0.194,
"奈瓦沙":0.193,
"奈良":0.08,
"奥伦奇":0.1,
"奥兰":0.078,
"奥兰多":0.138,
"奥古斯塔港":0.1,
"奥古斯塔（西澳）":0.1,
"奥尔堡":0.25,
"奥尔良":0.1,
"奥斯汀":0.142,
"奥斯陆":0.101,
"奥朗日":0.1,
"奥格斯堡":0.072,
"奥洛穆茨":0.15,
"奥瓦卡":0.15,
"奥维耶多":0.1,
"奥胡斯":0.25,
"奥达":0.1,
"奥马鲁":0.15,
"女皇镇":0.1,
"妈妈拍丝瓜岛":0.146,
"姬路":0.141,
"威尼斯":0.104,
"威廉姆斯":0.117,
"婆罗浮屠":0.21,
"孔苏埃格拉":0.096,
"宇治":0.08,
"宇都宫氏":0.08,
"安东":0.148,
"安克雷奇":0.121,
"安博塞利":0.16,
"安卡拉":0.082,
"安塔利亚":0.084,
"安塔那那利佛":0.2,
"安曼":0.249,
"安特卫普":0.06,
"安纳西":0.1,
"安道尔城":0.05,
"宜兰":0.15,
"宜昌":0.166,
"宜野湾":0.08,
"室兰":0.185,
"宫古岛":0.19,
"宫崎":0.162,
"宿雾":0.213,
"富埃特文图拉岛":0.07,
"富士河口湖":0.188,
"富山":0.08,
"富良野":0.08,
"小樽":0.08,
"小石城":0.138,
"尚贝里":0.1,
"尤拉拉":0.1,
"尼亚加拉瀑布市":0.13,
"尼姆":0.1,
"尼尔森":0.15,
"尼斯":0.1,
"居德旺恩":0.08,
"山口":0.08,
"山形":0.08,
"山打根":0.117,
"岐阜":0.163,
"岘港":0.158,
"巴东":0.21,
"巴利洛切":0.21,
"巴利阿里群岛":0.1,
"巴厘岛.乌布":0.21,
"巴厘岛.库塔":0.21,
"巴厘岛.库布":0.21,
"巴厘岛.登巴萨":0.21,
"巴塞尔":0.044,
"巴塞罗那":0.1,
"巴奇勒":0.1,
"巴尔":0.1,
"巴尔的摩":0.138,
"巴德依舍":0.13,
"巴拉瑞特":0.1,
"巴斯":0.2,
"巴淡岛":0.208,
"巴港":0.091,
"巴瑟尔顿":0.1,
"巴登巴登":0.072,
"巴约":0.098,
"巴西利亚":0.068,
"巴里巴板":0.21,
"巴黎":0.101,
"布伦亨":0.15,
"布卢瓦":0.1,
"布宜诺斯艾利斯":0.219,
"布尔戈斯":0.101,
"布尔诺":0.152,
"布拉加":0.069,
"布拉夫":0.15,
"布拉格":0.15,
"布罗莫腾格里塞梅鲁国家公园":0.21,
"布达佩斯":0.193,
"布里恩茨":0.038,
"布里斯托尔":0.2,
"布里斯班":0.1,
"布雷根茨":0.13,
"布鲁塞尔":0.06,
"布鲁姆":0.1,
"布鲁日":0.06,
"帕伦克":0.185,
"帕劳":0.126,
"帕岸岛":0.177,
"帕罗斯":0.135,
"平溪":0.15,
"平遥":0.166,
"广岛":0.08,
"广州":0.15,
"庆州":0.133,
"库伯佩迪":0.1,
"库克山镇":0.15,
"库兰达":0.1,
"库努纳拉":0.1,
"库特纳霍拉":0.15,
"库萨达斯":0.08,
"库马":0.1,
"底特律":0.108,
"庞贝":0.1,
"康斯坦丁":0.072,
"康斯坦茨":0.07,
"廊开":0.205,
"开塞利":0.08,
"开普敦":0.075,
"开罗":0.234,
"弗拉格斯塔夫":0.124,
"弗雷德里克顿":0.167,
"弗雷斯诺":0.121,
"弘前":0.188,
"张家界":0.162,
"彭世洛":0.177,
"彭纳肖（袋鼠岛）":0.1,
"彰化":0.15,
"御殿场":0.166,
"德尔斐":0.135,
"德岛":0.15,
"德文港":0.097,
"德比":0.1,
"德班":0.139,
"德累斯顿":0.087,
"德纳姆":0.1,
"怀托莫溶洞":0.15,
"怡保":0.143,
"恩德培":0.193,
"恩戈罗恩戈罗火山口":0.188,
"恩纳":0.184,
"恰纳卡莱":0.08,
"悉尼":0.1,
"惠斯勒":0.15,
"惠灵顿":0.15,
"慕尼黑":0.07,
"成都":0.163,
"戛纳":0.1,
"扎金索斯":0.135,
"托尔坎":0.1,
"托泽尔":0.06,
"托莱多":0.1,
"拉哥斯":0.061,
"拉巴特":0.105,
"拉戈梅拉岛":0.069,
"拉斯维加斯":0.126,
"拉福图纳":0.13,
"拉科鲁尼亚":0.099,
"拉罗谢尔":0.1,
"拉萨":0.131,
"拉迪格岛":0.156,
"拜伦湾":0.104,
"拜县":0.177,
"拿骚":0.214,
"摇篮山":0.1,
"摩纳哥":0.1,
"敦刻尔克":0.093,
"文根":0.038,
"斯卡恩":0.25,
"斯图加特":0.07,
"斯塔万格":0.098,
"斯德哥尔摩":0.126,
"斯旺西":0.1,
"斯法克斯":0.06,
"斯特拉恩":0.1,
"斯特拉斯堡":0.1,
"斯特拉特福":0.2,
"斯蒂芬斯港":0.1,
"新加坡":0.174,
"新奥尔良":0.15,
"新山":0.135,
"新普利茅斯":0.15,
"新潟 ":0.169,
"新竹":0.14,
"施泰因":0.038,
"施瓦茨":0.13,
"日光":0.167,
"日内瓦":0.066,
"日惹":0.206,
"旧金山":0.14,
"旭川":0.08,
"昂布瓦斯":0.1,
"昂热":0.104,
"昂蒂布":0.103,
"昆卡":0.098,
"昆明":0.131,
"明尼阿波利斯":0.116,
"春川":0.116,
"春蓬":0.177,
"普吉岛":0.178,
"普埃布拉":0.161,
"普拉兰岛":0.156,
"普林斯顿":0.1,
"普瓦捷":0.1,
"普纳凯基":0.15,
"普罗旺斯地区艾克斯":0.1,
"普罗维登斯":0.121,
"暹粒":0.206,
"曼谷":0.175,
"朗塞斯顿":0.1,
"朗斯":0.1,
"朗里奇":0.1,
"木浦":0.118,
"本迪戈":0.1,
"札幌":0.08,
"朱家角":0.159,
"朱诺":0.124,
"杜兹":0.06,
"杜塞尔多夫":0.076,
"杜马盖地":0.167,
"束草":0.14,
"杨基":0.1,
"杰克逊":0.086,
"杰克逊维尔":0.127,
"杰姆":0.06,
"杰尔巴岛":0.062,
"松山":0.145,
"松本":0.172,
"松江":0.08,
"林肯港":0.1,
"林茨":0.13,
"林道":0.07,
"林雪平":0.12,
"柏林":0.1,
"根室":0.08,
"根特":0.062,
"格勒诺布尔":0.1,
"格拉斯":0.096,
"格拉斯哥":0.2,
"格拉纳达":0.1,
"格拉茨":0.13,
"格林德瓦":0.038,
"格林诺奇":0.15,
"格罗宁根":0.06,
"格里菲斯":0.1,
"格雷梅":0.08,
"格雷茅斯":0.15,
"桂林":0.113,
"桃园":0.141,
"桑坦德":0.1,
"桑给巴尔":0.196,
"梅克内斯":0.104,
"梅尔祖卡":0.108,
"梅里达":0.1,
"棉兰":0.21,
"棉花堡":0.08,
"棕榈泉":0.155,
"楠迪":0.254,
"槟城":0.15,
"横滨":0.08,
"檀香山":0.178,
"欧登塞":0.25,
"死海":0.208,
"比勒陀利亚":0.135,
"比尔森":0.15,
"比灵斯":0.092,
"比舍诺":0.1,
"比萨":0.101,
"比隆":0.25,
"比雷埃夫斯":0.135,
"毕尔巴鄂":0.1,
"毛伊岛":0.134,
"民丹岛":0.21,
"水原市":0.146,
"水户":0.08,
"水牛城":0.13,
"汉堡":0.073,
"汉密尔顿":0.133,
"汉密尔顿岛":0.1,
"汉诺威":0.07,
"江原道":0.122,
"江陵":0.122,
"汤斯维尔":0.1,
"沃加沃加":0.1,
"沃斯":0.095,
"沃韦":0.049,
"沙努尔":0.21,
"沙夫豪森":0.045,
"沙姆沙伊赫":0.25,
"沙捞越":0.124,
"沙美岛":0.177,
"河内":0.156,
"法兰克福":0.07,
"法鲁":0.06,
"泗水":0.207,
"波兹曼":0.085,
"波士顿":0.129,
"波尔图":0.07,
"波尔多":0.1,
"波恩":0.069,
"波拉克":0.1,
"波拉波拉":0.152,
"波普":0.18,
"波特兰":0.125,
"波特兰（缅因州）":0.093,
"波茨坦":0.1,
"波鸿":0.072,
"洛克汉普顿":0.1,
"洛夫特胡斯":0.1,
"洛杉矶":0.135,
"洛桑":0.041,
"洛阳":0.158,
"洞爷湖":0.08,
"津":0.08,
"津加":0.191,
"派希亚":0.15,
"济州市":0.104,
"海德堡":0.07,
"海牙":0.062,
"涛岛":0.177,
"淡路岛":0.127,
"清孔":0.177,
"清州":0.152,
"清盛":0.177,
"清莱":0.175,
"清迈":0.184,
"渥太华":0.22,
"温哥华":0.159,
"温尼伯":0.181,
"温彻斯特":0.2,
"温德米尔和波尼斯":0.2,
"温莎":0.2,
"潘普罗那":0.1,
"澎湖":0.15,
"澳大利亚蓝山":0.1,
"澳门":0.151,
"热浪岛":0.102,
"热海":0.199,
"热那亚":0.101,
"熊本":0.08,
"爱丁堡":0.2,
"爱丽丝泉":0.1,
"爱尔福特":0.07,
"爱昵岛":0.179,
"牛津":0.2,
"特内里费岛":0.07,
"特威泽尔":0.15,
"特罗姆瑟":0.108,
"特里尔":0.063,
"特鲁瓦":0.1,
"猴子美亚":0.1,
"玛塔玛塔":0.15,
"玛格丽特河":0.1,
"玛玛努卡群岛":0.254,
"珀斯":0.1,
"珊瑚湾":0.1,
"班伯里":0.1,
"班夫":0.117,
"琅勃拉邦":0.21,
"琉球":0.15,
"瓜拉登嘉楼":0.131,
"瓜达拉哈拉":0.186,
"瓦伦西亚":0.11,
"瓦努阿岛":0.224,
"瓦南布尔":0.1,
"瓦哈卡":0.189,
"瓦尔扎扎特":0.102,
"瓦朗索尔":0.1,
"瓦纳卡":0.15,
"瓦迪拉姆":0.149,
"由布":0.08,
"甲米":0.18,
"登别":0.08,
"登马克":0.1,
"白川乡":0.186,
"皇后镇":0.15,
"皮亚琴察":0.1,
"皮克顿":0.15,
"皮皮岛":0.178,
"盐湖城":0.131,
"盖朗厄尔":0.1,
"盛冈":0.08,
"知床":0.191,
"石垣岛":0.183,
"神户":0.08,
"福井":0.08,
"福伦丹":0.063,
"福克斯冰川":0.15,
"福冈":0.08,
"福岛":0.178,
"福森":0.075,
"秋田":0.08,
"种子岛":0.188,
"科尔多瓦":0.1,
"科尔斯贝":0.1,
"科尔马":0.1,
"科布伦茨":0.07,
"科斯湾":0.1,
"科罗拉多斯普林":0.103,
"科罗曼德":0.15,
"科苏梅尔岛":0.179,
"科英布拉":0.061,
"科西嘉":0.021,
"科隆":0.072,
"稚内":0.187,
"穆尔西亚":0.1,
"穆龙达瓦":0.2,
"突尼斯城":0.064,
"第戎":0.1,
"箭镇":0.15,
"箱根":0.08,
"米伦小镇":0.038,
"米兰":0.1,
"米哈斯":0.1,
"米尔迪拉":0.1,
"米达尔":0.09,
"素可泰":0.177,
"素叻他尼":0.177,
"索伟拉":0.103,
"索尔兹伯里":0.2,
"约克":0.2,
"约翰内斯堡":0.114,
"纳什维尔":0.185,
"纳夫普利奥":0.135,
"纳尔逊贝":0.1,
"纳帕谷":0.155,
"纳库拉":0.406,
"纳库鲁":0.204,
"纹别":0.189,
"纽伦堡":0.07,
"纽卡斯尔":0.204,
"纽曼":0.1,
"纽约":0.188,
"纽黑文":0.15,
"维也纳":0.16,
"维多利亚市":0.138,
"维尔茨堡":0.07,
"维戈":0.097,
"维琴察":0.101,
"维罗纳":0.101,
"绿岛":0.15,
"网走":0.182,
"罗威纳":0.207,
"罗德岛":0.135,
"罗德岱尔堡":0.122,
"罗托鲁阿":0.15,
"罗斯基勒":0.25,
"罗斯小镇":0.1,
"罗滕堡":0.07,
"罗萨里奥":0.208,
"罗马":0.111,
"羊角村":0.06,
"美因茨":0.07,
"美奈":0.156,
"美瑛":0.08,
"耶拿":0.081,
"耶罗岛":0.07,
"肯尼亚山国家公园":0.207,
"胡尔格达":0.272,
"胡志明市":0.155,
"舍农索":0.1,
"舍夫沙万":0.1,
"艾于兰":0.095,
"艾尔利海滩":0.118,
"芝加哥":0.143,
"芭提雅":0.177,
"花卷":0.166,
"花莲":0.15,
"芽庄":0.151,
"苏伊士":0.266,
"苏厄德":0.077,
"苏塞":0.062,
"苏州":0.166,
"苏梅岛":0.178,
"苏瓦":0.255,
"苏黎世":0.038,
"苗栗":0.131,
"英格堡":0.038,
"莫阿布":0.141,
"莫雷阿":0.134,
"莱昂":0.099,
"莱比锡":0.07,
"莱顿":0.06,
"萨克拉门托":0.132,
"萨尔塔":0.21,
"萨尔瓦多":0.047,
"萨尔茨堡":0.13,
"萨拉戈萨":0.099,
"萨斯克通":0.114,
"萨武萨武":0.224,
"落基山国家公园":0.133,
"蒂华纳":0.152,
"蒂卡普湖":0.15,
"蒂阿瑙":0.15,
"蒂马鲁":0.15,
"蒙克顿":0.151,
"蒙巴萨":0.181,
"蒙彼利埃":0.1,
"蒙特利尔":0.177,
"蒙特勒":0.053,
"蒙特雷":0.128,
"蒙特韦尔德":0.13,
"蓝梦岛":0.21,
"蓝湾":0.15,
"蔚山":0.132,
"薄荷岛":0.145,
"藤南特克里克":0.1,
"袋鼠岛":0.1,
"西哈努克市":0.209,
"西归浦":0.11,
"西戴":0.084,
"西礁岛":0.133,
"西表岛":0.183,
"西雅图":0.134,
"西黄石":0.102,
"设菲尔德":0.1,
"诺丁汉":0.2,
"谢伯顿":0.1,
"贝尔法斯特":0.2,
"贝希特斯加登":0.11,
"贝桑松":0.1,
"贡布":0.207,
"费城":0.14,
"费尔班克斯":0.084,
"费拉":0.135,
"费特希耶":0.08,
"贺思盖":0.1,
"贾府":0.08,
"贾斯珀":0.116,
"赛尔丘克":0.08,
"赫尔辛基":0.1,
"赫尔辛堡":0.162,
"赫尔辛格":0.167,
"赫维湾":0.1,
"赫罗纳":0.1,
"路易港":0.15,
"轻井泽":0.187,
"辛加东卡":0.24,
"辛特拉":0.06,
"辛辛那提":0.145,
"达哈卜":0.15,
"达喀尔":0.1,
"达尔文":0.1,
"达累斯萨拉姆":0.183,
"迈阿密":0.177,
"道格拉斯港":0.1,
"那不勒斯":0.1,
"那慕尔":0.061,
"那霸":0.08,
"都江堰":0.155,
"都灵":0.106,
"采尔马特":0.038,
"里士满":0.1,
"里奥加耶戈斯":0.21,
"里尔":0.1,
"里斯本":0.06,
"里昂":0.1,
"里约热内卢":0.095,
"重庆":0.166,
"金巴兰":0.21,
"金斯顿":0.134,
"金泽":0.159,
"金边":0.204,
"金门":0.158,
"金马伦高地":0.148,
"釜山":0.164,
"钏路":0.172,
"锡卢埃特岛":0.159,
"锡拉奥":0.022,
"锡耶纳":0.1,
"镰仓":0.08,
"长崎":0.08,
"长滩岛":0.149,
"长野":0.184,
"门兴格拉德巴赫":0.075,
"门多萨":0.197,
"阳光海岸":0.1,
"阳朔":0.166,
"阿伯德尔国家公园":0.215,
"阿克萨赖":0.08,
"阿利坎特":0.1,
"阿卡罗阿":0.15,
"阿卡雄":0.1,
"阿姆斯特丹":0.063,
"阿威罗":0.061,
"阿尔伯克基":0.129,
"阿尔勒":0.1,
"阿尔及尔":0.078,
"阿布辛贝":0.14,
"阿德雷德":0.1,
"阿斯旺":0.264,
"阿比斯库":0.12,
"阿波罗小镇":0.1,
"阿瓦诺斯":0.08,
"阿纳姆":0.064,
"阿维尼翁":0.101,
"阿维拉":0.1,
"阿马尔菲":0.1,
"阿鲁沙":0.183,
"陶朗阿":0.15,
"陶波":0.15,
"隆德":0.124,
"雅典":0.135,
"雅加达":0.205,
"雪城":0.126,
"雷克雅未克":0.114,
"雷恩":0.1,
"霍基蒂卡":0.15,
"霍尔斯克里克":0.1,
"霍巴特":0.1,
"霍芬海姆":0.07,
"霍默":0.069,
"青森":0.08,
"静冈":0.184,
"非斯":0.095,
"顺化":0.155,
"首尔":0.186,
"香格里拉":0.166,
"香港":0.109,
"马六甲":0.145,
"马埃岛":0.155,
"马尔代夫（全区）":0.201,
"马尔肯":0.064,
"马尔默":0.155,
"马尼拉":0.155,
"马布岛":0.085,
"马德普拉塔":0.21,
"马德望":0.205,
"马德里":0.1,
"马拉加":0.1,
"马拉喀什":0.1,
"马斯特里赫特":0.06,
"马特鲁":0.266,
"马瑙斯":0.027,
"马略卡岛":0.107,
"马累":0.199,
"马诺斯克":0.1,
"马赛":0.101,
"马赛马拉国家保护区":0.204,
"高山":0.163,
"高松":0.149,
"高知":0.111,
"高雄":0.15,
"魁北克市":0.179,
"鲁尔蒙德":0.063,
"鲁汶":0.06,
"鲁法克":0.1,
"鸟取":0.08,
"鹿儿岛":0.08,
"鹿特丹":0.063,
"麦克夸利湾":0.1,
"麦凯":0.1,
"麦迪逊":0.131,
"黄刀镇":0.053,
"黄山":0.166,
"黄石国家公园":0.113,
"黄金海岸":0.1,
"黄金湾":0.15,
"黑得兰港":0.1,
"龙恩":0.1,
"龙目岛":0.21,
"龙胜":0.166,
"龙达":0.1
}