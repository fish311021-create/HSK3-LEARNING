# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn cho Bài 6 đến Bài 10 - HSK 3 Standard Course
"""

LESSONS_6_TO_10 = [
    # ==================== BÀI 6 ====================
    {
        "id": 6,
        "title_zh": "怎么突然找不到了？",
        "title_py": "Zěnme tūrán zhǎo bu dào le?",
        "title_vi": "Sao bỗng dưng lại không tìm thấy?",
        "dialogues": [
            {
                "title": "Đoạn 1: 在客厅找眼镜 (Tìm kính trong phòng khách)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "周明", "role": "male", "zh": "我的眼镜呢？怎么突然找不到了？你看见了吗？", "py": "Wǒ de yǎnjìng ne? Zěnme tūrán zhǎo bu dào le? Nǐ kànjiàn le ma?", "vi": "Kính mắt của anh đâu rồi? Sao tự dưng lại không tìm thấy? Em có thấy không?"},
                    {"speaker": "周太太", "role": "female", "zh": "我看不到，你自己刚才放哪儿了？", "py": "Wǒ kànbudào, nǐ zìjǐ gāngcái fàng nǎr le?", "vi": "Em không thấy, lúc nãy anh tự đặt ở đâu?"},
                    {"speaker": "周明", "role": "male", "zh": "我就放在桌子上，离开了一会儿就找不到了。", "py": "Wǒ jiù fàng zài zhuōzi shang, líkāi le yíhuìr jiù zhǎo bu dào le.", "vi": "Anh vừa để ngay trên bàn, rời đi một lát mà đã không thấy đâu nữa rồi."},
                    {"speaker": "周太太", "role": "female", "zh": "你戴着眼镜找眼镜呢！在你的头上！", "py": "Nǐ dàizhe yǎnjìng zhǎo yǎnjìng ne! Zài nǐ de tóu shang!", "vi": "Anh đang đội kính mà đi tìm kính kìa! Ở ngay trên đầu anh đấy!"}
                ]
            },
            {
                "title": "Đoạn 2: 在打电话 (Nói chuyện điện thoại)",
                "location": "在书房",
                "lines": [
                    {"speaker": "同学A", "role": "male", "zh": "喂，刚才老师讲的第三题你听懂了吗？", "py": "Wèi, gāngcái lǎoshī jiǎng de dì-sān tí nǐ tīngdǒng le ma?", "vi": "Alo, câu thứ 3 thầy vừa giảng lúc nãy cậu có nghe hiểu không?"},
                    {"speaker": "同学B", "role": "female", "zh": "听懂了，老师讲得很清楚。", "py": "Tīngdǒng le, lǎoshī jiǎng de hěn qīngchu.", "vi": "Tớ nghe hiểu rồi, thầy giảng rất rõ ràng."},
                    {"speaker": "同学A", "role": "male", "zh": "那你能帮我讲讲吗？我没太听明白。", "py": "Nà nǐ néng bāng wǒ jiǎngjiang ma? Wǒ méi tài tīng míngbai.", "vi": "Thế cậu giảng giúp tớ một chút được không? Tớ nghe chưa hiểu lắm."},
                    {"speaker": "同学B", "role": "female", "zh": "没问题，我把作业做完了就去你家找你。", "py": "Méi wèntí, wǒ bǎ zuòyè zuòwán le jiù qù nǐ jiā zhǎo nǐ.", "vi": "Không vấn đề gì, tớ làm xong bài tập sẽ sang nhà tìm cậu."}
                ]
            },
            {
                "title": "Đoạn 3: 聊锻炼身体 (Nói về tập luyện thân thể)",
                "location": "在公园",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "你每天都来公园锻炼吗？", "py": "Nǐ měitiān dōu lái gōngyuán duànliàn ma?", "vi": "Ngày nào cậu cũng đến công viên tập thể dục à?"},
                    {"speaker": "小丽", "role": "female", "zh": "只要不下雨，我都来跑跑步，散散步。", "py": "Zhǐyào bú xiàyǔ, wǒ dōu lái pǎopǎobù, sànsànbù.", "vi": "Chỉ cần trời không mưa, mình đều đến chạy bộ, đi dạo một chút."},
                    {"speaker": "小刚", "role": "male", "zh": "难怪你身体这么好，晚上睡得着吗？", "py": "Nánguài nǐ shēntǐ zhème hǎo, wǎnshang shuì de zháo ma?", "vi": "Thảo nào sức khỏe cậu tốt thế, buổi tối có ngủ ngon không?"},
                    {"speaker": "小丽", "role": "female", "zh": "锻炼以后睡得特别好，一闭眼就睡着了。", "py": "Duànliàn yǐhòu shuì de tèbié hǎo, yí bì yǎn jiù shuìzháo le.", "vi": "Tập thể dục xong ngủ rất ngon, vừa nhắm mắt là ngủ say liền."}
                ]
            },
            {
                "title": "Đoạn 4: 在咖啡馆 (Ở quán cà phê)",
                "location": "在咖啡馆",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "这家咖啡馆的音乐真好听，特别安静。", "py": "Zhè jiā kāfēiguǎn de yīnyuè zhēn hǎotīng, tèbié ānjìng.", "vi": "Âm nhạc ở quán cà phê này hay thật, lại đặc biệt yên tĩnh."},
                    {"speaker": "同事B", "role": "female", "zh": "是啊，下班后在这里坐着聊天儿，感觉真轻松。", "py": "Shì a, xiàbān hòu zài zhèlǐ zuòzhe liáotiānr, gǎnjué zhēn qīngsōng.", "vi": "Đúng vậy, tan làm ngồi ở đây trò chuyện thấy thật thư thái."},
                    {"speaker": "同事A", "role": "male", "zh": "喝点儿咖啡，听听音乐，工作上的烦恼都忘了。", "py": "Hē diǎnr kāfēi, tīngting yīnyuè, gōngzuò shang de fánnǎo dōu wàng le.", "vi": "Uống chút cà phê, nghe chút nhạc, muộn phiền công việc đều tan biến hết."},
                    {"speaker": "同事B", "role": "female", "zh": "明天还要更努力工作呢！", "py": "Míngtiān hái yào gèng nǔlì gōngzuò ne!", "vi": "Ngày mai chúng mình còn phải nỗ lực làm việc hơn nữa đấy!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：我的眼镜怎么找不到了？ 女：你看看你的头上，眼镜不是在那儿吗？",
                "question": "男的的眼镜在哪儿？",
                "options": ["A. 在桌子上", "B. 在他的头上", "C. 在衣服口袋里"],
                "ans": "B",
                "explain": "Người nữ nhắc: 眼镜就在你的头上 (ở ngay trên đầu anh)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "刚才老师讲的数学题太难了，小明听懂了，但是小红没听懂。",
                "question": "Phán đoán đúng hay sai: 小红听懂了老师讲的题。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Đoạn văn nói Tiểu Hồng chưa nghe hiểu (没听懂)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：你每天都去公园跑步吗？ 男：只要不下雨，我每天都去锻炼。",
                "question": "男的什么时候去公园跑步？",
                "options": ["A. 下雨的时候", "B. 不下雨的时候", "C. 只有周末"],
                "ans": "B",
                "explain": "Người nam nói: 只要不下雨，我每天都去锻炼."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "男：你最近晚上睡得着觉吗？ 女：锻炼身体以后，我睡得特别香。",
                "question": "女的为什么睡得好？",
                "options": ["A. 因为喝了牛奶", "B. 因为锻炼了身体", "C. 因为听了音乐"],
                "ans": "B",
                "explain": "Người nữ nói: 锻炼身体以后，我睡得特别香."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "你的眼镜在你的头上戴着呢。", "py": "Nǐ de yǎnjìng zài nǐ de tóu shang dàizhe ne.", "vi": "Kính của bạn đang đeo trên đầu kìa."},
                {"id": "B", "text": "老师讲得很清楚，我都听懂了。", "py": "Lǎoshī jiǎng de hěn qīngchu, wǒ dōu tīngdǒng le.", "vi": "Thầy giảng rất rõ ràng, tôi đều nghe hiểu hết rồi."},
                {"id": "C", "text": "他在公园里跑步锻炼身体呢。", "py": "Tā zài gōngyuán li pǎobù duànliàn shēntǐ ne.", "vi": "Anh ấy đang chạy bộ tập thể dục trong công viên kìa."},
                {"id": "D", "text": "这家店的音乐真好听，特别安静。", "py": "Zhè jiā diàn de yīnyuè zhēn hǎotīng, tèbié ānjìng.", "vi": "Âm nhạc ở quán này thật hay, lại đặc biệt yên tĩnh."},
                {"id": "E", "text": "我刚才放在桌子上的笔不见了。", "py": "Wǒ gāngcái fàng zài zhuōzi shang de bǐ bú jiàn le.", "vi": "Cây bút tôi vừa để trên bàn lúc nãy không thấy đâu nữa."}
            ],
            "questions": [
                {"num": 21, "text": "我的眼镜呢？怎么突然找不到了？", "py": "Wǒ de yǎnjìng ne? Zěnme tūrán zhǎo bu dào le?", "vi": "Kính mắt của tôi đâu rồi? Sao bỗng dưng không tìm thấy?", "ans": "A", "explain": "Chỉ ra kính đang đeo trên đầu."},
                {"num": 22, "text": "刚才那道数学题你听明白了没有？", "py": "Gāngcái nà dào shùxué tí nǐ tīng míngbai le méiyǒu?", "vi": "Câu toán lúc nãy bạn đã hiểu rõ chưa?", "ans": "B", "explain": "Trả lời đã nghe hiểu hết vì thầy giảng rõ ràng."},
                {"num": 23, "text": "你知道小刚去哪儿了吗？", "py": "Nǐ zhīdào Xiǎogāng qù nǎr le ma?", "vi": "Bạn có biết Tiểu Cương đi đâu rồi không?", "ans": "C", "explain": "Cho biết bạn ấy đang chạy bộ ở công viên."},
                {"num": 24, "text": "你觉得这家咖啡厅环境怎么样？", "py": "Nǐ juéde zhè jiā kāfēitīng huánjìng zěnmeyàng?", "vi": "Bạn thấy không gian quán cà phê này thế nào?", "ans": "D", "explain": "Khen nhạc hay và yên tĩnh."},
                {"num": 25, "text": "你怎么一直在找东西？", "py": "Nǐ zěnme yìzhí zài zhǎo dōngxi?", "vi": "Sao cậu cứ tìm đồ suốt thế?", "ans": "E", "explain": "Giải thích cây bút để trên bàn vừa biến mất."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "眼镜", "py": "yǎnjìng", "vi": "kính mắt"},
                {"id": "B", "zh": "突然", "py": "tūrán", "vi": "đột nhiên, bất ngờ"},
                {"id": "C", "zh": "清楚", "py": "qīngchu", "vi": "rõ ràng"},
                {"id": "D", "zh": "帮忙", "py": "bāngmáng", "vi": "giúp đỡ"},
                {"id": "E", "zh": "锻炼", "py": "duànliàn", "vi": "rèn luyện, tập thể dục"}
            ],
            "questions": [
                {"num": 26, "prefix": "奶奶年纪大了，不戴", "suffix": "看不清书上的字。", "py": "Nǎinai niánjì dà le, bú dài ( ? ) kàn bu qīng shū shang de zì.", "vi": "Bà tuổi đã cao, không đeo ( ? ) thì không nhìn rõ chữ trong sách.", "ans": "A", "word": "眼镜", "explain": "Đeo kính mắt (戴眼镜)."},
                {"num": 27, "prefix": "天空中", "suffix": "下起了大雨。", "py": "Tiānkōng zhōng ( ? ) xià qǐ le dàyǔ.", "vi": "Trên bầu trời ( ? ) đổ cơn mưa to.", "ans": "B", "word": "突然", "explain": "Đột nhiên mưa to (突然)."},
                {"num": 28, "prefix": "老师的话大家都听得很", "suffix": "。", "py": "Lǎoshī de huà dàjiā dōu tīng de hěn ( ? ).", "vi": "Lời thầy giáo mọi người đều nghe rất ( ? ).", "ans": "C", "word": "清楚", "explain": "Nghe rất rõ ràng (听得很清楚)."},
                {"num": 29, "prefix": "你一个人搬不动，让我来", "suffix": "吧。", "py": "Nǐ yí ge rén bānbudòng, ràng wǒ lái ( ? ) ba.", "vi": "Cậu một mình khiêng không nổi đâu, để tớ lại ( ? ) nhé.", "ans": "D", "word": "帮忙", "explain": "Đến giúp đỡ (帮忙)."},
                {"num": 30, "prefix": "每天早上跑步可以", "suffix": "身体。", "py": "Měitiān zǎoshang pǎobù kěyǐ ( ? ) shēntǐ.", "vi": "Mỗi sáng chạy bộ có thể ( ? ) thân thể.", "ans": "E", "word": "锻炼", "explain": "Rèn luyện thân thể (锻炼身体)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "周明经常丢三落四。今天早上，他准备去上班，突然发现自己的眼镜找不到了。他把书房、客厅和卧室都找了一遍，怎么也找不着。周太太走过来问他在找什么，周明着急地说：“我的眼镜不见了，今天没有眼镜我怎么开车啊？”周太太笑着指了指他的头说：“你头上戴着的是什么？”周明一摸头，不好意思地笑了。",
            "passage_py": "Zhōu Míng jīngcháng diūsān-làsì. Jīntiān zǎoshang, tā zhǔnbèi qù shàngbān, tūrán fāxiàn zìjǐ de yǎnjìng zhǎo bu dào le. Tā bǎ shūfáng, kètīng hé wòshì dōu zhǎo le yí biàn, zěnme yě zhǎobuzháo. Zhōu tàitai zǒu guòlái wèn tā zài zhǎo shénme, Zhōu Míng zháojí de shuō: 'Wǒ de yǎnjìng bú jiàn le, jīntiān méiyǒu yǎnjìng wǒ zěnme kāichē a?' Zhōu tàitai xiàozhe zhǐ le zhǐ tā de tóu shuō: 'Nǐ tóu shang dàizhe de shì shénme?' Zhōu Míng yì mō tóu, bù hǎoyìsi de xiào le.",
            "passage_vi": "Chu Minh thường hay đãng trí hay quên. Sáng hôm nay, ông chuẩn bị đi làm thì đột nhiên phát hiện kính mắt của mình tìm không thấy đâu. Ông tìm khắp một lượt phòng đọc sách, phòng khách và phòng ngủ, tìm thế nào cũng không ra. Bà Chu đi tới hỏi ông đang tìm gì, Chu Minh sốt ruột nói: 'Kính của anh biến mất rồi, hôm nay không có kính thì anh lái xe làm sao được?' Bà Chu mỉm cười chỉ chỉ lên đầu ông bảo: 'Thế cái đang đeo trên đầu anh là cái gì kia?' Chu Minh đưa tay sờ lên đầu, ngượng ngùng bật cười.",
            "questions": [
                {
                    "num": 31,
                    "text": "周明今天早上打算去做什么？",
                    "options": ["A. 去爬山", "B. 去上班", "C. 去医院"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 他准备去上班."
                },
                {
                    "num": 32,
                    "text": "周明在找什么东西？",
                    "options": ["A. 钥匙", "B. 手机", "C. 眼镜"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 发现自己的眼镜找不到了."
                },
                {
                    "num": 33,
                    "text": "周明为什么着急找眼镜？",
                    "options": ["A. 没有眼镜不能看书", "B. 没有眼镜不能开车", "C. 没有眼镜不能走路"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 今天没有眼镜我怎么开车啊."
                },
                {
                    "num": 34,
                    "text": "周明的眼镜到底在哪儿？",
                    "options": ["A. 在书桌上", "B. 在他的头上", "C. 在车里"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 你头上戴着的是什么."
                },
                {
                    "num": 35,
                    "text": "最后周明觉得怎么样？",
                    "options": ["A. 很生气", "B. 不好意思", "C. 很害怕"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 周明一摸头，不好意思地笑了."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["找不到了", "怎么", "眼镜", "突然"],
                "ans": "眼镜怎么突然找不到了？",
                "py": "Yǎnjìng zěnme tūrán zhǎo bu dào le?",
                "vi": "Mắt kính sao bỗng dưng lại không tìm thấy?"
            },
            {
                "num": 37,
                "chunks": ["很清楚", "老师讲得", "大家都听懂了"],
                "ans": "老师讲得很清楚，大家都听懂了。",
                "py": "Lǎoshī jiǎng de hěn qīngchu, dàjiā dōu tīngdǒng le.",
                "vi": "Thầy giáo giảng rất rõ ràng, mọi người đều nghe hiểu hết."
            },
            {
                "num": 38,
                "chunks": ["在公园里", "锻炼身体", "每天跑步", "他"],
                "ans": "他每天在公园里跑步锻炼身体。",
                "py": "Tā měitiān zài gōngyuán li pǎobù duànliàn shēntǐ.",
                "vi": "Hằng ngày anh ấy chạy bộ trong công viên để rèn luyện sức khỏe."
            },
            {
                "num": 39,
                "chunks": ["特别好听", "这家店的", "音乐"],
                "ans": "这家店的音乐特别好听。",
                "py": "Zhè jiā diàn de yīnyuè tèbié hǎotīng.",
                "vi": "Âm nhạc của quán này nghe đặc biệt hay."
            },
            {
                "num": 40,
                "chunks": ["刚才", "放在桌子上", "我把书"],
                "ans": "我刚才把书放在桌子上。",
                "py": "Wǒ gāngcái bǎ shū fàng zài zhuōzi shang.",
                "vi": "Lúc nãy tôi đã để cuốn sách ở trên bàn."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我看不清，请帮我拿 (yǎnjìng)。",
                "pinyin": "yǎnjìng",
                "ans": "眼镜",
                "vi": "Tôi nhìn không rõ, xin lấy giúp tôi kính mắt."
            },
            {
                "num": 42,
                "sentence": "外面 (tūrán) 刮起了大风。",
                "pinyin": "tūrán",
                "ans": "突然",
                "vi": "Bên ngoài đột nhiên nổi gió lớn."
            },
            {
                "num": 43,
                "sentence": "老师讲得很 (qīngchu)。",
                "pinyin": "qīngchu",
                "ans": "清楚",
                "vi": "Thầy giáo giảng rất rõ ràng."
            },
            {
                "num": 44,
                "sentence": "明天早上我们去 (gōngyuán) 散步吧。",
                "pinyin": "gōngyuán",
                "ans": "公园",
                "vi": "Sáng mai chúng mình đi công viên dạo bộ nhé."
            },
            {
                "num": 45,
                "sentence": "每天运动可以 (duànliàn) 身体。",
                "pinyin": "duànliàn",
                "ans": "锻炼",
                "vi": "Vận động mỗi ngày có thể rèn luyện thân thể."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "眼镜", "py": "yǎnjìng", "pos": "danh từ", "vi": "kính mắt", "eg": "他戴着一副黑眼镜。"},
            {"num": 2, "zh": "突然", "py": "tūrán", "pos": "tính từ/phó từ", "vi": "đột nhiên, bất ngờ", "eg": "刚才突然停电了。"},
            {"num": 3, "zh": "离开", "py": "líkāi", "pos": "động từ", "vi": "rời khỏi, rời xa", "eg": "他依依不舍地离开了家乡。"},
            {"num": 4, "zh": "清楚", "py": "qīngchu", "pos": "tính từ", "vi": "rõ ràng, rành mạch", "eg": "这道题你听清楚了吗？"},
            {"num": 5, "zh": "刚才", "py": "gāngcái", "pos": "danh từ chỉ thời gian", "vi": "vừa nãy, lúc nãy", "eg": "刚才谁打来的电话？"},
            {"num": 6, "zh": "帮忙", "py": "bāngmáng", "pos": "động từ", "vi": "giúp đỡ", "eg": "你能过来帮个忙吗？"},
            {"num": 7, "zh": "特别", "py": "tèbié", "pos": "phó từ/tính từ", "vi": "đặc biệt, vô cùng", "eg": "今天天气特别晴朗。"},
            {"num": 8, "zh": "讲", "py": "jiǎng", "pos": "động từ", "vi": "nói, giảng giải", "eg": "请老师再讲一遍。"},
            {"num": 9, "zh": "明白", "py": "míngbai", "pos": "động từ/tính từ", "vi": "hiểu rõ, thấu suốt", "eg": "我现在完全明白了。"},
            {"num": 10, "zh": "锻炼", "py": "duànliàn", "pos": "động từ", "vi": "rèn luyện thân thể", "eg": "常锻炼身体好。"},
            {"num": 11, "zh": "音乐", "py": "yīnyuè", "pos": "danh từ", "vi": "âm nhạc", "eg": "我喜欢一边做作业一边听音乐。"},
            {"num": 12, "zh": "公园", "py": "gōngyuán", "pos": "danh từ", "vi": "công viên", "eg": "周末很多人去公园玩。"},
            {"num": 13, "zh": "聊天儿", "py": "liáotiānr", "pos": "động từ", "vi": "nói chuyện phiếm, tán gẫu", "eg": "下班后大家坐在一起聊天儿。"},
            {"num": 14, "zh": "睡着", "py": "shuìzháo", "pos": "động từ", "vi": "ngủ thiếp đi, ngủ được", "eg": "孩子太累了，很快就睡着了。"},
            {"num": 15, "zh": "更", "py": "gèng", "pos": "phó từ", "vi": "càng, hơn nữa", "eg": "明天会更好。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Bổ ngữ khả năng (可能补语): V + 得 / 不 + Bổ ngữ kết quả/xu hướng",
                "desc": "Dùng để biểu thị điều kiện khách quan hoặc chủ quan có cho phép hành động đạt được kết quả nào đó hay không. Khẳng định: 'V + 得 + C'; Phủ định: 'V + 不 + C'.",
                "examples": [
                    {"zh": "怎么突然找不到了？", "py": "Zěnme tūrán zhǎo bu dào le?", "vi": "Sao bỗng nhiên lại tìm không ra?"},
                    {"zh": "你看得见黑板上的字吗？", "py": "Nǐ kàn de jiàn hēibǎn shang de zì ma?", "vi": "Bạn có nhìn thấy chữ trên bảng đen không?"},
                    {"zh": "老师讲的话，我都听得懂。", "py": "Lǎoshī jiǎng de huà, wǒ dōu tīng de dǒng.", "vi": "Lời thầy giảng tôi đều nghe hiểu được."}
                ]
            },
            {
                "title": "2. Phân biệt “刚” và “刚才”",
                "desc": "“刚” là phó từ (chỉ hành động vừa mới xảy ra cách đây không lâu, đứng sau chủ ngữ trước động từ). “刚才” là danh từ chỉ thời gian (chỉ thời điểm vài phút trước, có thể đứng trước hoặc sau chủ ngữ).",
                "examples": [
                    {"zh": "我刚来中国两个月。", "py": "Wǒ gāng lái Zhōngguó liǎng ge yuè.", "vi": "Tôi vừa mới đến Trung Quốc được hai tháng."},
                    {"zh": "刚才你放哪儿了？", "py": "Gāngcái nǐ fàng nǎr le?", "vi": "Vừa nãy bạn đặt ở đâu?"}
                ]
            }
        ]
    },

    # ==================== BÀI 7 ====================
    {
        "id": 7,
        "title_zh": "我跟他都认识五年了。",
        "title_py": "Wǒ gēn tā dōu rènshi wǔ nián le.",
        "title_vi": "Tôi và cô ấy quen nhau được năm năm rồi.",
        "dialogues": [
            {
                "title": "Đoạn 1: 在办公室 (Ở văn phòng)",
                "location": "在办公室",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "那个新来的同事是谁？你认识吗？", "py": "Nà ge xīn lái de tóngshì shì shéi? Nǐ rènshi ma?", "vi": "Người đồng nghiệp mới đến kia là ai thế? Cậu quen không?"},
                    {"speaker": "同事B", "role": "female", "zh": "认识啊，她以前在银行工作，上个月才来我们公司。", "py": "Rènshi a, tā yǐqián zài yínháng gōngzuò, shàng ge yuè cái lái wǒmen gōngsī.", "vi": "Quen chứ, cô ấy trước đây làm việc ở ngân hàng, tháng trước mới chuyển đến công ty mình."},
                    {"speaker": "同事A", "role": "male", "zh": "你们认识多久了？", "py": "Nǐmen rènshi duōjiǔ le?", "vi": "Các cậu quen nhau bao lâu rồi?"},
                    {"speaker": "同事B", "role": "female", "zh": "我们认识五年了，读大学时就是同班同学。", "py": "Wǒmen rènshi wǔ nián le, dú dàxué shí jiù shì tóngbān tóngxué.", "vi": "Chúng tớ quen nhau năm năm rồi, hồi học đại học đã là bạn cùng lớp."}
                ]
            },
            {
                "title": "Đoạn 2: 聊感情经历 (Nói về chuyện tình cảm)",
                "location": "在咖啡厅",
                "lines": [
                    {"speaker": "朋友", "role": "male", "zh": "听说你和小丽准备结婚了？恭喜你们！", "py": "Tīngshuō nǐ hé Xiǎolì zhǔnbèi jiéhūn le? Gōngxǐ nǐmen!", "vi": "Nghe nói cậu với Tiểu Lệ chuẩn bị kết hôn rồi à? Chúc mừng hai bạn nhé!"},
                    {"speaker": "小刚", "role": "male", "zh": "谢谢！我们在一起已经三年多了。", "py": "Xièxie! Wǒmen zài yìqǐ yǐjīng sān nián duō le.", "vi": "Cảm ơn cậu! Chúng tớ ở bên nhau đã hơn ba năm rồi."},
                    {"speaker": "朋友", "role": "male", "zh": "什么时候办婚礼？到时一定要请我啊。", "py": "Shénme shíhou bàn hūnlǐ? Dào shí yídìng yào qǐng wǒ a.", "vi": "Khi nào thì tổ chức đám cưới? Đến lúc đó nhất định phải mời tớ đấy nhé."},
                    {"speaker": "小刚", "role": "male", "zh": "大概在今年年底，欢迎你来参加！", "py": "Dàgài zài jīnnián niándǐ, huānyíng nǐ lái cānjiā!", "vi": "Khoảng chừng cuối năm nay, rất hoan nghênh cậu đến dự!"}
                ]
            },
            {
                "title": "Đoạn 3: 聊兴趣爱好 (Nói về sở thích)",
                "location": "在休息室",
                "lines": [
                    {"speaker": "同事A", "role": "male", "zh": "你周末经常去踢足球吗？", "py": "Nǐ zhōumò jīngcháng qù tī zúqiú ma?", "vi": "Cuối tuần cậu có hay đi đá bóng không?"},
                    {"speaker": "同事B", "role": "female", "zh": "我对踢足球不感兴趣，我喜欢听音乐和看书。", "py": "Wǒ duì tī zúqiú bù gǎnxìngqù, wǒ xǐhuan tīng yīnyuè hé kànshū.", "vi": "Tớ không có hứng thú với đá bóng, tớ thích nghe nhạc và đọc sách."},
                    {"speaker": "同事A", "role": "male", "zh": "我以前也不喜欢，后来看了几场比赛，就越来越感兴趣了。", "py": "Wǒ yǐqián yě bù xǐhuan, hòulái kàn le jǐ chǎng bǐsài, jiù yuè lái yuè gǎnxìngqù le.", "vi": "Trước đây tớ cũng không thích, sau xem vài trận đấu thì ngày càng thấy hào hứng."},
                    {"speaker": "同事B", "role": "female", "zh": "运动能让人更健康，确实挺好的。", "py": "Yùndòng néng ràng rén gèng jiànkāng, quèshí tǐng hǎo de.", "vi": "Thể thao giúp con người khỏe mạnh hơn, đúng là rất tốt."}
                ]
            },
            {
                "title": "Đoạn 4: 约会迟到 (Đi hẹn hò muộn)",
                "location": "在电影院门口",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "你怎么现在才来？我都等你半个小时了！", "py": "Nǐ zěnme xiànzài cái lái? Wǒ dōu děng nǐ bàn ge xiǎoshí le!", "vi": "Sao bây giờ anh mới đến? Em đợi anh cả nửa tiếng đồng hồ rồi đấy!"},
                    {"speaker": "小刚", "role": "male", "zh": "真对不起！公司临时开会，路上又堵车。", "py": "Zhēn duìbuqǐ! Gōngsī línshí kāihuì, lùshang yòu dǔchē.", "vi": "Thực sự xin lỗi em! Công ty họp đột xuất, trên đường lại bị tắc xe."},
                    {"speaker": "小丽", "role": "female", "zh": "电影差一刻钟就开演了，快点儿进去吧。", "py": "Diànyǐng chà yí kè zhōng jiù kāiyǎn le, kuài diǎnr jìnqù ba.", "vi": "Phim còn kém 15 phút nữa là chiếu rồi, mau vào thôi anh."},
                    {"speaker": "小刚", "role": "male", "zh": "好，电影看完我请你吃好吃的，给你赔礼！", "py": "Hǎo, diànyǐng kànwán wǒ qǐng nǐ chī hǎochī de, gěi nǐ péilǐ!", "vi": "Được rồi, xem phim xong anh mời em ăn món ngon để tạ lỗi nhé!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：你们认识多长时间了？ 女：我们读大学就认识了，到现在都五年了。",
                "question": "他们认识多长时间了？",
                "options": ["A. 三年", "B. 四年", "C. 五年"],
                "ans": "C",
                "explain": "Người nữ nói: 到现在都五年了 (đến giờ đã 5 năm rồi)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚今天准时到了电影院，小丽一点儿也没等他。",
                "question": "Phán đoán đúng hay sai: 小刚今天迟到了。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Tiểu Lệ phải đợi nửa tiếng, chứng tỏ Tiểu Cương đến muộn (迟到)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：你对中国历史感兴趣吗？ 男：我非常感兴趣，买了很多关于中国历史的书。",
                "question": "男的对什么感兴趣？",
                "options": ["A. 中国历史", "B. 踢足球", "C. 电脑游戏"],
                "ans": "A",
                "explain": "Người nam trả lời rất có hứng thú với lịch sử Trung Quốc."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "男：现在几点了？ 女：差一刻八点，电影八点开始。",
                "question": "电影几点开始？",
                "options": ["A. 七点三刻", "B. 八点", "C. 八点一刻"],
                "ans": "B",
                "explain": "Người nữ nói rõ: 电影八点开始."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "我和他是在大学认识的，都认识五年了。", "py": "Wǒ hé tā shì zài dàxué rènshi de, dōu rènshi wǔ nián le.", "vi": "Tôi và anh ấy quen nhau hồi đại học, quen nhau 5 năm rồi."},
                {"id": "B", "text": "路上堵车，我迟到了半个小时。", "py": "Lùshang dǔchē, wǒ chídào le bàn ge xiǎoshí.", "vi": "Trên đường kẹt xe, tôi đến muộn nửa tiếng."},
                {"id": "C", "text": "他对弹吉他特别感兴趣。", "py": "Tā duì tán jítā tèbié gǎnxìngqù.", "vi": "Anh ấy đặc biệt có hứng thú với việc gảy đàn guitar."},
                {"id": "D", "text": "欢迎新同事加入我们的团队！", "py": "Huānyíng xīn tóngshì jiārù wǒmen de tuánduì!", "vi": "Hoan nghênh đồng nghiệp mới gia nhập đội ngũ của chúng tôi!"},
                {"id": "E", "text": "他们准备今年年底结婚。", "py": "Tāmen zhǔnbèi jīnnián niándǐ jiéhūn.", "vi": "Họ chuẩn bị kết hôn vào cuối năm nay."}
            ],
            "questions": [
                {"num": 21, "text": "你们俩是怎么认识的？认识多久了？", "py": "Nǐmen liǎ shì zěnme rènshi de? Rènshi duōjiǔ le?", "vi": "Hai bạn quen nhau thế nào? Quen bao lâu rồi?", "ans": "A", "explain": "Kể lại quen nhau ở đại học được 5 năm."},
                {"num": 22, "text": "你怎么现在才到？电影都要开始了！", "py": "Nǐ zěnme xiànzài cái dào? Diànyǐng dōu yào kāishǐ le!", "vi": "Sao giờ này cậu mới tới? Phim sắp chiếu rồi!", "ans": "B", "explain": "Giải thích lý do kẹt xe nên đến muộn."},
                {"num": 23, "text": "你弟弟业余时间喜欢做些什么？", "py": "Nǐ dìdi yèyú shíjiān xǐhuan zuò xiē shénme?", "vi": "Em trai bạn thời gian rảnh thích làm gì?", "ans": "C", "explain": "Nói về sở thích gảy đàn guitar."},
                {"num": 24, "text": "今天是我们部门新员工第一天上班。", "py": "Jīntiān shì wǒmen bùmén xīn yuángōng dì-yī tiān shàngbān.", "vi": "Hôm nay là ngày đầu đi làm của nhân viên mới phòng mình.", "ans": "D", "explain": "Chào mừng đồng nghiệp mới."},
                {"num": 25, "text": "听说他们在一起恋爱三年多了，什么时候办喜事？", "py": "Tīngshuō tāmen zài yìqǐ liàn'ài sān nián duō le, shénme shíhou bàn xǐshì?", "vi": "Nghe nói họ yêu nhau hơn 3 năm rồi, bao giờ tổ chức đám cưới?", "ans": "E", "explain": "Cho biết cuối năm nay sẽ kết hôn."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "以前", "py": "yǐqián", "vi": "trước đây"},
                {"id": "B", "zh": "银行", "py": "yínháng", "vi": "ngân hàng"},
                {"id": "C", "zh": "久", "py": "jiǔ", "vi": "lâu, thời gian dài"},
                {"id": "D", "zh": "结婚", "py": "jiéhūn", "vi": "kết hôn"},
                {"id": "E", "zh": "迟到", "py": "chídào", "vi": "đến muộn, trễ"}
            ],
            "questions": [
                {"num": 26, "prefix": "他在一家", "suffix": "工作，每天跟数字打交道。", "py": "Tā zài yì jiā ( ? ) gōngzuò, měitiān gēn shùzì dǎ jiāodào.", "vi": "Anh ấy làm việc ở một ( ? ), ngày nào cũng tiếp xúc với các con số.", "ans": "B", "word": "银行", "explain": "Làm việc ở ngân hàng (银行)."},
                {"num": 27, "prefix": "我们好", "suffix": "没见面了，你最近好吗？", "py": "Wǒmen hǎo ( ? ) méi jiànmiàn le, nǐ zuìjìn hǎo ma?", "vi": "Chúng mình đã rất ( ? ) không gặp nhau rồi, dạo này cậu khỏe không?", "ans": "C", "word": "久", "explain": "好久没见 (đã rất lâu không gặp)."},
                {"num": 28, "prefix": "他", "suffix": "是个老师，现在开了一家公司。", "py": "Tā ( ? ) shì ge lǎoshī, xiànzài kāi le yì jiā gōngsī.", "vi": "Anh ấy ( ? ) là giáo viên, hiện nay mở một công ty.", "ans": "A", "word": "以前", "explain": "Trước đây (以前)."},
                {"num": 29, "prefix": "他们决定明年春天", "suffix": "。", "py": "Tāmen juédìng míngnián chūntiān ( ? ).", "vi": "Họ quyết định mùa xuân năm sau sẽ ( ? ).", "ans": "D", "word": "结婚", "explain": "Kết hôn (结婚)."},
                {"num": 30, "prefix": "今天早上闹钟没响，我上班", "suffix": "了。", "py": "Jīntiān zǎoshang nàozhōng méi xiǎng, wǒ shàngbān ( ? ) le.", "vi": "Sáng nay đồng hồ báo thức không reo, tôi đi làm ( ? ) rồi.", "ans": "E", "word": "迟到", "explain": "Đi làm muộn (上班迟到)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "王朋和李友是大学同学，他们认识已经五年了。在大学的时候，两个人就对中国文化非常感兴趣，经常一起去图书馆借关于中国历史的书。毕业以后，王朋去了一家银行工作，李友在一家外语学校当老师。虽然工作都很忙，但他们每个周末都要见一面，喝喝茶，聊聊工作和生活。下个月李友就要结婚了，王朋非常为她高兴。",
            "passage_py": "Wáng Péng hé Lǐ Yǒu shì dàxué tóngxué, tāmen rènshi yǐjīng wǔ nián le. Zài dàxué de shíhou, liǎng ge rén jiù duì Zhōngguó wénhuà fēicháng gǎnxìngqù, jīngcháng yìqǐ qù túshūguǎn jiè guānyú Zhōngguó lìshǐ de shū. Bìyè yǐhòu, Wáng Péng qù le yì jiā yínháng gōngzuò, Lǐ Yǒu zài yì jiā wàiyǔ xuéxiào dāng lǎoshī. Suīrán gōngzuò dōu hěn máng, dàn tāmen měi ge zhōumò dōu yào jiàn yí miàn, hēhe chá, liáoliao gōngzuò hé shēnghuó. Xià ge yuè Lǐ Yǒu jiù yào jiéhūn le, Wáng Péng fēicháng wèi tā gāoxìng.",
            "passage_vi": "Vương Bằng và Lý Hữu là bạn học đại học, họ quen nhau đã được năm năm. Khi còn ở trường đại học, hai người đều vô cùng có hứng thú với văn hóa Trung Quốc, thường xuyên cùng nhau lên thư viện mượn sách lịch sử Trung Quốc. Sau khi tốt nghiệp, Vương Bằng đến làm việc ở một ngân hàng, còn Lý Hữu làm giáo viên tại một trường ngoại ngữ. Mặc dù công việc đều rất bận rộn, nhưng mỗi cuối tuần họ đều gặp nhau một lần, uống trà, trò chuyện về công việc và cuộc sống. Tháng sau Lý Hữu sắp kết hôn rồi, Vương Bằng cảm thấy vô cùng mừng cho cô ấy.",
            "questions": [
                {
                    "num": 31,
                    "text": "王朋和李友认识多久了？",
                    "options": ["A. 三年", "B. 四年", "C. 五年"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 他们认识已经五年了."
                },
                {
                    "num": 32,
                    "text": "大学时他们对什么感兴趣？",
                    "options": ["A. 踢足球", "B. 中国文化", "C. 玩游戏"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 对中国文化非常感兴趣."
                },
                {
                    "num": 33,
                    "text": "王朋毕业后在哪儿工作？",
                    "options": ["A. 学校", "B. 银行", "C. 医院"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 王朋去了一家银行工作."
                },
                {
                    "num": 34,
                    "text": "李友的工作是什么？",
                    "options": ["A. 老师", "B. 医生", "C. 经理"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 李友在一家外语学校当老师."
                },
                {
                    "num": 35,
                    "text": "李友下个月要做什么？",
                    "options": ["A. 去旅游", "B. 搬家", "C. 结婚"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 下个月李友就要结婚了."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["五年了", "都认识", "我跟他"],
                "ans": "我跟他都认识五年了。",
                "py": "Wǒ gēn tā dōu rènshi wǔ nián le.",
                "vi": "Tôi và anh ấy quen nhau được 5 năm rồi."
            },
            {
                "num": 37,
                "chunks": ["感兴趣", "我对中国历史", "非常"],
                "ans": "我对中国历史非常感兴趣。",
                "py": "Wǒ duì Zhōngguó lìshǐ fēicháng gǎnxìngqù.",
                "vi": "Tôi rất có hứng thú với lịch sử Trung Quốc."
            },
            {
                "num": 38,
                "chunks": ["在一家银行", "工作", "她以前"],
                "ans": "她以前在一家银行工作。",
                "py": "Tā yǐqián zài yì jiā yínháng gōngzuò.",
                "vi": "Trước đây cô ấy làm việc tại một ngân hàng."
            },
            {
                "num": 39,
                "chunks": ["今天上班", "小张", "迟到了半个小时"],
                "ans": "小张今天上班迟到了半个小时。",
                "py": "Xiǎo Zhāng jīntiān shàngbān chídào le bàn ge xiǎoshí.",
                "vi": "Hôm nay Tiểu Trương đi làm muộn nửa tiếng đồng hồ."
            },
            {
                "num": 40,
                "chunks": ["欢迎你", "我们的公司", "来到"],
                "ans": "欢迎你来到我们的公司。",
                "py": "Huānyíng nǐ láidào wǒmen de gōngsī.",
                "vi": "Chào mừng bạn đến với công ty chúng tôi."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我 (yǐqián) 没去过北京。",
                "pinyin": "yǐqián",
                "ans": "以前",
                "vi": "Trước đây tôi chưa từng đi Bắc Kinh."
            },
            {
                "num": 42,
                "sentence": "哥哥下个月准备 (jiéhūn)。",
                "pinyin": "jiéhūn",
                "ans": "结婚",
                "vi": "Anh trai tháng sau chuẩn bị kết hôn."
            },
            {
                "num": 43,
                "sentence": "他对学汉语很感 (xìngqù)。",
                "pinyin": "xìngqù",
                "ans": "兴趣",
                "vi": "Anh ấy rất có hứng thú với việc học tiếng Hán."
            },
            {
                "num": 44,
                "sentence": "我们已经等了 (bàn) 个小时了。",
                "pinyin": "bàn",
                "ans": "半",
                "vi": "Chúng tôi đã chờ được nửa tiếng rồi."
            },
            {
                "num": 45,
                "sentence": "新来的 (tóngshì) 工作很努力。",
                "pinyin": "tóngshì",
                "ans": "同事",
                "vi": "Đồng nghiệp mới đến làm việc rất chăm chỉ."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "同事", "py": "tóngshì", "pos": "danh từ", "vi": "đồng nghiệp", "eg": "同事之间要互相帮助。"},
            {"num": 2, "zh": "以前", "py": "yǐqián", "pos": "danh từ chỉ thời gian", "vi": "trước đây, trước kia", "eg": "以前我不太喜欢吃辣。"},
            {"num": 3, "zh": "银行", "py": "yínháng", "pos": "danh từ", "vi": "ngân hàng", "eg": "我得去银行换点儿钱。"},
            {"num": 4, "zh": "久", "py": "jiǔ", "pos": "tính từ", "vi": "lâu, thời gian dài", "eg": "这个问题我想了很久。"},
            {"num": 5, "zh": "感兴趣", "py": "gǎn xìngqù", "pos": "cụm động từ", "vi": "có hứng thú, thích thú", "eg": "我对学画画很感兴趣。"},
            {"num": 6, "zh": "结婚", "py": "jiéhūn", "pos": "động từ", "vi": "kết hôn, lấy nhau", "eg": "他们结婚已经十年了。"},
            {"num": 7, "zh": "欢迎", "py": "huānyíng", "pos": "động từ", "vi": "hoan nghênh, chào đón", "eg": "热烈欢迎新同学！"},
            {"num": 8, "zh": "迟到", "py": "chídào", "pos": "động từ", "vi": "đến muộn, trễ giờ", "eg": "上课千万不要迟到。"},
            {"num": 9, "zh": "半", "py": "bàn", "pos": "số từ", "vi": "nửa, rưỡi", "eg": "现在是八点半。"},
            {"num": 10, "zh": "接", "py": "jiē", "pos": "động từ", "vi": "đón, nhận", "eg": "我去机场接一个朋友。"},
            {"num": 11, "zh": "刻", "py": "kè", "pos": "lượng từ", "vi": "khắc (15 phút)", "eg": "还有一刻钟就下课了。"},
            {"num": 12, "zh": "差", "py": "chà", "pos": "động từ/tính từ", "vi": "kém, thiếu", "eg": "差五分七点。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Bổ ngữ thời lượng (时量补语): V + 了 + Thời lượng + 了",
                "desc": "Biểu thị khoảng thời gian mà một hành động đã duy trì kéo dài. Nếu cuối câu có thêm '了' biểu thị hành động đó vẫn còn đang tiếp tục diễn ra.",
                "examples": [
                    {"zh": "他在中国学了两年汉语。", "py": "Tā zài Zhōngguó xué le liǎng nián Hànyǔ.", "vi": "Anh ấy đã học tiếng Hán ở Trung Quốc 2 năm (nay không học nữa)."},
                    {"zh": "我跟他都认识五年了。", "py": "Wǒ gēn tā dōu rènshi wǔ nián le.", "vi": "Tôi và anh ấy quen nhau đã 5 năm rồi (và hiện tại vẫn đang quen nhau)."},
                    {"zh": "我们等了他半个小时了。", "py": "Wǒmen děng le tā bàn ge xiǎoshí le.", "vi": "Chúng tôi đã đợi anh ấy được nửa tiếng rồi (vẫn đang đợi)."}
                ]
            },
            {
                "title": "2. Cấu trúc “对……感兴趣 / 有兴趣”",
                "desc": "Dùng để biểu thị có sự yêu thích, hứng thú đối với một lĩnh vực, môn học hoặc hoạt động nào đó. Phủ định dùng '对……不感兴趣'.",
                "examples": [
                    {"zh": "我对中国历史非常感兴趣。", "py": "Wǒ duì Zhōngguó lìshǐ fēicháng gǎnxìngqù.", "vi": "Tôi rất có hứng thú với lịch sử Trung Quốc."},
                    {"zh": "他对足球一点儿兴趣也没有。", "py": "Tā duì zúqiú yìdiǎnr xìngqù yě méiyǒu.", "vi": "Anh ấy một chút hứng thú với bóng đá cũng không có."}
                ]
            }
        ]
    },

    # ==================== BÀI 8 ====================
    {
        "id": 8,
        "title_zh": "你去哪儿我就去哪儿。",
        "title_py": "Nǐ qù nǎr wǒ jiù qù nǎr.",
        "title_vi": "Em đi đâu thì anh đi đến đó.",
        "dialogues": [
            {
                "title": "Đoạn 1: 租房子 (Thuê nhà)",
                "location": "在看房子",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "你看这套房子怎么样？满意吗？", "py": "Nǐ kàn zhè tào fángzi zěnmeyàng? Mǎnyì ma?", "vi": "Em xem căn nhà này thế nào? Có vừa ý không?"},
                    {"speaker": "小丽", "role": "female", "zh": "虽然在八层，但是有电梯，上下楼挺方便的。", "py": "Suīrán zài bā céng, dànshì yǒu diàntī, shàngxià lóu tǐng fāngbiàn de.", "vi": "Tuy ở tầng 8, nhưng có thang máy, lên xuống lầu khá thuận tiện."},
                    {"speaker": "小刚", "role": "male", "zh": "周围环境也很安静，离地铁站又近。", "py": "Zhōuwéi huánjìng yě hěn ānjìng, lí dìtiězhàn yòu jìn.", "vi": "Môi trường xung quanh cũng yên tĩnh, lại gần ga tàu điện ngầm."},
                    {"speaker": "小丽", "role": "female", "zh": "那好，你觉得满意我们就租这套吧。", "py": "Nà hǎo, nǐ juéde mǎnyì wǒmen jiù zū zhè tào ba.", "vi": "Thế thì tốt, anh thấy ưng ý thì chúng mình thuê căn này đi."}
                ]
            },
            {
                "title": "Đoạn 2: 动物园看熊猫 (Đi sở thú xem gấu trúc)",
                "location": "在动物园",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "快看，那边有两只大熊猫！", "py": "Kuài kàn, nàbiān yǒu liǎng zhī dà xióngmāo!", "vi": "Mau nhìn kìa, đằng kia có hai chú gấu trúc to lớn!"},
                    {"speaker": "小丽", "role": "female", "zh": "太可爱了！它们正在安静地吃竹子呢。", "py": "Tài kě'ài le! Tāmen zhèngzài ānjìng de chī zhúzi ne.", "vi": "Đáng yêu quá! Chúng đang yên lặng ăn tre trúc kìa."},
                    {"speaker": "小刚", "role": "male", "zh": "刚才看到老虎你还害怕，现在不怕了吧？", "py": "Gāngcái kàndào lǎohǔ nǐ hái hàipà, xiànzài bú pà le ba?", "vi": "Lúc nãy thấy hổ em còn sợ hãi, bây giờ hết sợ rồi chứ?"},
                    {"speaker": "小丽", "role": "female", "zh": "熊猫这么温和，谁会害怕熊猫呀。", "py": "Xióngmāo zhème wēnhé, shéi huì hàipà xióngmāo ya.", "vi": "Gấu trúc hiền hòa thế này, ai mà sợ gấu trúc chứ."}
                ]
            },
            {
                "title": "Đoạn 3: 在餐厅点餐 (Gọi món trong nhà hàng)",
                "location": "在餐厅",
                "lines": [
                    {"speaker": "服务员", "role": "male", "zh": "两位想吃点儿什么？", "py": "Liǎng wèi xiǎng chī diǎnr shénme?", "vi": "Hai vị muốn dùng món gì ạ?"},
                    {"speaker": "小丽", "role": "female", "zh": "小刚，你想吃什么？你点什么我就吃什么。", "py": "Xiǎogāng, nǐ xiǎng chī shénme? Nǐ diǎn shénme wǒ jiù chī shénme.", "vi": "Tiểu Cương, anh muốn ăn gì? Anh gọi gì thì em ăn nấy."},
                    {"speaker": "小刚", "role": "male", "zh": "那来一份宫保鸡丁，一条鱼，两杯可乐。", "py": "Nà lái yí fèn gōngbǎojīdīng, yì tiáo yú, liǎng bēi kělè.", "vi": "Thế cho một phần gà Cung Bảo, một con cá và hai cốc Coca nhé."},
                    {"speaker": "小丽", "role": "female", "zh": "我去洗手间洗一下手，马上就回来。", "py": "Wǒ qù xǐshǒujiān xǐ yíxià shǒu, mǎshàng jiù huílái.", "vi": "Em đi nhà vệ sinh rửa tay một chút, sẽ quay lại ngay."}
                ]
            },
            {
                "title": "Đoạn 4: 聊健康与变化 (Nói về sức khỏe và thay đổi)",
                "location": "在路上",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "几年没见，老张的变化真大。", "py": "Jǐ nián méi jiàn, lǎo Zhāng de biànhuà zhēn dà.", "vi": "Mấy năm không gặp, anh Trương thay đổi nhiều thật."},
                    {"speaker": "小丽", "role": "female", "zh": "是啊，他以前很瘦，现在几乎胖了一倍。", "py": "Shì a, tā yǐqián hěn shòu, xiànzài jīhū pàng le yí bèi.", "vi": "Đúng thế, trước đây anh ấy gầy lắm, giờ hầu như béo lên gấp đôi rồi."},
                    {"speaker": "小刚", "role": "male", "zh": "人上了年纪，健康最重要，明天我又要去锻炼了。", "py": "Rén shàng le niánjì, jiànkāng zuì zhòngyào, míngtiān wǒ yòu yào qù duànliàn le.", "vi": "Người ta có tuổi rồi sức khỏe là quan trọng nhất, ngày mai anh lại phải đi tập thể dục thôi."},
                    {"speaker": "小丽", "role": "female", "zh": "你去哪儿我就去哪儿，我们一起跑步吧！", "py": "Nǐ qù nǎr wǒ jiù qù nǎr, wǒmen yìqǐ pǎobù ba!", "vi": "Anh đi đâu thì em đi đó, chúng mình cùng chạy bộ nhé!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "男：你觉得这套房子怎么样？ 女：离地铁站很近，又有电梯，我很满意。",
                "question": "女的对房子满意吗？",
                "options": ["A. 不满意", "B. 很满意", "C. 觉得太贵"],
                "ans": "B",
                "explain": "Cô gái nói: 我很满意 (rất hài lòng)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小丽看到大熊猫的时候，吓得不敢看，特别害怕。",
                "question": "Phán đoán đúng hay sai: 小丽很害怕大熊猫。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Tiểu Lệ khen gấu trúc đáng yêu, hiền hòa, không hề sợ hãi."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：今天中饭吃什么？ 男：你想吃什么我们就吃什么，听你的。",
                "question": "男的意思是什么？",
                "options": ["A. 他想吃面条", "B. 让女的决定吃什么", "C. 他不想吃中饭"],
                "ans": "B",
                "explain": "Người nam nói: 你想吃什么我们就吃什么 (cậu muốn ăn gì thì ăn nấy)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "男：老张，好久不见，你变化真大！ 男2：是啊，最近几年越来越胖了。",
                "question": "老张最近几年有什么变化？",
                "options": ["A. 变瘦了", "B. 变胖了", "C. 变高了"],
                "ans": "B",
                "explain": "Đoạn thoại nói rõ: 最近几年越来越胖了."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "这套房子很安静，环境也很好。", "py": "Zhè tào fángzi hěn ānjìng, huánjìng yě hěn hǎo.", "vi": "Căn nhà này rất yên tĩnh, môi trường cũng rất tốt."},
                {"id": "B", "text": "熊猫在安静地吃竹子，太可爱了。", "py": "Xióngmāo zài ānjìng de chī zhúzi, tài kě'ài le.", "vi": "Gấu trúc đang yên lặng ăn tre trúc, đáng yêu quá."},
                {"id": "C", "text": "你去哪儿我就去哪儿，听你的。", "py": "Nǐ qù nǎr wǒ jiù qù nǎr, tīng nǐ de.", "vi": "Bạn đi đâu tôi đi đó, nghe theo bạn."},
                {"id": "D", "text": "我去洗手间洗一下手，马上就来。", "py": "Wǒ qù xǐshǒujiān xǐ yíxià shǒu, mǎshàng jiù lái.", "vi": "Tôi đi nhà vệ sinh rửa tay một chút, lại ngay đây."},
                {"id": "E", "text": "对人来说，身体健康是最重要的。", "py": "Duì rén lái shuō, shēntǐ jiànkāng shì zuì zhòngyào de.", "vi": "Đối với con người mà nói, sức khỏe là điều quan trọng nhất."}
            ],
            "questions": [
                {"num": 21, "text": "你觉得我们租这间屋子怎么样？", "py": "Nǐ juéde wǒmen zū zhè jiān wūzi zěnmeyàng?", "vi": "Bạn thấy chúng mình thuê căn phòng này thế nào?", "ans": "A", "explain": "Khen nhà yên tĩnh, môi trường tốt."},
                {"num": 22, "text": "动物园里的动物你最喜欢哪一个？", "py": "Dòngwùyuán li de dòngwù nǐ zuì xǐhuan nǎ yí ge?", "vi": "Động vật trong sở thú bạn thích con nào nhất?", "ans": "B", "explain": "Thích gấu trúc đáng yêu ăn tre trúc."},
                {"num": 23, "text": "明天放假，我们到底去哪儿玩儿呢？", "py": "Míngtiān fàngjià, wǒmen dàodǐ qù nǎr wánr ne?", "vi": "Ngày mai nghỉ lễ, rốt cuộc chúng mình đi đâu chơi?", "ans": "C", "explain": "Bạn đi đâu tôi đi đó (我去哪儿你就去哪儿)."},
                {"num": 24, "text": "菜都上齐了，快过来吃吧！", "py": "Cài dōu shàng qí le, kuài guòlái chī ba!", "vi": "Món ăn dọn đủ cả rồi, mau lại ăn đi!", "ans": "D", "explain": "Bảo đi rửa tay rồi lại ngay."},
                {"num": 25, "text": "工作再忙也要注意休息啊。", "py": "Gōngzuò zài máng yě yào zhùyì xiūxi a.", "vi": "Công việc dù bận cũng phải chú ý nghỉ ngơi nhé.", "ans": "E", "explain": "Khẳng định sức khỏe là quan trọng nhất."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "满意", "py": "mǎnyì", "vi": "hài lòng, vừa ý"},
                {"id": "B", "zh": "电梯", "py": "diàntī", "vi": "thang máy"},
                {"id": "C", "zh": "害怕", "py": "hàipà", "vi": "sợ hãi"},
                {"id": "D", "zh": "安静", "py": "ānjìng", "vi": "yên tĩnh"},
                {"id": "E", "zh": "健康", "py": "jiànkāng", "vi": "khỏe mạnh, sức khỏe"}
            ],
            "questions": [
                {"num": 26, "prefix": "大家都在图书馆看书，这里非常", "suffix": "。", "py": "Dàjiā dōu zài túshūguǎn kànshū, zhèlǐ fēicháng ( ? ).", "vi": "Mọi người đều đọc sách trong thư viện, ở đây vô cùng ( ? ).", "ans": "D", "word": "安静", "explain": "Thư viện rất yên tĩnh (安静)."},
                {"num": 27, "prefix": "住在十几层，没有", "suffix": "可不行。", "py": "Zhù zài shí jǐ céng, méiyǒu ( ? ) kě bùxíng.", "vi": "Sống ở mười mấy tầng lầu, không có ( ? ) thì không xong.", "ans": "B", "word": "电梯", "explain": "Lầu cao cần có thang máy (电梯)."},
                {"num": 28, "prefix": "老板对他的工作表现非常", "suffix": "。", "py": "Lǎobǎn duì tā de gōngzuò biǎoxiàn fēicháng ( ? ).", "vi": "Ông chủ đối với biểu hiện công việc của anh ấy rất ( ? ).", "ans": "A", "word": "满意", "explain": "Rất hài lòng (非常满意)."},
                {"num": 29, "prefix": "这只小狗很温和，你别", "suffix": "。", "py": "Zhè zhī xiǎogǒu hěn wēnhé, nǐ bié ( ? ).", "vi": "Chú chó con này rất ngoan hiền, bạn đừng ( ? ).", "ans": "C", "word": "害怕", "explain": "Đừng sợ hãi (别害怕)."},
                {"num": 30, "prefix": "多吃蔬菜和水果对身体", "suffix": "有好处。", "py": "Duō chī shūcài hé shuǐguǒ duì shēntǐ ( ? ) yǒu hǎochu.", "vi": "Ăn nhiều rau và trái cây có lợi cho ( ? ) cơ thể.", "ans": "E", "word": "健康", "explain": "Sức khỏe (身体健康)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "小刚和小丽打算租一套新房子。他们看了好几套房子，最后看中了学校附近的一套。这套房子在六层，虽然楼层有点儿高，但是大楼里有电梯，上下楼非常方便。房子的采光很好，周围环境特别安静。更重要的是，房子离地铁站走路只需要五分钟，小刚和小丽都觉得很满意，他们决定明天就跟房东签合同。",
            "passage_py": "Xiǎogāng hé Xiǎolì dǎsuàn zū yí tào xīn fángzi. Tāmen kàn le hǎo jǐ tào fángzi, zuìhòu kànzhòng le xuéxiào fùjìn de yí tào. Zhè tào fángzi zài liù céng, suīrán lóucéng yǒudiǎnr gāo, dànshì dàlóu li yǒu diàntī, shàngxià lóu fēicháng fāngbiàn. Fángzi de cǎiguāng hěn hǎo, zhōuwéi huánjìng tèbié ānjìng. Gèng zhòngyào de shì, fángzi lí dìtiězhàn zǒulù zhǐ xūyào wǔ fēnzhōng, Xiǎogāng hé Xiǎolì dōu juéde hěn mǎnyì, tāmen juédìng míngtiān jiù gēn fángdōng qiān hétong.",
            "passage_vi": "Tiểu Cương và Tiểu Lệ dự định thuê một căn nhà mới. Họ đã xem qua rất nhiều căn hộ, cuối cùng ưng ý một căn gần trường học. Căn nhà này ở tầng sáu, tuy tầng hơi cao nhưng trong tòa nhà có thang máy, việc lên xuống lầu rất thuận tiện. Ánh sáng của căn nhà rất tốt, môi trường xung quanh đặc biệt yên tĩnh. Quan trọng hơn là, căn nhà đi bộ đến ga tàu điện ngầm chỉ mất 5 phút, Tiểu Cương và Tiểu Lệ đều cảm thấy rất hài lòng, họ quyết định ngày mai sẽ ký hợp đồng với chủ nhà.",
            "questions": [
                {
                    "num": 31,
                    "text": "这套房子在几层？",
                    "options": ["A. 四层", "B. 六层", "C. 八层"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 这套房子在六层."
                },
                {
                    "num": 32,
                    "text": "房子周围的环境怎么样？",
                    "options": ["A. 特别吵", "B. 特别安静", "C. 车很多"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 周围环境特别安静."
                },
                {
                    "num": 33,
                    "text": "上下楼方便吗？为什么？",
                    "options": ["A. 方便，因为有电梯", "B. 不方便，楼梯太高", "C. 方便，因为在一楼"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 大楼里有电梯，上下楼非常方便."
                },
                {
                    "num": 34,
                    "text": "从房子走到地铁站需要多长时间？",
                    "options": ["A. 半个小时", "B. 十五分钟", "C. 五分钟"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 离地铁站走路只需要五分钟."
                },
                {
                    "num": 35,
                    "text": "他们打算明天做什么？",
                    "options": ["A. 继续看房子", "B. 签合同租房", "C. 去外地旅游"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 决定明天就跟房东签合同."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["你去哪儿", "我就去", "哪儿"],
                "ans": "你去哪儿我就去哪儿。",
                "py": "Nǐ qù nǎr wǒ jiù qù nǎr.",
                "vi": "Em đi đâu thì anh đi đến đó."
            },
            {
                "num": 37,
                "chunks": ["很满意", "对这套房子", "我们"],
                "ans": "我们对这套房子很满意。",
                "py": "Wǒmen duì zhè tào fángzi hěn mǎnyì.",
                "vi": "Chúng tôi rất hài lòng với căn nhà này."
            },
            {
                "num": 38,
                "chunks": ["在安静地", "大熊猫", "吃竹子"],
                "ans": "大熊猫在安静地吃竹子。",
                "py": "Dà xióngmāo zài ānjìng de chī zhúzi.",
                "vi": "Gấu trúc lớn đang yên lặng ăn tre trúc."
            },
            {
                "num": 39,
                "chunks": ["是最重要的", "身体健康", "对每个人来说"],
                "ans": "对每个人来说身体健康是最重要的。",
                "py": "Duì měi ge rén lái shuō shēntǐ jiànkāng shì zuì zhòngyào de.",
                "vi": "Đối với mỗi người mà nói, sức khỏe là điều quan trọng nhất."
            },
            {
                "num": 40,
                "chunks": ["有电梯", "上下楼", "很方便"],
                "ans": "有电梯上下楼很方便。",
                "py": "Yǒu diàntī shàngxià lóu hěn fāngbiàn.",
                "vi": "Có thang máy nên lên xuống lầu rất tiện lợi."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "坐 (diàntī) 上楼很快。",
                "pinyin": "diàntī",
                "ans": "电梯",
                "vi": "Đi thang máy lên lầu rất nhanh."
            },
            {
                "num": 42,
                "sentence": "小明很喜欢大 (xióngmāo)。",
                "pinyin": "xióngmāo",
                "ans": "熊猫",
                "vi": "Tiểu Minh rất thích gấu trúc lớn."
            },
            {
                "num": 43,
                "sentence": "图书馆里请保持 (ānjìng)。",
                "pinyin": "ānjìng",
                "ans": "安静",
                "vi": "Trong thư viện xin giữ yên tĩnh."
            },
            {
                "num": 44,
                "sentence": "我 (mǎshàng) 就做完作业了。",
                "pinyin": "mǎshàng",
                "ans": "马上",
                "vi": "Tôi sắp làm xong bài tập ngay rồi."
            },
            {
                "num": 45,
                "sentence": "祝你身体 (jiànkāng)！",
                "pinyin": "jiànkāng",
                "ans": "健康",
                "vi": "Chúc bạn sức khỏe dồi dào!"
            }
        ],
        "vocab": [
            {"num": 1, "zh": "又", "py": "yòu", "pos": "phó từ", "vi": "lại (hành động lặp lại)", "eg": "你怎么又迟到了？"},
            {"num": 2, "zh": "满意", "py": "mǎnyì", "pos": "tính từ", "vi": "hài lòng, vừa ý", "eg": "客人对服务感到很满意。"},
            {"num": 3, "zh": "电梯", "py": "diàntī", "pos": "danh từ", "vi": "thang máy", "eg": "我们坐电梯上八楼吧。"},
            {"num": 4, "zh": "层", "py": "céng", "pos": "lượng từ", "vi": "tầng, lớp", "eg": "这栋大楼一共有二十层。"},
            {"num": 5, "zh": "害怕", "py": "hàipà", "pos": "động từ/tính từ", "vi": "sợ hãi, e ngại", "eg": "小孩子都害怕打针。"},
            {"num": 6, "zh": "熊猫", "py": "xióngmāo", "pos": "danh từ", "vi": "gấu trúc", "eg": "大熊猫是中国的国宝。"},
            {"num": 7, "zh": "见面", "py": "jiànmiàn", "pos": "động từ", "vi": "gặp mặt", "eg": "好久没和你见面了。"},
            {"num": 8, "zh": "安静", "py": "ānjìng", "pos": "tính từ", "vi": "yên tĩnh, thanh tĩnh", "eg": "教室里非常安静。"},
            {"num": 9, "zh": "可乐", "py": "kělè", "pos": "danh từ", "vi": "nước coca", "eg": "服务员，给我来一杯可乐。"},
            {"num": 10, "zh": "一会儿", "py": "yíhuìr", "pos": "danh từ chỉ thời gian", "vi": "một lát, chốc lát", "eg": "请您稍等一会儿。"},
            {"num": 11, "zh": "马上", "py": "mǎshàng", "pos": "phó từ", "vi": "ngay lập tức, tức thì", "eg": "我马上就到。"},
            {"num": 12, "zh": "洗手间", "py": "xǐshǒujiān", "pos": "danh từ", "vi": "nhà vệ sinh", "eg": "请问洗手间在哪儿？"},
            {"num": 13, "zh": "老", "py": "lǎo", "pos": "tính từ", "vi": "già, cũ, lâu năm", "eg": "这是我的一位老朋友。"},
            {"num": 14, "zh": "几乎", "py": "jīhū", "pos": "phó từ", "vi": "hầu như, gần như", "eg": "作业几乎都做完了。"},
            {"num": 15, "zh": "变化", "py": "biànhuà", "pos": "danh từ/động từ", "vi": "sự thay đổi, biến hóa", "eg": "城市这几年的变化很大。"},
            {"num": 16, "zh": "健康", "py": "jiànkāng", "pos": "tính từ/danh từ", "vi": "khỏe mạnh, sức khỏe", "eg": "健康是最大的财富。"},
            {"num": 17, "zh": "重要", "py": "zhòngyào", "pos": "tính từ", "vi": "quan trọng", "eg": "学好汉语对我非常重要。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Đại từ nghi vấn dùng phiếm chỉ: Nghi vấn từ …… 就 ……",
                "desc": "Hai vế câu cùng dùng một đại từ nghi vấn (như 哪儿, 谁, 什么, 怎么), vế sau có thêm '就', biểu thị sự lựa chọn hoặc hành động ở vế sau hoàn toàn phụ thuộc vào vế trước.",
                "examples": [
                    {"zh": "你去哪儿我就去哪儿。", "py": "Nǐ qù nǎr wǒ jiù qù nǎr.", "vi": "Em đi đâu thì anh đi đến đó."},
                    {"zh": "你想吃什么我们就吃什么。", "py": "Nǐ xiǎng chī shénme wǒmen jiù chī shénme.", "vi": "Cậu muốn ăn gì thì chúng mình ăn nấy."},
                    {"zh": "谁想去谁就去。", "py": "Shéi xiǎng qù shéi jiù qù.", "vi": "Ai muốn đi thì người đó đi."}
                ]
            },
            {
                "title": "2. Phân biệt phó từ “又” và “再”",
                "desc": "Cả hai đều biểu thị sự lặp lại của hành động. '又' thường dùng cho hành động ĐÃ lặp lại (thường trong quá khứ hoặc hiện tại). '再' dùng cho hành động SẼ lặp lại trong tương lai.",
                "examples": [
                    {"zh": "昨天他来了，今天他又来了。", "py": "Zuótiān tā lái le, jīntiān tā yòu lái le.", "vi": "Hôm qua anh ấy đến, hôm nay anh ấy lại đến nữa rồi (đã xảy ra dùng 又)."},
                    {"zh": "欢迎你下次再来！", "py": "Huānyíng nǐ xià cì zài lái!", "vi": "Hoan nghênh bạn lần sau lại tới nhé! (tương lai dùng 再)."}
                ]
            }
        ]
    },

    # ==================== BÀI 9 ====================
    {
        "id": 9,
        "title_zh": "她的汉语说得跟中国人一样好。",
        "title_py": "Tā de hànyǔ shuō de gēn zhōngguó rén yíyàng hǎo.",
        "title_vi": "Cô ấy nói tiếng Trung hay như người Trung Quốc vậy.",
        "dialogues": [
            {
                "title": "Đoạn 1: 聊中文学习 (Nói về việc học tiếng Trung)",
                "location": "在教室",
                "lines": [
                    {"speaker": "大卫", "role": "male", "zh": "马可，你的汉语说得真流利！", "py": "Mǎkě, nǐ de hànyǔ shuō de zhēn liúlì!", "vi": "Marco, tiếng Hán của cậu nói lưu loát thật đấy!"},
                    {"speaker": "马可", "role": "male", "zh": "哪里哪里，我们班大山的中文说得跟中国人一样好。", "py": "Nǎli nǎli, wǒmen bān Dàshān de zhōngwén shuō de gēn zhōngguó rén yíyàng hǎo.", "vi": "Đâu có đâu, Đại Sơn lớp tớ nói tiếng Trung giỏi như người bản xứ vậy."},
                    {"speaker": "大卫", "role": "male", "zh": "他学了几年了？", "py": "Tā xué le jǐ nián le?", "vi": "Cậu ấy đã học mấy năm rồi?"},
                    {"speaker": "马可", "role": "male", "zh": "他学了四年了，而且天天跟中国朋友聊天儿。", "py": "Tā xué le sì nián le, érqiě tiāntiān gēn zhōngguó péngyou liáotiānr.", "vi": "Cậu ấy học 4 năm rồi, hơn nữa ngày nào cũng trò chuyện với bạn người Trung Quốc."}
                ]
            },
            {
                "title": "Đoạn 2: 谈考试与放心 (Nói về thi cử và an tâm)",
                "location": "在走廊",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "明天的HSK三级考试，你准备得怎么样了？", "py": "Míngtiān de HSK sān jí kǎoshì, nǐ zhǔnbèi de zěnmeyàng le?", "vi": "Kỳ thi HSK 3 ngày mai, cậu chuẩn bị thế nào rồi?"},
                    {"speaker": "小刚", "role": "male", "zh": "听力没问题，但我比较担心阅读题。", "py": "Tīnglì méi wèntí, dàn wǒ bǐjiào dānxīn yuèdú tí.", "vi": "Phần nghe không có vấn đề, nhưng tớ hơi lo lắng phần đọc hiểu."},
                    {"speaker": "小丽", "role": "female", "zh": "你平时那么努力，一定能考好的，放心吧！", "py": "Nǐ píngshí nàme nǔlì, yídìng néng kǎohǎo de, fàngxīn ba!", "vi": "Bình thường cậu chăm chỉ thế, nhất định sẽ thi tốt mà, yên tâm đi!"},
                    {"speaker": "小刚", "role": "male", "zh": "听你这么说，我心里轻松多了。", "py": "Tīng nǐ zhème shuō, wǒ xīnlǐ qīngsōng duō le.", "vi": "Nghe cậu nói vậy, trong lòng tớ nhẹ nhõm hơn nhiều rồi."}
                ]
            },
            {
                "title": "Đoạn 3: 爬山比赛 (Thi leo núi)",
                "location": "在山路上",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "小丽，你怎么走得跟我一样慢啊？", "py": "Xiǎolì, nǐ zěnme zǒu de gēn wǒ yíyàng màn a?", "vi": "Tiểu Lệ, sao em đi chậm như anh thế?"},
                    {"speaker": "小丽", "role": "female", "zh": "山路越走越高，我越走越累，脚都酸了。", "py": "Shānlù yuè zǒu yuè gāo, wǒ yuè zǒu yuè lèi, jiǎo dōu suān le.", "vi": "Đường núi càng đi càng dốc, em càng đi càng mệt, chân mỏi nhừ rồi."},
                    {"speaker": "小刚", "role": "male", "zh": "前面的风景特别漂亮，到了山顶我们就休息。", "py": "Qiánmiàn de fēngjǐng tèbié piàoliang, dào le shāndǐng wǒmen jiù xiūxi.", "vi": "Phong cảnh phía trước đẹp lắm, lên đến đỉnh núi chúng mình sẽ nghỉ ngơi."},
                    {"speaker": "小丽", "role": "female", "zh": "好，坚持就是胜利，我们一起上去！", "py": "Hǎo, jiānchí jiù shì shènglì, wǒmen yìqǐ shàngqù!", "vi": "Được, kiên trì là chiến thắng, chúng mình cùng lên nhé!"}
                ]
            },
            {
                "title": "Đoạn 4: 谈参加活动 (Nói về tham gia hoạt động)",
                "location": "在学生活动中心",
                "lines": [
                    {"speaker": "同学A", "role": "male", "zh": "学校下星期举办中国文化活动，你参加吗？", "py": "Xuéxiào xià xīngqī jǔbàn Zhōngguó wénhuà huódòng, nǐ cānjiā ma?", "vi": "Trường tuần sau tổ chức hoạt động văn hóa Trung Quốc, cậu có tham gia không?"},
                    {"speaker": "同学B", "role": "female", "zh": "我一定参加，多参加活动可以更了解中国文化。", "py": "Wǒ yídìng cānjiā, duō cānjiā huódòng kěyǐ gèng liǎojiě Zhōngguó wénhuà.", "vi": "Tớ nhất định tham gia, tham gia nhiều hoạt động có thể hiểu hơn về văn hóa Trung Quốc."},
                    {"speaker": "同学A", "role": "male", "zh": "我们班很多同学都报名了，大家的影响力真大。", "py": "Wǒmen bān hěn duō tóngxué dōu bàomíng le, dàjiā de yǐngxiǎnglì zhēn dà.", "vi": "Lớp mình rất nhiều bạn đã đăng ký rồi, sức lan tỏa của mọi người thật lớn."},
                    {"speaker": "同学B", "role": "female", "zh": "到时大家一起穿中国传统衣服，一定很有意思！", "py": "Dào shí dàjiā yìqǐ chuān Zhōngguó chuántǒng yīfu, yídìng hěn yǒu yìsi!", "vi": "Đến lúc đó mọi người cùng mặc trang phục truyền thống Trung Quốc, chắc chắn sẽ thú vị lắm!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你觉得大山的汉语水平怎么样？ 男：他的中文说得跟中国人一样好。",
                "question": "大山的汉语水平怎么样？",
                "options": ["A. 不太好", "B. 刚刚开始学", "C. 跟中国人一样好"],
                "ans": "C",
                "explain": "Đoạn thoại khẳng định: 跟中国人一样好."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚明天的考试准备得很好，一点儿也不担心。",
                "question": "Phán đoán đúng hay sai: 小刚很担心阅读题。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Tiểu Cương nói: 我比较担心阅读题 (khá lo lắng phần đọc)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：你越走越慢，是不是累了？ 女：是啊，山越来越高，我都走不动了。",
                "question": "女的为什么走得慢？",
                "options": ["A. 她不想去山顶", "B. 她太累了", "C. 她在看风景"],
                "ans": "B",
                "explain": "Cô gái bảo mệt quá không bước nổi: 我越走越累."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：下个星期的文化节你参加吗？ 男：我当然参加，我已经报名了。",
                "question": "男的会去参加文化节吗？",
                "options": ["A. 不去", "B. 会去", "C. 还没想好"],
                "ans": "B",
                "explain": "Người nam nói: 我当然参加，我已经报名了."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "她的中文说得跟中国人一样好。", "py": "Tā de zhōngwén shuō de gēn zhōngguó rén yíyàng hǎo.", "vi": "Tiếng Trung của cô ấy nói giỏi như người Trung Quốc vậy."},
                {"id": "B", "text": "你复习得很认真，考试一定没问题，放心吧。", "py": "Nǐ fùxí de hěn rènzhēn, kǎoshì yídìng méi wèntí, fàngxīn ba.", "vi": "Bạn ôn tập rất chăm chỉ, thi cử nhất định không vấn đề gì, yên tâm đi."},
                {"id": "C", "text": "山路越走越陡，大家走慢点儿。", "py": "Shānlù yuè zǒu yuè dǒu, dàjiā zǒu màn diǎnr.", "vi": "Đường núi càng đi càng dốc, mọi người đi chậm thôi."},
                {"id": "D", "text": "多跟中国朋友聊天儿，对学汉语有很大影响。", "py": "Duō gēn zhōngguó péngyou liáotiānr, duì xué hànyǔ yǒu hěn dà yǐngxiǎng.", "vi": "Trò chuyện nhiều với bạn bè người Trung Quốc có ảnh hưởng rất lớn tới việc học tiếng Hán."},
                {"id": "E", "text": "我们班同学都报名参加了这项比赛。", "py": "Wǒmen bān tóngxué dōu bàomíng cānjiā le zhè xiàng bǐsài.", "vi": "Các bạn lớp mình đều đã đăng ký tham gia cuộc thi này."}
            ],
            "questions": [
                {"num": 21, "text": "大山在中国生活了几年，口语怎么样？", "py": "Dàshān zài Zhōngguó shēnghuó le jǐ nián, kǒuyǔ zěnmeyàng?", "vi": "Đại Sơn sống ở Trung Quốc vài năm, khẩu ngữ thế nào?", "ans": "A", "explain": "Khen nói tiếng Trung tốt như người bản xứ."},
                {"num": 22, "text": "明天就要考试了，我心里很紧张。", "py": "Míngtiān jiù yào kǎoshì le, wǒ xīnlǐ hěn jǐnzhāng.", "vi": "Ngày mai thi rồi, trong lòng tôi căng thẳng quá.", "ans": "B", "explain": "Động viên yên tâm vì đã ôn tập kỹ."},
                {"num": 23, "text": "怎么大家都走得这么慢？", "py": "Zěnme dàjiā dōu zǒu de zhème màn?", "vi": "Sao mọi người đều đi chậm thế?", "ans": "C", "explain": "Do đường núi càng đi càng dốc."},
                {"num": 24, "text": "怎样才能快速提高汉语听说水平？", "py": "Zěnyàng cái néng kuàisù tígāo hànyǔ tīngshuō shuǐpíng?", "vi": "Làm thế nào mới nâng cao nhanh trình độ nghe nói tiếng Hán?", "ans": "D", "explain": "Khuyên trò chuyện nhiều với người bản ngữ."},
                {"num": 25, "text": "下周学校举行的演讲比赛有人去吗？", "py": "Xià zhōu xuéxiào jǔxíng de yǎnjiǎng bǐsài yǒu rén qù ma?", "vi": "Cuộc thi hùng biện trường tổ chức tuần sau có ai đi không?", "ans": "E", "explain": "Cả lớp đều đã đăng ký tham gia."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "中文", "py": "zhōngwén", "vi": "tiếng Trung, văn tự tiếng Hán"},
                {"id": "B", "zh": "一样", "py": "yíyàng", "vi": "như nhau, giống nhau"},
                {"id": "C", "zh": "放心", "py": "fàngxīn", "vi": "yên tâm"},
                {"id": "D", "zh": "了解", "py": "liǎojiě", "vi": "hiểu rõ, tìm hiểu"},
                {"id": "E", "zh": "参加", "py": "cānjiā", "vi": "tham gia"}
            ],
            "questions": [
                {"num": 26, "prefix": "他的大衣跟我买的颜色", "suffix": "。", "py": "Tā de dàyī gēn wǒ mǎi de yánsè ( ? ).", "vi": "Áo khoác của anh ấy màu sắc ( ? ) với cái tôi mua.", "ans": "B", "word": "一样", "explain": "Giống nhau: 跟...一样 (yíyàng)."},
                {"num": 27, "prefix": "你认真复习了，请", "suffix": "，一定能考过的。", "py": "Nǐ rènzhēn fùxí le, qǐng ( ? ), yídìng néng kǎoguò de.", "vi": "Cậu ôn tập chăm chỉ rồi, xin hãy ( ? ), nhất định sẽ đỗ thôi.", "ans": "C", "word": "放心", "explain": "Yên tâm: 放心 (fàngxīn)."},
                {"num": 28, "prefix": "多去各地走走，能更", "suffix": "当地的文化。", "py": "Duō qù gè dì zǒuzou, néng gèng ( ? ) dāngdì de wénhuà.", "vi": "Đi lại nhiều nơi có thể ( ? ) hơn về văn hóa địa phương.", "ans": "D", "word": "了解", "explain": "Hiểu rõ, am hiểu: 了解 (liǎojiě)."},
                {"num": 29, "prefix": "他会说英语、法语和", "suffix": "。", "py": "Tā huì shuō Yīngyǔ, Fǎyǔ hé ( ? ).", "vi": "Anh ấy biết nói tiếng Anh, tiếng Pháp và ( ? ).", "ans": "A", "word": "中文", "explain": "Tiếng Trung: 中文 (zhōngwén)."},
                {"num": 30, "prefix": "下个星期天你想", "suffix": "学校的晚会吗？", "py": "Xià ge xīngqītiān nǐ xiǎng ( ? ) xuéxiào de wǎnhuì ma?", "vi": "Chủ nhật tuần sau cậu có muốn ( ? ) dạ hội của trường không?", "ans": "E", "word": "参加", "explain": "Tham gia: 参加 (cānjiā)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "大山是一个美国留学生，他在北京语言大学学习中文。大山学汉语非常努力，每天早上听录音，晚上跟中国室友聊天儿。现在，他的中文说得跟中国人一样好。很多新认识的朋友第一次听他说话，都以为他是中国人。下个月大山打算参加HSK四级考试，老师和同学们都对他说：“你准备得这么充分，放一百个心吧，你一定能考最高分！”",
            "passage_py": "Dàshān shì yí ge Měiguó liúxuéshēng, tā zài Běijīng Yǔyán Dàxué xuéxí zhōngwén. Dàshān xué hànyǔ fēicháng nǔlì, měitiān zǎoshang tīng lùyīn, wǎnshang gēn zhōngguó shìyǒu liáotiānr. Xiànzài, tā de zhōngwén shuō de gēn zhōngguó rén yíyàng hǎo. Hěn duō xīn rènshi de péngyou dì-yī cì tīng tā shuōhuà, dōu yǐwéi tā shì zhōngguó rén. Xià ge yuè Dàshān dǎsuàn cānjiā HSK sì jí kǎoshì, lǎoshī hé tóngxuémen dōu duì tā shuō: 'Nǐ zhǔnbèi de zhème chōngfèn, fàng yí bǎi ge xīn ba, nǐ yídìng néng kǎo zuì gāo fēn!'",
            "passage_vi": "Đại Sơn là một du học sinh người Mỹ, cậu học tiếng Trung tại Đại học Ngôn ngữ Bắc Kinh. Đại Sơn học tiếng Hán vô cùng chăm chỉ, mỗi sáng nghe băng ghi âm, buổi tối trò chuyện cùng bạn cùng phòng người Trung Quốc. Hiện nay, tiếng Trung của cậu ấy nói giỏi như người Trung Quốc bản xứ. Rất nhiều bạn bè mới quen lần đầu nghe cậu nói chuyện đều tưởng cậu là người Trung Quốc. Tháng sau Đại Sơn dự định tham gia kỳ thi HSK 4, thầy cô và bạn bè đều nói với cậu: 'Em chuẩn bị chu đáo thế này, cứ yên tâm tuyệt đối đi, em nhất định sẽ giành điểm số cao nhất!'",
            "questions": [
                {
                    "num": 31,
                    "text": "大山是哪国人？",
                    "options": ["A. 中国人", "B. 美国人", "C. 英国人"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 大山是一个美国留学生."
                },
                {
                    "num": 32,
                    "text": "大山平时是怎么学习汉语的？",
                    "options": ["A. 只在网上看视频", "B. 早上听录音，晚上跟室友聊天", "C. 天天抄汉字"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 每天早上听录音，晚上跟中国室友聊天儿."
                },
                {
                    "num": 33,
                    "text": "大山的中文水平怎么样？",
                    "options": ["A. 说得跟中国人一样好", "B. 听得懂但不会说", "C. 水平不太高"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 他的中文说得跟中国人一样好."
                },
                {
                    "num": 34,
                    "text": "大山下个月打算参加什么考试？",
                    "options": ["A. HSK三级", "B. HSK四级", "C. 英语六级"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 参加HSK四级考试."
                },
                {
                    "num": 35,
                    "text": "老师和同学对大山说什么？",
                    "options": ["A. 让他别去考试", "B. 让他多买几本书", "C. 让他放心，一定能考最高分"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 放一百个心吧，你一定能考最高分."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["说得跟中国人", "她的汉语", "一样好"],
                "ans": "她的汉语说得跟中国人一样好。",
                "py": "Tā de hànyǔ shuō de gēn zhōngguó rén yíyàng hǎo.",
                "vi": "Tiếng Trung của cô ấy nói giỏi như người Trung Quốc vậy."
            },
            {
                "num": 37,
                "chunks": ["一定能", "放心吧", "考好的", "你"],
                "ans": "放心吧，你一定能考好的。",
                "py": "Fàngxīn ba, nǐ yídìng néng kǎohǎo de.",
                "vi": "Yên tâm đi, bạn nhất định sẽ thi tốt mà."
            },
            {
                "num": 38,
                "chunks": ["越走越累", "小丽", "爬山时"],
                "ans": "爬山时小丽越走越累。",
                "py": "Páshān shí Xiǎolì yuè zǒu yuè lèi.",
                "vi": "Lúc leo núi Tiểu Lệ càng đi càng mệt."
            },
            {
                "num": 39,
                "chunks": ["参加了", "中国文化活动", "我们班同学"],
                "ans": "我们班同学参加了中国文化活动。",
                "py": "Wǒmen bān tóngxué cānjiā le Zhōngguó wénhuà huódòng.",
                "vi": "Học sinh lớp chúng tôi đã tham gia hoạt động văn hóa Trung Quốc."
            },
            {
                "num": 40,
                "chunks": ["了解中国文化", "多跟朋友聊天", "可以更"],
                "ans": "多跟朋友聊天可以更了解中国文化。",
                "py": "Duō gēn péngyou liáotiān kěyǐ gèng liǎojiě Zhōngguó wénhuà.",
                "vi": "Trò chuyện nhiều với bạn bè có thể hiểu hơn về văn hóa Trung Quốc."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我妹妹也上这个 (bān)。",
                "pinyin": "bān",
                "ans": "班",
                "vi": "Em gái tôi cũng học lớp này."
            },
            {
                "num": 42,
                "sentence": "这本书跟我买的那本 (yíyàng)。",
                "pinyin": "yíyàng",
                "ans": "一样",
                "vi": "Quyển sách này giống hệt quyển tôi mua."
            },
            {
                "num": 43,
                "sentence": "请你 (fàngxīn)，我一定按时完成。",
                "pinyin": "fàngxīn",
                "ans": "放心",
                "vi": "Xin bạn hãy yên tâm, tôi nhất định hoàn thành đúng hạn."
            },
            {
                "num": 44,
                "sentence": "大家都去 (cānjiā) 晚会了。",
                "pinyin": "cānjiā",
                "ans": "参加",
                "vi": "Mọi người đều đi tham gia dạ hội rồi."
            },
            {
                "num": 45,
                "sentence": "我对他的情况很 (liǎojiě)。",
                "pinyin": "liǎojiě",
                "ans": "了解",
                "vi": "Tôi rất hiểu rõ tình hình của anh ấy."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "中文", "py": "zhōngwén", "pos": "danh từ", "vi": "tiếng Trung, văn tự tiếng Hán", "eg": "我的中文名字叫大山。"},
            {"num": 2, "zh": "班", "py": "bān", "pos": "danh từ", "vi": "lớp học, ca làm việc", "eg": "我们班一共有二十个学生。"},
            {"num": 3, "zh": "一样", "py": "yíyàng", "pos": "tính từ", "vi": "như nhau, giống nhau", "eg": "这两种颜色是一样的。"},
            {"num": 4, "zh": "最后", "py": "zuìhòu", "pos": "danh từ chỉ thời gian", "vi": "cuối cùng", "eg": "经过努力，他最后成功了。"},
            {"num": 5, "zh": "放心", "py": "fàngxīn", "pos": "động từ", "vi": "yên tâm, an tâm", "eg": "这件事交给我，你放心吧。"},
            {"num": 6, "zh": "一定", "py": "yídìng", "pos": "phó từ/tính từ", "vi": "nhất định, chắc chắn", "eg": "明天我一定去接你。"},
            {"num": 7, "zh": "担心", "py": "dānxīn", "pos": "động từ", "vi": "lo lắng, lo âu", "eg": "别为我担心，我很好。"},
            {"num": 8, "zh": "比较", "py": "bǐjiào", "pos": "phó từ/động từ", "vi": "khá là, so sánh", "eg": "今天天气比较冷。"},
            {"num": 9, "zh": "了解", "py": "liǎojiě", "pos": "động từ", "vi": "hiểu rõ, tìm hiểu", "eg": "我很了解这个地方。"},
            {"num": 10, "zh": "先", "py": "xiān", "pos": "phó từ", "vi": "trước tiên", "eg": "你先去，我一会儿就来。"},
            {"num": 11, "zh": "中间", "py": "zhōngjiān", "pos": "danh từ chỉ nơi chốn", "vi": "ở giữa, trung gian", "eg": "站在中间的那个人是谁？"},
            {"num": 12, "zh": "参加", "py": "cānjiā", "pos": "động từ", "vi": "tham gia, tham dự", "eg": "你想参加这次比赛吗？"},
            {"num": 13, "zh": "影响", "py": "yǐngxiǎng", "pos": "động từ/danh từ", "vi": "ảnh hưởng, tác động", "eg": "别看电视了，会影响学习的。"}
        ],
        "proper_nouns": [
            {"zh": "大山", "py": "Dàshān", "vi": "Đại Sơn (tên người nước ngoài)"}
        ],
        "grammar": [
            {
                "title": "1. So sánh ngang bằng: A 跟 / 和 B 一样 (+ Tính từ)",
                "desc": "Dùng để biểu thị hai sự vật, hiện tượng có đặc điểm, tính chất giống nhau. Phủ định dùng 'A 跟/和 B 不一样 (+ Tính từ)'.",
                "examples": [
                    {"zh": "她的汉语说得跟中国人一样好。", "py": "Tā de hànyǔ shuō de gēn zhōngguó rén yíyàng hǎo.", "vi": "Tiếng Hán của cô ấy nói giỏi như người Trung Quốc."},
                    {"zh": "这本书跟那本书一样厚。", "py": "Zhè běn shū gēn nà běn shū yíyàng hòu.", "vi": "Cuốn sách này dày bằng cuốn sách kia."},
                    {"zh": "我和弟弟的想法不一样。", "py": "Wǒ hé dìdi de xiǎngfǎ bù yíyàng.", "vi": "Suy nghĩ của tôi và em trai không giống nhau."}
                ]
            },
            {
                "title": "2. Bổ ngữ trạng thái với “得” (状态补语)",
                "desc": "Cấu trúc: 'Động từ + 得 + Cụm tính từ / Cụm vị ngữ' nhằm miêu tả hoặc đánh giá kết quả, trình độ đạt được của động tác.",
                "examples": [
                    {"zh": "他说得很好。", "py": "Tā shuō de hěn hǎo.", "vi": "Anh ấy nói rất tốt."},
                    {"zh": "她跑得非常快。", "py": "Tā pǎo de fēicháng kuài.", "vi": "Cô ấy chạy cực kỳ nhanh."}
                ]
            }
        ]
    },

    # ==================== BÀI 10 ====================
    {
        "id": 10,
        "title_zh": "数学比历史难多了。",
        "title_py": "Shùxué bǐ lìshǐ nán duō le.",
        "title_vi": "Môn Toán khó hơn môn Lịch Sử nhiều.",
        "dialogues": [
            {
                "title": "Đoạn 1: 聊学校功课 (Nói về các môn học ở trường)",
                "location": "在自习室",
                "lines": [
                    {"speaker": "大山", "role": "male", "zh": "你在做什么作业呢？这么认真。", "py": "Nǐ zài zuò shénme zuòyè ne? Zhème rènzhēn.", "vi": "Cậu đang làm bài tập môn gì thế? Chăm chú quá."},
                    {"speaker": "小明", "role": "male", "zh": "我在写数学作业，这几道题太难了！", "py": "Wǒ zài xiě shùxué zuòyè, zhè jǐ dào tí tài nán le!", "vi": "Tớ đang làm bài tập toán, mấy bài này khó quá trời!"},
                    {"speaker": "大山", "role": "male", "zh": "我也觉得数学比历史难多了。", "py": "Wǒ yě juéde shùxué bǐ lìshǐ nán duō le.", "vi": "Tớ cũng thấy môn toán khó hơn môn lịch sử nhiều."},
                    {"speaker": "小明", "role": "male", "zh": "历史只要多看书就能记住，数学要想半天。", "py": "Lìshǐ zhǐyào duō kànshū jiù néng jìzhù, shùxué yào xiǎng bàntiān.", "vi": "Lịch sử chỉ cần đọc nhiều sách là nhớ được, còn toán thì phải nghĩ cả buổi."}
                ]
            },
            {
                "title": "Đoạn 2: 骑自行车去公园 (Đi xe đạp ra công viên)",
                "location": "在楼下",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "小丽，你看我的新自行车怎么样？", "py": "Xiǎolì, nǐ kàn wǒ de xīn zìxíngchē zěnmeyàng?", "vi": "Tiểu Lệ, em xem chiếc xe đạp mới của anh thế nào?"},
                    {"speaker": "小丽", "role": "female", "zh": "挺漂亮的，比你原来那辆轻多了吧？", "py": "Tǐng piàoliang de, bǐ nǐ yuánlái nà liàng qīng duō le ba?", "vi": "Đẹp lắm, nhẹ hơn chiếc cũ của anh nhiều đúng không?"},
                    {"speaker": "小刚", "role": "male", "zh": "对，骑起来非常轻松，而且很便宜，才五百块。", "py": "Duì, qí qǐlái fēicháng qīngsōng, érqiě hěn piányi, cái wǔbǎi kuài.", "vi": "Đúng rồi, đạp rất nhẹ nhàng, hơn nữa lại rẻ, chỉ có 500 tệ thôi."},
                    {"speaker": "小丽", "role": "female", "zh": "走，我们骑车去奥林匹克公园转转！", "py": "Zǒu, wǒmen qí chē qù Àolínpǐkè Gōngyuán zhuànzhuan!", "vi": "Đi thôi, chúng mình đạp xe ra công viên Olympic dạo quanh một vòng nhé!"}
                ]
            },
            {
                "title": "Đoạn 3: 买乐器 (Mua nhạc cụ)",
                "location": "在琴行",
                "lines": [
                    {"speaker": "顾客", "role": "male", "zh": "老板，这两把吉他有什么不一样？", "py": "Lǎobǎn, zhè liǎng bǎ jítā yǒu shénme bù yíyàng?", "vi": "Chủ quán ơi, hai cây đàn guitar này có gì khác nhau?"},
                    {"speaker": "老板", "role": "female", "zh": "这把黑色的声音更好听，但是比那把原木色的贵一点儿。", "py": "Zhè bǎ hēisè de shēngyīn gèng hǎotīng, dànshì bǐ nà bǎ yuánmùsè de guì yìdiǎnr.", "vi": "Cây màu đen này âm thanh hay hơn, nhưng đắt hơn cây màu gỗ mộc một chút."},
                    {"speaker": "顾客", "role": "male", "zh": "贵多少钱？", "py": "Guì duōshǎo qián?", "vi": "Đắt hơn bao nhiêu tiền ạ?"},
                    {"speaker": "老板", "role": "female", "zh": "贵两百块钱。不过一把好琴可以用好多年呢。", "py": "Guì liǎng bǎi kuài qián. Búguò yì bǎ hǎo qín kěyǐ yòng hǎo duō nián ne.", "vi": "Đắt hơn 200 tệ. Nhưng một cây đàn tốt có thể dùng được nhiều năm lắm đấy."}
                ]
            },
            {
                "title": "Đoạn 4: 选租房子 (Chọn thuê nhà)",
                "location": "在房产中介",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "学校南边的房子比北边的贵一些。", "py": "Xuéxiào nánbiān de fángzi bǐ běibiān de guì yìxiē.", "vi": "Nhà ở phía nam trường đắt hơn phía bắc một chút."},
                    {"speaker": "小丽", "role": "female", "zh": "但是南边离地铁站近，交通比北边方便多了。", "py": "Dànshì nánbiān lí dìtiězhàn jìn, jiāotōng bǐ běibiān fāngbiàn duō le.", "vi": "Nhưng phía nam gần ga tàu điện, giao thông thuận tiện hơn phía bắc nhiều."},
                    {"speaker": "小刚", "role": "male", "zh": "那我们还是租南边的吧，每天上班能多睡半个小时。", "py": "Nà wǒmen háishì zū nánbiān de ba, měitiān shàngbān néng duō shuì bàn ge xiǎoshí.", "vi": "Thế chúng mình thuê phía nam đi, mỗi ngày đi làm có thể ngủ thêm được nửa tiếng."},
                    {"speaker": "小丽", "role": "female", "zh": "好，虽然贵了一点儿，但是住着方便！", "py": "Hǎo, suīrán guì le yìdiǎnr, dànshì zhùzhe fāngbiàn!", "vi": "Được, tuy đắt hơn một chút nhưng ở lại thuận tiện!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你觉得数学难还是历史难？ 男：我觉得数学比历史难多了。",
                "question": "男的觉得哪门课更难？",
                "options": ["A. 历史", "B. 数学", "C. 体育"],
                "ans": "B",
                "explain": "Người nam trả lời: 数学比历史难多了."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小刚的新自行车很重，骑起来非常累。",
                "question": "Phán đoán đúng hay sai: 小刚的新自行车比原来轻多了。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Đoạn thoại trong bài nói rõ xe mới nhẹ hơn chiếc cũ nhiều (比你原来那辆轻多了)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：黑色的吉他多少钱？ 女：原木色的八百块，黑色的比它贵两百块。",
                "question": "黑色的吉他多少钱？",
                "options": ["A. 八百块", "B. 一千块", "C. 六百块"],
                "ans": "B",
                "explain": "800 + 200 = 1000 tệ (一千块)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：学校南边的房子怎么样？ 男：虽然贵一点儿，但交通比北边方便多了。",
                "question": "男的为什么想租南边的房子？",
                "options": ["A. 价格便宜", "B. 交通方便", "C. 房间更大"],
                "ans": "B",
                "explain": "Người nam nhấn mạnh: 交通比北边方便多了."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "数学比历史难多了，我做了半天都没做完。", "py": "Shùxué bǐ lìshǐ nán duō le, wǒ zuò le bàntiān dōu méi zuòwán.", "vi": "Môn toán khó hơn môn lịch sử nhiều, tôi làm cả buổi vẫn chưa xong."},
                {"id": "B", "text": "我新买的自行车比原来的轻多了。", "py": "Wǒ xīn mǎi de zìxíngchē bǐ yuánlái de qīng duō le.", "vi": "Chiếc xe đạp mới mua của tôi nhẹ hơn chiếc cũ nhiều."},
                {"id": "C", "text": "学校南边的房子虽然贵，但比北边方便得多。", "py": "Xuéxiào nánbiān de fángzi suīrán guì, dàn bǐ běibiān fāngbiàn de duō.", "vi": "Nhà phía nam trường tuy đắt nhưng tiện hơn phía bắc nhiều."},
                {"id": "D", "text": "这把吉他音质好，便宜又好用。", "py": "Zhè bǎ jítā yīnzhì hǎo, piányi yòu hǎoyòng.", "vi": "Cây đàn guitar này chất âm tốt, rẻ lại dễ dùng."},
                {"id": "E", "text": "天天坚持体育锻炼，身体比以前好多了。", "py": "Tiāntiān jiānchí tǐyù duànliàn, shēntǐ bǐ yǐqián hǎo duō le.", "vi": "Ngày nào cũng kiên trì rèn luyện thể dục, cơ thể khỏe hơn trước nhiều."}
            ],
            "questions": [
                {"num": 21, "text": "你在抓耳挠腮想什么呢？", "py": "Nǐ zài zhuā'ěr-náosāi xiǎng shénme ne?", "vi": "Cậu đang vò đầu bứt tai nghĩ gì thế?", "ans": "A", "explain": "Đang suy nghĩ làm bài tập toán khó."},
                {"num": 22, "text": "今天骑车上班感觉怎么样？", "py": "Jīntiān qí chē shàngbān gǎnjué zěnmeyàng?", "vi": "Hôm nay đạp xe đi làm cảm giác thế nào?", "ans": "B", "explain": "Khen xe đạp mới nhẹ hơn nhiều."},
                {"num": 23, "text": "你们决定租哪边的房子了吗？", "py": "Nǐmen juédìng zū nǎ biān de fángzi le ma?", "vi": "Các bạn đã quyết định thuê nhà phía nào chưa?", "ans": "C", "explain": "Quyết định thuê phía nam trường vì tiện lợi hơn."},
                {"num": 24, "text": "你想买哪一把琴？", "py": "Nǐ xiǎng mǎi nǎ yì bǎ qín?", "vi": "Bạn muốn mua cây đàn nào?", "ans": "D", "explain": "Chọn cây đàn guitar vừa rẻ vừa hay."},
                {"num": 25, "text": "看你最近气色真不错，有什么秘诀？", "py": "Kàn nǐ zuìjìn qìsè zhēn búcuò, yǒu shénme mìjué?", "vi": "Trông sắc mặt cậu dạo này tốt thật đấy, có bí quyết gì?", "ans": "E", "explain": "Nhờ kiên trì rèn luyện thể dục mỗi ngày."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "历史", "py": "lìshǐ", "vi": "lịch sử"},
                {"id": "B", "zh": "数学", "py": "shùxué", "vi": "môn toán"},
                {"id": "C", "zh": "自行车", "py": "zìxíngchē", "vi": "xe đạp"},
                {"id": "D", "zh": "便宜", "py": "piányi", "vi": "rẻ"},
                {"id": "E", "zh": "方便", "py": "fāngbiàn", "vi": "thuận tiện, tiện lợi"}
            ],
            "questions": [
                {"num": 26, "prefix": "我对中国古代", "suffix": "非常感兴趣。", "py": "Wǒ duì Zhōngguó gǔdài ( ? ) fēicháng gǎnxìngqù.", "vi": "Tôi rất có hứng thú với ( ? ) cổ đại Trung Quốc.", "ans": "A", "word": "历史", "explain": "Lịch sử cổ đại (古代历史)."},
                {"num": 27, "prefix": "弟弟的", "suffix": "成绩一直在班里排前三名。", "py": "Dìdi de ( ? ) chéngjì yìzhí zài bān li pái qián sān míng.", "vi": "Thành tích môn ( ? ) của em trai luôn xếp top 3 trong lớp.", "ans": "B", "word": "数学", "explain": "Môn toán (数学)."},
                {"num": 28, "prefix": "骑", "suffix": "去上班既环保又健康。", "py": "Qí ( ? ) qù shàngbān jì huánbǎo yòu jiànkāng.", "vi": "Đạp ( ? ) đi làm vừa bảo vệ môi trường lại vừa khỏe mạnh.", "ans": "C", "word": "自行车", "explain": "Đi xe đạp (骑自行车)."},
                {"num": 29, "prefix": "超市今天打折，所有衣服都非常", "suffix": "。", "py": "Chāoshì jīntiān dǎzhé, suǒyǒu yīfu dōu fēicháng ( ? ).", "vi": "Siêu thị hôm nay giảm giá, mọi quần áo đều rất ( ? ).", "ans": "D", "word": "便宜", "explain": "Giá rẻ (便宜)."},
                {"num": 30, "prefix": "住在地铁站附近出行真", "suffix": "。", "py": "Zhù zài dìtiězhàn fùjìn chūxíng zhēn ( ? ).", "vi": "Sống gần ga tàu điện ngầm việc đi lại thật là ( ? ).", "ans": "E", "word": "方便", "explain": "Thuận tiện (方便)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "在中国大学里，学生们每天要上很多门课。有些同学喜欢文科，比如历史和中文；有些同学喜欢理科，比如数学和物理。大山觉得数学比历史难多了，因为学历史只要多读几遍书就能记住，但是数学不仅要记公式，还要做很多复杂的练习题。为了提高数学成绩，大山每天晚上都去图书馆自习两三个小时，现在他的数学成绩比以前好多了。",
            "passage_py": "Zài Zhōngguó dàxué li, xuéshengmen měitiān yào shàng hěn duō mén kè. Yǒuxiē tóngxué xǐhuan wénkē, bǐrú lìshǐ hé zhōngwén; yǒuxiē tóngxué xǐhuan lǐkē, bǐrú shùxué hé wùlǐ. Dàshān juéde shùxué bǐ lìshǐ nán duō le, yīnwèi xué lìshǐ zhǐyào duō dú jǐ biàn shū jiù néng jìzhù, dànshì shùxué bùjǐn yào jì gōngshì, hái yào zuò hěn duō fùzá de liànxítí. Wèile tígāo shùxué chéngjì, Dàshān měitiān wǎnshang dōu qù túshūguǎn zìxí liǎng-sān ge xiǎoshí, xiànzài tā de shùxué chéngjì bǐ yǐqián hǎo duō le.",
            "passage_vi": "Ở các trường đại học Trung Quốc, sinh viên mỗi ngày phải học rất nhiều môn. Có bạn thích các môn xã hội như lịch sử và tiếng Trung; có bạn thích các môn tự nhiên như toán học và vật lý. Đại Sơn thấy môn toán khó hơn môn lịch sử nhiều, bởi vì học lịch sử chỉ cần đọc vài lần sách là có thể nhớ được, nhưng toán học không những phải nhớ công thức mà còn phải làm rất nhiều bài tập phức tạp. Để nâng cao điểm môn toán, mỗi tối Đại Sơn đều lên thư viện tự học hai ba tiếng đồng hồ, hiện nay điểm số môn toán của cậu ấy đã tốt hơn trước rất nhiều.",
            "questions": [
                {
                    "num": 31,
                    "text": "大山觉得哪个科目比历史难？",
                    "options": ["A. 中文", "B. 体育", "C. 数学"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 大山觉得数学比历史难多了."
                },
                {
                    "num": 32,
                    "text": "为什么大山觉得历史相对容易？",
                    "options": ["A. 没有作业", "B. 多读几遍就能记住", "C. 老师讲得少"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 因为学历史只要多读几遍书就能记住."
                },
                {
                    "num": 33,
                    "text": "大山每天晚上去哪儿自习？",
                    "options": ["A. 宿舍", "B. 图书馆", "C. 教室"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 每天晚上都去图书馆自习."
                },
                {
                    "num": 34,
                    "text": "大山每天晚上自习多长时间？",
                    "options": ["A. 半个小时", "B. 一个小时", "C. 两三个小时"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 自习两三个小时."
                },
                {
                    "num": 35,
                    "text": "现在大山的数学成绩怎么样？",
                    "options": ["A. 考了零分", "B. 比以前好多了", "C. 和以前一样"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 现在他的数学成绩比以前好多了."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["难多了", "比历史", "数学"],
                "ans": "数学比历史难多了。",
                "py": "Shùxué bǐ lìshǐ nán duō le.",
                "vi": "Môn toán khó hơn môn lịch sử nhiều."
            },
            {
                "num": 37,
                "chunks": ["比原来那辆", "新自行车", "轻多了"],
                "ans": "新自行车比原来那辆轻多了。",
                "py": "Xīn zìxíngchē bǐ yuánlái nà liàng qīng duō le.",
                "vi": "Xe đạp mới nhẹ hơn chiếc cũ nhiều."
            },
            {
                "num": 38,
                "chunks": ["贵两百块钱", "这把黑吉他", "比那把"],
                "ans": "这把黑吉他比那把贵两百块钱。",
                "py": "Zhè bǎ hēi jítā bǐ nà bǎ guì liǎng bǎi kuài qián.",
                "vi": "Cây guitar đen này đắt hơn cây kia 200 tệ."
            },
            {
                "num": 39,
                "chunks": ["方便得多", "南边的交通", "比北边"],
                "ans": "南边的交通比北边方便得多。",
                "py": "Nánbiān de jiāotōng bǐ běibiān fāngbiàn de duō.",
                "vi": "Giao thông ở phía nam thuận tiện hơn phía bắc nhiều."
            },
            {
                "num": 40,
                "chunks": ["在图书馆自习", "每天晚上", "两三个小时", "他"],
                "ans": "他每天晚上在图书馆自习两三个小时。",
                "py": "Tā měitiān wǎnshang zài túshūguǎn zìxí liǎng-sān ge xiǎoshí.",
                "vi": "Mỗi tối anh ấy tự học ở thư viện khoảng hai ba tiếng."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我最喜欢的科目是 (lìshǐ)。",
                "pinyin": "lìshǐ",
                "ans": "历史",
                "vi": "Môn học tôi yêu thích nhất là lịch sử."
            },
            {
                "num": 42,
                "sentence": "今天的 (shùxué) 课很有意思。",
                "pinyin": "shùxué",
                "ans": "数学",
                "vi": "Tiết toán hôm nay rất thú vị."
            },
            {
                "num": 43,
                "sentence": "我买了一辆新 (zìxíngchē)。",
                "pinyin": "zìxíngchē",
                "ans": "自行车",
                "vi": "Tôi đã mua một chiếc xe đạp mới."
            },
            {
                "num": 44,
                "sentence": "这家商店的衣服很 (piányi)。",
                "pinyin": "piányi",
                "ans": "便宜",
                "vi": "Quần áo của cửa hàng này rất rẻ."
            },
            {
                "num": 45,
                "sentence": "住在市中心交通非常 (fāngbiàn)。",
                "pinyin": "fāngbiàn",
                "ans": "方便",
                "vi": "Sống ở trung tâm thành phố giao thông vô cùng thuận tiện."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "历史", "py": "lìshǐ", "pos": "danh từ", "vi": "lịch sử", "eg": "中国有悠久的历史。"},
            {"num": 2, "zh": "数学", "py": "shùxué", "pos": "danh từ", "vi": "toán học, môn toán", "eg": "数学课上老师讲得很精彩。"},
            {"num": 3, "zh": "体育", "py": "tǐyù", "pos": "danh từ", "vi": "thể dục, thể thao", "eg": "下午有一节体育课。"},
            {"num": 4, "zh": "一点儿", "py": "yìdiǎnr", "pos": "cụm số lượng", "vi": "một chút, một ít", "eg": "这件衣服比那件贵一点儿。"},
            {"num": 5, "zh": "得多", "py": "de duō", "pos": "bổ ngữ", "vi": "nhiều, hơn nhiều", "eg": "西瓜比苹果大得多。"},
            {"num": 6, "zh": "骑", "py": "qí", "pos": "động từ", "vi": "cưỡi, đạp (xe)", "eg": "骑马, 骑自行车。"},
            {"num": 7, "zh": "自行车", "py": "zìxíngchē", "pos": "danh từ", "vi": "xe đạp", "eg": "我每天骑自行车去上学。"},
            {"num": 8, "zh": "吉他", "py": "jítā", "pos": "danh từ", "vi": "đàn ghi-ta", "eg": "他弹吉他弹得非常好。"},
            {"num": 9, "zh": "便宜", "py": "piányi", "pos": "tính từ", "vi": "rẻ, giá thấp", "eg": "这双鞋子很便宜。"},
            {"num": 10, "zh": "容易", "py": "róngyì", "pos": "tính từ", "vi": "dễ dàng", "eg": "写汉字不太容易。"},
            {"num": 11, "zh": "方便", "py": "fāngbiàn", "pos": "tính từ", "vi": "thuận tiện, tiện lợi", "eg": "出门坐地铁非常方便。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu so sánh với “比” mang bổ ngữ mức độ: A 比 B + Tính từ + 一点儿 / 得多 / 多了",
                "desc": "Dùng để biểu thị mức độ chênh lệch giữa hai đối tượng. '一点儿' biểu thị chênh lệch ít; '得多' hoặc '多了' biểu thị chênh lệch rất lớn.",
                "examples": [
                    {"zh": "数学比历史难多了。", "py": "Shùxué bǐ lìshǐ nán duō le.", "vi": "Môn toán khó hơn môn lịch sử nhiều."},
                    {"zh": "这件衣服比那件便宜一点儿。", "py": "Zhè jiàn yīfu bǐ nà jiàn piányi yìdiǎnr.", "vi": "Chiếc áo này rẻ hơn chiếc kia một chút."},
                    {"zh": "今天比昨天冷得多。", "py": "Jīntiān bǐ zuótiān lěng de duō.", "vi": "Hôm nay lạnh hơn hôm qua nhiều."}
                ]
            },
            {
                "title": "2. Biểu thị số lượng ước lượng bằng hai chữ số liền kề",
                "desc": "Đặt hai con số liền nhau để biểu thị một khoảng số lượng ước chừng (ví dụ: 两三, 三四, 四五, 七八).",
                "examples": [
                    {"zh": "他在图书馆看书看了两三个小时。", "py": "Tā zài túshūguǎn kànshū kàn le liǎng-sān ge xiǎoshí.", "vi": "Anh ấy ở thư viện đọc sách khoảng hai ba tiếng đồng hồ."},
                    {"zh": "我们班有三四十个学生。", "py": "Wǒmen bān yǒu sān-sìshí ge xuésheng.", "vi": "Lớp chúng tôi có khoảng ba bốn chục học sinh."}
                ]
            }
        ]
    }
]
