# -*- coding: utf-8 -*-
LESSON_DATA = {
    "lesson_info": {
        "id": 10,
        "title_zh": "数学比历史难多了。",
        "title_py": "Shùxué bǐ lìshǐ nán duō le.",
        "title_vi": "Môn Toán khó hơn môn Lịch Sử nhiều.",
        "audio_file": "audio.mp3"
    },
    "audio_jump": [
        {
            "time": 0,
            "label": "▶ 00:00 Mở đầu"
        },
        {
            "time": 35,
            "label": "▶ 00:35 Phần 1 (1-5)"
        },
        {
            "time": 200,
            "label": "▶ 03:20 Phần 2 (6-10)"
        },
        {
            "time": 445,
            "label": "▶ 07:25 Phần 3 (11-15)"
        },
        {
            "time": 720,
            "label": "▶ 12:00 Phần 4 (16-20)"
        }
    ],
    "tab1_listening": {
        "part1_pictures": [
            {
                "id": "A",
                "file": "pic_A.png",
                "label": "Hình A: Sân thể dục học sinh đá bóng (踢足球 / 上体育课)"
            },
            {
                "id": "B",
                "file": "pic_B.png",
                "label": "Hình B: Mọi người cụng ly ăn tối vui vẻ (请客吃饭 / 饭馆环境 / 主菜)"
            },
            {
                "id": "C",
                "file": "pic_C.png",
                "label": "Hình C: Thầy giáo dạy toán đứng bên bảng đen (数学老师 / 讲题 / 个子真高)"
            },
            {
                "id": "D",
                "file": "pic_D.png",
                "label": "Hình D (Ví dụ): Nhân viên nữ nghe điện thoại (打电话)"
            },
            {
                "id": "E",
                "file": "pic_E.png",
                "label": "Hình E: Người đàn ông bịt một tai nghe điện thoại ngoài phố ồn ào (听得见吗 / 找个安静点的地方)"
            },
            {
                "id": "F",
                "file": "pic_F.png",
                "label": "Hình F: Cặp vợ chồng xem xe và trao đổi với nhân viên bán xe (旧车换新车 / 汽车)"
            }
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "妈，你看，给笑笑讲题的那个就是我们班数学老师。",
                        "py": "Mā, nǐ kàn, gěi Xiàoxiao jiǎngtí de nà ge jiù shì wǒmen bān shùxué lǎoshī.",
                        "vi": "Mẹ nhìn kìa, người đang giảng bài cho Tiếu Tiếu chính là thầy giáo dạy toán của lớp con đấy."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "他个子真高，讲得怎么样？",
                        "py": "Tā gèzi zhēn gāo, jiǎng de zěnmeyàng?",
                        "vi": "Thầy ấy vóc dáng cao thật đấy, thầy giảng bài thế nào?"
                    }
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Nhắc tới '数学老师' (thầy giáo dạy toán), '给笑笑讲题' (giảng bài) và '个子真高' (vóc dáng rất cao), tương ứng hình người thầy đứng cạnh bảng đen."
            },
            {
                "num": 2,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "喂，你听得见我说话吗？",
                        "py": "Wèi, nǐ tīng de jiàn wǒ shuōhuà ma?",
                        "vi": "A-lô, cậu có nghe rõ tôi nói gì không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "喂，喂，你等一会儿，我找个安静点儿的地方再跟你说啊。",
                        "py": "Wèi, wèi, nǐ děng yíhuìr, wǒ zhǎo ge ānjìng diǎnr de dìfang zài gēn nǐ shuō a.",
                        "vi": "A-lô, a-lô, cậu đợi một lát, tớ tìm chỗ nào yên tĩnh một chút rồi nói chuyện tiếp nhé."
                    }
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Đang ở chỗ đường phố ồn ào phải tìm chỗ yên tĩnh nói điện thoại ('找个安静点儿的地方再跟你说'), tương ứng hình người đàn ông bịt tai nghe máy ngoài đường."
            },
            {
                "num": 3,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "谢谢你们请我们吃饭，这家饭馆的环境真好，菜也很好吃，特别是主菜。",
                        "py": "Xièxie nǐmen qǐng wǒmen chīfàn, zhè jiā fànguǎn de huánjìng zhēn hǎo, cài yě hěn hǎochī, tèbié shì zhǔcài.",
                        "vi": "Cảm ơn các bạn đã mời chúng tôi ăn cơm, không gian nhà hàng này đẹp thật đấy, món ăn cũng rất ngon, đặc biệt là món chính."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我很高兴你们喜欢这个地方，下次我们再来。",
                        "py": "Wǒ hěn gāoxìng nǐmen xǐhuan zhè ge dìfang, xià cì wǒmen zài lái.",
                        "vi": "Tôi rất vui khi các bạn thích nơi này, lần sau chúng mình lại tới nhé."
                    }
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Tiệc mời ăn cơm nhà hàng ('请我们吃饭', '饭馆的环境真好', '特别是主菜'), tương ứng hình mọi người cụng ly chúc mừng tại bàn tiệc."
            },
            {
                "num": 4,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "听说你们店可以用旧车换新车？",
                        "py": "Tīngshuō nǐmen diàn kěyǐ yòng jiù chē huàn xīn chē?",
                        "vi": "Nghe nói cửa hàng các anh có thể dùng xe cũ đổi xe mới ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "对，这边请，我来给您介绍一下吧，您有旧车吗？",
                        "py": "Duì, zhèbiān qǐng, wǒ lái gěi nín jièshào yíxià ba, nín yǒu jiù chē ma?",
                        "vi": "Đúng vậy, xin mời đi lối này, tôi xin giới thiệu với chị, chị có xe cũ không ạ?"
                    }
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Đổi xe cũ lấy xe mới ('可以用旧车换新车'), tương ứng hình cặp đôi trao đổi mua bán ô tô cùng nhân viên showroom."
            },
            {
                "num": 5,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "看，那么多人踢足球，他们在比赛吗？",
                        "py": "Kàn, nàme duō rén tī zúqiú, tāmen zài bǐsài ma?",
                        "vi": "Nhìn kìa, nhiều người đá bóng thế, họ đang thi đấu à?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "不是，他们在上体育课呢。",
                        "py": "Bú shì, tāmen zài shàng tǐyùkè ne.",
                        "vi": "Không phải, họ đang học tiết thể dục đấy."
                    }
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đá bóng trên sân cỏ trong giờ thể dục ('踢足球', '上体育课'), tương ứng hình sân cỏ vận động."
            }
        ],
        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {
                    "zh": "地面上怎么都是雪？昨天我女朋友还穿裙子呢，今天怎么就下雪了？",
                    "py": "Dìmiàn shang zěnme dōu shì xuě? Zuótiān wǒ nǚpéngyou hái chuān qúnzi ne, jīntiān zěnme jiù xià xuě le?",
                    "vi": "Trên mặt đất sao toàn là tuyết thế này? Hôm qua bạn gái tôi còn mặc váy, hôm nay sao đã tuyết rơi rồi?"
                },
                "statement": {
                    "zh": "今天比昨天冷得多。",
                    "py": "Jīntiān bǐ zuótiān lěng de duō.",
                    "vi": "Hôm nay lạnh hơn hôm qua nhiều."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Hôm qua còn mặc váy mà hôm nay đã có tuyết rơi trên mặt đất, chứng tỏ hôm nay lạnh hơn hôm qua rất nhiều."
            },
            {
                "num": 7,
                "passage": {
                    "zh": "走，找个环境好的地方，我早就想跟你聊聊了。这附近有没有安静点儿的咖啡店？",
                    "py": "Zǒu, zhǎo ge huánjìng hǎo de dìfang, wǒ zǎojiù xiǎng gēn nǐ liáoliao le. Zhè fùjìn yǒu méiyǒu ānjìng diǎnr de kāfēidiàn?",
                    "vi": "Đi nào, tìm chỗ nào không gian đẹp một chút, tôi đã muốn trò chuyện với bạn từ lâu rồi. Gần đây có quán cà phê nào yên tĩnh một chút không?"
                },
                "statement": {
                    "zh": "他们要回家了。",
                    "py": "Tāmen yào huí jiā le.",
                    "vi": "Họ chuẩn bị về nhà rồi."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Họ đang tìm quán cà phê yên tĩnh gần đó để ngồi trò chuyện, chứ không phải đi về nhà."
            },
            {
                "num": 8,
                "passage": {
                    "zh": "我爸爸身体那么好，主要是因为每天锻炼。",
                    "py": "Wǒ bàba shēntǐ nàme hǎo, zhǔyào shì yīnwèi měitiān duànliàn.",
                    "vi": "Bố tôi sức khỏe tốt như vậy, chủ yếu là vì rèn luyện thân thể mỗi ngày."
                },
                "statement": {
                    "zh": "爸爸很健康，因为他喜欢运动。",
                    "py": "Bàba hěn jiànkāng, yīnwèi tā xǐhuan yùndòng.",
                    "vi": "Bố rất khỏe mạnh vì ông ấy thích vận động thể thao."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Sức khỏe tốt ('身体好' = '健康') là nhờ rèn luyện hàng ngày ('每天锻炼' = '喜欢运动')."
            },
            {
                "num": 9,
                "passage": {
                    "zh": "我每天工作八九个小时，中午也不能休息，能不累吗？",
                    "py": "Wǒ měitiān gōngzuò bā-jiǔ ge xiǎoshí, zhōngwǔ yě bù néng xiūxi, néng bú lèi ma?",
                    "vi": "Tôi mỗi ngày làm việc tám chín tiếng đồng hồ, buổi trưa cũng không được nghỉ ngơi, làm sao mà không mệt cho được?"
                },
                "statement": {
                    "zh": "他每天工作很累。",
                    "py": "Tā měitiān gōngzuò hěn lèi.",
                    "vi": "Anh ấy mỗi ngày làm việc rất mệt mỏi."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Câu phản vấn '能不累吗' (sao mà không mệt cho được) khẳng định anh ấy làm việc rất mệt mỏi."
            },
            {
                "num": 10,
                "passage": {
                    "zh": "我儿子的学习比以前好多了，主要是他有兴趣了。",
                    "py": "Wǒ érzi de xuéxí bǐ yǐqián hǎo duō le, zhǔyào shì tā yǒu xìngqù le.",
                    "vi": "Việc học của con trai tôi tốt hơn trước đây nhiều rồi, chủ yếu là vì cháu đã có hứng thú học tập."
                },
                "statement": {
                    "zh": "以前儿子不喜欢学习。",
                    "py": "Yǐqián érzi bù xǐhuan xuéxí.",
                    "vi": "Trước đây con trai không thích học tập."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Bây giờ học tốt hơn vì đã có hứng thú, suy ra trước đây con trai không có hứng thú, tức là không thích học."
            }
        ],
        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "前边有卖水果的，我们买点儿苹果吧。",
                        "py": "Qiánbian yǒu mài shuǐguǒ de, wǒmen mǎi diǎnr píngguǒ ba.",
                        "vi": "Phía trước có chỗ bán hoa quả kìa, chúng mình mua ít táo nhé."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "现在是换季的时候，苹果不一定好吃，别买太多，买两三个就行。",
                        "py": "Xiànzài shì huànjì de shíhou, píngguǒ bù yídìng hǎochī, bié mǎi tài duō, mǎi liǎng-sān ge jiù xíng.",
                        "vi": "Bây giờ đang lúc giao mùa, táo chưa chắc đã ngon đâu, đừng mua nhiều quá, mua hai ba quả là được rồi."
                    }
                ],
                "question": {
                    "zh": "女的是什么意思？",
                    "py": "Nǚ de shì shénme yìsi?",
                    "vi": "Người nữ có ý gì?"
                },
                "options": {
                    "A": {
                        "zh": "买两个",
                        "py": "Mǎi liǎng ge",
                        "vi": "Mua hai quả"
                    },
                    "B": {
                        "zh": "买三个",
                        "py": "Mǎi sān ge",
                        "vi": "Mua ba quả"
                    },
                    "C": {
                        "zh": "少买一点儿",
                        "py": "Shǎo mǎi yìdiǎnr",
                        "vi": "Mua ít thôi"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nữ khuyên '别买太多，买两三个就行' tức là khuyên nên mua ít thôi ('少买一点儿')."
            },
            {
                "num": 12,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "今天怎么样？还发烧吗？",
                        "py": "Jīntiān zěnmeyàng? Hái fāshāo ma?",
                        "vi": "Hôm nay em thế nào rồi? Còn sốt không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "吃了药比昨天好一些了，但还头疼。",
                        "py": "Chī le yào bǐ zuótiān hǎo yìxiē le, dàn hái tóuténg.",
                        "vi": "Uống thuốc rồi thấy đỡ hơn hôm qua một chút rồi, nhưng vẫn còn đau đầu."
                    }
                ],
                "question": {
                    "zh": "女的现在怎么样了？",
                    "py": "Nǚ de xiànzài zěnmeyàng le?",
                    "vi": "Người nữ bây giờ tình trạng thế nào?"
                },
                "options": {
                    "A": {
                        "zh": "好点儿了",
                        "py": "Hǎo diǎnr le",
                        "vi": "Đã đỡ hơn một chút"
                    },
                    "B": {
                        "zh": "好多了",
                        "py": "Hǎo duō le",
                        "vi": "Đã khỏi nhiều rồi"
                    },
                    "C": {
                        "zh": "越来越不好",
                        "py": "Yuè lái yuè bù hǎo",
                        "vi": "Ngày càng không tốt"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ nói '比昨天好一些了' (đỡ hơn một chút), tương đương với '好点儿了'."
            },
            {
                "num": 13,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "小刚，方明高还是你高？",
                        "py": "Xiǎogāng, Fāng Míng gāo hái shì nǐ gāo?",
                        "vi": "Tiểu Cương, Phương Minh cao hơn hay bạn cao hơn?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "他个子也不高，只比我高一点儿。",
                        "py": "Tā gèzi yě bù gāo, zhǐ bǐ wǒ gāo yìdiǎnr.",
                        "vi": "Cậu ấy dáng cũng chẳng cao, chỉ cao hơn tôi một chút thôi."
                    }
                ],
                "question": {
                    "zh": "小刚和方明谁高？",
                    "py": "Xiǎogāng hé Fāng Míng shéi gāo?",
                    "vi": "Tiểu Cương và Phương Minh ai cao hơn?"
                },
                "options": {
                    "A": {
                        "zh": "小刚",
                        "py": "Xiǎogāng",
                        "vi": "Tiểu Cương"
                    },
                    "B": {
                        "zh": "方明",
                        "py": "Fāng Míng",
                        "vi": "Phương Minh"
                    },
                    "C": {
                        "zh": "一样高",
                        "py": "Yíyàng gāo",
                        "vi": "Cao bằng nhau"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Tiểu Cương thừa nhận Phương Minh cao hơn mình ('只比我高一点儿'), nên Phương Minh là người cao hơn."
            },
            {
                "num": 14,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "怎么还没到？我都看了三四个电影了。",
                        "py": "Zěnme hái méi dào? Wǒ dōu kàn le sān-sì ge diànyǐng le.",
                        "vi": "Sao vẫn chưa tới nhỉ? Em đã xem ba bốn bộ phim rồi đấy."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我们是从中国到美国，还要再飞五六个小时，你睡一会儿或者再看几个电影。",
                        "py": "Wǒmen shì cóng Zhōngguó dào Měiguó, hái yào zài fēi wǔ-liù ge xiǎoshí, nǐ shuì yíhuìr huòzhě zài kàn jǐ ge diànyǐng.",
                        "vi": "Tụi mình bay từ Trung Quốc sang Mỹ cơ mà, còn phải bay 5-6 tiếng nữa, em ngủ một lát hoặc xem thêm mấy bộ phim nữa đi."
                    }
                ],
                "question": {
                    "zh": "他们可能在哪儿？",
                    "py": "Tāmen kěnéng zài nǎr?",
                    "vi": "Họ có thể đang ở đâu?"
                },
                "options": {
                    "A": {
                        "zh": "飞机上",
                        "py": "Fēijī shang",
                        "vi": "Trên máy bay"
                    },
                    "B": {
                        "zh": "电影院",
                        "py": "Diànyǐngyuàn",
                        "vi": "Trong rạp chiếu phim"
                    },
                    "C": {
                        "zh": "火车上",
                        "py": "Huǒchē shang",
                        "vi": "Trên tàu hỏa"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Bay từ Trung Quốc sang Mỹ ('从中国到美国', '还要再飞五六个小时'), rõ ràng đang ngồi trên máy bay."
            },
            {
                "num": 15,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "喂，你好，请找一下王老师。",
                        "py": "Wèi, nǐhǎo, qǐng zhǎo yíxià Wáng lǎoshī.",
                        "vi": "A-lô, xin chào, xin cho tôi gặp thầy/cô Vương ạ."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我们这儿有三四个姓王的老师呢，您找哪一个？",
                        "py": "Wǒmen zhèr yǒu sān-sì ge xìng Wáng de lǎoshī ne, nín zhǎo nǎ yí ge?",
                        "vi": "Ở chỗ chúng tôi có ba bốn thầy cô họ Vương lận, bác muốn tìm người nào ạ?"
                    }
                ],
                "question": {
                    "zh": "这个地方有几个姓王的老师？",
                    "py": "Zhè ge dìfang yǒu jǐ ge xìng Wáng de lǎoshī?",
                    "vi": "Nơi này có bao nhiêu giáo viên mang họ Vương?"
                },
                "options": {
                    "A": {
                        "zh": "三个",
                        "py": "Sān ge",
                        "vi": "3 người"
                    },
                    "B": {
                        "zh": "三十个",
                        "py": "Sānshí ge",
                        "vi": "30 người"
                    },
                    "C": {
                        "zh": "很多",
                        "py": "Hěn duō",
                        "vi": "Nhiều người (ba bốn người)"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: '有三四个姓王的老师呢' biểu thị số lượng nhiều, không cố định là 3 hay 30, nên chọn '很多' (nhiều)."
            }
        ],
        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你要出去吗？小丽，我问你，去中山南路骑自行车快还是坐公共汽车快？",
                        "py": "Nǐ yào chūqu ma? Xiǎolì, wǒ wèn nǐ, qù Zhōngshān Nán Lù qí zìxíngchē kuài hái shì zuò gōnggòng qìchē kuài?",
                        "vi": "Cậu định ra ngoài à? Tiểu Lệ, tôi hỏi cậu, đến đường Trung Sơn Nam thì đi xe đạp nhanh hơn hay xe buýt nhanh hơn?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "这个时间骑车比坐公共汽车快得多。你这么着急，要去上课吗？",
                        "py": "Zhè ge shíjiān qí chē bǐ zuò gōnggòng qìchē kuài de duō. Nǐ zhème zháojí, yào qù shàngkè ma?",
                        "vi": "Tầm giờ này đi xe đạp nhanh hơn xe buýt nhiều đấy. Cậu vội thế, đi học à?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "不，我要去见女朋友。",
                        "py": "Bù, wǒ yào qù jiàn nǚpéngyou.",
                        "vi": "Không, tôi đi gặp bạn gái."
                    }
                ],
                "question": {
                    "zh": "关于男的，可以知道什么？",
                    "py": "Guānyú nán de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nam, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "可能骑自行车",
                        "py": "Kěnéng qí zìxíngchē",
                        "vi": "Có thể sẽ đi xe đạp"
                    },
                    "B": {
                        "zh": "可能坐公共汽车",
                        "py": "Kěnéng zuò gōnggòng qìchē",
                        "vi": "Có thể sẽ đi xe buýt"
                    },
                    "C": {
                        "zh": "要去上课",
                        "py": "Yào qù shàngkè",
                        "vi": "Phải đi lên lớp"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Vì vội đi gặp bạn gái và được khuyên giờ này đi xe đạp nhanh hơn nhiều ('骑车比坐公共汽车快得多'), anh ta khả năng cao sẽ đạp xe."
            },
            {
                "num": 17,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "明天是晴天还是阴天？",
                        "py": "Míngtiān shì qíngtiān hái shì yīntiān?",
                        "vi": "Ngày mai là trời nắng hay trời râm hả anh?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "上午下雪，下午就晴了。",
                        "py": "Shàngwǔ xià xuě, xiàwǔ jiù qíng le.",
                        "vi": "Buổi sáng có tuyết rơi, buổi chiều sẽ tạnh nắng."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "太好了，明天可以穿我的新裙子了。",
                        "py": "Tài hǎo le, míngtiān kěyǐ chuān wǒ de xīn qúnzi le.",
                        "vi": "Tuyệt quá, mai em có thể diện váy mới rồi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "雪后晴天比下雪时冷得多，你不知道吗？",
                        "py": "Xuě hòu qíngtiān bǐ xià xuě shí lěng de duō, nǐ bù zhīdào ma?",
                        "vi": "Sau khi tuyết tan trời nắng còn lạnh hơn lúc tuyết rơi nhiều đấy, em không biết à?"
                    }
                ],
                "question": {
                    "zh": "男的是什么意思？",
                    "py": "Nán de shì shénme yìsi?",
                    "vi": "Người nam có ý gì?"
                },
                "options": {
                    "A": {
                        "zh": "明天很冷",
                        "py": "Míngtiān hěn lěng",
                        "vi": "Ngày mai sẽ rất lạnh"
                    },
                    "B": {
                        "zh": "明天是阴天",
                        "py": "Míngtiān shì yīntiān",
                        "vi": "Ngày mai là trời âm u"
                    },
                    "C": {
                        "zh": "下雪时最冷",
                        "py": "Xià xuě shí zuì lěng",
                        "vi": "Lúc tuyết rơi là lạnh nhất"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam nhắc nhở '雪后晴天比下雪时冷得多', khuyên bạn gái đừng mặc váy mỏng vì ngày mai thực tế sẽ rất lạnh."
            },
            {
                "num": 18,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我昨天换了辆新车，比那辆旧的舒服多了。",
                        "py": "Wǒ zuótiān huàn le liàng xīn chē, bǐ nà liàng jiù de shūfu duō le.",
                        "vi": "Hôm qua tôi mới đổi chiếc xe mới, êm hơn chiếc cũ nhiều."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "又换了？你已经换了四五辆了吧。多少钱？",
                        "py": "Yòu huàn le? Nǐ yǐjīng huàn le sì-wǔ liàng le ba. Duōshao qián?",
                        "vi": "Lại đổi à? Cậu đã đổi bốn năm chiếc rồi nhỉ. Hết bao nhiêu tiền?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "不贵，一百多。我那辆旧车送给你吧。",
                        "py": "Bú guì, yìbǎi duō. Wǒ nà liàng jiù chē sòng gěi nǐ ba.",
                        "vi": "Không đắt, hơn một trăm tệ thôi. Chiếc xe cũ của tôi tặng lại cho cậu nhé."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "一百多？自行车呀！",
                        "py": "Yìbǎi duō? Zìxíngchē ya!",
                        "vi": "Hơn một trăm tệ á? Hóa ra là xe đạp à!"
                    }
                ],
                "question": {
                    "zh": "关于男的，可以知道什么？",
                    "py": "Guānyú nán de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nam, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "买了一辆旧车",
                        "py": "Mǎi le yí liàng jiù chē",
                        "vi": "Đã mua một chiếc xe cũ"
                    },
                    "B": {
                        "zh": "买的是自行车",
                        "py": "Mǎi de shì zìxíngchē",
                        "vi": "Chiếc xe anh ấy mua là xe đạp"
                    },
                    "C": {
                        "zh": "买了五辆车",
                        "py": "Mǎi le wǔ liàng chē",
                        "vi": "Đã mua 5 chiếc xe"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Chiếc xe giá hơn một trăm tệ và được người nữ thốt lên '一百多？自行车呀！', xác nhận là xe đạp."
            },
            {
                "num": 19,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你女儿个子真高，比你高多了吧？",
                        "py": "Nǐ nǚ'ér gèzi zhēn gāo, bǐ nǐ gāo duō le ba?",
                        "vi": "Con gái chị dáng cao thật, cao hơn chị nhiều đúng không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "其实我跟她一样高，只是她比我瘦多了。",
                        "py": "Qíshí wǒ gēn tā yíyàng gāo, zhǐshì tā bǐ wǒ shòu duō le.",
                        "vi": "Thực ra tôi cao bằng cháu nó đấy, chỉ là cháu nó gầy hơn tôi nhiều thôi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "她今年多大？十七八岁？在哪儿学习呢？",
                        "py": "Tā jīnnián duō dà? Shíqī-bā suì? Zài nǎr xuéxí ne?",
                        "vi": "Năm nay cháu bao nhiêu tuổi rồi? 17-18 tuổi à? Đang học ở đâu thế?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "今年19了，正在国外学历史和数学。",
                        "py": "Jīnnián shíjiǔ le, zhèngzài guówài xué lìshǐ hé shùxué.",
                        "vi": "Năm nay cháu 19 tuổi rồi, đang học lịch sử và toán ở nước ngoài."
                    }
                ],
                "question": {
                    "zh": "关于女的和她女儿，可以知道什么？",
                    "py": "Guānyú nǚ de hé tā nǚ'ér, kěyǐ zhīdào shénme?",
                    "vi": "Về người phụ nữ và con gái cô ấy, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "妈妈高得多",
                        "py": "Māma gāo de duō",
                        "vi": "Người mẹ cao hơn nhiều"
                    },
                    "B": {
                        "zh": "一样高",
                        "py": "Yíyàng gāo",
                        "vi": "Hai mẹ con cao bằng nhau"
                    },
                    "C": {
                        "zh": "女儿高得多",
                        "py": "Nǚ'ér gāo de duō",
                        "vi": "Con gái cao hơn nhiều"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người mẹ đính chính rõ ràng '其实我跟她一样高' (thực ra tôi với con bé cao bằng nhau)."
            },
            {
                "num": 20,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "走了两三个小时了，还买了这么多东西，真累。我们休息一会儿吧。",
                        "py": "Zǒu le liǎng-sān ge xiǎoshí le, hái mǎi le zhème duō dōngxi, zhēn lèi. Wǒmen xiūxi yíhuìr ba.",
                        "vi": "Đi bộ 2-3 tiếng đồng hồ rồi, lại mua nhiều đồ thế này, mệt quá đi. Tụi mình nghỉ ngơi một lát đi anh."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "那就在这儿坐坐，喝点儿水。",
                        "py": "Nà jiù zài zhèr zuòzuo, hē diǎnr shuǐ.",
                        "vi": "Vậy thì ngồi tạm ở đây, uống chút nước nhé."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "楼上有咖啡店，比这儿安静得多，环境也不错，还有音乐。",
                        "py": "Lóu shang yǒu kāfēidiàn, bǐ zhèr ānjìng de duō, huánjìng yě búcuò, hái yǒu yīnyuè.",
                        "vi": "Trên lầu có quán cà phê, yên tĩnh hơn ở đây nhiều, không gian cũng đẹp lại có cả âm nhạc nữa."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "也好，我们上去喝点儿饮料。",
                        "py": "Yě hǎo, wǒmen shàngqu hē diǎnr yǐnliào.",
                        "vi": "Cũng được, chúng mình lên trên uống chút đồ uống."
                    }
                ],
                "question": {
                    "zh": "他们要做什么？",
                    "py": "Tāmen yào zuò shénme?",
                    "vi": "Họ dự định làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "去咖啡店",
                        "py": "Qù kāfēidiàn",
                        "vi": "Lên quán cà phê"
                    },
                    "B": {
                        "zh": "听音乐会",
                        "py": "Tīng yīnyuèhuì",
                        "vi": "Đi nghe hòa nhạc"
                    },
                    "C": {
                        "zh": "买东西",
                        "py": "Mǎi dōngxi",
                        "vi": "Đi mua sắm"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Cả hai quyết định lên quán cà phê trên lầu nghỉ ngơi, uống nước ('楼上有咖啡店...我们上去喝点儿饮料')."
            }
        ]
    },
    "tab2_reading": {
        "part1_21_25": {
            "options": {
                "A": {
                    "zh": "好，你等我一两分钟，我去一下洗手间。",
                    "py": "Hǎo, nǐ děng wǒ yì-liǎng fēnzhōng, wǒ qù yíxià xǐshǒujiān.",
                    "vi": "Được, bạn đợi tôi một hai phút, tôi đi nhà vệ sinh một chút."
                },
                "B": {
                    "zh": "你怎么在这么远的地方买房子？",
                    "py": "Nǐ zěnme zài zhème yuǎn de dìfang mǎi fángzi?",
                    "vi": "Sao bạn lại mua nhà ở nơi xa như thế này?"
                },
                "C": {
                    "zh": "体育比数学容易多了，也有意思多了。",
                    "py": "Tǐyù bǐ shùxué róngyì duō le, yě yǒu yìsi duō le.",
                    "vi": "Thể dục dễ hơn toán nhiều, cũng thú vị hơn nhiều."
                },
                "D": {
                    "zh": "今天我不上班，我昨天只睡了两三个小时，让我再睡一会儿。",
                    "py": "Jīntiān wǒ bú shàngbān, wǒ zuótiān zhǐ shuì le liǎng-sān ge xiǎoshí, ràng wǒ zài shuì yíhuìr.",
                    "vi": "Hôm nay tôi không đi làm, hôm qua tôi chỉ ngủ được có 2-3 tiếng thôi, cho tôi ngủ thêm một lúc nữa đi."
                },
                "E": {
                    "zh": "当然。我们先坐公共汽车，然后换地铁。",
                    "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.",
                    "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi tàu điện ngầm. (Ví dụ)"
                },
                "F": {
                    "zh": "小方，你跟小丽一样大吗？",
                    "py": "Xiǎofāng, nǐ gēn Xiǎolì yíyàng dà ma?",
                    "vi": "Tiểu Phương, bạn bằng tuổi Tiểu Lệ à?"
                }
            },
            "questions": [
                {
                    "num": 21,
                    "zh": "九点半了，你迟到了，快起床。",
                    "py": "Jiǔ diǎn bàn le, nǐ chídào le, kuài qǐchuáng.",
                    "vi": "9 giờ rưỡi rồi, bạn muộn giờ rồi kìa, mau dậy đi.",
                    "ans": "D",
                    "explain": "Ghép với <strong>D</strong>: Bị giục dậy vì đã muộn, giải thích hôm nay không đi làm và tối qua ngủ ít nên xin ngủ nướng thêm ('让我再睡一会儿')."
                },
                {
                    "num": 22,
                    "zh": "我们去买点儿吃的吧，我早就饿了。",
                    "py": "Wǒmen qù mǎi diǎnr chī de ba, wǒ zǎojiù è le.",
                    "vi": "Chúng mình đi mua chút đồ ăn đi, tôi đói từ sớm rồi.",
                    "ans": "A",
                    "explain": "Ghép với <strong>A</strong>: Đồng ý đi mua đồ ăn nhưng xin đợi 1-2 phút để đi vệ sinh trước ('好，你等我一两分钟，我去一下洗手间')."
                },
                {
                    "num": 23,
                    "zh": "她的生日是五月，我是一月，我比她大一点儿。",
                    "py": "Tā de shēngrì shì wǔ yuè, wǒ shì yī yuè, wǒ bǐ tā dà yìdiǎnr.",
                    "vi": "Sinh nhật cô ấy là tháng 5, tôi tháng 1, tôi lớn hơn cô ấy một chút.",
                    "ans": "F",
                    "explain": "Ghép với <strong>F</strong>: Trả lời câu hỏi có bằng tuổi Tiểu Lệ không ('小方，你跟小丽一样大吗？')."
                },
                {
                    "num": 24,
                    "zh": "你个子那么高，跑得也快，当然觉得容易。",
                    "py": "Nǐ gèzi nàme gāo, pǎo de yě kuài, dāngrán juéde róngyì.",
                    "vi": "Cậu dáng cao như thế, chạy lại nhanh, dĩ nhiên cảm thấy dễ rồi.",
                    "ans": "C",
                    "explain": "Ghép với <strong>C</strong>: Đáp lại ý kiến thể dục dễ hơn toán nhiều ('体育比数学容易多了')."
                },
                {
                    "num": 25,
                    "zh": "虽然远，但是附近有三四个车站，很方便。",
                    "py": "Suīrán yuǎn, dànshì fùjìn yǒu sān-sì ge chēzhàn, hěn fāngbiàn.",
                    "vi": "Tuy rằng xa nhưng gần đó có 3-4 trạm xe, rất thuận tiện.",
                    "ans": "B",
                    "explain": "Ghép với <strong>B</strong>: Trả lời câu hỏi tại sao lại mua nhà ở nơi xa như vậy ('你怎么在这么远的地方买房子？')."
                }
            ]
        },
        "part2_26_30": {
            "words": {
                "A": {
                    "zh": "方便",
                    "py": "fāngbiàn",
                    "vi": "thuận tiện, tiện lợi"
                },
                "B": {
                    "zh": "骑",
                    "py": "qí",
                    "vi": "cưỡi, đạp (xe đạp)"
                },
                "C": {
                    "zh": "换",
                    "py": "huàn",
                    "vi": "đổi, thay thế"
                },
                "D": {
                    "zh": "地方",
                    "py": "dìfang",
                    "vi": "nơi chốn, địa điểm"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "âm thanh, tiếng nói (Ví dụ)"
                },
                "F": {
                    "zh": "旧",
                    "py": "jiù",
                    "vi": "cũ"
                }
            },
            "questions": [
                {
                    "num": 26,
                    "sentence": "这件衣服有点儿（……）了，我不想穿了。",
                    "py": "Zhè jiàn yīfu yǒudiǎnr (……) le, wǒ bù xiǎng chuān le.",
                    "vi": "Chiếc áo này hơi (cũ) rồi, tôi không muốn mặc nữa.",
                    "ans": "F",
                    "explain": "Chọn <strong>F. 旧</strong>: '有点儿旧了' (hơi cũ rồi) phù hợp với lý do không muốn mặc nữa."
                },
                {
                    "num": 27,
                    "sentence": "我还没去过那个（……），漂亮吗？好玩儿吗？",
                    "py": "Wǒ hái méi qùguo nà ge (……), piàoliang ma? Hǎowánr ma?",
                    "vi": "Tôi vẫn chưa từng đến (nơi) đó, có đẹp không? Có vui không?",
                    "ans": "D",
                    "explain": "Chọn <strong>D. 地方</strong>: Danh từ chỉ nơi chốn '那个地方' (địa điểm đó, nơi đó)."
                },
                {
                    "num": 28,
                    "sentence": "你（……）得太快了，慢点儿，小心前边的车。",
                    "py": "Nǐ (……) de tài kuài le, màn diǎnr, xiǎoxīn qiánbian de chē.",
                    "vi": "Bạn (đạp xe) nhanh quá rồi, chậm lại chút, cẩn thận xe phía trước.",
                    "ans": "B",
                    "explain": "Chọn <strong>B. 骑</strong>: Động từ đi xe hai bánh '骑得太快' (đạp xe nhanh quá)."
                },
                {
                    "num": 29,
                    "sentence": "A: 你每天怎么去学校？坐车还是坐地铁？\nB: 坐地铁更快，也更（……）。",
                    "py": "A: Nǐ měitiān zěnme qù xuéxiào? Zuò chē hái shì zuò dìtiě?\nB: Zuò dìtiě gèng kuài, yě gèng (……).",
                    "vi": "A: Mỗi ngày bạn đến trường bằng cách nào? Đi xe buýt hay tàu điện ngầm?\nB: Đi tàu điện ngầm nhanh hơn, cũng (thuận tiện) hơn.",
                    "ans": "A",
                    "explain": "Chọn <strong>A. 方便</strong>: Tính từ '更方便' (thuận tiện hơn, tiện lợi hơn)."
                },
                {
                    "num": 30,
                    "sentence": "A: 这辆车买了十五六年了，总是出问题。\nB: 那（……）一辆新的吧，车出问题不是件小事儿。",
                    "py": "A: Zhè liàng chē mǎi le shíwǔ-liù nián le, zǒngshì chū wèntí.\nB: Nà (……) yí liàng xīn de ba, chē chū wèntí bú shì jiàn xiǎoshìr.",
                    "vi": "A: Chiếc xe này mua 15-16 năm rồi, toàn gặp trục trặc.\nB: Vậy thì (đổi) chiếc mới đi, xe hỏng hóc đâu phải chuyện nhỏ.",
                    "ans": "C",
                    "explain": "Chọn <strong>C. 换</strong>: Động từ '换一辆新的' (thay đổi / mua đổi một chiếc mới)."
                }
            ]
        },
        "part3_31_35": [
            {
                "num": 31,
                "passage": {
                    "zh": "每个周末，我们一家人都去公园或远的地方走走、玩儿玩儿。我们不坐公共汽车，也不坐出租车，我们骑自行车去。很多时候，骑车比开车、坐车方便得多，也快得多。最主要是因为骑车对身体好，对环境也好。",
                    "py": "Měi ge zhōumò, wǒmen yì jiā rén dōu qù gōngyuán huò yuǎn de dìfang zǒuzou, wánrwánr. Wǒmen bú zuò gōnggòng qìchē, yě bú zuò chūzūchē, wǒmen qí zìxíngchē qù. Hěn duō shíhou, qí chē bǐ kāi chē, zuò chē fāngbiàn de duō, yě kuài de duō. Zuì zhǔyào shì yīnwèi qí chē duì shēntǐ hǎo, duì huánjìng yě hǎo.",
                    "vi": "Mỗi dịp cuối tuần, cả gia đình chúng tôi đều đi công viên hoặc những nơi xa dạo chơi, thư giãn. Chúng tôi không đi xe buýt, cũng không đi taxi, chúng tôi đạp xe đạp đi. Rất nhiều khi, đạp xe tiện lợi hơn lái ô tô hay đi xe nhiều, cũng nhanh hơn nhiều. Điều chủ yếu nhất là vì đi xe đạp tốt cho sức khỏe, lại rất thân thiện với môi trường."
                },
                "question": {
                    "zh": "骑车：",
                    "py": "Qí chē:",
                    "vi": "Đi xe đạp:"
                },
                "options": {
                    "A": {
                        "zh": "没有坐车方便",
                        "py": "méiyǒu zuò chē fāngbiàn",
                        "vi": "Không thuận tiện bằng đi xe"
                    },
                    "B": {
                        "zh": "对环境很好",
                        "py": "duì huánjìng hěn hǎo",
                        "vi": "Rất tốt cho môi trường"
                    },
                    "C": {
                        "zh": "不健康",
                        "py": "bù jiànkāng",
                        "vi": "Không tốt cho sức khỏe"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Đoạn văn nêu rõ: '最主要是因为骑车对身体好，对环境也好' (tốt cho sức khỏe và môi trường)."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "以前中国有很多茶馆，但现在越来越少，咖啡店越来越多了，人们走累了可以去咖啡店坐坐，喝点儿咖啡，当然也有茶、牛奶和水。这样的咖啡店比以前的茶馆安静得多，环境也更好，大家很喜欢去。",
                    "py": "Yǐqián Zhōngguó yǒu hěn duō cháguǎn, dàn xiànzài yuè lái yuè shǎo, kāfēidiàn yuè lái yuè duō le, rénmen zǒu lèi le kěyǐ qù kāfēidiàn zuòzuo, hē diǎnr kāfēi, dāngrán yě yǒu chá, niúnǎi hé shuǐ. Zhèyàng de kāfēidiàn bǐ yǐqián de cháguǎn ānjìng de duō, huánjìng yě gèng hǎo, dàjiā hěn xǐhuan qù.",
                    "vi": "Trước đây ở Trung Quốc có rất nhiều quán trà, nhưng bây giờ ngày càng ít, quán cà phê ngày càng nhiều hơn. Mọi người đi bộ mệt có thể vào quán cà phê ngồi nghỉ, uống chút cà phê, dĩ nhiên cũng có cả trà, sữa và nước suối. Những quán cà phê như vậy yên tĩnh hơn quán trà xưa rất nhiều, không gian cũng đẹp hơn, mọi người rất thích đến."
                },
                "question": {
                    "zh": "咖啡店：",
                    "py": "Kāfēidiàn:",
                    "vi": "Quán cà phê:"
                },
                "options": {
                    "A": {
                        "zh": "没有茶馆多",
                        "py": "méiyǒu cháguǎn duō",
                        "vi": "Không nhiều bằng quán trà"
                    },
                    "B": {
                        "zh": "不太安静",
                        "py": "bú tài ānjìng",
                        "vi": "Không yên tĩnh lắm"
                    },
                    "C": {
                        "zh": "环境比茶馆好",
                        "py": "huánjìng bǐ cháguǎn hǎo",
                        "vi": "Không gian tốt hơn quán trà"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Tác giả so sánh '这样的咖啡店比以前的茶馆安静得多，环境也更好' (yên tĩnh hơn và môi trường tốt hơn)."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "我家楼下有一家旧车店，卖“二手”自行车。没有那么多钱买新车的人，可以到这儿来买辆旧的骑骑，特别便宜，也方便。",
                    "py": "Wǒ jiā lóu xià yǒu yì jiā jiù chē diàn, mài “èrshǒu” zìxíngchē. Méiyǒu nàme duō qián mǎi xīn chē de rén, kěyǐ dào zhèr lái mǎi liàng jiù de qíqi, tèbié piányi, yě fāngbiàn.",
                    "vi": "Dưới lầu nhà tôi có một tiệm bán xe cũ, bán xe đạp 'qua tay' (đã qua sử dụng). Những người không có nhiều tiền mua xe mới có thể đến đây mua một chiếc xe cũ để đi, vừa đặc biệt rẻ lại vừa tiện lợi."
                },
                "question": {
                    "zh": "“二手”车的意思是：",
                    "py": "“Èrshǒu” chē de yìsi shì:",
                    "vi": "Ý nghĩa của cụm từ xe 'nhị thủ' (二手) là:"
                },
                "options": {
                    "A": {
                        "zh": "便宜车",
                        "py": "piányi chē",
                        "vi": "Xe rẻ tiền"
                    },
                    "B": {
                        "zh": "新车",
                        "py": "xīn chē",
                        "vi": "Xe mới"
                    },
                    "C": {
                        "zh": "旧车",
                        "py": "jiù chē",
                        "vi": "Xe cũ (xe đã qua sử dụng)"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: '旧车店，卖“二手”自行车...买辆旧的骑骑' chỉ ra '二手车' chính là xe cũ đã qua người khác sử dụng."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "我女儿现在每天都要上历史课、体育课和数学课。她说她最喜欢历史课，因为历史课比数学课和体育课有意思多了。体育课比数学课容易一些，但是没有历史课那么好玩儿。",
                    "py": "Wǒ nǚ'ér xiànzài měitiān dōu yào shàng lìshǐkè, tǐyùkè hé shùxuékè. Tā shuō tā zuì xǐhuan lìshǐkè, yīnwèi lìshǐkè bǐ shùxuékè hé tǐyùkè yǒu yìsi duō le. Tǐyùkè bǐ shùxuékè róngyì yìxiē, dànshì méiyǒu lìshǐkè nàme hǎowánr.",
                    "vi": "Con gái tôi hiện giờ ngày nào cũng phải học tiết lịch sử, thể dục và toán. Cháu bảo cháu thích môn lịch sử nhất, vì lịch sử thú vị hơn toán và thể dục nhiều. Thể dục dễ hơn toán một chút, nhưng không vui như lịch sử."
                },
                "question": {
                    "zh": "女儿最不喜欢上什么课？",
                    "py": "Nǚ'ér zuì bù xǐhuan shàng shénme kè?",
                    "vi": "Cô con gái không thích học môn nào nhất?"
                },
                "options": {
                    "A": {
                        "zh": "数学课",
                        "py": "shùxuékè",
                        "vi": "Môn Toán"
                    },
                    "B": {
                        "zh": "历史课",
                        "py": "lìshǐkè",
                        "vi": "Môn Lịch Sử"
                    },
                    "C": {
                        "zh": "体育课",
                        "py": "tǐyùkè",
                        "vi": "Môn Thể Dục"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Con gái thích lịch sử nhất, thể dục dễ hơn toán, toán là môn khó nhất và ít thú vị nhất nên cô bé không thích môn toán nhất ('数学课')."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "有时候，我真想回到以前。五年前这个地方比现在安静得多，这儿只有一条路，房子也没有现在多。现在这儿有四五条路，路上都是车，大楼也越来越多，饭馆有二三十个呢！",
                    "py": "Yǒushíhou, wǒ zhēn xiǎng huídào yǐqián. Wǔ nián qián zhè ge dìfang bǐ xiànzài ānjìng de duō, zhèr zhǐ yǒu yì tiáo lù, fángzi yě méiyǒu xiànzài duō. Xiànzài zhèr yǒu sì-wǔ tiáo lù, lù shang dōu shì chē, dàlóu yě yuè lái yuè duō, fànguǎn yǒu èr-sānshí ge ne!",
                    "vi": "Có đôi lúc, tôi thật sự rất muốn quay về trước đây. Năm năm trước nơi này yên tĩnh hơn bây giờ nhiều, ở đây chỉ có một con đường độc đạo, nhà cửa cũng không nhiều như hiện tại. Bây giờ ở đây có bốn năm con đường, trên đường toàn là xe cộ, nhà cao tầng ngày càng nhiều, quán ăn có tới hai ba mươi quán lận!"
                },
                "question": {
                    "zh": "这个地方：",
                    "py": "Zhè ge dìfang:",
                    "vi": "Nơi chốn này:"
                },
                "options": {
                    "A": {
                        "zh": "以前没有路",
                        "py": "yǐqián méiyǒu lù",
                        "vi": "Trước đây không có đường"
                    },
                    "B": {
                        "zh": "现在有45条路",
                        "py": "xiànzài yǒu sìshíwǔ tiáo lù",
                        "vi": "Hiện giờ có 45 con đường"
                    },
                    "C": {
                        "zh": "现在的路比以前多",
                        "py": "xiànzài de lù bǐ yǐqián duō",
                        "vi": "Đường sá hiện nay nhiều hơn trước đây"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Trước đây chỉ có một con đường ('只有一条路'), bây giờ có bốn năm con đường ('四五条路'), nên đường sá hiện nay nhiều hơn trước ('现在的路比以前多')."
            }
        ]
    },
    "tab3_writing": {
        "part1_36_40": [
            {
                "num": 36,
                "chunks": [
                    "这个地方",
                    "安静",
                    "比",
                    "那个地方",
                    "一些"
                ],
                "ans": "这个地方比那个地方安静一些。",
                "py": "Zhè ge dìfang bǐ nà ge dìfang ānjìng yìxiē.",
                "vi": "Nơi này yên tĩnh hơn nơi kia một chút.",
                "grammar": "Cấu trúc câu so sánh chữ 比: 'A 比 B + Tính từ + 一些' (mức độ chênh lệch nhỏ)."
            },
            {
                "num": 37,
                "chunks": [
                    "周经理",
                    "都",
                    "一两杯",
                    "喝",
                    "咖啡",
                    "每天"
                ],
                "ans": "周经理每天都要喝一两杯咖啡。",
                "py": "Zhōu jīnglǐ měitiān dōu yào hē yì-liǎng bēi kāfēi.",
                "vi": "Giám đốc Chu mỗi ngày đều phải uống một hai tách cà phê.",
                "grammar": "Trạng ngữ chỉ thời gian thường xuyên '每天都' + số lượng ước lượng '一两杯' làm định ngữ cho '咖啡'."
            },
            {
                "num": 38,
                "chunks": [
                    "自行车",
                    "快",
                    "骑",
                    "比",
                    "得多",
                    "走路"
                ],
                "ans": "骑自行车比走路快得多。",
                "py": "Qí zìxíngchē bǐ zǒulù kuài de duō.",
                "vi": "Đi xe đạp nhanh hơn đi bộ rất nhiều.",
                "grammar": "So sánh hai phương thức hành động: 'A 比 B + Tính từ + 得多' (chênh lệch rất lớn)."
            },
            {
                "num": 39,
                "chunks": [
                    "矮",
                    "朋友",
                    "一点儿",
                    "我",
                    "比",
                    "个子"
                ],
                "ans": "我比朋友个子矮一点儿。",
                "py": "Wǒ bǐ péngyou gèzi ǎi yìdiǎnr.",
                "vi": "Vóc dáng tôi thấp hơn bạn một chút.",
                "grammar": "Câu so sánh mang vị ngữ hình dung từ có chủ ngữ nhỏ: 'A 比 B + Khía cạnh so sánh (个子) + Tính từ + 一点儿'."
            },
            {
                "num": 40,
                "chunks": [
                    "四",
                    "五",
                    "只有",
                    "教室里",
                    "个",
                    "学生"
                ],
                "ans": "教室里只有四五个学生。",
                "py": "Jiàoshì lǐ zhǐ yǒu sì-wǔ ge xuésheng.",
                "vi": "Trong phòng học chỉ có bốn năm học sinh thôi.",
                "grammar": "Câu tồn hiện nơi chốn: Nơi chốn '教室里' + '只有' + Cụm danh từ chỉ số ước lượng '四五个学生'."
            }
        ],
        "part2_41_45": [
            {
                "num": 41,
                "sentence": "我们坐公共汽车去吧，我不会（ 骑 ）自行车。",
                "pinyin": "qí",
                "ans": "骑",
                "hanviet": "Kỵ",
                "compound": "骑车 (qí chē - đi xe hai bánh), 骑马 (qí mǎ - cưỡi ngựa)",
                "vi": "Chúng mình đi xe buýt đi nhé, tôi không biết đi xe đạp."
            },
            {
                "num": 42,
                "sentence": "这条裙子有点儿瘦，我可以（ 换 ）一条吗？",
                "pinyin": "huàn",
                "ans": "换",
                "hanviet": "Hoán",
                "compound": "换衣服 (huàn yīfu - thay quần áo), 交换 (jiāohuàn - trao đổi)",
                "vi": "Chiếc váy này hơi chật một chút, tôi có thể đổi chiếc khác được không?"
            },
            {
                "num": 43,
                "sentence": "我喜欢住在这个地方，因为（ 环 ）境特别好，最重要的是有很多商店。",
                "pinyin": "huán",
                "ans": "环",
                "hanviet": "Hoàn",
                "compound": "环境 (huánjìng - môi trường, cảnh quan)",
                "vi": "Tôi thích sống ở khu vực này, vì môi trường ở đây đặc biệt tốt, quan trọng nhất là có rất nhiều cửa hàng tiện ích."
            },
            {
                "num": 44,
                "sentence": "这儿（ 附 ）近有个学校，每天下午都有很多爸爸妈妈接孩子。",
                "pinyin": "fù",
                "ans": "附",
                "hanviet": "Phụ",
                "compound": "附近 (fùjìn - gần đây, lân cận)",
                "vi": "Gần đây có một trường học, mỗi buổi chiều đều có rất nhiều phụ huynh đến đón con."
            },
            {
                "num": 45,
                "sentence": "在这个学校，我的工作（ 主 ）要是给学生上历史课。",
                "pinyin": "zhǔ",
                "ans": "主",
                "hanviet": "Chủ",
                "compound": "主要 (zhǔyào - chủ yếu, trọng yếu)",
                "vi": "Ở ngôi trường này, công việc của tôi chủ yếu là dạy môn lịch sử cho học sinh."
            }
        ]
    },
    "tab4_textbook": {
        "vocab": [
            {
                "num": 1,
                "zh": "个子",
                "py": "gèzi",
                "pos": "danh từ",
                "vi": "chiều cao, vóc dáng",
                "eg": {
                    "zh": "他的个子很高。",
                    "py": "Tā de gèzi hěn gāo.",
                    "vi": "Dáng người của anh ấy rất cao."
                },
                "id": 1
            },
            {
                "num": 2,
                "zh": "矮",
                "py": "ǎi",
                "pos": "tính từ",
                "vi": "thấp, lùn",
                "eg": {
                    "zh": "我比哥哥矮一点儿。",
                    "py": "Wǒ bǐ gēge ǎi yìdiǎnr.",
                    "vi": "Tôi thấp hơn anh trai một chút."
                },
                "id": 2
            },
            {
                "num": 3,
                "zh": "历史",
                "py": "lìshǐ",
                "pos": "danh từ",
                "vi": "lịch sử",
                "eg": {
                    "zh": "中国历史非常悠久。",
                    "py": "Zhōngguó lìshǐ fēicháng yōujiǔ.",
                    "vi": "Lịch sử Trung Quốc vô cùng lâu đời."
                },
                "id": 3
            },
            {
                "num": 4,
                "zh": "体育",
                "py": "tǐyù",
                "pos": "danh từ",
                "vi": "thể dục, thể thao",
                "eg": {
                    "zh": "今天下午有一节体育课。",
                    "py": "Jīntiān xiàwǔ yǒu yì jié tǐyùkè.",
                    "vi": "Chiều nay có một tiết học thể dục."
                },
                "id": 4
            },
            {
                "num": 5,
                "zh": "数学",
                "py": "shùxué",
                "pos": "danh từ",
                "vi": "toán học, môn toán",
                "eg": {
                    "zh": "数学是一门重要的学科。",
                    "py": "Shùxué shì yì mén zhòngyào de xuékē.",
                    "vi": "Toán học là một môn học quan trọng."
                },
                "id": 5
            },
            {
                "num": 6,
                "zh": "方便",
                "py": "fāngbiàn",
                "pos": "tính từ",
                "vi": "thuận tiện, tiện lợi",
                "eg": {
                    "zh": "坐地铁去机场很方便。",
                    "py": "Zuò dìtiě qù jīchǎng hěn fāngbiàn.",
                    "vi": "Đi tàu điện ngầm ra sân bay rất thuận tiện."
                },
                "id": 6
            },
            {
                "num": 7,
                "zh": "自行车",
                "py": "zìxíngchē",
                "pos": "danh từ",
                "vi": "xe đạp",
                "eg": {
                    "zh": "他每天骑自行车上班。",
                    "py": "Tā měitiān qí zìxíngchē shàngbān.",
                    "vi": "Anh ấy mỗi ngày đều đạp xe đạp đi làm."
                },
                "id": 7
            },
            {
                "num": 8,
                "zh": "骑",
                "py": "qí",
                "pos": "động từ",
                "vi": "cưỡi, đạp xe",
                "eg": {
                    "zh": "周末我们一起去骑车吧。",
                    "py": "Zhōumò wǒmen yìqǐ qù qí chē ba.",
                    "vi": "Cuối tuần chúng mình cùng nhau đi đạp xe nhé."
                },
                "id": 8
            },
            {
                "num": 9,
                "zh": "旧",
                "py": "jiù",
                "pos": "tính từ",
                "vi": "cũ (đối lập với 新)",
                "eg": {
                    "zh": "这辆旧车还能骑吗？",
                    "py": "Zhè liàng jiù chē hái néng qí ma?",
                    "vi": "Chiếc xe cũ này còn đi được không?"
                },
                "id": 9
            },
            {
                "num": 10,
                "zh": "换",
                "py": "huàn",
                "pos": "động từ",
                "vi": "đổi, thay thế",
                "eg": {
                    "zh": "我想换一件大一点儿的。",
                    "py": "Wǒ xiǎng huàn yí jiàn dà yìdiǎnr de.",
                    "vi": "Tôi muốn đổi một chiếc to hơn một chút."
                },
                "id": 10
            },
            {
                "num": 11,
                "zh": "地方",
                "py": "dìfang",
                "pos": "danh từ",
                "vi": "nơi chốn, địa điểm",
                "eg": {
                    "zh": "这个地方的环境真安静。",
                    "py": "Zhè ge dìfang de huánjìng zhēn ānjìng.",
                    "vi": "Không gian nơi này thật yên tĩnh."
                },
                "id": 11
            },
            {
                "num": 12,
                "zh": "中介",
                "py": "zhōngjiè",
                "pos": "danh từ",
                "vi": "môi giới, trung gian",
                "eg": {
                    "zh": "他找了一家中介公司租房子。",
                    "py": "Tā zhǎo le yì jiā zhōngjiè gōngsī zū fángzi.",
                    "vi": "Anh ấy tìm một công ty môi giới để thuê nhà."
                },
                "id": 12
            },
            {
                "num": 13,
                "zh": "主要",
                "py": "zhǔyào",
                "pos": "tính từ",
                "vi": "chủ yếu, trọng yếu",
                "eg": {
                    "zh": "这是我们今天的主要任务。",
                    "py": "Zhè shì wǒmen jīntiān de zhǔyào rènwu.",
                    "vi": "Đây là nhiệm vụ chủ yếu của chúng ta ngày hôm nay."
                },
                "id": 13
            },
            {
                "num": 14,
                "zh": "环境",
                "py": "huánjìng",
                "pos": "danh từ",
                "vi": "môi trường, hoàn cảnh xung quanh",
                "eg": {
                    "zh": "我们要保护生活环境。",
                    "py": "Wǒmen yào bǎohù shēnghuó huánjìng.",
                    "vi": "Chúng ta phải bảo vệ môi trường sống."
                },
                "id": 14
            },
            {
                "num": 15,
                "zh": "附近",
                "py": "fùjìn",
                "pos": "danh từ nơi chốn",
                "vi": "gần đây, lân cận, phụ cận",
                "eg": {
                    "zh": "学校附近有很多好吃的饭馆。",
                    "py": "Xuéxiào fùjìn yǒu hěn duō hǎochī de fànguǎn.",
                    "vi": "Gần trường học có rất nhiều quán ăn ngon."
                },
                "id": 15
            }
        ],
        "grammar": [
            {
                "title": "Câu so sánh chữ “比” kết hợp bổ ngữ mức độ",
                "structure": "A 比 B + Tính từ + 一点儿 / 一些 (Chênh lệch nhỏ) | A 比 B + Tính từ + 得多 / 多了 (Chênh lệch lớn)",
                "explanation": "Dùng để nhấn mạnh mức độ chênh lệch cụ thể trong so sánh hơn kém. Tuyệt đối không thêm các phó từ mức độ như “很”, “非常”, “真” trước tính từ trong câu chữ 比.",
                "examples": [
                    {
                        "zh": "今天比昨天冷一点儿。",
                        "py": "Jīntiān bǐ zuótiān lěng yìdiǎnr.",
                        "vi": "Hôm nay lạnh hơn hôm qua một chút."
                    },
                    {
                        "zh": "数学比历史难多了。",
                        "py": "Shùxué bǐ lìshǐ nán duō le.",
                        "vi": "Môn Toán khó hơn môn Lịch Sử nhiều."
                    },
                    {
                        "zh": "骑自行车比坐公共汽车快得多。",
                        "py": "Qí zìxíngchē bǐ zuò gōnggòng qìchē kuài de duō.",
                        "vi": "Đi xe đạp nhanh hơn đi xe buýt rất nhiều."
                    }
                ]
            },
            {
                "title": "Cách diễn đạt số ước lượng (概数 1)",
                "structure": "Ghép 2 con số liền kề: 一两, 两三, 三四, 四五, 五六, 七八, 八九, 十五六, 二三十...",
                "explanation": "Trong tiếng Trung, ghép hai con số liền kề nhau đi kèm lượng từ để biểu thị số lượng xấp xỉ ước chừng mà không cần thêm từ nối.",
                "examples": [
                    {
                        "zh": "我昨天只睡了两三个小时。",
                        "py": "Wǒ zuótiān zhǐ shuì le liǎng-sān ge xiǎoshí.",
                        "vi": "Hôm qua tôi chỉ ngủ được có hai ba tiếng đồng hồ."
                    },
                    {
                        "zh": "附近有三四个车站，很方便。",
                        "py": "Fùjìn yǒu sān-sì ge chēzhàn, hěn fāngbiàn.",
                        "vi": "Gần đây có ba bốn trạm xe, rất tiện lợi."
                    },
                    {
                        "zh": "教室里只有四五个学生。",
                        "py": "Jiàoshì lǐ zhǐ yǒu sì-wǔ ge xuésheng.",
                        "vi": "Trong lớp học chỉ có bốn năm học sinh thôi."
                    }
                ]
            }
        ],
        "word_expansion": [
            {
                "formula": "换 + 季节 → 换季",
                "py": "huànjì",
                "vi": "Chuyển mùa, giao mùa (thời điểm giao thoa giữa hai mùa thời tiết)",
                "eg": "现在正是换季的时候，很容易感冒。(Bây giờ đúng lúc giao mùa, rất dễ bị cảm cúm.)"
            },
            {
                "formula": "地方 + 上面 → 地面",
                "py": "dìmiàn",
                "vi": "Mặt đất (bề mặt đất đai, đường sá)",
                "eg": "雪停了，地面上积了厚厚的一层雪。(Tuyết đã tạnh, trên mặt đất đọng lại một tầng tuyết dày.)"
            },
            {
                "formula": "主要 + 菜 → 主菜",
                "py": "zhǔcài",
                "vi": "Món ăn chính (món quan trọng nhất trong bữa tiệc)",
                "eg": "今天请客的主菜是一条大清蒸鱼。(Món chính thết khách hôm nay là một con cá hấp lớn.)"
            }
        ],
        "idiom": {
            "proverb_zh": "不可同日而语",
            "proverb_py": "Bù kě tóngrì'éryǔ",
            "proverb_vi": "Không thể cùng một ngày mà bàn luận / Không thể so sánh ngang hàng",
            "story_vi": "Thành ngữ xuất phát từ 'Chiến Quốc Sách · Tề Sách': nói về hai sự vật, hai giai đoạn hoặc hoàn cảnh có sự phát triển và biến đổi quá khác biệt, một bên vượt trội hơn hẳn, không thể đặt ngang hàng cùng nhau trong cùng một bối cảnh để so sánh được. Trong bài học, tác giả hoài niệm về sự đổi mới chóng mặt của đô thị: con đường, nhà cao tầng ngày nay phát triển vượt bậc so với 5 năm trước."
        },
        "polyphonic": [
            {
                "char": "便",
                "sounds": [
                    {
                        "py": "biàn",
                        "meaning": "thuận tiện, tiện lợi, dễ dàng (tính từ)",
                        "example": "方便 (fāngbiàn), 便捷 (biànjié), 便饭 (biànfàn)"
                    },
                    {
                        "py": "pián",
                        "meaning": "giá rẻ, món hời nhỏ (tính từ)",
                        "example": "便宜 (piányi), 占便宜 (zhànpiányi)"
                    }
                ]
            }
        ],
        "expansion_and_idiom": {
            "word_expansion": [
                {
                    "word": "换季",
                    "py": "huànjì",
                    "meaning": "chuyển mùa, đổi mùa (换: thay đổi + 季节: mùa vụ)"
                },
                {
                    "word": "地面",
                    "py": "dìmiàn",
                    "meaning": "mặt đất, bề mặt đường sá (地方 + 上面)"
                },
                {
                    "word": "主菜",
                    "py": "zhǔcài",
                    "meaning": "món ăn chính trong bữa ăn (主要 + 菜)"
                }
            ],
            "proverb": {
                "zh": "不可同日而语",
                "py": "Bù kě tóngrì'éryǔ",
                "vi": "Không thể cùng một ngày mà bàn luận / Không thể so sánh ngang hàng (Dùng khi hai sự việc hoặc hai thời kỳ có sự khác biệt quá lớn, phát triển vượt bậc không thể đem ra so sánh với nhau)."
            }
        }
    },
    "quiz_data": {
        "1": {
            "type": "pic_select",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '数学老师', '讲题', '个子真高', tương ứng hình người thầy đứng bên bảng đen."
        },
        "2": {
            "type": "pic_select",
            "ans": "E",
            "explain": "Đáp án <strong>E</strong>: '听得见吗', '找个安静点儿的地方再跟你说', tương ứng hình người đàn ông bịt tai nghe máy ngoài phố ồn ào."
        },
        "3": {
            "type": "pic_select",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: '请我们吃饭', '饭馆的环境真好', '特别是主菜', tương ứng hình tiệc ăn mừng nhà hàng."
        },
        "4": {
            "type": "pic_select",
            "ans": "F",
            "explain": "Đáp án <strong>F</strong>: '可以用旧车换新车', tương ứng hình trao đổi xem xe ô tô mới."
        },
        "5": {
            "type": "pic_select",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: '踢足球', '上体育课', tương ứng hình học sinh chơi thể thao trên sân cỏ."
        },
        "6": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: Hôm qua mặc váy mà hôm nay tuyết rơi trên mặt đất chứng tỏ hôm nay lạnh hơn hôm qua rất nhiều ('冷得多')."
        },
        "7": {
            "type": "true_false",
            "ans": "×",
            "explain": "Đáp án <strong>Sai (×)</strong>: Họ tìm quán cà phê yên tĩnh gần đó để trò chuyện ('找个安静点儿的咖啡店'), chứ không phải về nhà."
        },
        "8": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: Bố có sức khỏe rất tốt nhờ kiên trì tập luyện mỗi ngày ('主要是因为每天锻炼')."
        },
        "9": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: Làm việc 8-9 tiếng trưa không nghỉ ('能不累吗'), khẳng định anh ấy làm việc rất mệt mỏi."
        },
        "10": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: Hiện giờ học tốt hơn vì đã có hứng thú, suy ra trước kia con trai không thích học."
        },
        "11": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Người nữ khuyên '别买太多，买两三个就行' tức là khuyên nên mua ít thôi ('少买一点儿')."
        },
        "12": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Uống thuốc xong đã đỡ hơn hôm qua một chút ('比昨天好一些了'), tương đương với '好点儿了'."
        },
        "13": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Phương Minh cao hơn Tiểu Cương một chút ('只比我高一点儿'), nên Phương Minh cao hơn."
        },
        "14": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Bay từ Trung Quốc sang Mỹ ('从中国到美国，还要再飞五六个小时'), đang ngồi trên máy bay."
        },
        "15": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '有三四个姓王的老师呢' biểu thị số lượng nhiều ('很多'), không xác định đơn lẻ 3 hay 30."
        },
        "16": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Vì vội đi gặp bạn gái và được biết đi xe đạp nhanh hơn nhiều ('骑车比坐公共汽车快得多'), anh ta sẽ đạp xe."
        },
        "17": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Người nam cảnh báo '雪后晴天比下雪时冷得多', nhắc bạn gái mai trời sẽ rất lạnh không nên mặc váy."
        },
        "18": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Mua xe hơn một trăm tệ và bạn nữ thốt lên '一百多？自行车呀！', đó là xe đạp."
        },
        "19": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Người mẹ đính chính rõ ràng '其实我跟她一样高' (hai mẹ con cao bằng nhau)."
        },
        "20": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Cả hai quyết định lên quán cà phê trên lầu nghỉ ngơi, uống nước ('楼上有咖啡店...我们上去喝点儿饮料')."
        },
        "21": {
            "type": "matching",
            "ans": "D",
            "explain": "Đáp án <strong>D</strong>: Bị giục thức dậy vì đã muộn, xin ngủ nướng thêm vì hôm qua ngủ ít và hôm nay được nghỉ ('让我再睡一会儿')."
        },
        "22": {
            "type": "matching",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Đồng ý đi mua đồ ăn nhưng xin đợi 1-2 phút để đi vệ sinh ('好，你等我一两分钟，我去一下洗手间')."
        },
        "23": {
            "type": "matching",
            "ans": "F",
            "explain": "Đáp án <strong>F</strong>: Trả lời câu hỏi có bằng tuổi Tiểu Lệ không ('小方，你跟小丽一样大吗？')."
        },
        "24": {
            "type": "matching",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Trả lời ý kiến thể dục dễ hơn toán nhiều ('体育比数学容易多了')."
        },
        "25": {
            "type": "matching",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Giải thích tại sao mua nhà ở xa: vì gần nhà có 3-4 trạm xe buýt rất thuận tiện ('虽然远，但是附近有三四个车站')."
        },
        "26": {
            "type": "word_fill",
            "ans": "F",
            "explain": "Đáp án <strong>F. 旧</strong>: '这件衣服有点儿旧了' (chiếc áo này hơi cũ rồi)."
        },
        "27": {
            "type": "word_fill",
            "ans": "D",
            "explain": "Đáp án <strong>D. 地方</strong>: '那个地方' (nơi chốn đó, địa điểm đó)."
        },
        "28": {
            "type": "word_fill",
            "ans": "B",
            "explain": "Đáp án <strong>B. 骑</strong>: '你骑得太快了' (bạn đạp xe nhanh quá)."
        },
        "29": {
            "type": "word_fill",
            "ans": "A",
            "explain": "Đáp án <strong>A. 方便</strong>: '更方便' (đi tàu điện ngầm thuận tiện hơn)."
        },
        "30": {
            "type": "word_fill",
            "ans": "C",
            "explain": "Đáp án <strong>C. 换</strong>: '换一辆新的' (đổi một chiếc xe mới)."
        },
        "31": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: '最主要是因为骑车对身体好，对环境也好' (đi xe đạp rất tốt cho môi trường)."
        },
        "32": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Tác giả so sánh quán cà phê '比以前的茶馆安静得多，环境也更好' (môi trường tốt hơn quán trà)."
        },
        "33": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '旧车店，卖“二手”自行车' xác định '二手车' là xe cũ đã qua sử dụng ('旧车')."
        },
        "34": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Con gái thích lịch sử nhất, thể dục dễ hơn toán, toán là môn khó nhất nên cô bé không thích môn toán nhất ('数学课')."
        },
        "35": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Xưa chỉ có 1 con đường nay có 4-5 con đường, đường sá nhiều hơn trước kia ('现在的路比以前多')."
        }
    }
}
