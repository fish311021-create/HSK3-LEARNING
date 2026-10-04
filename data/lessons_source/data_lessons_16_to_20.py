# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn cho Bài 16 đến Bài 20 - HSK 3 Standard Course
"""

LESSONS_16_TO_20 = [
    # ==================== BÀI 16 ====================
    {
        "id": 16,
        "title_zh": "我现在累得下了班就想睡觉。",
        "title_py": "Wǒ xiànzài lèi de xià le bān jiù xiǎng shuìjiào.",
        "title_vi": "Bây giờ tôi mệt đến nỗi chỉ muốn ngủ sau giờ làm.",
        "dialogues": [
            {
                "title": "Đoạn 1: 下班回家 (Tan làm về nhà)",
                "location": "在家",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "你怎么一进门就躺在沙发上了？", "py": "Nǐ zěnme yí jìn mén jiù tǎng zài shāfā shang le?", "vi": "Sao anh vừa bước vào cửa là đã nằm vật ra sofa thế kia?"},
                    {"speaker": "小刚", "role": "male", "zh": "今天在公司忙了一整天，我现在累得下了班就想睡觉。", "py": "Jīntiān zài gōngsī máng le yì zhěng tiān, wǒ xiànzài lèi de xià le bān jiù xiǎng shuìjiào.", "vi": "Hôm nay ở công ty bận rộn cả ngày, bây giờ anh mệt đến nỗi tan làm chỉ muốn ngủ ngay thôi."},
                    {"speaker": "小丽", "role": "female", "zh": "如果太累了，就先洗个热水澡，饭做好了我叫你。", "py": "Rúguǒ tài lèi le, jiù xiān xǐ ge rèshuǐzǎo, fàn zuòhǎo le wǒ jiào nǐ.", "vi": "Nếu mệt quá thì anh đi tắm nước nóng trước đi, cơm nấu xong em gọi."},
                    {"speaker": "小刚", "role": "male", "zh": "谢谢老婆，有你真好！", "py": "Xièxie lǎopo, yǒu nǐ zhēn hǎo!", "vi": "Cảm ơn bà xã, có em thật tuyệt vời!"}
                ]
            },
            {
                "title": "Đoạn 2: 去商场买皮鞋 (Đi siêu thị mua giày da)",
                "location": "在鞋帽店",
                "lines": [
                    {"speaker": "售货员", "role": "female", "zh": "先生，您看这双黑色的皮鞋怎么样？", "py": "Xiānsheng, nín kàn zhè shuāng hēisè de píxié zěnmeyàng?", "vi": "Thưa ngài, ngài xem đôi giày da màu đen này thế nào ạ?"},
                    {"speaker": "顾客", "role": "male", "zh": "皮质很软，穿起来很舒服。这顶帽子也很漂亮。", "py": "Pízhì hěn ruǎn, chuān qǐlái hěn shūfu. Zhè dǐng màozi yě hěn piàoliang.", "vi": "Chất da rất mềm, xỏ vào đi rất êm chân. Chiếc mũ này cũng rất đẹp nữa."},
                    {"speaker": "售货员", "role": "female", "zh": "这顶帽子跟您的皮鞋颜色很配，戴上去显得年轻极了。", "py": "Zhè dǐng màozi gēn nín de píxié yánsè hěn pèi, dài shàngqù xiǎnde niánqīng jí le.", "vi": "Chiếc mũ này màu rất hợp với đôi giày da của ngài, đội lên trông trẻ trung vô cùng."},
                    {"speaker": "顾客", "role": "male", "zh": "好，这两样我都买了！", "py": "Hǎo, zhè liǎng yàng wǒ dōu mǎi le!", "vi": "Được, cả hai món này tôi đều lấy!"}
                ]
            },
            {
                "title": "Đoạn 3: 聊小猫小狗 (Nói về thú cưng)",
                "location": "在朋友家",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "这只小白猫太可爱了，眼睛大大的，鼻子小小的！", "py": "Zhè zhī xiǎo bái māo tài kě'ài le, yǎnjing dàdà de, bízi xiǎoxiǎo de!", "vi": "Chú mèo trắng nhỏ này đáng yêu quá, đôi mắt tròn xoe, chiếc mũi nho nhỏ!"},
                    {"speaker": "朋友", "role": "female", "zh": "它才三个月大，毛长长的，特别喜欢跟人玩儿。", "py": "Tā cái sān ge yuè dà, máo chángcháng de, tèbié xǐhuan gēn rén wánr.", "vi": "Nó mới được 3 tháng tuổi thôi, lông dài mượt, rất thích quấn người chơi đùa."},
                    {"speaker": "小丽", "role": "female", "zh": "看它走路摇摇晃晃的样子，真让人喜欢。", "py": "Kàn tā zǒulù yáoyáo-huànghuàng de yàngzi, zhēn ràng rén xǐhuan.", "vi": "Nhìn dáng nó đi lững chững lắc lư, thật làm người ta yêu mến."},
                    {"speaker": "朋友", "role": "female", "zh": "如果你喜欢，下个月它生了小猫，我送你一只！", "py": "Rúguǒ nǐ xǐhuan, xià ge yuè tā shēng le xiǎomāo, wǒ sòng nǐ yì zhī!", "vi": "Nếu cậu thích, tháng sau nó sinh mèo con, tớ tặng cậu một bé nhé!"}
                ]
            },
            {
                "title": "Đoạn 4: 检查身体与生活 (Kiểm tra sức khỏe và lối sống)",
                "location": "在体检中心",
                "lines": [
                    {"speaker": "医生", "role": "male", "zh": "你的身高一米七五，体重七十公斤，身体指标很正常。", "py": "Nǐ de shēngāo yì mǐ qīshíwǔ, tǐzhòng qīshí gōngjīn, shēntǐ zhǐbiāo hěn zhèngcháng.", "vi": "Chiều cao của anh 1m75, cân nặng 70kg, các chỉ số cơ thể rất bình thường."},
                    {"speaker": "患者", "role": "female", "zh": "但我最近总觉得特别累，早晨起床头有点儿晕。", "py": "Dàn wǒ zuìjìn zǒng juéde tèbié lèi, zǎochén qǐchuáng tóu yǒudiǎnr yūn.", "vi": "Nhưng dạo này tôi luôn cảm thấy đặc biệt mệt mỏi, sáng thức dậy đầu hơi choáng."},
                    {"speaker": "医生", "role": "male", "zh": "我认为这跟你的工作压力有很大关系，平时要早点儿睡觉，少喝咖啡。", "py": "Wǒ rènwéi zhè gēn nǐ de gōngzuò yālì yǒu hěn dà guānxì, píngshí yào zǎo diǎnr shuìjiào, shǎo hē kāfēi.", "vi": "Tôi cho rằng điều này có liên quan mật thiết đến áp lực công việc của anh, thường ngày phải đi ngủ sớm hơn, bớt uống cà phê lại."},
                    {"speaker": "患者", "role": "female", "zh": "谢谢医生，我一定注意调整作息！", "py": "Xièxie yīshēng, wǒ yídìng zhùyì tiáozhěng zuòxī!", "vi": "Cảm ơn bác sĩ, tôi nhất định sẽ chú ý điều chỉnh giờ giấc sinh hoạt ạ!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你今天怎么这么没精神？ 男：我今天忙了一天，累得下了班就想睡觉。",
                "question": "男的现在感觉怎么样？",
                "options": ["A. 特别高兴", "B. 累得想睡觉", "C. 肚子很饿"],
                "ans": "B",
                "explain": "Người nam nói rõ: 累得下了班就想睡觉."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "那顶新买的帽子跟先生的黑色皮鞋颜色很配，戴上去很显年轻。",
                "question": "Phán đoán đúng hay sai: 帽子跟皮鞋的颜色一点儿也不配。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Đoạn thoại khẳng định hai màu rất hợp nhau (颜色很配)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：这只小猫长得真可爱。 女：是啊，如果你喜欢，我就送你一只。",
                "question": "女的打算做什么？",
                "options": ["A. 卖掉小猫", "B. 送给男的一只小猫", "C. 带小猫去医院"],
                "ans": "B",
                "explain": "Người nữ nói: 送你一只."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：医生，我的身体有什么大问题吗？ 男：指标都很正常，你的疲倦跟工作压力大有很大关系。",
                "question": "医生认为病人疲倦的原因是什么？",
                "options": ["A. 工作压力大", "B. 运动太多", "C. 感冒发烧"],
                "ans": "A",
                "explain": "Bác sĩ giải thích: 跟工作压力大有很大关系."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "我今天累得下了班就想睡觉，什么也不想做。", "py": "Wǒ jīntiān lèi de xià le bān jiù xiǎng shuìjiào, shénme yě bù xiǎng zuò.", "vi": "Hôm nay tôi mệt đến nỗi tan làm chỉ muốn ngủ, chẳng muốn làm gì cả."},
                {"id": "B", "text": "这双皮鞋的皮质很软，穿起来舒服极了。", "py": "Zhè shuāng píxié de pízhì hěn ruǎn, chuān qǐlái shūfu jí le.", "vi": "Đôi giày da này chất da rất mềm, đi vào dễ chịu vô cùng."},
                {"id": "C", "text": "这只小猫圆圆的脑袋，样子可爱极了。", "py": "Zhè zhī xiǎo māo yuányuán de nǎodai, yàngzi kě'ài jí le.", "vi": "Chú mèo con này cái đầu tròn xoe, dáng vẻ đáng yêu vô cùng."},
                {"id": "D", "text": "医生认为身体不舒服跟工作压力大有直接关系。", "py": "Yīshēng rènwéi shēntǐ bù shūfu gēn gōngzuò yālì dà yǒu zhíjiē guānxì.", "vi": "Bác sĩ cho rằng cơ thể không khỏe có liên quan trực tiếp đến áp lực công việc."},
                {"id": "E", "text": "如果明天下雨，我们的郊游就推迟到下周末。", "py": "Rúguǒ míngtiān xiàyǔ, wǒmen de jiāoyóu jiù tuīchí dào xià zhōumò.", "vi": "Nếu ngày mai trời mưa, chuyến dã ngoại của chúng ta sẽ hoãn lại sang cuối tuần sau."}
            ],
            "questions": [
                {"num": 21, "text": "下班后我们一起去唱歌吧？", "py": "Xiàbān hòu wǒmen yìqǐ qù chànggē ba?", "vi": "Tan làm chúng mình cùng đi hát karaoke nhé?", "ans": "A", "explain": "Từ chối vì quá mệt, chỉ muốn về nhà ngủ."},
                {"num": 22, "text": "你觉得这双鞋子质量怎么样？", "py": "Nǐ juéde zhè shuāng xiézi zhìliàng zěnmeyàng?", "vi": "Cậu thấy chất lượng đôi giày này thế nào?", "ans": "B", "explain": "Khen da mềm, đi rất thoải mái."},
                {"num": 23, "text": "快来看看我刚带回家的小动物！", "py": "Kuài lái kànkan wǒ gāng dài huí jiā de xiǎo dòngwù!", "vi": "Mau lại xem con vật nuôi nhỏ tớ vừa mang về nhà này!", "ans": "C", "explain": "Khen chú mèo con đầu tròn đáng yêu."},
                {"num": 24, "text": "体检报告出来了吗？医生怎么说？", "py": "Tǐjiǎn bàogào chūlái le ma? Yīshēng zěnme shuō?", "vi": "Phiếu khám sức khỏe có chưa? Bác sĩ nói sao?", "ans": "D", "explain": "Bác sĩ giải thích mệt mỏi do áp lực công việc."},
                {"num": 25, "text": "要是明天的天气不好，活动怎么办？", "py": "Yàoshi míngtiān de tiānqì bù hǎo, huódòng zěnme bàn?", "vi": "Nếu thời tiết ngày mai không thuận lợi thì hoạt động tính sao?", "ans": "E", "explain": "Nếu mưa sẽ hoãn dã ngoại (如果……就……)."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "如果", "py": "rúguǒ", "vi": "nếu, nếu như"},
                {"id": "B", "zh": "皮鞋", "py": "píxié", "vi": "giày da"},
                {"id": "C", "zh": "可爱", "py": "kě'ài", "vi": "đáng yêu"},
                {"id": "D", "zh": "关系", "py": "guānxì", "vi": "quan hệ, liên quan"},
                {"id": "E", "zh": "检查", "py": "jiǎnchá", "vi": "kiểm tra"}
            ],
            "questions": [
                {"num": 26, "prefix": "穿西装的时候最好配一双黑色的", "suffix": "。", "py": "Chuān xīzhuāng de shíhou zuì hǎo pèi yì shuāng hēisè de ( ? ).", "vi": "Khi mặc vest tốt nhất phối cùng một đôi ( ? ) màu đen.", "ans": "B", "word": "皮鞋", "explain": "Giày da: 皮鞋 (píxié)."},
                {"num": 27, "prefix": "这个小熊猫长得真是太", "suffix": "了。", "py": "Zhè ge xiǎo xióngmāo zhǎng de zhēn shì tài ( ? ) le.", "vi": "Chú gấu trúc nhỏ này trông thật là quá đỗi ( ? ).", "ans": "C", "word": "可爱", "explain": "Đáng yêu: 可爱 (kě'ài)."},
                {"num": 28, "prefix": "身体健康跟每天的生活作息有很大", "suffix": "。", "py": "Shēntǐ jiànkāng gēn měitiān de shēnghuó zuòxī yǒu hěn dà ( ? ).", "vi": "Sức khỏe cơ thể có ( ? ) rất lớn với nếp sinh hoạt hằng ngày.", "ans": "D", "word": "关系", "explain": "Quan hệ, liên quan: 关系 (guānxì)."},
                {"num": 29, "prefix": "交卷子前一定要认真", "suffix": "一遍。", "py": "Jiāo juànzi qián yídìng yào rènzhēn ( ? ) yí biàn.", "vi": "Trước khi nộp bài thi nhất định phải ( ? ) cẩn thận một lượt.", "ans": "E", "word": "检查", "explain": "Kiểm tra: 检查 (jiǎnchá)."},
                {"num": 30, "prefix": "明天下雨，我们", "suffix": "不去爬山了。", "py": "( ? ) míngtiān xiàyǔ, wǒmen jiù bú qù páshān le.", "vi": "( ? ) ngày mai trời mưa, chúng mình sẽ không đi leo núi nữa.", "ans": "A", "word": "如果", "explain": "Nếu như: 如果……就…… (rúguǒ)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "现代城市的生活节奏非常快，很多上班族每天都要面对巨大的工作压力。小王在一家外企工作，最近项目很紧，他每天早上七点出门，晚上九点多才到家。他经常对朋友说：“我现在累得下了班就想睡觉，连饭都懒得做。”医生提醒小王，虽然年轻，但是经常熬夜对身体危害很大。医生建议他：如果工作太忙，一定要学会合理安排时间，多吃新鲜蔬菜水果，每天坚持锻炼半小时，保持良好的人际关系，这样身心才能健康。",
            "passage_py": "Xiàndài chéngshì de shēnghuó jiézòu fēicháng kuài, hěn duō shàngbānzú měitiān dōu yào miànduì jùdà de gōngzuò yālì. Xiǎo Wáng zài yì jiā wàiqǐ gōngzuò, zuìjìn xiàngmù hěn jǐn, tā měitiān zǎoshang qī diǎn chūmén, wǎnshang jiǔ diǎn duō cái dào jiā. Tā jīngcháng duì péngyou shuō: 'Wǒ xiànzài lèi de xià le bān jiù xiǎng shuìjiào, lián fàn dōu lǎnde zuò.' Yīshēng tíxǐng Xiǎo Wáng, suīrán niánqīng, dànshì jīngcháng áoyè duì shēntǐ wēihài hěn dà. Yīshēng jiànyì tā: Rúguǒ gōngzuò tài máng, yídìng yào xuéhuì hélǐ ānpái shíjiān, duō chī xīnxiān shūcài shuǐguǒ, měitiān jiānchí duànliàn bàn xiǎoshí, bǎochí liánghǎo de rénjì guānxì, zhèyàng shēnxīn cái néng jiànkāng.",
            "passage_vi": "Nhịp sống ở các đô thị hiện đại vô cùng hối hả, rất nhiều người đi làm mỗi ngày đều phải đối mặt với áp lực công việc khổng lồ. Tiểu Vương làm việc tại một doanh nghiệp nước ngoài, dạo này dự án rất gấp, anh mỗi sáng 7 giờ ra khỏi cửa, tối hơn 9 giờ mới về đến nhà. Anh thường nói với bạn bè: 'Bây giờ tôi mệt đến nỗi tan làm chỉ muốn ngủ, đến cơm cũng lười chẳng buồn nấu.' Bác sĩ nhắc nhở Tiểu Vương rằng tuy còn trẻ nhưng thường xuyên thức khuya có tác hại rất lớn đối với sức khỏe. Bác sĩ khuyên anh: nếu công việc quá bận rộn, nhất định phải học cách sắp xếp thời gian hợp lý, ăn nhiều rau củ quả tươi, kiên trì tập thể dục nửa tiếng mỗi ngày, duy trì mối quan hệ tốt đẹp với mọi người xung quanh, như vậy cả thể chất lẫn tinh thần mới khỏe mạnh.",
            "questions": [
                {
                    "num": 31,
                    "text": "小王每天几点才能到家？",
                    "options": ["A. 下午五点", "B. 晚上七点", "C. 晚上九点多"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 晚上九点多才到家."
                },
                {
                    "num": 32,
                    "text": "小王下班后常常感觉怎么样？",
                    "options": ["A. 精神百倍", "B. 累得下了班就想睡觉", "C. 想去逛街买衣服"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 累得下了班就想睡觉."
                },
                {
                    "num": 33,
                    "text": "医生提醒小王注意什么问题？",
                    "options": ["A. 不要经常换工作", "B. 经常熬夜对身体危害很大", "C. 不要买太贵的皮鞋"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 经常熬夜对身体危害很大."
                },
                {
                    "num": 34,
                    "text": "医生建议小王每天坚持做什么？",
                    "options": ["A. 锻炼半小时", "B. 玩电脑游戏", "C. 喝两杯咖啡"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 每天坚持锻炼半小时."
                },
                {
                    "num": 35,
                    "text": "怎样才能让身心健康？",
                    "options": ["A. 每天多睡觉不运动", "B. 合理安排时间，多吃果蔬，坚持锻炼", "C. 只专注工作不管别人"],
                    "ans": "B",
                    "explain": "Đoạn văn tóm tắt lời khuyên của bác sĩ ở câu cuối."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["累得下了班", "我想睡觉", "现在就"],
                "ans": "我现在累得下了班就想睡觉。",
                "py": "Wǒ xiànzài lèi de xià le bān jiù xiǎng shuìjiào.",
                "vi": "Bây giờ tôi mệt đến mức tan làm chỉ muốn ngủ."
            },
            {
                "num": 37,
                "chunks": ["很舒服", "穿起来", "这双皮鞋"],
                "ans": "这双皮鞋穿起来很舒服。",
                "py": "Zhè shuāng píxié chuān qǐlái hěn shūfu.",
                "vi": "Đôi giày da này đi vào rất êm ái."
            },
            {
                "num": 38,
                "chunks": ["就早点儿休息", "如果太累了", "你"],
                "ans": "如果你太累了就早点儿休息。",
                "py": "Rúguǒ nǐ tài lèi le jiù zǎo diǎnr xiūxi.",
                "vi": "Nếu bạn quá mệt thì hãy nghỉ ngơi sớm một chút."
            },
            {
                "num": 39,
                "chunks": ["长得", "这只小白猫", "太可爱了"],
                "ans": "这只小白猫长得太可爱了。",
                "py": "Zhè zhī xiǎo bái māo zhǎng de tài kě'ài le.",
                "vi": "Chú mèo trắng nhỏ này trông thật là đáng yêu."
            },
            {
                "num": 40,
                "chunks": ["有很大关系", "健康状况", "跟作息时间"],
                "ans": "健康状况跟作息时间有很大关系。",
                "py": "Jiànkāng zhuàngkuàng gēn zuòxī shíjiān yǒu hěn dà guānxì.",
                "vi": "Tình trạng sức khỏe có liên quan rất lớn tới giờ giấc sinh hoạt."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "(Rúguǒ) 明天晴天，我们就去郊游。",
                "pinyin": "Rúguǒ",
                "ans": "如果",
                "vi": "Nếu ngày mai trời nắng, chúng mình sẽ đi dã ngoại."
            },
            {
                "num": 42,
                "sentence": "爸爸买了一双新 (píxié)。",
                "pinyin": "píxié",
                "ans": "皮鞋",
                "vi": "Bố đã mua một đôi giày da mới."
            },
            {
                "num": 43,
                "sentence": "冬天出门要戴好 (màozi)。",
                "pinyin": "màozi",
                "ans": "帽子",
                "vi": "Mùa đông ra ngoài phải đội mũ cẩn thận."
            },
            {
                "num": 44,
                "sentence": "这只小狗的样子真 (kě'ài)。",
                "pinyin": "kě'ài",
                "ans": "可爱",
                "vi": "Dáng vẻ chú cún con này thật đáng yêu."
            },
            {
                "num": 45,
                "sentence": "早晚认真 (shuāyá) 牙齿好。",
                "pinyin": "shuāyá",
                "ans": "刷牙",
                "vi": "Sáng tối đánh răng cẩn thận thì răng sẽ tốt."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "如果", "py": "rúguǒ", "pos": "liên từ", "vi": "nếu, nếu như", "eg": "如果有时间，我想去旅游。"},
            {"num": 2, "zh": "认为", "py": "rènwéi", "pos": "động từ", "vi": "cho rằng, nghĩ rằng", "eg": "我认为这个办法很好。"},
            {"num": 3, "zh": "皮鞋", "py": "píxié", "pos": "danh từ", "vi": "giày da", "eg": "他穿了一双新皮鞋。"},
            {"num": 4, "zh": "帽子", "py": "màozi", "pos": "danh từ", "vi": "mũ, nón", "eg": "这顶帽子很适合你。"},
            {"num": 5, "zh": "长", "py": "cháng", "pos": "tính từ", "vi": "dài", "eg": "她的头发很长。"},
            {"num": 6, "zh": "可爱", "py": "kě'ài", "pos": "tính từ", "vi": "đáng yêu, dễ thương", "eg": "小熊猫非常可爱。"},
            {"num": 7, "zh": "米", "py": "mǐ", "pos": "lượng từ", "vi": "mét", "eg": "他身高一米八。"},
            {"num": 8, "zh": "公斤", "py": "gōngjīn", "pos": "lượng từ", "vi": "ki-lô-gam (kg)", "eg": "一公斤等于两市斤。"},
            {"num": 9, "zh": "鼻子", "py": "bízi", "pos": "danh từ", "vi": "cái mũi", "eg": "小象长着长长的鼻子。"},
            {"num": 10, "zh": "头发", "py": "tóufa", "pos": "danh từ", "vi": "tóc", "eg": "奶奶的头发都白了。"},
            {"num": 11, "zh": "检查", "py": "jiǎnchá", "pos": "động từ/danh từ", "vi": "kiểm tra", "eg": "写完作业要认真检查。"},
            {"num": 12, "zh": "刷牙", "py": "shuāyá", "pos": "động từ", "vi": "đánh răng", "eg": "睡觉前一定要刷牙。"},
            {"num": 13, "zh": "关系", "py": "guānxì", "pos": "danh từ", "vi": "quan hệ, mối liên hệ", "eg": "他们之间的关系很好。"},
            {"num": 14, "zh": "别人", "py": "biérén", "pos": "đại từ", "vi": "người khác", "eg": "要多为别人着想。"},
            {"num": 15, "zh": "词语", "py": "cíyǔ", "pos": "danh từ", "vi": "từ ngữ", "eg": "我们要积累很多汉语词语。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Bổ ngữ trạng thái chỉ mức độ / kết quả: Tính từ / Động từ + 得 + Cụm từ",
                "desc": "Dùng cụm từ đứng sau '得' để miêu tả mức độ nghiêm trọng hoặc kết quả sống động của tính từ hoặc động từ phía trước.",
                "examples": [
                    {"zh": "我现在累得下了班就想睡觉。", "py": "Wǒ xiànzài lèi de xià le bān jiù xiǎng shuìjiào.", "vi": "Bây giờ tôi mệt đến nỗi tan làm là chỉ muốn ngủ."},
                    {"zh": "他高兴得跳了起来。", "py": "Tā gāoxìng de tiào le qǐlái.", "vi": "Anh ấy vui mừng đến mức nhảy cẫng lên."},
                    {"zh": "小明走得满头大汗。", "py": "Xiǎomíng zǒu de mǎntóu-dàhàn.", "vi": "Tiểu Minh đi bộ đến nỗi mồ hôi nhễ nhại."}
                ]
            },
            {
                "title": "2. Cặp câu điều kiện giả thiết: “如果……就……”",
                "desc": "Biểu thị giả thiết ở vế trước: 'Nếu như tình huống này xảy ra thì vế sau sẽ diễn ra'.",
                "examples": [
                    {"zh": "如果你喜欢，我就送给你。", "py": "Rúguǒ nǐ xǐhuan, wǒ jiù sòng gěi nǐ.", "vi": "Nếu bạn thích thì tôi sẽ tặng bạn."},
                    {"zh": "如果明天不下雨，我们去公园。", "py": "Rúguǒ míngtiān bú xiàyǔ, wǒmen qù gōngyuán.", "vi": "Nếu ngày mai trời không mưa, chúng mình đi công viên."}
                ]
            }
        ]
    },

    # ==================== BÀI 17 ====================
    {
        "id": 17,
        "title_zh": "谁都有办法看好你的“病”。",
        "title_py": "Shéi dōu yǒu bànfǎ kànhǎo nǐ de 'bìng'.",
        "title_vi": "Ai cũng có cách chữa khỏi “bệnh” của em.",
        "dialogues": [
            {
                "title": "Đoạn 1: 向经理请假 (Xin nghỉ phép với giám đốc)",
                "location": "在经理办公室",
                "lines": [
                    {"speaker": "员工", "role": "female", "zh": "周经理，我身体有点儿不舒服，想跟您请一天假。", "py": "Zhōu jīnglǐ, wǒ shēntǐ yǒudiǎnr bù shūfu, xiǎng gēn nín qǐng yì tiān jià.", "vi": "Giám đốc Chu ơi, người em hơi không khỏe, em muốn xin ngài nghỉ phép một ngày ạ."},
                    {"speaker": "经理", "role": "male", "zh": "怎么了？发烧了吗？看了医生没有？", "py": "Zěnme le? Fāshāo le ma? Kàn le yīshēng méiyǒu?", "vi": "Sao thế em? Có bị sốt không? Đã đi khám bác sĩ chưa?"},
                    {"speaker": "员工", "role": "female", "zh": "昨天晚上着凉了，头很疼，一共请两天假行吗？", "py": "Zuótiān wǎnshang zháoliáng le, tóu hěn téng, yígòng qǐng liǎng tiān jià xíng ma?", "vi": "Tối qua em bị trúng gió, đầu đau nhức, em xin nghỉ tổng cộng hai ngày được không ạ?"},
                    {"speaker": "经理", "role": "male", "zh": "没问题，身体要紧，快回去好好休息吧！", "py": "Méi wèntí, shēntǐ yàojǐn, kuài huíqù hǎohǎo xiūxi ba!", "vi": "Không vấn đề gì, sức khỏe là quan trọng nhất, mau về nhà nghỉ ngơi cho tốt nhé!"}
                ]
            },
            {
                "title": "Đoạn 2: 聊邻居与爱好 (Nói về hàng xóm và sở thích)",
                "location": "在小区花园",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "住在我们楼上的新邻居特别热情。", "py": "Zhù zài wǒmen lóu shàng de xīn línjū tèbié rèqíng.", "vi": "Người hàng xóm mới chuyển đến tầng trên nhà mình nhiệt tình lắm anh ạ."},
                    {"speaker": "小刚", "role": "male", "zh": "是吗？我昨天碰到他，他还主动跟我打招呼呢。", "py": "Shì ma? Wǒ zuótiān pèngdào tā, tā hái zhǔdòng gēn wǒ dǎ zhāohu ne.", "vi": "Thế à? Hôm qua anh gặp anh ấy, anh ấy còn chủ động chào hỏi anh nữa."},
                    {"speaker": "小丽", "role": "female", "zh": "后来聊天儿才知道，他的爱好跟我一样，也喜欢养花。", "py": "Hòulái liáotiānr cái zhīdào, tā de àihào gēn wǒ yíyàng, yě xǐhuan yǎng huā.", "vi": "Sau này trò chuyện mới biết, sở thích của anh ấy giống hệt em, cũng thích trồng hoa."},
                    {"speaker": "小刚", "role": "male", "zh": "好邻居比远方的亲戚还亲，以后多走动走动。", "py": "Hǎo línjū bǐ yuǎnfāng de qīnqi hái qīn, yǐhòu duō zǒudong zǒudong.", "vi": "Bán anh em xa mua láng giềng gần, sau này nên qua lại giao lưu nhiều hơn."}
                ]
            },
            {
                "title": "Đoạn 3: 减肥计划 (Kế hoạch giảm cân)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "晚饭吃得太饱了，我又长胖了一斤！", "py": "Wǎnfàn chī de tài bǎo le, wǒ yòu zhǎng pàng le yì jīn!", "vi": "Cơm tối ăn no quá, em lại béo thêm nửa cân rồi!"},
                    {"speaker": "小刚", "role": "male", "zh": "你每次吃完就坐着看电视，能不长肉吗？", "py": "Nǐ měi cì chīwán jiù zuòzhe kàn diànshì, néng bù zhǎng ròu ma?", "vi": "Lần nào em ăn xong cũng ngồi xem tivi, sao mà không tăng cân được?"},
                    {"speaker": "小丽", "role": "female", "zh": "为了减肥，我决定冬天也去游泳！你觉得这个办法怎么样？", "py": "Wèile jiǎnféi, wǒ juédìng dōngtiān yě qù yóuyǒng! Nǐ juéde zhè ge bànfǎ zěnmeyàng?", "vi": "Để giảm cân, em quyết định mùa đông cũng đi bơi! Anh thấy cách này thế nào?"},
                    {"speaker": "小刚", "role": "male", "zh": "谁都有办法看好你的‘胖病’，关键看你自己能不能坚持！", "py": "Shéi dōu yǒu bànfǎ kànhǎo nǐ de 'pàng bìng', guānjiàn kàn nǐ zìjǐ néng bu néng jiānchí!", "vi": "Ai cũng có cách chữa khỏi cái 'bệnh béo' của em, mấu chốt là xem bản thân em có kiên trì được hay không thôi!"}
                ]
            },
            {
                "title": "Đoạn 4: 医生看病 (Bác sĩ khám bệnh)",
                "location": "在门诊室",
                "lines": [
                    {"speaker": "医生", "role": "male", "zh": "你哪里觉得不舒服？", "py": "Nǐ nǎli juéde bù shūfu?", "vi": "Anh cảm thấy không khỏe ở chỗ nào?"},
                    {"speaker": "患者", "role": "female", "zh": "医生，我口很渴，喉咙特别干，浑身没力气。", "py": "Yīshēng, wǒ kǒu hěn kě, hóulóng tèbié gān, húnshēn méi lìqi.", "vi": "Thưa bác sĩ, tôi khát nước lắm, họng khô rát, toàn thân không có chút sức lực nào."},
                    {"speaker": "医生", "role": "male", "zh": "根据你的情况，你必须多喝水，按时吃药，不能再喝冰饮料了。", "py": "Gēnjù nǐ de qíngkuàng, nǐ bìxū duō hē shuǐ, ànshí chī yào, bù néng zài hē bīng yǐnliào le.", "vi": "Căn cứ vào tình hình của anh, anh bắt buộc phải uống nhiều nước, uống thuốc đúng giờ, không được uống đồ lạnh nữa."},
                    {"speaker": "患者", "role": "female", "zh": "好的医生，我一定照您说的做。", "py": "Hǎo de yīshēng, wǒ yídìng zhào nín shuō de zuò.", "vi": "Dạ được thưa bác sĩ, tôi nhất định sẽ làm đúng theo lời bác sĩ dặn ạ."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：经理，我今天发烧了，想请假去医院看病。 男：好的，你快去吧，身体最重要。",
                "question": "女的为什么向经理请假？",
                "options": ["A. 她想去旅游", "B. 她发烧了要去看病", "C. 她要搬家"],
                "ans": "B",
                "explain": "Cô gái nói: 我今天发烧了，想请假去医院看病."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小丽的新邻居跟她一样，也特别喜欢在阳台上养花。",
                "question": "Phán đoán đúng hay sai: 新邻居和小丽有相同的爱好。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Cả hai đều có chung sở thích trồng hoa (爱好跟我一样，也喜欢养花)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：你每次吃得那么饱，又不肯运动，能减肥吗？ 女：好，那我明天开始每天跑两公里。",
                "question": "男的觉得女的为什么减不了肥？",
                "options": ["A. 吃得太饱且不运动", "B. 喝水太少", "C. 睡得太早"],
                "ans": "A",
                "explain": "Ăn quá no và lười vận động (吃得那么饱，又不肯运动)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：医生，我喉咙特别干，经常口渴。 男：根据你的情况，你必须每天多喝温开水。",
                "question": "医生建议病人怎么做？",
                "options": ["A. 多喝温开水", "B. 多吃辣椒", "C. 喝冰啤酒"],
                "ans": "A",
                "explain": "Bác sĩ dặn: 必须每天多喝温开水."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "谁都有办法看好你的病，关键看你能不能坚持。", "py": "Shéi dōu yǒu bànfǎ kànhǎo nǐ de bìng, guānjiàn kàn nǐ néng bu néng jiānchí.", "vi": "Ai cũng có cách chữa khỏi bệnh cho bạn, mấu chốt là xem bạn có kiên trì được không."},
                {"id": "B", "text": "生病了就要及时去医院看医生，别硬撑着。", "py": "Shēngbìng le jiù yào jíshí qù yīyuàn kàn yīshēng, bié yìng chēngzhe.", "vi": "Ốm rồi thì phải kịp thời đi bệnh viện khám bác sĩ, đừng cố gượng."},
                {"id": "C", "text": "新搬来的邻居非常热情，大家关系很融洽。", "py": "Xīn bānlái de línjū fēicháng rèqíng, dàjiā guānxì hěn róngqià.", "vi": "Người hàng xóm mới chuyển tới rất nhiệt tình, quan hệ mọi người rất hòa thuận."},
                {"id": "D", "text": "根据目前的天气情况，明天可能会降温。", "py": "Gēnjù mùqián de tiānqì qíngkuàng, míngtiān kěnéng huì jiàngwēn.", "vi": "Căn cứ vào tình hình thời tiết hiện nay, ngày mai có thể sẽ hạ nhiệt."},
                {"id": "E", "text": "晚饭吃得太饱容易消化不良，应该少吃点儿。", "py": "Wǎnfàn chī de tài bǎo róngyì xiāohuà bùliáng, yīnggāi shǎo chī diǎnr.", "vi": "Bữa tối ăn quá no dễ khó tiêu, nên ăn ít lại một chút."}
            ],
            "questions": [
                {"num": 21, "text": "我试了很多减肥食谱，怎么都不管用？", "py": "Wǒ shì le hěn duō jiǎnféi shípǔ, zěnme dōu bù guǎnyòng?", "vi": "Tôi thử bao nhiêu thực đơn giảm cân, sao chẳng cái nào hiệu quả?", "ans": "A", "explain": "Ai cũng có phương pháp, mấu chốt là bản thân có kiên trì được không."},
                {"num": 22, "text": "他咳嗽了好几天，还坚持来公司上班呢。", "py": "Tā késou le hǎo jǐ tiān, hái jiānchí lái gōngsī shàngbān ne.", "vi": "Anh ấy ho mấy hôm liền rồi mà vẫn kiên quyết đến công ty làm việc kìa.", "ans": "B", "explain": "Khuyên ốm thì nên đi khám bệnh, đừng ráng sức."},
                {"num": 23, "text": "你觉得你们小区的人际环境好不好？", "py": "Nǐ juéde nǐmen xiǎoqū de rénjì huánjìng hǎobuhǎo?", "vi": "Bạn thấy môi trường quan hệ hàng xóm khu bạn thế nào?", "ans": "C", "explain": "Khen hàng xóm mới nhiệt tình, hòa thuận."},
                {"num": 24, "text": "明天的室外演出会不会受到天气影响？", "py": "Míngtiān de shìwài yǎnchū huì bu huì shòudào tiānqì yǐngxiǎng?", "vi": "Buổi biểu diễn ngoài trời ngày mai có bị ảnh hưởng thời tiết không?", "ans": "D", "explain": "Căn cứ tình hình dự báo ngày mai nhiệt độ giảm."},
                {"num": 25, "text": "你怎么摸着肚子喊难受啊？", "py": "Nǐ zěnme mōzhe dùzi hǎn nánshòu a?", "vi": "Sao cậu ôm bụng kêu khó chịu thế?", "ans": "E", "explain": "Do bữa tối ăn quá no dễ tức bụng."},
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "请假", "py": "qǐngjià", "vi": "xin nghỉ phép"},
                {"id": "B", "zh": "邻居", "py": "línjū", "vi": "hàng xóm"},
                {"id": "C", "zh": "办法", "py": "bànfǎ", "vi": "biện pháp, cách"},
                {"id": "D", "zh": "必须", "py": "bìxū", "vi": "bắt buộc, phải"},
                {"id": "E", "zh": "情况", "py": "qíngkuàng", "vi": "tình hình, hoàn cảnh"}
            ],
            "questions": [
                {"num": 26, "prefix": "他身体发烧了，不得不向经理", "suffix": "一天。", "py": "Tā shēntǐ fāshāo le, bùdébù xiàng jīnglǐ ( ? ) yì tiān.", "vi": "Cơ thể anh ấy phát sốt, buộc phải xin giám đốc ( ? ) một ngày.", "ans": "A", "word": "请假", "explain": "Xin nghỉ phép: 请假 (qǐngjià)."},
                {"num": 27, "prefix": "常言说得好，远亲不如近", "suffix": "。", "py": "Chángyán shuō de hǎo, yuǎnqīn bùrú jìn ( ? ).", "vi": "Tục ngữ nói rất hay: Bán anh em xa mua láng giềng ( ? ).", "ans": "B", "word": "邻居", "explain": "Hàng xóm láng giềng: 邻居 (línjū)."},
                {"num": 28, "prefix": "遇到困难不要怕，总会有解决的", "suffix": "。", "py": "Yùdào kùnnan bú yào pà, zǒng huì yǒu jiějué de ( ? ).", "vi": "Gặp khó khăn đừng sợ, luôn luôn sẽ có ( ? ) giải quyết.", "ans": "C", "word": "办法", "explain": "Biện pháp, cách: 办法 (bànfǎ)."},
                {"num": 29, "prefix": "过马路时", "suffix": "看清红绿灯。", "py": "Guò mǎlù shí ( ? ) kànqīng hónglǜdēng.", "vi": "Khi qua đường ( ? ) nhìn rõ đèn tín hiệu giao thông.", "ans": "D", "word": "必须", "explain": "Bắt buộc: 必须 (bìxū)."},
                {"num": 30, "prefix": "医生认真询问了病人的身体", "suffix": "。", "py": "Yīshēng rènzhēn xùnwèn le bìngrén de shēntǐ ( ? ).", "vi": "Bác sĩ cẩn thận hỏi han về ( ? ) sức khỏe của bệnh nhân.", "ans": "E", "word": "情况", "explain": "Tình hình: 情况 (qíngkuàng)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "现代很多人都有一个共同的毛病：总说自己太忙，没有时间锻炼身体。小丽就是这样，平时一下班就窝在家里看电视，吃零食，不知不觉胖了五公斤。有一天，小丽感觉头晕、口渴，走几步路就喘不过气来。她很害怕，就去医院看大夫。大夫给她检查后笑着说：“你这不叫生病，你这是‘懒病’！谁都有办法看好你的病：少吃多动，管住嘴，迈开腿。根据你的情况，你必须每天坚持走一万步，按时吃饭，不能暴饮暴食。”小丽听了医生的话，下定决心改变自己的生活习惯。",
            "passage_py": "Xiàndài hěn duō rén dōu yǒu yí ge gòngtóng de máobìng: zǒng shuō zìjǐ tài máng, méiyǒu shíjiān duànliàn shēntǐ. Xiǎolì jiù shì zhèyàng, píngshí yí xiàbān jiù wō zài jiā li kàn diànshì, chī língshí, bùzhī-bùjué pàng le wǔ gōngjīn. Yǒu yì tiān, Xiǎolì gǎnjué tóuyūn, kǒukě, zǒu jǐ bù lù jiù chuǎnbuguòqì lái. Tā hěn hàipà, jiù qù yīyuàn kàn dàifu. Dàifu gěi tā jiǎnchá hòu xiàozhe shuō: 'Nǐ zhè bù jiào shēngbìng, nǐ zhè shì \"lǎnbìng\"! Shéi dōu yǒu bànfǎ kànhǎo nǐ de bìng: shǎo chī duō dòng, guǎnzhu zǐ, màikāi tuǐ. Gēnjù nǐ de qíngkuàng, nǐ bìxū měitiān jiānchí zǒu yí wàn bù, ànshí chī fàn, bù néng bàoyǐn-bàoshí.' Xiǎolì tīng le yīshēng de huà, xiàdìng juéxīn gǎibiàn zìjǐ de shēnghuó xíguàn.",
            "passage_vi": "Rất nhiều người trong xã hội hiện đại đều có một tật xấu chung: luôn kêu ca mình quá bận rộn, không có thời gian rèn luyện thân thể. Tiểu Lệ cũng chính là như vậy, bình thường cứ tan làm là ru rú trong nhà xem tivi, ăn vặt, chẳng hay biết đã béo lên 5 cân. Có một hôm, Tiểu Lệ cảm thấy choáng váng, khát nước, đi vài bước chân là đã thở không ra hơi. Cô rất sợ hãi liền đi bệnh viện khám. Bác sĩ sau khi kiểm tra mỉm cười bảo: 'Cô cái này đâu phải là ốm bệnh, đây là \"bệnh lười\"! Ai cũng có cách chữa khỏi bệnh cho cô cả: ăn ít vận động nhiều, bóp mồm bóp miệng, cất bước đôi chân. Căn cứ vào tình trạng của cô, cô bắt buộc mỗi ngày phải kiên trì đi một vạn bước, ăn cơm đúng bữa, không được ăn uống vô độ.' Tiểu Lệ nghe xong lời bác sĩ, đã hạ quyết tâm thay đổi thói quen sinh hoạt của mình.",
            "questions": [
                {
                    "num": 31,
                    "text": "小丽平时下班后喜欢做什么？",
                    "options": ["A. 去健身房跑步", "B. 窝在家里看电视吃零食", "C. 去图书馆学习"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 平时一下班就窝在家里看电视，吃零食."
                },
                {
                    "num": 32,
                    "text": "小丽不知不觉胖了多少？",
                    "options": ["A. 两公斤", "B. 三公斤", "C. 五公斤"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 不知不觉胖了五公斤."
                },
                {
                    "num": 33,
                    "text": "大夫说小丽得的是什么“病”？",
                    "options": ["A. 发烧感冒", "B. “懒病”", "C. 胃病"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 大夫笑着说：你这不叫生病，你这是“懒病”!"
                },
                {
                    "num": 34,
                    "text": "大夫建议小丽每天必须坚持做什么？",
                    "options": ["A. 走一万步", "B. 喝三瓶啤酒", "C. 睡十个小时"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 必须每天坚持走一万步."
                },
                {
                    "num": 35,
                    "text": "听完大夫的话，小丽有什么打算？",
                    "options": ["A. 继续天天吃零食", "B. 下定决心改变生活习惯", "C. 不想再去医院"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 小丽听了医生的话，下定决心改变自己的生活习惯."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["谁都有办法", "看好", "你的病"],
                "ans": "谁都有办法看好你的病。",
                "py": "Shéi dōu yǒu bànfǎ kànhǎo nǐ de bìng.",
                "vi": "Ai cũng có cách chữa khỏi bệnh cho bạn."
            },
            {
                "num": 37,
                "chunks": ["向经理", "请了两天假", "他生病了"],
                "ans": "他生病了向经理请了两天假。",
                "py": "Tā shēngbìng le xiàng jīnglǐ qǐng le liǎng tiān jià.",
                "vi": "Anh ấy bị ốm đã xin phép giám đốc nghỉ 2 ngày."
            },
            {
                "num": 38,
                "chunks": ["热情好客", "新搬来的邻居", "非常"],
                "ans": "新搬来的邻居非常热情好客。",
                "py": "Xīn bānlái de línjū fēicháng rèqíng-hàokè.",
                "vi": "Người hàng xóm mới chuyển tới rất mực nhiệt tình hiếu khách."
            },
            {
                "num": 39,
                "chunks": ["根据你的情况", "按时吃药", "你必须"],
                "ans": "根据你的情况你必须按时吃药。",
                "py": "Gēnjù nǐ de qíngkuàng nǐ bìxū ànshí chī yào.",
                "vi": "Căn cứ vào tình hình của bạn, bạn bắt buộc phải uống thuốc đúng giờ."
            },
            {
                "num": 40,
                "chunks": ["为了身体健康", "多运动", "我们应该"],
                "ans": "为了身体健康我们应该多运动。",
                "py": "Wèile shēntǐ jiànkāng wǒmen yīnggāi duō yùndòng.",
                "vi": "Vì sức khỏe thân thể chúng ta nên vận động nhiều hơn."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "明天家里有事，我想 (qǐngjià)。",
                "pinyin": "qǐngjià",
                "ans": "请假",
                "vi": "Ngày mai nhà có việc, tôi muốn xin nghỉ phép."
            },
            {
                "num": 42,
                "sentence": "我们跟 (línjū) 的关系很好。",
                "pinyin": "línjū",
                "ans": "邻居",
                "vi": "Mối quan hệ giữa chúng tôi và hàng xóm rất tốt."
            },
            {
                "num": 43,
                "sentence": "你有解决这个问题的 (bànfǎ) 吗？",
                "pinyin": "bànfǎ",
                "ans": "办法",
                "vi": "Bạn có cách giải quyết vấn đề này không?"
            },
            {
                "num": 44,
                "sentence": "上课 (bìxū) 认真听讲。",
                "pinyin": "bìxū",
                "ans": "必须",
                "vi": "Trong giờ học bắt buộc phải chăm chú nghe giảng."
            },
            {
                "num": 45,
                "sentence": "跑步后我觉得很 (kě)，想喝水。",
                "pinyin": "kě",
                "ans": "渴",
                "vi": "Chạy bộ xong tôi thấy rất khát, muốn uống nước."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "请假", "py": "qǐngjià", "pos": "động từ", "vi": "xin nghỉ phép", "eg": "我向老师请假三天。"},
            {"num": 2, "zh": "一共", "py": "yígòng", "pos": "phó từ", "vi": "tổng cộng, tất cả", "eg": "这些苹果一共三十块钱。"},
            {"num": 3, "zh": "邻居", "py": "línjū", "pos": "danh từ", "vi": "hàng xóm, láng giềng", "eg": "王阿姨是我们家多年的老邻居。"},
            {"num": 4, "zh": "后来", "py": "hòulái", "pos": "danh từ chỉ thời gian", "vi": "về sau, sau này", "eg": "后来他去了一家外企工作。"},
            {"num": 5, "zh": "爱好", "py": "àihào", "pos": "danh từ/động từ", "vi": "sở thích, yêu thích", "eg": "我的业余爱好是听音乐。"},
            {"num": 6, "zh": "办法", "py": "bànfǎ", "pos": "danh từ", "vi": "biện pháp, cách thức", "eg": "你有什么好办法吗？"},
            {"num": 7, "zh": "饱", "py": "bǎo", "pos": "tính từ", "vi": "no, no bụng", "eg": "我已经吃饱了，吃不下了。"},
            {"num": 8, "zh": "为了", "py": "wèile", "pos": "giới từ", "vi": "để, vì (mục đích)", "eg": "为了学好汉语，他每天练习口语。"},
            {"num": 9, "zh": "决定", "py": "juédìng", "pos": "động từ/danh từ", "vi": "quyết định", "eg": "我决定明年去北京旅游。"},
            {"num": 10, "zh": "选择", "py": "xuǎnzé", "pos": "động từ/danh từ", "vi": "lựa chọn, chọn lựa", "eg": "做出正确的选择很重要。"},
            {"num": 11, "zh": "冬(天)", "py": "dōng (tiān)", "pos": "danh từ", "vi": "mùa đông", "eg": "北京的冬天经常下大雪。"},
            {"num": 12, "zh": "必须", "py": "bìxū", "pos": "phó từ", "vi": "bắt buộc, nhất định phải", "eg": "明天你必须把作业交上来。"},
            {"num": 13, "zh": "根据", "py": "gēnjù", "pos": "giới từ/danh từ", "vi": "căn cứ vào, dựa vào", "eg": "根据天气预报，明天要降温。"},
            {"num": 14, "zh": "情况", "py": "qíngkuàng", "pos": "danh từ", "vi": "tình hình, hoàn cảnh", "eg": "这里的具体情况我还不了解。"},
            {"num": 15, "zh": "口", "py": "kǒu", "pos": "danh từ/lượng từ", "vi": "miệng, ngụm, khẩu", "eg": "喝一口水, 一家五口人。"},
            {"num": 16, "zh": "渴", "py": "kě", "pos": "tính từ", "vi": "khát nước", "eg": "走得太累了，口好渴。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Đại từ nghi vấn biểu thị toàn thể: 谁 / 什么 / 哪儿 + 都 / 也 + Vị ngữ",
                "desc": "Dùng đại từ nghi vấn kết hợp với '都' hoặc '也' để biểu thị bất cứ người nào, vật nào, nơi chốn nào cũng có chung đặc điểm hoặc áp dụng chung một quy tắc (không có ngoại lệ).",
                "examples": [
                    {"zh": "谁都有办法看好你的病。", "py": "Shéi dōu yǒu bànfǎ kànhǎo nǐ de bìng.", "vi": "Ai cũng có cách chữa khỏi bệnh cho bạn."},
                    {"zh": "他什么都想吃。", "py": "Tā shénme dōu xiǎng chī.", "vi": "Cái gì nó cũng muốn ăn."},
                    {"zh": "我哪儿都不想去。", "py": "Wǒ nǎr dōu bù xiǎng qù.", "vi": "Tôi chẳng muốn đi bất cứ nơi đâu."}
                ]
            },
            {
                "title": "2. Giới từ chỉ căn cứ: “根据……”",
                "desc": "Được dùng để dẫn ra cơ sở, bằng chứng hoặc tình hình làm căn cứ cho nhận định hoặc hành động ở vế sau.",
                "examples": [
                    {"zh": "根据天气预报，明天要下雨。", "py": "Gēnjù tiānqì yùbào, míngtiān yào xiàyǔ.", "vi": "Căn cứ theo dự báo thời tiết, ngày mai trời sẽ mưa."},
                    {"zh": "根据他的表现，大家选他当班长。", "py": "Gēnjù tā de biǎoxiàn, dàjiā xuǎn tā dāng bānzhǎng.", "vi": "Dựa trên biểu hiện của bạn ấy, mọi người bầu bạn ấy làm lớp trưởng."}
                ]
            }
        ]
    },

    # ==================== BÀI 18 ====================
    {
        "id": 18,
        "title_zh": "我相信他们会同意的。",
        "title_py": "Wǒ xiāngxìn tāmen huì tóngyì de.",
        "title_vi": "Tôi tin họ sẽ đồng ý.",
        "dialogues": [
            {
                "title": "Đoạn 1: 谈商务合作 (Nói về hợp tác kinh doanh)",
                "location": "在会议室",
                "lines": [
                    {"speaker": "周明", "role": "male", "zh": "关于这次合作计划，你准备好了吗？", "py": "Guānyú zhè cì hézuò jìhuà, nǐ zhǔnbèi hǎo le ma?", "vi": "Về kế hoạch hợp tác lần này, cậu đã chuẩn bị xong chưa?"},
                    {"speaker": "同事", "role": "female", "zh": "准备好了，报告写得很详细，方案也非常合理。", "py": "Zhǔnbèi hǎo le, bàogào xiě de hěn xiángxì, fāng'àn yě fēicháng hélǐ.", "vi": "Chuẩn bị xong rồi anh, báo cáo viết rất chi tiết, phương án cũng vô cùng hợp lý."},
                    {"speaker": "周明", "role": "male", "zh": "我相信对方公司的主管一定会同意的。", "py": "Wǒ xiāngxìn duìfāng gōngsī de zhǔguǎn yídìng huì tóngyì de.", "vi": "Tôi tin là người phụ trách bên công ty đối tác nhất định sẽ đồng ý thôi."},
                    {"speaker": "同事", "role": "female", "zh": "太好了，能抓住这个难得的机会，我们部门就成功了一半！", "py": "Tài hǎo le, néng zhuāzhù zhè ge nándé de jīhuì, wǒmen bùmén jiù chénggōng le yíbàn!", "vi": "Tuyệt quá, nắm bắt được cơ hội hiếm có này là phòng mình đã thành công một nửa rồi!"}
                ]
            },
            {
                "title": "Đoạn 2: 聊工作机会 (Nói về cơ hội công việc)",
                "location": "在咖啡厅",
                "lines": [
                    {"speaker": "朋友A", "role": "male", "zh": "听说一家跨国大公司在招人，你去试试吗？", "py": "Tīngshuō yì jiā kuàguó dà gōngsī zài zhāorén, nǐ qù shìshi ma?", "vi": "Nghe nói có một tập đoàn đa quốc gia đang tuyển người, cậu có đi thử sức không?"},
                    {"speaker": "朋友B", "role": "female", "zh": "要求很高，我有点儿担心自己的能力不够。", "py": "Yāoqiú hěn gāo, wǒ yǒudiǎnr dānxīn zìjǐ de nénglì bú gòu.", "vi": "Yêu cầu cao lắm, tớ hơi lo năng lực bản thân chưa đủ."},
                    {"speaker": "朋友A", "role": "male", "zh": "只要有机会就要勇敢去试，不要害怕失败。", "py": "Zhǐyào yǒu jīhuì jiù yào yǒnggǎn qù shì, bú yào hàipà shībài.", "vi": "Chỉ cần có cơ hội là phải dũng cảm thử, đừng có sợ thất bại."},
                    {"speaker": "朋友B", "role": "female", "zh": "你说得对，明天我就把简历发过去！", "py": "Nǐ shuō de duì, míngtiān wǒ jiù bǎ jiǎnlì fā guòqù!", "vi": "Cậu nói đúng, ngày mai tớ sẽ gửi hồ sơ xin việc sang liền!"}
                ]
            },
            {
                "title": "Đoạn 3: 介绍家乡特点 (Giới thiệu nét đặc sắc quê hương)",
                "location": "在宿舍",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "每个国家和地方都有自己的文化特点。", "py": "Měi ge guójiā hé dìfang dōu yǒu zìjǐ de wénhuà tèdiǎn.", "vi": "Mỗi quốc gia và vùng miền đều có nét đặc sắc văn hóa riêng."},
                    {"speaker": "外国朋友", "role": "male", "zh": "是的，你们那里的菜有什么特点呢？", "py": "Shì de, nǐmen nàlǐ de cài yǒu shénme tèdiǎn ne?", "vi": "Đúng thế, món ăn ở quê bạn có đặc điểm gì vậy?"},
                    {"speaker": "小丽", "role": "female", "zh": "我们那里的菜偏甜，味道很清淡，一点儿也不辣。", "py": "Wǒmen nàlǐ de cài piān tián, wèidao hěn qīngdàn, yìdiǎnr yě bù là.", "vi": "Món ăn quê mình hơi ngọt, vị thanh đạm, một chút cũng không cay."},
                    {"speaker": "外国朋友", "role": "male", "zh": "听起来真奇怪，但在中国这也算是一种独特的风味吧。", "py": "Tīng qǐlái zhēn qíguài, dàn zài Zhōngguó zhè yě suàn shì yì zhǒng dútè de fēngwèi ba.", "vi": "Nghe có vẻ kỳ lạ thật, nhưng ở Trung Quốc đây cũng được coi là một phong vị độc đáo nhỉ."}
                ]
            },
            {
                "title": "Đoạn 4: 告别朋友 (Chia tay bạn bè)",
                "location": "在火车站站台",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "火车马上就要开了，你快上车吧。", "py": "Huǒchē mǎshàng jiù yào kāi le, nǐ kuài shàngchē ba.", "vi": "Tàu sắp chạy rồi, cậu mau lên tàu đi."},
                    {"speaker": "老同学", "role": "female", "zh": "想到要离开生活了四年的城市和朋友，心里真难受。", "py": "Xiǎngdào yào líkāi shēnghuó le sì nián de chéngshì hé péngyou, xīnlǐ zhēn nánshòu.", "vi": "Nghĩ đến việc phải rời xa thành phố và bạn bè đã gắn bó suốt 4 năm, trong lòng tớ buồn bã khó chịu quá."},
                    {"speaker": "小刚", "role": "male", "zh": "别难过了，现代交通这么方便，有空常回来看我们！", "py": "Bié nánguò le, xiàndài jiāotōng zhème fāngbiàn, yǒu kòng cháng huílái kàn wǒmen!", "vi": "Đừng buồn nữa, giao thông hiện đại thuận tiện thế này, rảnh rỗi thường xuyên quay lại thăm chúng tớ nhé!"},
                    {"speaker": "老同学", "role": "female", "zh": "好，保重身体，我们保持联系！", "py": "Hǎo, bǎozhòng shēntǐ, wǒmen bǎochí liánxì!", "vi": "Được, cậu bảo trọng sức khỏe nhé, chúng mình luôn giữ liên lạc!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：对方公司看了我们的报告，同意合作了吗？ 男：是的，他们非常满意，我相信一切都会很顺利。",
                "question": "对方公司的态度怎么样？",
                "options": ["A. 不同意", "B. 非常满意，同意合作", "C. 还在考虑"],
                "ans": "B",
                "explain": "Đoạn thoại nêu: 非常满意，同意合作."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "面对大公司的招聘机会，朋友A鼓励朋友B一定要去试一试。",
                "question": "Phán đoán đúng hay sai: 朋友A劝朋友B放弃这个机会。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Bạn A khuyên phải dũng cảm thử sức (勇敢去试), không hề khuyên từ bỏ."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：小丽，你家乡的菜有什么特点？ 女：我们那里的菜味道偏甜，一点儿也不辣。",
                "question": "小丽家乡的菜味道怎么样？",
                "options": ["A. 特别辣", "B. 偏甜不辣", "C. 很咸"],
                "ans": "B",
                "explain": "Cô gái nói: 偏甜，一点儿也不辣."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：要离开生活了四年的大学，我心里真难受。 男：别难过了，以后常回来看我们。",
                "question": "女的为什么心里难受？",
                "options": ["A. 因为生病了", "B. 因为要离开大学和朋友", "C. 因为考试没考好"],
                "ans": "B",
                "explain": "Cô ấy buồn vì phải rời xa bạn bè và trường đại học."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "方案非常合理，我相信他们一定会同意的。", "py": "Fāng'àn fēicháng hélǐ, wǒ xiāngxìn tāmen yídìng huì tóngyì de.", "vi": "Phương án rất hợp lý, tôi tin họ nhất định sẽ đồng ý."},
                {"id": "B", "text": "既然有这么好的工作机会，就一定要去试一试。", "py": "Jìrán yǒu zhème hǎo de gōngzuò jīhuì, jiù yídìng yào qù shì yí shì.", "vi": "Đã có cơ hội công việc tốt như vậy thì nhất định phải đi thử sức xem sao."},
                {"id": "C", "text": "这道菜的味道有点儿奇怪，但吃起来很甜。", "py": "Zhè dào cài de wèidao yǒudiǎnr qíguài, dàn chī qǐlái hěn tián.", "vi": "Mùi vị món ăn này hơi kỳ lạ một chút, nhưng ăn vào rất ngọt."},
                {"id": "D", "text": "要离开相处多年的老朋友，心里真舍不得。", "py": "Yào líkāi xiāngchǔ duō nián de lǎo péngyou, xīnlǐ zhēn shěbude.", "vi": "Phải rời xa bạn bè cũ gắn bó nhiều năm, trong lòng thật không nỡ."},
                {"id": "E", "text": "孩子们在操场上高兴地做游戏。", "py": "Háizimen zài cāochǎng shang gāoxìng de zuò yóuxì.", "vi": "Lũ trẻ vui vẻ chơi trò chơi trên sân vận động."}
            ],
            "questions": [
                {"num": 21, "text": "周经理对今天下午的谈判有信心吗？", "py": "Zhōu jīnglǐ duì jīntiān xiàwǔ de tánpàn yǒu xìnxīn ma?", "vi": "Giám đốc Chu có tự tin vào cuộc đàm phán chiều nay không?", "ans": "A", "explain": "Tin tưởng đối phương sẽ đồng ý phương án."},
                {"num": 22, "text": "听说名企在招储备干部，你报不报名？", "py": "Tīngshuō míngqǐ zài zhāo chǔbèi gānbù, nǐ bào bu bàomíng?", "vi": "Nghe nói doanh nghiệp lớn đang tuyển cán bộ nguồn, bạn có đăng ký không?", "ans": "B", "explain": "Khẳng định có cơ hội tốt nhất định phải thử sức."},
                {"num": 23, "text": "你尝尝这盘特色点心，感觉怎么样？", "py": "Nǐ chángchang zhè pán tèsè diǎnxin, gǎnjué zěnmeyàng?", "vi": "Cậu nếm thử đĩa điểm tâm đặc sản này xem cảm giác thế nào?", "ans": "C", "explain": "Nhận xét vị hơi lạ nhưng ngọt."},
                {"num": 24, "text": "站在火车站站台上，你怎么哭了？", "py": "Zhàn zài huǒchēzhàn zhàntái shang, nǐ zěnme kū le?", "vi": "Đứng ở sân ga xe lửa, sao cậu lại khóc thế?", "ans": "D", "explain": "Xúc động vì phải chia tay bạn bè cũ."},
                {"num": 25, "text": "操场上怎么传来那么多欢笑声？", "py": "Cāochǎng shang zěnme chuánlái nàme duō huānxiàoshēng?", "vi": "Trên sân vận động sao truyền lại nhiều tiếng cười thế?", "ans": "E", "explain": "Lũ trẻ đang vui vẻ chơi trò chơi."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "相信", "py": "xiāngxìn", "vi": "tin tưởng, tin"},
                {"id": "B", "zh": "同意", "py": "tóngyì", "vi": "đồng ý"},
                {"id": "C", "zh": "机会", "py": "jīhuì", "vi": "cơ hội"},
                {"id": "D", "zh": "奇怪", "py": "qíguài", "vi": "kỳ lạ"},
                {"id": "E", "zh": "试", "py": "shì", "vi": "thử, thử sức"}
            ],
            "questions": [
                {"num": 26, "prefix": "只要你肯努力，我就", "suffix": "你能成功。", "py": "Zhǐyào nǐ kěn nǔlì, wǒ jiù ( ? ) nǐ néng chénggōng.", "vi": "Chỉ cần bạn chịu nỗ lực, tôi ( ? ) bạn có thể thành công.", "ans": "A", "word": "相信", "explain": "Tin tưởng: 相信 (xiāngxìn)."},
                {"num": 27, "prefix": "大家讨论了很久，最后都", "suffix": "了这个方案。", "py": "Dàjiā tǎolùn le hěn jiǔ, zuìhòu dōu ( ? ) le zhè ge fāng'àn.", "vi": "Mọi người thảo luận hồi lâu, cuối cùng đều ( ? ) phương án này.", "ans": "B", "word": "同意", "explain": "Đồng ý: 同意 (tóngyì)."},
                {"num": 28, "prefix": "这次出国留学是一个难得的好", "suffix": "。", "py": "Zhè cì chūguó liúxué shì yí ge nándé de hǎo ( ? ).", "vi": "Lần đi du học này là một ( ? ) tốt hiếm có.", "ans": "C", "word": "机会", "explain": "Cơ hội: 机会 (jīhuì)."},
                {"num": 29, "prefix": "这件衣服的样式很", "suffix": "，我从来没见过。", "py": "Zhè jiàn yīfu de yàngshì hěn ( ? ), wǒ cónglái méi jiànguo.", "vi": "Kiểu dáng bộ quần áo này rất ( ? ), tôi chưa từng thấy bao giờ.", "ans": "D", "word": "奇怪", "explain": "Kỳ lạ: 奇怪 (qíguài)."},
                {"num": 30, "prefix": "这件新衣服大小合适，快去", "suffix": "一试吧。", "py": "Zhè jiàn xīn yīfu dàxiǎo héshì, kuài qù ( ? ) yí shì ba.", "vi": "Bộ quần áo mới này kích cỡ vừa vặn, mau đi ( ? ) một chút đi.", "ans": "E", "word": "试", "explain": "Thử: 试一试 (shì yí shì)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "毕业找工作的时候，很多大学生都觉得自己缺乏工作经验，不敢向大公司投简历。张明也是这样，但是他的辅导员老师鼓励他：“只要有适合自己的机会，就要勇敢地去试一试。你不去尝试，怎么知道自己行不行呢？”张明听了老师的话，认真修改了自己的简历，并向一家知名企业提出了申请。面试的时候，张明自信、大方地回答了考官的所有问题。最后考官非常满意，我相信他们会同意录用张明的，因为机会永远留给有准备且敢于尝试的人。",
            "passage_py": "Bìyè zhǎo gōngzuò de shíhou, hěn duō dàxuéshēng dōu juéde zìjǐ quēfá gōngzuò jīngyàn, bù gǎn xiàng dà gōngsī tóu jiǎnlì. Zhāng Míng yě shì zhèyàng, dànshì tā de fǔdǎoyuán lǎoshī gǔlì tā: 'Zhǐyào yǒu shìhé zìjǐ de jīhuì, jiù yào yǒnggǎn de qù shì yí shì. Nǐ bú qù chángshì, zěnme zhīdào zìjǐ xíng bu xíng ne?' Zhāng Míng tīng le lǎoshī de huà, rènzhēn xiūgǎi le zìjǐ de jiǎnlì, bìng xiàng yì jiā zhīmíng qǐyè tíchū le shēnqǐng. Miànshì de shíhou, Zhāng Míng zìxìn, dàfang de huídá le kǎoguān de suǒyǒu wèntí. Zuìhòu kǎoguān fēicháng mǎnyì, wǒ xiāngxìn tāmen huì tóngyì lùyòng Zhāng Míng de, yīnwèi jīhuì yǒngyuǎn liú gěi yǒu zhǔnbèi qiě gǎnyú chángshì de rén.",
            "passage_vi": "Lúc tốt nghiệp tìm việc làm, rất nhiều sinh viên đại học đều cảm thấy mình thiếu kinh nghiệm làm việc, không dám nộp hồ sơ vào các công ty lớn. Trương Minh cũng như vậy, nhưng thầy cố vấn học tập đã động viên cậu: 'Chỉ cần có cơ hội phù hợp với bản thân thì hãy dũng cảm đi thử sức. Em không thử thì làm sao biết mình có làm được hay không?' Trương Minh nghe lời thầy giáo, cẩn thận chỉnh sửa bản lý lịch của mình và nộp đơn xin việc vào một doanh nghiệp danh tiếng. Lúc phỏng vấn, Trương Minh tự tin, đàng hoàng trả lời trôi chảy mọi câu hỏi của giám khảo. Cuối cùng các giám khảo vô cùng hài lòng, tôi tin rằng họ sẽ đồng ý tuyển dụng Trương Minh, bởi vì cơ hội luôn luôn dành cho những người có sự chuẩn bị và dám thử sức.",
            "questions": [
                {
                    "num": 31,
                    "text": "很多大学生找工作时为什么不敢投大公司？",
                    "options": ["A. 不想去上班", "B. 觉得自己缺乏工作经验", "C. 嫌工资太低"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 觉得自己缺乏工作经验."
                },
                {
                    "num": 32,
                    "text": "老师怎么鼓励张明？",
                    "options": ["A. 让他回家休息", "B. 有机会就要勇敢地试一试", "C. 建议他考研究生"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 只要有适合自己的机会，就要勇敢地去试一试."
                },
                {
                    "num": 33,
                    "text": "面试的时候张明表现得怎么样？",
                    "options": ["A. 特别紧张说不出话", "B. 自信、大方地回答问题", "C. 迟到了半个小时"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 自信、大方地回答了考官的所有问题."
                },
                {
                    "num": 34,
                    "text": "考官对张明的面试评价怎么样？",
                    "options": ["A. 非常满意", "B. 不满意", "C. 觉得他不够努力"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 最后考官非常满意."
                },
                {
                    "num": 35,
                    "text": "根据这段话，机会留给什么样的人？",
                    "options": ["A. 运气好的人", "B. 有准备且敢于尝试的人", "C. 有很多钱的人"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 机会永远留给有准备且敢于尝试的人."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["我相信", "会同意的", "他们"],
                "ans": "我相信他们会同意的。",
                "py": "Wǒ xiāngxìn tāmen huì tóngyì de.",
                "vi": "Tôi tin là họ sẽ đồng ý."
            },
            {
                "num": 37,
                "chunks": ["去试一试", "勇敢地", "我们应该"],
                "ans": "我们应该勇敢地去试一试。",
                "py": "Wǒmen yīnggāi yǒnggǎn de qù shì yí shì.",
                "vi": "Chúng ta nên dũng cảm đi thử sức một lần."
            },
            {
                "num": 38,
                "chunks": ["每个国家", "都有自己的", "文化特点"],
                "ans": "每个国家都有自己的文化特点。",
                "py": "Měi ge guójiā dōu yǒu zìjǐ de wénhuà tèdiǎn.",
                "vi": "Mỗi quốc gia đều có đặc điểm văn hóa riêng của mình."
            },
            {
                "num": 39,
                "chunks": ["真让人难受", "离开老朋友", "要"],
                "ans": "要离开老朋友真让人难受。",
                "py": "Yào líkāi lǎo péngyou zhēn ràng rén nánshòu.",
                "vi": "Phải rời xa bạn bè cũ thật khiến lòng người buồn bã."
            },
            {
                "num": 40,
                "chunks": ["详细地", "这个方案", "分析了", "周经理"],
                "ans": "周经理详细地分析了这个方案。",
                "py": "Zhōu jīnglǐ xiángxì de fēnxī le zhè ge fāng'àn.",
                "vi": "Giám đốc Chu đã phân tích kỹ lưỡng phương án này."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我完全 (xiāngxìn) 你的能力。",
                "pinyin": "xiāngxìn",
                "ans": "相信",
                "vi": "Tôi hoàn toàn tin tưởng năng lực của bạn."
            },
            {
                "num": 42,
                "sentence": "大家都 (tóngyì) 明天去春游。",
                "pinyin": "tóngyì",
                "ans": "同意",
                "vi": "Mọi người đều đồng ý ngày mai đi du xuân."
            },
            {
                "num": 43,
                "sentence": "抓住每一次宝贵的 (jīhuì)。",
                "pinyin": "jīhuì",
                "ans": "机会",
                "vi": "Nắm bắt từng cơ hội quý báu."
            },
            {
                "num": 44,
                "sentence": "中国是一个历史悠久的 (guójiā)。",
                "pinyin": "guójiā",
                "ans": "国家",
                "vi": "Trung Quốc là một quốc gia có lịch sử lâu đời."
            },
            {
                "num": 45,
                "sentence": "这个西瓜真 (tián) 啊！",
                "pinyin": "tián",
                "ans": "甜",
                "vi": "Quả dưa hấu này ngọt thật đấy!"
            }
        ],
        "vocab": [
            {"num": 1, "zh": "相信", "py": "xiāngxìn", "pos": "động từ", "vi": "tin tưởng, tin", "eg": "我相信你一定能做到。"},
            {"num": 2, "zh": "同意", "py": "tóngyì", "pos": "động từ", "vi": "đồng ý, tán thành", "eg": "爸爸同意我买新电脑。"},
            {"num": 3, "zh": "关于", "py": "guānyú", "pos": "giới từ", "vi": "về, liên quan tới", "eg": "关于中国历史的书。"},
            {"num": 4, "zh": "机会", "py": "jīhuì", "pos": "danh từ", "vi": "cơ hội, thời cơ", "eg": "不要错过这个好机会。"},
            {"num": 5, "zh": "国家", "py": "guójiā", "pos": "danh từ", "vi": "quốc gia, đất nước", "eg": "中国是一个美丽的国家。"},
            {"num": 6, "zh": "种", "py": "zhǒng", "pos": "lượng từ", "vi": "loại, dạng", "eg": "这是一种新品种的水果。"},
            {"num": 7, "zh": "特点", "py": "tèdiǎn", "pos": "danh từ", "vi": "đặc điểm, nét đặc sắc", "eg": "北方菜和南方菜有不同的特点。"},
            {"num": 8, "zh": "奇怪", "py": "qíguài", "pos": "tính từ", "vi": "kỳ lạ, quái lạ", "eg": "这件事听起来很奇怪。"},
            {"num": 9, "zh": "地", "py": "de", "pos": "trợ từ kết cấu", "vi": "được đặt sau tính từ/phó từ làm trạng ngữ", "eg": "高兴地笑, 认真地听。"},
            {"num": 10, "zh": "试", "py": "shì", "pos": "động từ", "vi": "thử nghiệm, thử", "eg": "请穿上试一试合适不合适。"},
            {"num": 11, "zh": "甜", "py": "tián", "pos": "tính từ", "vi": "ngọt ngào", "eg": "这个苹果又脆又甜。"},
            {"num": 12, "zh": "简单", "py": "jiǎndān", "pos": "tính từ", "vi": "đơn giản", "eg": "这个问题很不容易，一点儿也不简单。"},
            {"num": 13, "zh": "难受", "py": "nánshòu", "pos": "tính từ", "vi": "khó chịu, đau lòng", "eg": "发烧了浑身难受。"},
            {"num": 14, "zh": "离开", "py": "líkāi", "pos": "động từ", "vi": "rời khỏi, chia tay", "eg": "他依依不舍地离开了学校。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Trợ từ kết cấu “地”: Tính từ / Cụm từ + 地 + Động từ",
                "desc": "Được dùng để liên kết trạng ngữ với động từ vị ngữ trung tâm, miêu tả phương thức hoặc thái độ khi thực hiện hành động.",
                "examples": [
                    {"zh": "小丽高兴地笑了。", "py": "Xiǎolì gāoxìng de xiào le.", "vi": "Tiểu Lệ vui vẻ mỉm cười."},
                    {"zh": "老师认真地看着大家的作业。", "py": "Lǎoshī rènzhēn de kànzhe dàjiā de zuòyè.", "vi": "Thầy giáo chăm chú xem bài tập của mọi người."},
                    {"zh": "大家勇敢地去试一试。", "py": "Dàjiā yǒnggǎn de qù shì yí shì.", "vi": "Mọi người dũng cảm đi thử sức."}
                ]
            },
            {
                "title": "2. Sự lặp lại của động từ (动词重叠: AA / ABAB)",
                "desc": "Biểu thị hành động diễn ra trong thời gian ngắn hoặc mang tính chất thử nghiệm, ngữ khí nhẹ nhàng thoải mái.",
                "examples": [
                    {"zh": "你快来尝尝这个苹果。", "py": "Nǐ kuài lái chángchang zhè ge píngguǒ.", "vi": "Bạn mau lại nếm thử quả táo này đi."},
                    {"zh": "周末我想在家里休息休息。", "py": "Zhōumò wǒ xiǎng zài jiā li xiūxi xiūxi.", "vi": "Cuối tuần tôi muốn ở nhà nghỉ ngơi một chút."}
                ]
            }
        ]
    },

    # ==================== BÀI 19 ====================
    {
        "id": 19,
        "title_zh": "你没看出来吗？",
        "title_py": "Nǐ méi kàn chūlái ma?",
        "title_vi": "Anh không nhận ra à?",
        "dialogues": [
            {
                "title": "Đoạn 1: 看老照片认人 (Xem ảnh cũ nhận người)",
                "location": "在客厅",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "小刚，你看这张老照片，骑马的这个小男孩儿是谁？", "py": "Xiǎogāng, nǐ kàn zhè zhāng lǎo zhàopiàn, qí mǎ de zhè ge xiǎo nánháir shì shéi?", "vi": "Tiểu Cương, anh xem bức ảnh cũ này, cậu bé đang cưỡi ngựa này là ai thế?"},
                    {"speaker": "小刚", "role": "male", "zh": "圆圆的脸，大大的耳朵，难道你没看出来吗？", "py": "Yuányuán de liǎn, dàdà de ěrduo, nándào nǐ méi kàn chūlái ma?", "vi": "Khuôn mặt tròn xoe, đôi tai to tướng, chẳng lẽ em không nhận ra à?"},
                    {"speaker": "小丽", "role": "female", "zh": "天哪，这是你小时候的照片啊！你小时候长得真可爱！", "py": "Tiān na, zhè shì nǐ xiǎoshíhou de zhàopiàn a! Nǐ xiǎoshíhou zhǎng de zhēn kě'ài!", "vi": "Trời ơi, đây là ảnh hồi nhỏ của anh sao! Hồi bé anh trông đáng yêu thật đấy!"},
                    {"speaker": "小刚", "role": "male", "zh": "哈哈，岁月变化真大，现在我都长成大叔了。", "py": "Hāhā, suìyuè biànhuà zhēn dà, xiànzài wǒ dōu zhǎngchéng dàshū le.", "vi": "Haha, năm tháng thay đổi nhiều thật, giờ anh đã thành ông chú mất rồi."}
                ]
            },
            {
                "title": "Đoạn 2: 剪短发 (Cắt tóc ngắn)",
                "location": "在理发店门口",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "小刚，你看我今天有什么变化？", "py": "Xiǎogāng, nǐ kàn wǒ jīntiān yǒu shénme biànhuà?", "vi": "Tiểu Cương, anh nhìn xem hôm nay em có gì khác biệt không?"},
                    {"speaker": "小刚", "role": "male", "zh": "你穿了一条漂亮的蓝裙子。", "py": "Nǐ chuān le yì tiáo piàoliang de lán qúnzi.", "vi": "Em mặc một chiếc váy màu xanh da trời rất đẹp."},
                    {"speaker": "小丽", "role": "female", "zh": "再仔细看，你没看出来我把头发剪短了吗？", "py": "Zài zǐxì kàn, nǐ méi kàn chūlái wǒ bǎ tóufa jiǎnduǎn le ma?", "vi": "Nhìn kỹ lại xem nào, anh không nhận ra em vừa cắt tóc ngắn rồi à?"},
                    {"speaker": "小刚", "role": "male", "zh": "看出来了看出来了！短头发显得特别有活力，真好看！", "py": "Kàn chūlái le kàn chūlái le! Duǎn tóufa xiǎnde tèbié yǒu huólì, zhēn hǎokàn!", "vi": "Anh nhận ra rồi nhận ra rồi! Tóc ngắn trông em tràn đầy sức sống, đẹp lắm em ơi!"}
                ]
            },
            {
                "title": "Đoạn 3: 坐船游黄河 (Đi thuyền ngắm sông Hoàng Hà)",
                "location": "在黄河游船上",
                "lines": [
                    {"speaker": "游客", "role": "male", "zh": "这就是中国母亲河——黄河啊！真壮观！", "py": "Zhè jiù shì Zhōngguó mǔqīnhé——Huáng Hé a! Zhēn zhuàngguān!", "vi": "Đây chính là con sông mẹ của Trung Quốc - sông Hoàng Hà sao! Hùng vĩ quá!"},
                    {"speaker": "导游", "role": "female", "zh": "是的，秋天是游览黄河最好的季节，凉风习习，鸟儿在天空中飞。", "py": "Shì de, qiūtiān shì yóulǎn Huáng Hé zuì hǎo de jìjié, liángfēng xíxí, niǎor zài tiānkōng zhōng fēi.", "vi": "Đúng thế ạ, mùa thu là mùa đẹp nhất để du ngoạn Hoàng Hà, gió mát hiu hiu, chim chóc bay lượn trên bầu trời."},
                    {"speaker": "游客", "role": "male", "zh": "我们坐船经过前面那座大桥需要多长时间？", "py": "Wǒmen zuò chuán jīngguò qiánmiàn nà zuò dàqiáo xūyào duō cháng shíjiān?", "vi": "Chúng ta đi thuyền qua cây cầu lớn phía trước mất bao lâu ạ?"},
                    {"speaker": "导游", "role": "female", "zh": "大概十分钟左右，大家可以拿出手机拍照留念。", "py": "Dàgài shí fēnzhōng zuǒyòu, dàjiā kěyǐ ná chū shǒujī pāizhào liúniàn.", "vi": "Khoảng 10 phút thôi ạ, mọi người có thể lấy điện thoại ra chụp ảnh kỷ niệm."}
                ]
            },
            {
                "title": "Đoạn 4: 经过老学校 (Đi ngang qua ngôi trường cũ)",
                "location": "在校门口",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "你看，前面是我们十年前读过的中学。", "py": "Nǐ kàn, qiánmiàn shì wǒmen shí nián qián dú guo de zhōngxué.", "vi": "Em nhìn kìa, phía trước là ngôi trường cấp hai chúng mình từng học mười năm trước."},
                    {"speaker": "小丽", "role": "female", "zh": "学校建起了新教学楼，操场也变大了，我差点儿没认出来！", "py": "Xuéxiào jiàn qǐ le xīn jiàoxuélóu, cāochǎng yě biàn dà le, wǒ chàdiǎnr méi rèn chūlái!", "vi": "Trường đã xây thêm dãy phòng học mới, sân trường cũng rộng hơn, em suýt chút nữa không nhận ra!"},
                    {"speaker": "小刚", "role": "male", "zh": "时间过得真快，过去的记忆又在脑海里浮现出来了。", "py": "Shíjiān guò de zhēn kuài, guòqù de jìyì yòu zài nǎohǎi li fúxiàn chūlái le.", "vi": "Thời gian trôi nhanh thật, ký ức xưa lại hiện về trong tâm trí anh rồi."},
                    {"speaker": "小丽", "role": "female", "zh": "真想走进去看看我们以前的教室啊。", "py": "Zhēn xiǎng zǒu jìnqù kànkan wǒmen yǐqián de jiàoshì a.", "vi": "Thực sự muốn bước vào xem lại lớp học ngày xưa của chúng mình quá."}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你看照片里骑马的小孩儿是谁？ 男：圆圆的脸，大大的耳朵，难道你没看出来是我吗？",
                "question": "照片里的人是谁？",
                "options": ["A. 男的小时候", "B. 女的弟弟", "C. 男的朋友"],
                "ans": "A",
                "explain": "Người nam trả lời: 难道你没看出来是我吗 (chẳng lẽ em không nhận ra là anh sao)."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "小丽今天穿了蓝裙子，还把长头发剪短了，显得特别有活力。",
                "question": "Phán đoán đúng hay sai: 小丽把头发剪短了。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Đúng (√)",
                "explain": "Đoạn văn nói rõ: 把头发剪短了."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "男：现在秋天坐船游黄河真舒服。 女：是啊，凉风吹着，天空中还有很多小鸟在飞。",
                "question": "他们现在在做什么？",
                "options": ["A. 爬山", "B. 坐船游黄河", "C. 坐飞机"],
                "ans": "B",
                "explain": "Họ đang đi thuyền trên sông Hoàng Hà (坐船游黄河)."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：学校变化真大，我差点儿没认出来。 男：是啊，盖了新楼，操场也更宽了。",
                "question": "学校有什么变化？",
                "options": ["A. 搬走了", "B. 盖了新楼，操场变大", "C. 学生变少了"],
                "ans": "B",
                "explain": "Đoạn thoại nhắc: 盖了新楼，操场也更宽了."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "圆圆的脸，大大的耳朵，你没看出来这是我小时候吗？", "py": "Yuányuán de liǎn, dàdà de ěrduo, nǐ méi kàn chūlái zhè shì wǒ xiǎoshíhou ma?", "vi": "Mặt tròn xoe, tai to tướng, bạn không nhận ra đây là tôi hồi nhỏ à?"},
                {"id": "B", "text": "她剪了短发，换上了蓝裙子，整个人精神极了。", "py": "Tā jiǎn le duǎnfà, huàn shàng le lán qúnzi, zhěng ge rén jīngshen jí le.", "vi": "Cô ấy cắt tóc ngắn, thay chiếc váy xanh, trông cả người tràn đầy sức sống."},
                {"id": "C", "text": "秋天坐船游黄河，风景特别美丽壮观。", "py": "Qiūtiān zuò chuán yóu Huáng Hé, fēngjǐng tèbié měilì zhuàngguān.", "vi": "Mùa thu đi thuyền du ngoạn sông Hoàng Hà, phong cảnh vô cùng tươi đẹp hùng vĩ."},
                {"id": "D", "text": "十年没见，母校建起了现代化新教学楼。", "py": "Shí nián méi jiàn, mǔxiào jiàn qǐ le xiàndàihuà xīn jiàoxuélóu.", "vi": "Mười năm không gặp, trường cũ đã xây lên tòa nhà học hiện đại mới."},
                {"id": "E", "text": "蓝天白云下，小鸟在天空中自由地飞翔。", "py": "Lántiān bái yún xià, xiǎoniǎo zài tiānkōng zhōng zìyóu de fēixiáng.", "vi": "Dưới bầu trời xanh mây trắng, đàn chim nhỏ tự do bay lượn trên không trung."}
            ],
            "questions": [
                {"num": 21, "text": "这张发黄的照片上是谁呀？", "py": "Zhè zhāng fāhuáng de zhàopiàn shang shì shéi ya?", "vi": "Trên bức ảnh ngả vàng này là ai thế nhỉ?", "ans": "A", "explain": "Nhận ra hình ảnh thuở bé mặt tròn tai to."},
                {"num": 22, "text": "小丽今天给人的感觉怎么不一样了？", "py": "Xiǎolì jīntiān gěi rén de gǎnjué zěnme bù yíyàng le?", "vi": "Tiểu Lệ hôm nay mang lại cảm giác sao khác thế?", "ans": "B", "explain": "Nhờ cắt tóc ngắn và mặc váy xanh tràn đầy năng lượng."},
                {"num": 23, "text": "国庆假期去哪里旅游最惬意？", "py": "Guóqìng jiàqī qù nǎlǐ lǚyóu zuì qièyì?", "vi": "Kỳ nghỉ Quốc khánh đi đâu du lịch thú vị nhất?", "ans": "C", "explain": "Khuyên đi thuyền ngắm sông Hoàng Hà vào mùa thu."},
                {"num": 24, "text": "听说你们中学这几年变化非常大？", "py": "Tīngshuō nǐmen zhōngxué zhè jǐ nián biànhuà fēicháng dà?", "vi": "Nghe nói trường cấp hai của các bạn mấy năm nay thay đổi dữ lắm?", "ans": "D", "explain": "Trường đã xây thêm dãy nhà học hiện đại mới."},
                {"num": 25, "text": "抬头看看秋天的天空，感觉真好！", "py": "Táitóu kànkan qiūtiān de tiānkōng, gǎnjué zhēn hǎo!", "vi": "Ngẩng đầu ngắm nhìn bầu trời mùa thu, cảm giác thật tuyệt!", "ans": "E", "explain": "Ngắm chim bay dưới trời xanh mây trắng."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "耳朵", "py": "ěrduo", "vi": "cái tai, tai"},
                {"id": "B", "zh": "短", "py": "duǎn", "vi": "ngắn"},
                {"id": "C", "zh": "蓝", "py": "lán", "vi": "xanh da trời, xanh lam"},
                {"id": "D", "zh": "船", "py": "chuán", "vi": "thuyền, tàu"},
                {"id": "E", "zh": "经过", "py": "jīngguò", "vi": "đi qua, trải qua"}
            ],
            "questions": [
                {"num": 26, "prefix": "小兔子的两只", "suffix": "长长的，立在头上。", "py": "Xiǎo tùzi de liǎng zhī ( ? ) chángcháng de, lì zài tóu shang.", "vi": "Hai chiếc ( ? ) của chú thỏ con dài dài, dựng đứng trên đầu.", "ans": "A", "word": "耳朵", "explain": "Cái tai: 耳朵 (ěrduo)."},
                {"num": 27, "prefix": "夏天天气热，很多人喜欢剪", "suffix": "头发。", "py": "Xiàtiān tiānqì rè, hěn duō rén xǐhuan jiǎn ( ? ) tóufa.", "vi": "Mùa hè thời tiết nóng, nhiều người thích cắt tóc ( ? ).", "ans": "B", "word": "短", "explain": "Tóc ngắn: 短头发 (duǎn tóufa)."},
                {"num": 28, "prefix": "晴朗的天空像大海一样", "suffix": "。", "py": "Qínglǎng de tiānkōng xiàng dàhǎi yíyàng ( ? ).", "vi": "Bầu trời trong xanh như biển cả vậy.", "ans": "C", "word": "蓝", "explain": "Màu xanh da trời: 蓝 (lán)."},
                {"num": 29, "prefix": "我们坐着大游", "suffix": "在湖面上看风景。", "py": "Wǒmen zuòzhe dà yóu ( ? ) zài húmiàn shang kàn fēngjǐng.", "vi": "Chúng tôi ngồi trên du ( ? ) lớn ngắm cảnh trên mặt hồ.", "ans": "D", "word": "船", "explain": "Du thuyền: 游船 (yóuchuán)."},
                {"num": 30, "prefix": "每天上班我都要", "suffix": "人民公园。", "py": "Měitiān shàngbān wǒ dōu yào ( ? ) Rénmín Gōngyuán.", "vi": "Mỗi ngày đi làm tôi đều phải ( ? ) công viên Nhân Dân.", "ans": "E", "word": "经过", "explain": "Đi qua: 经过 (jīngguò)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "秋天到了，天气变得越来越凉快。树叶慢慢变黄了，天空中偶尔飞过几只小鸟。周末，大山和小刚相约一起去黄河边游玩。黄河是中国第二长河，气势十分宏大。他们买了两张船票，坐上游船沿着黄河顺流而下。小刚指着远处的一座红色大桥说：“看，我们马上就要经过黄河大桥了！”大山拿出手机，拍下了蓝天、黄河和壮观的大桥。站在船头吹着微风，大山感叹道：“中国的风景真是一幅美丽动人的画卷！”",
            "passage_py": "Qiūtiān dào le, tiānqì biàn de yuè lái yuè liángkuai. Shùyè mànmàn biàn huáng le, tiānkōng zhōng ǒu'ěr fēiguò jǐ zhī xiǎoniǎo. Zhōumò, Dàshān hé Xiǎogāng xiāngyuē yìqǐ qù Huáng Hé biān yóuwán. Huáng Hé shì Zhōngguó dì-èr cháng hé, qìshì shífēn hóngdà. Tāmen mǎi le liǎng zhāng chuánpiào, zuò shàng yóuchuán yánzhe Huáng Hé shùnliú ér xià. Xiǎogāng zhǐzhe yuǎnchù de yí zuò hóngsè dàqiáo shuō: 'Kàn, wǒmen mǎshàng jiù yào jīngguò Huáng Hé dàqiáo le!' Dàshān ná chū shǒujī, pāixià le lántiān, Huáng Hé hé zhuàngguān de dàqiáo. Zhàn zài chuántóu chuīzhe wēifēng, Dàshān gǎntàn dào: 'Zhōngguó de fēngjǐng zhēn shì yì fú měilì dòngrén de huàjuàn!'",
            "passage_vi": "Mùa thu đến rồi, thời tiết trở nên ngày một mát mẻ. Lá cây dần dần ngả vàng, trên nền trời thi thoảng có vài cánh chim nhỏ bay qua. Cuối tuần, Đại Sơn và Tiểu Cương hẹn nhau cùng đến bên bờ sông Hoàng Hà dạo chơi. Hoàng Hà là con sông dài thứ hai của Trung Quốc, khí thế vô cùng hùng vĩ. Họ mua hai vé tàu thủy, bước lên du thuyền xuôi theo dòng nước Hoàng Hà. Tiểu Cương chỉ vào cây cầu lớn màu đỏ ở phía xa bảo: 'Xem kìa, chúng mình sắp đi qua cầu Hoàng Hà rồi đấy!' Đại Sơn lấy điện thoại ra, chụp lại bầu trời xanh, dòng sông Hoàng Hà và cây cầu lớn tráng lệ. Đứng ở mũi thuyền đón từng làn gió nhẹ, Đại Sơn cảm thán thốt lên: 'Phong cảnh của Trung Quốc thật đúng là một bức tranh thủy mặc đẹp lay động lòng người!'",
            "questions": [
                {
                    "num": 31,
                    "text": "大山和小刚周末去了哪儿？",
                    "options": ["A. 去爬长城", "B. 去黄河边游玩", "C. 去故宫博物馆"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 去黄河边游玩."
                },
                {
                    "num": 32,
                    "text": "黄河在中国的河流中排名第几？",
                    "options": ["A. 第一长河", "B. 第二长河", "C. 第三长河"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 黄河是中国第二长河."
                },
                {
                    "num": 33,
                    "text": "他们是怎么游览黄河的？",
                    "options": ["A. 走路", "B. 骑自行车", "C. 坐游船"],
                    "ans": "C",
                    "explain": "Đoạn văn viết: 买了两张船票，坐上游船."
                },
                {
                    "num": 34,
                    "text": "游船马上就要经过什么地方？",
                    "options": ["A. 黄河大桥", "B. 一个小岛", "C. 一座高山"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 马上就要经过黄河大桥了."
                },
                {
                    "num": 35,
                    "text": "大山觉得中国的风景怎么样？",
                    "options": ["A. 一般般", "B. 像一幅美丽动人的画卷", "C. 很让人害怕"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 中国的风景真是一幅美丽动人的画卷."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["难道你", "没看出来吗", "这是我小时候"],
                "ans": "难道你没看出来吗？这是我小时候。",
                "py": "Nándào nǐ méi kàn chūlái ma? Zhè shì wǒ xiǎoshíhou.",
                "vi": "Chẳng lẽ bạn không nhận ra à? Đây là tôi hồi nhỏ đấy."
            },
            {
                "num": 37,
                "chunks": ["显得特别年轻", "把头发剪短了", "她"],
                "ans": "她把头发剪短了，显得特别年轻。",
                "py": "Tā bǎ tóufa jiǎnduǎn le, xiǎnde tèbié niánqīng.",
                "vi": "Cô ấy cắt tóc ngắn rồi, trông trẻ trung hẳn ra."
            },
            {
                "num": 38,
                "chunks": ["坐船经过", "我们马上要", "黄河大桥"],
                "ans": "我们马上要坐船经过黄河大桥。",
                "py": "Wǒmen mǎshàng yào zuò chuán jīngguò Huáng Hé dàqiáo.",
                "vi": "Chúng tôi sắp sửa ngồi thuyền đi qua cầu Hoàng Hà."
            },
            {
                "num": 39,
                "chunks": ["自由地飞翔", "在蓝天白云下", "小鸟"],
                "ans": "小鸟在蓝天白云下自由地飞翔。",
                "py": "Xiǎoniǎo zài lántiān bái yún xià zìyóu de fēixiáng.",
                "vi": "Đàn chim tự do bay lượn dưới bầu trời xanh mây trắng."
            },
            {
                "num": 40,
                "chunks": ["建起了新大楼", "十年后", "母校"],
                "ans": "十年后母校建起了新大楼。",
                "py": "Shí nián hòu mǔxiào jiàn qǐ le xīn dàlóu.",
                "vi": "Mười năm sau trường cũ đã xây lên tòa nhà mới."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "小兔子的 (ěrduo) 很长。",
                "pinyin": "ěrduo",
                "ans": "耳朵",
                "vi": "Tai của thỏ con rất dài."
            },
            {
                "num": 42,
                "sentence": "她洗完 (liǎn) 涂了护肤品。",
                "pinyin": "liǎn",
                "ans": "脸",
                "vi": "Cô ấy rửa mặt xong thoa kem dưỡng da."
            },
            {
                "num": 43,
                "sentence": "我穿了一条 (lán) 色的裙子。",
                "pinyin": "lán",
                "ans": "蓝",
                "vi": "Tôi đã mặc một chiếc váy màu xanh da trời."
            },
            {
                "num": 44,
                "sentence": "夏天很多人喜欢坐 (chuán) 游湖。",
                "pinyin": "chuán",
                "ans": "船",
                "vi": "Mùa hè nhiều người thích ngồi thuyền dạo hồ."
            },
            {
                "num": 45,
                "sentence": "秋天到了，树叶变 (huáng) 了。",
                "pinyin": "huáng",
                "ans": "黄",
                "vi": "Mùa thu đến rồi, lá cây ngả vàng rồi."
            }
        ],
        "vocab": [
            {"num": 1, "zh": "会", "py": "huì", "pos": "động từ năng nguyện", "vi": "biết, có thể, sẽ", "eg": "明天会下雨吗？"},
            {"num": 2, "zh": "耳朵", "py": "ěrduo", "pos": "danh từ", "vi": "tai, cái tai", "eg": "我的耳朵冻得发红。"},
            {"num": 3, "zh": "脸", "py": "liǎn", "pos": "danh từ", "vi": "khuôn mặt, mặt", "eg": "小姑娘洗得干干净净的小脸。"},
            {"num": 4, "zh": "短", "py": "duǎn", "pos": "tính từ", "vi": "ngắn", "eg": "这件衣服有点儿短。"},
            {"num": 5, "zh": "马", "py": "mǎ", "pos": "danh từ", "vi": "con ngựa", "eg": "草原上有一群奔跑的马。"},
            {"num": 6, "zh": "张", "py": "zhāng", "pos": "lượng từ", "vi": "tấm, tờ, chiếc (mặt phẳng)", "eg": "一张照片, 一张地图。"},
            {"num": 7, "zh": "位", "py": "wèi", "pos": "lượng từ lịch sự", "vi": "vị (người)", "eg": "这位老师非常认真。"},
            {"num": 8, "zh": "蓝", "py": "lán", "pos": "tính từ", "vi": "màu xanh da trời, xanh lam", "eg": "蓝蓝的天空上飘着白云。"},
            {"num": 9, "zh": "秋(天)", "py": "qiū (tiān)", "pos": "danh từ", "vi": "mùa thu", "eg": "北京的秋天最美丽。"},
            {"num": 10, "zh": "鸟", "py": "niǎo", "pos": "danh từ", "vi": "con chim", "eg": "树上有许多小鸟在唱歌。"},
            {"num": 11, "zh": "黄河", "py": "Huáng Hé", "pos": "danh từ riêng", "vi": "sông Hoàng Hà", "eg": "黄河是中国的母亲河。"},
            {"num": 12, "zh": "船", "py": "chuán", "pos": "danh từ", "vi": "thuyền, tàu thủy", "eg": "我们坐船游览江景。"},
            {"num": 13, "zh": "经过", "py": "jīngguò", "pos": "động từ/giới từ", "vi": "đi qua, trải qua, qua", "eg": "经过努力，他终于学会了开车。"}
        ],
        "proper_nouns": [
            {"zh": "黄河", "py": "Huáng Hé", "vi": "Hoàng Hà (con sông lớn ở Trung Quốc)"}
        ],
        "grammar": [
            {
                "title": "1. Bổ ngữ xu hướng kép với nghĩa chuyển tiếp: “出来”",
                "desc": "Được dùng sau các động từ như 看, 听, 闻, 想... để biểu thị sự nhận biết, nhận ra hoặc phát hiện ra một sự vật, hiện tượng thông qua tri giác hoặc suy nghĩ.",
                "examples": [
                    {"zh": "你没看出来这是我小时候吗？", "py": "Nǐ méi kàn chūlái zhè shì wǒ xiǎoshíhou ma?", "vi": "Bạn không nhìn nhận ra đây là tôi hồi nhỏ à?"},
                    {"zh": "我听出来了，这是周老师的声音。", "py": "Wǒ tīng chūlái le, zhè shì Zhōu lǎoshī de shēngyīn.", "vi": "Tôi nghe nhận ra rồi, đây là giọng của thầy Chu."},
                    {"zh": "他终于想出办法来了。", "py": "Tā zhōngyú xiǎng chū bànfǎ lái le.", "vi": "Anh ấy cuối cùng đã nghĩ ra được cách rồi."}
                ]
            },
            {
                "title": "2. Câu hỏi tu từ với “没……吗？”",
                "desc": "Hình thức nghi vấn phủ định dùng để nhấn mạnh hoặc nhắc nhở đối phương về một sự việc hiển nhiên.",
                "examples": [
                    {"zh": "你没看见我正在忙吗？", "py": "Nǐ méi kànjiàn wǒ zhèngzài máng ma?", "vi": "Cậu không nhìn thấy tớ đang bận à?"},
                    {"zh": "你没听明白老师的话吗？", "py": "Nǐ méi tīng míngbai lǎoshī de huà ma?", "vi": "Cậu không nghe hiểu lời thầy giáo nói sao?"}
                ]
            }
        ]
    },

    # ==================== BÀI 20 ====================
    {
        "id": 20,
        "title_zh": "我被他影响了。",
        "title_py": "Wǒ bèi tā yǐngxiǎng le.",
        "title_vi": "Mình chịu ảnh hưởng từ anh ấy.",
        "dialogues": [
            {
                "title": "Đoạn 1: 谈运动习惯 (Nói về thói quen thể thao)",
                "location": "在体育馆",
                "lines": [
                    {"speaker": "小丽", "role": "female", "zh": "你怎么突然喜欢上游泳了？以前你不是最讨厌水吗？", "py": "Nǐ zěnme tūrán xǐhuan shàng yóuyǒng le? Yǐqián nǐ bú shì zuì tǎoyàn shuǐ ma?", "vi": "Sao anh đột nhiên lại mê bơi lội thế? Trước đây anh chẳng phải ghét nước nhất sao?"},
                    {"speaker": "小刚", "role": "male", "zh": "我被我的新室友影响了，他每天早晨都去游泳。", "py": "Wǒ bèi wǒ de xīn shìyǒu yǐngxiǎng le, tā měitiān zǎochén dōu qù yóuyǒng.", "vi": "Anh bị cậu bạn cùng phòng mới ảnh hưởng đấy, sáng nào cậu ấy cũng đi bơi."},
                    {"speaker": "小丽", "role": "female", "zh": "坚持游泳对身体确实很好，你看你精神多了！", "py": "Jiānchí yóuyǒng duì shēntǐ quèshí hěn hǎo, nǐ kàn nǐ jīngshen duō le!", "vi": "Kiên trì bơi lội đối với sức khỏe quả thực rất tốt, anh xem anh phong độ hẳn ra!"},
                    {"speaker": "小刚", "role": "male", "zh": "受到他的影响，我也养成了早睡早起的好习惯。", "py": "Shòudào tā de yǐngxiǎng, wǒ yě yǎngchéng le zǎoshuì-zǎoqǐ de hǎo xíguàn.", "vi": "Chịu ảnh hưởng từ cậu ấy, anh cũng hình thành được thói quen tốt ngủ sớm dậy sớm."}
                ]
            },
            {
                "title": "Đoạn 2: 足球比赛 (Trận đấu bóng đá)",
                "location": "在足球场",
                "lines": [
                    {"speaker": "同学A", "role": "male", "zh": "昨天的足球比赛，你们班赢了吗？", "py": "Zuótiān de zúqiú bǐsài, nǐmen bān yíng le ma?", "vi": "Trận bóng đá hôm qua, lớp cậu có thắng không?"},
                    {"speaker": "同学B", "role": "male", "zh": "别提了，最后五分钟我们的球门被对方踢进了一个球。", "py": "Biétí le, zuìhòu wǔ fēnzhōng wǒmen de qiúmén bèi duìfāng tī jìn le yí ge qiú.", "vi": "Đừng nhắc nữa, 5 phút cuối cầu môn bên tớ bị đối phương sút thủng lưới một bàn."},
                    {"speaker": "同学A", "role": "male", "zh": "那太可惜了！大家都很伤心吧？", "py": "Nà tài kěxī le! Dàjiā dōu hěn shāngxīn ba?", "vi": "Thế thì đáng tiếc quá! Mọi người đều buồn lắm nhỉ?"},
                    {"speaker": "同学B", "role": "male", "zh": "虽然有点儿难过，但是大家都努力了，下次比赛再争取赢回来！", "py": "Suīrán yǒudiǎnr nánguò, dànshì dàjiā dōu nǔlì le, xià cì bǐsài zài zhēngqǔ yíng huílái!", "vi": "Tuy có chút buồn, nhưng mọi người đều đã nỗ lực hết mình, trận đấu sau sẽ cố gắng thắng lại!"}
                ]
            },
            {
                "title": "Đoạn 3: 骑自行车去郊外 (Đạp xe đi ngoại ô)",
                "location": "在郊外绿道",
                "lines": [
                    {"speaker": "小刚", "role": "male", "zh": "骑自行车出来吹吹风，心情真好。", "py": "Qí zìxíngchē chūlái chuīchuifēng, xīnqíng zhēn hǎo.", "vi": "Đạp xe ra ngoài hóng gió mát, tâm trạng thật tuyệt."},
                    {"speaker": "小丽", "role": "female", "zh": "是啊，平时整天在电脑前坐着，人都被电脑‘绑架’了。", "py": "Shì a, píngshí zhěng tiān zài diànnǎo qián zuòzhe, rén dōu bèi diànnǎo 'bǎngjià' le.", "vi": "Đúng thế, bình thường cả ngày ngồi trước máy tính, người ta như bị máy tính 'bắt cóc' vậy."},
                    {"speaker": "小刚", "role": "male", "zh": "多亲近大自然，呼吸新鲜空气，整个人都轻松了。", "py": "Duō qīnjìn dàzìrán, hūxī xīnxiān kōngqì, zhěng ge rén dōu qīngsōng le.", "vi": "Gần gũi thiên nhiên nhiều hơn, hít thở không khí trong lành, cả con người đều thư thái hẳn."},
                    {"speaker": "小丽", "role": "female", "zh": "走，我们骑到前面的湖边去跑步！", "py": "Zǒu, wǒmen qí dào qiánmiàn de húbiān qù pǎobù!", "vi": "Đi thôi, chúng mình đạp đến bờ hồ phía trước rồi chạy bộ nhé!"}
                ]
            },
            {
                "title": "Đoạn 4: 总结HSK 3与未来 (Tổng kết HSK 3 và tương lai)",
                "location": "在结业典礼上",
                "lines": [
                    {"speaker": "老师", "role": "female", "zh": "祝贺大家！今天我们学完了HSK三级的全部二十课！", "py": "Zhùhè dàjiā! Jīntiān wǒmen xuéwán le HSK sān jí de quánbù èrshí kè!", "vi": "Chúc mừng tất cả các em! Hôm nay chúng ta đã học xong toàn bộ 20 bài của HSK cấp 3!"},
                    {"speaker": "学生们", "role": "female", "zh": "谢谢老师！这几个月我们被老师的敬业精神深深打动了。", "py": "Xièxie lǎoshī! Zhè jǐ ge yuè wǒmen bèi lǎoshī de jìngyè jīngshén shēnshēn dǎdòng le.", "vi": "Cảm ơn cô giáo ạ! Mấy tháng qua chúng em đã được tinh thần tận tụy yêu nghề của cô làm lay động sâu sắc."},
                    {"speaker": "老师", "role": "female", "zh": "只要坚持努力，大家在未来的汉语学习中一定能取得更大的成功！", "py": "Zhǐyào jiānchí nǔlì, dàjiā zài wèilái de hànyǔ xuéxí zhōng yídìng néng qǔdé gèng dà de chénggōng!", "vi": "Chỉ cần kiên trì nỗ lực, các em trong chặng đường học tiếng Hán tương lai nhất định sẽ gặt hái thành công lớn hơn nữa!"},
                    {"speaker": "学生们", "role": "male", "zh": "我们一定继续加油，向HSK四级出发！", "py": "Wǒmen yídìng jìxù jiāyóu, xiàng HSK sì jí chūfā!", "vi": "Chúng em nhất định tiếp tục cố gắng, tiến bước chinh phục HSK 4 ạ!"}
                ]
            }
        ],
        "listening_quiz": [
            {
                "num": 1,
                "type": "dialogue",
                "audio_script": "女：你以前不喜欢运动，现在怎么天天跑步？ 男：我被新室友影响了，他是一个长跑运动员。",
                "question": "男的为什么现在天天跑步？",
                "options": ["A. 他想减肥", "B. 他被室友影响了", "C. 他要参加比赛"],
                "ans": "B",
                "explain": "Người nam trả lời: 我被新室友影响了."
            },
            {
                "num": 2,
                "type": "true_false",
                "audio_script": "在昨天的足球比赛中，小刚他们班赢了对方三个球。",
                "question": "Phán đoán đúng hay sai: 小刚他们班赢了昨天的比赛。",
                "options": ["Đúng (√)", "Sai (×)"],
                "ans": "Sai (×)",
                "explain": "Đoạn thoại kể lớp Tiểu Cương bị thủng lưới phút cuối và thua cuộc (踢进了一个球，输了)."
            },
            {
                "num": 3,
                "type": "dialogue",
                "audio_script": "女：骑自行车去郊外感觉怎么样？ 男：空气特别新鲜，心情好极了。",
                "question": "男的觉得去郊外骑车怎么样？",
                "options": ["A. 太累了", "B. 心情好极了", "C. 路上太堵"],
                "ans": "B",
                "explain": "Người nam nói: 心情好极了."
            },
            {
                "num": 4,
                "type": "dialogue",
                "audio_script": "女：祝贺大家学完了HSK三级全部二十课！ 男：谢谢老师，我们打算继续考HSK四级。",
                "question": "学生们接下来的目标是什么？",
                "options": ["A. 停止学习", "B. 考HSK四级", "C. 去外地工作"],
                "ans": "B",
                "explain": "Học sinh nói: 我们打算继续考HSK四级."
            }
        ],
        "reading_p1": {
            "options": [
                {"id": "A", "text": "受到他的影响，我也养成了天天晨练的好习惯。", "py": "Shòudào tā de yǐngxiǎng, wǒ yě yǎngchéng le tiāntiān chénliàn de hǎo xíguàn.", "vi": "Chịu ảnh hưởng từ anh ấy, tôi cũng hình thành thói quen tốt tập thể dục buổi sáng hằng ngày."},
                {"id": "B", "text": "比赛虽然输了，但大家都努力拼搏了。", "py": "Bǐsài suīrán shū le, dàn dàjiā dōu nǔlì pīnbó le.", "vi": "Trận đấu tuy thua nhưng mọi người đều đã nỗ lực hết mình."},
                {"id": "C", "text": "骑自行车去郊外呼吸新鲜空气，感觉真放松。", "py": "Qí zìxíngchē qù jiāowài hūxī xīnxiān kōngqì, gǎnjué zhēn fàngsōng.", "vi": "Đạp xe ra ngoại ô hít thở không khí trong lành, cảm giác thật thư giãn."},
                {"id": "D", "text": "只要坚持下去，我们一定能取得最后的成功。", "py": "Zhǐyào jiānchí xiàqù, wǒmen yídìng néng qǔdé zuìhòu de chénggōng.", "vi": "Chỉ cần kiên trì tới cùng, chúng ta nhất định có thể giành được thành công cuối cùng."},
                {"id": "E", "text": "我的钱包在公共汽车上被小偷偷走了。", "py": "Wǒ de qiánbāo zài gōnggòng qìchē shang bèi xiǎotōu tōuzǒu le.", "vi": "Ví tiền của tôi bị kẻ trộm lấy mất trên xe buýt rồi."}
            ],
            "questions": [
                {"num": 21, "text": "你以前不是个夜猫子吗？怎么现在起这么早？", "py": "Nǐ yǐqián bú shì ge yèmāozi ma? Zěnme xiànzài qǐ zhème zǎo?", "vi": "Trước đây cậu chẳng phải là cú đêm sao? Sao giờ dậy sớm thế?", "ans": "A", "explain": "Chịu ảnh hưởng từ người khác nên có thói quen dậy sớm."},
                {"num": 22, "text": "昨天的拔河比赛你们班成绩怎么样？", "py": "Zuótiān de báhé bǐsài nǐmen bān chéngjì zěnmeyàng?", "vi": "Cuộc thi kéo co hôm qua lớp bạn kết quả thế nào?", "ans": "B", "explain": "Tuy thua nhưng mọi người đều đã nỗ lực."},
                {"num": 23, "text": "周末你打算怎么放松一下紧张的心情？", "py": "Zhōumò nǐ dǎsuàn zěnme fàngsōng yíxià jǐnzhāng de xīnqíng?", "vi": "Cuối tuần bạn định thư giãn tâm trạng căng thẳng thế nào?", "ans": "C", "explain": "Đạp xe ra ngoại ô hít thở không khí trong lành."},
                {"num": 24, "text": "学好一门外语需要付出很多汗水，你害怕吗？", "py": "Xuéhǎo yì mén wàiyǔ xūyào fùchū hěn duō hànshuǐ, nǐ hàipà ma?", "vi": "Học giỏi một ngoại ngữ cần bỏ ra nhiều mồ hôi công sức, bạn có sợ không?", "ans": "D", "explain": "Khẳng định kiên trì ắt sẽ gặt hái thành công."},
                {"num": 25, "text": "你怎么站在路边着急地打电话报警啊？", "py": "Nǐ zěnme zhàn zài lùbiān zháojí de dǎ diànhuà bàojǐng a?", "vi": "Sao cậu đứng bên đường sốt ruột gọi điện thoại báo cảnh sát thế?", "ans": "E", "explain": "Ví tiền bị kẻ gian lấy trộm trên xe buýt."}
            ]
        },
        "reading_p2": {
            "words": [
                {"id": "A", "zh": "被", "py": "bèi", "vi": "bị, được (câu bị động)"},
                {"id": "B", "zh": "游泳", "py": "yóuyǒng", "vi": "bơi lội"},
                {"id": "C", "zh": "难过", "py": "nánguò", "vi": "buồn bã, đau lòng"},
                {"id": "D", "zh": "努力", "py": "nǔlì", "vi": "nỗ lực, cố gắng"},
                {"id": "E", "zh": "成功", "py": "chénggōng", "vi": "thành công"}
            ],
            "questions": [
                {"num": 26, "prefix": "桌子上的蛋糕", "suffix": "弟弟吃光了。", "py": "Zhuōzi shang de dàngāo ( ? ) dìdi chīguāng le.", "vi": "Bánh ngọt trên bàn ( ? ) em trai ăn hết sạch rồi.", "ans": "A", "word": "被", "explain": "Câu bị động: 被弟弟吃光了."},
                {"num": 27, "prefix": "夏天去海边", "suffix": "是最舒服的运动。", "py": "Xiàtiān qù hǎibiān ( ? ) shì zuì shūfu de yùndòng.", "vi": "Mùa hè ra biển ( ? ) là môn thể thao sảng khoái nhất.", "ans": "B", "word": "游泳", "explain": "Bơi lội: 游泳 (yóuyǒng)."},
                {"num": 28, "prefix": "没考好不要太", "suffix": "，下次再继续加油。", "py": "Méi kǎohǎo bú yào tài ( ? ), xià cì zài jìxù jiāyóu.", "vi": "Thi chưa tốt đừng quá ( ? ), lần sau tiếp tục cố gắng.", "ans": "C", "word": "难过", "explain": "Buồn bã: 难过 (nánguò)."},
                {"num": 29, "prefix": "只要我们坚持", "suffix": "，梦想就一定会实现。", "py": "Zhǐyào wǒmen jiānchí ( ? ), mèngxiǎng jiù yídìng huì shíxiàn.", "vi": "Chỉ cần chúng ta kiên trì ( ? ), ước mơ nhất định sẽ thành hiện thực.", "ans": "D", "word": "努力", "explain": "Nỗ lực: 努力 (nǔlì)."},
                {"num": 30, "prefix": "经过五年的奋斗，他终于取得了事业的", "suffix": "。", "py": "Jīngguò wǔ nián de fèndòu, tā zhōngyú qǔdé le shìyè de ( ? ).", "vi": "Trải qua 5 năm phấn đấu, cuối cùng anh ấy đã gặt hái ( ? ) trong sự nghiệp.", "ans": "E", "word": "成功", "explain": "Thành công: 成功 (chénggōng)."}
            ]
        },
        "reading_p3": {
            "passage_zh": "学习一门外语就像攀登一座高山。刚开始的时候，很多人觉得汉字很难写，发音很难读。但在学完HSK三级的这二十课之后，你会发现自己的汉语水平有了巨大的进步。我们学会了用‘把’字句安排事情，用‘被’字句表达被动，还会用各种补语把话说得更准确、更生动。学习过程中，你可能会被优秀的老师和热情的同学所影响，养成每天读中文的好习惯。只要保持这份对中文的热爱与坚持，未来在HSK四级、五级甚至更高的水平测试中，你一定能取得更大的成功！",
            "passage_py": "Xuéxí yì mén wàiyǔ jiù xiàng pāndēng yí zuò gāoshān. Gāng kāishǐ de shíhou, hěn duō rén juéde hànzì hěn nán xiě, fāyīn hěn nán dú. Dàn zài xuéwán HSK sān jí de zhè èrshí kè zhīhòu, nǐ huì fāxiàn zìjǐ de hànyǔ shuǐpíng yǒu le jùdà de jìnbù. Wǒmen xuéhuì le yòng 'bǎ' zìjù ānpái shìqing, yòng 'bèi' zìjù biǎodá bèidòng, hái huì yòng gè zhǒng bǔyǔ bǎ huà shuō de gèng zhǔnquè, gèng shēngdòng. Xuéxí guòchéng zhōng, nǐ kěnéng huì bèi yōuxiù de lǎoshī hé rèqíng de tóngxué suǒ yǐngxiǎng, yǎngchéng měitiān dú zhōngwén de hǎo xíguàn. Zhǐyào bǎochí zhè fèn duì zhōngwén de rè'ài yǔ jiānchí, wèilái zài HSK sì jí, wǔ jí shènzhì gèng gāo de shuǐpíng cèshì zhōng, nǐ yídìng néng qǔdé gèng dà de chénggōng!",
            "passage_vi": "Học một ngoại ngữ cũng tựa như leo lên một ngọn núi cao. Khi mới bắt đầu, rất nhiều người đều cảm thấy chữ Hán khó viết, phát âm khó đọc. Nhưng sau khi học xong toàn bộ 20 bài của HSK 3 này, bạn sẽ nhận ra trình độ tiếng Hán của mình đã có sự tiến bộ vượt bậc. Chúng ta đã học được cách dùng câu chữ '把' để xử lý sự vật, dùng câu chữ '被' để diễn đạt thể bị động, lại còn biết dùng các loại bổ ngữ để diễn đạt câu từ chính xác và sinh động hơn. Trong quá trình học tập, bạn có thể đã chịu ảnh hưởng tích cực từ những người thầy ưu tú và những người bạn nhiệt tình, hình thành thói quen tốt đọc tiếng Trung mỗi ngày. Chỉ cần duy trì niềm đam mê và lòng kiên trì với tiếng Trung này, trong tương lai ở các kỳ thi HSK 4, HSK 5 và thậm chí cao hơn nữa, bạn nhất định sẽ giành được thành công to lớn hơn!",
            "questions": [
                {
                    "num": 31,
                    "text": "学完HSK三级全部二十课后，学习者会有什么感受？",
                    "options": ["A. 觉得越来越难想放弃", "B. 发现汉语水平有了巨大进步", "C. 依然什么都不会"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 你会发现自己的汉语水平有了巨大的进步."
                },
                {
                    "num": 32,
                    "text": "我们在HSK三级学会了哪些重要语法？",
                    "options": ["A. 只学会了拼音", "B. '把'字句、'被'字句和各种补语", "C. 只学会了写汉字"],
                    "ans": "B",
                    "explain": "Đoạn văn liệt kê: '把'字句, '被'字句, 各类补语."
                },
                {
                    "num": 33,
                    "text": "学习过程中，我们可能会受到谁的影响？",
                    "options": ["A. 优秀老师和热情同学", "B. 陌生人", "C. 电视广告"],
                    "ans": "A",
                    "explain": "Đoạn văn viết: 被优秀的老师和热情的同学所影响."
                },
                {
                    "num": 34,
                    "text": "要想学好中文，最重要的是保持什么？",
                    "options": ["A. 睡懒觉", "B. 对中文的热爱与坚持", "C. 只背单词不说话"],
                    "ans": "B",
                    "explain": "Đoạn văn viết: 只要保持这份对中文的热爱与坚持."
                },
                {
                    "num": 35,
                    "text": "这段话主要想表达什么思想？",
                    "options": ["A. 鼓励学习者继续努力，勇攀高峰", "B. 告诉大家不要学外语", "C. 介绍爬山的技巧"],
                    "ans": "A",
                    "explain": "Thông điệp chính: Động viên người học tiếp tục nỗ lực chinh phục các nấc thang HSK cao hơn."
                }
            ]
        },
        "writing_p1": [
            {
                "num": 36,
                "chunks": ["我被他", "影响了", "新室友"],
                "ans": "我被新室友影响了。",
                "py": "Wǒ bèi xīn shìyǒu yǐngxiǎng le.",
                "vi": "Tôi bị người bạn cùng phòng mới làm ảnh hưởng."
            },
            {
                "num": 37,
                "chunks": ["被对方", "踢进了一个球", "我们的球门"],
                "ans": "我们的球门被对方踢进了一个球。",
                "py": "Wǒmen de qiúmén bèi duìfāng tī jìn le yí ge qiú.",
                "vi": "Cầu môn của chúng tôi bị đối phương sút vào một bàn."
            },
            {
                "num": 38,
                "chunks": ["人都被电脑", "整天在办公室", "‘绑架’了"],
                "ans": "整天在办公室人都被电脑‘绑架’了。",
                "py": "Zhěng tiān zài bàngōngshì rén dōu bèi diànnǎo 'bǎngjià' le.",
                "vi": "Cả ngày ở văn phòng người ta như bị máy tính 'bắt cóc' vậy."
            },
            {
                "num": 39,
                "chunks": ["一定能取得", "坚持努力", "更大的成功"],
                "ans": "坚持努力一定能取得更大的成功。",
                "py": "Jiānchí nǔlì yídìng néng qǔdé gèng dà de chénggōng.",
                "vi": "Kiên trì nỗ lực nhất định sẽ gặt hái thành công lớn hơn."
            },
            {
                "num": 40,
                "chunks": ["学完了", "全部二十课", "今天我们"],
                "ans": "今天我们学完了全部二十课。",
                "py": "Jīntiān wǒmen xuéwán le quánbù èrshí kè.",
                "vi": "Hôm nay chúng ta đã học xong toàn bộ 20 bài."
            }
        ],
        "writing_p2": [
            {
                "num": 41,
                "sentence": "我 (bèi) 他的刻苦精神感动了。",
                "pinyin": "bèi",
                "ans": "被",
                "vi": "Tôi bị tinh thần chịu khó của anh ấy làm cảm động."
            },
            {
                "num": 42,
                "sentence": "夏天我最喜欢去 (yóuyǒng)。",
                "pinyin": "yóuyǒng",
                "ans": "游泳",
                "vi": "Mùa hè tôi thích nhất là đi bơi."
            },
            {
                "num": 43,
                "sentence": "周末他们去踢 (zúqiú) 了。",
                "pinyin": "zúqiú",
                "ans": "足球",
                "vi": "Cuối tuần họ đi đá bóng rồi."
            },
            {
                "num": 44,
                "sentence": "遇到困难千万不要 (nánguò)。",
                "pinyin": "nánguò",
                "ans": "难过",
                "vi": "Gặp khó khăn tuyệt đối đừng nản lòng đau buồn."
            },
            {
                "num": 45,
                "sentence": "祝你的新工作取得 (chénggōng)！",
                "pinyin": "chénggōng",
                "ans": "成功",
                "vi": "Chúc công việc mới của bạn gặt hái thành công!"
            }
        ],
        "vocab": [
            {"num": 1, "zh": "被", "py": "bèi", "pos": "giới từ", "vi": "bị, được (biểu thị thể bị động)", "eg": "蛋糕被弟弟吃光了。"},
            {"num": 2, "zh": "影响", "py": "yǐngxiǎng", "pos": "động từ/danh từ", "vi": "ảnh hưởng, tác động", "eg": "父母的言行对孩子有很大影响。"},
            {"num": 3, "zh": "体育", "py": "tǐyù", "pos": "danh từ", "vi": "thể dục, thể thao", "eg": "体育锻炼能增强体质。"},
            {"num": 4, "zh": "游泳", "py": "yóuyǒng", "pos": "động từ", "vi": "bơi lội", "eg": "他在游泳池里游得真快。"},
            {"num": 5, "zh": "踢", "py": "tī", "pos": "động từ", "vi": "đá (bằng chân)", "eg": "踢足球, 踢毽子。"},
            {"num": 6, "zh": "足球", "py": "zúqiú", "pos": "danh từ", "vi": "bóng đá", "eg": "今晚有一场精彩的足球决赛。"},
            {"num": 7, "zh": "骑", "py": "qí", "pos": "động từ", "vi": "cưỡi, đạp (xe)", "eg": "骑自行车去郊游。"},
            {"num": 8, "zh": "自行车", "py": "zìxíngchē", "pos": "danh từ", "vi": "xe đạp", "eg": "我的自行车坏了，需要修一下。"},
            {"num": 9, "zh": "跑步", "py": "pǎobù", "pos": "động từ", "vi": "chạy bộ", "eg": "早起跑步身体棒。"},
            {"num": 10, "zh": "比赛", "py": "bǐsài", "pos": "danh từ/động từ", "vi": "cuộc thi, thi đấu", "eg": "下周我们学校要举办汉语比赛。"},
            {"num": 11, "zh": "难过", "py": "nánguò", "pos": "tính từ", "vi": "đau lòng, buồn rầu", "eg": "听到这个消息他很难过。"},
            {"num": 12, "zh": "努力", "py": "nǔlì", "pos": "tính từ/động từ", "vi": "nỗ lực, chăm chỉ", "eg": "只要努力，就会有收获。"},
            {"num": 13, "zh": "成功", "py": "chénggōng", "pos": "động từ/danh từ", "vi": "thành công", "eg": "坚持到底就是成功。"}
        ],
        "proper_nouns": [],
        "grammar": [
            {
                "title": "1. Câu bị động với “被”: Chủ ngữ (Đối tượng chịu tác động) + 被 (+ Tác nhân) + Động từ + Thành phần khác",
                "desc": "Dùng để nhấn mạnh chủ ngữ bị hoặc được một tác nhân nào đó tác động và gây ra kết quả hay sự biến đổi. Trong khẩu ngữ, '被' có thể được thay bằng '叫' hoặc '让'.",
                "examples": [
                    {"zh": "我被他影响了。", "py": "Wǒ bèi tā yǐngxiǎng le.", "vi": "Tôi bị anh ấy làm ảnh hưởng."},
                    {"zh": "蛋糕被弟弟吃光了。", "py": "Dàngāo bèi dìdi chīguāng le.", "vi": "Bánh ngọt đã bị em trai ăn hết sạch rồi."},
                    {"zh": "钱包被小偷偷走了。", "py": "Qiánbāo bèi xiǎotōu tōuzǒu le.", "vi": "Ví tiền bị kẻ gian lấy trộm mất."}
                ]
            },
            {
                "title": "2. Tổng kết ngữ pháp trọng điểm toàn bộ HSK 3",
                "desc": "HSK 3 bao gồm các kết cấu nền tảng cốt lõi: Câu chữ 把 (xử lý sự vật), Câu chữ 被 (thể bị động), Bổ ngữ kết quả (好, 完, 懂, 到), Bổ ngữ xu hướng đơn và kép (来, 去, 出来, 起来), Bổ ngữ khả năng (看得懂, 找不到), Bổ ngữ thời lượng, Bổ ngữ trạng thái với 得, và các cấu trúc so sánh (比, 跟...一样, 越来越...). Nắm vững các cấu trúc này giúp người học tự tin giao tiếp và chuẩn bị bước lên HSK 4!",
                "examples": [
                    {"zh": "把重要的东西放在我这儿。（Câu chữ 把）", "py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr.", "vi": "Hãy để đồ quan trọng ở chỗ tôi."},
                    {"zh": "我被他影响了。（Câu chữ 被）", "py": "Wǒ bèi tā yǐngxiǎng le.", "vi": "Tôi bị anh ấy làm ảnh hưởng."},
                    {"zh": "数学比历史难多了。（Câu so sánh 比）", "py": "Shùxué bǐ lìshǐ nán duō le.", "vi": "Môn toán khó hơn môn lịch sử nhiều."}
                ]
            }
        ]
    }
]
