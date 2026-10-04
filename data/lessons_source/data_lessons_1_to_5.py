# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn cho Bài 1 đến Bài 5 - HSK 3 Standard Course
"""

LESSONS_1_TO_5 = [
    # ==================== BÀI 1 ====================
    {
        "id": 1,
        "title_zh": "周末你有什么打算？",
        "title_py": "Zhōumò nǐ yǒu shénme dǎsuàn?",
        "title_vi": "Cuối tuần bạn có dự định gì?",
        "dialogues": [
            {
                "title": "Đoạn 1: 谈周末的打算 (Nói về dự định cuối tuần)",
                "location": "在学校 / 在谈话",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "周末你有什么打算？", "py": "Zhōumò nǐ yǒu shénme dǎsuàn?", "vi": "Cuối tuần cậu có dự định gì không?"},
                    {"speaker": "小丽", "role": "female", "zh": "我早就想好了，请你吃饭，看电影，喝咖啡。", "py": "Wǒ zǎojiù xiǎnghǎo le, qǐng nǐ chī fàn, kàn diànyǐng, hē kāfēi.", "vi": "Mình đã tính từ sớm rồi: mời cậu đi ăn cơm, xem phim, uống cà phê."},
                    {"speaker": "小刚", "role": "male", "zh": "请我？", "py": "Qǐng wǒ?", "vi": "Mời mình á?"},
                    {"speaker": "小丽", "role": "female", "zh": "是啊，我已经找好饭馆了，电影票也买好了。", "py": "Shì a, wǒ yǐjīng zhǎohǎo fànguǎn le, diànyǐngpiào yě mǎihǎo le.", "vi": "Đúng vậy, mình đã chọn quán ăn xong rồi, vé xem phim cũng mua xong rồi."},
                    {"speaker": "小刚", "role": "male", "zh": "我还没想好要不要跟你去呢。", "py": "Wǒ hái méi xiǎnghǎo yào bu yào gēn nǐ qù ne.", "vi": "Mình thì còn chưa nghĩ kỹ có nên đi với cậu không đây."}
                ]
            },
            {
                "title": "Đoạn 2: 在家 (Ở nhà)",
                "location": "在家",
                "lines": [
                    {"speaker": "妈妈", "role": "female", "zh": "你一直玩儿电脑游戏，作业写完了吗？", "py": "Nǐ yìzhí wánr diànnǎo yóuxì, zuòyè xiěwán le ma?", "vi": "Con cứ chơi game máy tính suốt, bài tập làm xong chưa?"},
                    {"speaker": "儿子", "role": "male", "zh": "都写完了。", "py": "Dōu xiěwán le.", "vi": "Con làm xong hết rồi ạ."},
                    {"speaker": "妈妈", "role": "female", "zh": "明天不是有考试吗？你怎么一点儿也不着急？", "py": "Míngtiān bú shì yǒu kǎoshì ma? Nǐ zěnme yìdiǎnr yě bù zháojí?", "vi": "Mai chẳng phải có bài kiểm tra sao? Sao con chẳng thấy sốt ruột tí nào thế?"},
                    {"speaker": "儿子", "role": "male", "zh": "我早就复习好了。", "py": "Wǒ zǎojiù fùxíhǎo le.", "vi": "Con đã ôn tập xong từ sớm rồi mà mẹ."},
                    {"speaker": "妈妈", "role": "female", "zh": "那也不能一直玩儿啊。", "py": "Nà yě bù néng yìzhí wánr a.", "vi": "Thế thì cũng không thể cứ chơi suốt như vậy chứ."}
                ]
            },
            {
                "title": "Đoạn 3: 聊旅游计划 (Nói về kế hoạch du lịch)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "下个月我去旅游，你能跟我一起去吗？", "py": "Xià ge yuè wǒ qù lǚyóu, nǐ néng gēn wǒ yìqǐ qù ma?", "vi": "Tháng sau mình đi du lịch, cậu có thể đi cùng mình không?"},
                    {"speaker": "小丽", "role": "female", "zh": "我还没想好呢。你觉得哪儿最好玩儿？", "py": "Wǒ hái méi xiǎnghǎo ne. Nǐ juéde nǎr zuì hǎowánr?", "vi": "Mình còn chưa nghĩ xong. Cậu thấy nơi nào vui nhất?"},
                    {"speaker": "小刚", "role": "male", "zh": "南方啊，我们去南方旅游吧，我们去爬山。", "py": "Nánfāng a, wǒmen qù nánfāng lǚyóu ba, wǒmen qù páshān.", "vi": "Miền Nam đó, chúng mình đi miền Nam du lịch đi, chúng mình đi leo núi."},
                    {"speaker": "小丽", "role": "female", "zh": "好啊，那我们带什么呢？", "py": "Hǎo a, nà wǒmen dài shénme ne?", "vi": "Được thôi, vậy chúng ta đem theo những gì?"},
                    {"speaker": "小刚", "role": "male", "zh": "水果、面包、茶，都带上。", "py": "Shuǐguǒ, miànbāo, chá, dōu dàishang.", "vi": "Trái cây, bánh mì, trà, mang theo hết nhé."}
                ]
            },
            {
                "title": "Đoạn 4: 准备出发 (Chuẩn bị xuất phát)",
                "location": "在收拾行李",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "水果、面包、茶都准备好了，我们还带什么？", "py": "Shuǐguǒ, miànbāo, chá dōu zhǔnbèihǎo le, wǒmen hái dài shénme?", "vi": "Hoa quả, bánh mì, trà đều đã chuẩn bị xong rồi, chúng ta còn đem theo gì nữa không?"},
                    {"speaker": "小刚", "role": "male", "zh": "手机、电脑、地图，一个也不能少。", "py": "Shǒujī, diànnǎo, dìtú, yí ge yě bù néng shǎo.", "vi": "Điện thoại, máy tính, bản đồ, một thứ cũng không thể thiếu."},
                    {"speaker": "小丽", "role": "female", "zh": "这些我昨天下午就准备好了。", "py": "Zhèxiē wǒ zuótiān xiàwǔ jiù zhǔnbèihǎo le.", "vi": "Mấy thứ này chiều hôm qua em đã chuẩn bị xong rồi."},
                    {"speaker": "小刚", "role": "male", "zh": "再多带几件衣服吧。", "py": "Zài duō dài jǐ jiàn yīfu ba.", "vi": "Đem thêm vài bộ quần áo nữa đi."},
                    {"speaker": "小丽", "role": "female", "zh": "我们是去旅游，不是搬家，还是少带一些吧。", "py": "Wǒmen shì qù lǚyóu, bú shì bānjiā, háishì shǎo dài yìxiē ba.", "vi": "Chúng mình là đi du lịch chứ đâu phải chuyển nhà, tốt nhất mang ít thôi."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "match_pic",
                "audio_script": "男：你怎么又不高兴了？ 女：你工作一直忙，一次电影都没跟我一起看过。",
                "question": "Nghe đoạn thoại, chọn bức tranh thích hợp nhất:",
                "options": ["A. Chuyển nhà (搬家)", "B. Mua bánh mì (买面包)", "C. Xem phim giận dỗi (看电影)", "D. Leo núi (爬山)"],
                "ans": "C",
                "explain": "Cô gái phàn nàn bạn nam lúc nào cũng bận, chưa từng cùng cô đi xem phim lần nào."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "下个星期就要考试了，小明每天都复习到很晚，一点儿也不着急。",
                "question": "Phán đoán đúng hay sai: 小明一点儿也不着急。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Đoạn văn nói Tiểu Minh học tới khuya mỗi ngày nên câu phán đoán không vội là không phù hợp với ngữ cảnh thực tế."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：明天去旅游的东西你准备好了吗？ 男：早就准备好了，面包、水果和水都带了。",
                "question": "男的准备了什么？",
                "options": ["A. 电脑和手机", "B. 面包、水果和水", "C. 地图和衣服"],
                "ans": "B",
                "explain": "Người nam trả lời: 面包、水果和水都带了."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "男：你打算什么时候搬家？ 女：我想下个周末搬，你有时间帮我吗？",
                "question": "女的打算什么时候搬家？",
                "options": ["A. 今天下午", "B. 明天早上", "C. 下个周末"],
                "ans": "C",
                "explain": "Người nữ nói: 我想下个周末搬."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "不是，我一直在这家医院工作。", "py": "Bú shì, wǒ yìzhí zài zhè jiā yīyuàn gōngzuò.", "vi": "Không phải, tôi vẫn luôn làm việc ở bệnh viện này."},
                {"id": "B", "text": "对不起，周老师现在不在。", "py": "Duìbuqǐ, Zhōu lǎoshī xiànzài bú zài.", "vi": "Xin lỗi, thầy Chu hiện tại không có ở đây."},
                {"id": "C", "text": "今天学校里一个人都没有，大家都去哪儿了？", "py": "Jīntiān xuéxiào li yí ge rén dōu méiyǒu, dàjiā dōu qù nǎr le?", "vi": "Hôm nay trong trường một người cũng không có, mọi người đi đâu hết rồi?"},
                {"id": "D", "text": "周末有时间吗？我打算请你吃个饭。", "py": "Zhōumò yǒu shíjiān ma? Wǒ dǎsuàn qǐng nǐ chī ge fàn.", "vi": "Cuối tuần có thời gian rảnh không? Mình định mời cậu đi ăn bữa cơm."},
                {"id": "E", "text": "可能是工作太累，生病了。", "py": "Kěnéng shì gōngzuò tài lèi, shēngbìng le.", "vi": "Có lẽ là do công việc quá mệt, nên bị ốm rồi."}
            ],
            "questions": [
                {"num": 21, "text": "你怎么了？今天一点儿东西都没吃。", "py": "Nǐ zěnme le? Jīntiān yìdiǎnr dōngxi dōu méi chī.", "vi": "Cậu sao thế? Hôm nay chẳng ăn chút đồ gì cả.", "ans": "E", "explain": "Đáp lại lý do không ăn gì là vì làm việc mệt quá, bị ốm rồi."},
                {"num": 22, "text": "今天是周末，你去学校做什么？", "py": "Jīntiān shì zhōumò, nǐ qù xuéxiào zuò shénme?", "vi": "Hôm nay là cuối tuần, cậu đến trường làm gì vậy?", "ans": "C", "explain": "Đến trường thấy vắng tanh nên thắc mắc mọi người đi đâu."},
                {"num": 23, "text": "好啊，哪天？", "py": "Hǎo a, nǎ tiān?", "vi": "Được thôi, hôm nào thế?", "ans": "D", "explain": "Đồng ý với lời mời ăn cơm cuối tuần."},
                {"num": 24, "text": "你是新来的医生吗？", "py": "Nǐ shì xīn lái de yīshēng ma?", "vi": "Bạn là bác sĩ mới đến à?", "ans": "A", "explain": "Bác sĩ phủ định và nói đã làm ở đây suốt."},
                {"num": 25, "text": "那我明天再来吧，谢谢。", "py": "Nà wǒ míngtiān zài lái ba, xièxie.", "vi": "Vậy ngày mai tôi lại đến nhé, cảm ơn.", "ans": "B", "explain": "Vì thầy Chu không có ở đây nên hẹn mai lại đến."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "一直", "py": "yìzhí", "vi": "luôn luôn, suốt"},
                {"id": "B", "zh": "周末", "py": "zhōumò", "vi": "cuối tuần"},
                {"id": "C", "zh": "带", "py": "dài", "vi": "mang theo, đem theo"},
                {"id": "D", "zh": "搬", "py": "bān", "vi": "dọn, dời, chuyển"},
                {"id": "E", "zh": "面包", "py": "miànbāo", "vi": "bánh mì"}
            ],
            "questions": [
                {"num": 26, "prefix": "这个", "suffix": "你打算做什么？", "py": "Zhège ( ? ) nǐ dǎsuàn zuò shénme?", "vi": "( ? ) này bạn dự định làm gì?", "ans": "B", "word": "周末", "explain": "Cụm từ: 这个周末 (cuối tuần này)."},
                {"num": 27, "prefix": "你别", "suffix": "玩电脑游戏了，快写作业吧。", "py": "Nǐ bié ( ? ) wán diànnǎo yóuxì le, kuài xiě zuòyè ba.", "vi": "Con đừng chơi game máy tính ( ? ) nữa, mau làm bài tập đi.", "ans": "A", "word": "一直", "explain": "一直玩: cứ chơi suốt."},
                {"num": 28, "prefix": "外面下雨了，你出门记得", "suffix": "雨伞。", "py": "Wàimiàn xiàyǔ le, nǐ chūmén jìde ( ? ) yǔsǎn.", "vi": "Bên ngoài trời mưa rồi, con ra ngoài nhớ ( ? ) ô nhé.", "ans": "C", "word": "带", "explain": "带雨伞: mang theo ô."},
                {"num": 29, "prefix": "下个月我们要", "suffix": "家了。", "py": "Xià ge yuè wǒmen yào ( ? ) jiā le.", "vi": "Tháng sau chúng tôi sắp ( ? ) nhà rồi.", "ans": "D", "word": "搬", "explain": "搬家: chuyển nhà."},
                {"num": 30, "prefix": "早上我只吃了一块", "suffix": "，喝了一杯牛奶。", "py": "Zǎoshang wǒ zhǐ chī le yí kuài ( ? ), hē le yì bēi niúnǎi.", "vi": "Buổi sáng tôi chỉ ăn một miếng ( ? ), uống một ly sữa.", "ans": "E", "word": "面包", "explain": "吃面包: ăn bánh mì."}
            ]
        },
        "reading_p3": {
            "passage_zh": "小刚和小丽下个月打算去南方旅游。小刚想去爬山，所以准备带很多东西：面包、水果、茶、电脑和地图。但是小丽觉得带太多东西太累了，因为他们是去旅游，不是搬家。小丽觉得带几件衣服、手机和一点儿吃的就可以了。",
            "passage_py": "Xiǎogāng hé Xiǎolì xià ge yuè dǎsuàn qù nánfāng lǚyóu. Xiǎogāng xiǎng qù páshān, suǒyǐ zhǔnbèi dài hěn duō dōngxi: miànbāo, shuǐguǒ, chá, diànnǎo hé dìtú. Dànshì Xiǎolì juéde dài tài duō dōngxi tài lèi le, yīnwèi tāmen shì qù lǚyóu, bú shì bānjiā. Xiǎolì juéde dài jǐ jiàn yīfu, shǒujī hé yìdiǎnr chī de jiù kěyǐ le.",
            "passage_vi": "Tiểu Cương và Tiểu Lệ tháng sau dự định đi miền Nam du lịch. Tiểu Cương muốn đi leo núi, nên chuẩn bị mang rất nhiều thứ: bánh mì, hoa quả, trà, máy tính và bản đồ. Nhưng Tiểu Lệ cảm thấy mang quá nhiều đồ sẽ rất mệt, bởi vì họ là đi du lịch chứ không phải chuyển nhà. Tiểu Lệ cho rằng mang vài bộ quần áo, điện thoại và chút đồ ăn là được rồi.",
            "questions": [
                {
                    "num": 31,
                    "text": "小刚和小丽打算什么时候去旅游？",
                    "options": ["A. 这个周末", "B. 下个月", "C. 明天"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小刚和小丽下个月打算去南方旅游."
                },
                {
                    "num": 32,
                    "text": "他们打算去哪儿旅游？",
                    "options": ["A. 北方", "B. 南方", "C. 外国"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 去南方旅游."
                },
                {
                    "num": 33,
                    "text": "小刚为什么想带很多东西？",
                    "options": ["A. 他要去搬家", "B. 他想去爬山", "C. 他要送给朋友"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小刚想去爬山，所以准备带很多东西."
                },
                {
                    "num": 34,
                    "text": "小丽觉得带很多东西怎么样？",
                    "options": ["A. 很有用", "B. 太累了", "C. 很好玩儿"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小丽觉得带太多东西太累了."
                },
                {
                    "num": 35,
                    "text": "根据这段话，可以知道什么？",
                    "options": ["A. 他们是去搬家", "B. 小丽不想带电脑", "C. 小刚不想去旅游"],
                    "ans": "B",
                    "explain": "Tiểu Lệ cho rằng chỉ cần mang quần áo, điện thoại và đồ ăn, không muốn mang đồ cồng kềnh như máy tính."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["写完了", "作业", "我", "都"],
                "ans": "我都写完了作业。",
                "py": "Wǒ dōu xiěwán le zuòyè.",
                "vi": "Tôi đã làm xong hết bài tập rồi."
            },
            {
                "num": 37,
                "chunks": ["一点儿", "他不", "也", "着急"],
                "ans": "他一点儿也不着急。",
                "py": "Tā yìdiǎnr yě bù zháojí.",
                "vi": "Anh ấy một chút cũng không sốt ruột."
            },
            {
                "num": 38,
                "chunks": ["买好了", "电影票", "已经", "我"],
                "ans": "我已经买好电影票了。",
                "py": "Wǒ yǐjīng mǎihǎo diànyǐngpiào le.",
                "vi": "Tôi đã mua xong vé xem phim rồi."
            },
            {
                "num": 39,
                "chunks": ["打算", "去", "我们", "旅游", "南方"],
                "ans": "我们打算去南方旅游。",
                "py": "Wǒmen dǎsuàn qù nánfāng lǚyóu.",
                "vi": "Chúng tôi dự định đi du lịch miền Nam."
            },
            {
                "num": 40,
                "chunks": ["一个苹果", "没吃", "也", "他"],
                "ans": "他一个苹果也没吃。",
                "py": "Tā yí ge píngguǒ yě méi chī.",
                "vi": "Anh ấy một quả táo cũng không ăn."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "这个 (zhōumò) 你有什么打算？",
                "pinyin": "zhōumò",
                "ans": "周末",
                "vi": "Cuối tuần này bạn có dự định gì?"
            },
            {
                "num": 42,
                "sentence": "妈妈，今天晚上吃 (miànbāo) 吗？",
                "pinyin": "miànbāo",
                "ans": "面包",
                "vi": "Mẹ ơi, tối nay ăn bánh mì ạ?"
            },
            {
                "num": 43,
                "sentence": "去旅游别忘了 (dài) 地图。",
                "pinyin": "dài",
                "ans": "带",
                "vi": "Đi du lịch đừng quên mang theo bản đồ."
            },
            {
                "num": 44,
                "sentence": "下个月朋友要 (bān) 家了。",
                "pinyin": "bān",
                "ans": "搬",
                "vi": "Tháng sau bạn tôi sắp chuyển nhà rồi."
            },
            {
                "num": 45,
                "sentence": "明天的考试我已经 (fùxí) 好了。",
                "pinyin": "fùxí",
                "ans": "复习",
                "vi": "Bài thi ngày mai tôi đã ôn tập xong rồi."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "周末", "py": "zhōumò", "pos": "danh từ", "vi": "cuối tuần", "eg": "这个周末你打算做什么？"},
            {"num": 2, "zh": "打算", "py": "dǎsuàn", "pos": "động từ/danh từ", "vi": "kế hoạch; dự định", "eg": "我打算请你吃个饭。"},
            {"num": 3, "zh": "啊", "py": "a", "pos": "trợ từ", "vi": "a, hả, nhé", "eg": "好啊，我们一起去吧！"},
            {"num": 4, "zh": "跟", "py": "gēn", "pos": "giới từ", "vi": "cùng, với", "eg": "你能跟我一起去吗？"},
            {"num": 5, "zh": "一直", "py": "yìzhí", "pos": "phó từ", "vi": "suốt, liên tục, luôn", "eg": "他一直在玩电脑游戏。"},
            {"num": 6, "zh": "游戏", "py": "yóuxì", "pos": "danh từ", "vi": "trò chơi, game", "eg": "作业写完了才能玩游戏。"},
            {"num": 7, "zh": "作业", "py": "zuòyè", "pos": "danh từ", "vi": "bài tập về nhà", "eg": "今天的作业你写完了吗？"},
            {"num": 8, "zh": "着急", "py": "zháojí", "pos": "tính từ", "vi": "lo lắng, sốt ruột", "eg": "别着急，时间还早呢。"},
            {"num": 9, "zh": "复习", "py": "fùxí", "pos": "động từ", "vi": "ôn tập", "eg": "明天考试，今天得好好复习。"},
            {"num": 10, "zh": "南方", "py": "nánfāng", "pos": "danh từ", "vi": "phía nam, miền nam", "eg": "南方冬天的天气不太冷。"},
            {"num": 11, "zh": "北方", "py": "běifāng", "pos": "danh từ", "vi": "phía bắc, miền bắc", "eg": "北方冬天经常下雪。"},
            {"num": 12, "zh": "面包", "py": "miànbāo", "pos": "danh từ", "vi": "bánh mì", "eg": "早上我吃了一块面包。"},
            {"num": 13, "zh": "带", "py": "dài", "pos": "động từ", "vi": "mang theo, đem theo", "eg": "出门记得带钥匙和雨伞。"},
            {"num": 14, "zh": "地图", "py": "dìtú", "pos": "danh từ", "vi": "bản đồ", "eg": "手机上有中国电子地图。"},
            {"num": 15, "zh": "搬", "py": "bān", "pos": "động từ", "vi": "chuyển, dời", "eg": "下星期我们就要搬家了。"}
        ],
        "proper_nouns": [
            {"zh": "小丽", "py": "Xiǎolì", "vi": "Tiểu Lệ (tên riêng)"},
            {"zh": "小刚", "py": "Xiǎogāng", "vi": "Tiểu Cương (tên riêng)"}
        ],
        "grammar": [
            {
                "title": "1. Bổ ngữ kết quả “好” (结果补语 “好”)",
                "desc": "Bổ ngữ kết quả “好” đặt sau động từ biểu thị hành động đã hoàn thành tốt đẹp, thỏa đáng và người nói cảm thấy hài lòng. Cấu trúc phủ định dùng “没(有) + Động từ + 好”.",
                "examples": [
                    {"zh": "今晚的电影票小刚已经买好了。", "py": "Jīnwǎn de diànyǐngpiào Xiǎogāng yǐjīng mǎihǎo le.", "vi": "Vé xem phim tối nay Tiểu Cương đã mua xong xuôi rồi."},
                    {"zh": "饭还没做好，请你等一会儿。", "py": "Fàn hái méi zuòhǎo, qǐng nǐ děng yíhuìr.", "vi": "Cơm vẫn chưa nấu xong, xin bạn đợi một lát."},
                    {"zh": "去旅游的东西你都准备好了吗？", "py": "Qù lǚyóu de dōngxi nǐ dōu zhǔnbèihǎo le ma?", "vi": "Đồ đạc đi du lịch bạn đã chuẩn bị xong cả chưa?"}
                ]
            },
            {
                "title": "2. Cấu trúc phủ định tuyệt đối: “一……也/都 + 不/没……”",
                "desc": "Dùng để nhấn mạnh sự phủ định hoàn toàn. Cấu trúc: 'Chủ ngữ + 一 + Lượng từ + Danh từ + 也/都 + 不/没 + Vị ngữ'. Khi danh từ không đếm được hoặc tính từ, dùng '一点儿 + 也/都 + 不/没'.",
                "examples": [
                    {"zh": "我一个苹果也不想吃。", "py": "Wǒ yí ge píngguǒ yě bù xiǎng chī.", "vi": "Tôi một quả táo cũng không muốn ăn."},
                    {"zh": "昨天他一件衣服都没买。", "py": "Zuótiān tā yí jiàn yīfu dōu méi mǎi.", "vi": "Hôm qua anh ấy một bộ quần áo cũng không mua."},
                    {"zh": "你怎么一点儿也不着急？", "py": "Nǐ zěnme yìdiǎnr yě bù zháojí?", "vi": "Sao bạn một chút cũng không thấy sốt ruột thế?"}
                ]
            },
            {
                "title": "3. Liên từ “那” (连词 “那”)",
                "desc": "Liên từ “那” đặt ở đầu câu, có nghĩa là 'vậy thì, thế thì', biểu thị sự suy đoán hoặc đưa ra giải pháp dựa trên điều đã được nói ở câu trước.",
                "examples": [
                    {"zh": "A: 我不想去看电影。 B: 那我也不去了。", "py": "A: Wǒ bù xiǎng qù kàn diànyǐng. B: Nà wǒ yě bú qù le.", "vi": "A: Mình không muốn đi xem phim. - B: Thế thì mình cũng không đi nữa."},
                    {"zh": "A: 晚饭还没做好呢。 B: 那我们出去吃吧。", "py": "A: Wǎnfàn hái méi zuòhǎo ne. B: Nà wǒmen chūqù chī ba.", "vi": "A: Cơm tối vẫn chưa nấu xong. - B: Vậy chúng mình ra ngoài ăn nhé."}
                ]
            }
        ]
    },

    # ==================== BÀI 2 ====================
    {
        "id": 2,
        "title_zh": "他什么时候回来？",
        "title_py": "Tā shénme shíhou huílái?",
        "title_vi": "Khi nào anh ấy quay về?",
        "dialogues": [
            {
                "title": "Đoạn 1: 下山的路上 (Trên đường xuống núi)",
                "location": "在山下 / 路上",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "休息一下吧，怎么了？", "py": "Xiūxi yíxià ba, zěnme le?", "vi": "Nghỉ một lát đi, sao thế anh?"},
                    {"speaker": "小刚", "role": "male", "zh": "我现在腿也酸，脚也疼。", "py": "Wǒ xiànzài tuǐ yě suān, jiǎo yě téng.", "vi": "Bây giờ chân anh vừa mỏi, bàn chân lại vừa đau."},
                    {"speaker": "小丽", "role": "female", "zh": "那我们去那边树下坐坐吧。", "py": "Nà wǒmen qù nàbiān shù xià zuòzuo ba.", "vi": "Thế chúng mình qua dưới gốc cây đằng kia ngồi đi."},
                    {"speaker": "小刚", "role": "male", "zh": "上山容易下山难，你不知道吗？", "py": "Shàngshān róngyì xiàshān nán, nǐ bù zhīdào ma?", "vi": "Lên núi dễ xuống núi khó, em không biết sao?"}
                ]
            },
            {
                "title": "Đoạn 2: 在打电话 (Nói chuyện điện thoại)",
                "location": "在家 / 办公室",
                "lines": [
                    {"speaker": "周太太", "role": "female", "zh": "喂，你好，周明在吗？", "py": "Wèi, nǐ hǎo, Zhōu Míng zài ma?", "vi": "Alo, xin chào, Chu Minh có ở đó không?"},
                    {"speaker": "秘书", "role": "male", "zh": "周经理出去了，不在办公室。", "py": "Zhōu jīnglǐ chūqù le, bú zài bàngōngshì.", "vi": "Giám đốc Chu đi ra ngoài rồi, không có ở văn phòng."},
                    {"speaker": "周太太", "role": "female", "zh": "他去哪儿了？什么时候回来？", "py": "Tā qù nǎr le? Shénme shíhou huílái?", "vi": "Anh ấy đi đâu rồi? Khi nào thì quay về?"},
                    {"speaker": "秘书", "role": "male", "zh": "他出去办事了，下午两点左右回来。", "py": "Tā chūqù bànshì le, xiàwǔ liǎng diǎn zuǒyòu huílái.", "vi": "Ông ấy ra ngoài làm việc, khoảng 2 giờ chiều sẽ quay lại ạ."}
                ]
            },
            {
                "title": "Đoạn 3: 在办公室 (Ở văn phòng)",
                "location": "在办公室",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "周经理，外面下雨了，您带伞了吗？", "py": "Zhōu jīnglǐ, wàimiàn xiàyǔ le, nín dài sǎn le ma?", "vi": "Giám đốc Chu ơi, bên ngoài mưa rồi, ngài có mang ô không ạ?"},
                    {"speaker": "周明", "role": "male", "zh": "我没带。办公室里有伞吗？", "py": "Wǒ méi dài. Bàngōngshì li yǒu sǎn ma?", "vi": "Tôi không mang. Trong văn phòng có ô không?"},
                    {"speaker": "小丽", "role": "female", "zh": "这里有一把伞，您拿去用吧。", "py": "Zhèlǐ yǒu yì bǎ sǎn, nín ná qù yòng ba.", "vi": "Ở đây có một chiếc ô, ngài cầm lấy dùng đi ạ."},
                    {"speaker": "周明", "role": "male", "zh": "谢谢你，我明天就带回来。", "py": "Xièxie nǐ, wǒ míngtiān jiù dài huílái.", "vi": "Cảm ơn cô, ngày mai tôi sẽ mang trả lại."}
                ]
            },
            {
                "title": "Đoạn 4: 在楼下 (Dưới tầng lầu)",
                "location": "在楼下",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "你怎么走得这么慢？", "py": "Nǐ zěnme zǒu de zhème màn?", "vi": "Sao em đi chậm thế?"},
                    {"speaker": "小丽", "role": "female", "zh": "我有点儿累，我们坐电梯上去吧。", "py": "Wǒ yǒudiǎnr lèi, wǒmen zuò diàntī shàngqù ba.", "vi": "Em hơi mệt, chúng mình đi thang máy lên đi anh."},
                    {"speaker": "小刚", "role": "male", "zh": "其实爬楼梯对身体很好。", "py": "Qíshí pá lóutī duì shēntǐ hěn hǎo.", "vi": "Thực ra leo cầu thang bộ rất tốt cho sức khỏe."},
                    {"speaker": "小丽", "role": "female", "zh": "你每天都吃那么多，能不胖吗？", "py": "Nǐ měitiān dōu chī nàme duō, néng bú pàng ma?", "vi": "Ngày nào anh cũng ăn nhiều thế, bảo sao không béo được?"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：周经理去哪儿了？他什么时候回来？ 男：他去开会了，下午三点回来。",
                "question": "周经理什么时候回来？",
                "options": ["A. 下午两点", "B. 下午三点", "C. 明天早上"],
                "ans": "B",
                "explain": "Đoạn thoại nêu rõ: 下午三点回来."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "今天下大雨，小刚出门的时候带了伞，所以没有淋湿。",
                "question": "Phán đoán đúng hay sai: 小刚出门带了雨伞。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Thông tin hoàn toàn khớp với câu nói: 小刚出门的时候带了伞."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：今天爬山太累了，我的腿好疼。 女：那我们在树下坐一会儿吧。",
                "question": "他们打算在哪儿休息？",
                "options": ["A. 家里", "B. 树下", "C. 办公室"],
                "ans": "B",
                "explain": "Cô gái bảo: 那我们在树下坐一会儿吧 (ngồi dưới gốc cây)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：你每天吃了饭就坐着看电视，能不胖吗？ 男：好，我明天开始跑步。",
                "question": "女的觉得男的为什么胖？",
                "options": ["A. 吃得多，不运动", "B. 工作太累", "C. 水喝得太少"],
                "ans": "A",
                "explain": "Ăn xong chỉ ngồi xem TV, không vận động thì làm sao không béo."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "办公室里有一把雨伞，你拿去吧。", "py": "Bàngōngshì li yǒu yì bǎ yǔsǎn, nǐ ná qù ba.", "vi": "Trong văn phòng có một chiếc ô, bạn cầm đi đi."},
                {"id": "B", "text": "他下午两点左右回来。", "py": "Tā xiàwǔ liǎng diǎn zuǒyòu huílái.", "vi": "Anh ấy khoảng 2 giờ chiều sẽ quay lại."},
                {"id": "C", "text": "上山容易下山难，慢慢走吧。", "py": "Shàngshān róngyì xiàshān nán, mànmàn zǒu ba.", "vi": "Lên núi dễ xuống núi khó, cứ đi từ từ thôi."},
                {"id": "D", "text": "天天吃肉不运动，能不胖吗？", "py": "Tiāntiān chī ròu bú yùndòng, néng bú pàng ma?", "vi": "Ngày nào cũng ăn thịt mà không tập thể dục, sao không béo được?"},
                {"id": "E", "text": "我腿疼，我们坐电梯上去吧。", "py": "Wǒ tuǐ téng, wǒmen zuò diàntī shàngqù ba.", "vi": "Chân tôi đau, chúng mình đi thang máy lên đi."}
            ],
            "questions": [
                {"num": 21, "text": "周经理什么时候回办公室？", "py": "Zhōu jīnglǐ shénme shíhou huí bàngōngshì?", "vi": "Giám đốc Chu khi nào về văn phòng?", "ans": "B", "explain": "Đáp án B nêu rõ thời gian: 下午两点左右回来."},
                {"num": 22, "text": "外面下大雨了，怎么办？", "py": "Wàimiàn xià dàyǔ le, zěnme bàn?", "vi": "Bên ngoài mưa to rồi, làm thế nào?", "ans": "A", "explain": "Đáp án A: Cầm chiếc ô trong văn phòng đi."},
                {"num": 23, "text": "我都走不动了，下山怎么这么累？", "py": "Wǒ dōu zǒubúdòng le, xiàshān zěnme zhème lèi?", "vi": "Tôi hết đi nổi rồi, xuống núi sao mà mệt thế?", "ans": "C", "explain": "Đáp án C giải thích: 上山容易下山难."},
                {"num": 24, "text": "你看，我又重了两公斤！", "py": "Nǐ kàn, wǒ yòu zhòng le liǎng gōngjīn!", "vi": "Cậu xem, tớ lại tăng 2 cân rồi!", "ans": "D", "explain": "Đáp lại việc tăng cân: không chịu vận động bảo sao không béo."},
                {"num": 25, "text": "要爬五楼，我们走楼梯吗？", "py": "Yào pá wǔ lóu, wǒmen zǒu lóutī ma?", "vi": "Phải leo 5 tầng, chúng ta đi thang bộ à?", "ans": "E", "explain": "Đáp án E đề nghị: chân đau, đi thang máy lên."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "容易", "py": "róngyì", "vi": "dễ dàng"},
                {"id": "B", "zh": "其实", "py": "qíshí", "vi": "thực ra"},
                {"id": "C", "zh": "伞", "py": "sǎn", "vi": "chiếc ô, dù"},
                {"id": "D", "zh": "胖", "py": "pàng", "vi": "béo, mập"},
                {"id": "E", "zh": "脚", "py": "jiǎo", "vi": "bàn chân"}
            ],
            "questions": [
                {"num": 26, "prefix": "这道题一点儿也不难，很", "suffix": "。", "py": "Zhè dào tí yìdiǎnr yě bù nán, hěn ( ? ).", "vi": "Câu này chẳng khó chút nào, rất ( ? ).", "ans": "A", "word": "容易", "explain": "Không khó tức là rất dễ (容易)."},
                {"num": 27, "prefix": "今天下雨，你记得带一把", "suffix": "。", "py": "Jīntiān xiàyǔ, nǐ jìde dài yì bǎ ( ? ).", "vi": "Hôm nay trời mưa, con nhớ mang một chiếc ( ? ).", "ans": "C", "word": "伞", "explain": "Lượng từ 把 đi với 雨伞 (ô, dù)."},
                {"num": 28, "prefix": "爬了一天的山，我的", "suffix": "特别疼。", "py": "Pá le yì tiān de shān, wǒ de ( ? ) tèbié téng.", "vi": "Leo núi cả một ngày, ( ? ) của tôi đau quá.", "ans": "E", "word": "脚", "explain": "脚疼: đau chân."},
                {"num": 29, "prefix": "他看起来很年轻，", "suffix": "已经四十岁了。", "py": "Tā kàn qǐlái hěn niánqīng, ( ? ) yǐjīng sìshí suì le.", "vi": "Anh ấy trông rất trẻ, ( ? ) đã 40 tuổi rồi.", "ans": "B", "word": "其实", "explain": "其实: thực ra."},
                {"num": 30, "prefix": "最近吃得太多，我又变", "suffix": "了。", "py": "Zuìjìn chī de tài duō, wǒ yòu biàn ( ? ) le.", "vi": "Dạo này ăn nhiều quá, mình lại trở nên ( ? ) rồi.", "ans": "D", "word": "胖", "explain": "变胖: trở nên béo ra."}
            ]
        },
        "reading_p3": {
            "passage_zh": "周经理今天上午去别的公司开会了，不在办公室。他的秘书告诉周太太，经理下午两点左右会回来。外面突然下起了大雨，秘书看到周经理没带雨伞，就帮他找了一把伞放在桌子上。经理回来了看到伞，非常高兴。",
            "passage_py": "Zhōu jīnglǐ jīntiān shàngwǔ qù bié de gōngsī kāihuì le, bú zài bàngōngshì. Tā de mìshū gàosu Zhōu tàitai, jīnglǐ xiàwǔ liǎng diǎn zuǒyòu huì huílái. Wàimiàn tūrán xià qǐ le dàyǔ, mìshū kàndào Zhōu jīnglǐ méi dài yǔsǎn, jiù bāng tā zhǎo le yì bǎ sǎn fàng zài zhuōzi shang. Jīnglǐ huílái le kàndào sǎn, fēicháng gāoxìng.",
            "passage_vi": "Giám đốc Chu sáng nay sang công ty khác họp, không ở văn phòng. Thư ký của ông báo cho Chu phu nhân biết giám đốc khoảng 2 giờ chiều sẽ về. Bên ngoài đột nhiên đổ mưa to, thư ký thấy giám đốc Chu chưa mang ô liền tìm giúp một chiếc để trên bàn. Giám đốc quay về nhìn thấy chiếc ô, cảm thấy vô cùng hài lòng.",
            "questions": [
                {
                    "num": 31,
                    "text": "周经理上午做什么去了？",
                    "options": ["A. 去爬山", "B. 去开会", "C. 去医院"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 周经理今天上午去别的公司开会了."
                },
                {
                    "num": 32,
                    "text": "周经理下午几点回办公室？",
                    "options": ["A. 两点左右", "B. 三点半", "C. 五点"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 经理下午两点左右会回来."
                },
                {
                    "num": 33,
                    "text": "外面天气怎么了？",
                    "options": ["A. 刮大风", "B. 下起了大雨", "C. 出太阳"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 外面突然下起了大雨."
                },
                {
                    "num": 34,
                    "text": "秘书帮周经理准备了什么？",
                    "options": ["A. 一杯咖啡", "B. 一把雨伞", "C. 电脑"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 帮他找了一把伞放在桌子上."
                },
                {
                    "num": 35,
                    "text": "周经理看到桌子上的伞觉得怎么样？",
                    "options": ["A. 很着急", "B. 非常高兴", "C. 有点儿累"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 经理回来了看到伞，非常高兴."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["什么时候", "回来", "他", "？"],
                "ans": "他什么时候回来？",
                "py": "Tā shénme shíhou huílái?",
                "vi": "Khi nào anh ấy quay về?"
            },
            {
                "num": 37,
                "chunks": ["上山", "容易", "难", "下山"],
                "ans": "上山容易下山难。",
                "py": "Shàngshān róngyì xiàshān nán.",
                "vi": "Lên núi dễ xuống núi khó."
            },
            {
                "num": 38,
                "chunks": ["就给", "回去了", "打电话", "我"],
                "ans": "回去了就给我打电话。",
                "py": "Huíqù le jiù gěi wǒ dǎ diànhuà.",
                "vi": "Về tới nơi thì gọi điện cho tôi nhé."
            },
            {
                "num": 39,
                "chunks": ["能", "不运动", "胖", "不", "吗？"],
                "ans": "不运动能不胖吗？",
                "py": "Bù yùndòng néng bú pàng ma?",
                "vi": "Không tập thể dục thì bảo sao không béo được?"
            },
            {
                "num": 40,
                "chunks": ["一把伞", "拿去", "你", "用吧"],
                "ans": "你拿一把伞去用吧。",
                "py": "Nǐ ná yì bǎ sǎn qù yòng ba.",
                "vi": "Bạn cầm một chiếc ô đi mà dùng."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我昨天买了一 (liàng) 新自行车。",
                "pinyin": "liàng",
                "ans": "辆",
                "vi": "Hôm qua tôi đã mua một chiếc xe đạp mới."
            },
            {
                "num": 42,
                "sentence": "下雨了，出门记得带 (sǎn)。",
                "pinyin": "sǎn",
                "ans": "伞",
                "vi": "Mưa rồi, ra ngoài nhớ mang theo ô."
            },
            {
                "num": 43,
                "sentence": "爬完山我的 (tuǐ) 很疼。",
                "pinyin": "tuǐ",
                "ans": "腿",
                "vi": "Leo núi xong chân tôi rất đau."
            },
            {
                "num": 44,
                "sentence": "周 (jīnglǐ) 在办公室开会。",
                "pinyin": "jīnglǐ",
                "ans": "经理",
                "vi": "Giám đốc Chu đang họp trong văn phòng."
            },
            {
                "num": 45,
                "sentence": "你住在几 (lóu)？",
                "pinyin": "lóu",
                "ans": "楼",
                "vi": "Bạn sống ở tầng mấy?"
            }
        ],
        "vocab": [
            {"num": 1, "zh": "腿", "py": "tuǐ", "pos": "danh từ", "vi": "chân, cẳng chân", "eg": "爬山之后我的腿很酸。"},
            {"num": 2, "zh": "脚", "py": "jiǎo", "pos": "danh từ", "vi": "bàn chân", "eg": "我的脚走得好疼。"},
            {"num": 3, "zh": "树", "py": "shù", "pos": "danh từ", "vi": "cây cối", "eg": "树下很凉快。"},
            {"num": 4, "zh": "容易", "py": "róngyì", "pos": "tính từ", "vi": "dễ dàng", "eg": "这道汉语题很容易。"},
            {"num": 5, "zh": "难", "py": "nán", "pos": "tính từ", "vi": "khó khăn", "eg": "学好外语并不难。"},
            {"num": 6, "zh": "太太", "py": "tàitai", "pos": "danh từ", "vi": "bà xã, phu nhân", "eg": "周太太在打电话找经理。"},
            {"num": 7, "zh": "秘书", "py": "mìshū", "pos": "danh từ", "vi": "thư ký", "eg": "王秘书正在写会议报告。"},
            {"num": 8, "zh": "经理", "py": "jīnglǐ", "pos": "danh từ", "vi": "giám đốc, quản lý", "eg": "张经理去外面办事了。"},
            {"num": 9, "zh": "办公室", "py": "bàngōngshì", "pos": "danh từ", "vi": "văn phòng làm việc", "eg": "请进办公室坐坐。"},
            {"num": 10, "zh": "辆", "py": "liàng", "pos": "lượng từ", "vi": "chiếc (xe)", "eg": "公司门口停着一辆车。"},
            {"num": 11, "zh": "楼", "py": "lóu", "pos": "danh từ", "vi": "tòa nhà, lầu, tầng", "eg": "我家住在三楼。"},
            {"num": 12, "zh": "拿", "py": "ná", "pos": "động từ", "vi": "cầm, lấy", "eg": "请帮我拿一下手机。"},
            {"num": 13, "zh": "把", "py": "bǎ", "pos": "lượng từ", "vi": "chiếc, cái (có cán)", "eg": "桌子上有一把雨伞。"},
            {"num": 14, "zh": "伞", "py": "sǎn", "pos": "danh từ", "vi": "chiếc ô, dù", "eg": "下雨天出门别忘了带伞。"},
            {"num": 15, "zh": "胖", "py": "pàng", "pos": "tính từ", "vi": "béo, mập", "eg": "他最近好像长胖了。"},
            {"num": 16, "zh": "其实", "py": "qíshí", "pos": "phó từ", "vi": "thực ra, kỳ thực", "eg": "其实这件事情很简单。"}
        ],
        "proper_nouns": [
            {"zh": "周明", "py": "Zhōu Míng", "vi": "Chu Minh (tên riêng)"},
            {"zh": "周太太", "py": "Zhōu tàitai", "vi": "Chu phu nhân / bà Chu"}
        ],
        "grammar": [
            {
                "title": "1. Bổ ngữ xu hướng đơn giản (简单趋向补语): V + 来 / 去",
                "desc": "Được dùng sau động từ để biểu thị phương hướng của động tác. Nếu hành động hướng về phía người nói thì dùng '来'; nếu hướng ra xa người nói thì dùng '去'.",
                "examples": [
                    {"zh": "你在楼上等我，我上去了。", "py": "Nǐ zài lóu shàng děng wǒ, wǒ shàngqù le.", "vi": "Bạn ở trên lầu đợi tôi, tôi đi lên đó đây."},
                    {"zh": "他在楼下，你快下来吧。", "py": "Tā zài lóu xià, nǐ kuài xiàlái ba.", "vi": "Anh ấy ở dưới lầu, bạn mau xuống đây đi."},
                    {"zh": "他什么时候回来？", "py": "Tā shénme shíhou huílái?", "vi": "Khi nào anh ấy quay về đây?"}
                ]
            },
            {
                "title": "2. Cấu trúc diễn tả hai hành động liên tiếp: V1 + 了……就 + V2……",
                "desc": "Dùng để diễn đạt hành động thứ hai diễn ra ngay lập tức sau khi hành động thứ nhất kết thúc.",
                "examples": [
                    {"zh": "我起了床就吃早饭。", "py": "Wǒ qǐ le chuáng jiù chī zǎofàn.", "vi": "Tôi thức dậy là ăn sáng liền."},
                    {"zh": "小刚回去了就给我打电话。", "py": "Xiǎogāng huíqù le jiù gěi wǒ dǎ diànhuà.", "vi": "Tiểu Cương về đến nơi là gọi điện thoại cho tôi ngay."},
                    {"zh": "下课了我们就去吃饭。", "py": "Xiàkè le wǒmen jiù qù chī fàn.", "vi": "Tan học là chúng mình đi ăn cơm liền."}
                ]
            },
            {
                "title": "3. Câu hỏi phản vấn với “能……吗？” (反问句)",
                "desc": "Dùng hình thức hỏi nhưng nhằm mục đích khẳng định hoặc nhấn mạnh một chân lý hiển nhiên, người nghe tự hiểu đáp án.",
                "examples": [
                    {"zh": "你每天都吃那么多，能不胖吗？", "py": "Nǐ měitiān dōu chī nàme duō, néng bú pàng ma?", "vi": "Ngày nào cậu cũng ăn nhiều như thế, sao mà không béo được? (Tất nhiên là sẽ béo)."},
                    {"zh": "他不努力学习，能考好吗？", "py": "Tā bù nǔlì xuéxí, néng kǎohǎo ma?", "vi": "Nó không chăm học, làm sao thi tốt được?"}
                ]
            }
        ]
    },

    # ==================== BÀI 3 ====================
    {
        "id": 3,
        "title_zh": "桌子上放着很多饮料。",
        "title_py": "Zhuōzi shang fàngzhe hěn duō yǐnliào.",
        "title_vi": "Trên bàn có rất nhiều thức uống.",
        "dialogues": [
            {
                "title": "Đoạn 1: 在家喝茶 (Ở nhà uống trà)",
                "location": "在家",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "明天是晴天还是阴天？", "py": "Míngtiān shì qíngtiān háishì yīntiān?", "vi": "Ngày mai là trời nắng hay trời âm u thế anh?"},
                    {"speaker": "小刚", "role": "male", "zh": "阴天，电视上说多云。你打算去爬山吗？", "py": "Yīntiān, diànshì shang shuō duōyún. Nǐ dǎsuàn qù páshān ma?", "vi": "Trời râm, trên tivi bảo nhiều mây. Em định đi leo núi à?"},
                    {"speaker": "小丽", "role": "female", "zh": "我想去，你跟我去吗？", "py": "Wǒ xiǎng qù, nǐ gēn wǒ qù ma?", "vi": "Em muốn đi, anh đi cùng em không?"},
                    {"speaker": "小刚", "role": "male", "zh": "有你带路，我当然去，爬山时要小心点儿。", "py": "Yǒu nǐ dàilù, wǒ dāngrán qù, páshān shí yào xiǎoxīn diǎnr.", "vi": "Có em dẫn đường anh đương nhiên đi rồi, lúc leo núi nhớ cẩn thận nhé."}
                ]
            },
            {
                "title": "Đoạn 2: 在商场买衣服 (Mua quần áo ở trung tâm thương mại)",
                "location": "在商场",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "你看这条裤子怎么样？", "py": "Nǐ kàn zhè tiáo kùzi zěnmeyàng?", "vi": "Em xem chiếc quần này thế nào?"},
                    {"speaker": "小丽", "role": "female", "zh": "我记得你已经有两条这样的裤子了。", "py": "Wǒ jìde nǐ yǐjīng yǒu liǎng tiáo zhèyàng de kùzi le.", "vi": "Em nhớ anh đã có hai chiếc quần kiểu này rồi mà."},
                    {"speaker": "小刚", "role": "male", "zh": "那我们再看一件衬衫吧。", "py": "Nà wǒmen zài kàn yí jiàn chènshān ba.", "vi": "Vậy chúng mình xem thêm một chiếc áo sơ mi nhé."},
                    {"speaker": "小丽", "role": "female", "zh": "这件白衬衫不错，才两百元。", "py": "Zhè jiàn bái chènshān búcuò, cái liǎng bǎi yuán.", "vi": "Chiếc sơ mi trắng này được đấy, chỉ có hai trăm tệ thôi."}
                ]
            },
            {
                "title": "Đoạn 3: 在水果摊买水果 (Mua hoa quả ở quầy trái cây)",
                "location": "在水果摊",
                "lines": [
                    {"speaker": "顾客", "role": "male", "zh": "西瓜新鲜吗？甜不甜？", "py": "Xīguā xīnxiān ma? Tián bu tián?", "vi": "Dưa hấu có tươi không? Có ngọt không bác?"},
                    {"speaker": "售货员", "role": "female", "zh": "当然新鲜了，不甜不要钱。", "py": "Dāngrán xīnxiān le, bù tián bú yào qián.", "vi": "Đương nhiên là tươi rồi, không ngọt không lấy tiền."},
                    {"speaker": "顾客", "role": "male", "zh": "那给我来一个大西瓜，再买几斤苹果。", "py": "Nà gěi wǒ lái yí ge dà xīguā, zài mǎi jǐ jīn píngguǒ.", "vi": "Thế lấy cho tôi một quả dưa hấu to, với mua thêm vài cân táo nữa."},
                    {"speaker": "售货员", "role": "female", "zh": "好嘞，一共五十八块钱。", "py": "Hǎolei, yígòng wǔshíbā kuài qián.", "vi": "Dạ được rồi, tất cả hết 58 tệ ạ."}
                ]
            },
            {
                "title": "Đoạn 4: 在休息室 (Ở phòng nghỉ)",
                "location": "在休息室",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "桌子上放着很多饮料，你想喝点儿什么？", "py": "Zhuōzi shang fàngzhe hěn duō yǐnliào, nǐ xiǎng hē diǎnr shénme?", "vi": "Trên bàn có đặt nhiều đồ uống lắm, cậu muốn uống gì?"},
                    {"speaker": "小刚", "role": "male", "zh": "茶或者咖啡都可以。你呢？", "py": "Chá huòzhě kāfēi dōu kěyǐ. Nǐ ne?", "vi": "Trà hoặc cà phê đều được. Cậu thì sao?"},
                    {"speaker": "小丽", "role": "female", "zh": "我喝绿茶，夏天喝绿茶很舒服。", "py": "Wǒ hē lǜchá, xiàtiān hē lǜchá hěn shūfu.", "vi": "Tớ uống trà xanh, mùa hè uống trà xanh rất dễ chịu."},
                    {"speaker": "小刚", "role": "male", "zh": "外面花开得很漂亮，我们去花园坐坐吧。", "py": "Wàimiàn huā kāi de hěn piàoliang, wǒmen qù huāyuán zuòzuo ba.", "vi": "Bên ngoài hoa nở đẹp lắm, chúng mình ra vườn ngồi đi."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你想喝绿茶还是咖啡？ 男：今天有点儿困，给我来杯咖啡吧。",
                "question": "男的想喝什么？",
                "options": ["A. 绿茶", "B. 咖啡", "C. 水果汁"],
                "ans": "B",
                "explain": "Người nam trả lời: 给我来杯咖啡吧."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚看到这件衬衫很贵，要八百块钱，所以他没买。",
                "question": "Phán đoán đúng hay sai: 这件衬衫很便宜，小刚买了。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Áo sơ mi đắt 800 tệ nên anh ấy không mua."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：桌子上的水果真新鲜，是谁买的？ 女：是妈妈今天早上买的。",
                "question": "水果是谁买的？",
                "options": ["A. 妈妈", "B. 爸爸", "C. 小丽"],
                "ans": "A",
                "explain": "Người nữ nói: 是妈妈今天早上买的."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：明天爬山你穿哪件衣服？ 男：我穿白衬衫和黑裤子。",
                "question": "男的明天穿什么颜色的裤子？",
                "options": ["A. 白色", "B. 黑色", "C. 蓝色"],
                "ans": "B",
                "explain": "Người nam bảo: 黑裤子 (quần đen)."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "桌子上放着很多新鲜水果。", "py": "Zhuōzi shang fàngzhe hěn duō xīnxiān shuǐguǒ.", "vi": "Trên bàn có đặt nhiều hoa quả tươi ngon."},
                {"id": "B", "text": "我想喝茶或者咖啡。", "py": "Wǒ xiǎng hē chá huòzhě kāfēi.", "vi": "Tôi muốn uống trà hoặc cà phê."},
                {"id": "C", "text": "这件衬衫只要一百五十元。", "py": "Zhè jiàn chènshān zhǐ yào yì bǎi wǔshí yuán.", "vi": "Chiếc áo sơ mi này chỉ có 150 tệ thôi."},
                {"id": "D", "text": "爬山的时候要特别小心。", "py": "Páshān de shíhou yào tèbié xiǎoxīn.", "vi": "Lúc leo núi phải hết sức cẩn thận."},
                {"id": "E", "text": "明天是晴天还是阴天？", "py": "Míngtiān shì qíngtiān háishì yīntiān?", "vi": "Ngày mai là trời nắng hay trời râm?"}
            ],
            "questions": [
                {"num": 21, "text": "电视上说多云，不是晴天。", "py": "Diànshì shang shuō duōyún, bú shì qíngtiān.", "vi": "Tivi nói nhiều mây, không phải trời nắng.", "ans": "E", "explain": "Trả lời câu hỏi dự báo thời tiết ngày mai."},
                {"num": 22, "text": "你看山路这么滑，我们慢点儿走。", "py": "Nǐ kàn shānlù zhème huá, wǒmen màn diǎnr zǒu.", "vi": "Cậu xem đường núi trơn thế này, chúng mình đi chậm thôi.", "ans": "D", "explain": "Khuyên cẩn thận khi leo núi."},
                {"num": 23, "text": "你想喝点儿什么饮料？", "py": "Nǐ xiǎng hē diǎnr shénme yǐnliào?", "vi": "Bạn muốn uống chút đồ uống gì?", "ans": "B", "explain": "Đáp lại loại đồ uống muốn dùng."},
                {"num": 24, "text": "这么便宜的衣服质量好吗？", "py": "Zhème piányi de yīfu zhìliàng hǎo ma?", "vi": "Quần áo rẻ thế này chất lượng có tốt không?", "ans": "C", "explain": "Liên quan đến giá cả chiếc áo sơ mi chỉ 150 tệ."},
                {"num": 25, "text": "快来看看，今天买的西瓜又甜又大！", "py": "Kuài lái kànkan, jīntiān mǎi de xīguā yòu tián yòu dà!", "vi": "Mau lại xem này, dưa hấu hôm nay mua vừa ngọt vừa to!", "ans": "A", "explain": "Hoa quả tươi để trên bàn."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "还是", "py": "háishì", "vi": "hay là (câu hỏi)"},
                {"id": "B", "zh": "记得", "py": "jìde", "vi": "nhớ, còn nhớ"},
                {"id": "C", "zh": "新鲜", "py": "xīnxiān", "vi": "tươi mới"},
                {"id": "D", "zh": "舒服", "py": "shūfu", "vi": "thoải mái, dễ chịu"},
                {"id": "E", "zh": "饮料", "py": "yǐnliào", "vi": "thức uống"}
            ],
            "questions": [
                {"num": 26, "prefix": "你想喝苹果汁", "suffix": "西瓜汁？", "py": "Nǐ xiǎng hē píngguǒzhī ( ? ) xīguāzhī?", "vi": "Bạn muốn uống nước táo ( ? ) nước dưa hấu?", "ans": "A", "word": "还是", "explain": "Câu hỏi lựa chọn dùng 还是."},
                {"num": 27, "prefix": "桌子上放着很多", "suffix": "，有茶也有咖啡。", "py": "Zhuōzi shang fàngzhe hěn duō ( ? ), yǒu chá yě yǒu kāfēi.", "vi": "Trên bàn đặt nhiều ( ? ), có trà cũng có cà phê.", "ans": "E", "word": "饮料", "explain": "Trà và cà phê là thức uống (饮料)."},
                {"num": 28, "prefix": "这些草莓非常", "suffix": "，快尝尝吧。", "py": "Zhèxiē cǎoméi fēicháng ( ? ), kuài chángchang ba.", "vi": "Những trái dâu tây này rất ( ? ), mau nếm thử đi.", "ans": "C", "word": "新鲜", "explain": "Hoa quả tươi ngon (新鲜)."},
                {"num": 29, "prefix": "坐在大树下吹风真", "suffix": "。", "py": "Zuò zài dà shù xià chuīfēng zhēn ( ? ).", "vi": "Ngồi dưới bóng cây hóng gió thật là ( ? ).", "ans": "D", "word": "舒服", "explain": "Cảm giác dễ chịu, thoải mái (舒服)."},
                {"num": 30, "prefix": "你还", "suffix": "小学老师的名字吗？", "py": "Nǐ hái ( ? ) xiǎoxué lǎoshī de míngzi ma?", "vi": "Bạn còn ( ? ) tên của giáo viên tiểu học không?", "ans": "B", "word": "记得", "explain": "Nhớ tên (记得名字)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "今天下午，小刚和小丽去商场买衣服。小丽看到一条漂亮的裙子，才两百元，非常喜欢。小刚买了一件白衬衫和一条黑裤子。买完衣服，他们坐在咖啡馆里休息。桌子上放着两杯热咖啡和一块甜蛋糕，两个人一边喝咖啡一边聊天儿，觉得很舒服。",
            "passage_py": "Jīntiān xiàwǔ, Xiǎogāng hé Xiǎolì qù shāngchǎng mǎi yīfu. Xiǎolì kàndào yì tiáo piàoliang de qúnzi, cái liǎng bǎi yuán, fēicháng xǐhuan. Xiǎogāng mǎi le yí jiàn bái chènshān hé yì tiáo hēi kùzi. Mǎi wán yīfu, tāmen zuò zài kāfēiguǎn li xiūxi. Zhuōzi shang fàngzhe liǎng bēi rè kāfēi hé yí kuài tián dàngāo, liǎng ge rén yìbiān hē kāfēi yìbiān liáotiānr, juéde hěn shūfu.",
            "passage_vi": "Chiều hôm nay, Tiểu Cương và Tiểu Lệ đến trung tâm thương mại mua quần áo. Tiểu Lệ nhìn thấy một chiếc váy rất đẹp, chỉ có hai trăm tệ, cô vô cùng thích. Tiểu Cương mua một chiếc sơ mi trắng và một chiếc quần đen. Mua quần áo xong, họ ngồi nghỉ ở quán cà phê. Trên bàn đặt hai ly cà phê nóng và một miếng bánh ngọt, hai người vừa uống cà phê vừa trò chuyện, cảm thấy vô cùng thoải mái.",
            "questions": [
                {
                    "num": 31,
                    "text": "小丽买了什么？",
                    "options": ["A. 一件衬衫", "B. 一条漂亮的裙子", "C. 一条黑裤子"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小丽看到一条漂亮的裙子，才两百元，非常喜欢."
                },
                {
                    "num": 32,
                    "text": "小刚买了什么衣服？",
                    "options": ["A. 白衬衫和黑裤子", "B. 运动鞋", "C. 雨衣"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 小刚买了一件白衬衫和一条黑裤子."
                },
                {
                    "num": 33,
                    "text": "买完衣服后他们去哪儿了？",
                    "options": ["A. 回家", "B. 去咖啡馆", "C. 去公园"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 买完衣服，他们坐在咖啡馆里休息."
                },
                {
                    "num": 34,
                    "text": "咖啡馆的桌子上放着什么？",
                    "options": ["A. 电脑和手机", "B. 咖啡和蛋糕", "C. 西瓜和绿茶"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 桌子上放着两杯热咖啡和一块甜蛋糕."
                },
                {
                    "num": 35,
                    "text": "他们在咖啡馆里觉得怎么样？",
                    "options": ["A. 很累", "B. 很着急", "C. 很舒服"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 觉得很舒服."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["很多饮料", "放着", "桌子上"],
                "ans": "桌子上放着很多饮料。",
                "py": "Zhuōzi shang fàngzhe hěn duō yǐnliào.",
                "vi": "Trên bàn có đặt rất nhiều đồ uống."
            },
            {
                "num": 37,
                "chunks": ["还是", "喝茶", "喝咖啡", "你想"],
                "ans": "你想喝茶还是喝咖啡？",
                "py": "Nǐ xiǎng hē chá háishì hē kāfēi?",
                "vi": "Bạn muốn uống trà hay là uống cà phê?"
            },
            {
                "num": 38,
                "chunks": ["很新鲜", "这块西瓜", "又大又甜"],
                "ans": "这块西瓜很新鲜，又大又甜。",
                "py": "Zhè kuài xīguā hěn xīnxiān, yòu dà yòu tián.",
                "vi": "Miếng dưa hấu này rất tươi, vừa to vừa ngọt."
            },
            {
                "num": 39,
                "chunks": ["绿茶", "夏天喝", "很舒服"],
                "ans": "夏天喝绿茶很舒服。",
                "py": "Xiàtiān hē lǜchá hěn shūfu.",
                "vi": "Mùa hè uống trà xanh rất dễ chịu."
            },
            {
                "num": 40,
                "chunks": ["两百元", "这条裤子", "才"],
                "ans": "这条裤子才两百元。",
                "py": "Zhè tiáo kùzi cái liǎng bǎi yuán.",
                "vi": "Chiếc quần này chỉ có 200 tệ thôi."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我买了一 (tiáo) 漂亮的裙子。",
                "pinyin": "tiáo",
                "ans": "条",
                "vi": "Tôi đã mua một chiếc váy rất đẹp."
            },
            {
                "num": 42,
                "sentence": "桌子上 (fàng) 着很多书。",
                "pinyin": "fàng",
                "ans": "放",
                "vi": "Trên bàn đặt rất nhiều sách."
            },
            {
                "num": 43,
                "sentence": "这件白 (chènshān) 很好看。",
                "pinyin": "chènshān",
                "ans": "衬衫",
                "vi": "Chiếc áo sơ mi trắng này rất đẹp."
            },
            {
                "num": 44,
                "sentence": "你喜欢喝茶 (huòzhě) 咖啡吗？",
                "pinyin": "huòzhě",
                "ans": "或者",
                "vi": "Bạn thích uống trà hoặc cà phê không?"
            },
            {
                "num": 45,
                "sentence": "今天的水果真 (xīnxiān)。",
                "pinyin": "xīnxiān",
                "ans": "新鲜",
                "vi": "Hoa quả hôm nay thật là tươi."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "还是", "py": "háishì", "pos": "liên từ", "vi": "hay là (trong câu hỏi)", "eg": "你喝咖啡还是喝茶？"},
            {"num": 2, "zh": "爬山", "py": "páshān", "pos": "động từ", "vi": "leo núi", "eg": "周末我们一起去爬山吧。"},
            {"num": 3, "zh": "小心", "py": "xiǎoxīn", "pos": "tính từ/động từ", "vi": "cẩn thận", "eg": "路上车多，要小心点儿。"},
            {"num": 4, "zh": "条", "py": "tiáo", "pos": "lượng từ", "vi": "chiếc, con, sợi", "eg": "他买了一条新裤子。"},
            {"num": 5, "zh": "裤子", "py": "kùzi", "pos": "danh từ", "vi": "quần", "eg": "这条裤子长短正合适。"},
            {"num": 6, "zh": "记得", "py": "jìde", "pos": "động từ", "vi": "nhớ, ghi nhớ", "eg": "我还记得我们第一次见面的地方。"},
            {"num": 7, "zh": "衬衫", "py": "chènshān", "pos": "danh từ", "vi": "áo sơ mi", "eg": "穿白衬衫看起来很精神。"},
            {"num": 8, "zh": "元", "py": "yuán", "pos": "lượng từ", "vi": "đồng nhân dân tệ", "eg": "这本书一共三十元。"},
            {"num": 9, "zh": "新鲜", "py": "xīnxiān", "pos": "tính từ", "vi": "tươi ngon, trong lành", "eg": "早晨山上的空气很新鲜。"},
            {"num": 10, "zh": "甜", "py": "tián", "pos": "tính từ", "vi": "ngọt ngào", "eg": "这个西瓜真甜。"},
            {"num": 11, "zh": "只", "py": "zhǐ", "pos": "phó từ", "vi": "chỉ, chỉ có", "eg": "我只有一个姐姐。"},
            {"num": 12, "zh": "放", "py": "fàng", "pos": "động từ", "vi": "đặt, để", "eg": "请把手机放在桌子上。"},
            {"num": 13, "zh": "饮料", "py": "yǐnliào", "pos": "danh từ", "vi": "đồ uống, thức uống", "eg": "冰箱里有很多冷饮料。"},
            {"num": 14, "zh": "或者", "py": "huòzhě", "pos": "liên từ", "vi": "hoặc, hoặc là (câu trần thuật)", "eg": "星期天我常看书或者听音乐。"},
            {"num": 15, "zh": "舒服", "py": "shūfu", "pos": "tính từ", "vi": "dễ chịu, thoải mái", "eg": "吹着凉风真舒服。"},
            {"num": 16, "zh": "花", "py": "huā", "pos": "danh từ", "vi": "hoa", "eg": "公园里的花开了。"},
            {"num": 17, "zh": "绿", "py": "lǜ", "pos": "tính từ", "vi": "xanh lá cây", "eg": "春天草地变得很绿。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu tồn hiện với “着” (存现句)",
                "desc": "Dùng để biểu thị ở một nơi chốn nào đó đang tồn tại hoặc duy trì một trạng thái của sự vật. Cấu trúc: 'Từ chỉ nơi chốn + Động từ + 着 + Cụm danh từ'.",
                "examples": [
                    {"zh": "桌子上放着很多饮料。", "py": "Zhuōzi shang fàngzhe hěn duō yǐnliào.", "vi": "Trên bàn đặt rất nhiều đồ uống."},
                    {"zh": "门开着呢，请进吧。", "py": "Mén kāizhe ne, qǐng jìn ba.", "vi": "Cửa đang mở đấy, xin mời vào."},
                    {"zh": "墙上挂着一张中国地图。", "py": "Qiáng shang guàzhe yì zhāng Zhōngguó dìtú.", "vi": "Trên tường có treo một tấm bản đồ Trung Quốc."}
                ]
            },
            {
                "title": "2. Phân biệt “还是” và “或者”",
                "desc": "Cả hai đều có nghĩa là 'hoặc, hay là'. Nhưng '还是' dùng trong câu hỏi lựa chọn, còn '或者' dùng trong câu trần thuật hoặc câu khẳng định.",
                "examples": [
                    {"zh": "你喝咖啡还是喝茶？", "py": "Nǐ hē kāfēi háishì hē chá?", "vi": "Bạn uống cà phê hay là uống trà? (Câu hỏi dùng 还是)"},
                    {"zh": "我喝茶或者喝咖啡都可以。", "py": "Wǒ hē chá huòzhě hē kāfēi dōu kěyǐ.", "vi": "Tôi uống trà hay cà phê đều được. (Câu khẳng định dùng 或者)"}
                ]
            }
        ]
    },

    # ==================== BÀI 4 ====================
    {
        "id": 4,
        "title_zh": "她总是笑着跟客人说话。",
        "title_py": "Tā zǒngshì xiàozhe gēn kèrén shuōhuà.",
        "title_vi": "Cô ấy luôn cười khi nói chuyện với khách hàng.",
        "dialogues": [
            {
                "title": "Đoạn 1: 聊学校比赛 (Nói về cuộc thi ở trường)",
                "location": "在操场",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "这是你们比赛的照片吗？", "py": "Zhè shì nǐmen bǐsài de zhàopiàn ma?", "vi": "Đây là ảnh trận thi đấu của các bạn à?"},
                    {"speaker": "小丽", "role": "female", "zh": "是啊，站在中间的那个女孩儿是我们班的。", "py": "Shì a, zhàn zài zhōngjiān de nà ge nǚháir shì wǒmen bān de.", "vi": "Đúng thế, cô bạn gái đứng ở giữa là học cùng lớp với mình đó."},
                    {"speaker": "小刚", "role": "male", "zh": "她长得真漂亮，又聪明又热情。", "py": "Tā zhǎng de zhēn piàoliang, yòu cōngming yòu rèqíng.", "vi": "Bạn ấy xinh thật, vừa thông minh lại vừa nhiệt tình."},
                    {"speaker": "小丽", "role": "female", "zh": "她学习也很努力，经常考第一名。", "py": "Tā xuéxí yě hěn nǔlì, jīngcháng kǎo dì-yī míng.", "vi": "Bạn ấy học tập cũng chăm chỉ lắm, thường xuyên thi đỗ hạng nhất."}
                ]
            },
            {
                "title": "Đoạn 2: 看照片 (Xem ảnh)",
                "location": "在教室",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "那个笑着说话的人是谁？", "py": "Nà ge xiàozhe shuōhuà de rén shì shéi?", "vi": "Người đang vừa cười vừa nói chuyện kia là ai thế?"},
                    {"speaker": "同事B", "role": "female", "zh": "那是我们新来的李老师。", "py": "Nà shì wǒmen xīn lái de Lǐ lǎoshī.", "vi": "Đó là cô giáo Lý mới đến trường mình."},
                    {"speaker": "同事A", "role": "male", "zh": "她看起来真年轻，教几年级？", "py": "Tā kàn qǐlái zhēn niánqīng, jiāo jǐ niánjí?", "vi": "Cô ấy trông trẻ thật, dạy lớp mấy vậy?"},
                    {"speaker": "同事B", "role": "female", "zh": "她教三年级，对待学生非常认真。", "py": "Tā jiāo sān niánjí, duìdài xuésheng fēicháng rènzhēn.", "vi": "Cô ấy dạy lớp 3, đối xử với học sinh vô cùng nghiêm túc và ân cần."}
                ]
            },
            {
                "title": "Đoạn 3: 在超市 (Ở siêu thị)",
                "location": "在超市",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "走了一下午，我有点儿饿了。", "py": "Zǒu le yí xiàwǔ, wǒ yǒudiǎnr è le.", "vi": "Đi bộ cả buổi chiều, anh thấy hơi đói rồi."},
                    {"speaker": "小丽", "role": "female", "zh": "前面有一家超市，我们去买点儿蛋糕吧。", "py": "Qiánmiàn yǒu yì jiā chāoshì, wǒmen qù mǎi diǎnr dàngāo ba.", "vi": "Phía trước có một siêu thị, chúng mình vào mua chút bánh ngọt nhé."},
                    {"speaker": "小刚", "role": "male", "zh": "好啊，超市的服务员态度特别好。", "py": "Hǎo a, chāoshì de fúwùyuán tàidù tèbié hǎo.", "vi": "Được thôi, nhân viên ở siêu thị đó thái độ phục vụ rất tốt."},
                    {"speaker": "小丽", "role": "female", "zh": "对，她总是笑着跟客人说话。", "py": "Duì, tā zǒngshì xiàozhe gēn kèrén shuōhuà.", "vi": "Đúng thế, cô ấy luôn luôn mỉm cười khi nói chuyện với khách."}
                ]
            },
            {
                "title": "Đoạn 4: 谈工作态度 (Nói về thái độ làm việc)",
                "location": "在办公室",
                "lines": [
                    {"speaker": "经理", "role": "male", "zh": "做服务工作，态度最重要。", "py": "Zuò fúwù gōngzuò, tàidù zuì zhòngyào.", "vi": "Làm công việc phục vụ khách hàng, thái độ là quan trọng nhất."},
                    {"speaker": "员工", "role": "female", "zh": "是的，客人提问题时要认真回答。", "py": "Shì de, kèrén tí wèntí shí yào rènzhēn huídá.", "vi": "Vâng ạ, khi khách đặt câu hỏi phải trả lời thật nghiêm túc."},
                    {"speaker": "经理", "role": "male", "zh": "哪怕站了一整天，也要保持微笑。", "py": "Nǎpà zhàn le yì zhěng tiān, yě yào bǎochí wēixiào.", "vi": "Cho dù phải đứng suốt cả ngày, cũng luôn luôn giữ nụ cười trên môi."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：你觉得新来的李老师怎么样？ 女：她又聪明又热情，大家都喜欢她。",
                "question": "大家为什么喜欢李老师？",
                "options": ["A. 她又聪明又热情", "B. 她经常请大家吃饭", "C. 她长得很胖"],
                "ans": "A",
                "explain": "Người nữ trả lời: 她又聪明又热情."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小丽在超市买衣服的时候，服务员一点儿也不热情。",
                "question": "Phán đoán đúng hay sai: 超市服务员态度不好。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Bài học nói rõ: 服务员总是笑着跟客人说话，态度特别好."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：你肚子饿不饿？要不要吃块蛋糕？ 男：太好了，我正想吃点儿甜的东西呢。",
                "question": "男的想吃什么？",
                "options": ["A. 米饭", "B. 蛋糕", "C. 面包"],
                "ans": "B",
                "explain": "Đoạn thoại nhắc đến ăn bánh ngọt (蛋糕)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "男：站在中间拿着书的那个人是谁？ 女：那是我们年级的数学老师。",
                "question": "中间的那个人教什么？",
                "options": ["A. 语文", "B. 英语", "C. 数学"],
                "ans": "C",
                "explain": "Người nữ nói: 数学老师 (giáo viên dạy toán)."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "她总是笑着跟客人说话。", "py": "Tā zǒngshì xiàozhe gēn kèrén shuōhuà.", "vi": "Cô ấy luôn mỉm cười khi trò chuyện với khách hàng."},
                {"id": "B", "text": "这个孩子又聪明又努力。", "py": "Zhè ge háizi yòu cōngming yòu nǔlì.", "vi": "Đứa bé này vừa thông minh lại vừa chăm chỉ."},
                {"id": "C", "text": "我站了一下午，腿都酸了。", "py": "Wǒ zhàn le yí xiàwǔ, tuǐ dōu suān le.", "vi": "Tôi đứng cả buổi chiều, chân mỏi nhừ rồi."},
                {"id": "D", "text": "超市里有很多好吃的水果蛋糕。", "py": "Chāoshì li yǒu hěn duō hǎochī de shuǐguǒ dàngāo.", "vi": "Trong siêu thị có rất nhiều bánh ngọt hoa quả ngon."},
                {"id": "E", "text": "他在认真回答老师的问题。", "py": "Tā zài rènzhēn huídá lǎoshī de wèntí.", "vi": "Bạn ấy đang nghiêm túc trả lời câu hỏi của thầy giáo."}
            ],
            "questions": [
                {"num": 21, "text": "你怎么总是考班里第一名？", "py": "Nǐ zěnme zǒngshì kǎo bān li dì-yī míng?", "vi": "Sao cậu lúc nào cũng thi đỗ hạng nhất lớp thế?", "ans": "B", "explain": "Khen bạn vừa thông minh vừa nỗ lực."},
                {"num": 22, "text": "这家店的服务态度怎么样？", "py": "Zhè jiā diàn de fúwù tàidù zěnmeyàng?", "vi": "Thái độ phục vụ của cửa hàng này thế nào?", "ans": "A", "explain": "Nhân viên luôn tươi cười với khách."},
                {"num": 23, "text": "你走了那么久，要不要坐下来休息？", "py": "Nǐ zǒu le nàme jiǔ, yào bu yào zuò xiàlái xiūxi?", "vi": "Cậu đi lâu thế rồi, có muốn ngồi xuống nghỉ ngơi không?", "ans": "C", "explain": "Đứng suốt cả buổi chiều nên chân mỏi nhừ."},
                {"num": 24, "text": "我们去买点儿甜品吃吧。", "py": "Wǒmen qù mǎi diǎnr tiánpǐn chī ba.", "vi": "Chúng mình đi mua chút đồ ngọt ăn đi.", "ans": "D", "explain": "Trong siêu thị có nhiều bánh ngọt ngon."},
                {"num": 25, "text": "老师问你话呢，你怎么不说话？", "py": "Lǎoshī wèn nǐ huà ne, nǐ zěnme bù shuōhuà?", "vi": "Thầy giáo đang hỏi cậu đấy, sao cậu không nói?", "ans": "E", "explain": "Đang chuẩn bị nghiêm túc trả lời câu hỏi."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "聪明", "py": "cōngming", "vi": "thông minh"},
                {"id": "B", "zh": "热情", "py": "rèqíng", "vi": "nhiệt tình"},
                {"id": "C", "zh": "总是", "py": "zǒngshì", "vi": "luôn luôn"},
                {"id": "D", "zh": "饿", "py": "è", "vi": "đói bụng"},
                {"id": "E", "zh": "回答", "py": "huídá", "vi": "trả lời"}
            ],
            "questions": [
                {"num": 26, "prefix": "这个小女孩儿", "suffix": "极了，一学就会。", "py": "Zhè ge xiǎo nǚháir ( ? ) jí le, yì xué jiù huì.", "vi": "Bé gái này ( ? ) vô cùng, học một cái là biết ngay.", "ans": "A", "word": "聪明", "explain": "Học một biết mười tức là rất thông minh (聪明)."},
                {"num": 27, "prefix": "大家遇到困难，他", "suffix": "跑来帮忙。", "py": "Dàjiā yùdào kùnnan, tā ( ? ) pǎolái bāngmáng.", "vi": "Mọi người gặp khó khăn, anh ấy ( ? ) chạy lại giúp đỡ.", "ans": "C", "word": "总是", "explain": "总是: luôn luôn."},
                {"num": 28, "prefix": "玩了一整天，孩子们肚子都", "suffix": "了。", "py": "Wán le yì zhěng tiān, háizimen dùzi dōu ( ? ) le.", "vi": "Chơi cả ngày trời, bụng lũ trẻ đều ( ? ) rồi.", "ans": "D", "word": "饿", "explain": "Đói bụng (肚子饿)."},
                {"num": 29, "prefix": "邻居们对我们非常", "suffix": "，经常送水果给我们。", "py": "Línjūmen duì wǒmen fēicháng ( ? ), jīngcháng sòng shuǐguǒ gěi wǒmen.", "vi": "Hàng xóm đối với chúng tôi rất ( ? ), thường xuyên tặng hoa quả cho chúng tôi.", "ans": "B", "word": "热情", "explain": "Nhiệt tình, hiếu khách (热情)."},
                {"num": 30, "prefix": "请你认真", "suffix": "我的问题。", "py": "Qǐng nǐ rènzhēn ( ? ) wǒ de wèntí.", "vi": "Xin bạn hãy nghiêm túc ( ? ) câu hỏi của tôi.", "ans": "E", "word": "回答", "explain": "Trả lời câu hỏi (回答问题)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "我们学校有一位年轻的女老师，她教三年级数学。她长得漂亮，又聪明又热情。上课的时候，她总是笑着跟同学们说话，从来不生气。如果有同学听不懂，她会很耐心地一遍一遍讲，直到大家都明白。大家都非常喜欢上她的课。",
            "passage_py": "Wǒmen xuéxiào yǒu yí wèi niánqīng de nǚ lǎoshī, tā jiāo sān niánjí shùxué. Tā zhǎng de piàoliang, yòu cōngming yòu rèqíng. Shàngkè de shíhou, tā zǒngshì xiàozhe gēn tóngxuémen shuōhuà, cónglái bù shēngqì. Rúguǒ yǒu tóngxué tīngbudǒng, tā huì hěn nàixīn de yí biàn yí biàn jiǎng, zhídào dàjiā dōu míngbai. Dàjiā dōu fēicháng xǐhuan shàng tā de kè.",
            "passage_vi": "Trường chúng tôi có một cô giáo trẻ, cô dạy toán lớp ba. Cô rất xinh đẹp, vừa thông minh lại vừa nhiệt tình. Trong giờ học, cô luôn luôn mỉm cười khi nói chuyện với học sinh, không bao giờ cáu gắt. Nếu có học sinh nào nghe không hiểu, cô sẽ rất kiên nhẫn giảng đi giảng lại từng lượt cho đến khi tất cả đều hiểu rõ. Mọi người đều vô cùng thích học tiết của cô.",
            "questions": [
                {
                    "num": 31,
                    "text": "这位女老师教几年级？",
                    "options": ["A. 一年级", "B. 二年级", "C. 三年级"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 她教三年级数学."
                },
                {
                    "num": 32,
                    "text": "她教什么科目？",
                    "options": ["A. 汉语", "B. 数学", "C. 历史"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 教三年级数学."
                },
                {
                    "num": 33,
                    "text": "上课的时候她态度怎么样？",
                    "options": ["A. 经常生气", "B. 总是笑着说话", "C. 很严肃"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 她总是笑着跟同学们说话."
                },
                {
                    "num": 34,
                    "text": "有同学听不懂时，她怎么做？",
                    "options": ["A. 让同学回家看书", "B. 耐心地一遍遍讲", "C. 批评同学"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 很耐心地一遍一遍讲."
                },
                {
                    "num": 35,
                    "text": "同学们对这位老师感觉怎么样？",
                    "options": ["A. 很害怕", "B. 非常喜欢", "C. 不太了解"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 大家都非常喜欢上她的课."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["笑着", "她总是", "跟客人", "说话"],
                "ans": "她总是笑着跟客人说话。",
                "py": "Tā zǒngshì xiàozhe gēn kèrén shuōhuà.",
                "vi": "Cô ấy luôn mỉm cười khi nói chuyện với khách hàng."
            },
            {
                "num": 37,
                "chunks": ["又聪明", "这个女孩儿", "又漂亮"],
                "ans": "这个女孩儿又聪明又漂亮。",
                "py": "Zhè ge nǚháir yòu cōngming yòu piàoliang.",
                "vi": "Cô bé này vừa thông minh vừa xinh đẹp."
            },
            {
                "num": 38,
                "chunks": ["认真回答", "问题", "请你"],
                "ans": "请你认真回答问题。",
                "py": "Qǐng nǐ rènzhēn huídá wèntí.",
                "vi": "Xin bạn hãy nghiêm túc trả lời câu hỏi."
            },
            {
                "num": 39,
                "chunks": ["买蛋糕", "去超市", "我们吧"],
                "ans": "我们去超市买蛋糕吧。",
                "py": "Wǒmen qù chāoshì mǎi dàngāo ba.",
                "vi": "Chúng mình đi siêu thị mua bánh ngọt nhé."
            },
            {
                "num": 40,
                "chunks": ["努力学习", "经常考", "第一名", "他"],
                "ans": "他努力学习，经常考第一名。",
                "py": "Tā nǔlì xuéxí, jīngcháng kǎo dì-yī míng.",
                "vi": "Cậu ấy nỗ lực học tập, thường xuyên thi đỗ hạng nhất."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "这是我们比赛的 (zhàopiàn)。",
                "pinyin": "zhàopiàn",
                "ans": "照片",
                "vi": "Đây là ảnh trận thi đấu của chúng tôi."
            },
            {
                "num": 42,
                "sentence": "她 (zǒngshì) 热情地帮助别人。",
                "pinyin": "zǒngshì",
                "ans": "总是",
                "vi": "Cô ấy luôn luôn nhiệt tình giúp đỡ người khác."
            },
            {
                "num": 43,
                "sentence": "我肚子很 (è)，想吃点儿东西。",
                "pinyin": "è",
                "ans": "饿",
                "vi": "Bụng tôi rất đói, muốn ăn chút gì đó."
            },
            {
                "num": 44,
                "sentence": "学校前面有一家大 (chāoshì)。",
                "pinyin": "chāoshì",
                "ans": "超市",
                "vi": "Phía trước trường học có một siêu thị lớn."
            },
            {
                "num": 45,
                "sentence": "弟弟很 (cōngming)，很会玩电脑。",
                "pinyin": "cōngming",
                "ans": "聪明",
                "vi": "Em trai rất thông minh, rất thạo dùng máy tính."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "比赛", "py": "bǐsài", "pos": "danh từ/động từ", "vi": "cuộc thi, thi đấu", "eg": "昨天的足球比赛太精彩了。"},
            {"num": 2, "zh": "照片", "py": "zhàopiàn", "pos": "danh từ", "vi": "bức ảnh", "eg": "这是我们全家的合影照片。"},
            {"num": 3, "zh": "年级", "py": "niánjí", "pos": "danh từ", "vi": "lớp, năm học", "eg": "我弟弟读大学三年级。"},
            {"num": 4, "zh": "又", "py": "yòu", "pos": "phó từ", "vi": "vừa... vừa...", "eg": "西瓜又大又甜。"},
            {"num": 5, "zh": "聪明", "py": "cōngming", "pos": "tính từ", "vi": "thông minh", "eg": "小狗非常聪明。"},
            {"num": 6, "zh": "热情", "py": "rèqíng", "pos": "tính từ", "vi": "nhiệt tình, hiếu khách", "eg": "中国朋友非常热情。"},
            {"num": 7, "zh": "努力", "py": "nǔlì", "pos": "tính từ/động từ", "vi": "nỗ lực, chăm chỉ", "eg": "只要努力，就能学好汉语。"},
            {"num": 8, "zh": "总是", "py": "zǒngshì", "pos": "phó từ", "vi": "luôn luôn, lúc nào cũng", "eg": "他总是第一个来到教室。"},
            {"num": 9, "zh": "回答", "py": "huídá", "pos": "động từ", "vi": "trả lời", "eg": "请认真回答我的问题。"},
            {"num": 10, "zh": "站", "py": "zhàn", "pos": "động từ", "vi": "đứng, trạm xe", "eg": "请大家站起来。"},
            {"num": 11, "zh": "饿", "py": "è", "pos": "tính từ", "vi": "đói bụng", "eg": "我好饿，快点儿吃饭吧。"},
            {"num": 12, "zh": "超市", "py": "chāoshì", "pos": "danh từ", "vi": "siêu thị", "eg": "晚上去超市买些水果。"},
            {"num": 13, "zh": "蛋糕", "py": "dàngāo", "pos": "danh từ", "vi": "bánh ngọt, bánh gato", "eg": "今天是小丽的生日蛋糕。"},
            {"num": 14, "zh": "年轻", "py": "niánqīng", "pos": "tính từ", "vi": "trẻ tuổi, thanh xuân", "eg": "王老师看起来很年轻。"},
            {"num": 15, "zh": "认真", "py": "rènzhēn", "pos": "tính từ", "vi": "nghiêm túc, chăm chỉ", "eg": "他做事情一向很认真。"},
            {"num": 16, "zh": "客人", "py": "kèrén", "pos": "danh từ", "vi": "khách, khách hàng", "eg": "家里来客人了，快倒茶。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Cấu trúc miêu tả nhiều đặc điểm: “又……又……”",
                "desc": "Dùng để liên kết hai tính từ hoặc động từ có tính chất tương đồng (cùng mang ý tốt hoặc cùng mang ý xấu), biểu thị hai trạng thái cùng tồn tại cùng lúc (vừa... lại vừa...).",
                "examples": [
                    {"zh": "这个西瓜又大又甜。", "py": "Zhè ge xīguā yòu dà yòu tián.", "vi": "Quả dưa hấu này vừa to vừa ngọt."},
                    {"zh": "那个女孩儿又聪明又漂亮。", "py": "Nà ge nǚháir yòu cōngming yòu piàoliang.", "vi": "Cô bạn gái đó vừa thông minh lại vừa xinh đẹp."},
                    {"zh": "这里的苹果又新鲜又便宜。", "py": "Zhèlǐ de píngguǒ yòu xīnxiān yòu piányi.", "vi": "Táo ở đây vừa tươi lại vừa rẻ."}
                ]
            },
            {
                "title": "2. Động từ 1 + 着 (+ Tân ngữ 1) + Động từ 2",
                "desc": "Biểu thị Động tác 1 diễn ra như một phương thức hoặc trạng thái đệm đi kèm của Động tác 2.",
                "examples": [
                    {"zh": "她总是笑着跟客人说话。", "py": "Tā zǒngshì xiàozhe gēn kèrén shuōhuà.", "vi": "Cô ấy luôn mỉm cười khi nói chuyện với khách."},
                    {"zh": "弟弟站着吃苹果。", "py": "Dìdi zhànzhe chī píngguǒ.", "vi": "Em trai đứng ăn táo."},
                    {"zh": "他们坐着喝咖啡聊天儿。", "py": "Tāmen zuòzhe hē kāfēi liáotiānr.", "vi": "Họ ngồi uống cà phê trò chuyện."}
                ]
            }
        ]
    },

    # ==================== BÀI 5 ====================
    {
        "id": 5,
        "title_zh": "我最近越来越胖了。",
        "title_py": "Wǒ zuìjìn yuè lái yuè pàng le.",
        "title_vi": "Dạo này em ngày càng béo ra.",
        "dialogues": [
            {
                "title": "Đoạn 1: 在小丽家 (Ở nhà Tiểu Lệ)",
                "location": "在家",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "小丽，听说你身体不舒服，怎么了？", "py": "Xiǎolì, tīngshuō nǐ shēntǐ bù shūfu, zěnme le?", "vi": "Tiểu Lệ, nghe nói em người không khỏe, sao thế?"},
                    {"speaker": "小丽", "role": "female", "zh": "前天有点儿发烧，头也疼。", "py": "Qiántiān yǒudiǎnr fāshāo, tóu yě téng.", "vi": "Hôm kia em hơi sốt, đầu cũng nhức."},
                    {"speaker": "小刚", "role": "male", "zh": "吃药了吗？要不要去医院？", "py": "Chī yào le ma? Yào bu yào qù yīyuàn?", "vi": "Em uống thuốc chưa? Có cần đi bệnh viện không?"},
                    {"speaker": "小丽", "role": "female", "zh": "吃了感冒药，现在好多了，不用去医院。", "py": "Chī le gǎnmàoyào, xiànzài hǎoduō le, bú yòng qù yīyuàn.", "vi": "Em uống thuốc cảm rồi, giờ đỡ nhiều rồi, không cần đi viện đâu."}
                ]
            },
            {
                "title": "Đoạn 2: 在打电话 (Nói chuyện điện thoại)",
                "location": "在家",
                "lines": [
                    {"speaker": "朋友", "role": "male", "zh": "周太太，明天我们一起去逛街吧？", "py": "Zhōu tàitai, míngtiān wǒmen yìqǐ qù guàngjiē ba?", "vi": "Bà Chu ơi, ngày mai chúng mình cùng đi dạo phố nhé?"},
                    {"speaker": "周太太", "role": "female", "zh": "对不起，我儿子生病了，我得在家里照顾他。", "py": "Duìbuqǐ, wǒ érzi shēngbìng le, wǒ děi zài jiā li zhàogù tā.", "vi": "Xin lỗi nhé, con trai tôi bị ốm rồi, tôi phải ở nhà chăm sóc cháu."},
                    {"speaker": "朋友", "role": "male", "zh": "严重吗？去看了医生没有？", "py": "Yánzhòng ma? Qù kàn le yīshēng méiyǒu?", "vi": "Có nặng không? Đã đi khám bác sĩ chưa?"},
                    {"speaker": "周太太", "role": "female", "zh": "看了，医生说是换季节感冒，不用担心。", "py": "Kàn le, yīshēng shuō shì huàn jìjié gǎnmào, bú yòng dānxīn.", "vi": "Khám rồi, bác sĩ bảo do giao mùa bị cảm thôi, không cần lo lắng đâu."}
                ]
            },
            {
                "title": "Đoạn 3: 聊季节与运动 (Nói về các mùa và vận động)",
                "location": "在公园",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "一年四个季节中，你最喜欢哪个季节？", "py": "Yì nián sì ge jìjié zhōng, nǐ zuì xǐhuan nǎ ge jìjié?", "vi": "Trong bốn mùa một năm, cậu thích mùa nào nhất?"},
                    {"speaker": "同事B", "role": "female", "zh": "我当然最喜欢春天，草绿了，花开了，天气不冷也不热。", "py": "Wǒ dāngrán zuì xǐhuan chūntiān, cǎo lǜ le, huā kāi le, tiānqì bù lěng yě bú rè.", "vi": "Tớ đương nhiên thích mùa xuân nhất, cỏ xanh hoa nở, thời tiết không lạnh cũng không nóng."},
                    {"speaker": "同事A", "role": "male", "zh": "春天跑步最舒服了，可以多锻炼身体。", "py": "Chūntiān pǎobù zuì shūfu le, kěyǐ duō duànliàn shēntǐ.", "vi": "Mùa xuân chạy bộ là thích nhất, có thể rèn luyện sức khỏe nhiều hơn."},
                    {"speaker": "同事B", "role": "female", "zh": "是啊，夏天的天气太热，只想待在空调房里。", "py": "Shì a, xiàtiān de tiānqì tài rè, zhǐ xiǎng dāi zài kōngtiáofáng li.", "vi": "Đúng thế, thời tiết mùa hè thì nóng quá, chỉ muốn ở trong phòng máy lạnh thôi."}
                ]
            },
            {
                "title": "Đoạn 4: 聊穿衣服与减肥 (Nói về mặc quần áo và giảm cân)",
                "location": "在试衣间",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "我最近越来越胖了，去年买的裙子都穿不上了。", "py": "Wǒ zuìjìn yuè lái yuè pàng le, qùnián mǎi de qúnzi dōu chuān bu shàng le.", "vi": "Dạo này em ngày càng béo ra rồi, chiếc váy mua năm ngoái mặc không vừa nữa."},
                    {"speaker": "小刚", "role": "male", "zh": "谁让你每天晚上都吃甜点呢。", "py": "Shéi ràng nǐ měitiān wǎnshang dōu chī tiándiǎn ne.", "vi": "Ai bảo tối nào em cũng ăn đồ ngọt làm chi."},
                    {"speaker": "小丽", "role": "female", "zh": "为了变瘦，我决定从明天开始每天跑三千米！", "py": "Wèile biàn shòu, wǒ juédìng cóng míngtiān kāishǐ měitiān pǎo sānqiān mǐ!", "vi": "Để trở nên gầy đi, em quyết định từ ngày mai mỗi ngày chạy ba ngàn mét!"},
                    {"speaker": "小刚", "role": "male", "zh": "希望你这次能坚持下去。", "py": "Xīwàng nǐ zhè cì néng jiānchí xiàqù.", "vi": "Hy vọng lần này em có thể kiên trì được tới cùng."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：小丽，你的感冒好点儿了吗？ 女：吃了药，烧已经退了，头也不疼了。",
                "question": "小丽现在怎么样了？",
                "options": ["A. 还发高烧", "B. 已经好多了", "C. 还在医院"],
                "ans": "B",
                "explain": "Cô gái nói: 已经退了，头也不疼了 (đã đỡ nhiều rồi)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "周太太今天要去跟朋友逛街，不能在家里照顾孩子。",
                "question": "Phán đoán đúng hay sai: 周太太今天去逛街了。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Bà Chu phải ở nhà chăm sóc con trai bị ốm, không đi dạo phố được."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：你最喜欢哪个季节？ 男：我喜欢夏天，因为夏天可以去海边游泳。",
                "question": "男的为什么喜欢夏天？",
                "options": ["A. 天气不冷", "B. 可以去游泳", "C. 草绿花开"],
                "ans": "B",
                "explain": "Người nam trả lời: 因为夏天可以去海边游泳."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：去年的裙子我都穿不下了，太胖了！ 男：那以后晚上少吃点儿蛋糕吧。",
                "question": "男的建议女的怎么做？",
                "options": ["A. 买新裙子", "B. 晚上少吃蛋糕", "C. 多睡觉"],
                "ans": "B",
                "explain": "Người nam khuyên: 晚上少吃点儿蛋糕吧."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "我最喜欢春天，草绿了，花开了。", "py": "Wǒ zuì xǐhuan chūntiān, cǎo lǜ le, huā kāi le.", "vi": "Tôi thích nhất mùa xuân, cỏ xanh hoa nở."},
                {"id": "B", "text": "我最近越来越胖了，得少吃点儿。", "py": "Wǒ zuìjìn yuè lái yuè pàng le, děi shǎo chī diǎnr.", "vi": "Dạo này tôi ngày càng béo ra, phải ăn ít lại thôi."},
                {"id": "C", "text": "他发烧感冒了，在家里休息呢。", "py": "Tā fāshāo gǎnmào le, zài jiā li xiūxi ne.", "vi": "Anh ấy bị sốt cảm rồi, đang nghỉ ở nhà."},
                {"id": "D", "text": "为了身体健康，你应该多运动。", "py": "Wèile shēntǐ jiànkāng, nǐ yīnggāi duō yùndòng.", "vi": "Vì sức khỏe, bạn nên vận động nhiều hơn."},
                {"id": "E", "text": "这件夏天的裙子真好看。", "py": "Zhè jiàn xiàtiān de qúnzi zhēn hǎokàn.", "vi": "Chiếc váy mùa hè này thật là đẹp."}
            ],
            "questions": [
                {"num": 21, "text": "小明今天怎么没来上课？", "py": "Xiǎomíng jīntiān zěnme méi lái shàngkè?", "vi": "Tiểu Minh hôm nay sao không đi học?", "ans": "C", "explain": "Lý do vắng học là vì bị sốt cảm, nghỉ ở nhà."},
                {"num": 22, "text": "你一年四季中最喜欢哪个季节？", "py": "Nǐ yì nián sì jì zhōng zuì xǐhuan nǎ ge jìjié?", "vi": "Trong bốn mùa bạn thích nhất mùa nào?", "ans": "A", "explain": "Thích nhất mùa xuân vì cỏ xanh hoa nở."},
                {"num": 23, "text": "你看你，怎么又胖了一圈？", "py": "Nǐ kàn nǐ, zěnme yòu pàng le yì quān?", "vi": "Cậu xem cậu kìa, sao lại béo lên một vòng rồi?", "ans": "B", "explain": "Thừa nhận dạo này ngày càng béo ra."},
                {"num": 24, "text": "我天天坐着工作，经常腰疼。", "py": "Wǒ tiāntiān zuòzhe gōngzuò, jīngcháng yāo téng.", "vi": "Tôi ngày nào cũng ngồi làm việc, hay bị đau lưng.", "ans": "D", "explain": "Khuyên vì sức khỏe nên vận động nhiều hơn."},
                {"num": 25, "text": "今年夏天你打算买什么衣服？", "py": "Jīnnián xiàtiān nǐ dǎsuàn mǎi shénme yīfu?", "vi": "Mùa hè năm nay cậu định mua quần áo gì?", "ans": "E", "explain": "Khen chiếc váy mùa hè đẹp."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "发烧", "py": "fāshāo", "vi": "sốt"},
                {"id": "B", "zh": "照顾", "py": "zhàogù", "vi": "chăm sóc"},
                {"id": "C", "zh": "季节", "py": "jìjié", "vi": "mùa, thời vụ"},
                {"id": "D", "zh": "裙子", "py": "qúnzi", "vi": "váy"},
                {"id": "E", "zh": "最近", "py": "zuìjìn", "vi": "dạo này, gần đây"}
            ],
            "questions": [
                {"num": 26, "prefix": "生病的时候，家人一直在医院", "suffix": "他。", "py": "Shēngbìng de shíhou, jiārén yìzhí zài yīyuàn ( ? ) tā.", "vi": "Lúc bị ốm, người nhà luôn ở viện ( ? ) anh ấy.", "ans": "B", "word": "照顾", "explain": "Chăm sóc bệnh nhân (照顾)."},
                {"num": 27, "prefix": "孩子有点儿", "suffix": "，快量个体温吧。", "py": "Háizi yǒudiǎnr ( ? ), kuài liáng ge tǐwēn ba.", "vi": "Đứa bé hơi bị ( ? ), mau đo nhiệt độ đi.", "ans": "A", "word": "发烧", "explain": "Bị sốt đo nhiệt độ (发烧)."},
                {"num": 28, "prefix": "秋天是北京最好的", "suffix": "，天气非常舒服。", "py": "Qiūtiān shì Běijīng zuì hǎo de ( ? ), tiānqì fēicháng shūfu.", "vi": "Mùa thu là ( ? ) đẹp nhất của Bắc Kinh, thời tiết rất dễ chịu.", "ans": "C", "word": "季节", "explain": "Mùa thu là mùa đẹp nhất (季节)."},
                {"num": 29, "prefix": "她今天穿着一条白色的", "suffix": "。", "py": "Tā jīntiān chuānzhe yì tiáo báisè de ( ? ).", "vi": "Hôm nay cô ấy mặc một chiếc ( ? ) màu trắng.", "ans": "D", "word": "裙子", "explain": "Lượng từ 条 đi với 裙子 (váy)."},
                {"num": 30, "prefix": "你", "suffix": "工作忙不忙？", "py": "Nǐ ( ? ) gōngzuò máng bu máng?", "vi": "( ? ) công việc của bạn có bận không?", "ans": "E", "word": "最近", "explain": "Dạo này, gần đây (最近)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "春天来了，天气越来越暖和了。公园里的草绿了，花也开了，景色非常美丽。小丽很喜欢春天，但是她最近有点儿感冒发烧。为了照顾小丽，小刚每天都来给她做饭。在小刚的照顾下，小丽的病好得很快。为了感谢小刚，小丽打算周末请他吃大餐。",
            "passage_py": "Chūntiān lái le, tiānqì yuè lái yuè nuǎnhuo le. Gōngyuán li de cǎo lǜ le, huā yě kāi le, jǐngsè fēicháng měilì. Xiǎolì hěn xǐhuan chūntiān, dànshì tā zuìjìn yǒudiǎnr gǎnmào fāshāo. Wèile zhàogù Xiǎolì, Xiǎogāng měitiān dōu lái gěi tā zuò fàn. Zài Xiǎogāng de zhàogù xià, Xiǎolì de bìng hǎo de hěn kuài. Wèile gǎnxiè Xiǎogāng, Xiǎolì dǎsuàn zhōumò qǐng tā chī dàcān.",
            "passage_vi": "Mùa xuân đến rồi, thời tiết ngày càng ấm áp hơn. Cỏ trong công viên đã xanh, hoa cũng đã nở, phong cảnh vô cùng tươi đẹp. Tiểu Lệ rất thích mùa xuân, nhưng dạo này cô ấy hơi bị cảm sốt. Để chăm sóc Tiểu Lệ, ngày nào Tiểu Cương cũng đến nấu cơm cho cô. Dưới sự chăm sóc của Tiểu Cương, bệnh của Tiểu Lệ khỏi rất nhanh. Để cảm ơn Tiểu Cương, Tiểu Lệ dự định cuối tuần mời anh ấy một bữa thịnh soạn.",
            "questions": [
                {
                    "num": 31,
                    "text": "春天来了，天气怎么样？",
                    "options": ["A. 越来越冷", "B. 越来越暖和", "C. 经常下雪"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 天气越来越暖和了."
                },
                {
                    "num": 32,
                    "text": "小丽最近怎么了？",
                    "options": ["A. 去旅游了", "B. 感冒发烧了", "C. 搬家了"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 她最近有点儿感冒发烧."
                },
                {
                    "num": 33,
                    "text": "小刚每天来给小丽做什么？",
                    "options": ["A. 做饭", "B. 讲故事", "C. 扫地"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 小刚每天都来给她做饭."
                },
                {
                    "num": 34,
                    "text": "小丽的病好得快是因为什么？",
                    "options": ["A. 天气好", "B. 小刚的照顾", "C. 吃了很多蛋糕"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 在小刚的照顾下，小丽的病好得很快."
                },
                {
                    "num": 35,
                    "text": "小丽周末打算怎么感谢小刚？",
                    "options": ["A. 送他一辆自行车", "B. 请他吃大餐", "C. 陪他去爬山"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小丽打算周末请他吃大餐."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["越来越", "天气", "暖和了"],
                "ans": "天气越来越暖和了。",
                "py": "Tiānqì yuè lái yuè nuǎnhuo le.",
                "vi": "Thời tiết ngày càng ấm áp hơn."
            },
            {
                "num": 37,
                "chunks": ["越来越胖了", "最近", "我"],
                "ans": "我最近越来越胖了。",
                "py": "Wǒ zuìjìn yuè lái yuè pàng le.",
                "vi": "Dạo này tôi ngày càng béo ra."
            },
            {
                "num": 38,
                "chunks": ["照顾", "在家里", "生病的孩子", "妈妈"],
                "ans": "妈妈在家里照顾生病的孩子。",
                "py": "Māma zài jiā li zhàogù shēngbìng de háizi.",
                "vi": "Mẹ ở nhà chăm sóc đứa con bị ốm."
            },
            {
                "num": 39,
                "chunks": ["喜欢", "我当然", "春天"],
                "ans": "我当然喜欢春天。",
                "py": "Wǒ dāngrán xǐhuan chūntiān.",
                "vi": "Tôi đương nhiên thích mùa xuân rồi."
            },
            {
                "num": 40,
                "chunks": ["为了", "每天跑步", "健康身体", "他"],
                "ans": "为了身体健康他每天跑步。",
                "py": "Wèile shēntǐ jiànkāng tā měitiān pǎobù.",
                "vi": "Vì sức khỏe anh ấy ngày nào cũng chạy bộ."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我 (zuìjìn) 工作比较忙。",
                "pinyin": "zuìjìn",
                "ans": "最近",
                "vi": "Dạo này công việc của tôi tương đối bận."
            },
            {
                "num": 42,
                "sentence": "春天的草很 (lǜ)，花很红。",
                "pinyin": "lǜ",
                "ans": "绿",
                "vi": "Cỏ mùa xuân rất xanh, hoa rất đỏ."
            },
            {
                "num": 43,
                "sentence": "他生病 (fāshāo) 了，在床上休息。",
                "pinyin": "fāshāo",
                "ans": "发烧",
                "vi": "Anh ấy bị ốm phát sốt rồi, đang nghỉ trên giường."
            },
            {
                "num": 44,
                "sentence": "妹妹买了一条漂亮的 (qúnzi)。",
                "pinyin": "qúnzi",
                "ans": "裙子",
                "vi": "Em gái mua một chiếc váy rất đẹp."
            },
            {
                "num": 45,
                "sentence": "一年有四个 (jìjié)。",
                "pinyin": "jìjié",
                "ans": "季节",
                "vi": "Một năm có 4 mùa."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "发烧", "py": "fāshāo", "pos": "động từ", "vi": "phát sốt, sốt", "eg": "他今天有点儿发烧。"},
            {"num": 2, "zh": "为", "py": "wèi", "pos": "giới từ", "vi": "vì, cho", "eg": "父母为我们做了很多。"},
            {"num": 3, "zh": "照顾", "py": "zhàogù", "pos": "động từ", "vi": "chăm sóc, săn sóc", "eg": "姐姐在医院照顾生病的妈妈。"},
            {"num": 4, "zh": "用", "py": "yòng", "pos": "động từ/phó từ", "vi": "dùng, cần phải", "eg": "病好多了，不用吃药了。"},
            {"num": 5, "zh": "感冒", "py": "gǎnmào", "pos": "động từ/danh từ", "vi": "bị cảm, cảm cúm", "eg": "换季容易感冒，要注意身体。"},
            {"num": 6, "zh": "季节", "py": "jìjié", "pos": "danh từ", "vi": "mùa trong năm", "eg": "秋天是一个收获的季节。"},
            {"num": 7, "zh": "当然", "py": "dāngrán", "pos": "phó từ", "vi": "đương nhiên, tất nhiên", "eg": "有朋友来，我当然高兴。"},
            {"num": 8, "zh": "春(天)", "py": "chūn (tiān)", "pos": "danh từ", "vi": "mùa xuân", "eg": "春天的天气非常舒服。"},
            {"num": 9, "zh": "草", "py": "cǎo", "pos": "danh từ", "vi": "cỏ", "eg": "小羊在草地上吃草。"},
            {"num": 10, "zh": "夏(天)", "py": "xià (tiān)", "pos": "danh từ", "vi": "mùa hè", "eg": "夏天去游泳最凉快。"},
            {"num": 11, "zh": "裙子", "py": "qúnzi", "pos": "danh từ", "vi": "chiếc váy", "eg": "这条长裙子很合身。"},
            {"num": 12, "zh": "最近", "py": "zuìjìn", "pos": "danh từ", "vi": "dạo này, gần đây", "eg": "你最近在忙些什么？"},
            {"num": 13, "zh": "越", "py": "yuè", "pos": "phó từ", "vi": "càng (ngày càng)", "eg": "雨越下越大了。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Cấu trúc “越来越……”",
                "desc": "Biểu thị mức độ của sự vật, hiện tượng đang biến đổi tăng dần theo thời gian (ngày càng... hơn). Sau '越来越' thường là tính từ hoặc động từ tâm lý, không dùng thêm phó từ chỉ mức độ như '很', '非常'.",
                "examples": [
                    {"zh": "我最近越来越胖了。", "py": "Wǒ zuìjìn yuè lái yuè pàng le.", "vi": "Dạo này em ngày càng béo ra."},
                    {"zh": "天气越来越冷了。", "py": "Tiānqì yuè lái yuè lěng le.", "vi": "Thời tiết ngày càng lạnh hơn."},
                    {"zh": "汉语越来越有意思了。", "py": "Hànyǔ yuè lái yuè yǒu yìsi le.", "vi": "Tiếng Hán ngày càng thú vị hơn."}
                ]
            },
            {
                "title": "2. Trợ từ “了” biểu thị sự thay đổi (变化)",
                "desc": "Đặt ở cuối câu để diễn đạt đã có một tình huống mới hoặc trạng thái mới xuất hiện so với trước đây.",
                "examples": [
                    {"zh": "春天来了，草绿了。", "py": "Chūntiān lái le, cǎo lǜ le.", "vi": "Mùa xuân đến rồi, cỏ đã xanh rồi."},
                    {"zh": "我现在不想去了。", "py": "Wǒ xiànzài bù xiǎng qù le.", "vi": "Bây giờ tôi không muốn đi nữa rồi (trước đó muốn đi)."}
                ]
            }
        ]
    }
]
