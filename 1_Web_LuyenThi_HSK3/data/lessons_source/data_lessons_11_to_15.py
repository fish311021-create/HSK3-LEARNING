# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn cho Bài 11 đến Bài 15 - HSK 3 Standard Course
"""

LESSONS_11_TO_15 = [
    # ==================== BÀI 11 ====================
    {
        "id": 11,
        "title_zh": "别忘了把空调关了。",
        "title_py": "Bié wàng le bǎ kōngtiáo guān le.",
        "title_vi": "Đừng quên tắt máy điều hòa nhé.",
        "dialogues": [
            {
                "title": "Đoạn 1: 下班离开办公室 (Tan làm rời khỏi văn phòng)",
                "location": "在办公室",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "我要下班了，你还不走吗？", "py": "Wǒ yào xiàbān le, nǐ hái bù zǒu ma?", "vi": "Tôi chuẩn bị tan làm rồi, bạn vẫn chưa về à?"},
                    {"speaker": "同事B", "role": "female", "zh": "我把这份电子邮件发完就走。", "py": "Wǒ bǎ zhè fèn diànzǐ yóujiàn fāwán jiù zǒu.", "vi": "Tôi gửi nốt bức thư điện tử này xong là về ngay."},
                    {"speaker": "同事A", "role": "male", "zh": "走的时候别忘了把灯和空调关了。", "py": "Zǒu de shíhou bié wàng le bǎ dēng hé kōngtiáo guān le.", "vi": "Lúc về đừng quên tắt đèn và điều hòa nhé."},
                    {"speaker": "同事B", "role": "female", "zh": "放心吧，我已经养成好习惯了，走前一定检查。", "py": "Fàngxīn ba, wǒ yǐjīng yǎngchéng hǎo xíguàn le, zǒu qián yídìng jiǎnchá.", "vi": "Yên tâm đi, tôi đã hình thành thói quen tốt rồi, trước khi đi nhất định sẽ kiểm tra."}
                ]
            },
            {
                "title": "Đoạn 2: 在图书馆借书 (Mượn sách ở thư viện)",
                "location": "在图书馆",
                "lines": [
                    {"speaker": "学生", "role": "male", "zh": "老师，我想借这两本关于历史的书。", "py": "Lǎoshī, wǒ xiǎng jiè zhè liǎng běn guānyú lìshǐ de shū.", "vi": "Thưa thầy, em muốn mượn hai cuốn sách về lịch sử này ạ."},
                    {"speaker": "管理员", "role": "female", "zh": "好的，请把学生证给我一下。", "py": "Hǎo de, qǐng bǎ xuéshengzhèng gěi wǒ yíxià.", "vi": "Được rồi, em đưa thẻ học sinh cho cô một chút."},
                    {"speaker": "学生", "role": "male", "zh": "给您。请问可以借多长时间？", "py": "Gěi nín. Qǐngwèn kěyǐ jiè duō cháng shíjiān?", "vi": "Dạ gửi cô. Xin hỏi em có thể mượn trong bao lâu ạ?"},
                    {"speaker": "管理员", "role": "female", "zh": "一个月左右，记得按时把书还回来。", "py": "Yí ge yuè zuǒyòu, jìde ànshí bǎ shū huán huílái.", "vi": "Khoảng chừng một tháng, nhớ mang sách trả đúng hạn nhé."}
                ]
            },
            {
                "title": "Đoạn 3: 乘地铁 (Đi tàu điện ngầm)",
                "location": "在地铁站",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "我们坐地铁去，还是打车去？", "py": "Wǒmen zuò dìtiě qù, háishì dǎchē qù?", "vi": "Chúng mình đi tàu điện ngầm hay là bắt taxi đi?"},
                    {"speaker": "小丽", "role": "female", "zh": "现在是下班时间，路上肯定堵车，坐地铁快得多。", "py": "Xiànzài shì xiàbān shíjiān, lùshang kěndìng dǔchē, zuò dìtiě kuài de duō.", "vi": "Bây giờ là giờ tan tầm, trên đường chắc chắn kẹt xe, đi tàu điện ngầm nhanh hơn nhiều."},
                    {"speaker": "小刚", "role": "male", "zh": "坐地铁大概需要多长时间？", "py": "Zuò dìtiě dàgài xūyào duō cháng shíjiān?", "vi": "Đi tàu điện ngầm khoảng mất bao lâu?"},
                    {"speaker": "小丽", "role": "female", "zh": "二十分钟左右就到了，快把地铁卡拿出来吧。", "py": "Èrshí fēnzhōng zuǒyòu jiù dào le, kuài bǎ dìtiěkǎ ná chūlái ba.", "vi": "Khoảng 20 phút là tới nơi rồi, mau lấy thẻ tàu điện ra đi anh."}
                ]
            },
            {
                "title": "Đoạn 4: 在饭馆吃饭 (Ăn cơm trong quán)",
                "location": "在饭馆",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "服务员，请给我们拿一双筷子和两个杯子。", "py": "Fúwùyuán, qǐng gěi wǒmen ná yì shuāng kuàizi hé liǎng ge bēizi.", "vi": "Phục vụ ơi, lấy giúp chúng tôi một đôi đũa và hai chiếc cốc."},
                    {"speaker": "服务员", "role": "female", "zh": "好的，两位还要点些什么饮料吗？", "py": "Hǎo de, liǎng wèi hái yào diǎn xiē shénme yǐnliào ma?", "vi": "Dạ được, hai vị có muốn gọi thêm đồ uống gì không ạ?"},
                    {"speaker": "小刚", "role": "male", "zh": "再来一瓶啤酒吧，要冰的。", "py": "Zài lái yì píng píjiǔ ba, yào bīng de.", "vi": "Cho thêm một chai bia nữa nhé, lấy bia ướp lạnh."},
                    {"speaker": "小丽", "role": "female", "zh": "你开车来的，千万别把酒喝了！", "py": "Nǐ kāichē lái de, qiānwàn bié bǎ jiǔ hē le!", "vi": "Anh lái xe đến đấy, tuyệt đối không được uống rượu bia đâu đấy!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：走的时候别忘了把空调关了。 女：好的，我已经关好了，灯也关了。",
                "question": "女的刚才做了什么？",
                "options": ["A. 打开了空调", "B. 关了空调和灯", "C. 正在看书"],
                "ans": "B",
                "explain": "Cô gái nói: 已经关好了，灯也关了."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "在图书馆借的书，必须在一个月以内还回来。",
                "question": "Phán đoán đúng hay sai: 借的书可以看一年。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Chỉ được mượn khoảng một tháng (一个月左右)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：坐地铁去要多长时间？ 男：大概半个小时左右就到了。",
                "question": "坐地铁需要多长时间？",
                "options": ["A. 十分钟", "B. 半个小时左右", "C. 一个小时"],
                "ans": "B",
                "explain": "Đoạn thoại nêu rõ: 半个小时左右."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：你今天开车来了，千万别喝酒。 男：好，那我就喝绿茶吧。",
                "question": "男的最后决定喝什么？",
                "options": ["A. 啤酒", "B. 可乐", "C. 绿茶"],
                "ans": "C",
                "explain": "Người nam nói: 那我就喝绿茶吧."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "离开办公室前别忘了把空调和灯关了。", "py": "Líkāi bàngōngshì qián bié wàng le bǎ kōngtiáo hé dēng guān le.", "vi": "Trước khi rời văn phòng đừng quên tắt điều hòa và đèn."},
                {"id": "B", "text": "借的书请在一个月左右还给图书馆。", "py": "Jiè de shū qǐng zài yí ge yuè zuǒyòu huán gěi túshūguǎn.", "vi": "Sách mượn xin vui lòng trả lại thư viện trong khoảng một tháng."},
                {"id": "C", "text": "路上堵车严重，坐地铁快得多。", "py": "Lùshang dǔchē yánzhòng, zuò dìtiě kuài de duō.", "vi": "Trên đường kẹt xe nghiêm trọng, đi tàu điện ngầm nhanh hơn nhiều."},
                {"id": "D", "text": "服务员，请给我们拿一双筷子和一个杯子。", "py": "Fúwùyuán, qǐng gěi wǒmen ná yì shuāng kuàizi hé yí ge bēizi.", "vi": "Phục vụ ơi, lấy giúp chúng tôi một đôi đũa và một chiếc cốc."},
                {"id": "E", "text": "他开车来的，绝对不能喝酒。", "py": "Tā kāichē lái de, juéduì bù néng hējiǔ.", "vi": "Anh ấy lái xe đến, tuyệt đối không được uống rượu."}
            ],
            "questions": [
                {"num": 21, "text": "走的时候要注意什么？", "py": "Zǒu de shíhou yào zhùyì shénme?", "vi": "Lúc rời đi cần chú ý điều gì?", "ans": "A", "explain": "Nhắc nhở tắt điều hòa và đèn."},
                {"num": 22, "text": "这本借来的书什么时候要还？", "py": "Zhè běn jiè lái de shū shénme shíhou yào huán?", "vi": "Cuốn sách mượn này khi nào phải trả?", "ans": "B", "explain": "Trả trong khoảng một tháng."},
                {"num": 23, "text": "下班高峰期怎么去火车站最快？", "py": "Xiàbān gāofēngqī zěnme qù huǒchēzhàn zuì kuài?", "vi": "Giờ cao điểm tan tầm đi đến ga tàu thế nào nhanh nhất?", "ans": "C", "explain": "Khuyên đi tàu điện ngầm để tránh tắc đường."},
                {"num": 24, "text": "桌子上少了一套餐具，怎么办？", "py": "Zhuōzi shang shǎo le yí tào cānjù, zěnme bàn?", "vi": "Trên bàn thiếu mất một bộ dụng cụ ăn, làm sao đây?", "ans": "D", "explain": "Nhờ phục vụ mang thêm đũa và cốc."},
                {"num": 25, "text": "聚餐时怎么不给老李倒酒呢？", "py": "Jùcān shí zěnme bù gěi lǎo Lǐ dào jiǔ ne?", "vi": "Lúc liên hoan sao không rót rượu cho anh Lý thế?", "ans": "E", "explain": "Vì anh ấy lái xe đến nên không được uống."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "借", "py": "jiè", "vi": "mượn, vay"},
                {"id": "B", "zh": "还", "py": "huán", "vi": "trả lại"},
                {"id": "C", "zh": "关", "py": "guān", "vi": "đóng, tắt"},
                {"id": "D", "zh": "习惯", "py": "xíguàn", "vi": "thói quen, quen với"},
                {"id": "E", "zh": "双", "py": "shuāng", "vi": "đôi, cặp"}
            ],
            "questions": [
                {"num": 26, "prefix": "离开房间的时候请把门和窗户", "suffix": "好。", "py": "Líkāi fángjiān de shíhou qǐng bǎ mén hé chuānghu ( ? ) hǎo.", "vi": "Lúc rời khỏi phòng xin hãy ( ? ) kỹ cửa chính và cửa sổ.", "ans": "C", "word": "关", "explain": "Đóng cửa (关门)."},
                {"num": 27, "prefix": "我想向你", "suffix": "一下这本词典，用完马上还。", "py": "Wǒ xiǎng xiàng nǐ ( ? ) yíxià zhè běn cídiǎn, yòng wán mǎshàng huán.", "vi": "Tôi muốn ( ? ) bạn cuốn từ điển này một chút, dùng xong trả ngay.", "ans": "A", "word": "借", "explain": "Mượn sách (借词典)."},
                {"num": 28, "prefix": "早睡早起是一个非常好的生活", "suffix": "。", "py": "Zǎoshuì zǎoqǐ shì yí ge fēicháng hǎo de shēnghuó ( ? ).", "vi": "Ngủ sớm dậy sớm là một ( ? ) sinh hoạt rất tốt.", "ans": "D", "word": "习惯", "explain": "Thói quen tốt (好习惯)."},
                {"num": 29, "prefix": "服务员，请给我拿一", "suffix": "筷子。", "py": "Fúwùyuán, qǐng gěi wǒ ná yì ( ? ) kuàizi.", "vi": "Phục vụ ơi, lấy giúp tôi một ( ? ) đũa.", "ans": "E", "word": "双", "explain": "Lượng từ: 一双筷子 (một đôi đũa)."},
                {"num": 30, "prefix": "上次借你的五百块钱，我现在", "suffix": "给你。", "py": "Shàng cì jiè nǐ de wǔbǎi kuài qián, wǒ xiànzài ( ? ) gěi nǐ.", "vi": "Lần trước vay bạn 500 tệ, bây giờ tôi ( ? ) lại cho bạn.", "ans": "B", "word": "还", "explain": "Trả tiền: 还钱 (huán qián)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "王经理每天下班前都有一个好习惯：他会认真检查办公室的门窗，把所有的灯和电脑都关上，最后把空调也关了。有时候新员工急着走，忘了关空调，王经理就会提醒他们：“保护环境，节约用电，这是我们每个人的责任，离开前别忘了把空调关了。”在王经理的影响下，现在公司里的每个员工下班前都会主动把电器关好。",
            "passage_py": "Wáng jīnglǐ měitiān xiàbān qián dōu yǒu yí ge hǎo xíguàn: tā huì rènzhēn jiǎnchá bàngōngshì de ménchuāng, bǎ suǒyǒu de dēng hé diànnǎo dōu guānshang, zuìhòu bǎ kōngtiáo yě guān le. Yǒushíhou xīn yuángōng jízhe zǒu, wàng le guān kōngtiáo, Wáng jīnglǐ jiù huì tíxǐng tāmen: 'Bǎohù huánjìng, jiéyuē yòngdiàn, zhè shì wǒmen měi ge rén de zérèn, líkāi qián bié wàng le bǎ kōngtiáo guān le.' Zài Wáng jīnglǐ de yǐngxiǎng xià, xiànzài gōngsī li de měi ge yuángōng xiàbān qián dōu huì zhǔdòng bǎ diànqì guānhǎo.",
            "passage_vi": "Giám đốc Vương mỗi ngày trước khi tan làm đều có một thói quen rất tốt: ông sẽ cẩn thận kiểm tra cửa sổ và cửa ra vào văn phòng, tắt toàn bộ đèn và máy tính, cuối cùng tắt luôn cả máy điều hòa. Thỉnh thoảng nhân viên mới vội về, quên tắt điều hòa, giám đốc Vương sẽ nhắc nhở họ: 'Bảo vệ môi trường, tiết kiệm điện năng, đây là trách nhiệm của mỗi người chúng ta, trước khi rời đi đừng quên tắt điều hòa nhé.' Dưới sự ảnh hưởng của giám đốc Vương, giờ đây mọi nhân viên trong công ty trước khi tan làm đều chủ động tắt hết các thiết bị điện.",
            "questions": [
                {
                    "num": 31,
                    "text": "王经理每天下班前有什么习惯？",
                    "options": ["A. 去饭馆吃饭", "B. 检查并关好门窗、电脑和空调", "C. 在办公室看电影"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 认真检查办公室的门窗，把所有的灯和电脑都关上，最后把空调也关了."
                },
                {
                    "num": 32,
                    "text": "有时候新员工会忘记做什么？",
                    "options": ["A. 忘记带包", "B. 忘记关空调", "C. 忘记锁门"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 有时候新员工急着走，忘了关空调."
                },
                {
                    "num": 33,
                    "text": "王经理觉得节约用电是谁的责任？",
                    "options": ["A. 经理一个人的", "B. 每个人的", "C. 保安人员的"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 这是我们每个人的责任."
                },
                {
                    "num": 34,
                    "text": "受到王经理的影响后，员工们怎么样了？",
                    "options": ["A. 经常迟到", "B. 主动把电器关好", "C. 不想上班"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 每个员工下班前都会主动把电器关好."
                },
                {
                    "num": 35,
                    "text": "这段话主要告诉我们什么？",
                    "options": ["A. 开空调身体好", "B. 要养成离开关电的好习惯", "C. 电脑容易坏"],
                    "ans": "B",
                    "explain": "Thông điệp chính: Hình thành thói quen tốt tắt thiết bị điện khi rời đi."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["别忘了", "把空调", "关了"],
                "ans": "别忘了把空调关了。",
                "py": "Bié wàng le bǎ kōngtiáo guān le.",
                "vi": "Đừng quên tắt máy điều hòa nhé."
            },
            {
                "num": 37,
                "chunks": ["请把学生证", "给我", "一下"],
                "ans": "请把学生证给我一下。",
                "py": "Qǐng bǎ xuéshengzhèng gěi wǒ yíxià.",
                "vi": "Xin hãy đưa thẻ sinh viên cho tôi một chút."
            },
            {
                "num": 38,
                "chunks": ["作业做完了", "我把", "再去玩儿"],
                "ans": "我把作业做完了再去玩儿。",
                "py": "Wǒ bǎ zuòyè zuòwán le zài qù wánr.",
                "vi": "Tôi làm xong bài tập rồi mới đi chơi."
            },
            {
                "num": 39,
                "chunks": ["二十分钟左右", "坐地铁", "就到了"],
                "ans": "坐地铁二十分钟左右就到了。",
                "py": "Zuò dìtiě èrshí fēnzhōng zuǒyòu jiù dào le.",
                "vi": "Đi tàu điện ngầm khoảng chừng 20 phút là tới rồi."
            },
            {
                "num": 40,
                "chunks": ["把酒喝了", "开车来的", "千万别", "他"],
                "ans": "他开车来的，千万别把酒喝了。",
                "py": "Tā kāichē lái de, qiānwàn bié bǎ jiǔ hē le.",
                "vi": "Anh ấy lái xe đến, tuyệt đối đừng uống rượu."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "离开前请 (guān) 好电灯。",
                "pinyin": "guān",
                "ans": "关",
                "vi": "Trước khi rời đi xin hãy tắt đèn điện."
            },
            {
                "num": 42,
                "sentence": "我从图书馆 (jiè) 了一本书。",
                "pinyin": "jiè",
                "ans": "借",
                "vi": "Tôi đã mượn một cuốn sách từ thư viện."
            },
            {
                "num": 43,
                "sentence": "坐 (dìtiě) 既快又方便。",
                "pinyin": "dìtiě",
                "ans": "地铁",
                "vi": "Đi tàu điện ngầm vừa nhanh vừa tiện."
            },
            {
                "num": 44,
                "sentence": "喝一 (píng) 啤酒解解渴。",
                "pinyin": "píng",
                "ans": "瓶",
                "vi": "Uống một chai bia giải khát."
            },
            {
                "num": 45,
                "sentence": "每天运动是一个好 (xíguàn)。",
                "pinyin": "xíguàn",
                "ans": "习惯",
                "vi": "Mỗi ngày vận động là một thói quen tốt."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "借", "py": "jiè", "pos": "động từ", "vi": "mượn, vay", "eg": "我向朋友借了一辆车。"},
            {"num": 2, "zh": "还", "py": "huán", "pos": "động từ", "vi": "trả lại, hoàn trả", "eg": "借的书要按时还。"},
            {"num": 3, "zh": "关", "py": "guān", "pos": "động từ", "vi": "đóng, tắt", "eg": "请把门关上。"},
            {"num": 4, "zh": "灯", "py": "dēng", "pos": "danh từ", "vi": "đèn", "eg": "屋子里太暗了，开灯吧。"},
            {"num": 5, "zh": "会议", "py": "huìyì", "pos": "danh từ", "vi": "cuộc họp, hội nghị", "eg": "今天下午有一个重要会议。"},
            {"num": 6, "zh": "结束", "py": "jiéshù", "pos": "động từ", "vi": "kết thúc", "eg": "考试在五点钟结束。"},
            {"num": 7, "zh": "忘记", "py": "wàngjì", "pos": "động từ", "vi": "quên, lãng quên", "eg": "别忘记带雨伞。"},
            {"num": 8, "zh": "空调", "py": "kōngtiáo", "pos": "danh từ", "vi": "máy điều hòa nhiệt độ", "eg": "房间里开着空调很舒服。"},
            {"num": 9, "zh": "地铁", "py": "dìtiě", "pos": "danh từ", "vi": "tàu điện ngầm", "eg": "我们坐地铁去市中心。"},
            {"num": 10, "zh": "双", "py": "shuāng", "pos": "lượng từ", "vi": "đôi, cặp", "eg": "我买了一双新皮鞋。"},
            {"num": 11, "zh": "筷子", "py": "kuàizi", "pos": "danh từ", "vi": "đũa", "eg": "中国人吃饭习惯用筷子。"},
            {"num": 12, "zh": "啤酒", "py": "píjiǔ", "pos": "danh từ", "vi": "bia", "eg": "夏天喝冰啤酒真痛快。"},
            {"num": 13, "zh": "瓶子", "py": "píngzi", "pos": "danh từ", "vi": "chai, lọ, bình", "eg": "桌子上有一个空瓶子。"},
            {"num": 14, "zh": "笔记本", "py": "bǐjìběn", "pos": "danh từ", "vi": "vở ghi chép, laptop", "eg": "我带了笔记本电脑。"},
            {"num": 15, "zh": "电子邮件", "py": "diànzǐ yóujiàn", "pos": "danh từ", "vi": "thư điện tử, email", "eg": "请查收我发给你的电子邮件。"},
            {"num": 16, "zh": "习惯", "py": "xíguàn", "pos": "danh từ/động từ", "vi": "thói quen, quen với", "eg": "我已经习惯了这里的气候。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu chữ “把” cơ bản: Chủ ngữ + 把 + Tân ngữ + Động từ + Thành phần khác",
                "desc": "Câu chữ 把 dùng để diễn đạt chủ ngữ thông qua một hành động tác động lên tân ngữ xác định, làm cho tân ngữ đó có sự thay đổi vị trí, trạng thái hoặc kết quả.",
                "examples": [
                    {"zh": "别忘了把空调关了。", "py": "Bié wàng le bǎ kōngtiáo guān le.", "vi": "Đừng quên tắt máy điều hòa."},
                    {"zh": "请把书还给图书馆。", "py": "Qǐng bǎ shū huán gěi túshūguǎn.", "vi": "Xin hãy trả sách cho thư viện."},
                    {"zh": "我把作业写完了。", "py": "Wǒ bǎ zuòyè xiěwán le.", "vi": "Tôi đã làm xong bài tập rồi."}
                ]
            },
            {
                "title": "2. Biểu thị số lượng ước chừng với “左右”",
                "desc": "Đặt sau số từ + lượng từ hoặc từ chỉ thời gian để biểu thị khoảng chừng, xấp xỉ (khoảng...)",
                "examples": [
                    {"zh": "坐地铁需要半个小时左右。", "py": "Zuò dìtiě xūyào bàn ge xiǎoshí zuǒyòu.", "vi": "Đi tàu điện ngầm cần khoảng chừng nửa tiếng."},
                    {"zh": "他大概二十岁左右。", "py": "Tā dàgài èrshí suì zuǒyòu.", "vi": "Anh ấy khoảng chừng 20 tuổi."}
                ]
            }
        ]
    },

    # ==================== BÀI 12 ====================
    {
        "id": 12,
        "title_zh": "把重要的东西放在我这儿吧。",
        "title_py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr ba.",
        "title_vi": "Hãy để những đồ quan trọng ở chỗ tôi đi.",
        "dialogues": [
            {
                "title": "Đoạn 1: 准备出差 (Chuẩn bị đi công tác)",
                "location": "在收拾行李",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "你的护照和机票都带了吗？", "py": "Nǐ de hùzhào hé jīpiào dōu dài le ma?", "vi": "Hộ chiếu và vé máy bay của anh mang đủ chưa?"},
                    {"speaker": "小刚", "role": "male", "zh": "都在行李箱里呢，放心吧。", "py": "Dōu zài xínglǐxiāng li ne, fàngxīn ba.", "vi": "Đều để trong vali cả rồi, em yên tâm đi."},
                    {"speaker": "小丽", "role": "female", "zh": "行李箱要托运，把重要的东西放在我这儿的包里吧。", "py": "Xínglǐxiāng yào tuōyùn, bǎ zhòngyào de dōngxi fàng zài wǒ zhèr de bāo li ba.", "vi": "Vali phải gửi hàng lý ký gửi đấy, hãy để những đồ quan trọng vào chiếc túi chỗ em đây này."},
                    {"speaker": "小刚", "role": "male", "zh": "你说得对，还是随身带着最安全。", "py": "Nǐ shuō de duì, háishì suíshēn dàizhe zuì ānquán.", "vi": "Em nói đúng, mang theo người vẫn là an toàn nhất."}
                ]
            },
            {
                "title": "Đoạn 2: 去机场路上 (Trên đường ra sân bay)",
                "location": "在出租车上",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "师傅，请问到机场还要多久？", "py": "Shīfu, qǐngwèn dào jīchǎng hái yào duōjiǔ?", "vi": "Bác tài ơi, xin hỏi đến sân bay còn mất bao lâu nữa ạ?"},
                    {"speaker": "司机", "role": "female", "zh": "只要不堵车，半个小时就能到。", "py": "Zhǐyào bù dǔchē, bàn ge xiǎoshí jiù néng dào.", "vi": "Chỉ cần không kẹt xe thì nửa tiếng là đến nơi thôi."},
                    {"speaker": "小刚", "role": "male", "zh": "飞机还有两个小时起飞，我们时间挺充分的。", "py": "Fēijī hái yǒu liǎng ge xiǎoshí qǐfēi, wǒmen shíjiān tǐng chōngfèn de.", "vi": "Máy bay còn 2 tiếng nữa mới cất cánh, thời gian của chúng mình khá dư dả."},
                    {"speaker": "司机", "role": "female", "zh": "别着急，我走机场高速，保证按时送到！", "py": "Bié zháojí, wǒ zǒu jīchǎng gāosù, bǎozhèng ànshí sòngdào!", "vi": "Đừng vội, tôi đi đường cao tốc sân bay, đảm bảo đưa tới đúng giờ!"}
                ]
            },
            {
                "title": "Đoạn 3: 在教室画画 (Vẽ tranh trong lớp)",
                "location": "在美术教室",
                "lines": [
                    {"speaker": "老师", "role": "male", "zh": "同学们，今天我们画日落。", "py": "Tóngxuémen, jīntiān wǒmen huà rìluò.", "vi": "Các em học sinh, hôm nay chúng ta vẽ cảnh hoàng hôn lặn nhé."},
                    {"speaker": "学生", "role": "female", "zh": "老师，太阳是从西边落下的吗？", "py": "Lǎoshī, tàiyáng shì cóng xībiān luòxià de ma?", "vi": "Thưa thầy, mặt trời là lặn từ phía tây phải không ạ?"},
                    {"speaker": "老师", "role": "male", "zh": "是的，大家把太阳画在黑板的左边，把山画在下面。", "py": "Shì de, dàjiā bǎ tàiyáng huà zài hēibǎn de zuǒbian, bǎ shān huà zài xiàmian.", "vi": "Đúng rồi, các em hãy vẽ mặt trời ở bên trái bảng đen, vẽ núi ở phía dưới."},
                    {"speaker": "学生", "role": "female", "zh": "看我画的红太阳，多漂亮啊！", "py": "Kàn wǒ huà de hóng tàiyáng, duō piàoliang a!", "vi": "Xem vầng mặt trời đỏ em vẽ này, đẹp biết bao!"}
                ]
            },
            {
                "title": "Đoạn 4: 找行李箱 (Tìm vali)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "奇怪，我的行李箱怎么不见了？", "py": "Qíguài, wǒ de xínglǐxiāng zěnme bú jiàn le?", "vi": "Kỳ lạ thật, vali của anh sao lại không thấy đâu nữa rồi?"},
                    {"speaker": "小丽", "role": "female", "zh": "你别生气，自己想想刚才放在哪儿了？", "py": "Nǐ bié shēngqì, zìjǐ xiǎngxiang gāngcái fàng zài nǎr le?", "vi": "Anh đừng nóng giận, tự mình nhớ lại xem vừa nãy để ở đâu?"},
                    {"speaker": "小刚", "role": "male", "zh": "我记起来了，我把它放在卧室衣柜旁边了。", "py": "Wǒ jì qǐlái le, wǒ bǎ tā fàng zài wòshì yīguì pángbiān le.", "vi": "Anh nhớ ra rồi, anh đã để nó ở cạnh tủ quần áo trong phòng ngủ rồi."},
                    {"speaker": "小丽", "role": "female", "zh": "找到了就好，快去拿出来吧。", "py": "Zhǎodào le jiù hǎo, kuài qù ná chūlái ba.", "vi": "Tìm thấy là tốt rồi, mau vào lấy ra đi anh."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：把你的护照和机票放在我的小包里吧。 男：好的，给你，这样最安全。",
                "question": "男的把护照放在哪儿了？",
                "options": ["A. 行李箱里", "B. 女的小包里", "C. 口袋里"],
                "ans": "B",
                "explain": "Để hộ chiếu vào túi nhỏ của người nữ: 放在我的小包里."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "只要路上不堵车，我们半个小时就能赶到机场。",
                "question": "Phán đoán đúng hay sai: 路上如果堵车，半小时也能到。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Điều kiện là chỉ khi KHÔNG kẹt xe mới đến trong nửa tiếng (只要不堵车)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：太阳是从哪边升起，从哪边落下的？ 女：太阳从东边升起，从西边落下。",
                "question": "太阳从哪边落下？",
                "options": ["A. 东边", "B. 西边", "C. 南边"],
                "ans": "B",
                "explain": "Mặt trời lặn ở phía tây (从西边落下)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：你的行李箱找到了吗？ 男：找到了，刚才被我放在卧室衣柜旁边了。",
                "question": "行李箱在哪儿找到的？",
                "options": ["A. 卧室衣柜旁边", "B. 门外", "C. 客厅桌子下"],
                "ans": "A",
                "explain": "Vali ở cạnh tủ quần áo phòng ngủ (卧室衣柜旁边)."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "把重要的证件和钱放在随身带的小包里吧。", "py": "Bǎ zhòngyào de zhèngjiàn hé qián fàng zài suíshēn dài de xiǎobāo li ba.", "vi": "Hãy để giấy tờ quan trọng và tiền vào chiếc túi nhỏ mang theo bên người."},
                {"id": "B", "text": "只要努力复习，就一定能通过考试。", "py": "Zhǐyào nǔlì fùxí, jiù yídìng néng tōngguò kǎoshì.", "vi": "Chỉ cần chăm chỉ ôn tập thì nhất định có thể vượt qua kỳ thi."},
                {"id": "C", "text": "飞机还有一个多小时才起飞呢，不用着急。", "py": "Fēijī hái yǒu yí ge duō xiǎoshí cái qǐfēi ne, bú yòng zháojí.", "vi": "Máy bay còn hơn một tiếng nữa mới cất cánh, không cần vội."},
                {"id": "D", "text": "老师把今天的新生词写在黑板上了。", "py": "Lǎoshī bǎ jīntiān de xīn shēngcí xiě zài hēibǎn shang le.", "vi": "Thầy giáo đã viết từ mới của ngày hôm nay lên bảng đen rồi."},
                {"id": "E", "text": "有话好好说，你别动不动就生气。", "py": "Yǒu huà hǎohǎo shuō, nǐ bié dòngbudòng jiù shēngqì.", "vi": "Có chuyện gì thì bình tĩnh nói, cậu đừng hơi tí là nổi giận."}
            ],
            "questions": [
                {"num": 21, "text": "去机场托运行李时要注意什么？", "py": "Qù jīchǎng tuōyùn xínglǐ shí yào zhùyì shénme?", "vi": "Khi đi sân bay gửi hành lý ký gửi cần chú ý điều gì?", "ans": "A", "explain": "Để giấy tờ quan trọng vào túi xách mang theo."},
                {"num": 22, "text": "我真的很想学好汉语，有什么好办法？", "py": "Wǒ zhēn de hěn xiǎng xuéhǎo hànyǔ, yǒu shénme hǎo bànfǎ?", "vi": "Tôi thực sự rất muốn học giỏi tiếng Hán, có cách gì hay không?", "ans": "B", "explain": "Chỉ cần nỗ lực ôn tập nhất định sẽ đỗ (只要……就……)."},
                {"num": 23, "text": "快点儿开车，不然赶不上航班了！", "py": "Kuài diǎnr kāichē, bùrán gǎnbushàng hángbān le!", "vi": "Lái xe nhanh lên, không thì không kịp chuyến bay mất!", "ans": "C", "explain": "Trấn an máy bay còn hơn 1 tiếng nữa mới cất cánh."},
                {"num": 24, "text": "刚才讲的课文重点在哪儿？", "py": "Gāngcái jiǎng de kèwén zhòngdiǎn zài nǎr?", "vi": "Trọng điểm bài giảng vừa rồi ở đâu thế?", "ans": "D", "explain": "Chỉ ra thầy giáo đã ghi từ mới lên bảng đen."},
                {"num": 25, "text": "你怎么又跟同桌吵架了？", "py": "Nǐ zěnme yòu gēn tóngzhuō chǎojià le?", "vi": "Sao cậu lại cãi nhau với bạn cùng bàn rồi?", "ans": "E", "explain": "Khuyên bình tĩnh nói chuyện, đừng dễ nổi giận."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "太阳", "py": "tàiyáng", "vi": "mặt trời"},
                {"id": "B", "zh": "护照", "py": "hùzhào", "vi": "hộ chiếu"},
                {"id": "C", "zh": "生气", "py": "shēngqì", "vi": "tức giận, giận dữ"},
                {"id": "D", "zh": "司机", "py": "sījī", "vi": "tài xế, bác tài"},
                {"id": "E", "zh": "黑板", "py": "hēibǎn", "vi": "bảng đen"}
            ],
            "questions": [
                {"num": 26, "prefix": "出境旅游必须随身带好", "suffix": "。", "py": "Chūjìng lǚyóu bìxū suíshēn dàihǎo ( ? ).", "vi": "Đi du lịch nước ngoài phải mang theo ( ? ) bên mình.", "ans": "B", "word": "护照", "explain": "Hộ chiếu: 护照 (hùzhào)."},
                {"num": 27, "prefix": "早晨的", "suffix": "从东方升起来了。", "py": "Zǎochén de ( ? ) cóng dōngfāng shēng qǐlái le.", "vi": "( ? ) buổi sáng đã mọc lên từ phương Đông.", "ans": "A", "word": "太阳", "explain": "Mặt trời: 太阳 (tàiyáng)."},
                {"num": 28, "prefix": "别", "suffix": "了，事情已经过去了。", "py": "Bié ( ? ) le, shìqing yǐjīng guòqù le.", "vi": "Đừng ( ? ) nữa, chuyện đã qua rồi.", "ans": "C", "word": "生气", "explain": "Tức giận: 生气 (shēngqì)."},
                {"num": 29, "prefix": "出租车", "suffix": "热情地帮乘客把行李搬上车。", "py": "Chūzūchē ( ? ) rèqíng de bāng chéngkè bǎ xínglǐ bān shàng chē.", "vi": "( ? ) taxi nhiệt tình giúp hành khách chuyển hành lý lên xe.", "ans": "D", "word": "司机", "explain": "Tài xế: 司机 (sījī)."},
                {"num": 30, "prefix": "请大家看着", "suffix": "，听老师讲课。", "py": "Qǐng dàjiā kànzhe ( ? ), tīng lǎoshī jiǎngkè.", "vi": "Xin mọi người nhìn lên ( ? ), nghe thầy giảng bài.", "ans": "E", "word": "黑板", "explain": "Bảng đen: 黑板 (hēibǎn)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "明天小明就要去国外留学了。今天晚上，全家人都在帮他收拾行李。妈妈把准备好的几件厚衣服整齐地放进大行李箱里。爸爸对小明说：“把护照、身份证、录取通知书和手机放在随身带的小背包里，千万别弄丢了。”小明认真地点了点头，把重要的证件都放进了小包。爸爸还告诉他：“只要在国外努力学习，照顾好自己，我们就会为你感到骄傲。”",
            "passage_py": "Míngtiān Xiǎomíng jiù yào qù guówài liúxué le. Jīntiān wǎnshang, quán jiā rén dōu zài bāng tā shōushi xínglǐ. Māma bǎ zhǔnbèihǎo de jǐ jiàn hòu yīfu zhěngqí de fàng jìn dà xínglǐxiāng li. Bàba duì Xiǎomíng shuō: 'Bǎ hùzhào, shēnfènzhèng, lùqǔ tōngzhīshū hé shǒujī fàng zài suíshēn dài de xiǎo bèibāo li, qiānwàn bié nòngdiū le.' Xiǎomíng rènzhēn de diǎn le diǎn tóu, bǎ zhòngyào de zhèngjiàn dōu fàng jìn le xiǎobāo. Bàba hái gàosu tā: 'Zhǐyào zài guówài nǔlì xuéxí, zhàogù hǎo zìjǐ, wǒmen jiù huì wèi nǐ gǎndào jiāo'ào.'",
            "passage_vi": "Ngày mai Tiểu Minh sắp ra nước ngoài du học rồi. Tối nay, cả gia đình đều đang giúp cậu thu dọn hành lý. Mẹ xếp gọn gàng mấy chiếc áo ấm đã chuẩn bị vào chiếc vali to. Bố dặn Tiểu Minh: 'Hãy để hộ chiếu, chứng minh thư, giấy báo nhập học và điện thoại vào chiếc balo nhỏ mang theo người, tuyệt đối đừng làm mất đấy.' Tiểu Minh nghiêm túc gật đầu, cất hết các giấy tờ quan trọng vào túi nhỏ. Bố còn bảo cậu: 'Chỉ cần con nỗ lực học tập ở nước ngoài và biết tự chăm sóc tốt bản thân, bố mẹ sẽ luôn tự hào về con.'",
            "questions": [
                {
                    "num": 31,
                    "text": "小明明天打算去做什么？",
                    "options": ["A. 去旅游", "B. 去国外留学", "C. 去医院看病"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 明天小明就要去国外留学了."
                },
                {
                    "num": 32,
                    "text": "妈妈把厚衣服放在哪儿了？",
                    "options": ["A. 大行李箱里", "B. 小背包里", "C. 床底下"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 放进大行李箱里."
                },
                {
                    "num": 33,
                    "text": "爸爸让小明把护照放在哪儿？",
                    "options": ["A. 大行李箱里", "B. 随身带的小背包里", "C. 家里桌子上"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 放在随身带的小背包里."
                },
                {
                    "num": 34,
                    "text": "为什么要把重要证件放在小背包里？",
                    "options": ["A. 因为行李箱太重", "B. 随身带着最安全，怕弄丢", "C. 方便别人看"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 千万别弄丢了."
                },
                {
                    "num": 35,
                    "text": "爸爸对小明有什么期望？",
                    "options": ["A. 只要努力学习并照顾好自己就行", "B. 每天都必须给家里打电话", "C. 毕业后立刻回国工作"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 只要在国外努力学习，照顾好自己..."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["放在我这儿吧", "把重要的东西"],
                "ans": "把重要的东西放在我这儿吧。",
                "py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr ba.",
                "vi": "Hãy để những thứ quan trọng ở chỗ tôi đi."
            },
            {
                "num": 37,
                "chunks": ["半个小时", "只要不堵车", "就能到机场"],
                "ans": "只要不堵车半个小时就能到机场。",
                "py": "Zhǐyào bù dǔchē bàn ge xiǎoshí jiù néng dào jīchǎng.",
                "vi": "Chỉ cần không kẹt xe thì nửa tiếng là đến được sân bay."
            },
            {
                "num": 38,
                "chunks": ["写在黑板上", "老师把生词"],
                "ans": "老师把生词写在黑板上。",
                "py": "Lǎoshī bǎ shēngcí xiě zài hēibǎn shang.",
                "vi": "Thầy giáo viết từ mới lên bảng đen."
            },
            {
                "num": 39,
                "chunks": ["放在行李箱里", "把护照和机票", "他"],
                "ans": "他把护照和机票放在行李箱里。",
                "py": "Tā bǎ hùzhào hé jīpiào fàng zài xínglǐxiāng li.",
                "vi": "Anh ấy để hộ chiếu và vé máy bay vào trong vali."
            },
            {
                "num": 40,
                "chunks": ["从西边", "慢慢地", "太阳落下了"],
                "ans": "太阳从西边慢慢地落下了。",
                "py": "Tàiyáng cóng xībiān mànmàn de luòxià le.",
                "vi": "Mặt trời từ từ lặn xuống ở phía tây."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "早晨 (tàiyáng) 升起来了。",
                "pinyin": "tàiyáng",
                "ans": "太阳",
                "vi": "Buổi sớm mặt trời đã mọc lên."
            },
            {
                "num": 42,
                "sentence": "出国需要办 (hùzhào)。",
                "pinyin": "hùzhào",
                "ans": "护照",
                "vi": "Ra nước ngoài cần phải làm hộ chiếu."
            },
            {
                "num": 43,
                "sentence": "别 (shēngqì) 了，笑一笑吧。",
                "pinyin": "shēngqì",
                "ans": "生气",
                "vi": "Đừng giận nữa, hãy cười lên một chút nào."
            },
            {
                "num": 44,
                "sentence": "这是我 (zìjǐ) 做的决定。",
                "pinyin": "zìjǐ",
                "ans": "自己",
                "vi": "Đây là quyết định do chính bản thân tôi đưa ra."
            },
            {
                "num": 45,
                "sentence": "老师在 (hēibǎn) 上写字。",
                "pinyin": "hēibǎn",
                "ans": "黑板",
                "vi": "Thầy giáo viết chữ lên bảng đen."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "太阳", "py": "tàiyáng", "pos": "danh từ", "vi": "mặt trời", "eg": "太阳晒在身上暖洋洋的。"},
            {"num": 2, "zh": "西", "py": "xī", "pos": "danh từ chỉ phương vị", "vi": "hướng tây, phía tây", "eg": "太阳从西边落下。"},
            {"num": 3, "zh": "生气", "py": "shēngqì", "pos": "động từ/tính từ", "vi": "tức giận, giận hờn", "eg": "别生他的气了。"},
            {"num": 4, "zh": "行李箱", "py": "xínglǐxiāng", "pos": "danh từ", "vi": "va-li, hòm đựng hành lý", "eg": "这个大行李箱很结实。"},
            {"num": 5, "zh": "自己", "py": "zìjǐ", "pos": "đại từ", "vi": "bản thân, tự mình", "eg": "自己的事情自己做。"},
            {"num": 6, "zh": "包", "py": "bāo", "pos": "danh từ/động từ", "vi": "túi xách, bao gói", "eg": "我把钱包放进背包里了。"},
            {"num": 7, "zh": "发现", "py": "fāxiàn", "pos": "động từ", "vi": "phát hiện, nhận ra", "eg": "我突然发现钥匙不见了。"},
            {"num": 8, "zh": "护照", "py": "hùzhào", "pos": "danh từ", "vi": "hộ chiếu", "eg": "出国前要检查护照有效期。"},
            {"num": 9, "zh": "起飞", "py": "qǐfēi", "pos": "động từ", "vi": "cất cánh", "eg": "飞机马上就要起飞了。"},
            {"num": 10, "zh": "司机", "py": "sījī", "pos": "danh từ", "vi": "tài xế, lái xe", "eg": "出租车司机对路线非常熟悉。"},
            {"num": 11, "zh": "教", "py": "jiāo", "pos": "động từ", "vi": "dạy dỗ, giảng dạy", "eg": "张老师教我们三年级数学。"},
            {"num": 12, "zh": "画", "py": "huà", "pos": "động từ/danh từ", "vi": "vẽ, bức tranh", "eg": "他画了一只可爱的小猫。"},
            {"num": 13, "zh": "需要", "py": "xūyào", "pos": "động từ/danh từ", "vi": "cần, nhu cầu", "eg": "学好外语需要多加练习。"},
            {"num": 14, "zh": "黑板", "py": "hēibǎn", "pos": "danh từ", "vi": "bảng đen", "eg": "请看黑板上的例句。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu chữ “把” mang bổ ngữ nơi chốn: S + 把 + O + Động từ + 在 / 到 + Nơi chốn",
                "desc": "Dùng để biểu thị hành động tác động làm cho sự vật di chuyển và lưu lại ở một vị trí cụ thể.",
                "examples": [
                    {"zh": "把重要的东西放在我这儿吧。", "py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr ba.", "vi": "Hãy để những thứ quan trọng ở chỗ tôi đi."},
                    {"zh": "老师把字写在黑板上。", "py": "Lǎoshī bǎ zì xiě zài hēibǎn shang.", "vi": "Thầy giáo viết chữ lên bảng đen."},
                    {"zh": "请把车停在门外。", "py": "Qǐng bǎ chē tíng zài mén wài.", "vi": "Xin hãy đỗ xe ở bên ngoài cửa."}
                ]
            },
            {
                "title": "2. Cặp liên từ điều kiện: “只要……就……”",
                "desc": "Biểu thị điều kiện đầy đủ: 'Chỉ cần có điều kiện này thì ắt sẽ đạt được kết quả ở vế sau'.",
                "examples": [
                    {"zh": "只要不堵车，半个小时就能到。", "py": "Zhǐyào bù dǔchē, bàn ge xiǎoshí jiù néng dào.", "vi": "Chỉ cần không kẹt xe thì nửa tiếng là đến nơi."},
                    {"zh": "只要努力，就一定能学会。", "py": "Zhǐyào nǔlì, jiù yídìng néng xuéhuì.", "vi": "Chỉ cần chăm chỉ thì nhất định có thể học được."}
                ]
            }
        ]
    },

    # ==================== BÀI 13 ====================
    {
        "id": 13,
        "title_zh": "我是走回来的。",
        "title_py": "Wǒ shì zǒu huílái de.",
        "title_vi": "Anh đi bộ về.",
        "dialogues": [
            {
                "title": "Đoạn 1: 回家见到爷爷奶奶 (Về nhà gặp ông bà)",
                "location": "在家门口",
                "lines": [
                    {"speaker": "奶奶", "role": "female", "zh": "小刚，你怎么一身大汗？怎么回来的？", "py": "Xiǎogāng, nǐ zěnme yì shēn dàhàn? Zěnme huílái de?", "vi": "Tiểu Cương, sao cháu mồ hôi đầm đìa thế kia? Về bằng gì đấy?"},
                    {"speaker": "小刚", "role": "male", "zh": "奶奶，我是走回来的，路上顺便锻炼身体。", "py": "Nǎinai, wǒ shì zǒu huílái de, lùshang shùnbiàn duànliàn shēntǐ.", "vi": "Bà ơi, cháu đi bộ về đấy ạ, trên đường tiện thể rèn luyện sức khỏe luôn."},
                    {"speaker": "爷爷", "role": "male", "zh": "年轻人多走走好，快坐下来喝口热茶。", "py": "Niánqīngrén duō zǒuzou hǎo, kuài zuò xiàlái hē kǒu rèchá.", "vi": "Người trẻ đi lại nhiều là tốt, mau ngồi xuống uống ngụm trà nóng đi cháu."},
                    {"speaker": "小刚", "role": "male", "zh": "爷爷奶奶，我还给你们买了一盒点心当礼物呢！", "py": "Yéye nǎinai, wǒ hái gěi nǐmen mǎi le yì hé diǎnxin dāng lǐwù ne!", "vi": "Ông bà ơi, cháu còn mua tặng ông bà một hộp bánh điểm tâm làm quà nữa này!"}
                ]
            },
            {
                "title": "Đoạn 2: 路上遇到老朋友 (Gặp bạn cũ trên đường)",
                "location": "在街上",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "真巧啊，没想到在这里遇到你！", "py": "Zhēn qiǎo a, méi xiǎngdào zài zhèlǐ yùdào nǐ!", "vi": "Khéo thật đấy, không ngờ lại gặp cậu ở đây!"},
                    {"speaker": "老同学", "role": "female", "zh": "是啊，几年不见，你越来越精神了。", "py": "Shì a, jǐ nián bú jiàn, nǐ yuè lái yuè jīngshen le.", "vi": "Đúng thế, mấy năm không gặp trông cậu ngày càng phong độ ra đấy."},
                    {"speaker": "小刚", "role": "male", "zh": "我们一边走一边聊吧，你现在在哪儿工作？", "py": "Wǒmen yìbiān zǒu yìbiān liáo ba, nǐ xiànzài zài nǎr gōngzuò?", "vi": "Chúng mình vừa đi vừa nói chuyện nhé, cậu bây giờ làm việc ở đâu?"},
                    {"speaker": "老同学", "role": "female", "zh": "我在过去的一所中学当语文老师呢。", "py": "Wǒ zài guòqù de yì suǒ zhōngxué dāng yǔwén lǎoshī ne.", "vi": "Tớ đang làm giáo viên dạy văn ở một trường cấp hai gần đây thôi."}
                ]
            },
            {
                "title": "Đoạn 3: 聊学校生活 (Nói về cuộc sống trường học)",
                "location": "在校长办公室",
                "lines": [
                    {"speaker": "校长", "role": "male", "zh": "新学期开始了，大家在学校生活习惯了吗？", "py": "Xīn xuéqī kāishǐ le, dàjiā zài xuéxiào shēnghuó xíguàn le ma?", "vi": "Học kỳ mới bắt đầu rồi, mọi người sinh hoạt ở trường đã quen chưa?"},
                    {"speaker": "学生", "role": "female", "zh": "校长您好，我们都很适应，食堂饭菜也很好吃。", "py": "Xiàozhǎng nín hǎo, wǒmen dōu hěn shìyìng, shítáng fàncài yě hěn hǎochī.", "vi": "Chào thầy hiệu trưởng ạ, chúng em đều rất thích nghi, cơm nước ở căng tin cũng rất ngon."},
                    {"speaker": "校长", "role": "male", "zh": "遇到任何困难，都应该及时告诉老师。", "py": "Yùdào rènhé kùnnan, dōu yīnggāi jíshí gàosu lǎoshī.", "vi": "Gặp bất kỳ khó khăn gì đều nên kịp thời báo cho thầy cô biết nhé."},
                    {"speaker": "学生", "role": "female", "zh": "谢谢校长关心，我们一定会好好努力学习！", "py": "Xièxie xiàozhǎng guānxīn, wǒmen yídìng huì hǎohǎo nǔlì xuéxí!", "vi": "Cảm ơn thầy hiệu trưởng đã quan tâm, chúng em nhất định sẽ cố gắng học tập thật tốt!"}
                ]
            },
            {
                "title": "Đoạn 4: 谈健康习惯 (Nói về thói quen giữ sức khỏe)",
                "location": "在医院诊室",
                "lines": [
                    {"speaker": "医生", "role": "male", "zh": "你的身体没有什么大问题，就是平时运动太少了。", "py": "Nǐ de shēntǐ méiyǒu shénme dà wèntí, jiù shì píngshí yùndòng tài shǎo le.", "vi": "Cơ thể anh không có vấn đề gì lớn, chỉ là bình thường vận động quá ít thôi."},
                    {"speaker": "患者", "role": "female", "zh": "经常坐办公室，确实很少出去走动。", "py": "Jīngcháng zuò bàngōngshì, quèshí hěn shǎo chūqù zǒudòng.", "vi": "Tôi thường xuyên ngồi văn phòng, đúng là rất ít khi ra ngoài đi lại."},
                    {"speaker": "医生", "role": "male", "zh": "应该多站起来走走，饭后散散步，坏习惯要慢慢改掉。", "py": "Yīnggāi duō zhàn qǐlái zǒuzou, fàn hòu sànsànbù, huài xíguàn yào mànmàn gǎidiào.", "vi": "Nên đứng dậy đi lại nhiều hơn, sau bữa ăn đi dạo một chút, thói quen xấu phải dần sửa đi."},
                    {"speaker": "患者", "role": "female", "zh": "好的医生，我一定听您的建议！", "py": "Hǎo de yīshēng, wǒ yídìng tīng nín de jiànyì!", "vi": "Dạ vâng thưa bác sĩ, tôi nhất định sẽ nghe theo lời khuyên của bác sĩ ạ!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你怎么满头大汗？ 男：今天路上车坏了，我是走回来的。",
                "question": "男的是怎么回来的？",
                "options": ["A. 坐公共汽车", "B. 骑车", "C. 走回来的"],
                "ans": "C",
                "explain": "Người nam trả lời: 我是走回来的 (đi bộ về)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚今天回老家看爷爷奶奶，还给他们带了礼物。",
                "question": "Phán đoán đúng hay sai: 小刚给爷爷奶奶买了礼物。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Đoạn văn nói rõ: 给他们买了一盒点心当礼物."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：老同学，你现在在哪儿工作？ 女：我在一家中学教语文。",
                "question": "女的职业是什么？",
                "options": ["A. 医生", "B. 中学语文老师", "C. 银行职员"],
                "ans": "B",
                "explain": "Cô ấy nói: 在一家中学教语文."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：医生，我需要吃药吗？ 男：不需要，你只要平时多运动就可以了。",
                "question": "医生建议女的做什么？",
                "options": ["A. 多吃药", "B. 多去旅游", "C. 多运动"],
                "ans": "C",
                "explain": "Bác sĩ khuyên: 只要平时多运动就可以了."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "我是走回来的，路上顺便锻炼身体。", "py": "Wǒ shì zǒu huílái de, lùshang shùnbiàn duànliàn shēntǐ.", "vi": "Tôi là đi bộ về đấy, trên đường tiện thể tập thể dục luôn."},
                {"id": "B", "text": "真没想到今天在街上遇到老同学！", "py": "Zhēn méi xiǎngdào jīntiān zài jiē shang yùdào lǎo tóngxué!", "vi": "Thật không ngờ hôm nay lại gặp bạn học cũ trên phố!"},
                {"id": "C", "text": "两个人一边喝茶一边聊天儿，特别开心。", "py": "Liǎng ge rén yìbiān hē chá yìbiān liáotiānr, tèbié kāixīn.", "vi": "Hai người vừa uống trà vừa trò chuyện, đặc biệt vui vẻ."},
                {"id": "D", "text": "校长对学生们的日常生活非常关心。", "py": "Xiàozhǎng duì xuéshengmen de rìcháng shēnghuó fēicháng guānxīn.", "vi": "Thầy hiệu trưởng rất quan tâm đến đời sống hằng ngày của các học sinh."},
                {"id": "E", "text": "久坐对身体不好，应该经常站起来活动一下。", "py": "Jiǔ zuò duì shēntǐ bù hǎo, yīnggāi jīngcháng zhàn qǐlái huódòng yíxià.", "vi": "Ngồi lâu không tốt cho cơ thể, nên thường xuyên đứng dậy vận động một chút."}
            ],
            "questions": [
                {"num": 21, "text": "你怎么满头大汗地跑回来了？", "py": "Nǐ zěnme mǎntóu-dàhàn de pǎo huílái le?", "vi": "Sao cậu lại mồ hôi nhễ nhại chạy về thế kia?", "ans": "A", "explain": "Giải thích mình đi bộ về để rèn luyện thân thể."},
                {"num": 22, "text": "刚才跟你打招呼的那位女士是谁呀？", "py": "Gāngcái gēn nǐ dǎ zhāohu de nà wèi nǚshì shì shéi ya?", "vi": "Người phụ nữ vừa chào bạn lúc nãy là ai thế?", "ans": "B", "explain": "Giới thiệu đó là bạn học cũ tình cờ gặp trên đường."},
                {"num": 23, "text": "你们在休息室聊什么呢，笑得这么开心？", "py": "Nǐmen zài xiūxishì liáo shénme ne, xiào de zhème kāixīn?", "vi": "Các cậu ở phòng nghỉ nói chuyện gì đấy mà cười vui thế?", "ans": "C", "explain": "Đang vừa uống trà vừa nói chuyện phiếm."},
                {"num": 24, "text": "新学期学校对大家有什么要求？", "py": "Xīn xuéqī xuéxiào duì dàjiā yǒu shénme yāoqiú?", "vi": "Học kỳ mới trường học có yêu cầu gì đối với mọi người?", "ans": "D", "explain": "Hiệu trưởng quan tâm chu đáo tới đời sống sinh viên."},
                {"num": 25, "text": "每天坐在电脑前工作，感觉腰酸背痛。", "py": "Měitiān zuò zài diànnǎo qián gōngzuò, gǎnjué yāosuān-bèitòng.", "vi": "Ngày nào cũng ngồi trước máy tính làm việc, cảm thấy đau lưng mỏi cổ.", "ans": "E", "explain": "Khuyên nên đứng dậy đi lại vận động thường xuyên."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "终于", "py": "zhōngyú", "vi": "cuối cùng"},
                {"id": "B", "zh": "礼物", "py": "lǐwù", "vi": "món quà"},
                {"id": "C", "zh": "遇到", "py": "yùdào", "vi": "gặp phải, tình cờ gặp"},
                {"id": "D", "zh": "应该", "py": "yīnggāi", "vi": "nên, cần phải"},
                {"id": "E", "zh": "经常", "py": "jīngcháng", "vi": "thường xuyên"}
            ],
            "questions": [
                {"num": 26, "prefix": "经过两个月的努力，他", "suffix": "通过了考试。", "py": "Jīngguò liǎng ge yuè de nǔlì, tā ( ? ) tōngguò le kǎoshì.", "vi": "Trải qua 2 tháng nỗ lực, cuối cùng anh ấy ( ? ) đã đỗ kỳ thi.", "ans": "A", "word": "终于", "explain": "Cuối cùng: 终于 (zhōngyú)."},
                {"num": 27, "prefix": "这是我给爷爷奶奶买的生日", "suffix": "。", "py": "Zhè shì wǒ gěi yéye nǎinai mǎi de shēngrì ( ? ).", "vi": "Đây là ( ? ) sinh nhật tôi mua tặng ông bà.", "ans": "B", "word": "礼物", "explain": "Món quà: 礼物 (lǐwù)."},
                {"num": 28, "prefix": "今天在商场买东西时我", "suffix": "了小学老师。", "py": "Jīntiān zài shāngchǎng mǎi dōngxi shí wǒ ( ? ) le xiǎoxué lǎoshī.", "vi": "Hôm nay lúc mua sắm ở siêu thị tôi ( ? ) cô giáo tiểu học.", "ans": "C", "word": "遇到", "explain": "Tình cờ gặp: 遇到 (yùdào)."},
                {"num": 29, "prefix": "学生在学校里", "suffix": "认真听讲，完成作业。", "py": "Xuésheng zài xuéxiào li ( ? ) rènzhēn tīngjiǎng, wánchéng zuòyè.", "vi": "Học sinh ở trường ( ? ) nghiêm túc nghe giảng và làm bài tập.", "ans": "D", "word": "应该", "explain": "Nên, phải: 应该 (yīnggāi)."},
                {"num": 30, "prefix": "他身体很好，因为他", "suffix": "去健身房锻炼。", "py": "Tā shēntǐ hěn hǎo, yīnwèi tā ( ? ) qù jiànshēnfáng duànliàn.", "vi": "Sức khỏe anh ấy rất tốt vì anh ấy ( ? ) đến phòng tập rèn luyện.", "ans": "E", "word": "经常", "explain": "Thường xuyên: 经常 (jīngcháng)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "今天下午放学的时候，天空中突然下起了大雨。小刚没有带伞，公共汽车站也挤满了人。等了半天没有坐上车，小刚就决定一个人走回家。虽然路上鞋子和裤子都淋湿了，但是他觉得走在雨中空气特别清新，很舒服。回到家，妈妈看到他满身是水，心疼地问：“你怎么不坐车呢？”小刚笑着说：“今天等车的人太多了，我是走回来的，顺便锻炼锻炼身体！”",
            "passage_py": "Jīntiān xiàwǔ fàngxué de shíhou, tiānkōng zhōng tūrán xià qǐ le dàyǔ. Xiǎogāng méiyǒu dài sǎn, gōnggòng qìchēzhàn yě jǐmǎn le rén. Děng le bàntiān méiyǒu zuò shàng chē, Xiǎogāng jiù juédìng yí ge rén zǒu huí jiā. Suīrán lùshang xiézi hé kùzi dōu línshī le, dànshì tā juéde zǒu zài yǔ zhōng kōngqì tèbié qīngxīn, hěn shūfu. Huídào jiā, māma kàndào tā mǎn shēn shì shuǐ, xīnténg de wèn: 'Nǐ zěnme bú zuò chē ne?' Xiǎogāng xiàozhe shuō: 'Jīntiān děng chē de rén tài duō le, wǒ shì zǒu huílái de, shùnbiàn duànliàn duànliàn shēntǐ!'",
            "passage_vi": "Chiều hôm nay lúc tan học, trên trời đột nhiên đổ một cơn mưa to. Tiểu Cương không mang theo ô, trạm xe buýt cũng chật ních người. Đợi cả buổi không lên được xe, Tiểu Cương quyết định một mình đi bộ về nhà. Tuy trên đường đi giày và quần đều bị nước mưa làm ướt sũng, nhưng cậu cảm thấy đi trong mưa không khí vô cùng trong lành, rất dễ chịu. Về đến nhà, mẹ nhìn thấy người cậu ướt sũng, xót xa hỏi: 'Sao con không đi xe thế?' Tiểu Cương mỉm cười bảo: 'Hôm nay người chờ xe đông quá mẹ ạ, con đi bộ về, tiện thể rèn luyện sức khỏe luôn!'",
            "questions": [
                {
                    "num": 31,
                    "text": "今天下午放学时天气怎么样？",
                    "options": ["A. 出太阳", "B. 下起了大雨", "C. 刮大风"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 天空中突然下起了大雨."
                },
                {
                    "num": 32,
                    "text": "小刚为什么没有坐公共汽车？",
                    "options": ["A. 他没带钱", "B. 等车的人太多，没坐上", "C. 他不喜欢坐公共汽车"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 等了半天没有坐上车，等车的人太多."
                },
                {
                    "num": 33,
                    "text": "小刚是怎么回家的？",
                    "options": ["A. 打出租车回来的", "B. 骑车回来的", "C. 一个人走回家的"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 小刚就决定一个人走回家."
                },
                {
                    "num": 34,
                    "text": "小刚走在雨中感觉怎么样？",
                    "options": ["A. 觉得空气清新很舒服", "B. 觉得很害怕", "C. 特别生气"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 觉得走在雨中空气特别清新，很舒服."
                },
                {
                    "num": 35,
                    "text": "小刚觉得走回家有什么好处？",
                    "options": ["A. 省了车费", "B. 顺便锻炼身体", "C. 可以买好吃的"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 顺便锻炼锻炼身体."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["我是", "走回来的", "今天下午"],
                "ans": "今天下午我是走回来的。",
                "py": "Jīntiān xiàwǔ wǒ shì zǒu huílái de.",
                "vi": "Chiều hôm nay tôi là đi bộ về đấy."
            },
            {
                "num": 37,
                "chunks": ["一边走", "聊聊天儿", "我们一边"],
                "ans": "我们一边走一边聊聊天儿。",
                "py": "Wǒmen yìbiān zǒu yìbiān liáoliao tiānr.",
                "vi": "Chúng mình vừa đi vừa trò chuyện một lát nhé."
            },
            {
                "num": 38,
                "chunks": ["老朋友", "在街上", "遇到了", "我"],
                "ans": "我在街上遇到了老朋友。",
                "py": "Wǒ zài jiē shang yùdào le lǎo péngyou.",
                "vi": "Tôi đã tình cờ gặp lại bạn cũ trên phố."
            },
            {
                "num": 39,
                "chunks": ["买了礼物", "爷爷奶奶", "小刚给"],
                "ans": "小刚给爷爷奶奶买了礼物。",
                "py": "Xiǎogāng gěi yéye nǎinai mǎi le lǐwù.",
                "vi": "Tiểu Cương đã mua quà cho ông bà."
            },
            {
                "num": 40,
                "chunks": ["改掉", "坏习惯", "我们应该"],
                "ans": "我们应该改掉坏习惯。",
                "py": "Wǒmen yīnggāi gǎidiào huài xíguàn.",
                "vi": "Chúng ta nên sửa bỏ thói quen xấu."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我 (zhōngyú) 把作业写完了。",
                "pinyin": "zhōngyú",
                "ans": "终于",
                "vi": "Cuối cùng tôi cũng viết xong bài tập rồi."
            },
            {
                "num": 42,
                "sentence": "今天我收到了很多生日 (lǐwù)。",
                "pinyin": "lǐwù",
                "ans": "礼物",
                "vi": "Hôm nay tôi nhận được rất nhiều quà sinh nhật."
            },
            {
                "num": 43,
                "sentence": "周末我常去看望 (yéye) 和奶奶。",
                "pinyin": "yéye",
                "ans": "爷爷",
                "vi": "Cuối tuần tôi thường đến thăm ông và bà."
            },
            {
                "num": 44,
                "sentence": "大家 (yìbiān) 喝茶一边看电视。",
                "pinyin": "yìbiān",
                "ans": "一边",
                "vi": "Mọi người vừa uống trà vừa xem tivi."
            },
            {
                "num": 45,
                "sentence": "遇到不懂的问题 (yīnggāi) 问老师。",
                "pinyin": "yīnggāi",
                "ans": "应该",
                "vi": "Gặp câu hỏi không hiểu nên hỏi thầy cô."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "终于", "py": "zhōngyú", "pos": "phó từ", "vi": "cuối cùng (sau nhiều nỗ lực)", "eg": "经过努力，他终于成功了。"},
            {"num": 2, "zh": "爷爷", "py": "yéye", "pos": "danh từ", "vi": "ông nội", "eg": "爷爷今年七十岁了。"},
            {"num": 3, "zh": "礼物", "py": "lǐwù", "pos": "danh từ", "vi": "món quà, quà tặng", "eg": "这是送给你的生日礼物。"},
            {"num": 4, "zh": "奶奶", "py": "nǎinai", "pos": "danh từ", "vi": "bà nội", "eg": "奶奶包的饺子最好吃。"},
            {"num": 5, "zh": "遇到", "py": "yùdào", "pos": "động từ", "vi": "bắt gặp, chạm trán, gặp phải", "eg": "在路上遇到了多年不见的同学。"},
            {"num": 6, "zh": "一边……一边……", "py": "yìbiān... yìbiān...", "pos": "liên từ", "vi": "vừa... vừa... (hai hành động song song)", "eg": "他喜欢一边听歌一边看书。"},
            {"num": 7, "zh": "过去", "py": "guòqù", "pos": "danh từ chỉ thời gian", "vi": "quá khứ, trước kia", "eg": "过去的事情就让它过去吧。"},
            {"num": 8, "zh": "一般", "py": "yìbān", "pos": "tính từ/phó từ", "vi": "bình thường, thông thường", "eg": "我周末一般在家里休息。"},
            {"num": 9, "zh": "愿意", "py": "yuànyì", "pos": "động từ năng nguyện", "vi": "bằng lòng, sẵn lòng", "eg": "你愿意和我一起去吗？"},
            {"num": 10, "zh": "起来", "py": "qǐlái", "pos": "động từ/bổ ngữ", "vi": "đứng dậy, bắt đầu", "eg": "快站起来活动活动。"},
            {"num": 11, "zh": "应该", "py": "yīnggāi", "pos": "động từ năng nguyện", "vi": "nên, phải", "eg": "生病了应该去医院看医生。"},
            {"num": 12, "zh": "生活", "py": "shēnghuó", "pos": "danh từ/động từ", "vi": "cuộc sống, sinh hoạt", "eg": "他在北京生活了五年。"},
            {"num": 13, "zh": "校长", "py": "xiàozhǎng", "pos": "danh từ", "vi": "hiệu trưởng", "eg": "校长在全校大会上讲话。"},
            {"num": 14, "zh": "坏", "py": "huài", "pos": "tính từ", "vi": "hỏng, xấu, hư", "eg": "电脑坏了，需要修一下。"},
            {"num": 15, "zh": "经常", "py": "jīngcháng", "pos": "phó từ", "vi": "thường xuyên, hay", "eg": "我们经常去图书馆看书。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Bổ ngữ xu hướng kép (复合趋向补语): V + 上/下/进/出/回/过/起 + 来/去",
                "desc": "Kết hợp giữa một động từ chỉ phương hướng và '来' hoặc '去' để miêu tả phương hướng chuyển động phức hợp của hành vi.",
                "examples": [
                    {"zh": "我是走回来的。", "py": "Wǒ shì zǒu huílái de.", "vi": "Tôi là đi bộ về đây."},
                    {"zh": "老师从教室里走出来了。", "py": "Lǎoshī cóng jiàoshì li zǒu chūlái le.", "vi": "Thầy giáo từ trong lớp bước ra ngoài này."},
                    {"zh": "快把行李搬上去吧。", "py": "Kuài bǎ xínglǐ bān shàngqù ba.", "vi": "Mau chuyển hành lý lên trên kia đi."}
                ]
            },
            {
                "title": "2. Cấu trúc nhấn mạnh: “是……的”",
                "desc": "Dùng để nhấn mạnh thời gian, địa điểm, phương thức hoặc người thực hiện của một hành động đã diễn ra trong quá khứ.",
                "examples": [
                    {"zh": "我是走回来的。（nhấn mạnh phương thức）", "py": "Wǒ shì zǒu huílái de.", "vi": "Tôi là đi bộ về đấy."},
                    {"zh": "我们是去年认识的。（nhấn mạnh thời gian）", "py": "Wǒmen shì qùnián rènshi de.", "vi": "Chúng tôi quen nhau vào năm ngoái."}
                ]
            }
        ]
    },

    # ==================== BÀI 14 ====================
    {
        "id": 14,
        "title_zh": "你把水果拿过来。",
        "title_py": "Nǐ bǎ shuǐguǒ ná guòlái.",
        "title_vi": "Cậu hãy mang trái cây đến đây.",
        "dialogues": [
            {
                "title": "Đoạn 1: 在客厅打扫卫生 (Dọn dẹp vệ sinh phòng khách)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "妈妈", "role": "female", "zh": "今天家里要来客人，快把客厅打扫干净。", "py": "Jīntiān jiā li yào lái kèrén, kuài bǎ kètīng dǎsǎo gānjìng.", "vi": "Hôm nay nhà mình có khách đến, mau quét dọn phòng khách sạch sẽ đi con."},
                    {"speaker": "儿子", "role": "male", "zh": "地我已经扫好了，桌子也擦干净了。", "py": "Dì wǒ yǐjīng sǎohǎo le, zhuōzi yě cā gānjìng le.", "vi": "Sàn nhà con đã quét xong rồi, bàn cũng lau sạch bóng rồi mẹ."},
                    {"speaker": "妈妈", "role": "female", "zh": "那你去把冰箱里的水果拿过来，放在盘子里。", "py": "Nà nǐ qù bǎ bīngxiāng li de shuǐguǒ ná guòlái, fàng zài pánzi li.", "vi": "Thế con ra lấy hoa quả trong tủ lạnh mang lại đây, bày vào trong đĩa đi."},
                    {"speaker": "儿子", "role": "male", "zh": "好的，有苹果、香蕉和西瓜，我这就去拿！", "py": "Hǎo de, yǒu píngguǒ, xiāngjiāo hé xīguā, wǒ zhè jiù qù ná!", "vi": "Dạ vâng, có táo, chuối và dưa hấu, con đi lấy ngay đây ạ!"}
                ]
            },
            {
                "title": "Đoạn 2: 准备晚饭 (Chuẩn bị bữa tối)",
                "location": "在厨房",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "你洗完澡了吗？快来帮帮我。", "py": "Nǐ xǐwán zǎo le ma? Kuài lái bāngbang wǒ.", "vi": "Anh tắm xong chưa? Mau lại giúp em một tay nào."},
                    {"speaker": "小刚", "role": "male", "zh": "洗完了，有什么需要我做的？", "py": "Xǐwán le, yǒu shénme xūyào wǒ zuò de?", "vi": "Anh tắm xong rồi, có việc gì cần anh làm không?"},
                    {"speaker": "小丽", "role": "female", "zh": "你先把鱼洗干净，然后再把青菜切一切。", "py": "Nǐ xiān bǎ yú xǐ gānjìng, ránhòu zài bǎ qīngcài qiē yiqie.", "vi": "Anh trước tiên rửa sạch cá đi, sau đó thái rau giúp em nhé."},
                    {"speaker": "小刚", "role": "male", "zh": "没问题，今天晚上我们吃鱼和新鲜蔬菜！", "py": "Méi wèntí, jīntiān wǎnshang wǒmen chī yú hé xīnxiān shūcài!", "vi": "Không thành vấn đề, tối nay chúng mình ăn cá và rau tươi xanh!"}
                ]
            },
            {
                "title": "Đoạn 3: 看中秋月亮 (Ngắm trăng rằm Trung Thu)",
                "location": "在阳台",
                "lines": [
                    {"speaker": "叔叔", "role": "male", "zh": "今晚的月亮真圆啊，像一个大白盘子。", "py": "Jīnwǎn de yuèliang zhēn yuán a, xiàng yí ge dà bái pánzi.", "vi": "Trăng tối nay tròn thật đấy, trông như một chiếc đĩa trắng lớn."},
                    {"speaker": "阿姨", "role": "female", "zh": "外面刮风了，有点儿凉，把外套穿上吧。", "py": "Wàimiàn guāfēng le, yǒudiǎnr liáng, bǎ wàitào chuānshang ba.", "vi": "Bên ngoài có gió thổi rồi, hơi se lạnh, mặc thêm áo khoác vào đi anh."},
                    {"speaker": "侄子", "role": "male", "zh": "叔叔，您给我们讲一个月亮上的故事吧！", "py": "Shūshu, nín gěi wǒmen jiǎng yí ge yuèliang shang de gùshi ba!", "vi": "Chú ơi, chú kể cho chúng cháu nghe một câu chuyện về cung trăng đi ạ!"},
                    {"speaker": "叔叔", "role": "male", "zh": "好啊，大家一边吃月饼，一边听叔叔讲嫦娥奔月的故事。", "py": "Hǎo a, dàjiā yìbiān chī yuèbǐng, yìbiān tīng shūshu jiǎng Cháng'é bèn yuè de gùshi.", "vi": "Được chứ, mọi người vừa ăn bánh trung thu, vừa nghe chú kể chuyện Hằng Nga bay lên cung trăng nhé."}
                ]
            },
            {
                "title": "Đoạn 4: 在餐厅看菜单 (Xem thực đơn ở nhà hàng)",
                "location": "在餐厅",
                "lines": [
                    {"speaker": "服务员", "role": "male", "zh": "请把菜单递给那位女士看一看。", "py": "Qǐng bǎ càidān dì gěi nà wèi nǚshì kàn yí kàn.", "vi": "Xin hãy chuyển thực đơn cho quý cô kia xem một chút ạ."},
                    {"speaker": "小丽", "role": "female", "zh": "这家餐厅的菜真丰富，不过名字都挺简单的。", "py": "Zhè jiā cāntīng de cài zhēn fēngfù, búguò míngzi dōu tǐng jiǎndān de.", "vi": "Món ăn nhà hàng này phong phú thật, nhưng tên gọi đều khá giản dị."},
                    {"speaker": "小刚", "role": "male", "zh": "简单的菜最好吃，你点你最爱吃的吧。", "py": "Jiǎndān de cài zuì hǎochī, nǐ diǎn nǐ zuì ài chī de ba.", "vi": "Món giản dị là ăn ngon nhất, em cứ gọi những món em thích nhất đi."},
                    {"speaker": "小丽", "role": "female", "zh": "那我们来一份北京烤鸭，饭后再来一盘香蕉甜点。", "py": "Nà wǒmen lái yí fèn Běijīng kǎoyā, fàn hòu zài lái yì pán xiāngjiāo tiándiǎn.", "vi": "Thế cho chúng tôi một phần vịt quay Bắc Kinh, sau bữa ăn thêm một đĩa tráng miệng chuối nhé."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你把冰箱里的水果拿过来，放在桌子上。 男：好，我马上拿过来。",
                "question": "女的让男的把水果放在哪儿？",
                "options": ["A. 放在盘子里", "B. 放在桌子上", "C. 放在冰箱里"],
                "ans": "B",
                "explain": "Cô gái bảo: 放在桌子上."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "今天晚上的月亮特别圆，像一个大白盘子。",
                "question": "Phán đoán đúng hay sai: 今晚月亮不圆。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Trăng tối nay rất tròn (今晚的月亮真圆)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：外面刮大风了，你冷不冷？ 女：有点儿冷，我把外套穿上了。",
                "question": "女的觉得怎么样？",
                "options": ["A. 很热", "B. 有点儿冷", "C. 特别渴"],
                "ans": "B",
                "explain": "Cô gái nói: 有点儿冷."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：今天谁来做晚饭？ 男：我来做，我先把菜洗干净，然后再做鱼。",
                "question": "男的先做什么？",
                "options": ["A. 先吃水果", "B. 先把菜洗干净", "C. 先做鱼"],
                "ans": "B",
                "explain": "Người nam nói: 我先把菜洗干净."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "你把冰箱里的水果拿过来放在盘子里。", "py": "Nǐ bǎ bīngxiāng li de shuǐguǒ ná guòlái fàng zài pánzi li.", "vi": "Con đem hoa quả trong tủ lạnh lại đây bày vào đĩa."},
                {"id": "B", "text": "今晚的月亮又大又圆，像一个白盘子。", "py": "Jīnwǎn de yuèliang yòu dà yòu yuán, xiàng yí ge bái pánzi.", "vi": "Trăng tối nay vừa to vừa tròn, trông như một chiếc đĩa trắng."},
                {"id": "C", "text": "先做作业，然后再看电视。", "py": "Xiān zuò zuòyè, ránhòu zài kàn diànshì.", "vi": "Làm bài tập trước, rồi sau đó mới xem tivi."},
                {"id": "D", "text": "外面刮风了，天气凉，多穿件衣服。", "py": "Wàimiàn guāfēng le, tiānqì liáng, duō chuān jiàn yīfu.", "vi": "Bên ngoài nổi gió rồi, trời lạnh, mặc thêm áo vào."},
                {"id": "E", "text": "请把菜单拿给我看一下，谢谢。", "py": "Qǐng bǎ càidān ná gěi wǒ kàn yíxià, xièxie.", "vi": "Xin đưa thực đơn cho tôi xem một chút, cảm ơn."}
            ],
            "questions": [
                {"num": 21, "text": "客人要来了，水果准备好了吗？", "py": "Kèrén yào lái le, shuǐguǒ zhǔnbèihǎo le ma?", "vi": "Khách sắp đến rồi, hoa quả đã chuẩn bị xong chưa?", "ans": "A", "explain": "Bảo lấy hoa quả trong tủ lạnh bày ra đĩa."},
                {"num": 22, "text": "快抬头看天空，今天的景色多美！", "py": "Kuài táitóu kàn tiānkōng, jīntiān de jǐngsè duō měi!", "vi": "Mau ngẩng đầu nhìn lên trời xem, cảnh tượng hôm nay đẹp biết bao!", "ans": "B", "explain": "Khen trăng rằm tròn như cái đĩa."},
                {"num": 23, "text": "妈妈，我现在能玩游戏了吗？", "py": "Māma, wǒ xiànzài néng wán yóuxì le ma?", "vi": "Mẹ ơi, bây giờ con chơi game được chưa ạ?", "ans": "C", "explain": "Yêu cầu làm xong bài tập rồi mới được giải trí."},
                {"num": 24, "text": "出门散步感觉有点儿冷。", "py": "Chūmén sànbù gǎnjué yǒudiǎnr lěng.", "vi": "Ra ngoài đi dạo cảm thấy hơi lạnh.", "ans": "D", "explain": "Nhắc bên ngoài nổi gió nên mặc thêm áo."},
                {"num": 25, "text": "两位顾客，你们打算点什么菜？", "py": "Liǎng wèi gùkè, nǐmen dǎsuàn diǎn shénme cài?", "vi": "Hai vị khách, quý khách dự định gọi món gì ạ?", "ans": "E", "explain": "Yêu cầu đưa thực đơn để chọn món."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "打扫", "py": "dǎsǎo", "vi": "quét dọn, dọn dẹp"},
                {"id": "B", "zh": "干净", "py": "gānjìng", "vi": "sạch sẽ"},
                {"id": "C", "zh": "冰箱", "py": "bīngxiāng", "vi": "tủ lạnh"},
                {"id": "D", "zh": "菜单", "py": "càidān", "vi": "thực đơn"},
                {"id": "E", "zh": "香蕉", "py": "xiāngjiāo", "vi": "quả chuối"}
            ],
            "questions": [
                {"num": 26, "prefix": "周末我们一起把房间", "suffix": "了一下。", "py": "Zhōumò wǒmen yìqǐ bǎ fángjiān ( ? ) le yíxià.", "vi": "Cuối tuần chúng tôi cùng nhau ( ? ) phòng một chút.", "ans": "A", "word": "打扫", "explain": "Quét dọn phòng: 打扫房间 (dǎsǎo fángjiān)."},
                {"num": 27, "prefix": "洗完手，手变得非常", "suffix": "。", "py": "Xǐwán shǒu, shǒu biàn de fēicháng ( ? ).", "vi": "Rửa tay xong, bàn tay trở nên rất ( ? ).", "ans": "B", "word": "干净", "explain": "Sạch sẽ: 干净 (gānjìng)."},
                {"num": 28, "prefix": "把吃不完的饭菜放进", "suffix": "里保存。", "py": "Bǎ chī bu wán de fàncài fàng jìn ( ? ) li bǎocún.", "vi": "Để đồ ăn không ăn hết vào trong ( ? ) bảo quản.", "ans": "C", "word": "冰箱", "explain": "Tủ lạnh: 冰箱 (bīngxiāng)."},
                {"num": 29, "prefix": "服务员，请给我们拿一份", "suffix": "，我们要点菜。", "py": "Fúwùyuán, qǐng gěi wǒmen ná yí fèn ( ? ), wǒmen yào diǎncài.", "vi": "Phục vụ ơi, lấy cho chúng tôi một bản ( ? ), chúng tôi cần gọi món.", "ans": "D", "word": "菜单", "explain": "Thực đơn: 菜单 (càidān)."},
                {"num": 30, "prefix": "猴子最喜欢吃的水果是", "suffix": "。", "py": "Hóuzi zuì xǐhuan chī de shuǐguǒ shì ( ? ).", "vi": "Trái cây mà khỉ thích ăn nhất là ( ? ).", "ans": "E", "word": "香蕉", "explain": "Quả chuối: 香蕉 (xiāngjiāo)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "今天是八月十五中秋节，是中国人全家团圆的传统节日。晚饭后，小刚一家人在阳台上赏月。小丽把打扫得干干净净的桌子搬到阳台上，上面放着月饼、苹果和香蕉。今晚的月亮又大又圆，像一个白色的玉盘挂在天上。微风轻轻地吹着，叔叔一边吃月饼，一边给孩子们讲关于月亮的美丽故事。大家都听得非常认真，笑声不断。",
            "passage_py": "Jīntiān shì bā yuè shíwǔ Zhōngqiūjié, shì Zhōngguó rén quánjiā tuányuán de chuántǒng jiérì. Wǎnfàn hòu, Xiǎogāng yì jiā rén zài yángtái shang shǎngyuè. Xiǎolì bǎ dǎsǎo de gāngānjìngjìng de zhuōzi bān dào yángtái shang, shàngmiàn fàngzhe yuèbǐng, píngguǒ hé xiāngjiāo. Jīnwǎn de yuèliang yòu dà yòu yuán, xiàng yí ge báisè de yùpán guà zài tiān shang. Wēifēng qīngqīng de chuīzhe, shūshu yìbiān chī yuèbǐng, yìbiān gěi háizimen jiǎng guānyú yuèliang de měilì gùshi. Dàjiā dōu tīng de fēicháng rènzhēn, xiàoshēng búduàn.",
            "passage_vi": "Hôm nay là ngày 15 tháng 8 tết Trung Thu, là ngày lễ truyền thống đoàn viên cả gia đình của người Trung Quốc. Sau bữa cơm tối, gia đình Tiểu Cương ngồi ngắm trăng ngoài ban công. Tiểu Lệ khiêng chiếc bàn đã lau chùi sạch sẽ ra ban công, bên trên bày bánh trung thu, táo và chuối. Trăng đêm nay vừa to vừa tròn, tựa như một chiếc đĩa ngọc trắng treo lơ lửng trên nền trời. Gió hiu hiu thổi, chú vừa ăn bánh vừa kể cho lũ trẻ nghe câu chuyện tươi đẹp về cung trăng. Mọi người đều lắng nghe chăm chú, tiếng cười không ngớt.",
            "questions": [
                {
                    "num": 31,
                    "text": "今天是中国的什么节日？",
                    "options": ["A. 春节", "B. 中秋节", "C. 端午节"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 今天是八月十五中秋节."
                },
                {
                    "num": 32,
                    "text": "晚饭后小刚一家人在哪儿赏月？",
                    "options": ["A. 在客厅", "B. 在公园", "C. 在阳台上"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 小刚一家人在阳台上赏月."
                },
                {
                    "num": 33,
                    "text": "阳台上的桌子上放了什么东西？",
                    "options": ["A. 电脑和手机", "B. 月饼、苹果和香蕉", "C. 啤酒和烤肉"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 上面放着月饼、苹果和香蕉."
                },
                {
                    "num": 34,
                    "text": "今晚的月亮看起来像什么？",
                    "options": ["A. 一艘小船", "B. 一个白色的玉盘", "C. 一朵云"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 像一个白色的玉盘挂在天上."
                },
                {
                    "num": 35,
                    "text": "叔叔在做什么？",
                    "options": ["A. 给大家做饭", "B. 给孩子们讲月亮的故事", "C. 在玩手机游戏"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 给孩子们讲关于月亮的美丽故事."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["拿过来", "你把水果", "放在盘子里"],
                "ans": "你把水果拿过来放在盘子里。",
                "py": "Nǐ bǎ shuǐguǒ ná guòlái fàng zài pánzi li.",
                "vi": "Cậu đem hoa quả lại đây bày vào trong đĩa."
            },
            {
                "num": 37,
                "chunks": ["打扫干净了", "已经把房间", "我们"],
                "ans": "我们已经把房间打扫干净了。",
                "py": "Wǒmen yǐjīng bǎ fángjiān dǎsǎo gānjìng le.",
                "vi": "Chúng tôi đã quét dọn phòng sạch sẽ rồi."
            },
            {
                "num": 38,
                "chunks": ["像一个白玉盘", "今晚的月亮", "真圆啊"],
                "ans": "今晚的月亮真圆啊，像一个白玉盘。",
                "py": "Jīnwǎn de yuèliang zhēn yuán a, xiàng yí ge bái yùpán.",
                "vi": "Trăng đêm nay tròn thật đấy, tựa như chiếc đĩa ngọc trắng."
            },
            {
                "num": 39,
                "chunks": ["先洗干净鱼", "然后再做菜", "请你"],
                "ans": "请你先洗干净鱼，然后再做菜。",
                "py": "Qǐng nǐ xiān xǐ gānjìng yú, ránhòu zài zuò cài.",
                "vi": "Xin bạn trước tiên rửa sạch cá, sau đó mới nấu ăn."
            },
            {
                "num": 40,
                "chunks": ["把菜单递给", "看一看", "请服务员", "那位客人"],
                "ans": "请服务员把菜单递给那位客人看一看。",
                "py": "Qǐng fúwùyuán bǎ càidān dì gěi nà wèi kèrén kàn yí kàn.",
                "vi": "Xin người phục vụ chuyển thực đơn cho vị khách kia xem một chút."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "周末要好好 (dǎsǎo) 房间。",
                "pinyin": "dǎsǎo",
                "ans": "打扫",
                "vi": "Cuối tuần phải dọn dẹp phòng cho tốt."
            },
            {
                "num": 42,
                "sentence": "把手洗 (gānjìng) 再吃东西。",
                "pinyin": "gānjìng",
                "ans": "干净",
                "vi": "Rửa tay sạch sẽ rồi mới ăn đồ."
            },
            {
                "num": 43,
                "sentence": "水果放在 (bīngxiāng) 里保鲜。",
                "pinyin": "bīngxiāng",
                "ans": "冰箱",
                "vi": "Hoa quả để trong tủ lạnh bảo quản tươi."
            },
            {
                "num": 44,
                "sentence": "请看 (càidān) 点菜。",
                "pinyin": "càidān",
                "ans": "菜单",
                "vi": "Xin xem thực đơn gọi món."
            },
            {
                "num": 45,
                "sentence": "我买了一把 (xiāngjiāo)。",
                "pinyin": "xiāngjiāo",
                "ans": "香蕉",
                "vi": "Tôi đã mua một nải chuối."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "打扫", "py": "dǎsǎo", "pos": "động từ", "vi": "quét dọn, dọn dẹp", "eg": "请把教室打扫一下。"},
            {"num": 2, "zh": "干净", "py": "gānjìng", "pos": "tính từ", "vi": "sạch sẽ", "eg": "洗得干干净净。"},
            {"num": 3, "zh": "然后", "py": "ránhòu", "pos": "liên từ", "vi": "sau đó, tiếp theo", "eg": "先吃饭，然后再去看电影。"},
            {"num": 4, "zh": "冰箱", "py": "bīngxiāng", "pos": "danh từ", "vi": "tủ lạnh", "eg": "把饮料放进冰箱里。"},
            {"num": 5, "zh": "洗澡", "py": "xǐzǎo", "pos": "động từ", "vi": "tắm, tắm rửa", "eg": "天热了，每天都要洗澡。"},
            {"num": 6, "zh": "节目", "py": "jiémù", "pos": "danh từ", "vi": "tiết mục, chương trình", "eg": "今晚的电视节目很精彩。"},
            {"num": 7, "zh": "月亮", "py": "yuèliang", "pos": "danh từ", "vi": "mặt trăng", "eg": "中秋节的月亮特别圆。"},
            {"num": 8, "zh": "像", "py": "xiàng", "pos": "động từ/tính từ", "vi": "giống như, tựa như", "eg": "这只小猫长得像小老虎。"},
            {"num": 9, "zh": "盘子", "py": "pánzi", "pos": "danh từ", "vi": "cái đĩa", "eg": "桌子上放着几个水果盘子。"},
            {"num": 10, "zh": "刮风", "py": "guāfēng", "pos": "động từ", "vi": "nổi gió, gió thổi", "eg": "外面突然刮起了大风。"},
            {"num": 11, "zh": "叔叔", "py": "shūshu", "pos": "danh từ", "vi": "chú (em trai bố)", "eg": "叔叔送给我一辆自行车。"},
            {"num": 12, "zh": "阿姨", "py": "āyí", "pos": "danh từ", "vi": "dì, cô, bác gái", "eg": "邻居李阿姨非常热情。"},
            {"num": 13, "zh": "声音", "py": "shēngyīn", "pos": "danh từ", "vi": "âm thanh, tiếng, giọng", "eg": "他说话的声音真好听。"},
            {"num": 14, "zh": "故事", "py": "gùshi", "pos": "danh từ", "vi": "câu chuyện", "eg": "奶奶给我讲了一个有趣的故事。"},
            {"num": 15, "zh": "菜单", "py": "càidān", "pos": "danh từ", "vi": "thực đơn", "eg": "服务员，请给我们一份菜单。"},
            {"num": 16, "zh": "简单", "py": "jiǎndān", "pos": "tính từ", "vi": "đơn giản, dễ dàng", "eg": "这道题非常简单。"},
            {"num": 17, "zh": "香蕉", "py": "xiāngjiāo", "pos": "danh từ", "vi": "quả chuối", "eg": "香蕉又甜又软。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu chữ “把” kết hợp bổ ngữ xu hướng: S + 把 + O + V + 来 / 去",
                "desc": "Biểu thị hành động tác động làm cho sự vật di chuyển lại gần hoặc ra xa người nói.",
                "examples": [
                    {"zh": "你把水果拿过来。", "py": "Nǐ bǎ shuǐguǒ ná guòlái.", "vi": "Cậu hãy mang hoa quả qua đây."},
                    {"zh": "请把作业交上去。", "py": "Qǐng bǎ zuòyè jiāo shàngqù.", "vi": "Xin hãy nộp bài tập lên trên kia."},
                    {"zh": "快把雨伞带回去吧。", "py": "Kuài bǎ yǔsǎn dài huíqù ba.", "vi": "Mau mang ô về đi nhé."}
                ]
            },
            {
                "title": "2. Cấu trúc diễn tả trình tự: “先……再 / 然后……”",
                "desc": "Dùng để biểu thị thứ tự trước sau của các hành động (Trước tiên làm việc A, sau đó mới làm việc B).",
                "examples": [
                    {"zh": "你先洗干净鱼，然后再做菜。", "py": "Nǐ xiān xǐ gānjìng yú, ránhòu zài zuò cài.", "vi": "Anh trước tiên rửa sạch cá, sau đó mới nấu món ăn."},
                    {"zh": "我们先坐地铁，然后换公共汽车。", "py": "Wǒmen xiān zuò dìtiě, ránhòu huàn gōnggòng qìchē.", "vi": "Chúng ta trước tiên đi tàu điện ngầm, sau đó đổi sang xe buýt."}
                ]
            }
        ]
    },

    # ==================== BÀI 15 ====================
    {
        "id": 15,
        "title_zh": "其他都没什么问题。",
        "title_py": "Qítā dōu méi shénme wèntí.",
        "title_vi": "Những câu khác đều không có vấn đề gì.",
        "dialogues": [
            {
                "title": "Đoạn 1: 检查考试卷子 (Kiểm tra bài thi)",
                "location": "在办公室",
                "lines": [
                    {"speaker": "老师", "role": "female", "zh": "小明，你的这张试卷考得真不错，得了九十五分。", "py": "Xiǎomíng, nǐ de zhè zhāng shìjuàn kǎo de zhēn búcuò, dé le jiǔshíwǔ fēn.", "vi": "Tiểu Minh, bài thi này của em làm rất khá, được 95 điểm đấy."},
                    {"speaker": "学生", "role": "male", "zh": "老师，我错在哪道题了？", "py": "Lǎoshī, wǒ cuò zài nǎ dào tí le?", "vi": "Thưa cô, em sai ở câu nào thế ạ?"},
                    {"speaker": "老师", "role": "female", "zh": "第三题汉字写错了，其他都没什么问题。", "py": "Dì-sān tí hànzì xiěcuò le, qítā dōu méi shénme wèntí.", "vi": "Câu số 3 viết sai chữ Hán, còn những câu khác đều không có vấn đề gì."},
                    {"speaker": "学生", "role": "male", "zh": "太好了，下次我一定认真检查，争取考一百分！", "py": "Tài hǎo le, xià cì wǒ yídìng rènzhēn jiǎnchá, zhēngqǔ kǎo yì bǎi fēn!", "vi": "Tuyệt quá, lần sau em nhất định sẽ kiểm tra cẩn thận, phấn đấu đạt 100 điểm ạ!"}
                ]
            },
            {
                "title": "Đoạn 2: 准备出国留学 (Chuẩn bị đi du học)",
                "location": "在咖啡馆",
                "lines": [
                    {"speaker": "朋友", "role": "male", "zh": "你的留学申请材料准备得怎么样了？", "py": "Nǐ de liúxué shēnqǐng cáiliào zhǔnbèi de zěnmeyàng le?", "vi": "Hồ sơ xin đi du học của cậu chuẩn bị đến đâu rồi?"},
                    {"speaker": "小刚", "role": "male", "zh": "除了成绩单以外，其他材料都准备齐全了。", "py": "Chúle chéngjìdān yǐwài, qítā cáiliào dōu zhǔnbèi qíquán le.", "vi": "Ngoài bảng điểm ra, những giấy tờ khác đều đã chuẩn bị đầy đủ cả rồi."},
                    {"speaker": "朋友", "role": "male", "zh": "那你的汉语水平怎么样？能听懂课吗？", "py": "Nà nǐ de hànyǔ shuǐpíng zěnmeyàng? Néng tīngdǒng kè ma?", "vi": "Thế trình độ tiếng Hán của cậu thế nào? Có nghe hiểu bài giảng không?"},
                    {"speaker": "小刚", "role": "male", "zh": "通过了HSK四级，日常交流没有问题，但我还要继续提高。", "py": "Tōngguò le HSK sì jí, rìcháng jiāoliú méiyǒu wèntí, dàn wǒ hái yào jìxù tígāo.", "vi": "Tớ đã đỗ HSK 4 rồi, giao tiếp hằng ngày không thành vấn đề, nhưng tớ vẫn phải tiếp tục nâng cao."}
                ]
            },
            {
                "title": "Đoạn 3: 聊网络新闻 (Nói về tin tức trên mạng)",
                "location": "在自习室",
                "lines": [
                    {"speaker": "同学A", "role": "male", "zh": "你经常上网看新闻吗？", "py": "Nǐ jīngcháng shàngwǎng kàn xīnwén ma?", "vi": "Cậu có hay lên mạng đọc tin tức không?"},
                    {"speaker": "同学B", "role": "female", "zh": "经常看，网上有很多关于传统节日的报道，有趣极了！", "py": "Jīngcháng kàn, wǎng shang yǒu hěn duō guānyú chuántǒng jiérì de bàodào, yǒuqù jí le!", "vi": "Hay đọc lắm, trên mạng có rất nhiều bài phóng sự về các ngày lễ truyền thống, thú vị vô cùng!"},
                    {"speaker": "同学A", "role": "male", "zh": "现在网络真方便，世界各地发生的事情马上就能知道。", "py": "Xiànzài wǎngluò zhēn fāngbiàn, shìjiè gè dì fāshēng de shìqing mǎshàng jiù néng zhīdào.", "vi": "Hiện giờ mạng internet tiện thật, việc xảy ra ở khắp nơi trên thế giới đều biết được ngay."},
                    {"speaker": "同学B", "role": "female", "zh": "是啊，不过上网也要注意保护眼睛，不能看太久。", "py": "Shì a, búguò shàngwǎng yě yào zhùyì bǎohù yǎnjìng, bù néng kàn tài jiǔ.", "vi": "Đúng thế, nhưng lên mạng cũng cần chú ý bảo vệ mắt, không được nhìn màn hình quá lâu."}
                ]
            },
            {
                "title": "Đoạn 4: 谈礼貌与交流 (Nói về lễ phép và giao tiếp)",
                "location": "在家",
                "lines": [
                    {"speaker": "妈妈", "role": "female", "zh": "在学校跟老师说话要有礼貌，知道吗？", "py": "Zài xuéxiào gēn lǎoshī shuōhuà yào yǒu lǐmào, zhīdào ma?", "vi": "Ở trường nói chuyện với thầy cô phải có lễ phép, biết chưa con?"},
                    {"speaker": "儿子", "role": "male", "zh": "知道，我每次见到老师都鞠躬说‘老师好’。", "py": "Zhīdào, wǒ měi cì jiàndào lǎoshī dōu jūgōng shuō 'lǎoshī hǎo'.", "vi": "Dạ con biết, mỗi lần gặp thầy cô con đều cúi chào và nói 'Em chào thầy cô' ạ."},
                    {"speaker": "妈妈", "role": "female", "zh": "跟同学交流时也要注意说话的语气。", "py": "Gēn tóngxué jiāoliú shí yě yào zhùyì shuōhuà de yǔqì.", "vi": "Lúc giao lưu với bạn bè cũng phải chú ý ngữ khí lời nói nhé."},
                    {"speaker": "儿子", "role": "male", "zh": "放心吧妈妈，大家都说我是一个懂礼貌的好孩子！", "py": "Fàngxīn ba māma, dàjiā dōu shuō wǒ shì yí ge dǒng lǐmào de hǎo háizi!", "vi": "Mẹ yên tâm đi, mọi người đều khen con là một đứa bé ngoan biết lễ phép đấy ạ!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：小明的试卷考得怎么样？ 男：考了九十五分，除了错了一个字，其他都没问题。",
                "question": "小明的考试考得怎么样？",
                "options": ["A. 没及格", "B. 考得很好，得了95分", "C. 错了很多题"],
                "ans": "B",
                "explain": "Đoạn thoại nêu rõ: 考了九十五分，考得真不错."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚除了成绩单还没拿到，其他留学材料都已经准备好了。",
                "question": "Phán đoán đúng hay sai: 小刚的所有材料都没准备好。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Ngoài bảng điểm ra thì các tài liệu khác đều đã chuẩn bị xong (其他材料都准备齐全了)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：你觉得网上的节日报道怎么样？ 女：写得太好了，有趣极了！",
                "question": "女的对网上的报道有什么评价？",
                "options": ["A. 不好看", "B. 很难懂", "C. 有趣极了"],
                "ans": "C",
                "explain": "Người nữ nhận xét: 有趣极了 (thú vị vô cùng)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：跟长辈说话的时候，最重要的是什么？ 男：最重要的是懂礼貌，态度要好。",
                "question": "男的觉得说话最重要的是什么？",
                "options": ["A. 声音大", "B. 懂礼貌", "C. 语速快"],
                "ans": "B",
                "explain": "Người nam trả lời: 最重要的是懂礼貌."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "除了第三题写错了一个字，其他都没什么问题。", "py": "Chúle dì-sān tí xiěcuò le yí ge zì, qítā dōu méi shénme wèntí.", "vi": "Ngoài câu số 3 viết sai một chữ ra, những câu khác đều không vấn đề gì."},
                {"id": "B", "text": "为了去中国留学，他每天努力提高汉语水平。", "py": "Wèile qù Zhōngguó liúxué, tā měitiān nǔlì tígāo hànyǔ shuǐpíng.", "vi": "Để đi Trung Quốc du học, hằng ngày anh ấy nỗ lực nâng cao trình độ tiếng Hán."},
                {"id": "C", "text": "网上关于传统节日的介绍有趣极了。", "py": "Wǎng shang guānyú chuántǒng jiérì de jièshào yǒuqù jí le.", "vi": "Giới thiệu trên mạng về các ngày lễ truyền thống thú vị vô cùng."},
                {"id": "D", "text": "不管是跟老师还是跟同学说话，都要懂礼貌。", "py": "Bùguǎn shì gēn lǎoshī háishì gēn tóngxué shuōhuà, dōu yào dǒng lǐmào.", "vi": "Dù là nói chuyện với thầy cô hay bạn bè, đều phải biết lễ phép."},
                {"id": "E", "text": "除了周日以外，图书馆每天都开门。", "py": "Chúle zhōurì yǐwài, túshūguǎn měitiān dōu kāimén.", "vi": "Ngoại trừ chủ nhật ra, thư viện ngày nào cũng mở cửa."}
            ],
            "questions": [
                {"num": 21, "text": "你看我的这篇中文文章写得怎么样？", "py": "Nǐ kàn wǒ de zhè piān zhōngwén wénzhāng xiě de zěnmeyàng?", "vi": "Cậu xem bài văn tiếng Trung này tớ viết thế nào?", "ans": "A", "explain": "Nhận xét bài chỉ sai một chữ, còn lại rất tốt."},
                {"num": 22, "text": "小明最近为什么起早贪黑地学中文？", "py": "Xiǎomíng zuìjìn wèishénme qǐzǎo-tānhēi de xué zhōngwén?", "vi": "Tiểu Minh dạo này sao lại dậy sớm thức khuya học tiếng Trung thế?", "ans": "B", "explain": "Mục đích là để chuẩn bị đi du học Trung Quốc."},
                {"num": 23, "text": "你刚才在电脑上笑什么呢？", "py": "Nǐ gāngcái zài diànnǎo shang xiào shénme ne?", "vi": "Vừa nãy cậu cười gì trên máy tính thế?", "ans": "C", "explain": "Đọc tin tức về ngày lễ thấy thú vị vô cùng."},
                {"num": 24, "text": "妈妈为什么总夸小李是个好孩子？", "py": "Māma wèishénme zǒng kuā xiǎo Lǐ shì ge hǎo háizi?", "vi": "Mẹ sao lúc nào cũng khen Tiểu Lý là đứa trẻ ngoan?", "ans": "D", "explain": "Khen bạn ấy luôn biết lễ phép với mọi người."},
                {"num": 25, "text": "图书馆星期六也可以借书吗？", "py": "Túshūguǎn xīngqīliù yě kěyǐ jiè shū ma?", "vi": "Thư viện thứ Bảy cũng mượn được sách à?", "ans": "E", "explain": "Chỉ nghỉ chủ nhật, các ngày khác đều mở cửa."},
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "留学", "py": "liúxué", "vi": "du học"},
                {"id": "B", "zh": "水平", "py": "shuǐpíng", "vi": "trình độ"},
                {"id": "C", "zh": "其他", "py": "qítā", "vi": "khác, còn lại"},
                {"id": "D", "zh": "上网", "py": "shàngwǎng", "vi": "lên mạng, lướt web"},
                {"id": "E", "zh": "极了", "py": "jí le", "vi": "vô cùng, cực kỳ"}
            ],
            "questions": [
                {"num": 26, "prefix": "高中毕业后他打算去中国", "suffix": "。", "py": "Gāozhōng bìyè hòu tā dǎsuàn qù Zhōngguó ( ? ).", "vi": "Sau khi tốt nghiệp cấp 3 anh ấy dự định đi Trung Quốc ( ? ).", "ans": "A", "word": "留学", "explain": "Đi du học: 留学 (liúxué)."},
                {"num": 27, "prefix": "多听多说能快速提高汉语", "suffix": "。", "py": "Duō tīng duō shuō néng kuàisù tígāo hànyǔ ( ? ).", "vi": "Nghe nhiều nói nhiều có thể nâng cao nhanh ( ? ) tiếng Hán.", "ans": "B", "word": "水平", "explain": "Trình độ: 水平 (shuǐpíng)."},
                {"num": 28, "prefix": "除了小王，", "suffix": "人都按时到了。", "py": "Chúle xiǎo Wáng, ( ? ) rén dōu ànshí dào le.", "vi": "Ngoại trừ Tiểu Vương, những người ( ? ) đều đến đúng giờ.", "ans": "C", "word": "其他", "explain": "Những người khác: 其他人 (qítā rén)."},
                {"num": 29, "prefix": "现在的年轻人每天都喜欢", "suffix": "。", "py": "Xiànzài de niánqīngrén měitiān dōu xǐhuan ( ? ).", "vi": "Giới trẻ ngày nay mỗi ngày đều thích ( ? ).", "ans": "D", "word": "上网", "explain": "Lên mạng internet: 上网 (shàngwǎng)."},
                {"num": 30, "prefix": "妈妈今天做的红烧鱼好吃", "suffix": "！", "py": "Māma jīntiān zuò de hóngshāoyú hǎochī ( ? )!", "vi": "Món cá kho hôm nay mẹ nấu ngon ( ? )!", "ans": "E", "word": "极了", "explain": "Ngon vô cùng: 好吃极了 (hǎochī jí le)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "王朋是一位来自越南的留学生，现在在北京大学学习中文。来中国以前，王朋的汉语水平一般，只能说一些简单的句子。在中国生活了半年以后，在老师和同学们的帮助下，他的汉语水平提高得非常快。上个星期，王朋参加了全校留学生汉语演讲比赛，他的发音很准确，态度非常有礼貌。最后评委老师评价他的演讲：“除了一个小生词用得不够自然，其他都表现得非常棒！”王朋获得了比赛第一名，他高兴极了。",
            "passage_py": "Wáng Péng shì yí wèi láizì Yuènán de liúxuéshēng, xiànzài zài Běijīng Dàxué xuéxí zhōngwén. Lái Zhōngguó yǐqián, Wáng Péng de hànyǔ shuǐpíng yìbān, zhǐ néng shuō yìxiē jiǎndān de jùzi. Zài Zhōngguó shēnghuó le bàn nián yǐhòu, zài lǎoshī hé tóngxuémen de bāngzhù xià, tā de hànyǔ shuǐpíng tígāo de fēicháng kuài. Shàng ge xīngqī, Wáng Péng cānjiā le quán xiào liúxuéshēng hànyǔ yǎnjiǎng bǐsài, tā de fāyīn hěn zhǔnquè, tàidù fēicháng yǒu lǐmào. Zuìhòu píngwěi lǎoshī píngjià tā de yǎnjiǎng: 'Chúle yí ge xiǎo shēngcí yòng de bú gòu zìrán, qítā dōu biǎoxiàn de fēicháng bàng!' Wáng Péng huòdé le bǐsài dì-yī míng, tā gāoxìng jí le.",
            "passage_vi": "Vương Bằng là một du học sinh đến từ Việt Nam, hiện đang học tiếng Trung tại Đại học Bắc Kinh. Trước khi sang Trung Quốc, trình độ tiếng Hán của Vương Bằng chỉ ở mức bình thường, chỉ biết nói vài câu đơn giản. Sau khi sống ở Trung Quốc nửa năm, dưới sự giúp đỡ của thầy cô và bạn bè, trình độ tiếng Hán của cậu nâng cao cực kỳ nhanh. Tuần trước, Vương Bằng tham gia cuộc thi hùng biện tiếng Hán dành cho du học sinh toàn trường, phát âm của cậu rất chuẩn xác, thái độ vô cùng lễ phép. Cuối cùng các thầy cô giám khảo đánh giá bài diễn thuyết của cậu: 'Ngoài một từ mới dùng chưa thật tự nhiên ra, mọi mặt khác đều thể hiện vô cùng xuất sắc!' Vương Bằng đã giành giải nhất cuộc thi, cậu cảm thấy vui mừng vô cùng.",
            "questions": [
                {
                    "num": 31,
                    "text": "王朋来自哪个国家？",
                    "options": ["A. 美国", "B. 越南", "C. 韩国"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 王朋是一位来自越南的留学生."
                },
                {
                    "num": 32,
                    "text": "刚来中国时王朋的汉语水平怎么样？",
                    "options": ["A. 水平一般，只会说简单句子", "B. 水平非常高", "C. 一点儿也不会说"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 汉语水平一般，只能说一些简单的句子."
                },
                {
                    "num": 33,
                    "text": "王朋上个星期参加了什么比赛？",
                    "options": ["A. 足球比赛", "B. 汉语演讲比赛", "C. 唱歌比赛"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 参加了全校留学生汉语演讲比赛."
                },
                {
                    "num": 34,
                    "text": "评委老师对王朋有什么评价？",
                    "options": ["A. 表现非常糟糕", "B. 发音不准确", "C. 除了一个小生词，其他都非常棒"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 除了一个小生词用得不够自然，其他都表现得非常棒."
                },
                {
                    "num": 35,
                    "text": "王朋在比赛中取得了什么成绩？",
                    "options": ["A. 第一名", "B. 第二名", "C. 没有得奖"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 王朋获得了比赛第一名."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["都没什么问题", "其他", "这张试卷"],
                "ans": "这张试卷其他都没什么问题。",
                "py": "Zhè zhāng shìjuàn qítā dōu méi shénme wèntí.",
                "vi": "Bài thi này những câu khác đều không có vấn đề gì."
            },
            {
                "num": 37,
                "chunks": ["汉语水平", "提高得", "他的", "非常快"],
                "ans": "他的汉语水平提高得非常快。",
                "py": "Tā de hànyǔ shuǐpíng tígāo de fēicháng kuài.",
                "vi": "Trình độ tiếng Hán của cậu ấy nâng cao rất nhanh."
            },
            {
                "num": 38,
                "chunks": ["大家都很喜欢", "传统节日的报道", "网上关于"],
                "ans": "大家都很喜欢网上关于传统节日的报道。",
                "py": "Dàjiā dōu hěn xǐhuan wǎng shang guānyú chuántǒng jiérì de bàodào.",
                "vi": "Mọi người đều rất thích bài phóng sự về ngày lễ truyền thống trên mạng."
            },
            {
                "num": 39,
                "chunks": ["他是一个", "有礼貌的孩子", "懂礼貌"],
                "ans": "他是一个懂礼貌有礼貌的孩子。",
                "py": "Tā shì yí ge dǒng lǐmào yǒu lǐmào de háizi.",
                "vi": "Cậu ấy là một đứa trẻ hiểu chuyện và lễ phép."
            },
            {
                "num": 40,
                "chunks": ["全家人", "高兴极了", "听到这个好消息"],
                "ans": "听到这个好消息全家人高兴极了。",
                "py": "Tīngdào zhè ge hǎo xiāoxi quán jiā rén gāoxìng jí le.",
                "vi": "Nghe được tin tốt này cả nhà đều vui mừng khôn xiết."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "哥哥打算去法国 (liúxué)。",
                "pinyin": "liúxué",
                "ans": "留学",
                "vi": "Anh trai dự định đi Pháp du học."
            },
            {
                "num": 42,
                "sentence": "他的中文 (shuǐpíng) 提高得很快。",
                "pinyin": "shuǐpíng",
                "ans": "水平",
                "vi": "Trình độ tiếng Trung của anh ấy nâng cao rất nhanh."
            },
            {
                "num": 43,
                "sentence": "这个 (jùzi) 的意思你明白吗？",
                "pinyin": "jùzi",
                "ans": "句子",
                "vi": "Ý nghĩa của câu này bạn có hiểu không?"
            },
            {
                "num": 44,
                "sentence": "下课后小明经常 (shàngwǎng) 查资料。",
                "pinyin": "shàngwǎng",
                "ans": "上网",
                "vi": "Tan học Tiểu Minh thường lên mạng tra tài liệu."
            },
            {
                "num": 45,
                "sentence": "对人说话要懂 (lǐmào)。",
                "pinyin": "lǐmào",
                "ans": "礼貌",
                "vi": "Nói chuyện với mọi người phải biết lễ phép."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "节日", "py": "jiérì", "pos": "danh từ", "vi": "ngày lễ, ngày tết", "eg": "春节是中国最重要的传统节日。"},
            {"num": 2, "zh": "留学", "py": "liúxué", "pos": "động từ", "vi": "du học", "eg": "他打算明年去中国留学。"},
            {"num": 3, "zh": "水平", "py": "shuǐpíng", "pos": "danh từ", "vi": "trình độ, đẳng cấp", "eg": "他的汉语水平非常高。"},
            {"num": 4, "zh": "提高", "py": "tígāo", "pos": "động từ", "vi": "nâng cao, cải thiện", "eg": "多练习能提高听力水平。"},
            {"num": 5, "zh": "完成", "py": "wánchéng", "pos": "động từ", "vi": "hoàn thành", "eg": "今天的任务已经全部完成。"},
            {"num": 6, "zh": "句子", "py": "jùzi", "pos": "danh từ", "vi": "câu văn", "eg": "请用这个词造一个句子。"},
            {"num": 7, "zh": "其他", "py": "qítā", "pos": "đại từ", "vi": "khác, còn lại", "eg": "其他同学都去操场了。"},
            {"num": 8, "zh": "发", "py": "fā", "pos": "động từ", "vi": "gửi, phát ra", "eg": "我给你发了一份电子邮件。"},
            {"num": 9, "zh": "要求", "py": "yāoqiú", "pos": "động từ/danh từ", "vi": "yêu cầu, đòi hỏi", "eg": "老师对我们的要求很严格。"},
            {"num": 10, "zh": "注意", "py": "zhùyì", "pos": "động từ", "vi": "chú ý, để ý", "eg": "过马路要格外注意安全。"},
            {"num": 11, "zh": "上网", "py": "shàngwǎng", "pos": "động từ", "vi": "lên mạng internet", "eg": "周末我喜欢上网看电影。"},
            {"num": 12, "zh": "除了", "py": "chúle", "pos": "giới từ", "vi": "ngoại trừ, ngoài ra", "eg": "除了星期天，他每天都工作。"},
            {"num": 13, "zh": "新闻", "py": "xīnwén", "pos": "danh từ", "vi": "tin tức, thời sự", "eg": "爷爷每天早晨看电视新闻。"},
            {"num": 14, "zh": "花", "py": "huā", "pos": "động từ", "vi": "tiêu tốn (thời gian, tiền bạc)", "eg": "买这辆车花了不少钱。"},
            {"num": 15, "zh": "极了", "py": "jí le", "pos": "bổ ngữ", "vi": "cực kỳ, vô cùng", "eg": "今天天气好极了。"},
            {"num": 16, "zh": "礼貌", "py": "lǐmào", "pos": "danh từ/tính từ", "vi": "lễ phép, lịch sự", "eg": "有礼貌的人大家都会喜欢。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Cấu trúc “除了……以外，都 / 还……”",
                "desc": "Biểu thị sự ngoại trừ hoặc bổ sung. '除了……以外，都……' biểu thị ngoại trừ phần được nhắc đến, tất cả những cái khác đều như nhau. '除了……以外，还……' biểu thị ngoài cái đó ra, còn có thêm cái khác nữa.",
                "examples": [
                    {"zh": "除了第三题写错了，其他都没问题。", "py": "Chúle dì-sān tí xiěcuò le, qítā dōu méi wèntí.", "vi": "Ngoài câu số 3 viết sai ra, những câu khác đều không có vấn đề gì."},
                    {"zh": "除了英语以外，他还会说汉语和法语。", "py": "Chúle Yīngyǔ yǐwài, tā hái huì shuō Hànyǔ hé Fǎyǔ.", "vi": "Ngoài tiếng Anh ra, anh ấy còn biết nói tiếng Hán và tiếng Pháp."}
                ]
            },
            {
                "title": "2. Bổ ngữ mức độ “极了”",
                "desc": "Đặt sau tính từ hoặc động từ tâm lý để biểu thị mức độ cao nhất (cực kỳ, vô cùng).",
                "examples": [
                    {"zh": "今天的天气好极了！", "py": "Jīntiān de tiānqì hǎo jí le!", "vi": "Thời tiết hôm nay đẹp tuyệt vời!"},
                    {"zh": "小丽高兴极了。", "py": "Xiǎolì gāoxìng jí le.", "vi": "Tiểu Lệ mừng rỡ vô cùng."}
                ]
            }
        ]
    }
]
