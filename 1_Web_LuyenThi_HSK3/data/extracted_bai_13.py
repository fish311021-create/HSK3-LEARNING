# -*- coding: utf-8 -*-
LESSON_DATA = {
    "lesson_info": {
        "id": 13,
        "title_zh": "我是走回来的。",
        "title_py": "Wǒ shì zǒu huílái de.",
        "title_vi": "Tôi đi bộ về đấy.",
        "audio_file": "audio.mp3"
    },
    "audio_jump": [
        {
            "time": 0,
            "label": "▶ 00:00 Mở đầu"
        },
        {
            "time": 30,
            "label": "▶ 00:30 Phần 1 (1-5)"
        },
        {
            "time": 190,
            "label": "▶ 03:10 Phần 2 (6-10)"
        },
        {
            "time": 490,
            "label": "▶ 08:10 Phần 3 (11-15)"
        },
        {
            "time": 790,
            "label": "▶ 13:10 Phần 4 (16-20)"
        }
    ],
    "tab1_listening": {
        "part1_pictures": [
            {
                "id": "A",
                "file": "pic_A.png",
                "label": "Hình A: Hai ông cháu cùng ngồi đọc sách (爷爷送生日礼物 / 读故事)"
            },
            {
                "id": "B",
                "file": "pic_B.png",
                "label": "Hình B: Đôi nam nữ vừa đi dạo vừa trò chuyện (面试 / 边走边聊)"
            },
            {
                "id": "C",
                "file": "pic_C.png",
                "label": "Hình C: Chú chó con chạy lon ton về phía trước (小狗跑过去 / 拿好吃的)"
            },
            {
                "id": "D",
                "file": "pic_D.png",
                "label": "Hình D (Ví dụ): Nhân viên nữ nghe điện thoại (打电话)"
            },
            {
                "id": "E",
                "file": "pic_E.png",
                "label": "Hình E: Em bé ngã bò trên sàn khóc mếu (孩子摔倒 / 让他自己站起来)"
            },
            {
                "id": "F",
                "file": "pic_F.png",
                "label": "Hình F: Chàng trai giúp bê thùng đồ to nặng (箱子搬不动 / 帮你搬下去)"
            }
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "爷爷，这本书我没看过，是您新买的吗？",
                        "py": "Yéye, zhè běn shū wǒ méi kànguo, shì nín xīn mǎi de ma?",
                        "vi": "Ông ơi, cuốn sách này cháu chưa xem bao giờ, là ông mới mua ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "这是爷爷送给你的生日礼物。",
                        "py": "Zhè shì yéye sònggěi nǐ de shēngrì lǐwù.",
                        "vi": "Đây là món quà sinh nhật ông tặng cho cháu đấy."
                    }
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Ông tặng sách làm quà sinh nhật cho cháu ('爷爷送给你的生日礼物'), tương ứng hình A hai ông cháu cùng đọc sách."
            },
            {
                "num": 2,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你终于来了，箱子里东西太多，我刚才搬了几次都没搬起来。",
                        "py": "Nǐ zhōngyú lái le, xiāngzi lǐ dōngxi tài duō, wǒ gāngcái bān le jǐ cì dōu méi bān qǐlái.",
                        "vi": "Anh cuối cùng cũng đến rồi, trong thùng nhiều đồ quá, vừa rồi em nhấc mấy lần đều không nhấc nổi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我放下电话马上就跑过来了，来，我帮你搬下去。",
                        "py": "Wǒ fàngxià diànhuà mǎshàng jiù pǎo guòlái le, lái, wǒ bāng nǐ bān xiàqù.",
                        "vi": "Anh đặt điện thoại xuống là chạy ngay qua đây, nào, để anh giúp em chuyển xuống dưới."
                    }
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Chàng trai chạy qua giúp cô gái khiêng thùng đồ nặng xuống ('箱子里东西太多', '帮你搬下去'), tương ứng hình F."
            },
            {
                "num": 3,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你看我家小狗多喜欢你，见了你就跑过去了。",
                        "py": "Nǐ kàn wǒ jiā xiǎogǒu duō xǐhuan nǐ, jiàn le nǐ jiù pǎo guòqù le.",
                        "vi": "Bạn xem chú cún nhà tôi thích bạn biết bao, vừa thấy bạn là chạy tót qua rồi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "它这么快跑过来是因为我拿着好吃的。",
                        "py": "Tā zhème kuài pǎo guòlái shì yīnwèi wǒ ná zhe hǎochī de.",
                        "vi": "Nó chạy nhanh qua đây như vậy là vì tôi đang cầm đồ ăn ngon đấy."
                    }
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Nhắc tới '小狗跑过去了' (chú chó chạy qua), tương ứng hình C chú chó con."
            },
            {
                "num": 4,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好久不见，没想到在这儿遇到你了，你来这儿做什么？",
                        "py": "Hǎojiǔ bújjiàn, méi xiǎngdào zài zhèr yùdào nǐ le, nǐ lái zhèr zuò shénme?",
                        "vi": "Lâu lắm không gặp, không ngờ lại gặp bạn ở đây, bạn đến đây làm gì thế?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我来这家公司面试，刚面完。走，我们边走边聊。",
                        "py": "Wǒ lái zhè jiā gōngsī miànshì, gāng miànwán. Zǒu, wǒmen biān zǒu biān liáo.",
                        "vi": "Tôi đến công ty này phỏng vấn, vừa phỏng vấn xong. Đi nào, chúng mình vừa đi vừa nói chuyện."
                    }
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Hai người gặp nhau sau buổi phỏng vấn rủ '边走边聊' (vừa đi vừa nói chuyện), tương ứng hình B đôi nam nữ công sở đi dạo."
            },
            {
                "num": 5,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你看这孩子怎么了？我过去帮他一下。",
                        "py": "Nǐ kàn zhè háizi zěnme le? Wǒ guòqù bāng tā yíxià.",
                        "vi": "Bạn xem em bé kia bị làm sao thế? Tôi qua giúp bé một chút nhé."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "让他自己站起来，他一定可以。",
                        "py": "Ràng tā zìjǐ zhàn qǐlái, tā yídìng kěyǐ.",
                        "vi": "Hãy để bé tự đứng dậy, bé nhất định làm được mà."
                    }
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Thấy em bé ngã bò trên đất và muốn để bé tự đứng lên ('让他自己站起来'), tương ứng hình E em bé đang bò khóc."
            }
        ],
        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {
                    "zh": "住在我家旁边的是个老人，他很热情，喜欢帮助大家，大家有了问题都愿意请他帮忙。",
                    "py": "Zhù zài wǒ jiā pángbiān de shì ge lǎorén, tā hěn rèqíng, xǐhuan bāngzhù dàjiā, dàjiā yǒu le wèntí dōu yuànyì qǐng tā bāngmáng.",
                    "vi": "Sống cạnh nhà tôi là một cụ già, cụ rất nhiệt tình, thích giúp đỡ mọi người, mọi người có vấn đề gì đều thích nhờ cụ giúp."
                },
                "statement": {
                    "zh": "那位老人遇到了问题。",
                    "py": "Nà wèi lǎorén yùdào le wèntí.",
                    "vi": "Cụ già đó đã gặp phải vấn đề."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Cụ già là người nhiệt tình giúp đỡ người khác giải quyết vấn đề, chứ không phải cụ gặp vấn đề."
            },
            {
                "num": 7,
                "passage": {
                    "zh": "过去我喜欢每天早上起床后一边吃早饭一边看报纸，现在我没有这个习惯了，因为太忙了没时间了。",
                    "py": "Guòqù wǒ xǐhuan měitiān zǎoshang qǐchuáng hòu yìbiān chī zǎofàn yìbiān kàn bàozhǐ, xiànzài wǒ méiyǒu zhè ge xíguàn le, yīnwèi tài máng le méi shíjiān le.",
                    "vi": "Trước đây tôi thích mỗi sáng sau khi thức dậy vừa ăn sáng vừa đọc báo, hiện tại tôi không còn thói quen này nữa, bởi vì quá bận không có thời gian."
                },
                "statement": {
                    "zh": "他一直一边吃早饭一边看报纸。",
                    "py": "Tā yìzhí yìbiān chī zǎofàn yìbiān kàn bàozhǐ.",
                    "vi": "Anh ấy vẫn luôn vừa ăn sáng vừa đọc báo."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Đoạn văn nêu rõ bây giờ vì quá bận nên đã bỏ thói quen đó ('现在我没有这个习惯了')."
            },
            {
                "num": 8,
                "passage": {
                    "zh": "早上我起床就出门了，到了半路发现没带电脑和钱包，又开回去拿，到公司的时候已经10点半了。",
                    "py": "Zǎoshang wǒ qǐchuáng jiù chūmén le, dào le bànlù fāxiàn méi dài diànnǎo hé qiánbāo, yòu kāi huíqù ná, dào gōngsī de shíhou yǐjīng shí diǎn bàn le.",
                    "vi": "Sáng nay tôi thức dậy là ra khỏi cửa ngay, đi đến nửa đường phát hiện quên mang máy tính và ví tiền, lại lái xe quay về lấy, lúc đến công ty đã 10 giờ rưỡi rồi."
                },
                "statement": {
                    "zh": "他是开车来公司的。",
                    "py": "Tā shì kāichē lái gōngsī de.",
                    "vi": "Anh ấy lái xe đến công ty."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đoạn văn dùng từ '又开回去拿' (lại lái xe quay về lấy), chứng tỏ anh ấy lái xe ô tô."
            },
            {
                "num": 9,
                "passage": {
                    "zh": "妈妈忙了一天，回家还要做饭，我让她坐下来休息一会儿，但她总是边笑边说：“为你和你爸做饭，我很高兴。”",
                    "py": "Māma máng le yì tiān, huíjiā hái yào zuòfàn, wǒ ràng tā zuò xiàlai xiūxi yíhuìr, dàn tā zǒngshì biān xiào biān shuō: \"Wèi nǐ hé nǐ bà zuòfàn, wǒ hěn gāoxìng.\"",
                    "vi": "Mẹ bận rộn cả ngày, về nhà lại còn nấu cơm, tôi bảo mẹ ngồi xuống nghỉ ngơi một lát, nhưng mẹ luôn vừa cười vừa nói: \"Nấu cơm cho con và bố con, mẹ vui lắm.\""
                },
                "statement": {
                    "zh": "爸爸很喜欢做饭。",
                    "py": "Bàba hěn xǐhuan zuòfàn.",
                    "vi": "Bố rất thích nấu cơm."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người nấu cơm là mẹ ('为你和你爸做饭'), câu nhận định bố thích nấu cơm là sai."
            },
            {
                "num": 10,
                "passage": {
                    "zh": "方校长的办公室过去在四层，他每天都爬上去。上个月搬到十二层以后，他开始坐电梯，不爬楼了。",
                    "py": "Fāng xiàozhǎng de bàngōngshì guòqù zài sì céng, tā měitiān dōu pá shàngqù. Shàng ge yuè bān dào shí'èr céng yǐhòu, tā kāishǐ zuò diàntī, bù pá lóu le.",
                    "vi": "Phòng làm việc của thầy hiệu trưởng Phương trước đây ở tầng 4, ngày nào thầy cũng leo bộ lên. Từ sau khi tháng trước chuyển lên tầng 12, thầy bắt đầu đi thang máy, không leo cầu thang nữa."
                },
                "statement": {
                    "zh": "以前方校长喜欢爬山。",
                    "py": "Yǐqián Fāng xiàozhǎng xǐhuan páshān.",
                    "vi": "Trước đây thầy hiệu trưởng Phương thích leo núi."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Thầy leo cầu thang lên phòng làm việc ở tầng 4 ('爬楼', '爬上去'), không phải thích leo núi ('爬山')."
            }
        ],
        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你怎么这么累？",
                        "py": "Nǐ zěnme zhème lèi?",
                        "vi": "Sao em mệt mỏi thế này?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "电梯坏了，我是爬上来的，快给我喝口水。",
                        "py": "Diàntī huài le, wǒ shì pá shànglai de, kuài gěi wǒ hē kǒu shuǐ.",
                        "vi": "Thang máy hỏng rồi, em phải leo bộ lên đấy, mau cho em hớp nước đi."
                    }
                ],
                "question": {
                    "zh": "女的为什么很累？",
                    "py": "Nǚ de wèishénme hěn lèi?",
                    "vi": "Tại sao người nữ lại rất mệt?"
                },
                "options": {
                    "A": {
                        "zh": "她去爬山了",
                        "py": "Tā qù páshān le",
                        "vi": "Cô ấy đi leo núi"
                    },
                    "B": {
                        "zh": "她喝了很多水",
                        "py": "Tā hē le hěn duō shuǐ",
                        "vi": "Cô ấy uống rất nhiều nước"
                    },
                    "C": {
                        "zh": "她是走上楼来的",
                        "py": "Tā shì zǒu shàng lóu lái de",
                        "vi": "Cô ấy phải đi bộ leo cầu thang lên"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Vì thang máy hỏng nên cô ấy phải leo bộ cầu thang lên ('电梯坏了，我是爬上来的')."
            },
            {
                "num": 12,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "超市离家这么远，我们真的要走回去吗？",
                        "py": "Chāoshì lí jiā zhème yuǎn, wǒmen zhēn de yào zǒu huíqù ma?",
                        "vi": "Siêu thị cách nhà xa thế này, chúng mình thực sự phải đi bộ về sao?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "只有三站，我们边走边聊，一会儿就到家了。多走走还能锻炼身体，不是吗？",
                        "py": "Zhǐ yǒu sān zhàn, wǒmen biān zǒu biān liáo, yíhuìr jiù dào jiā le. Duō zǒuzou hái néng duànliàn shēntǐ, bú shì ma?",
                        "vi": "Chỉ có 3 trạm thôi mà, chúng mình vừa đi vừa nói chuyện, một lát là về đến nhà rồi. Đi bộ nhiều còn rèn luyện sức khỏe nữa, chẳng phải thế sao?"
                    }
                ],
                "question": {
                    "zh": "女的想做什么？",
                    "py": "Nǚ de xiǎng zuò shénme?",
                    "vi": "Người nữ muốn làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "走回家去",
                        "py": "Zǒu huí jiā qù",
                        "vi": "Đi bộ về nhà"
                    },
                    "B": {
                        "zh": "聊天儿",
                        "py": "Liáotiānr",
                        "vi": "Tán gẫu"
                    },
                    "C": {
                        "zh": "去超市",
                        "py": "Qù chāoshì",
                        "vi": "Đi siêu thị"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ thuyết phục người nam đi bộ về nhà ('走回去', '走回家去')."
            },
            {
                "num": 13,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你真的要出国？去那么远的地方，不是想回来就能回来的，你爸妈多想你啊。",
                        "py": "Nǐ zhēn de yào chūguó? Qù nàme yuǎn de dìfang, bú shì xiǎng huílái jiù néng huílái de, nǐ bàma duō xiǎng nǐ a.",
                        "vi": "Bạn thực sự muốn ra nước ngoài sao? Đi nơi xa như vậy, không phải muốn về là về được ngay đâu, bố mẹ bạn sẽ nhớ bạn biết bao."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "他们说年轻人应该走出去，多看看外边的人和事。",
                        "py": "Tāmen shuō niánqīngrén yīnggāi zǒu chūqù, duō kànkan wàibian de rén hé shì.",
                        "vi": "Bố mẹ tôi bảo người trẻ tuổi nên bước ra ngoài, xem nhiều hiểu rộng về con người và sự việc bên ngoài."
                    }
                ],
                "question": {
                    "zh": "关于女的，可以知道什么？",
                    "py": "Guānyú nǚ de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nữ, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "已经不年轻了",
                        "py": "Yǐjīng bù niánqīng le",
                        "vi": "Đã không còn trẻ nữa"
                    },
                    "B": {
                        "zh": "很想爸妈",
                        "py": "Hěn xiǎng bàma",
                        "vi": "Rất nhớ bố mẹ"
                    },
                    "C": {
                        "zh": "要去国外",
                        "py": "Yào qù guówài",
                        "vi": "Sắp đi ra nước ngoài"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam hỏi '你真的要出国' và người nữ giải thích lý do đi ra nước ngoài."
            },
            {
                "num": 14,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "那么多车，吃饭的人真不少。",
                        "py": "Nàme duō chē, chīfàn de rén zhēn bù shǎo.",
                        "vi": "Nhiều xe thế kia, người đến ăn cơm đông thật đấy."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我们把车放在这儿，走过去吧，也不远，两分钟就到了。",
                        "py": "Wǒmen bǎ chē fàng zài zhèr, zǒu guòqù ba, yě bù yuǎn, liǎng fēnzhōng jiù dào le.",
                        "vi": "Chúng mình đỗ xe ở đây rồi đi bộ qua đó nhé, cũng không xa đâu, 2 phút là tới nơi rồi."
                    }
                ],
                "question": {
                    "zh": "他们现在最可能在哪儿？",
                    "py": "Tāmen xiànzài zuì kěnéng zài nǎr?",
                    "vi": "Họ hiện tại có khả năng nhất đang ở đâu?"
                },
                "options": {
                    "A": {
                        "zh": "饭馆门口",
                        "py": "Fànguǎn ménkǒu",
                        "vi": "Trước cửa quán ăn"
                    },
                    "B": {
                        "zh": "饭馆里边",
                        "py": "Fànguǎn lǐbian",
                        "vi": "Bên trong quán ăn"
                    },
                    "C": {
                        "zh": "离饭馆不远的地方",
                        "py": "Lí fànguǎn bù yuǎn de dìfang",
                        "vi": "Nơi cách quán ăn không xa"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Đỗ xe ở ngoài và đi bộ 2 phút nữa mới đến quán ăn ('走过去吧，也不远，两分钟就到了')."
            },
            {
                "num": 15,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你几号到北京？票买好了没有？",
                        "py": "Nǐ jǐ hào dào Běijīng? Piào mǎihǎo le méi yǒu?",
                        "vi": "Mùng mấy anh đến Bắc Kinh? Vé đã mua xong chưa?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "别担心，我下个星期六就飞回去了。",
                        "py": "Bié dānxīn, wǒ xià ge xīngqīliù jiù fēi huíqù le.",
                        "vi": "Đừng lo, thứ bảy tuần sau là anh bay về rồi."
                    }
                ],
                "question": {
                    "zh": "男的怎么回北京？",
                    "py": "Nán de zěnme huí Běijīng?",
                    "vi": "Người nam về Bắc Kinh bằng phương tiện gì?"
                },
                "options": {
                    "A": {
                        "zh": "坐火车",
                        "py": "Zuò huǒchē",
                        "vi": "Đi tàu hỏa"
                    },
                    "B": {
                        "zh": "坐飞机",
                        "py": "Zuò fēijī",
                        "vi": "Đi máy bay"
                    },
                    "C": {
                        "zh": "开车",
                        "py": "Kāichē",
                        "vi": "Lái xe"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam nói '我下个星期六就飞回去了' (anh bay về), nghĩa là đi máy bay."
            }
        ],
        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你好，昨天从你们洗衣店拿回去的衣服不是我的。",
                        "py": "Nǐ hǎo, zuótiān cóng nǐmen xǐyīdiàn ná huíqù de yīfu bú shì wǒ de.",
                        "vi": "Xin chào, bộ quần áo hôm qua lấy từ tiệm giặt của các bạn về không phải của tôi."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "这件衣服不是您的？",
                        "py": "Zhè jiàn yīfu bú shì nín de?",
                        "vi": "Bộ quần áo này không phải của ngài ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "您看，我叫方明，这上面写的是方鹏。",
                        "py": "Nín kàn, wǒ jiào Fāng Míng, zhè shàngmiàn xiě de shì Fāng Péng.",
                        "vi": "Cô xem, tôi tên Phương Minh, trên này lại ghi là Phương Bằng."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "一定是服务员边听音乐边工作拿错了，真对不起，您先坐下来喝点儿水，我马上就去给您换。",
                        "py": "Yídìng shì fúwùyuán biān tīng yīnyuè biān gōngzuò ná cuò le, zhēn duìbuqǐ, nín xiān zuò xiàlai hē diǎnr shuǐ, wǒ mǎshàng jiù qù gěi nín huàn.",
                        "vi": "Chắc chắn là nhân viên vừa nghe nhạc vừa làm nên lấy nhầm rồi, thật xin lỗi ngài, ngài ngồi xuống uống nước một chút, tôi đi đổi lại cho ngài ngay đây ạ."
                    }
                ],
                "question": {
                    "zh": "关于男的，可以知道什么？",
                    "py": "Guānyú nán de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nam, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "叫“方朋”",
                        "py": "Jiào \"Fāng Péng\"",
                        "vi": "Tên là \"Phương Bằng\""
                    },
                    "B": {
                        "zh": "在商店买衣服",
                        "py": "Zài shāngdiàn mǎi yīfu",
                        "vi": "Mua quần áo ở cửa hàng"
                    },
                    "C": {
                        "zh": "在洗衣店换衣服",
                        "py": "Zài xǐyīdiàn huàn yīfu",
                        "vi": "Đến tiệm giặt đổi lại quần áo"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam mang áo bị lấy nhầm đến tiệm giặt là để đổi lại ('在洗衣店换衣服')."
            },
            {
                "num": 17,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "小周，你现在要回公司吗？你是开车来的吗？",
                        "py": "Xiǎo Zhōu, nǐ xiànzài yào huí gōngsī ma? Nǐ shì kāichē lái de ma?",
                        "vi": "Tiểu Chu, bây giờ bạn chuẩn bị về công ty à? Bạn lái xe đến đấy à?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我是走过来的，车放在公司门口了。怎么了？有事吗？",
                        "py": "Wǒ shì zǒu guòlái de, chē fàng zài gōngsī ménkǒu le. Zěnme le? Yǒu shì ma?",
                        "vi": "Tôi đi bộ qua đây, xe để ở trước cổng công ty rồi. Sao thế? Có việc gì à?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你能帮我给老周带回去点儿东西吗？他放在我这儿好长时间了。",
                        "py": "Nǐ néng bāng wǒ gěi lǎo Zhōu dài huíqù diǎnr dōngxi ma? Tā fàng zài wǒ zhèr hǎo cháng shíjiān le.",
                        "vi": "Bạn mang về giúp tôi ít đồ cho anh Chu được không? Anh ấy để ở chỗ tôi lâu lắm rồi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "明天可以吗？明天我还来你们这儿，到时候开车过来。",
                        "py": "Míngtiān kěyǐ ma? Míngtiān wǒ hái lái nǐmen zhèr, dào shíhou kāichē guòlái.",
                        "vi": "Ngày mai được không? Ngày mai tôi lại sang chỗ các bạn, khi đó tôi sẽ lái xe qua."
                    }
                ],
                "question": {
                    "zh": "女的想请男的做什么？",
                    "py": "Nǚ de xiǎng qǐng nán de zuò shénme?",
                    "vi": "Người nữ muốn nhờ người nam làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "回公司",
                        "py": "Huí gōngsī",
                        "vi": "Về công ty"
                    },
                    "B": {
                        "zh": "给老周带东西",
                        "py": "Gěi lǎo Zhōu dài dōngxi",
                        "vi": "Cầm hộ đồ cho anh Chu"
                    },
                    "C": {
                        "zh": "开车过去",
                        "py": "Kāichē guòqù",
                        "vi": "Lái xe qua"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nhờ: '你能帮我给老周带回去点儿东西吗' (cầm hộ đồ về cho anh Chu)."
            },
            {
                "num": 18,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "刚才从电梯里走出去的那个瘦瘦的女孩，你认识？",
                        "py": "Gāngcái cóng diàntī lǐ zǒu chūqù de nà ge shòushòu de nǚhái, nǐ rènshi?",
                        "vi": "Cô gái gầy gầy vừa từ trong thang máy bước ra ngoài kia, anh quen à?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "是我以前的同事，听说现在都是经理了。",
                        "py": "Shì wǒ yǐqián de tóngshì, tīngshuō xiànzài dōu shì jīnglǐ le.",
                        "vi": "Là đồng nghiệp trước đây của tôi, nghe nói bây giờ đã làm giám đốc rồi đấy."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "以后你介绍我们认识一下吧。",
                        "py": "Yǐhòu nǐ jièshào wǒmen rènshi yíxià ba.",
                        "vi": "Sau này anh giới thiệu cho chúng tôi làm quen với nhau nhé."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "没问题。",
                        "py": "Méi wèntí.",
                        "vi": "Không thành vấn đề."
                    }
                ],
                "question": {
                    "zh": "女的在电梯里遇到了谁？",
                    "py": "Nǚ de zài diàntī lǐ yùdào le shéi?",
                    "vi": "Người nữ đã gặp ai trong thang máy?"
                },
                "options": {
                    "A": {
                        "zh": "司机",
                        "py": "Sījī",
                        "vi": "Tài xế"
                    },
                    "B": {
                        "zh": "服务员",
                        "py": "Fúwùyuán",
                        "vi": "Nhân viên phục vụ"
                    },
                    "C": {
                        "zh": "同事",
                        "py": "Tóngshì",
                        "vi": "Đồng nghiệp (cũ của người nam)"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam cho biết cô gái đó là '我以前的同事' (đồng nghiệp cũ của tôi)."
            },
            {
                "num": 19,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "服务员，来瓶红酒。",
                        "py": "Fúwùyuán, lái píng hóngjiǔ.",
                        "vi": "Phục vụ ơi, cho một chai rượu vang đỏ."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你不是开车了吗？能喝酒吗？",
                        "py": "Nǐ bú shì kāichē le ma? Néng hējiǔ ma?",
                        "vi": "Chẳng phải anh lái xe à? Uống rượu được sao?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "没关系，今天是你的生日，喝几口没关系。",
                        "py": "Méi guānxi, jīntiān shì nǐ de shēngrì, hē jǐ kǒu méi guānxi.",
                        "vi": "Không sao cả, hôm nay là sinh nhật em, uống vài ngụm không hề gì."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "那你的车今天放在这儿吧，明天再过来开回去。",
                        "py": "Nà nǐ de chē jīntiān fàng zài zhèr ba, míngtiān zài guòlái kāi huíqù.",
                        "vi": "Thế thì xe của anh hôm nay cứ để lại ở đây, mai hãy sang lái về."
                    }
                ],
                "question": {
                    "zh": "关于男的，可以知道什么？",
                    "py": "Guānyú nán de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nam, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "今天是他生日",
                        "py": "Jīntiān shì tā shēngrì",
                        "vi": "Hôm nay là sinh nhật anh ấy"
                    },
                    "B": {
                        "zh": "没开车来",
                        "py": "Méi kāichē lái",
                        "vi": "Không lái xe đến"
                    },
                    "C": {
                        "zh": "想喝点儿酒",
                        "py": "Xiǎng hē diǎnr jiǔ",
                        "vi": "Muốn uống chút rượu"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam gọi rượu vang mừng sinh nhật người nữ ('服务员，来瓶红酒'), chứng tỏ muốn uống chút rượu."
            },
            {
                "num": 20,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "走累了吧，我们去太阳咖啡店坐一会儿吧。",
                        "py": "Zǒu lèi le ba, wǒmen qù Tàiyáng Kāfēidiàn zuò yíhuìr ba.",
                        "vi": "Đi bộ mệt rồi phải không, chúng mình vào quán cà phê Thái Dương ngồi một lát nhé."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "那家店在三层，也没有电梯，要走上去，喝完咖啡还要走下来，我腿疼。",
                        "py": "Nà jiā diàn zài sān céng, yě méiyǒu diàntī, yào zǒu shàngqù, hēwán kāfēi hái yào zǒu xiàlai, wǒ tuǐ téng.",
                        "vi": "Quán đó ở tầng 3, lại không có thang máy, phải leo bộ lên, uống xong cà phê lại phải đi bộ xuống, em đau chân lắm."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "那去西西蛋糕店吧，有电梯。",
                        "py": "Nà qù Xīxī Dàngāodiàn ba, yǒu diàntī.",
                        "vi": "Thế thì đến tiệm bánh ngọt Tây Tây nhé, có thang máy đấy."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好啊好啊，那家店在高层，从上面看下去特别漂亮。",
                        "py": "Hǎo a hǎo a, nà jiā diàn zài gāocéng, cóng shàngmiàn kàn xiàqù tèbié piàoliang.",
                        "vi": "Được đấy được đấy, tiệm đó ở tầng cao, từ trên nhìn xuống ngắm cảnh đẹp tuyệt vời."
                    }
                ],
                "question": {
                    "zh": "女的要去哪儿？",
                    "py": "Nǚ de yào qù nǎr?",
                    "vi": "Người nữ muốn đi đâu?"
                },
                "options": {
                    "A": {
                        "zh": "太阳咖啡店",
                        "py": "Tàiyáng Kāfēidiàn",
                        "vi": "Quán cà phê Thái Dương"
                    },
                    "B": {
                        "zh": "西西蛋糕店",
                        "py": "Xīxī Dàngāodiàn",
                        "vi": "Tiệm bánh ngọt Tây Tây"
                    },
                    "C": {
                        "zh": "西西咖啡店",
                        "py": "Xīxī Kāfēidiàn",
                        "vi": "Quán cà phê Tây Tây"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ đồng ý đến tiệm bánh ngọt có thang máy ('那去西西蛋糕店吧，有电梯', '好啊好啊')."
            }
        ]
    },
    "tab2_reading": {
        "part1_21_25": {
            "options": {
                "A": {
                    "zh": "你下班有时间吗？能跟我聊聊吗？",
                    "py": "Nǐ xiàbān yǒu shíjiān ma? Néng gēn wǒ liáoliao ma?",
                    "vi": "Tan làm bạn có thời gian không? Có thể trò chuyện với tôi một chút không?"
                },
                "B": {
                    "zh": "这是谁的照片？让我也看看吧。",
                    "py": "Zhè shì shéi de zhàopiàn? Ràng wǒ yě kànkan ba.",
                    "vi": "Đây là ảnh của ai thế? Cho tôi xem cùng với."
                },
                "C": {
                    "zh": "是她，刚进来就出去了，很着急。",
                    "py": "Shì tā, gāng jìnlái jiù chūqù le, hěn zháojí.",
                    "vi": "Là cô ấy đấy, vừa bước vào lại đi ra ngoài ngay, rất vội vàng."
                },
                "D": {
                    "zh": "咖啡和牛奶都买回来了吗？",
                    "py": "Kāfēi hé niúnǎi dōu mǎi huílái le ma?",
                    "vi": "Cà phê và sữa tươi đã mua về hết chưa?"
                },
                "E": {
                    "zh": "当然。我们先坐公共汽车，然后换地铁。",
                    "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.",
                    "vi": "Đương nhiên rồi. Chúng mình đi xe buýt trước, sau đó đổi sang tàu điện ngầm. (Ví dụ)"
                },
                "F": {
                    "zh": "都快到家了，车坏了，所以我走回来了。",
                    "py": "Dōu kuài dào jiā le, chē huài le, suǒyǐ wǒ zǒu huílái le.",
                    "vi": "Đã sắp về đến nhà rồi thì xe hỏng, thế nên tôi đi bộ về."
                }
            },
            "questions": [
                {
                    "num": 21,
                    "zh": "刚才走出去的那个人是谁？是笑笑吗？",
                    "py": "Gāngcái zǒu chūqù de nà ge rén shì shéi? Shì Xiàoxiao ma?",
                    "vi": "Người vừa bước ra ngoài kia là ai thế? Có phải Tiếu Tiếu không?",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C</strong>: Xác nhận người vừa đi ra ngoài vội vã ('是她，刚进来就出去了，很着急')."
                },
                {
                    "num": 22,
                    "zh": "你怎么走回来了？你的车呢？",
                    "py": "Nǐ zěnme zǒu huílái le? Nǐ de chē ne?",
                    "vi": "Sao bạn lại đi bộ về thế này? Xe của bạn đâu rồi?",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F</strong>: Giải thích lý do đi bộ về do xe bị hỏng ('都快到家了，车坏了，所以我走回来了')."
                },
                {
                    "num": 23,
                    "zh": "牛奶都卖完了，我只买回来一些咖啡。",
                    "py": "Niúnǎi dōu màiwán le, wǒ zhǐ mǎi huílái yìxiē kāfēi.",
                    "vi": "Sữa tươi bán hết sạch rồi, tôi chỉ mua về được ít cà phê thôi.",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D</strong>: Trả lời cho câu hỏi đồ đã mua về chưa ('咖啡和牛奶都买回来了吗')."
                },
                {
                    "num": 24,
                    "zh": "是小李女儿的照片，你坐过来一点儿，我们一起看。",
                    "py": "Shì Xiǎolǐ nǚ'ér de zhàopiàn, nǐ zuò guòlái yìdiǎnr, wǒmen yìqǐ kàn.",
                    "vi": "Là ảnh con gái của Tiểu Lý, bạn ngồi sát qua đây một chút, chúng mình cùng xem.",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B</strong>: Trả lời cho câu hỏi ảnh của ai và rủ xem cùng ('这是谁的照片？让我也看看吧')."
                },
                {
                    "num": 25,
                    "zh": "好啊，去公司楼下的咖啡店吧，边喝边聊。",
                    "py": "Hǎo a, qù gōngsī lóuxià de kāfēidiàn ba, biān hē biān liáo.",
                    "vi": "Được chứ, xuống quán cà phê dưới tầng công ty nhé, vừa uống vừa trò chuyện.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A</strong>: Nhận lời rủ trò chuyện sau giờ làm ('你下班有时间吗？能跟我聊聊吗')."
                }
            ]
        },
        "part2_26_30": {
            "options": {
                "A": {
                    "zh": "爷爷",
                    "py": "yéye",
                    "vi": "ông nội"
                },
                "B": {
                    "zh": "礼物",
                    "py": "lǐwù",
                    "vi": "món quà"
                },
                "C": {
                    "zh": "过去",
                    "py": "guòqù",
                    "vi": "qua đó, đi qua"
                },
                "D": {
                    "zh": "一般",
                    "py": "yìbān",
                    "vi": "thông thường, bình thường"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "tiếng, âm thanh (Ví dụ)"
                },
                "F": {
                    "zh": "经常",
                    "py": "jīngcháng",
                    "vi": "thường xuyên"
                }
            },
            "questions": [
                {
                    "num": 26,
                    "zh": "爸爸妈妈在饭馆等我们呢，我们快（ ）吧。",
                    "py": "Bàba māma zài fànguǎn děng wǒmen ne, wǒmen kuài ( ) ba.",
                    "vi": "Bố mẹ đang đợi chúng ta ở quán ăn đấy, chúng mình mau (qua đó) thôi.",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C: 过去</strong> (đi qua đó).",
                    "sentence": "爸爸妈妈在饭馆等我们呢，我们快（ ）吧。"
                },
                {
                    "num": 27,
                    "zh": "这是我为你买的生日（ ），你打开看看，喜欢不喜欢？",
                    "py": "Zhè shì wǒ wèi nǐ mǎi de shēngrì ( ), nǐ dǎkāi kànkan, xǐhuan bù xǐhuan?",
                    "vi": "Đây là (món quà) sinh nhật tôi mua tặng bạn, bạn mở ra xem thử có thích không?",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B: 礼物</strong> (món quà - 生日礼物).",
                    "sentence": "这是我为你买的生日（ ），你打开看看，喜欢不喜欢？"
                },
                {
                    "num": 28,
                    "zh": "我（ ）今年快九十岁了，身体特别好，他走路比我都快。",
                    "py": "Wǒ ( ) jīnnián kuài jiǔshí suì le, shēntǐ tèbié hǎo, tā zǒulù bǐ wǒ dōu kuài.",
                    "vi": "(Ông nội) tôi năm nay gần 90 tuổi rồi, sức khỏe rất tốt, ông đi bộ còn nhanh hơn cả tôi.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A: 爷爷</strong> (ông nội).",
                    "sentence": "我（ ）今年快九十岁了，身体特别好，他走路比我都快。"
                },
                {
                    "num": 29,
                    "zh": "A：这几天我眼睛看东西不太清楚。\nB：你应该（ ）出去走走，看看远方的绿树，别总坐在电脑前。",
                    "py": "A: Zhè jǐ tiān wǒ yǎnjing kàn dōngxi bú tài qīngchu.\nB: Nǐ yīnggāi ( ) chūqù zǒuzou, kànkan yuǎnfāng de lǜ shù, bié zǒng zuò zài diànnǎo qián.",
                    "vi": "A: Mấy hôm nay mắt tôi nhìn đồ vật không rõ lắm.\nB: Bạn nên (thường xuyên) ra ngoài đi dạo, ngắm nhìn cây cối xanh tươi ở đằng xa, đừng lúc nào cũng ngồi trước máy tính.",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F: 经常</strong> (thường xuyên).",
                    "sentence": "A：这几天我眼睛看东西不太清楚。\nB：你应该（ ）出去走走，看看远方的绿树，别总坐在电脑前。"
                },
                {
                    "num": 30,
                    "zh": "A：只有你一个人吃晚饭吗？你丈夫呢？\nB：我丈夫（ ）八点半才回来，所以不在家吃。",
                    "py": "A: Zhǐ yǒu nǐ yí ge rén chī wǎnfàn ma? Nǐ zhàngfu ne?\nB: Wǒ zhàngfu ( ) bā diǎn bàn cái huílái, suǒyǐ bú zài jiā chī.",
                    "vi": "A: Chỉ có một mình bạn ăn cơm tối thôi à? Chồng bạn đâu rồi?\nB: Chồng tôi (thông thường) 8 rưỡi mới về, thế nên không ăn ở nhà.",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D: 一般</strong> (thông thường, thường lệ).",
                    "sentence": "A：只有你一个人吃晚饭吗？你丈夫呢？\nB：我丈夫（ ）八点半才回来，所以不在家吃。"
                }
            ],
            "words": {
                "A": {
                    "zh": "爷爷",
                    "py": "yéye",
                    "vi": "ông nội"
                },
                "B": {
                    "zh": "礼物",
                    "py": "lǐwù",
                    "vi": "món quà"
                },
                "C": {
                    "zh": "过去",
                    "py": "guòqù",
                    "vi": "qua đó, đi qua"
                },
                "D": {
                    "zh": "一般",
                    "py": "yìbān",
                    "vi": "thông thường, bình thường"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "tiếng, âm thanh (Ví dụ)"
                },
                "F": {
                    "zh": "经常",
                    "py": "jīngcháng",
                    "vi": "thường xuyên"
                }
            }
        },
        "part3_31_35": [
            {
                "num": 31,
                "passage": {
                    "zh": "我最大的兴趣是看书。没事的时候，经常找一个安静的地方，静静地坐下来边喝茶边读书。看累了的时候，站起来看看远方的绿树，或者运动一下。这就是我最大的快乐。",
                    "py": "Wǒ zuì dà de xìngqù shì kànshū. Méi shì de shíhou, jīngcháng zhǎo yí ge ānjìng de dìfang, jìngjìng de zuò xiàlai biān hē chá biān dú shū. Kàn lèi le de shíhou, zhàn qǐlái kànkan yuǎnfāng de lǜ shù, huòzhě yùndòng yíxià. Zhè jiù shì wǒ zuì dà de kuàilè.",
                    "vi": "Sở thích lớn nhất của tôi là đọc sách. Những lúc rảnh rỗi, tôi thường tìm một nơi yên tĩnh, thảnh thơi ngồi xuống vừa thưởng trà vừa đọc sách. Khi mắt đã mỏi, lại đứng dậy ngắm nhìn cây xanh phía xa hoặc vận động một chút. Đó chính là niềm vui lớn nhất của tôi."
                },
                "question": {
                    "zh": "我喜欢：",
                    "py": "Wǒ xǐhuan:",
                    "vi": "Tôi thích:"
                },
                "options": {
                    "A": {
                        "zh": "坐下来看远方",
                        "py": "Zuò xiàlai kàn yuǎnfāng",
                        "vi": "Ngồi xuống ngắm phương xa"
                    },
                    "B": {
                        "zh": "站起来看书",
                        "py": "Zhàn qǐlái kànshū",
                        "vi": "Đứng dậy đọc sách"
                    },
                    "C": {
                        "zh": "坐下来读书",
                        "py": "Zuò xiàlai dú shū",
                        "vi": "Ngồi xuống đọc sách"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Đoạn văn viết: '静静地坐下来边喝茶边读书' (ngồi xuống vừa uống trà vừa đọc sách)."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "你们看，这就是我家的小狗，花花。它经常跑出去帮我拿今天的报纸，还能帮我照顾女儿，跟她玩儿。最有意思的是它可以站起来走路，还能边走边叫。花花这么聪明，大家都喜欢它。",
                    "py": "Nǐmen kàn, zhè jiù shì wǒ jiā de xiǎogǒu, Huāhua. Tā jīngcháng pǎo chūqù bāng wǒ ná jīntiān de bàozhǐ, hái néng bāng wǒ zhàogù nǚ'ér, gēn tā wánr. Zuì yǒu yìsi de shì tā kěyǐ zhàn qǐlái zǒulù, hái néng biān zǒu biān jiào. Huāhua zhème cōngmíng, dàjiā dōu xǐhuan tā.",
                    "vi": "Các bạn nhìn xem, đây là chú cún nhà tôi, tên là Hoa Hoa. Nó thường chạy ra ngoài lấy báo hôm nay giúp tôi, lại còn biết trông nom con gái và chơi với con bé nữa. Thú vị nhất là nó có thể đứng lên bằng hai chân đi lại, vừa đi vừa sủa. Hoa Hoa thông minh như thế nên ai ai cũng quý mến nó."
                },
                "question": {
                    "zh": "花花：",
                    "py": "Huāhua:",
                    "vi": "Hoa Hoa:"
                },
                "options": {
                    "A": {
                        "zh": "能站着走路",
                        "py": "Néng zhàn zhe zǒulù",
                        "vi": "Có thể đứng đi bộ"
                    },
                    "B": {
                        "zh": "不会站着",
                        "py": "Bú huì zhàn zhe",
                        "vi": "Không biết đứng"
                    },
                    "C": {
                        "zh": "总是跑出去玩儿",
                        "py": "Zǒngshì pǎo chūqù wánr",
                        "vi": "Toàn chạy ra ngoài chơi"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn nêu: '最有意思的是它可以站起来走路' (thú vị nhất là nó biết đứng lên đi bộ)."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "昨天我一天都没带手机，回到家看见有8个电话，都是姐姐打过来的。我突然想到：姐姐今天要飞回美国去，她一定是想在上飞机前跟我说会儿话。等我给她打回去的时候，姐姐已经关机了。",
                    "py": "Zuótiān wǒ yì tiān dōu méi dài shǒujī, huí dào jiā kànjiàn yǒu bā ge diànhuà, dōu shì jiějie dǎ guòlái de. Wǒ tūrán xiǎngdào: Jiějie jīntiān yào fēi huí Měiguó qù, tā yídìng shì xiǎng zài shàng fēijī qián gēn wǒ shuō huìr huà. Děng wǒ gěi tā dǎ huíqù de shíhou, jiějie yǐjīng guānjī le.",
                    "vi": "Hôm qua cả ngày tôi không mang theo điện thoại, về đến nhà thấy có 8 cuộc gọi nhỡ, đều là chị gái gọi đến. Tôi sực nhớ ra: hôm nay chị bay về Mỹ, chắc hẳn chị muốn nói chuyện với tôi một lát trước khi lên máy bay. Đến lúc tôi gọi lại thì chị đã tắt máy mất rồi."
                },
                "question": {
                    "zh": "我：",
                    "py": "Wǒ:",
                    "vi": "Tôi:"
                },
                "options": {
                    "A": {
                        "zh": "忘了带手机",
                        "py": "Wàng le dài shǒujī",
                        "vi": "Quên mang theo điện thoại"
                    },
                    "B": {
                        "zh": "不想接姐姐的电话",
                        "py": "Bù xiǎng jiē jiějie de diànhuà",
                        "vi": "Không muốn nghe máy của chị"
                    },
                    "C": {
                        "zh": "给姐姐打了8个电话",
                        "py": "Gěi jiějie dǎ le bā ge diànhuà",
                        "vi": "Đã gọi cho chị 8 cuộc điện thoại"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn nêu: '昨天我一天都没带手机' (hôm qua cả ngày tôi không mang điện thoại)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "中国人常说“一心不可二用”，意思是做这件事的时候不要同时做那件事。我女儿一点儿也不这么想，她经常一心多用，回到家总是边听音乐边吃苹果边看书。这样学习，能知道书上说的是什么吗？",
                    "py": "Zhōngguórén cháng shuō \"yì xīn bù kě èr yòng\", yìsi shì zuò zhè jiàn shì de shíhou bú yào tóngshí zuò nà jiàn shì. Wǒ nǚ'ér yìdiǎnr yě bù zhème xiǎng, tā jīngcháng yì xīn duō yòng, huí dào jiā zǒngshì biān tīng yīnyuè biān chī píngguǒ biān kànshū. Zhèyàng xuéxí, néng zhīdào shū shang shuō de shì shénme ma?",
                    "vi": "Người Trung Quốc thường bảo \"Nhất tâm bất khả nhị dụng\", ý nói khi làm việc này thì không nên cùng lúc làm việc khác. Con gái tôi thì chẳng nghĩ thế chút nào, con bé toàn làm nhiều việc cùng lúc, về đến nhà là vừa nghe nhạc, vừa ăn táo, lại vừa đọc sách. Học như thế thì làm sao nhớ nổi sách viết những gì?"
                },
                "question": {
                    "zh": "女儿经常：",
                    "py": "Nǚ'ér jīngcháng:",
                    "vi": "Con gái thường xuyên:"
                },
                "options": {
                    "A": {
                        "zh": "同时做很多事",
                        "py": "Tóngshí zuò hěn duō shì",
                        "vi": "Cùng lúc làm nhiều việc"
                    },
                    "B": {
                        "zh": "认真学习",
                        "py": "Rènzhēn xuéxí",
                        "vi": "Chăm chỉ học tập"
                    },
                    "C": {
                        "zh": "只做一件事",
                        "py": "Zhǐ zuò yí jiàn shì",
                        "vi": "Chỉ làm một việc"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Con gái thường làm nhiều việc cùng lúc ('一心多用', '边听音乐边吃苹果边看书')."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "我丈夫这次出国给每个家人都带回来一件礼物。我爸爸是一瓶好酒，我妈妈是一件漂亮的衣服，给我的礼物是画儿。因为我最喜欢画画儿，所以我觉得这是他带回来的最特别的礼物。",
                    "py": "Wǒ zhàngfu zhè cì chūguó gěi měi ge jiārén dōu dài huílái yí jiàn lǐwù. Wǒ bàba shì yì píng hǎo jiǔ, wǒ māma shì yí jiàn piàoliang de yīfu, gěi wǒ de lǐwù shì huàr. Yīnwèi wǒ zuì xǐhuan huàhuàr, suǒyǐ wǒ juéde zhè shì tā dài huílái de zuì tèbié de lǐwù.",
                    "vi": "Chồng tôi chuyến đi nước ngoài lần này mang quà về cho tất cả mọi người trong nhà. Cho bố tôi là một chai rượu ngon, mẹ tôi là một bộ quần áo đẹp, còn quà cho tôi là bức tranh. Vì tôi thích vẽ tranh nhất, thế nên tôi thấy đây là món quà đặc biệt nhất mà anh ấy mang về."
                },
                "question": {
                    "zh": "丈夫给我带回来：",
                    "py": "Zhàngfu gěi wǒ dài huílái:",
                    "vi": "Người chồng mang về cho tôi:"
                },
                "options": {
                    "A": {
                        "zh": "三件礼物",
                        "py": "Sān jiàn lǐwù",
                        "vi": "Ba món quà"
                    },
                    "B": {
                        "zh": "一件衣服",
                        "py": "Yí jiàn yīfu",
                        "vi": "Một bộ quần áo"
                    },
                    "C": {
                        "zh": "一件特别的礼物",
                        "py": "Yí jiàn tèbié de lǐwù",
                        "vi": "Một món quà rất đặc biệt"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người vợ chia sẻ: '我觉得这是他带回来的最特别的礼物' (tôi thấy đây là món quà đặc biệt nhất anh ấy mang về)."
            }
        ]
    },
    "tab3_writing": {
        "part1_36_40": [
            {
                "num": 36,
                "chunks": [
                    "一边",
                    "聊天儿",
                    "走路",
                    "我们",
                    "一边"
                ],
                "ans": "我们一边走路一边聊天儿。",
                "py": "Wǒmen yìbiān zǒulù yìbiān liáotiānr.",
                "vi": "Chúng mình vừa đi bộ vừa nói chuyện tán gẫu.",
                "grammar": "Cấu trúc song hành biểu thị hai hành động cùng diễn ra: Chủ ngữ + 一边 + Động từ 1 + 一边 + Động từ 2."
            },
            {
                "num": 37,
                "chunks": [
                    "出去",
                    "跑",
                    "谁",
                    "刚才",
                    "了"
                ],
                "ans": "刚才谁跑出去了？",
                "py": "Gāngcái shéi pǎo chūqù le?",
                "vi": "Vừa rồi ai đã chạy ra ngoài thế?",
                "grammar": "Cấu trúc câu hỏi có bổ ngữ xu hướng phức: Thời gian (刚才) + Đại từ nghi vấn (谁) + Động từ (跑) + Bổ ngữ xu hướng (出去) + 了?"
            },
            {
                "num": 38,
                "chunks": [
                    "别",
                    "开车",
                    "一边",
                    "打电话",
                    "请",
                    "一边"
                ],
                "ans": "请别一边开车一边打电话。",
                "py": "Qǐng bié yìbiān kāichē yìbiān dǎ diànhuà.",
                "vi": "Xin vui lòng đừng vừa lái xe vừa nghe điện thoại.",
                "grammar": "Cấu trúc câu khuyên ngăn/cấm đoán lịch sự: 请别 + 一边 + Hành động 1 + 一边 + Hành động 2."
            },
            {
                "num": 39,
                "chunks": [
                    "就要",
                    "过",
                    "开",
                    "火车",
                    "来",
                    "了"
                ],
                "ans": "火车就要开过来了。",
                "py": "Huǒchē jiù yào kāi guòlai le.",
                "vi": "Tàu hỏa sắp sửa chạy qua đây rồi.",
                "grammar": "Cấu trúc biểu thị sự việc sắp xảy ra trong tương lai gần: Chủ ngữ (火车) + 就要 + Động từ mang bổ ngữ xu hướng phức (开过来) + 了."
            },
            {
                "num": 40,
                "chunks": [
                    "同学们",
                    "走",
                    "教室",
                    "去",
                    "出",
                    "都",
                    "了"
                ],
                "ans": "同学们都走出教室去了。",
                "py": "Tóngxuémen dōu zǒu chū jiàoshì qù le.",
                "vi": "Các bạn học sinh đều đã bước ra khỏi phòng học rồi.",
                "grammar": "Cấu trúc bổ ngữ xu hướng phức kèm tân ngữ nơi chốn: Động từ (走) + Xu hướng 1 (出) + Nơi chốn (教室) + Xu hướng 2 (去) + 了."
            }
        ],
        "part2_41_45": [
            {
                "num": 41,
                "sentence": "送给你一个小（ 礼 ）物，希望你能喜欢。",
                "pinyin": "lǐ",
                "ans": "礼",
                "hanviet": "Lễ",
                "compound": "礼物 (lǐwù: món quà)",
                "vi": "Tặng bạn một món quà nhỏ, mong rằng bạn sẽ thích."
            },
            {
                "num": 42,
                "sentence": "你知道我在回来的路上（ 遇 ）到谁了吗？",
                "pinyin": "yù",
                "ans": "遇",
                "hanviet": "Ngộ",
                "compound": "遇到 (yùdào: tình cờ gặp gỡ)",
                "vi": "Bạn có biết trên đường trở về tôi đã gặp ai không?"
            },
            {
                "num": 43,
                "sentence": "在家吃吧，我忙了一天刚回来，不（ 愿 ）意再出去了。",
                "pinyin": "yuàn",
                "ans": "愿",
                "hanviet": "Nguyện",
                "compound": "愿意 (yuànyì: bằng lòng, mong muốn)",
                "vi": "Ăn ở nhà đi, tôi bận rộn cả ngày vừa mới về, không muốn ra ngoài nữa đâu."
            },
            {
                "num": 44,
                "sentence": "你应（ 该 ）多走出去运动，少在家看电视。",
                "pinyin": "gāi",
                "ans": "该",
                "hanviet": "Cai",
                "compound": "应该 (yīnggāi: nên, cần phải)",
                "vi": "Bạn nên đi ra ngoài vận động nhiều hơn, bớt ở nhà xem tivi lại."
            },
            {
                "num": 45,
                "sentence": "我们在一个公司上班，（ 经 ）常见面，我对她很了解。",
                "pinyin": "jīng",
                "ans": "经",
                "hanviet": "Kinh",
                "compound": "经常 (jīngcháng: thường xuyên)",
                "vi": "Chúng tôi làm việc cùng một công ty, thường xuyên gặp mặt, tôi rất hiểu về cô ấy."
            }
        ]
    },
    "tab4_textbook": {
        "vocab": [
            {
                "id": 1,
                "num": 1,
                "zh": "终于",
                "py": "zhōngyú",
                "pos": "phó từ",
                "vi": "cuối cùng",
                "eg": "作业终于做完了。"
            },
            {
                "id": 2,
                "num": 2,
                "zh": "爷爷",
                "py": "yéye",
                "pos": "danh từ",
                "vi": "ông nội",
                "eg": "这是爷爷送给我的书。"
            },
            {
                "id": 3,
                "num": 3,
                "zh": "礼物",
                "py": "lǐwù",
                "pos": "danh từ",
                "vi": "món quà",
                "eg": "你喜欢这个生日礼物吗？"
            },
            {
                "id": 4,
                "num": 4,
                "zh": "奶奶",
                "py": "nǎinai",
                "pos": "danh từ",
                "vi": "bà nội",
                "eg": "奶奶在厨房做饭。"
            },
            {
                "id": 5,
                "num": 5,
                "zh": "遇到",
                "py": "yùdào",
                "pos": "động từ",
                "vi": "gặp phải, tình cờ gặp",
                "eg": "在路上遇到了老同学。"
            },
            {
                "id": 6,
                "num": 6,
                "zh": "一边",
                "py": "yìbiān",
                "pos": "phó từ",
                "vi": "vừa... vừa...",
                "eg": "我们一边走一边聊吧。"
            },
            {
                "id": 7,
                "num": 7,
                "zh": "过去",
                "py": "guòqù",
                "pos": "danh từ",
                "vi": "quá khứ, trước đây",
                "eg": "过去的事情就别提了。"
            },
            {
                "id": 8,
                "num": 8,
                "zh": "一般",
                "py": "yìbān",
                "pos": "tính từ",
                "vi": "thông thường, bình thường",
                "eg": "我一般七点起床。"
            },
            {
                "id": 9,
                "num": 9,
                "zh": "愿意",
                "py": "yuànyì",
                "pos": "động từ",
                "vi": "bằng lòng, muốn",
                "eg": "你愿意和我一起去吗？"
            },
            {
                "id": 10,
                "num": 10,
                "zh": "起来",
                "py": "qǐlái",
                "pos": "động từ",
                "vi": "đứng dậy, trỗi dậy",
                "eg": "快站起来，别坐着。"
            },
            {
                "id": 11,
                "num": 11,
                "zh": "应该",
                "py": "yīnggāi",
                "pos": "động từ",
                "vi": "nên, phải",
                "eg": "你应该多吃新鲜水果。"
            },
            {
                "id": 12,
                "num": 12,
                "zh": "生活",
                "py": "shēnghuó",
                "pos": "danh từ/động từ",
                "vi": "cuộc sống / sinh sống",
                "eg": "在北京的生活很丰富。"
            },
            {
                "id": 13,
                "num": 13,
                "zh": "校长",
                "py": "xiàozhǎng",
                "pos": "danh từ",
                "vi": "hiệu trưởng",
                "eg": "方校长正在给老师们开会。"
            },
            {
                "id": 14,
                "num": 14,
                "zh": "坏",
                "py": "huài",
                "pos": "tính từ",
                "vi": "hỏng, xấu, hư",
                "eg": "电梯坏了，我们走楼梯吧。"
            },
            {
                "id": 15,
                "num": 15,
                "zh": "经常",
                "py": "jīngcháng",
                "pos": "phó từ",
                "vi": "thường xuyên",
                "eg": "他经常去图书馆借书。"
            }
        ],
        "grammar": [
            {
                "title": "Bổ ngữ xu hướng phức (复合趋向补语 1)",
                "structure": "Động từ (上/下/进/出/回/过/起) + 来 / 去",
                "explanation": "Bổ ngữ xu hướng phức biểu thị hướng chuyển động của hành động. Các động từ xu hướng như 上, 下, 进, 出, 回, 过 kết hợp với 来 (hướng về phía người nói) hoặc 去 (hướng xa khỏi người nói). Khi có tân ngữ chỉ nơi chốn, tân ngữ bắt buộc đặt giữa động từ xu hướng và 来/去 (VD: 走出教室去).",
                "examples": [
                    {
                        "zh": "我是走回来的。",
                        "py": "Wǒ shì zǒu huílái de.",
                        "vi": "Tôi đi bộ về đấy (người nói đang ở nhà)."
                    },
                    {
                        "zh": "我们下楼去等他们吧。",
                        "py": "Wǒmen xià lóu qù děng tāmen ba.",
                        "vi": "Chúng ta xuống dưới nhà đợi họ đi."
                    },
                    {
                        "zh": "刚才谁跑出去了？",
                        "py": "Gāngcái shéi pǎo chūqù le?",
                        "vi": "Vừa nãy ai chạy ra ngoài thế?"
                    }
                ]
            },
            {
                "title": "Cấu trúc song hành “一边……一边……”",
                "structure": "Chủ ngữ + 一边 + Động từ 1 + 一边 + Động từ 2",
                "explanation": "Biểu thị hai hành động cùng diễn ra đồng thời, song song tại một thời điểm do cùng một chủ thể thực hiện.",
                "examples": [
                    {
                        "zh": "我们一边走一边聊吧。",
                        "py": "Wǒmen yìbiān zǒu yìbiān liáo ba.",
                        "vi": "Chúng mình vừa đi vừa nói chuyện nhé."
                    },
                    {
                        "zh": "他经常一边吃早饭一边看报纸。",
                        "py": "Tā jīngcháng yìbiān chī zǎofàn yìbiān kàn bàozhǐ.",
                        "vi": "Anh ấy thường vừa ăn sáng vừa đọc báo."
                    },
                    {
                        "zh": "开车的时候请别一边开车一边打电话。",
                        "py": "Kāichē de shíhou qǐng bié yìbiān kāichē yìbiān dǎ diànhuà.",
                        "vi": "Lúc lái xe xin đừng vừa lái xe vừa nghe điện thoại."
                    }
                ]
            }
        ],
        "expansion_and_idiom": {
            "word_expansion": [
                {
                    "word": "出差",
                    "py": "chūchāi",
                    "meaning": "đi công tác xa"
                },
                {
                    "word": "走过来",
                    "py": "zǒu guòlai",
                    "meaning": "đi bộ qua đây (tiến về phía người nói)"
                },
                {
                    "word": "跑过去",
                    "py": "pǎo guòqù",
                    "meaning": "chạy qua đó (xa dần người nói)"
                }
            ],
            "proverb": {
                "zh": "一心不可二用",
                "py": "Yì xīn bù kě èr yòng",
                "vi": "Một lòng không thể dùng hai việc (Khi làm việc gì cần phải tập trung chuyên tâm, không nên cùng lúc làm nhiều việc khiến tâm trí phân tán)."
            }
        },
        "polyphonic": [
            {
                "char": "长",
                "sounds": [
                    {
                        "py": "cháng",
                        "meaning": "dài, xa (chiều dài, thời gian)",
                        "example": "很长 (hěn cháng), 长时间 (cháng shíjiān)"
                    },
                    {
                        "py": "zhǎng",
                        "meaning": "lớn lên, trưởng thành, người đứng đầu",
                        "example": "长大 (zhǎngdà), 校长 (xiàozhǎng)"
                    }
                ]
            },
            {
                "char": "得",
                "sounds": [
                    {
                        "py": "de",
                        "meaning": "trợ từ kết cấu đứng sau động từ dẫn ra bổ ngữ trạng thái",
                        "example": "跑得快 (pǎo de kuài), 走得慢 (zǒu de màn)"
                    },
                    {
                        "py": "děi",
                        "meaning": "phải, cần phải (động từ năng nguyện)",
                        "example": "我得走了 (wǒ děi zǒu le)"
                    }
                ]
            }
        ]
    },
    "quiz_data": {
        "1": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: '爷爷送给你的生日礼物' (ông tặng quà sinh nhật) tương ứng hình A hai ông cháu đọc sách."
        },
        "2": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: '箱子里东西太多搬不动' (thùng đồ nặng) tương ứng hình F chàng trai bê thùng đồ to."
        },
        "3": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: '你看我家小狗多喜欢你，见了你就跑过去了' tương ứng hình C chú chó con."
        },
        "4": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Hai đồng nghiệp gặp nhau rủ '边走边聊' (vừa đi vừa nói chuyện) tương ứng hình B."
        },
        "5": {
            "ans": "E",
            "explain": "Đáp án đúng là <strong>E</strong>: '你看这孩子怎么了，让他自己站起来' tương ứng hình E em bé đang bò khóc."
        },
        "6": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Cụ già nhiệt tình giúp đỡ người khác giải quyết vấn đề, chứ không phải cụ gặp vấn đề."
        },
        "7": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Bây giờ quá bận nên đã bỏ thói quen đó ('现在我没有这个习惯了')."
        },
        "8": {
            "ans": "√",
            "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Nói '又开回去拿' (lại lái xe quay về lấy) chứng tỏ anh ấy lái xe đến công ty."
        },
        "9": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người nấu cơm là người mẹ ('为你和你爸做饭'), không phải bố."
        },
        "10": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Thầy hiệu trưởng leo cầu thang lên phòng làm việc ở tầng 4 ('爬楼', '爬上去'), không phải leo núi."
        },
        "11": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Vì thang máy hỏng nên cô ấy phải leo bộ cầu thang lên ('电梯坏了，我是爬上来的')."
        },
        "12": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nữ thuyết phục người nam cùng đi bộ về nhà ('走回去', '走回家去')."
        },
        "13": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nữ sắp đi ra nước ngoài ('你真的要出国')."
        },
        "14": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Họ đỗ xe ở ngoài và phải đi bộ 2 phút nữa mới đến quán ăn ('走过去吧，也不远，两分钟就到了')."
        },
        "15": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nam nói '我下个星期六就飞回去了' (anh bay về), nghĩa là đi máy bay."
        },
        "16": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nam mang áo bị lấy nhầm đến tiệm giặt là để đổi lại ('在洗衣店换衣服')."
        },
        "17": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nhờ: '你能帮我给老周带回去点儿东西吗' (cầm hộ đồ về cho anh Chu)."
        },
        "18": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Cô gái đi ra từ thang máy là đồng nghiệp cũ của người nam ('是我以前的同事')."
        },
        "19": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nam gọi rượu vang mừng sinh nhật người nữ ('服务员，来瓶红酒'), chứng tỏ muốn uống chút rượu."
        },
        "20": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ đồng ý đến tiệm bánh ngọt có thang máy ('那去西西蛋糕店吧，有电梯', '好啊好啊')."
        },
        "21": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Xác nhận người vừa đi ra ngoài vội vã '是她，刚进来就出去了，很着急'."
        },
        "22": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: Giải thích đi bộ về do xe bị hỏng '都快到家了，车坏了，所以我走回来了'."
        },
        "23": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D</strong>: Trả lời câu hỏi đồ đã mua về chưa '咖啡和牛奶都买回来了吗'."
        },
        "24": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Trả lời ảnh con gái Tiểu Lý và rủ xem cùng '这是谁的照片？让我也看看吧'."
        },
        "25": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Đồng ý rủ rê nói chuyện sau giờ làm '你下班有时间吗？能跟我聊聊吗'."
        },
        "26": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C: 过去</strong> (đi qua đó)."
        },
        "27": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B: 礼物</strong> (món quà - 生日礼物)."
        },
        "28": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A: 爷爷</strong> (ông nội)."
        },
        "29": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F: 经常</strong> (thường xuyên)."
        },
        "30": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D: 一般</strong> (thông thường)."
        },
        "31": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Thích '静静地坐下来边喝茶边读书' (ngồi xuống đọc sách)."
        },
        "32": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Hoa Hoa '可以站起来走路' (có thể đứng đi bộ)."
        },
        "33": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: '昨天我一天都没带手机' (quên mang điện thoại)."
        },
        "34": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Con gái làm nhiều việc cùng lúc '一心多用'."
        },
        "35": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: '这是他带回来的最特别的礼物' (món quà đặc biệt nhất)."
        }
    }
}
