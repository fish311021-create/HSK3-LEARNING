# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn bị Bài 06: 怎么突然找不到了？
Sẵn sàng đưa vào template_master.html
"""

LESSON_DATA = {
    "lesson_info": {
        "id": 6,
        "title_zh": "怎么突然找不到了？",
        "title_py": "Zěnme tūrán zhǎo bu dào le?",
        "title_vi": "Sao bỗng dưng lại không tìm thấy?",
        "audio_file": "audio.mp3"
    },
    
    "audio_jump": [
        {"time": 0, "label": "▶ 00:00 Mở đầu"},
        {"time": 35, "label": "▶ 00:35 Phần 1 (1-5)"},
        {"time": 175, "label": "▶ 02:55 Phần 2 (6-10)"},
        {"time": 435, "label": "▶ 07:15 Phần 3 (11-15)"},
        {"time": 715, "label": "▶ 11:55 Phần 4 (16-20)"}
    ],

    "tab1_listening": {
        "part1_pictures": [
            {"id": "A", "file": "pic_A.png", "label": "Hình A: Ghé tai lắng nghe (听不清楚 / 听)"},
            {"id": "B", "file": "pic_B.png", "label": "Hình B: Chiếc kính mắt (眼镜)"},
            {"id": "C", "file": "pic_C.png", "label": "Hình C: Xe hơi hỏng mở nắp capo (修车 / 帮忙)"},
            {"id": "D", "file": "pic_D.png", "label": "Hình D (Ví dụ): Gọi điện thoại (打电话)"},
            {"id": "E", "file": "pic_E.png", "label": "Hình E: Mẹ ôm em bé ngồi máy tính (照顾孩子 / 离不开人)"},
            {"id": "F", "file": "pic_F.png", "label": "Hình F: Cầm ô đi dưới trời mưa (拿伞 / 突然不下了)"}
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你刚才说什么？我听不清楚。", "py": "Nǐ gāngcái shuō shénme? Wǒ tīng bu qīngchu.", "vi": "Vừa nãy bạn nói gì cơ? Tôi nghe không rõ."},
                    {"role": "female", "speaker": "女", "zh": "我让你快点儿过来。", "py": "Wǒ ràng nǐ kuài diǎnr guòlái.", "vi": "Tôi bảo bạn mau chóng qua đây."}
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Nhắc đến '我听不清楚' (tôi nghe không rõ) và cử chỉ ghé tai nghe."
            },
            {
                "num": 2,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "怎么突然不下了？", "py": "Zěnme tūrán bú xià le?", "vi": "Sao bỗng nhiên lại tạnh mưa rồi?"},
                    {"role": "female", "speaker": "女", "zh": "是啊，刚才还下得那么大。", "py": "Shì a, gāngcái hái xià de nàme dà.", "vi": "Đúng thế, vừa nãy còn mưa to như vậy cơ mà."}
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Nói về việc trời mưa bỗng tạnh ('怎么突然不下了', '刚才还下得那么大'), tương ứng hình người cầm ô che mưa."
            },
            {
                "num": 3,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "喂，你今天不出来跟大家一起玩儿了吗？", "py": "Wèi, nǐ jīntiān bù chūlái gēn dàjiā yìqǐ wánr le ma?", "vi": "Alo, hôm nay bạn không ra ngoài đi chơi cùng mọi người à?"},
                    {"role": "female", "speaker": "女", "zh": "对不起，我孩子太小，离不开人。", "py": "Duìbuqǐ, wǒ háizi tài xiǎo, lí bu kāi rén.", "vi": "Xin lỗi nhé, con mình còn nhỏ quá, không thể rời mắt được."}
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Nhắc đến '孩子太小，离不开人' (con nhỏ không rời được) tương ứng hình mẹ ôm con nhỏ."
            },
            {
                "num": 4,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "喂，我的车可能有点儿问题，你能过来帮个忙吗？", "py": "Wèi, wǒ de chē kěnéng yǒudiǎnr wèntí, nǐ néng guòlái bāng ge máng ma?", "vi": "Alo, xe của tôi hình như có chút vấn đề, bạn có thể qua giúp một tay không?"},
                    {"role": "male", "speaker": "男", "zh": "我现在就过去，你在哪儿？", "py": "Wǒ xiànzài jiù guòqù, nǐ zài nǎr?", "vi": "Tôi qua ngay đây, bạn đang ở đâu?"}
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Xe gặp sự cố cần giúp đỡ ('我的车可能有点儿问题', '帮个忙')."
            },
            {
                "num": 5,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "树那么远，你看得清楚吗？", "py": "Shù nàme yuǎn, nǐ kàn de qīngchu ma?", "vi": "Cái cây ở xa thế kia, bạn có nhìn rõ không?"},
                    {"role": "male", "speaker": "男", "zh": "我有眼镜，看得清楚。", "py": "Wǒ yǒu yǎnjìng, kàn de qīngchu.", "vi": "Tôi có kính mắt, nhìn rất rõ ràng."}
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Nhắc trực tiếp đến '我有眼镜' (tôi có đeo kính mắt)."
            }
        ],

        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {"zh": "外边特别冷，你出去的时候多穿点儿。伞呢？带把伞吧，可能要下雨。", "py": "Wàibian tèbié lěng, nǐ chūqù de shíhou duō chuān diǎnr. Sǎn ne? Dài bǎ sǎn ba, kěnéng yào xià yǔ.", "vi": "Bên ngoài rất lạnh, khi bạn ra ngoài nhớ mặc dày vào. Ô đâu rồi? Mang theo ô đi nhé, có thể trời sắp mưa đấy."},
                "statement": {"zh": "外面下雪了。", "py": "Wàimiàn xià xuě le.", "vi": "Bên ngoài tuyết rơi rồi."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Lời thoại nhắc '可能要下雨' (có thể trời sắp mưa), chứ không phải tuyết rơi (下雪)."
            },
            {
                "num": 7,
                "passage": {"zh": "车上那么多人，我们还有这么多东西，等下一辆吧，五分钟就来车了。", "py": "Chē shang nàme duō rén, wǒmen hái yǒu zhème duō dōngxi, děng xià yí liàng ba, wǔ fēnzhōng jiù lái chē le.", "vi": "Trên xe đông người như thế, chúng ta lại có nhiều đồ thế này, đợi chuyến sau đi, năm phút nữa là có xe rồi."},
                "statement": {"zh": "这辆车他们不打算上去。", "py": "Zhè liàng chē tāmen bù dǎsuàn shàngqù.", "vi": "Chuyến xe này họ không định lên."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Vì xe đông và nhiều đồ nên họ quyết định đợi xe sau ('等下一辆吧')."
            },
            {
                "num": 8,
                "passage": {"zh": "小丽，我刚看见你给我打的电话。刚才我去楼下送客人了，没带手机。你找我有事吗？", "py": "Xiǎolì, wǒ gāng kànjiàn nǐ gěi wǒ dǎ de diànhuà. Gāngcái wǒ qù lóuxià sòng kèrén le, méi dài shǒujī. Nǐ zhǎo wǒ yǒu shì ma?", "vi": "Tiểu Lệ, anh vừa thấy cuộc gọi nhỡ của em. Vừa nãy anh xuống lầu tiễn khách nên không mang điện thoại. Em tìm anh có việc gì không?"},
                "statement": {"zh": "他正在打电话。", "py": "Tā zhèngzài dǎ diànhuà.", "vi": "Anh ấy đang gọi điện thoại."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Anh ấy đang nói chuyện trực tiếp giải thích lý do vừa rồi không mang máy, chứ không phải đang gọi điện thoại."
            },
            {
                "num": 9,
                "passage": {"zh": "我每天早上都去公园跑步，锻炼身体。", "py": "Wǒ měitiān zǎoshang dōu qù gōngyuán pǎobù, duànliàn shēntǐ.", "vi": "Mỗi buổi sáng tôi đều đến công viên chạy bộ, rèn luyện thân thể."},
                "statement": {"zh": "我每天都运动。", "py": "Wǒ měitiān dōu yùndòng.", "vi": "Tôi ngày nào cũng vận động rèn luyện."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Sáng nào cũng đi công viên chạy bộ rèn luyện sức khỏe tức là ngày nào cũng vận động."
            },
            {
                "num": 10,
                "passage": {"zh": "昨天的作业真容易，我不到一个小时就写完了。小丽，你的作业呢？带了吗？", "py": "Zuótiān de zuòyè zhēn róngyì, wǒ bú dào yí ge xiǎoshí jiù xiěwán le. Xiǎolì, nǐ de zuòyè ne? Dài le ma?", "vi": "Bài tập hôm qua dễ thật đấy, tớ chưa đầy một tiếng đã viết xong rồi. Tiểu Lệ, bài tập của cậu đâu? Mang theo chưa?"},
                "statement": {"zh": "他想知道小丽觉得作业难不难。", "py": "Tā xiǎng zhīdào Xiǎolì juéde zuòyè nán bu nán.", "vi": "Bạn ấy muốn biết Tiểu Lệ cảm thấy bài tập khó hay không."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Bạn nam chỉ khoe bài tập dễ và hỏi Tiểu Lệ có mang bài tập theo không, chứ không hỏi cô ấy thấy khó hay không."
            }
        ],

        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "饭桌上的蛋糕怎么没吃完？你们吃饱了吗？", "py": "Fànzhuō shang de dàngāo zěnme méi chīwán? Nǐmen chībǎo le ma?", "vi": "Bánh kem trên bàn ăn sao chưa ăn hết thế? Các bạn đã ăn no chưa?"},
                    {"role": "female", "speaker": "女", "zh": "刚才还吃了很多饭，怎么吃得完呀？", "py": "Gāngcái hái chī le hěn duō fàn, zěnme chī de wán ya?", "vi": "Vừa nãy đã ăn bao nhiêu là cơm rồi, sao mà ăn hết được chứ?"}
                ],
                "question": {"zh": "问：女的是什么意思？", "py": "Wèn: Nǚ de shì shénme yìsi?", "vi": "Hỏi: Người nữ có ý gì?"},
                "options": ["蛋糕不好吃", "没吃饱", "蛋糕太多了"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Vì đã ăn nhiều cơm nên bánh kem nhiều quá không thể ăn hết nổi (蛋糕太多了)."
            },
            {
                "num": 12,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "这个题我还不太清楚怎么做。", "py": "Zhè ge tí wǒ hái bú tài qīngchu zěnme zuò.", "vi": "Câu này em vẫn chưa rõ lắm cách làm thế nào."},
                    {"role": "male", "speaker": "男", "zh": "我都讲了三次了，你怎么还听不明白？", "py": "Wǒ dōu jiǎng le sān cì le, nǐ zěnme hái tīng bu míngbai?", "vi": "Anh đã giảng tận ba lần rồi, sao em vẫn nghe không hiểu vậy?"}
                ],
                "question": {"zh": "问：关于男的，可以知道什么？", "py": "Wèn: Guānyú nán de, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về người nam, chúng ta có thể biết điều gì?"},
                "options": ["没听清楚", "没听明白", "讲了三次"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam nói rõ '我都讲了三次了' (anh đã giảng 3 lần rồi)."
            },
            {
                "num": 13,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "小雨呢？在你们这儿吗？", "py": "Xiǎoyǔ ne? Zài nǐmen zhèr ma?", "vi": "Tiểu Vũ đâu rồi? Có ở chỗ các bạn không?"},
                    {"role": "female", "speaker": "女", "zh": "您去旁边的办公室问问。", "py": "Nín qù pángbiān de bàngōngshì wènwen.", "vi": "Bác sang văn phòng bên cạnh hỏi xem sao ạ."}
                ],
                "question": {"zh": "问：男的在做什么？", "py": "Wèn: Nán de zài zuò shénme?", "vi": "Hỏi: Người nam đang làm gì?"},
                "options": ["聊天儿", "找人", "问旁边办公室的人"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam đang đi tìm người (tìm Tiểu Vũ: '小雨呢？在你们这儿吗？')."
            },
            {
                "num": 14,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你怎么了？突然说要用我的车。你的车呢？", "py": "Nǐ zěnme le? Tūrán shuō yào yòng wǒ de chē. Nǐ de chē ne?", "vi": "Cậu sao thế? Tự dưng lại bảo mượn xe tôi. Xe cậu đâu?"},
                    {"role": "female", "speaker": "女", "zh": "我弟弟去外地，他开走了，这几天回不来。", "py": "Wǒ dìdi qù wàidì, tā kāizǒu le, zhè jǐ tiān huí bu lái.", "vi": "Em trai tôi đi ngoại tỉnh, nó lái xe đi rồi, mấy hôm nay không về được."}
                ],
                "question": {"zh": "问：关于女的，可以知道什么？", "py": "Wèn: Guānyú nǚ de, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về người nữ, chúng ta có thể biết điều gì?"},
                "options": ["现在没有车", "要去外地", "这几天不在家"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Xe bị em trai mượn đi tỉnh khác nên hiện tại cô ấy không có xe dùng (现在没有车)."
            },
            {
                "num": 15,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "喂，你下飞机了吗？吃饭了没有？", "py": "Wèi, nǐ xià fēijī le ma? Chī fàn le méiyǒu?", "vi": "Alo, anh đã xuống máy bay chưa? Đã ăn cơm chưa?"},
                    {"role": "male", "speaker": "男", "zh": "我刚到宾馆，刚才跟朋友在下边的花园聊天儿，聊得特别高兴，还没吃饭呢。", "py": "Wǒ gāng dào bīnguǎn, gāngcái gēn péngyou zài xiàbian de huāyuán liáotiānr, liáo de tèbié gāoxìng, hái méi chī fàn ne.", "vi": "Anh vừa tới khách sạn, lúc nãy cùng bạn ngồi ở vườn hoa phía dưới tán gẫu, trò chuyện vui lắm, vẫn chưa ăn cơm đâu."}
                ],
                "question": {"zh": "问：男的现在在哪儿？", "py": "Wèn: Nán de xiànzài zài nǎr?", "vi": "Hỏi: Người nam bây giờ đang ở đâu?"},
                "options": ["在花园", "在饭馆", "在宾馆"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Anh ấy vừa tới khách sạn ('我刚到宾馆')."
            }
        ],

        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "你妻子找到新工作了吗？", "py": "Nǐ qīzi zhǎodào xīn gōngzuò le ma?", "vi": "Vợ anh đã tìm được việc làm mới chưa?"},
                    {"role": "male", "speaker": "男", "zh": "她刚离开学校，最近一直在家休息。", "py": "Tā gāng líkāi xuéxiào, zuìjìn yìzhí zài jiā xiūxi.", "vi": "Cô ấy vừa mới rời khỏi trường học, dạo này vẫn đang ở nhà nghỉ ngơi."},
                    {"role": "female", "speaker": "女", "zh": "你问问她想不想来我们公司？", "py": "Nǐ wènwen tā xiǎng bu xiǎng lái wǒmen gōngsī?", "vi": "Anh hỏi thử xem cô ấy có muốn đến công ty chúng tôi làm không?"},
                    {"role": "male", "speaker": "男", "zh": "谢谢你，我回家就告诉她。", "py": "Xièxie nǐ, wǒ huí jiā jiù gàosu tā.", "vi": "Cảm ơn bạn nhé, tôi về nhà sẽ bảo cô ấy ngay."}
                ],
                "question": {"zh": "问：关于男的的妻子，可以知道什么？", "py": "Wèn: Guānyú nán de de qīzi, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về vợ của người nam, chúng ta có thể biết điều gì?"},
                "options": ["在学校工作过", "在女的的公司工作过", "一直没有工作"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam nói '她刚离开学校' (cô ấy vừa rời khỏi trường học), chứng tỏ trước đây từng làm việc ở trường học."
            },
            {
                "num": 17,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "这些都是你女儿的照片吗？", "py": "Zhèxiē dōu shì nǐ nǚ'ér de zhàopiàn ma?", "vi": "Những tấm ảnh này đều là của con gái chị à?"},
                    {"role": "female", "speaker": "女", "zh": "对，这是今年的，那是她六岁时的。", "py": "Duì, zhè shì jīnnián de, nà shì tā liù suì shí de.", "vi": "Đúng rồi, bức này là năm nay, bức kia là lúc bé sáu tuổi."},
                    {"role": "male", "speaker": "男", "zh": "你女儿越来越漂亮了。", "py": "Nǐ nǚ'ér yuè lái yuè piàoliang le.", "vi": "Con gái chị ngày càng xinh đẹp hơn đấy."},
                    {"role": "female", "speaker": "女", "zh": "谢谢，她最爱听这些了。", "py": "Xièxie, tā zuì ài tīng zhèxiē le.", "vi": "Cảm ơn anh, cháu thích nghe nhất là những lời này đấy."}
                ],
                "question": {"zh": "问：关于女儿，可以知道什么？", "py": "Wèn: Guānyú nǚ'ér, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về cô con gái, chúng ta có thể biết điều gì?"},
                "options": ["现在更漂亮", "小时候更漂亮", "最爱看照片"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam khen '越来越漂亮了' (ngày càng xinh hơn so với trước kia) nên hiện tại xinh đẹp hơn."
            },
            {
                "num": 18,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "我刚到北京，晚上总是睡不着。", "py": "Wǒ gāng dào Běijīng, wǎnshang zǒngshì shuì bu zháo.", "vi": "Tôi vừa mới đến Bắc Kinh, buổi tối toàn trằn trọc không ngủ được."},
                    {"role": "female", "speaker": "女", "zh": "我睡不着的时候喜欢看电视，你也看看吧。", "py": "Wǒ shuì bu zháo de shíhou xǐhuan kàn diànshì, nǐ yě kànkan ba.", "vi": "Lúc tôi mất ngủ hay thích xem tivi, bạn cũng xem thử đi."},
                    {"role": "male", "speaker": "男", "zh": "我听不懂汉语，也看不懂汉字，多没意思啊。", "py": "Wǒ tīng bu dǒng Hànyǔ, yě kàn bu dǒng Hànzì, duō méi yìsi a.", "vi": "Tôi nghe không hiểu tiếng Hán, cũng không đọc được chữ Hán, chán chết đi được."},
                    {"role": "female", "speaker": "女", "zh": "那跟我聊聊天儿吧。", "py": "Nà gēn wǒ liáoliáo tiānr ba.", "vi": "Thế thì nói chuyện phiếm với tôi đi."}
                ],
                "question": {"zh": "问：男的有什么问题？", "py": "Wèn: Nán de yǒu shénme wèntí?", "vi": "Hỏi: Người nam đang gặp vấn đề gì?"},
                "options": ["考得不好", "睡不着", "喜欢看电视"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam nói '晚上总是睡不着' (buổi tối luôn không ngủ được)."
            },
            {
                "num": 19,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "怎么回来这么晚？去哪儿了？", "py": "Zěnme huílái zhème wǎn? Qù nǎr le?", "vi": "Sao anh về muộn thế? Đi đâu đấy?"},
                    {"role": "male", "speaker": "男", "zh": "你不是让我给小猫买点儿吃的吗？刚才我去商店了。", "py": "Nǐ bú shì ràng wǒ gěi xiǎomāo mǎi diǎnr chī de ma? Gāngcái wǒ qù shāngdiàn le.", "vi": "Chẳng phải em bảo anh đi mua ít đồ ăn cho mèo sao? Lúc nãy anh đi ra cửa hàng."},
                    {"role": "female", "speaker": "女", "zh": "商店就在楼下，你怎么去了那么长时间？", "py": "Shāngdiàn jiù zài lóuxià, nǐ zěnme qù le nàme cháng shíjiān?", "vi": "Cửa hàng ngay dưới tầng, sao anh đi lâu thế?"},
                    {"role": "male", "speaker": "男", "zh": "刚出商店，有个孩子找不到回家的路了，我过去帮他，给他家里打了个电话。", "py": "Gāng chū shāngdiàn, yǒu ge háizi zhǎo bu dào huí jiā de lù le, wǒ guòqù bāng tā, gěi tā jiā li dǎ le ge diànhuà.", "vi": "Vừa ra khỏi tiệm, có đứa bé không tìm thấy đường về nhà, anh qua giúp nó gọi điện cho người nhà."}
                ],
                "question": {"zh": "问：男的为什么回来晚了？", "py": "Wèn: Nán de wèishénme huílái wǎn le?", "vi": "Hỏi: Vì sao người nam lại về nhà muộn?"},
                "options": ["去商店买东西了", "找不到回家的路了", "帮孩子的忙了"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Vì bận giúp đỡ đứa trẻ lạc đường gọi điện cho người nhà ('帮孩子的忙了')."
            },
            {
                "num": 20,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "看，前边那个人是不是周朋？我们快点儿走过去看看是不是他。", "py": "Kàn, qiánbian nà ge rén shì bú shì Zhōu Péng? Wǒmen kuài diǎnr zǒu guòqù kànkan shì bú shì tā.", "vi": "Kìa, người phía trước có phải Chu Bằng không? Chúng mình đi nhanh lên xem có đúng là cậu ấy không."},
                    {"role": "male", "speaker": "男", "zh": "刚才买了这么多东西，你也不帮我拿，我走不快。", "py": "Gāngcái mǎi le zhème duō dōngxi, nǐ yě bù bāng wǒ ná, wǒ zǒu bu kuài.", "vi": "Vừa nãy mua bao nhiêu là đồ, em chẳng giúp anh xách gì cả, anh không đi nhanh được."}
                ],
                "question": {"zh": "问：关于男的，可以知道什么？", "py": "Wèn: Guānyú nán de, kěyǐ zhīdào shénme?", "vi": "Hỏi: Về người nam, chúng ta có thể biết điều gì?"},
                "options": ["手里的东西多", "看不见前边那个人", "离周朋很近"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Anh ấy xách nhiều đồ nên không đi nhanh được ('手里的东西多')."
            }
        ]
    },

    "tab2_reading": {
        "part1": {
            "options": [
                {"id": "A", "zh": "他刚离开学校，没走太远。", "py": "Tā gāng líkāi xuéxiào, méi zǒu tài yuǎn.", "vi": "Cậu ấy vừa rời trường, chưa đi xa đâu."},
                {"id": "B", "zh": "我的手表和裤子呢？", "py": "Wǒ de shǒubiǎo hé kùzi ne?", "vi": "Đồng hồ và quần của anh đâu rồi?"},
                {"id": "C", "zh": "你刚下飞机，休息一下吧。", "py": "Nǐ gāng xià fēijī, xiūxi yíxià ba.", "vi": "Bạn vừa xuống máy bay, nghỉ ngơi một lát đi."},
                {"id": "D", "zh": "你不是要出去吗？怎么还在这儿？", "py": "Nǐ bú shì yào chūqù ma? Zěnme hái zài zhèr?", "vi": "Chẳng phải bạn định đi ra ngoài sao? Sao vẫn ở đây thế?"},
                {"id": "E", "zh": "当然。我们先坐公共汽车，然后换地铁。", "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.", "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi sang tàu điện ngầm."},
                {"id": "F", "zh": "喂，你听得见我说话吗？", "py": "Wèi, nǐ tīng de jiàn wǒ shuōhuà ma?", "vi": "Alo, bạn có nghe thấy tôi nói không?"}
            ],
            "questions": [
                {"num": 21, "zh": "不行，刚才公司来电话，让我过去一下。", "py": "Bù xíng, gāngcái gōngsī lái diànhuà, ràng wǒ guòqù yíxià.", "vi": "Không được rồi, vừa nãy công ty gọi điện bảo tôi qua gấp một lát.", "ans": "C", "explain": "Đáp lại lời khuyên nghỉ ngơi sau chuyến bay (你刚下飞机，休息一下吧)."},
                {"num": 22, "zh": "小方呢？不在校园里吗？", "py": "Xiǎofāng ne? Bú zài xiàoyuán li ma?", "vi": "Tiểu Phương đâu rồi? Không có trong khuôn viên trường à?", "ans": "A", "explain": "Hỏi về vị trí Tiểu Phương đáp lại bằng (他刚离开学校，没走太远)."},
                {"num": 23, "zh": "雨下得太大，出不去了。", "py": "Yǔ xià de tài dà, chū bu qù le.", "vi": "Mưa rơi to quá, không ra ngoài được.", "ans": "D", "explain": "Giải thích vì sao chưa đi ra ngoài (你不是要出去吗？怎么还在这儿？)."},
                {"num": 24, "zh": "你说什么？我一个字也听不见。", "py": "Nǐ shuō shénme? Wǒ yí ge zì yě tīng bu jiàn.", "vi": "Cậu nói gì cơ? Tớ một chữ cũng không nghe thấy.", "ans": "F", "explain": "Đáp lại câu hỏi kiểm tra đường truyền (喂，你听得见我说话吗？)."},
                {"num": 25, "zh": "你怎么总是找不到东西？", "py": "Nǐ zěnme zǒngshì zhǎo bu dào dōngxi?", "vi": "Sao anh cứ luôn không tìm thấy đồ thế?", "ans": "B", "explain": "Trách móc việc hay hỏi mất đồ đáp lại câu hỏi (我的手表和裤子呢？)."}
            ]
        },

        "part2": {
            "vocab_bank": [
                {"id": "A", "zh": "离开", "py": "líkāi", "vi": "rời khỏi"},
                {"id": "B", "zh": "明白", "py": "míngbai", "vi": "hiểu rõ"},
                {"id": "C", "zh": "特别", "py": "tèbié", "vi": "đặc biệt"},
                {"id": "D", "zh": "音乐", "py": "yīnyuè", "vi": "âm nhạc"},
                {"id": "E", "zh": "声音", "py": "shēngyīn", "vi": "giọng nói (Ví dụ)"},
                {"id": "F", "zh": "刚才", "py": "gāngcái", "vi": "vừa nãy"}
            ],
            "questions": [
                {"num": 26, "prefix": "我快要（ ", "suffix": " ）这儿了，我们一起吃个饭吧。", "py": "Wǒ kuàiyào ( líkāi ) zhèr le, wǒmen yìqǐ chī ge fàn ba.", "vi": "Tôi sắp sửa rời khỏi nơi này rồi, chúng mình cùng nhau đi ăn bữa cơm nhé.", "ans": "A", "word": "离开", "explain": "Động từ '离开' (rời khỏi nơi đây)."},
                {"num": 27, "prefix": "这个电影（ ", "suffix": " ）有意思，我给你讲讲吧。", "py": "Zhè ge diànyǐng ( tèbié ) yǒu yìsi, wǒ gěi nǐ jiǎngjiang ba.", "vi": "Bộ phim này đặc biệt thú vị, để tôi kể cho bạn nghe nhé.", "ans": "C", "word": "特别", "explain": "Phó từ mức độ '特别' (vô cùng/đặc biệt thú vị)."},
                {"num": 28, "prefix": "今天的考试有点儿难，不少题我都不（ ", "suffix": " ）。", "py": "Jīntiān de kǎoshì yǒudiǎnr nán, bù shǎo tí wǒ dōu bù ( míngbai ).", "vi": "Bài thi hôm nay hơi khó một chút, không ít câu tôi đều không hiểu.", "ans": "B", "word": "明白", "explain": "Động từ nhận thức '明白' (hiểu rõ, thấu hiểu)."},
                {"num": 29, "prefix": "A: 我今天喝了两杯咖啡，现在睡不着了。<br>B: 你可以听听（ ", "suffix": " ）。", "py": "A: Wǒ jīntiān hē le liǎng bēi kāfēi, xiànzài shuì bu zháo le.<br>B: Nǐ kěyǐ tīngting ( yīnyuè ).", "vi": "A: Hôm nay tôi uống hai cốc cà phê, giờ không ngủ được.<br>B: Bạn có thể nghe chút âm nhạc.", "ans": "D", "word": "音乐", "explain": "Cụm '听听音乐' (nghe nhạc để thư giãn)."},
                {"num": 30, "prefix": "A: 小方，（ ", "suffix": " ）经理找你。<br>B: 好，我现在就去经理办公室。", "py": "A: Xiǎofāng, ( gāngcái ) jīnglǐ zhǎo nǐ.<br>B: Hǎo, wǒ xiànzài jiù qù jīnglǐ bàngōngshì.", "vi": "A: Tiểu Phương, vừa nãy giám đốc tìm bạn đấy.<br>B: Vâng, tôi sang phòng giám đốc ngay đây.", "ans": "F", "word": "刚才", "explain": "Từ chỉ thời gian '刚才' (vừa nãy, lúc nãy)."}
            ]
        },

        "part3": [
            {
                "num": 31,
                "passage": {
                    "zh": "不少人觉得现在的人都不太会说话了。有时候想得很清楚，但是说不明白。",
                    "py": "Bù shǎo rén juéde xiànzài de rén dōu bú tài huì shuōhuà le. Yǒushíhou xiǎng de hěn qīngchu, dànshì shuō bu míngbai.",
                    "vi": "Không ít người cảm thấy người ngày nay đều không biết cách ăn nói cho lắm. Đôi khi suy nghĩ rất rõ ràng, nhưng diễn đạt lại không rành mạch."
                },
                "question": {"zh": "★ 现在的人：", "py": "★ Xiànzài de rén:", "vi": "★ Người ngày nay:"},
                "options": [
                    {"id": "A", "zh": "不说话", "py": "bù shuōhuà", "vi": "không nói chuyện"},
                    {"id": "B", "zh": "说话说得太快", "py": "shuōhuà shuō de tài kuài", "vi": "nói chuyện quá nhanh"},
                    {"id": "C", "zh": "有时候说话说不明白", "py": "yǒushíhou shuōhuà shuō bu míngbai", "vi": "đôi khi nói không rõ ràng rành mạch"}
                ],
                "ans": "C",
                "explain": "Đoạn văn viết: '有时候想得很清楚，但是说不明白' nên đáp án là C."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "考试或者做作业不明白的时候别着急问，其实多读读题、多想想，很快就能看懂问题。",
                    "py": "Kǎoshì huòzhě zuò zuòyè bù míngbai de shíhou bié zháojí wèn, qíshí duō dúdu tí, duō xiǎngxiang, hěn kuài jiù néng kàndǒng wèntí.",
                    "vi": "Khi đi thi hoặc làm bài tập không hiểu đừng vội hỏi ngay, thực ra chỉ cần đọc kỹ đề bài hơn, suy nghĩ kỹ hơn thì rất nhanh sẽ hiểu được câu hỏi."
                },
                "question": {"zh": "★ 看不懂问题时：", "py": "★ Kàn bu dǒng wèntí shí:", "vi": "★ Khi nhìn không hiểu câu hỏi:"},
                "options": [
                    {"id": "A", "zh": "不要着急问朋友", "py": "bú yào zháojí wèn péngyou", "vi": "không nên vội vàng đi hỏi bạn"},
                    {"id": "B", "zh": "多问问朋友", "py": "duō wènwen péngyou", "vi": "nên hỏi bạn bè nhiều hơn"},
                    {"id": "C", "zh": "问老师", "py": "wèn lǎoshī", "vi": "hỏi giáo viên"}
                ],
                "ans": "A",
                "explain": "Đoạn văn khuyên: '不明白的时候别着急问' (không hiểu thì đừng vội vàng hỏi)."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "在中国，去朋友家玩儿，离开时朋友可能对你说“慢走”，很多外国人听不明白。其实他们的意思是让你在回去的路上小心点儿，不是让你慢点儿走。",
                    "py": "Zài Zhōngguó, qù péngyou jiā wánr, líkāi shí péngyou kěnéng duì nǐ shuō “màn zǒu”, hěn duō wàiguó rén tīng bu míngbai. Qíshí tāmen de yìsi shì ràng nǐ zài huíqù de lù shang xiǎoxīn diǎnr, bú shì ràng nǐ màn diǎnr zǒu.",
                    "vi": "Ở Trung Quốc, khi đến nhà bạn chơi, lúc ra về bạn bè có thể nói với bạn 'Đi thong thả nhé', nhiều người nước ngoài nghe không hiểu. Thực ra ý của họ là nhắc bạn trên đường về cẩn thận một chút, chứ không phải bắt bạn đi chầm chậm."
                },
                "question": {"zh": "★ 朋友说“慢走”的意思可能是：", "py": "★ Péngyou shuō “màn zǒu” de yìsi kěnéng shì:", "vi": "★ Bạn bè nói 'Màn zǒu' (Đi thong thả) ý có thể là:"},
                "options": [
                    {"id": "A", "zh": "路上小心", "py": "lù shang xiǎoxīn", "vi": "trên đường đi cẩn thận"},
                    {"id": "B", "zh": "别走得太快", "py": "bié zǒu de tài kuài", "vi": "đừng đi quá nhanh"},
                    {"id": "C", "zh": "听不明白", "py": "tīng bu míngbai", "vi": "nghe không hiểu"}
                ],
                "ans": "A",
                "explain": "Đoạn văn nêu rõ: '其实他们的意思是让你在回去的路上小心点儿' (路上小心)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "经理，我觉得店里的服务员有点儿少，现在来吃饭的客人越来越多，特别是晚上，这几个人忙不过来，您看要不要多找几个人来帮忙？",
                    "py": "Jīnglǐ, wǒ juéde diàn li de fúwùyuán yǒudiǎnr shǎo, xiànzài lái chī fàn de kèrén yuè lái yuè duō, tèbié shì wǎnshang, zhè jǐ ge rén máng bu guòlái, nín kàn yào bu yào duō zhǎo jǐ ge rén lái bāngmáng?",
                    "vi": "Thưa giám đốc, tôi thấy nhân viên phục vụ trong quán hơi ít, hiện nay khách đến ăn cơm ngày càng đông, nhất là buổi tối mấy người này bận không xuể, ông xem có nên tuyển thêm vài người đến giúp không ạ?"
                },
                "question": {"zh": "★ 说话人的意思是：", "py": "★ Shuōhuà rén de yìsi shì:", "vi": "★ Ý của người nói là:"},
                "options": [
                    {"id": "A", "zh": "客人太少", "py": "kèrén tài shǎo", "vi": "khách quá ít"},
                    {"id": "B", "zh": "想多找几个服务员", "py": "xiǎng duō zhǎo jǐ ge fúwùyuán", "vi": "muốn tuyển thêm nhân viên phục vụ"},
                    {"id": "C", "zh": "让经理来吃饭", "py": "ràng jīnglǐ lái chī fàn", "vi": "mời giám đốc đến ăn cơm"}
                ],
                "ans": "B",
                "explain": "Người nói đề xuất: '您看要不要多找几个人来帮忙' tức là muốn tuyển thêm nhân viên (想多找几个服务员)."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "小红，你过来帮爸爸一个忙好不好？爸爸的眼镜找不到了，你看看在哪儿呢？我记得刚才放到椅子上了，是不是妈妈拿走了？",
                    "py": "Xiǎohóng, nǐ guòlái bāng bàba yí ge máng hǎo bu hǎo? Bàba de yǎnjìng zhǎo bu dào le, nǐ kànkan zài nǎr ne? Wǒ jìde gāngcái fàng dào yǐzi shang le, shì bú shì māma názǒu le?",
                    "vi": "Tiểu Hồng, con qua đây giúp bố một tay được không? Kính mắt của bố tìm không thấy đâu rồi, con nhìn xem ở đâu nào? Bố nhớ lúc nãy đặt trên ghế mà, có phải mẹ cầm đi rồi không?"
                },
                "question": {"zh": "★ 爸爸让小红：", "py": "★ Bàba ràng Xiǎohóng:", "vi": "★ Bố bảo Tiểu Hồng làm gì:"},
                "options": [
                    {"id": "A", "zh": "找眼镜", "py": "zhǎo yǎnjìng", "vi": "tìm kính mắt"},
                    {"id": "B", "zh": "找妈妈", "py": "zhǎo māma", "vi": "tìm mẹ"},
                    {"id": "C", "zh": "搬椅子", "py": "bān yǐzi", "vi": "dọn ghế"}
                ],
                "ans": "A",
                "explain": "Bố nhờ con gái: '爸爸的眼镜找不到了，你看看在哪儿呢' (tìm kính mắt giúp bố)."
            }
        ]
    },

    "tab3_writing": {
        "part1": [
            {
                "num": 36,
                "chunks": ["明白", "电话里", "讲", "不"],
                "ans": "电话里讲不明白。",
                "py": "Diànhuà li jiǎng bu míngbai.",
                "vi": "Nói qua điện thoại thì không giải thích rõ được.",
                "grammar": "Trạng ngữ nơi chốn (电话里) + Động từ + Bổ ngữ khả năng phủ định (讲不明白)."
            },
            {
                "num": 37,
                "chunks": ["听", "清楚", "你", "什么", "说", "不"],
                "ans": "你说什么听不清楚。",
                "py": "Nǐ shuō shénme tīng bu qīngchu.",
                "vi": "Bạn nói gì tôi nghe không rõ.",
                "grammar": "Chủ - vị làm tân ngữ (你说什么) + Động từ + Bổ ngữ khả năng (听不清楚)."
            },
            {
                "num": 38,
                "chunks": ["到", "买", "这儿", "不", "在", "咖啡"],
                "ans": "在这儿买不到咖啡。",
                "py": "Zài zhèr mǎi bu dào kāfēi.",
                "vi": "Ở chỗ này không mua được cà phê.",
                "grammar": "Trạng ngữ (在这儿) + Động từ + Bổ ngữ khả năng (买不到) + Tân ngữ (咖啡)."
            },
            {
                "num": 39,
                "chunks": ["完", "得", "饭不多", "吃", "我"],
                "ans": "饭不多我吃得完。",
                "py": "Fàn bù duō wǒ chī de wán.",
                "vi": "Cơm không nhiều, tôi ăn hết được.",
                "grammar": "Phân câu trạng thái (饭不多) + Chủ ngữ (我) + Động từ + Bổ ngữ khả năng (吃得完)."
            },
            {
                "num": 40,
                "chunks": ["吗", "懂", "看", "汉语报纸", "得", "你"],
                "ans": "你看得懂汉语报纸吗？",
                "py": "Nǐ kàn de dǒng Hànyǔ bàozhǐ ma?",
                "vi": "Bạn đọc có hiểu báo tiếng Trung không?",
                "grammar": "Chủ ngữ (你) + Động từ + Bổ ngữ khả năng (看得懂) + Tân ngữ (汉语报纸) + 吗?"
            }
        ],

        "part2": [
            {
                "num": 41,
                "sentence": "我（ gāng ）才一直在玩儿电脑游戏，可能没听见。",
                "pinyin": "gāng",
                "ans": "刚",
                "hanviet": "Cương",
                "compound": "刚才 (gāngcái): vừa nãy, lúc nãy",
                "vi": "Lúc nãy tôi mải chơi game máy tính suốt, có lẽ không nghe thấy."
            },
            {
                "num": 42,
                "sentence": "这个问题我已经（ jiǎng ）得很明白了，不要再问我了。",
                "pinyin": "jiǎng",
                "ans": "讲",
                "hanviet": "Giảng",
                "compound": "讲 (jiǎng): nói, giảng giải",
                "vi": "Vấn đề này tôi đã giảng giải rất rõ ràng rồi, đừng hỏi tôi thêm nữa."
            },
            {
                "num": 43,
                "sentence": "中午休息的时候，大家都去公司楼下的饭馆吃饭、（ liáo ）天儿。",
                "pinyin": "liáo",
                "ans": "聊",
                "hanviet": "Liêu",
                "compound": "聊天儿 (liáotiānr): tán gẫu, trò chuyện",
                "vi": "Lúc nghỉ trưa, mọi người đều xuống nhà hàng dưới tầng công ty ăn cơm, tán gẫu."
            },
            {
                "num": 44,
                "sentence": "我家旁边有一个小公（ yuán ），我每天都带我的小狗去那儿走走。",
                "pinyin": "yuán",
                "ans": "园",
                "hanviet": "Viên",
                "compound": "公园 (gōngyuán): công viên",
                "vi": "Bên cạnh nhà tôi có một công viên nhỏ, ngày nào tôi cũng dắt cún cưng ra đó dạo chơi."
            },
            {
                "num": 45,
                "sentence": "他跑得（ tè ）别快，现在已经看不到他了。",
                "pinyin": "tè",
                "ans": "特",
                "hanviet": "Đặc",
                "compound": "特别 (tèbié): đặc biệt, vô cùng",
                "vi": "Anh ấy chạy cực kỳ nhanh, giờ đã không còn nhìn thấy bóng dáng đâu nữa rồi."
            }
        ]
    },

    "tab4_textbook": {
        "vocab": [
            {"id": 1, "zh": "眼镜", "py": "yǎnjìng", "pos": "danh từ", "vi": "kính mắt"},
            {"id": 2, "zh": "突然", "py": "tūrán", "pos": "tính từ/phó từ", "vi": "đột nhiên, bất ngờ"},
            {"id": 3, "zh": "离开", "py": "líkāi", "pos": "động từ", "vi": "rời khỏi, rời xa"},
            {"id": 4, "zh": "清楚", "py": "qīngchu", "pos": "tính từ", "vi": "rõ ràng, rành mạch"},
            {"id": 5, "zh": "刚才", "py": "gāngcái", "pos": "danh từ chỉ thời gian", "vi": "vừa nãy, lúc nãy"},
            {"id": 6, "zh": "帮忙", "py": "bāngmáng", "pos": "động từ", "vi": "giúp đỡ"},
            {"id": 7, "zh": "特别", "py": "tèbié", "pos": "phó từ/tính từ", "vi": "đặc biệt, vô cùng"},
            {"id": 8, "zh": "讲", "py": "jiǎng", "pos": "động từ", "vi": "nói, giảng giải"},
            {"id": 9, "zh": "明白", "py": "míngbai", "pos": "động từ/tính từ", "vi": "hiểu rõ, thấu suốt"},
            {"id": 10, "zh": "锻炼", "py": "duànliàn", "pos": "động từ", "vi": "rèn luyện thân thể"},
            {"id": 11, "zh": "音乐", "py": "yīnyuè", "pos": "danh từ", "vi": "âm nhạc"},
            {"id": 12, "zh": "公园", "py": "gōngyuán", "pos": "danh từ", "vi": "công viên"},
            {"id": 13, "zh": "聊天儿", "py": "liáotiānr", "pos": "động từ", "vi": "nói chuyện phiếm, tán gẫu"},
            {"id": 14, "zh": "睡着", "py": "shuìzháo", "pos": "động từ", "vi": "ngủ thiếp đi, ngủ được"},
            {"id": 15, "zh": "更", "py": "gèng", "pos": "phó từ", "vi": "càng, hơn nữa"}
        ],

        "grammar": [
            {
                "title": "1. Bổ ngữ khả năng (可能补语): V + 得 / 不 + Bổ ngữ kết quả/xu hướng",
                "structure": "Khẳng định: V + 得 + C | Phủ định: V + 不 + C | Nghi vấn: V + 得 + C + V + 不 + C?",
                "explanation": "Dùng để biểu thị trong điều kiện chủ quan hoặc khách quan có đủ khả năng thực hiện hay làm được kết quả nào đó hay không.",
                "examples": [
                    {"zh": "怎么突然找不到了？", "py": "Zěnme tūrán zhǎo bu dào le?", "vi": "Sao bỗng nhiên lại tìm không ra?"},
                    {"zh": "你看得见黑板上的字吗？", "py": "Nǐ kàn de jiàn hēibǎn shang de zì ma?", "vi": "Bạn có nhìn thấy chữ trên bảng đen không?"},
                    {"zh": "老师讲的话，我都听得懂。", "py": "Lǎoshī jiǎng de huà, wǒ dōu tīng de dǒng.", "vi": "Lời thầy giảng tôi đều nghe hiểu được."}
                ]
            },
            {
                "title": "2. Phân biệt “刚” và “刚才”",
                "structure": "“刚” là phó từ (đứng sau CN, trước ĐT) | “刚才” là danh từ thời gian (đứng trước hoặc sau CN)",
                "explanation": "“刚” nhấn mạnh hành động vừa mới xảy ra trong cảm giác của người nói (thời gian có thể dài); “刚才” chỉ khoảng thời gian ngắn vừa mới trôi qua cách đây vài phút.",
                "examples": [
                    {"zh": "我刚来中国两个月。", "py": "Wǒ gāng lái Zhōngguó liǎng ge yuè.", "vi": "Tôi vừa mới đến Trung Quốc được hai tháng (thời gian 2 tháng nhưng cảm giác như vừa mới)."},
                    {"zh": "刚才你去哪儿了？", "py": "Gāngcái nǐ qù nǎr le?", "vi": "Vừa nãy bạn đã đi đâu đấy?"}
                ]
            }
        ],

        "expansion_and_idiom": {
            "hanzi_knowledge": {
                "type": "旧字新词 (Từ ghép tạo nghĩa mới)",
                "characters": []
            },
            "word_expansion": [
                {"word": "校园", "py": "xiàoyuán", "meaning": "khuôn viên trường (校: trường + 园: vườn, khuôn viên)"},
                {"word": "饭桌", "py": "fànzhuō", "meaning": "bàn ăn cơm (饭: cơm + 桌: bàn)"},
                {"word": "花园", "py": "huāyuán", "meaning": "vườn hoa (花: hoa + 园: vườn)"}
            ],
            "proverb": {
                "zh": "万事开头难",
                "py": "Wàn shì kāitóu nán",
                "vi": "Vạn sự khởi đầu nan. Mọi công việc khi mới bắt đầu đều gặp nhiều khó khăn, thử thách."
            }
        },

        "polyphonic": [
            {
                "char": "更",
                "sounds": [
                    {"py": "gèng", "meaning": "càng, hơn (phó từ so sánh)", "example": "更好 (gèng hǎo), 更多 (gèng duō)"},
                    {"py": "gēng", "meaning": "canh giờ, thay đổi", "example": "三更 (sāngēng), 更改 (gēnggǎi)"}
                ]
            },
            {
                "char": "着",
                "sounds": [
                    {"py": "zháo", "meaning": "được, trúng (biểu thị kết quả)", "example": "睡着 (shuìzháo), 着急 (zháojí)"},
                    {"py": "zhe", "meaning": "trợ từ động thái (đang tiếp diễn)", "example": "看着 (kànzhe), 笑着 (xiàozhe)"}
                ]
            }
        ]
    },

    "quiz_data": {
        "1": {"ans": "A", "explain": "A: Nhắc đến '我听不清楚' (tôi nghe không rõ) và cử chỉ ghé tai nghe."},
        "2": {"ans": "F", "explain": "F: Nói về việc trời mưa bỗng tạnh ('怎么突然不下了', '刚才还下得那么大'), tương ứng hình người cầm ô che mưa."},
        "3": {"ans": "E", "explain": "E: Nhắc đến '孩子太小，离不开人' (con nhỏ không rời được) tương ứng hình mẹ ôm con nhỏ."},
        "4": {"ans": "C", "explain": "C: Xe gặp sự cố cần giúp đỡ ('我的车可能有点儿问题', '帮个忙')."},
        "5": {"ans": "B", "explain": "B: Nhắc trực tiếp đến '我有眼镜' (tôi có đeo kính mắt)."},
        "6": {"ans": "×", "explain": "Sai (×): Lời thoại nhắc '可能要下雨' (có thể trời sắp mưa), chứ không phải tuyết rơi (下雪)."},
        "7": {"ans": "√", "explain": "Đúng (√): Vì xe đông và nhiều đồ nên họ quyết định đợi xe sau ('等下一辆吧')."},
        "8": {"ans": "×", "explain": "Sai (×): Anh ấy đang nói chuyện trực tiếp giải thích lý do vừa rồi không mang máy, chứ không phải đang gọi điện thoại."},
        "9": {"ans": "√", "explain": "Đúng (√): Sáng nào cũng đi công viên chạy bộ rèn luyện sức khỏe tức là ngày nào cũng vận động."},
        "10": {"ans": "×", "explain": "Sai (×): Bạn nam chỉ khoe bài tập dễ và hỏi Tiểu Lệ có mang bài tập theo không, chứ không hỏi cô ấy thấy khó hay không."},
        "11": {"ans": "C", "explain": "C: Vì đã ăn nhiều cơm nên bánh kem nhiều quá không thể ăn hết nổi (蛋糕太多了)."},
        "12": {"ans": "C", "explain": "C: Người nam nói rõ '我都讲了三次了' (anh đã giảng 3 lần rồi)."},
        "13": {"ans": "B", "explain": "B: Người nam đang đi tìm người (tìm Tiểu Vũ: '小雨呢？在你们这儿吗？')."},
        "14": {"ans": "A", "explain": "A: Xe bị em trai mượn đi tỉnh khác nên hiện tại cô ấy không có xe dùng (现在没有车)."},
        "15": {"ans": "C", "explain": "C: Anh ấy vừa tới khách sạn ('我刚到宾馆')."},
        "16": {"ans": "A", "explain": "A: Người nam nói '她刚离开学校' (cô ấy vừa rời khỏi trường học), chứng tỏ trước đây từng làm việc ở trường học."},
        "17": {"ans": "A", "explain": "A: Người nam khen '越来越漂亮了' (ngày càng xinh hơn so với trước kia) nên hiện tại xinh đẹp hơn."},
        "18": {"ans": "B", "explain": "B: Người nam nói '晚上总是睡不着' (buổi tối luôn không ngủ được)."},
        "19": {"ans": "C", "explain": "C: Vì bận giúp đỡ đứa trẻ lạc đường gọi điện cho người nhà ('帮孩子的忙了')."},
        "20": {"ans": "A", "explain": "A: Anh ấy xách nhiều đồ nên không đi nhanh được ('手里的东西多')."},
        "21": {"ans": "C", "explain": "C: Đáp lại lời khuyên nghỉ ngơi sau chuyến bay (你刚下飞机，休息一下吧)."},
        "22": {"ans": "A", "explain": "A: Hỏi về vị trí Tiểu Phương đáp lại bằng (他刚离开学校，没走太远)."},
        "23": {"ans": "D", "explain": "D: Giải thích vì sao chưa đi ra ngoài (你不是要出去吗？怎么还在这儿？)."},
        "24": {"ans": "F", "explain": "F: Đáp lại câu hỏi kiểm tra đường truyền (喂，你听得见我说话吗？)."},
        "25": {"ans": "B", "explain": "B: Trách móc việc hay hỏi mất đồ đáp lại câu hỏi (我的手表和裤子呢？)."},
        "26": {"ans": "A", "explain": "A: Động từ '离开' (rời khỏi nơi đây)."},
        "27": {"ans": "C", "explain": "C: Phó từ mức độ '特别' (vô cùng/đặc biệt thú vị)."},
        "28": {"ans": "B", "explain": "B: Động từ nhận thức '明白' (hiểu rõ, thấu hiểu)."},
        "29": {"ans": "D", "explain": "D: Cụm '听听音乐' (nghe nhạc để thư giãn)."},
        "30": {"ans": "F", "explain": "F: Từ chỉ thời gian '刚才' (vừa nãy, lúc nãy)."},
        "31": {"ans": "C", "explain": "C: Đoạn văn viết: '有时候想得很清楚，但是说不明白' nên đáp án là C."},
        "32": {"ans": "A", "explain": "A: Đoạn văn khuyên: '不明白的时候别着急问' (không hiểu thì đừng vội vàng hỏi)."},
        "33": {"ans": "A", "explain": "A: Đoạn văn nêu rõ: '其实他们的意思是让你在回去的路上小心点儿' (路上小心)."},
        "34": {"ans": "B", "explain": "B: Người nói đề xuất: '您看要不要多找几个人来帮忙' tức là muốn tuyển thêm nhân viên (想多找几个服务员)."},
        "35": {"ans": "A", "explain": "A: Bố nhờ con gái: '爸爸的眼镜找不到了，你看看在哪儿呢' (tìm kính mắt giúp bố)."}
    }
}
