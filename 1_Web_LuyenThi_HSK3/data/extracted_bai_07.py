# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn bị Bài 07: 我跟他都认识五年了。
Sẵn sàng đưa vào template_master.html
"""

LESSON_DATA = {
    "lesson_info": {
        "id": 7,
        "title_zh": "我跟他都认识五年了。",
        "title_py": "Wǒ gēn tā dōu rènshi wǔ nián le.",
        "title_vi": "Tôi và cô ấy quen nhau được năm năm rồi.",
        "audio_file": "audio.mp3"
    },
    
    "audio_jump": [
        {"time": 0, "label": "▶ 00:00 Mở đầu"},
        {"time": 35, "label": "▶ 00:35 Phần 1 (1-5)"},
        {"time": 175, "label": "▶ 02:55 Phần 2 (6-10)"},
        {"time": 395, "label": "▶ 06:35 Phần 3 (11-15)"},
        {"time": 675, "label": "▶ 11:15 Phần 4 (16-20)"}
    ],

    "tab1_listening": {
        "part1_pictures": [
            {"id": "A", "file": "pic_A.png", "label": "Hình A: Người xem đồng hồ vội vã (看表 / 迟到)"},
            {"id": "B", "file": "pic_B.png", "label": "Hình B: Hai người kéo tay leo núi (爬山)"},
            {"id": "C", "file": "pic_C.png", "label": "Hình C: Người nằm ngủ trên giường (睡觉)"},
            {"id": "D", "file": "pic_D.png", "label": "Hình D (Ví dụ): Gọi điện thoại (打电话)"},
            {"id": "E", "file": "pic_E.png", "label": "Hình E: Người đàn ông đọc báo (看报纸 / 等车)"},
            {"id": "F", "file": "pic_F.png", "label": "Hình F: Bắt tay chào đón đồng nghiệp (握手 / 银行 / 欢迎)"}
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你看看，只有半个小时了，快要迟到了。", "py": "Nǐ kànkan, zhǐ yǒu bàn ge xiǎoshí le, kuàiyào chídào le.", "vi": "Em nhìn xem, chỉ còn nửa tiếng nữa thôi, sắp muộn rồi đấy."},
                    {"role": "female", "speaker": "女", "zh": "你别着急，走路十五分钟就到了。", "py": "Nǐ bié zháojí, zǒulù shíwǔ fēnzhōng jiù dào le.", "vi": "Anh đừng cuống lên thế, đi bộ 15 phút là đến nơi rồi."}
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Nhắc đến thời gian gấp gáp xem đồng hồ '快要迟到了' (sắp muộn rồi)."
            },
            {
                "num": 2,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "你都睡了十几个钟头了，快要迟到了。", "py": "Nǐ dōu shuì le shí jǐ ge zhōngtóu le, kuàiyào chídào le.", "vi": "Con đã ngủ mười mấy tiếng đồng hồ rồi, sắp muộn rồi đấy."},
                    {"role": "male", "speaker": "男", "zh": "我想多睡一会儿，太累了。", "py": "Wǒ xiǎng duō shuì yíhuìr, tài lèi le.", "vi": "Con muốn ngủ thêm một lát nữa, mệt quá mẹ ơi."}
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Nhắc đến '睡了十几个钟头' (ngủ mười mấy tiếng) và cảnh nằm ngủ trên giường."
            },
            {
                "num": 3,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "你慢点儿走，刚爬了几分钟你就累了？", "py": "Nǐ màn diǎnr zǒu, gāng pá le jǐ fēnzhōng nǐ jiù lèi le?", "vi": "Anh đi chậm lại chút đi, mới leo có mấy phút mà anh đã mệt rồi à?"},
                    {"role": "male", "speaker": "男", "zh": "平时不运动，爬山真累啊。", "py": "Píngshí bú yùndòng, páshān zhēn lèi a.", "vi": "Bình thường không vận động, leo núi mệt thật đấy."}
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Nhắc đến hoạt động leo núi '刚爬了几分钟', '爬山真累啊'."
            },
            {
                "num": 4,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "我都看了二十分钟报纸了，车怎么还不来？", "py": "Wǒ dōu kàn le èrshí fēnzhōng bàozhǐ le, chē zěnme hái bù lái?", "vi": "Tôi đã đọc báo suốt hai mươi phút rồi, sao xe vẫn chưa tới thế?"},
                    {"role": "female", "speaker": "女", "zh": "再等等，快来了。", "py": "Zài děngdeng, kuài lái le.", "vi": "Chờ thêm chút nữa đi, sắp đến rồi đấy."}
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Nhắc đến '看了二十分钟报纸' (đọc báo 20 phút) tương ứng hình người cầm đọc báo."
            },
            {
                "num": 5,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "欢迎你来我们银行。", "py": "Huānyíng nǐ lái wǒmen yínháng.", "vi": "Chào mừng bạn đến với ngân hàng của chúng tôi."},
                    {"role": "female", "speaker": "女", "zh": "经理你好，我一定好好工作。", "py": "Jīnglǐ nǐ hǎo, wǒ yídìng hǎohāo gōngzuò.", "vi": "Chào giám đốc, tôi nhất định sẽ làm việc thật tốt."}
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Chào mừng nhân viên mới gia nhập ngân hàng ('欢迎你来我们银行'), bắt tay hợp tác."
            }
        ],

        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {"zh": "我是2010年开始工作的，在银行工作了两年以后来到了这家公司。", "py": "Wǒ shì 2010 nián kāishǐ gōngzuò de, zài yínháng gōngzuò le liǎng nián yǐhòu láidào le zhè jiā gōngsī.", "vi": "Tôi bắt đầu đi làm từ năm 2010, sau khi làm ở ngân hàng được 2 năm thì chuyển sang công ty này."},
                "statement": {"zh": "他现在在银行上班。", "py": "Tā xiànzài zài yínháng shàngbān.", "vi": "Hiện tại anh ấy đang đi làm ở ngân hàng."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Anh ấy đã chuyển sang công ty hiện tại sau 2 năm làm ở ngân hàng, nên hiện không còn làm ở ngân hàng nữa."
            },
            {
                "num": 7,
                "passage": {"zh": "飞机可能晚到十分钟，您再等一会儿吧。", "py": "Fēijī kěnéng wǎndào shí fēnzhōng, nín zài děng yíhuìr ba.", "vi": "Máy bay có thể đến muộn mười phút, xin quý khách đợi thêm một lát ạ."},
                "statement": {"zh": "他们还要等。", "py": "Tāmen hái yào děng.", "vi": "Họ vẫn cần phải đợi tiếp."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Vì máy bay đến muộn nên hành khách phải chờ thêm ('您再等一会儿吧')."
            },
            {
                "num": 8,
                "passage": {"zh": "我对爬山不感兴趣，爬山太累了。", "py": "Wǒ duì páshān bù gǎnxìngqù, páshān tài lèi le.", "vi": "Tôi không có hứng thú với việc leo núi, leo núi mệt lắm."},
                "statement": {"zh": "他喜欢跟朋友一起去爬山。", "py": "Tā xǐhuan gēn péngyou yìqǐ qù páshān.", "vi": "Anh ấy thích cùng bạn bè đi leo núi."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Nhân vật nói '我对爬山不感兴趣' (tôi không có hứng thú với leo núi), không phải thích leo núi."
            },
            {
                "num": 9,
                "passage": {"zh": "小刚在门口站了一个小时，小方也没出来。", "py": "Xiǎogāng zài ménkǒu zhàn le yí ge xiǎoshí, Xiǎofāng yě méi chūlái.", "vi": "Tiểu Cương đã đứng đợi ở cửa suốt một tiếng đồng hồ mà Tiểu Phương vẫn chưa ra."},
                "statement": {"zh": "小刚在等人。", "py": "Xiǎogāng zài děng rén.", "vi": "Tiểu Cương đang đợi người."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đứng trước cửa một tiếng để chờ Tiểu Phương tức là đang đợi người."
            },
            {
                "num": 10,
                "passage": {"zh": "他已经80多岁了，可是身体好，爱运动，还喜欢听年轻人唱的歌。", "py": "Tā yǐjīng 80 duō suì le, kěshì shēntǐ hǎo, ài yùndòng, hái xǐhuan tīng niánqīngrén chàng de gē.", "vi": "Cụ ấy đã ngoài 80 tuổi rồi, nhưng sức khỏe rất tốt, thích vận động, lại còn thích nghe nhạc giới trẻ hát nữa."},
                "statement": {"zh": "她对音乐不感兴趣。", "py": "Tā duì yīnyuè bù gǎnxìngqù.", "vi": "Bà ấy không có hứng thú với âm nhạc."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Cụ rất thích nghe bài hát người trẻ hát ('喜欢听年轻人唱的歌'), chứng tỏ rất yêu âm nhạc."
            }
        ],

        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "雨下得这么大，你家离这儿太远了，怎么办啊？", "py": "Yǔ xià de zhème dà, nǐ jiā lí zhèr tài yuǎn le, zěnmebàn a?", "vi": "Mưa rơi to thế này, nhà bạn lại xa đây quá, làm sao bây giờ?"},
                    {"role": "female", "speaker": "女", "zh": "没关系，我坐出租车，半个小时就回去了。", "py": "Méi guānxi, wǒ zuò chūzūchē, bàn ge xiǎoshí jiù huíqù le.", "vi": "Không sao đâu, tôi bắt xe taxi, nửa tiếng là về tới nhà rồi."}
                ],
                "question": {"zh": "问：女的准备怎么回去？", "py": "Wèn: Nǚ de zhǔnbèi zěnme huíqù?", "vi": "Hỏi: Người nữ chuẩn bị về nhà bằng cách nào?"},
                "options": ["打车", "坐公共汽车", "走路"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: '坐出租车' đồng nghĩa với '打车' (bắt taxi)."
            },
            {
                "num": 12,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你哪儿不舒服？", "py": "Nǐ nǎr bù shūfu?", "vi": "Cháu thấy không khỏe ở chỗ nào?"},
                    {"role": "female", "speaker": "女", "zh": "白医生，我头疼了一个星期了，都没去上课，怎么办呢？", "py": "Bái yīshēng, wǒ tóuténg le yí ge xīngqī le, dōu méi qù shàngkè, zěnmebàn ne?", "vi": "Bác sĩ Bạch ơi, cháu bị đau đầu suốt một tuần nay rồi, đều không đi học được, phải làm sao ạ?"}
                ],
                "question": {"zh": "问：女的怎么了？", "py": "Wèn: Nǚ de zěnme le?", "vi": "Hỏi: Người nữ bị làm sao?"},
                "options": ["她病了", "她迟到了", "她没去工作"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Bị đau đầu một tuần phải đi gặp bác sĩ ('她病了')."
            },
            {
                "num": 13,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你周末喜欢做什么？", "py": "Nǐ zhōumò xǐhuan zuò shénme?", "vi": "Cuối tuần bạn thích làm gì?"},
                    {"role": "female", "speaker": "女", "zh": "我不爱运动，周末就在家看看电视。", "py": "Wǒ bú ài yùndòng, zhōumò jiù zài jiā kànkan diànshì.", "vi": "Tôi không thích vận động, cuối tuần chỉ ở nhà xem tivi thôi."}
                ],
                "question": {"zh": "问：女的对什么没有兴趣？", "py": "Wèn: Nǚ de duì shénme méiyǒu xìngqù?", "vi": "Hỏi: Người nữ không có hứng thú với điều gì?"},
                "options": ["看电视", "运动", "周末"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nói rõ '我不爱运动' (tôi không thích thể thao/vận động)."
            },
            {
                "num": 14,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "今天的工作我还没做完，你来帮帮我好吗？", "py": "Jīntiān de gōngzuò wǒ hái méi zuòwán, nǐ lái bāngbang wǒ hǎo ma?", "vi": "Công việc hôm nay tôi vẫn chưa làm xong, bạn qua giúp tôi một tay được không?"},
                    {"role": "male", "speaker": "男", "zh": "行啊，不过到时候你要请我吃饭。", "py": "Xíng a, búguò dào shíhou nǐ yào qǐng wǒ chī fàn.", "vi": "Được chứ, nhưng mà sau đó bạn phải mời tôi đi ăn đấy nhé."}
                ],
                "question": {"zh": "问：男的和女的可能是什么关系？", "py": "Wèn: Nán de hé nǚ de kěnéng shì shénme guānxi?", "vi": "Hỏi: Người nam và người nữ có khả năng là mối quan hệ gì?"},
                "options": ["同学", "同事", "师生"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Cùng xử lý công việc cơ quan ('今天的工作') nên họ là đồng nghiệp (同事)."
            },
            {
                "num": 15,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "这是什么电影啊？我看了半天也没看懂。", "py": "Zhè shì shénme diànyǐng a? Wǒ kàn le bàntiān yě méi kàndǒng.", "vi": "Đây là phim gì thế nhỉ? Tôi xem cả buổi rồi mà vẫn không hiểu gì."},
                    {"role": "female", "speaker": "女", "zh": "很多人都是这样，你再看一会儿就明白了。", "py": "Hěn duō rén dōu shì zhèyàng, nǐ zài kàn yíhuìr jiù míngbai le.", "vi": "Nhiều người cũng thế mà, bạn xem thêm lát nữa là sẽ hiểu thôi."}
                ],
                "question": {"zh": "问：男的看了多长时间电影了？", "py": "Wèn: Nán de kàn le duō cháng shíjiān diànyǐng le?", "vi": "Hỏi: Người nam đã xem phim được bao lâu rồi?"},
                "options": ["一会儿", "十二个小时", "很久"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: '看了半天' trong khẩu ngữ chỉ khoảng thời gian rất lâu ('很久')."
            }
        ],

        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "我下个月结婚，到时候欢迎你来。", "py": "Wǒ xià ge yuè jiéhūn, dào shíhou huānyíng nǐ lái.", "vi": "Tháng sau mình kết hôn, khi đó hoan nghênh bạn đến dự nhé."},
                    {"role": "male", "speaker": "男", "zh": "什么？结婚？太突然了吧？", "py": "Shénme? Jiéhūn? Tài tūrán le ba?", "vi": "Cái gì? Lấy chồng á? Sao bất ngờ thế?"},
                    {"role": "female", "speaker": "女", "zh": "其实我和我男朋友认识已经五年了。", "py": "Qíshí wǒ hé wǒ nánpéngyou rènshi yǐjīng wǔ nián le.", "vi": "Thực ra mình và bạn trai đã quen nhau được năm năm rồi."},
                    {"role": "male", "speaker": "男", "zh": "就是那天来公司接你的那个？", "py": "Jiù shì nà tiān lái gōngsī jiē nǐ de nà ge?", "vi": "Có phải là anh chàng hôm nọ đến công ty đón cậu không?"}
                ],
                "question": {"zh": "问：关于女的，可以知道什么？", "py": "Wèn: Guānyú nǚ de, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về người nữ, chúng ta có thể biết điều gì?"},
                "options": ["欢迎男的来公司", "要结婚了", "在迎接新同事"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ thông báo tháng sau tổ chức hôn lễ ('我下个月结婚' = 要结婚了)."
            },
            {
                "num": 17,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "喂，我已经等了半个小时了，你在哪儿呢？", "py": "Wèi, wǒ yǐjīng děng le bàn ge xiǎoshí le, nǐ zài nǎr ne?", "vi": "Alo, anh đã đợi suốt nửa tiếng rồi, em đang ở đâu thế?"},
                    {"role": "female", "speaker": "女", "zh": "我刚下飞机，我穿着红衣服。你呢？", "py": "Wǒ gāng xià fēijī, wǒ chuānzhe hóng yīfu. Nǐ ne?", "vi": "Em vừa xuống máy bay, em đang mặc áo đỏ. Còn anh?"},
                    {"role": "male", "speaker": "男", "zh": "我穿着白裤子，你看见我了吗？", "py": "Wǒ chuānzhe bái kùzi, nǐ kànjiàn wǒ le ma?", "vi": "Anh mặc quần trắng, em nhìn thấy anh chưa?"},
                    {"role": "female", "speaker": "女", "zh": "看见了，看见了！", "py": "Kànjiàn le, kànjiàn le!", "vi": "Em thấy rồi, thấy rồi!"}
                ],
                "question": {"zh": "问：男的在做什么？", "py": "Wèn: Nán de zài zuò shénme?", "vi": "Hỏi: Người nam đang làm gì?"},
                "options": ["等车", "接人", "买东西"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam đứng ở sân bay đón bạn gái vừa đáp chuyến bay xuống ('接人')."
            },
            {
                "num": 18,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "你为什么不在书店工作了？", "py": "Nǐ wèishénme bú zài shūdiàn gōngzuò le?", "vi": "Sao anh không làm việc ở hiệu sách nữa?"},
                    {"role": "male", "speaker": "男", "zh": "那不是我喜欢的，我在那儿工作了半年以后就来了这家银行。", "py": "Nà bú shì wǒ xǐhuan de, wǒ zài nàr gōngzuò le bàn nián yǐhòu jiù lái le zhè jiā yínháng.", "vi": "Đó không phải công việc tôi thích, tôi làm ở đó nửa năm thì chuyển sang ngân hàng này."},
                    {"role": "female", "speaker": "女", "zh": "这家银行的工作我很喜欢。", "py": "Zhè jiā yínháng de gōngzuò wǒ hěn xǐhuan.", "vi": "Công việc ở ngân hàng này em cũng rất thích."},
                    {"role": "male", "speaker": "男", "zh": "对，同事们都很好。", "py": "Duì, tóngshìmen dōu hěn hǎo.", "vi": "Đúng thế, các đồng nghiệp đều rất tốt."}
                ],
                "question": {"zh": "问：男的现在在哪儿工作？", "py": "Wèn: Nán de xiànzài zài nǎr gōngzuò?", "vi": "Hỏi: Người nam hiện nay đang làm việc ở đâu?"},
                "options": ["银行", "书店", "学校"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Anh ấy đã chuyển sang ngân hàng làm việc ('就来了这家银行')."
            },
            {
                "num": 19,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "我两岁大的儿子对音乐特别感兴趣。电视上有人唱歌，他也一起唱；有时候大家在吃饭，他也唱。", "py": "Wǒ liǎng suì dà de érzi duì yīnyuè tèbié gǎnxìngqù. Diànshì shang yǒurén chàng gē, tā yě yìqǐ chàng; yǒushíhou dàjiā zài chī fàn, tā yě chàng.", "vi": "Cậu con trai hai tuổi của em đặc biệt thích âm nhạc. Trên tivi có người hát là cu cậu cũng hát theo; nhiều lúc mọi người đang ăn cơm nó cũng hát."},
                    {"role": "male", "speaker": "男", "zh": "真可爱！", "py": "Zhēn kě'ài!", "vi": "Đáng yêu thật đấy!"}
                ],
                "question": {"zh": "问：女的的儿子喜欢什么？", "py": "Wèn: Nǚ de de érzi xǐhuan shénme?", "vi": "Hỏi: Con trai của người nữ thích gì?"},
                "options": ["唱歌", "吃饭", "看电视"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Cu cậu mê âm nhạc và luôn hát theo ('唱歌')."
            },
            {
                "num": 20,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "祝你生日快乐！这个送给你。", "py": "Zhù nǐ shēngrì kuàilè! Zhè ge sòng gěi nǐ.", "vi": "Chúc bạn sinh nhật vui vẻ! Cái này tặng bạn nè."},
                    {"role": "female", "speaker": "女", "zh": "什么呀？打开看看。音乐会的票！我太喜欢了，谢谢你！", "py": "Shénme ya? Dǎkāi kànkan. Yīnyuèhuì de piào! Wǒ tài xǐhuan le, xièxie nǐ!", "vi": "Cái gì thế nhỉ? Mở ra xem nào. Vé hòa nhạc! Mình thích mê luôn, cảm ơn bạn nhé!"}
                ],
                "question": {"zh": "问：女的对什么感兴趣？", "py": "Wèn: Nǚ de duì shénme gǎnxìngqù?", "vi": "Hỏi: Người nữ có hứng thú với điều gì?"},
                "options": ["电影", "运动", "音乐"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Nhận được vé buổi hòa nhạc rất thích thú chứng tỏ cô ấy say mê âm nhạc ('音乐')."
            }
        ]
    },

    "tab2_reading": {
        "part1": {
            "options": [
                {"id": "A", "zh": "不行，要迟到了，我要走了。", "py": "Bù xíng, yào chídào le, wǒ yào zǒu le.", "vi": "Không được đâu, sắp muộn rồi, tôi phải đi đây."},
                {"id": "B", "zh": "我是新来的，刚工作三个月。", "py": "Wǒ shì xīn lái de, gāng gōngzuò sān ge yuè.", "vi": "Tôi là người mới đến, mới làm việc được ba tháng thôi."},
                {"id": "C", "zh": "刚十几分钟，还有很远呢。", "py": "Gāng shí jǐ fēnzhōng, hái yǒu hěn yuǎn ne.", "vi": "Mới có mười mấy phút thôi, còn xa lắm."},
                {"id": "D", "zh": "我看看，慢了半个小时。", "py": "Wǒ kànkan, màn le bàn ge xiǎoshí.", "vi": "Để tôi xem nào, chậm mất nửa tiếng rồi."},
                {"id": "E", "zh": "当然。我们先坐公共汽车，然后换地铁。", "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.", "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi sang tàu điện ngầm."},
                {"id": "F", "zh": "不太累，每个月的钱也不少。", "py": "Bú tài lèi, měi ge yuè de qián yě bù shǎo.", "vi": "Không mệt lắm, tiền lương mỗi tháng cũng không ít."}
            ],
            "questions": [
                {"num": 21, "zh": "你在这家公司工作多久了？", "py": "Nǐ zài zhè jiā gōngsī gōngzuò duōjiǔ le?", "vi": "Bạn làm việc ở công ty này bao lâu rồi?", "ans": "B", "explain": "Hỏi thời gian làm việc trả lời: 我是新来的，刚工作三个月。"},
                {"num": 22, "zh": "别着急，再游一会儿吧。", "py": "Bié zháojí, zài yóu yíhuìr ba.", "vi": "Đừng vội, bơi thêm một lát nữa đi.", "ans": "A", "explain": "Từ chối vì sợ muộn giờ: 不行，要迟到了，我要走了。"},
                {"num": 23, "zh": "你为什么选择在银行工作？", "py": "Nǐ wèishénme xuǎnzé zài yínháng gōngzuò?", "vi": "Vì sao bạn chọn làm việc tại ngân hàng?", "ans": "F", "explain": "Nêu lý do công việc: 不太累，每个月的钱也不少。"},
                {"num": 24, "zh": "你们爬了多长时间山了？", "py": "Nǐmen pá le duō cháng shíjiān shān le?", "vi": "Các bạn đã leo núi được bao lâu rồi?", "ans": "C", "explain": "Trả lời thời lượng leo núi: 刚十几分钟，还有很远呢。"},
                {"num": 25, "zh": "我的手表怎么了？", "py": "Wǒ de shǒubiǎo zěnme le?", "vi": "Đồng hồ của tôi bị làm sao thế này?", "ans": "D", "explain": "Kiểm tra tình trạng đồng hồ: 我看看，慢了半个小时。"}
            ]
        },

        "part2": {
            "vocab_bank": [
                {"id": "A", "zh": "以前", "py": "yǐqián", "vi": "trước đây"},
                {"id": "B", "zh": "半", "py": "bàn", "vi": "nửa, rưỡi"},
                {"id": "C", "zh": "差", "py": "chà", "vi": "kém, thiếu"},
                {"id": "D", "zh": "久", "py": "jiǔ", "vi": "lâu, thời gian dài"},
                {"id": "E", "zh": "声音", "py": "shēngyīn", "vi": "giọng nói (Ví dụ)"},
                {"id": "F", "zh": "同事", "py": "tóngshì", "vi": "đồng nghiệp"}
            ],
            "questions": [
                {"num": 26, "prefix": "小丽是我的（ ", "suffix": " ），也是我的好朋友，我们已经认识二十年了。", "py": "Xiǎolì shì wǒ de ( tóngshì ), yě shì wǒ de hǎo péngyou, wǒmen yǐjīng rènshi èrshí nián le.", "vi": "Tiểu Lệ là đồng nghiệp của tôi, cũng là bạn thân của tôi, chúng tôi đã quen nhau 20 năm rồi.", "ans": "F", "word": "同事", "explain": "Danh từ quan hệ nghề nghiệp '同事' (đồng nghiệp)."},
                {"num": 27, "prefix": "来这家银行（ ", "suffix": " ），我在两家公司工作过。", "py": "Lái zhè jiā yínháng ( yǐqián ), wǒ zài liǎng jiā gōngsī gōngzuò guò.", "vi": "Trước khi đến ngân hàng này, tôi từng làm việc ở hai công ty.", "ans": "A", "word": "以前", "explain": "Cấu trúc thời gian 'Hành động + 以前' (trước khi...)."},
                {"num": 28, "prefix": "我们每天早上八点（ ", "suffix": " ）上课，上四个小时。", "py": "Wǒmen měitiān zǎoshang bā diǎn ( bàn ) shàngkè, shàng sì ge xiǎoshí.", "vi": "Chúng tôi mỗi sáng tám giờ rưỡi vào học, học bốn tiếng đồng hồ.", "ans": "B", "word": "半", "explain": "Chỉ giờ rưỡi: 八点半 (8 giờ 30 phút)."},
                {"num": 29, "prefix": "A: 看一下手表，现在几点了？<br>B: （ ", "suffix": " ）一刻八点。", "py": "A: Kàn yíxià shǒubiǎo, xiànzài jǐ diǎn le?<br>B: ( Chà ) yí kè bā diǎn.", "vi": "A: Xem đồng hồ giúp tớ, bây giờ là mấy giờ rồi?<br>B: Kém 15 phút 8 giờ (7 giờ 45).", "ans": "C", "word": "差", "explain": "Cách nói giờ kém: 差一刻八点."},
                {"num": 30, "prefix": "A: 都九点了，你怎么回来这么晚？<br>B: 下班以后跟朋友在咖啡店聊天儿聊了很（ ", "suffix": " ），天黑了都不知道。", "py": "A: Dōu jiǔ diǎn le, nǐ zěnme huílái zhème wǎn?<br>B: Xiàbān yǐhòu gēn péngyou zài kāfēidiàn liáotiānr liáo le hěn ( jiǔ ), tiān hēi le dōu bù zhīdào.", "vi": "A: Đã 9 giờ rồi, sao bạn về muộn thế?<br>B: Sau khi tan làm cùng bạn ngồi cà phê nói chuyện rất lâu, trời tối mịt lúc nào cũng không hay.", "ans": "D", "word": "久", "explain": "Cụm bổ ngữ thời lượng '聊了很久' (trò chuyện rất lâu)."}
            ]
        },

        "part3": [
            {
                "num": 31,
                "passage": {
                    "zh": "六个月大的女儿对音乐很感兴趣。她不高的时候，唱歌给她听或者让她听听音乐，一会儿她就笑了。",
                    "py": "Liù ge yuè dà de nǚ'ér duì yīnyuè hěn gǎnxìngqù. Tā bù gāoxìng de shíhou, chàng gē gěi tā tīng huòzhě ràng tā tīngting yīnyuè, yíhuìr tā jiù xiào le.",
                    "vi": "Cô con gái 6 tháng tuổi rất có hứng thú với âm nhạc. Lúc bé không vui, chỉ cần hát cho bé nghe hoặc cho bé nghe nhạc một lát là bé cười ngay."
                },
                "question": {"zh": "★ 她的女儿：", "py": "★ Tā de nǚ'ér:", "vi": "★ Con gái của cô ấy:"},
                "options": [
                    {"id": "A", "zh": "喜欢音乐", "py": "xǐhuan yīnyuè", "vi": "thích âm nhạc"},
                    {"id": "B", "zh": "不喜欢听歌", "py": "bù xǐhuan tīng gē", "vi": "không thích nghe hát"},
                    {"id": "C", "zh": "六岁了", "py": "liù suì le", "vi": "sáu tuổi rồi"}
                ],
                "ans": "A",
                "explain": "Đoạn văn viết: '对音乐很感兴趣' đồng nghĩa với '喜欢音乐' (thích âm nhạc)."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "我在北京住过十年，吃了不少北京菜，学了不少中国文化，现在还都记得。",
                    "py": "Wǒ zài Běijīng zhù guò shí nián, chī le bù shǎo Běijīng cài, xué le bù shǎo Zhōngguó wénhuà, xiànzài hái dōu jìde.",
                    "vi": "Tôi từng sống ở Bắc Kinh 10 năm, ăn không ít món Bắc Kinh, học được không ít văn hóa Trung Quốc, đến giờ vẫn còn nhớ như in."
                },
                "question": {"zh": "★ 我：", "py": "★ Wǒ:", "vi": "★ Tôi:"},
                "options": [
                    {"id": "A", "zh": "现在住在北京", "py": "xiànzài zhù zài Běijīng", "vi": "hiện đang sống ở Bắc Kinh"},
                    {"id": "B", "zh": "现在不住在北京", "py": "xiànzài bú zhù zài Běijīng", "vi": "hiện không sống ở Bắc Kinh"},
                    {"id": "C", "zh": "是北京人", "py": "shì Běijīng rén", "vi": "là người Bắc Kinh"}
                ],
                "ans": "B",
                "explain": "Dùng '住过十年' (đã từng sống 10 năm) chứng tỏ hiện tại không còn sống ở Bắc Kinh nữa."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "我妹妹不喜欢画画儿、唱歌，只对踢足球感兴趣。她会踢足球，也爱看足球比赛。",
                    "py": "Wǒ mèimei bù xǐhuan huàhuàr, chàng gē, zhǐ duì tī zúqiú gǎnxìngqù. Tā huì tī zúqiú, yě ài kàn zúqiú bǐsài.",
                    "vi": "Em gái tôi không thích vẽ tranh, ca hát, chỉ có hứng thú với việc đá bóng. Em ấy biết đá bóng và cũng thích xem các trận đấu bóng đá."
                },
                "question": {"zh": "★ 我妹妹喜欢：", "py": "★ Wǒ mèimei xǐhuan:", "vi": "★ Em gái tôi thích:"},
                "options": [
                    {"id": "A", "zh": "唱歌", "py": "chàng gē", "vi": "ca hát"},
                    {"id": "B", "zh": "踢足球", "py": "tī zúqiú", "vi": "đá bóng"},
                    {"id": "C", "zh": "画画儿", "py": "huàhuàr", "vi": "vẽ tranh"}
                ],
                "ans": "B",
                "explain": "Đoạn văn viết: '只对踢足球感兴趣' (chỉ có hứng thú với đá bóng)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "以前中国人结婚的时候，男女都不认识。丈夫会在结婚迎接妻子那天第一次见到妻子，妻子也第一次见到丈夫。",
                    "py": "Yǐqián Zhōngguó rén jiéhūn de shíhou, nán nǚ dōu bù rènshi. Zhàngfu huì zài jiéhūn yíngjiē qīzi nà tiān dì-yī cì jiàndào qīzi, qīzi yě dì-yī cì jiàndào zhàngfu.",
                    "vi": "Trước đây khi người Trung Quốc kết hôn, nam nữ đều không quen biết nhau. Người chồng sẽ vào đúng ngày đón dâu mới lần đầu tiên nhìn thấy vợ, và người vợ cũng lần đầu tiên nhìn thấy chồng."
                },
                "question": {"zh": "★ 以前中国人结婚，丈夫：", "py": "★ Yǐqián Zhōngguó rén jiéhūn, zhàngfu:", "vi": "★ Ngày trước người Trung Quốc kết hôn, người chồng:"},
                "options": [
                    {"id": "A", "zh": "对妻子不感兴趣", "py": "duì qīzi bù gǎnxìngqù", "vi": "không có hứng thú với vợ"},
                    {"id": "B", "zh": "以前就认识妻子", "py": "yǐqián jiù rènshi qīzi", "vi": "trước đó đã quen vợ"},
                    {"id": "C", "zh": "结婚那天第一次见到妻子", "py": "jiéhūn nà tiān dì-yī cì jiàndào qīzi", "vi": "ngày cưới mới lần đầu nhìn thấy vợ"}
                ],
                "ans": "C",
                "explain": "Đoạn văn nêu rõ: '丈夫会在结婚迎接妻子那天第一次见到妻子' (lần đầu gặp vợ vào ngày cưới)."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "很多年轻人说不知道怎么找工作，总觉得自己的工作不好。有的人都工作了好几年了，钱也不少，但还不知道喜欢做什么。我觉得找工作的时候，兴趣第一，怎么能把钱放在第一呢？",
                    "py": "Hěn duō niánqīngrén shuō bù zhīdào zěnme zhǎo gōngzuò, zǒng juéde zìjǐ de gōngzuò bù hǎo. Yǒu de rén dōu gōngzuò le hǎo jǐ nián le, qián yě bù shǎo, dàn hái bù zhīdào xǐhuan zuò shénme. Wǒ juéde zhǎo gōngzuò de shíhou, xìngqù dì-yī, zěnme néng bǎ qián fàng zài dì-yī ne?",
                    "vi": "Nhiều người trẻ nói không biết tìm việc làm thế nào, luôn thấy công việc của mình không tốt. Có người đã đi làm được mấy năm rồi, thu nhập cũng không ít, nhưng vẫn không biết bản thân thích làm gì. Tôi thấy khi tìm việc, sở thích và hứng thú là số một, sao có thể đặt tiền bạc lên hàng đầu được chứ?"
                },
                "question": {"zh": "★ 我觉得找工作的时候要看：", "py": "★ Wǒ juéde zhǎo gōngzuò de shíhou yào kàn:", "vi": "★ Tôi cảm thấy khi tìm việc cần phải xem xét:"},
                "options": [
                    {"id": "A", "zh": "公司给多少钱", "py": "gōngsī gěi duōshao qián", "vi": "công ty trả bao nhiêu tiền"},
                    {"id": "B", "zh": "喜欢不喜欢", "py": "xǐhuan bu xǐhuan", "vi": "có yêu thích hay không"},
                    {"id": "C", "zh": "工作时间是多少", "py": "gōngzuò shíjiān shì duōshao", "vi": "thời gian làm việc là bao lâu"}
                ],
                "ans": "B",
                "explain": "Tác giả khẳng định '兴趣第一' (hứng thú, sở thích là trên hết) tức là xem bản thân có yêu thích công việc đó hay không (喜欢不喜欢)."
            }
        ]
    },

    "tab3_writing": {
        "part1": [
            {
                "num": 36,
                "chunks": ["唱", "歌", "两个小时", "我们", "了"],
                "ans": "我们唱歌唱了两个小时。",
                "py": "Wǒmen chàng gē chàng le liǎng ge xiǎoshí.",
                "vi": "Chúng tôi hát karaoke suốt hai tiếng đồng hồ.",
                "grammar": "Động từ ly hợp lặp lại động từ trong bổ ngữ thời lượng: Động từ + Tân ngữ + Động từ + 了 + Thời lượng."
            },
            {
                "num": 37,
                "chunks": ["什么", "感兴趣", "对", "你"],
                "ans": "你对什么感兴趣？",
                "py": "Nǐ duì shénme gǎnxìngqù?",
                "vi": "Bạn có hứng thú với cái gì?",
                "grammar": "Chủ ngữ (你) + 对 + Đối tượng nghi vấn (什么) + 感兴趣?"
            },
            {
                "num": 38,
                "chunks": ["以前", "银行", "在", "我", "工作", "两年", "了"],
                "ans": "以前我在银行工作了两年。",
                "py": "Yǐqián wǒ zài yínháng gōngzuò le liǎng nián.",
                "vi": "Trước đây tôi từng làm việc ở ngân hàng hai năm.",
                "grammar": "Thời gian (以前) + Chủ ngữ (我) + Địa điểm (在银行) + Động từ (工作) + 了 + Thời lượng (两年)."
            },
            {
                "num": 39,
                "chunks": ["电视", "看", "了", "三个钟头", "弟弟", "了"],
                "ans": "弟弟看电视看了三个钟头。",
                "py": "Dìdi kàn diànshì kàn le sān ge zhōngtóu.",
                "vi": "Em trai đã xem tivi suốt ba tiếng đồng hồ.",
                "grammar": "Động từ lặp lại trong bổ ngữ thời lượng: Chủ ngữ (弟弟) + Động từ (看) + Tân ngữ (电视) + Động từ (看) + 了 + Thời lượng (三个钟头)."
            },
            {
                "num": 40,
                "chunks": ["了", "听", "十几分钟", "音乐", "昨天", "我"],
                "ans": "昨天我听了十几分钟音乐。",
                "py": "Zuótiān wǒ tīng le shí jǐ fēnzhōng yīnyuè.",
                "vi": "Hôm qua tôi đã nghe nhạc khoảng hơn mười phút.",
                "grammar": "Thời gian (昨天) + Chủ ngữ (我) + Động từ (听) + 了 + Thời lượng (十几分钟) + Tân ngữ (音乐)."
            }
        ],

        "part2": [
            {
                "num": 41,
                "sentence": "我对音乐（ gǎn ）兴趣，你呢？",
                "pinyin": "gǎn",
                "ans": "感",
                "hanviet": "Cảm",
                "compound": "感兴趣 (gǎn xìngqù): có hứng thú, yêu thích",
                "vi": "Tôi có hứng thú với âm nhạc, còn bạn thì sao?"
            },
            {
                "num": 42,
                "sentence": "明天下午你去（ yín ）行吗？我跟你一起去吧。",
                "pinyin": "yín",
                "ans": "银",
                "hanviet": "Ngân",
                "compound": "银行 (yínháng): ngân hàng",
                "vi": "Chiều mai bạn đi ngân hàng à? Để tôi đi cùng bạn nhé."
            },
            {
                "num": 43,
                "sentence": "你是什么时候（ jié ）婚的？怎么都没告诉我们啊？",
                "pinyin": "jié",
                "ans": "结",
                "hanviet": "Kết",
                "compound": "结婚 (jiéhūn): kết hôn, lấy vợ/lấy chồng",
                "vi": "Bạn kết hôn từ khi nào thế? Sao chẳng nói gì với chúng tôi thế?"
            },
            {
                "num": 44,
                "sentence": "您慢走，欢（ yíng ）下次再来。",
                "pinyin": "yíng",
                "ans": "迎",
                "hanviet": "Nghênh",
                "compound": "欢迎 (huānyíng): hoan nghênh, chào đón",
                "vi": "Bác đi thong thả, hoan nghênh bác lần sau lại ghé chơi."
            },
            {
                "num": 45,
                "sentence": "我问你，你多（ jiǔ ）没去公司上班了？",
                "pinyin": "jiǔ",
                "ans": "久",
                "hanviet": "Cửu",
                "compound": "多久 (duōjiǔ): bao lâu, thời gian dài bao nhiêu",
                "vi": "Tôi hỏi bạn nhé, bạn đã bao lâu rồi không đến công ty đi làm?"
            }
        ]
    },

    "tab4_textbook": {
        "vocab": [
            {"id": 1, "zh": "同事", "py": "tóngshì", "pos": "danh từ", "vi": "đồng nghiệp"},
            {"id": 2, "zh": "以前", "py": "yǐqián", "pos": "danh từ chỉ thời gian", "vi": "trước đây, trước kia"},
            {"id": 3, "zh": "银行", "py": "yínháng", "pos": "danh từ", "vi": "ngân hàng"},
            {"id": 4, "zh": "久", "py": "jiǔ", "pos": "tính từ", "vi": "lâu, thời gian dài"},
            {"id": 5, "zh": "感兴趣", "py": "gǎn xìngqù", "pos": "cụm động từ", "vi": "có hứng thú, thích thú"},
            {"id": 6, "zh": "结婚", "py": "jiéhūn", "pos": "động từ", "vi": "kết hôn, lấy nhau"},
            {"id": 7, "zh": "欢迎", "py": "huānyíng", "pos": "động từ", "vi": "hoan nghênh, chào đón"},
            {"id": 8, "zh": "迟到", "py": "chídào", "pos": "động từ", "vi": "đến muộn, trễ giờ"},
            {"id": 9, "zh": "半", "py": "bàn", "pos": "số từ", "vi": "nửa, rưỡi"},
            {"id": 10, "zh": "接", "py": "jiē", "pos": "động từ", "vi": "đón, nhận"},
            {"id": 11, "zh": "刻", "py": "kè", "pos": "lượng từ", "vi": "khắc (15 phút)"},
            {"id": 12, "zh": "差", "py": "chà", "pos": "động từ/tính từ", "vi": "kém, thiếu"}
        ],

        "grammar": [
            {
                "title": "1. Bổ ngữ thời lượng (时量补语): Biểu thị độ dài thời gian của hành động",
                "structure": "Cấu trúc 1: S + V + 了 + Thời lượng (+ Tân ngữ) | Cấu trúc 2: S + V + Tân ngữ + V + 了 + Thời lượng (+ 了)",
                "explanation": "Dùng để biểu thị một hành động kéo dài trong bao lâu. Nếu cuối câu có thêm trợ từ “了” thứ hai, biểu thị hành động vẫn đang tiếp tục diễn ra.",
                "examples": [
                    {"zh": "他在中国学了两年汉语。", "py": "Tā zài Zhōngguó xué le liǎng nián Hànyǔ.", "vi": "Anh ấy đã học tiếng Hán ở Trung Quốc 2 năm (hiện đã kết thúc việc học)."},
                    {"zh": "我跟他都认识五年了。", "py": "Wǒ gēn tā dōu rènshi wǔ nián le.", "vi": "Tôi và anh ấy quen nhau đã 5 năm rồi (và hiện nay vẫn đang quen biết nhau)."},
                    {"zh": "我们等了他半个小时了。", "py": "Wǒmen děng le tā bàn ge xiǎoshí le.", "vi": "Chúng tôi đã đợi anh ấy được nửa tiếng rồi (và vẫn đang tiếp tục đợi)."}
                ]
            },
            {
                "title": "2. Cấu trúc “对……感兴趣 / 有兴趣” biểu thị sự hứng thú",
                "structure": "Chủ ngữ + 对 + Danh từ/Động từ + 感兴趣 / 有兴趣",
                "explanation": "Dùng để diễn tả một người có sở thích, đam mê hoặc sự quan tâm sâu sắc đối với một sự vật hay hoạt động nào đó.",
                "examples": [
                    {"zh": "我对中国历史非常感兴趣。", "py": "Wǒ duì Zhōngguó lìshǐ fēicháng gǎnxìngqù.", "vi": "Tôi rất có hứng thú với lịch sử Trung Quốc."},
                    {"zh": "他对足球一点儿兴趣也没有。", "py": "Tā duì zúqiú yìdiǎnr xìngqù yě méiyǒu.", "vi": "Anh ấy một chút hứng thú với bóng đá cũng không có."}
                ]
            },
            {
                "title": "3. Cách diễn đạt thời gian với “半”, “刻”, “差”",
                "structure": "Giờ + 半 (rưỡi) | Giờ + 一刻 / 三刻 (15p / 45p) | 差 + Phút + Giờ (giờ kém)",
                "explanation": "Cách nói giờ chi tiết trong tiếng Hán hằng ngày.",
                "examples": [
                    {"zh": "八点半上课。", "py": "Bā diǎn bàn shàngkè.", "vi": "Tám rưỡi vào lớp."},
                    {"zh": "差一刻八点。", "py": "Chà yí kè bā diǎn.", "vi": "Tám giờ kém mười lăm (7h45)."}
                ]
            }
        ],

        "expansion_and_idiom": {
            "hanzi_knowledge": {
                "type": "旧字新词 (Từ ghép tạo nghĩa mới)",
                "characters": []
            },
            "word_expansion": [
                {"word": "以后", "py": "yǐhòu", "meaning": "sau này, sau khi (以: lấy, làm + 后: sau)"},
                {"word": "到时候", "py": "dào shíhou", "meaning": "đến lúc đó (到: đến + 时候: lúc, thời điểm)"},
                {"word": "迎接", "py": "yíngjiē", "meaning": "đón rước, chào đón (迎: nghênh + 接: tiếp, đón)"}
            ],
            "proverb": {
                "zh": "一步走错步步错",
                "py": "Yí bù zǒu cuò bù bù cuò",
                "vi": "Đi sai một bước, các bước kế tiếp đều sai (Sai một ly đi một dặm). Nhắc nhở con người cần phải cẩn trọng trong từng quyết định quan trọng của cuộc đời."
            }
        },

        "polyphonic": [
            {
                "char": "差",
                "sounds": [
                    {"py": "chà", "meaning": "kém, thiếu, tệ", "example": "差不多 (chàbuduō), 差得远 (chà de yuǎn)"},
                    {"py": "chā", "meaning": "sai số, chênh lệch", "example": "差别 (chābié), 差距 (chājù)"},
                    {"py": "chāi", "meaning": "công vụ, việc sai phái", "example": "出差 (chūchāi)"}
                ]
            }
        ]
    },

    "quiz_data": {
        "1": {"ans": "A", "explain": "A: Nhắc đến thời gian gấp gáp xem đồng hồ '快要迟到了' (sắp muộn rồi)."},
        "2": {"ans": "C", "explain": "C: Nhắc đến '睡了十几个钟头' (ngủ mười mấy tiếng) và cảnh nằm ngủ trên giường."},
        "3": {"ans": "B", "explain": "B: Nhắc đến hoạt động leo núi '刚爬了几分钟', '爬山真累啊'."},
        "4": {"ans": "E", "explain": "E: Nhắc đến '看了二十分钟报纸' (đọc báo 20 phút) tương ứng hình người cầm đọc báo."},
        "5": {"ans": "F", "explain": "F: Chào mừng nhân viên mới gia nhập ngân hàng ('欢迎你来我们银行'), bắt tay hợp tác."},
        "6": {"ans": "×", "explain": "Sai (×): Anh ấy đã chuyển sang công ty hiện tại sau 2 năm làm ở ngân hàng, nên hiện không còn làm ở ngân hàng nữa."},
        "7": {"ans": "√", "explain": "Đúng (√): Vì máy bay đến muộn nên hành khách phải chờ thêm ('您再等一会儿吧')."},
        "8": {"ans": "×", "explain": "Sai (×): Nhân vật nói '我对爬山不感兴趣' (tôi không có hứng thú với leo núi), không phải thích leo núi."},
        "9": {"ans": "√", "explain": "Đúng (√): Đứng trước cửa một tiếng để chờ Tiểu Phương tức là đang đợi người."},
        "10": {"ans": "×", "explain": "Sai (×): Cụ rất thích nghe bài hát người trẻ hát ('喜欢听年轻人唱的歌'), chứng tỏ rất yêu âm nhạc."},
        "11": {"ans": "A", "explain": "A: '坐出租车' đồng nghĩa với '打车' (bắt taxi)."},
        "12": {"ans": "A", "explain": "A: Bị đau đầu một tuần phải đi gặp bác sĩ ('她病了')."},
        "13": {"ans": "B", "explain": "B: Người nữ nói rõ '我不爱运动' (tôi không thích thể thao/vận động)."},
        "14": {"ans": "B", "explain": "B: Cùng xử lý công việc cơ quan ('今天的工作') nên họ là đồng nghiệp (同事)."},
        "15": {"ans": "C", "explain": "C: '看了半天' trong khẩu ngữ chỉ khoảng thời gian rất lâu ('很久')."},
        "16": {"ans": "B", "explain": "B: Người nữ thông báo tháng sau tổ chức hôn lễ ('我下个月结婚' = 要结婚了)."},
        "17": {"ans": "B", "explain": "B: Người nam đứng ở sân bay đón bạn gái vừa đáp chuyến bay xuống ('接人')."},
        "18": {"ans": "A", "explain": "A: Anh ấy đã chuyển sang ngân hàng làm việc ('就来了这家银行')."},
        "19": {"ans": "A", "explain": "A: Cu cậu mê âm nhạc và luôn hát theo ('唱歌')."},
        "20": {"ans": "C", "explain": "C: Nhận được vé buổi hòa nhạc rất thích thú chứng tỏ cô ấy say mê âm nhạc ('音乐')."},
        "21": {"ans": "B", "explain": "B: Hỏi thời gian làm việc trả lời: 我是新来的，刚工作三个月。"},
        "22": {"ans": "A", "explain": "A: Từ chối vì sợ muộn giờ: 不行，要迟到了，我要走了。"},
        "23": {"ans": "F", "explain": "F: Nêu lý do công việc: 不太累，每个月的钱也不少。"},
        "24": {"ans": "C", "explain": "C: Trả lời thời lượng leo núi: 刚十几分钟，还有很远呢。"},
        "25": {"ans": "D", "explain": "D: Kiểm tra tình trạng đồng hồ: 我看看，慢了半个小时。"},
        "26": {"ans": "F", "explain": "F: Danh từ quan hệ nghề nghiệp '同事' (đồng nghiệp)."},
        "27": {"ans": "A", "explain": "A: Cấu trúc thời gian 'Hành động + 以前' (trước khi...)."},
        "28": {"ans": "B", "explain": "B: Chỉ giờ rưỡi: 八点半 (8 giờ 30 phút)."},
        "29": {"ans": "C", "explain": "C: Cách nói giờ kém: 差一刻八点."},
        "30": {"ans": "D", "explain": "D: Cụm bổ ngữ thời lượng '聊了很久' (trò chuyện rất lâu)."},
        "31": {"ans": "A", "explain": "A: Đoạn văn viết: '对音乐很感兴趣' đồng nghĩa với '喜欢音乐' (thích âm nhạc)."},
        "32": {"ans": "B", "explain": "B: Dùng '住过十年' (đã từng sống 10 năm) chứng tỏ hiện tại không còn sống ở Bắc Kinh nữa."},
        "33": {"ans": "B", "explain": "B: Đoạn văn viết: '只对踢足球感兴趣' (chỉ có hứng thú với đá bóng)."},
        "34": {"ans": "C", "explain": "C: Đoạn văn nêu rõ: '丈夫会在结婚迎接妻子那天第一次见到妻子' (lần đầu gặp vợ vào ngày cưới)."},
        "35": {"ans": "B", "explain": "B: Tác giả khẳng định '兴趣第一' (hứng thú, sở thích là trên hết) tức là xem bản thân có yêu thích công việc đó hay không (喜欢不喜欢)."}
    }
}
