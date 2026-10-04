# -*- coding: utf-8 -*-
LESSON_DATA = {
    "lesson_info": {
        "id": 14,
        "title_zh": "你把水果拿过来。",
        "title_py": "Nǐ bǎ shuǐguǒ ná guòlái.",
        "title_vi": "Cậu hãy mang trái cây đến đây.",
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
                "label": "Hình A: Người phục vụ đón tiếp và giới thiệu món ăn tại nhà hàng (看菜单 / 点菜)"
            },
            {
                "id": "B",
                "file": "pic_B.png",
                "label": "Hình B: Bé trai ngồi đọc sách, kể chuyện cho ông bà nghe (给爷爷奶奶讲故事)"
            },
            {
                "id": "C",
                "file": "pic_C.png",
                "label": "Hình C: Người phụ nữ cầm chiếc ô bị gió thổi bay rách (刮大风 / 伞被刮跑)"
            },
            {
                "id": "D",
                "file": "pic_D.png",
                "label": "Hình D (Ví dụ): Nhân viên nữ nghe điện thoại (打电话)"
            },
            {
                "id": "E",
                "file": "pic_E.png",
                "label": "Hình E: Cô gái buồn bã nhìn vào chiếc tủ lạnh trống rỗng (把冰箱里的东西吃完了)"
            },
            {
                "id": "F",
                "file": "pic_F.png",
                "label": "Hình F: Đang rửa cốc chén và đĩa ăn dưới vòi nước (先洗杯子再洗盘子)"
            }
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "我的伞，我的伞，怎么突然刮大风了，把伞都刮跑了！",
                        "py": "Wǒ de sǎn, wǒ de sǎn, zěnme tūrán guā dàfēng le, bǎ sǎn dōu guā pǎo le!",
                        "vi": "Ô của tôi, ô của tôi, sao tự nhiên gió to thổi ào tới, cuốn bay chiếc ô của tôi đi mất rồi!"
                    }
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nữ thốt lên vì gió lớn bất ngờ thổi bay mất ô ('突然刮大风了，把伞都刮跑了'), khớp với hình C người phụ nữ cầm ô trong gió bão."
            },
            {
                "num": 2,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "你怎么把冰箱里的东西都吃完了？我们今晚吃什么呀？",
                        "py": "Nǐ zěnme bǎ bīngxiāng li de dōngxi dōu chīwán le? Wǒmen jīnwǎn chī shénme ya?",
                        "vi": "Sao anh lại ăn hết sạch đồ ăn trong tủ lạnh thế này? Tối nay chúng ta ăn gì đây?"
                    },
                    {
                        "speaker": "男",
                        "zh": "你不在家这几天，我一直没出去。",
                        "py": "Nǐ bú zài jiā zhè jǐ tiān, wǒ yìzhí méi chūqù.",
                        "vi": "Mấy ngày em không ở nhà, anh chẳng hề bước chân ra ngoài."
                    }
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Người nữ than thở anh nam đã ăn hết đồ trong tủ lạnh ('把冰箱里的东西都吃完了'), khớp với hình E cô gái nhìn vào tủ lạnh trống rỗng."
            },
            {
                "num": 3,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "这些盘子都要洗干净。",
                        "py": "Zhèxiē pánzi dōu yào xǐ gānjìng.",
                        "vi": "Chỗ đĩa này đều cần phải rửa sạch đấy nhé."
                    },
                    {
                        "speaker": "女",
                        "zh": "我先把杯子洗完，然后再洗盘子。",
                        "py": "Wǒ xiān bǎ bēizi xǐ wán, ránhòu zài xǐ pánzi.",
                        "vi": "Em sẽ rửa cốc xong trước, rồi sau đó mới rửa đĩa."
                    }
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Trò chuyện về việc rửa cốc chén và đĩa ăn ('先把杯子洗完，然后再洗盘子'), khớp với hình F đôi tay đang cọ rửa cốc chén bên bồn rửa."
            },
            {
                "num": 4,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "先生，今天的鱼很新鲜，您要不要来一条？",
                        "py": "Xiānsheng, jīntiān de yú hěn xīnxiān, nín yào bu yào lái yì tiáo?",
                        "vi": "Thưa quý khách, cá hôm nay rất tươi, anh có muốn gọi một con không ạ?"
                    },
                    {
                        "speaker": "男",
                        "zh": "我们先看看菜单，然后再点菜，好吗？",
                        "py": "Wǒmen xiān kànkan càidān, ránhòu zài diǎncài, hǎo ma?",
                        "vi": "Chúng tôi xem qua thực đơn trước, rồi sau đó mới gọi món được chứ?"
                    }
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Nhân viên phục vụ giới thiệu cá tươi và khách đề nghị xem thực đơn gọi món ('先看看菜单，然后再点菜'), khớp với hình A người phục vụ tiếp đón khách tại nhà hàng."
            },
            {
                "num": 5,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "爷爷奶奶，你们别说话，今天我来给你们讲故事。",
                        "py": "Yéye nǎinai, nǐmen bié shuōhuà, jīntiān wǒ lái gěi nǐmen jiǎng gùshi.",
                        "vi": "Ông nội bà nội ơi, hai người đừng nói chuyện, hôm nay cháu sẽ kể chuyện cho ông bà nghe."
                    },
                    {
                        "speaker": "女",
                        "zh": "好啊，爷爷奶奶最喜欢听你讲故事了。",
                        "py": "Hǎo a, yéye nǎinai zuì xǐhuan tīng nǐ jiǎng gùshi le.",
                        "vi": "Được chứ, ông bà thích nghe cháu kể chuyện nhất trần đời."
                    }
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Cậu bé muốn kể chuyện cho ông bà nghe ('今天我来给你们讲故事'), khớp với hình B hai ông bà ngồi quây quần nghe cháu đọc truyện."
            }
        ],
        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {
                    "zh": "今天早上我妻子把车开出去了，要很晚才回来。儿子9点要去学校上课，我只好带他坐地铁。",
                    "py": "Jīntiān zǎoshang wǒ qīzi bǎ chē kāi chūqù le, yào hěn wǎn cái huílái. Érzi jiǔ diǎn yào qù xuéxiào shàngkè, wǒ zhǐhǎo dài tā zuò dìtiě.",
                    "vi": "Sáng nay vợ tôi lái xe đi ra ngoài rồi, mãi muộn mới về. Con trai 9 giờ phải đến trường học, tôi đành phải đưa con đi tàu điện ngầm."
                },
                "statement": {
                    "zh": "他今天坐地铁去上课。",
                    "py": "Tā jīntiān zuò dìtiě qù shàngkè.",
                    "vi": "Hôm nay cậu ấy đi học bằng tàu điện ngầm."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Người bố nói vì xe ô tô vợ đã lái đi nên đành phải đưa con đi tàu điện ngầm ('我只好带他坐地铁'), khớp với câu nhận định."
            },
            {
                "num": 7,
                "passage": {
                    "zh": "常阿姨住在我家楼下，她经常把我叫下去听她唱歌。我很喜欢她的声音，有时候我还和她一起唱呢。",
                    "py": "Cháng āyí zhù zài wǒ jiā lóu xià, tā jīngcháng bǎ wǒ jiào xiàqu tīng tā chànggē. Wǒ hěn xǐhuan tā de shēngyīn, yǒushíhou wǒ hái hé tā yìqǐ chàng ne.",
                    "vi": "Dì Thường sống ở tầng dưới nhà tôi, dì hay gọi tôi xuống nghe dì hát. Tôi rất thích giọng hát của dì, thỉnh thoảng tôi còn hát cùng dì nữa."
                },
                "statement": {
                    "zh": "常阿姨的声音很大。",
                    "py": "Cháng āyí de shēngyīn hěn dà.",
                    "vi": "Tiếng hát/giọng của dì Thường rất to."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Đoạn văn chỉ nói tác giả rất thích giọng hát của dì Thường ('我很喜欢她的声音'), không hề đề cập đến việc giọng của dì rất to ('声音很大')."
            },
            {
                "num": 8,
                "passage": {
                    "zh": "方叔叔爱看教做饭的节目，每天晚上不到7点半都坐在电视前等着节目开始。看完了他马上就开始做，做好了饭就请大家来吃。",
                    "py": "Fāng shūshu ài kàn jiāo zuòfàn de jiémù, měitiān wǎnshang bú dào qī diǎn bàn dōu zuò zài diànshì qián děng zhe jiémù kāishǐ. Kàn wán le tā mǎshàng jiù kāishǐ zuò, zuò hǎo le fàn jiù qǐng dàjiā lái chī.",
                    "vi": "Chú Phương rất thích xem các chương trình dạy nấu ăn, mỗi tối chưa đến 7 rưỡi chú đã ngồi trước tivi đợi chương trình bắt đầu. Xem xong là chú bắt tay vào nấu ngay, nấu xong lại mời mọi người tới thưởng thức."
                },
                "statement": {
                    "zh": "方叔叔喜欢做饭。",
                    "py": "Fāng shūshu xǐhuan zuòfàn.",
                    "vi": "Chú Phương thích nấu ăn."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đoạn văn nói chú Phương rất mê xem chương trình dạy nấu ăn và xem xong là tự mình làm rồi mời mọi người ('爱看教做饭的节目... 马上就开始做'), chứng tỏ chú rất thích nấu ăn."
            },
            {
                "num": 9,
                "passage": {
                    "zh": "一天的工作结束后，小周总是最后一个离开公司的。他每天都要先把办公室打扫干净，然后才回家。",
                    "py": "Yì tiān de gōngzuò jiéshù hòu, Xiǎo Zhōu zǒngshì zuìhòu yí ge líkāi gōngsī de. Tā měitiān dōu yào xiān bǎ bàngōngshì dǎsǎo gānjìng, ránhòu cái huíjiā.",
                    "vi": "Sau khi công việc trong ngày kết thúc, Tiểu Chu luôn là người cuối cùng rời khỏi công ty. Anh ấy ngày nào cũng phải quét dọn văn phòng sạch sẽ trước rồi mới về nhà."
                },
                "statement": {
                    "zh": "小周回家以前要打扫办公室。",
                    "py": "Xiǎo Zhōu huíjiā yǐqián yào dǎsǎo bàngōngshì.",
                    "vi": "Trước khi về nhà Tiểu Chu phải quét dọn văn phòng."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đoạn văn nêu rõ Tiểu Chu luôn quét dọn văn phòng sạch sẽ rồi mới về ('先把办公室打扫干净，然后才回家'), hoàn toàn trùng khớp với câu nhận định."
            },
            {
                "num": 10,
                "passage": {
                    "zh": "方叔叔和白阿姨特别热情，每次我去他们家做客，都要从冰箱里拿出很多吃的喝的来。吃完饭还让我把饮料水果带回家。",
                    "py": "Fāng shūshu hé Bái āyí tèbié rèqíng, měicì wǒ qù tāmen jiā zuòkè, dōu yào cóng bīngxiāng li ná chū hěn duō chī de hē de lái. Chī wán fàn hái ràng wǒ bǎ yǐnliào shuǐguǒ dài huíjiā.",
                    "vi": "Chú Phương và dì Bạch vô cùng nhiệt tình, mỗi lần tôi đến nhà họ làm khách, hai người đều lấy từ tủ lạnh ra rất nhiều đồ ăn thức uống. Ăn cơm xong còn bảo tôi mang đồ uống hoa quả về nhà."
                },
                "statement": {
                    "zh": "去方叔叔家时，我要带很多东西去。",
                    "py": "Qù Fāng shūshu jiā shí, wǒ yào dài hěn duō dōngxi qù.",
                    "vi": "Khi đến nhà chú Phương, tôi phải mang rất nhiều đồ đi."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Đoạn văn nói chú Phương và dì Bạch lấy nhiều đồ ăn mời và sau đó cho tôi mang đồ về ('让我在冰箱里拿出很多吃的喝的... 带回家'), chứ không phải tôi phải mang đồ tới nhà chú."
            }
        ],
        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "我们买点儿香蕉吧，家里没有水果了。",
                        "py": "Wǒmen mǎi diǎnr xiāngjiāo ba, jiā li méiyǒu shuǐguǒ le.",
                        "vi": "Chúng ta mua ít chuối đi, ở nhà hết hoa quả rồi."
                    },
                    {
                        "speaker": "女",
                        "zh": "买西瓜吧，这些香蕉像是放了很久了。",
                        "py": "Mǎi xīguā ba, zhèxiē xiāngjiāo xiàng shì fàng le hěn jiǔ le.",
                        "vi": "Mua dưa hấu đi, mấy quả chuối này trông như để lâu lắm rồi."
                    }
                ],
                "question": {
                    "zh": "女的觉得香蕉怎么样？",
                    "py": "Nǚ de juéde xiāngjiāo zěnmeyàng?",
                    "vi": "Người nữ cảm thấy chuối như thế nào?"
                },
                "options": {
                    "A": {
                        "zh": "不新鲜",
                        "py": "bù xīnxiān",
                        "vi": "Không tươi"
                    },
                    "B": {
                        "zh": "太贵了",
                        "py": "tài guì le",
                        "vi": "Quá đắt"
                    },
                    "C": {
                        "zh": "很新鲜",
                        "py": "hěn xīnxiān",
                        "vi": "Rất tươi"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ nhận xét chuối để lâu lắm rồi ('放了很久了'), đồng nghĩa với chuối không còn tươi (不新鲜)."
            },
            {
                "num": 12,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "你的熊猫画得真好，像真的一样。我要多久才可以像你一样？",
                        "py": "Nǐ de xióngmāo huà de zhēn hǎo, xiàng zhēn de yíyàng. Wǒ yào duōjiǔ cái kěyǐ xiàng nǐ yíyàng?",
                        "vi": "Bạn vẽ gấu trúc đẹp thật đấy, trông y như thật vậy. Tôi phải mất bao lâu mới được như bạn nhỉ?"
                    },
                    {
                        "speaker": "男",
                        "zh": "这不是时间的问题，主要是要有兴趣。",
                        "py": "Zhè bú shì shíjiān de wèntí, zhǔyào shì yào yǒu xìngqù.",
                        "vi": "Đây không phải là vấn đề thời gian, chủ yếu là phải có niềm đam mê yêu thích."
                    }
                ],
                "question": {
                    "zh": "女的觉得熊猫画得怎么样？",
                    "py": "Nǚ de juéde xióngmāo huà de zěnmeyàng?",
                    "vi": "Người nữ cảm thấy tranh vẽ gấu trúc như thế nào?"
                },
                "options": {
                    "A": {
                        "zh": "画了很长时间",
                        "py": "huà le hěn cháng shíjiān",
                        "vi": "Vẽ mất thời gian dài"
                    },
                    "B": {
                        "zh": "画得很像",
                        "py": "huà de hěn xiàng",
                        "vi": "Vẽ rất giống (y như thật)"
                    },
                    "C": {
                        "zh": "画得不好看",
                        "py": "huà de bù hǎokàn",
                        "vi": "Vẽ không đẹp"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ khen '画得真好，像真的一样' (vẽ rất đẹp, y như thật), khớp với đáp án B (画得很像)."
            },
            {
                "num": 13,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "女儿越来越像谁？像你还是像她爸爸？",
                        "py": "Nǚ'ér yuèláiyuè xiàng shéi? Xiàng nǐ háishi xiàng tā bàba?",
                        "vi": "Con gái càng lớn càng giống ai? Giống em hay là giống bố nó?"
                    },
                    {
                        "speaker": "女",
                        "zh": "小时候像我，现在越来越像她爸爸了。",
                        "py": "Xiǎoshíhou xiàng wǒ, xiànzài yuèláiyuè xiàng tā bàba le.",
                        "vi": "Hồi nhỏ thì giống em, giờ càng lớn lại càng giống bố nó."
                    }
                ],
                "question": {
                    "zh": "关于女儿，可以知道什么？",
                    "py": "Guānyú nǚ'ér, kěyǐ zhīdào shénme?",
                    "vi": "Về cô con gái, chúng ta có thể biết điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "以前像妈妈",
                        "py": "yǐqián xiàng māma",
                        "vi": "Trước kia giống mẹ"
                    },
                    "B": {
                        "zh": "以前像爸爸",
                        "py": "yǐqián xiàng bàba",
                        "vi": "Trước kia giống bố"
                    },
                    "C": {
                        "zh": "现在像妈妈",
                        "py": "xiànzài xiàng māma",
                        "vi": "Hiện tại giống mẹ"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người mẹ cho biết hồi nhỏ con gái giống mình ('小时候像我'), khớp với lựa chọn A (以前像妈妈)."
            },
            {
                "num": 14,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "这个字有几个读音？我记得只有一个。",
                        "py": "Zhè ge zì yǒu jǐ ge dùyīn? Wǒ jìde zhǐyǒu yí ge.",
                        "vi": "Chữ này có mấy âm đọc vậy? Tôi nhớ chỉ có một âm thôi mà."
                    },
                    {
                        "speaker": "女",
                        "zh": "我记得有两个。你帮我把词典拿过来，我们一起看看。",
                        "py": "Wǒ jìde yǒu liǎng ge. Nǐ bāng wǒ bǎ cídiǎn ná guòlái, wǒmen yìqǐ kànkan.",
                        "vi": "Tôi nhớ là có hai âm. Bạn lấy hộ tôi cuốn từ điển qua đây, chúng mình cùng xem nhé."
                    }
                ],
                "question": {
                    "zh": "他们想知道什么？",
                    "py": "Tāmen xiǎng zhīdào shénme?",
                    "vi": "Họ muốn biết điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "词典在哪儿",
                        "py": "cídiǎn zài nǎr",
                        "vi": "Từ điển ở đâu"
                    },
                    "B": {
                        "zh": "这个字怎么写",
                        "py": "zhè ge zì zěnme xiě",
                        "vi": "Chữ này viết thế nào"
                    },
                    "C": {
                        "zh": "这个字怎么读",
                        "py": "zhè ge zì zěnme dú",
                        "vi": "Chữ này đọc thế nào"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Hai người đang thảo luận xem chữ này có mấy cách phát âm ('几个读音'), tức là muốn biết chữ này đọc thế nào (这个字怎么读)."
            },
            {
                "num": 15,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "快来看啊，这个节目太有意思了。",
                        "py": "Kuài lái kàn a, zhè ge jiémù tài yǒuyìsi le.",
                        "vi": "Mau lại đây xem này, tiết mục này thú vị quá đi mất."
                    },
                    {
                        "speaker": "女",
                        "zh": "我在洗盘子呢，你把电视声音开大一点儿。",
                        "py": "Wǒ zài xǐ pánzi ne, nǐ bǎ diànshì shēngyīn kāi dà yìdiǎnr.",
                        "vi": "Em đang rửa đĩa, anh bật tiếng tivi to lên một chút đi."
                    }
                ],
                "question": {
                    "zh": "女的想让男的做什么？",
                    "py": "Nǚ de xiǎng ràng nán de zuò shénme?",
                    "vi": "Người nữ muốn người nam làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "洗盘子",
                        "py": "xǐ pánzi",
                        "vi": "Rửa đĩa"
                    },
                    "B": {
                        "zh": "看节目",
                        "py": "kàn jiémù",
                        "vi": "Xem tiết mục"
                    },
                    "C": {
                        "zh": "把声音开大",
                        "py": "bǎ shēngyīn kāi dà",
                        "vi": "Bật tiếng to lên"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nữ đang bận rửa đĩa nên nhờ: '你把电视声音开大一点儿' (anh bật tiếng tivi to lên một chút)."
            }
        ],
        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "他们第一次来我们家，是不是走错路了？已经3点05了。",
                        "py": "Tāmen dì-yī cì lái wǒmen jiā, shì bu shì zǒu cuò lù le? Yǐjīng sān diǎn líng wǔ le.",
                        "vi": "Lần đầu họ đến nhà mình, có phải đi nhầm đường rồi không? Đã 3 giờ 5 phút rồi."
                    },
                    {
                        "speaker": "男",
                        "zh": "你先把盘子洗一下，再从冰箱里把香蕉、苹果、饮料拿出来放好，然后我们下楼去等他们。",
                        "py": "Nǐ xiān bǎ pánzi xǐ yíxià, zài cóng bīngxiāng li bǎ xiāngjiāo, píngguǒ, yǐnliào ná chūlái fàng hǎo, ránhòu wǒmen xiàlóu qù děng tāmen.",
                        "vi": "Em trước hết rửa qua mấy cái đĩa, rồi lấy chuối, táo, đồ uống trong tủ lạnh ra bày biện cẩn thận, sau đó chúng mình xuống lầu đón họ."
                    },
                    {
                        "speaker": "女",
                        "zh": "这些我早就准备好了。这些水果少不少？要不要再买点儿？",
                        "py": "Zhèxiē wǒ zǎojiù zhǔnbèi hǎo le. Zhèxiē shuǐguǒ shǎo bu shǎo? Yào bu yào zài mǎi diǎnr?",
                        "vi": "Những thứ này em chuẩn bị xong từ lâu rồi. Chỗ hoa quả này có ít quá không, có cần mua thêm chút nữa không?"
                    },
                    {
                        "speaker": "男",
                        "zh": "不少，快把衣服穿好，我们下去吧。",
                        "py": "Bù shǎo, kuài bǎ yīfu chuān hǎo, wǒmen xiàqu ba.",
                        "vi": "Không ít đâu, mau mặc quần áo tử tế vào rồi mình cùng xuống dưới thôi."
                    }
                ],
                "question": {
                    "zh": "他们现在要做什么？",
                    "py": "Tāmen xiànzài yào zuò shénme?",
                    "vi": "Bây giờ họ chuẩn bị làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "洗盘子",
                        "py": "xǐ pánzi",
                        "vi": "Rửa đĩa"
                    },
                    "B": {
                        "zh": "买水果",
                        "py": "mǎi shuǐguǒ",
                        "vi": "Mua hoa quả"
                    },
                    "C": {
                        "zh": "下楼",
                        "py": "xiàlóu",
                        "vi": "Xuống lầu đón khách"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Mọi đồ ăn đã chuẩn bị sẵn, người nam giục mặc đồ rồi cùng xuống lầu đợi khách ('快把衣服穿好，我们下去吧 / 下楼去等他们')."
            },
            {
                "num": 17,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "雨下得真大，你的车放哪儿了？我们快点儿跑过去。",
                        "py": "Yǔ xià de zhēn dà, nǐ de chē fàng nǎr le? Wǒmen kuài diǎnr pǎo guòqù.",
                        "vi": "Mưa to quá, xe của anh đỗ ở đâu thế? Mình chạy nhanh qua đó đi."
                    },
                    {
                        "speaker": "男",
                        "zh": "你就在这儿等，我先过去把车开过来，然后你再上车。",
                        "py": "Nǐ jiù zài zhèr děng, wǒ xiān guòqù bǎ chē kāi guòlái, ránhòu nǐ zài shàngchē.",
                        "vi": "Em cứ đứng đây đợi, anh qua đó lái xe lại đây trước rồi em hẵng lên xe."
                    },
                    {
                        "speaker": "女",
                        "zh": "那我把伞给你，你拿着伞走过去。",
                        "py": "Nà wǒ bǎ sǎn gěi nǐ, nǐ ná zhe sǎn zǒu guòqù.",
                        "vi": "Thế em đưa ô cho anh, anh cầm ô đi qua đó nhé."
                    },
                    {
                        "speaker": "男",
                        "zh": "刮这么大的风，伞没有用。",
                        "py": "Guā zhème dà de fēng, sǎn méiyǒu yòng.",
                        "vi": "Gió thổi to thế này, che ô chẳng có tác dụng gì đâu."
                    }
                ],
                "question": {
                    "zh": "男的现在要做什么？",
                    "py": "Nán de xiànzài yào zuò shénme?",
                    "vi": "Người nam bây giờ chuẩn bị làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "开车",
                        "py": "kāichē",
                        "vi": "Đi lái xe qua đón"
                    },
                    "B": {
                        "zh": "买伞",
                        "py": "mǎi sǎn",
                        "vi": "Đi mua ô"
                    },
                    "C": {
                        "zh": "跑步",
                        "py": "pǎobù",
                        "vi": "Chạy bộ"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam dặn người nữ đứng đợi để mình chạy qua lái xe lại đón ('我先过去把车开过来')."
            },
            {
                "num": 18,
                "dialogue": [
                    {
                        "speaker": "男",
                        "zh": "你在看什么呢？一直笑。",
                        "py": "Nǐ zài kàn shénme ne? Yìzhí xiào.",
                        "vi": "Em đang xem cái gì thế? Cứ cười suốt thôi."
                    },
                    {
                        "speaker": "女",
                        "zh": "这个节目里的小猫小狗特别有意思，你先过来看一会儿再打扫房间。",
                        "py": "Zhè ge jiémù li de xiǎomāo xiǎogǒu tèbié yǒuyìsi, nǐ xiān guòlái kàn yíhuìr zài dǎsǎo fángjiān.",
                        "vi": "Chó mèo trong tiết mục này buồn cười lắm, anh lại đây xem một lúc rồi hẵng quét dọn phòng."
                    },
                    {
                        "speaker": "男",
                        "zh": "把电视声音关小点儿，儿子明天考试，正复习呢，别影响他。",
                        "py": "Bǎ diànshì shēngyīn guān xiǎo diǎnr, érzi míngtiān kǎoshì, zhèng fùxí ne, bié yǐngxiǎng tā.",
                        "vi": "Vặn nhỏ tiếng tivi lại một chút đi, con trai mai thi đang ôn bài đấy, đừng làm phiền nó."
                    },
                    {
                        "speaker": "女",
                        "zh": "好，你快过来吧。",
                        "py": "Hǎo, nǐ kuài guòlái ba.",
                        "vi": "Vâng, anh mau qua đây đi."
                    }
                ],
                "question": {
                    "zh": "男的现在要让女的做什么？",
                    "py": "Nán de xiànzài yào ràng nǚ de zuò shénme?",
                    "vi": "Người nam bây giờ muốn người nữ làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "把电视声音关小",
                        "py": "bǎ diànshì shēngyīn guān xiǎo",
                        "vi": "Vặn nhỏ âm lượng tivi"
                    },
                    "B": {
                        "zh": "把房间打扫干净",
                        "py": "bǎ fángjiān dǎsǎo gānjìng",
                        "vi": "Dọn dẹp phòng sạch sẽ"
                    },
                    "C": {
                        "zh": "过来看电视节目",
                        "py": "guòlái kàn diànshì jiémù",
                        "vi": "Lại xem tivi"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam nhắc nhở: '把电视声音关小点儿，儿子明天考试，正复习呢' (vặn nhỏ tiếng tivi lại kẻo ảnh hưởng con học)."
            },
            {
                "num": 19,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "这椅子有点儿矮，坐着不舒服。",
                        "py": "Zhè yǐzi yǒudiǎnr ǎi, zuò zhe bù shūfu.",
                        "vi": "Chiếc ghế này hơi thấp, ngồi không được thoải mái."
                    },
                    {
                        "speaker": "男",
                        "zh": "没关系，我们去那边看看，那儿也有。",
                        "py": "Méi guānxi, wǒmen qù nàbiān kànkan, nàr yě yǒu.",
                        "vi": "Không sao, chúng mình qua phía bên kia xem thử, bên đó cũng có."
                    },
                    {
                        "speaker": "女",
                        "zh": "这层有桌子吗？今天把桌子椅子都一起换了吧。",
                        "py": "Zhè céng yǒu zhuōzi ma? Jīntiān bǎ zhuōzi yǐzi dōu yìqǐ huàn le ba.",
                        "vi": "Tầng này có bàn không anh? Hôm nay tiện thể đổi mới cả bàn lẫn ghế luôn đi."
                    },
                    {
                        "speaker": "男",
                        "zh": "好，我们先看椅子，再看桌子，然后去吃饭。",
                        "py": "Hǎo, wǒmen xiān kàn yǐzi, zài kàn zhuōzi, ránhòu qù chīfàn.",
                        "vi": "Được, chúng mình xem ghế trước, rồi xem bàn, sau đó đi ăn cơm."
                    }
                ],
                "question": {
                    "zh": "他们在做什么？",
                    "py": "Tāmen zài zuò shénme?",
                    "vi": "Họ đang làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "看房子",
                        "py": "kàn fángzi",
                        "vi": "Đi xem nhà"
                    },
                    "B": {
                        "zh": "买桌椅",
                        "py": "mǎi zhuō yǐ",
                        "vi": "Mua bàn ghế"
                    },
                    "C": {
                        "zh": "找饭馆",
                        "py": "zhǎo fànguǎn",
                        "vi": "Tìm quán ăn"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Cặp đôi đang chọn mua bàn ghế mới ('今天把桌子椅子都一起换了吧 / 先看椅子，再看桌子')."
            },
            {
                "num": 20,
                "dialogue": [
                    {
                        "speaker": "女",
                        "zh": "你听，外边是谁的声音？是不是爸爸回来了？",
                        "py": "Nǐ tīng, wàibian shì shéi de shēngyīn? Shì bu shì bàba huílái le?",
                        "vi": "Em nghe xem, bên ngoài là tiếng của ai thế? Có phải bố đã về rồi không?"
                    },
                    {
                        "speaker": "男",
                        "zh": "我听不见呢，你把音乐声音关小些。",
                        "py": "Wǒ tīng bú jiàn ne, nǐ bǎ yīnyuè shēngyīn guān xiǎo xiē.",
                        "vi": "Anh chẳng nghe thấy gì cả, em vặn nhỏ tiếng nhạc lại một chút đi."
                    },
                    {
                        "speaker": "女",
                        "zh": "不是爸爸，是楼上的周叔叔在说话。",
                        "py": "Bú shì bàba, shì lóushàng de Zhōu shūshu zài shuōhuà.",
                        "vi": "Không phải bố, là chú Chu ở tầng trên đang nói chuyện."
                    },
                    {
                        "speaker": "男",
                        "zh": "那我听歌了啊。",
                        "py": "Nà wǒ tīng gē le a.",
                        "vi": "Thế anh nghe nhạc tiếp đây nhé."
                    },
                    {
                        "speaker": "女",
                        "zh": "你别把声音开那么大，我想安静一会儿。",
                        "py": "Nǐ bié bǎ shēngyīn kāi nàme dà, wǒ xiǎng ānjìng yíhuìr.",
                        "vi": "Anh đừng bật tiếng to thế, em muốn yên tĩnh một lát."
                    }
                ],
                "question": {
                    "zh": "女的为什么让男的把声音关小？",
                    "py": "Nǚ de wèishénme ràng nán de bǎ shēngyīn guān xiǎo?",
                    "vi": "Tại sao người nữ bảo người nam vặn nhỏ âm thanh lại?"
                },
                "options": {
                    "A": {
                        "zh": "爸爸回来了",
                        "py": "bàba huílái le",
                        "vi": "Bố đã về rồi"
                    },
                    "B": {
                        "zh": "她要唱歌",
                        "py": "tā yào chànggē",
                        "vi": "Cô ấy muốn hát"
                    },
                    "C": {
                        "zh": "她想安静一会儿",
                        "py": "tā xiǎng ānjìng yíhuìr",
                        "vi": "Cô ấy muốn yên tĩnh một lát"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nữ nói rõ lý do muốn vặn nhỏ tiếng nhạc: '你别把声音开那么大，我想安静一会儿' (anh đừng bật to thế, em muốn yên tĩnh một lúc)."
            }
        ]
    },
    "tab2_reading": {
        "part1_21_25": {
            "options": {
                "A": {
                    "zh": "好的，周经理，我已经把名单准备好了。",
                    "py": "Hǎo de, Zhōu jīnglǐ, wǒ yǐjīng bǎ míngdān zhǔnbèi hǎo le.",
                    "vi": "Vâng thưa giám đốc Chu, em đã chuẩn bị xong danh sách rồi ạ."
                },
                "B": {
                    "zh": "老师，这个故事要写多少个字？",
                    "py": "Lǎoshī, zhè ge gùshi yào xiě duōshao ge zì?",
                    "vi": "Thưa thầy, câu chuyện này cần viết bao nhiêu chữ ạ?"
                },
                "C": {
                    "zh": "你送完孩子就来办公室吗？",
                    "py": "Nǐ sòng wán háizi jiù lái bàngōngshì ma?",
                    "vi": "Anh đưa con đi học xong là tới văn phòng luôn à?"
                },
                "D": {
                    "zh": "先放牛奶，1分钟以后再放鸡蛋。",
                    "py": "Xiān fàng niúnǎi, yì fēnzhōng yǐhòu zài fàng jīdàn.",
                    "vi": "Cho sữa vào trước, 1 phút sau mới cho trứng gà vào."
                },
                "E": {
                    "zh": "当然。我们先坐公共汽车，然后换地铁。",
                    "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.",
                    "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi sang tàu điện ngầm."
                },
                "F": {
                    "zh": "爸爸，下午你来接我吧。",
                    "py": "Bàba, xiàwǔ nǐ lái jiē wǒ ba.",
                    "vi": "Bố ơi, chiều nay bố đến đón con nhé."
                }
            },
            "questions": [
                {
                    "num": 21,
                    "zh": "我先送孩子，再把衣服送到洗衣店，然后去上班。",
                    "py": "Wǒ xiān sòng háizi, zài bǎ yīfu sòng dào xǐyīdiàn, ránhòu qù shàngbān.",
                    "vi": "Tôi đưa con đi trước, rồi mang quần áo đến tiệm giặt, sau đó mới đi làm.",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C</strong>: Câu 21 giải thích lịch trình trước khi đến cơ quan, đối đáp chuẩn xác với câu hỏi C ('你送完孩子就来办公室吗？')."
                },
                {
                    "num": 22,
                    "zh": "这个菜怎么做？先放鸡蛋再放牛奶吗？",
                    "py": "Zhè ge cài zěnme zuò? Xiān fàng jīdàn zài fàng niúnǎi ma?",
                    "vi": "Món này nấu thế nào? Cho trứng gà vào trước rồi mới cho sữa vào à?",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D</strong>: Hỏi về thứ tự nấu món ăn ('先放鸡蛋再放牛奶吗？'), đối đáp khớp với hướng dẫn D ('先放牛奶，1分钟以后再放鸡蛋')."
                },
                {
                    "num": 23,
                    "zh": "好，我先去公司接你妈妈，然后到学校接你。",
                    "py": "Hǎo, wǒ xiān qù gōngsī jiē nǐ māma, ránhòu dào xuéxiào jiē nǐ.",
                    "vi": "Được rồi, bố qua công ty đón mẹ con trước, sau đó sẽ đến trường đón con.",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F</strong>: Lời người bố đồng ý đón sau khi con xin bố đến đón ở câu F ('爸爸，下午你来接我吧')."
                },
                {
                    "num": 24,
                    "zh": "请同学们用黑板上的这10个词写一个小故事。",
                    "py": "Qǐng tóngxuémen yòng hēibǎn shang de zhè shí ge cí xiě yí ge xiǎo gùshi.",
                    "vi": "Mời các em dùng 10 từ trên bảng đen để viết một mẩu truyện ngắn.",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B</strong>: Thầy giáo giao bài tập viết truyện, học sinh hỏi về số lượng chữ B ('老师，这个故事要写多少个字？')."
                },
                {
                    "num": 25,
                    "zh": "小刚，明天都有谁参加会议？你把名单拿过来。",
                    "py": "Xiǎogāng, míngtiān dōu yǒu shéi cānjiā huìyì? Nǐ bǎ míngdān ná guòlái.",
                    "vi": "Tiểu Cương, ngày mai có những ai tham gia cuộc họp? Em đem danh sách qua đây nhé.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A</strong>: Sếp yêu cầu đưa danh sách họp, nhân viên trả lời A ('好的，周经理，我已经把名单准备好了')."
                }
            ]
        },
        "part2_26_30": {
            "options": {
                "A": {
                    "zh": "打扫",
                    "py": "dǎsǎo",
                    "vi": "quét dọn, làm vệ sinh"
                },
                "B": {
                    "zh": "然后",
                    "py": "ránhòu",
                    "vi": "sau đó, tiếp theo"
                },
                "C": {
                    "zh": "节目",
                    "py": "jiémù",
                    "vi": "tiết mục, chương trình"
                },
                "D": {
                    "zh": "简单",
                    "py": "jiǎndān",
                    "vi": "đơn giản, dễ dàng"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "âm thanh, giọng nói (Ví dụ)"
                },
                "F": {
                    "zh": "洗澡",
                    "py": "xǐzǎo",
                    "vi": "tắm rửa"
                }
            },
            "questions": [
                {
                    "num": 26,
                    "zh": "游泳以前应该先吃点儿饭，（ ）休息半个小时。",
                    "py": "Yóuyǒng yǐqián yīnggāi xiān chī diǎnr fàn, ( ) xiūxi bàn ge xiǎoshí.",
                    "vi": "Trước khi bơi lội nên ăn chút cơm trước, (sau đó) nghỉ ngơi nửa tiếng.",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B: 然后</strong> (sau đó): Phù hợp cấu trúc trình tự '先……，然后……' (trước tiên... sau đó...).",
                    "sentence": "游泳以前应该先吃点儿饭，（ ）休息半个小时。"
                },
                {
                    "num": 27,
                    "zh": "小丽，会议室（ ）干净了吗？别忘了把椅子放回去。",
                    "py": "Xiǎolì, huìyìshì ( ) gānjìng le ma? Bié wàng le bǎ yǐzi fàng huíqù.",
                    "vi": "Tiểu Lệ, phòng họp đã (dọn dẹp) sạch sẽ chưa? Đừng quên xếp ghế lại chỗ cũ nhé.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A: 打扫</strong> (quét dọn): Cụm động bổ phổ biến '打扫干净' (quét dọn sạch sẽ).",
                    "sentence": "小丽，会议室（ ）干净了吗？别忘了把椅子放回去。"
                },
                {
                    "num": 28,
                    "zh": "天气这么热，回家以后你先（ ）吧。",
                    "py": "Tiānqì zhème rè, huíjiā yǐhòu nǐ xiān ( ) ba.",
                    "vi": "Thời tiết oi bức thế này, sau khi về nhà anh đi (tắm) trước đi nhé.",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F: 洗澡</strong> (tắm): Trời nóng về nhà đi tắm trước cho mát mẻ, dễ chịu.",
                    "sentence": "天气这么热，回家以后你先（ ）吧。"
                },
                {
                    "num": 29,
                    "zh": "A：小丽，我的包找不到了，你过来帮我找找。\nB：我看了这个（ ）就过去帮你。",
                    "py": "A: Xiǎolì, wǒ de bāo zhǎo bú dào le, nǐ guòlái bāng wǒ zhǎozhao.\nB: Wǒ kàn le zhè ge ( ) jiù guòqù bāng nǐ.",
                    "vi": "A: Tiểu Lệ ơi, anh không tìm thấy túi đâu rồi, em qua đây tìm giúp anh với.\nB: Em xem nốt (chương trình) này rồi sẽ qua giúp anh ngay.",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C: 节目</strong> (tiết mục, chương trình tivi): Đi với động từ '看' (xem hết tiết mục này).",
                    "sentence": "A：小丽，我的包找不到了，你过来帮我找找。\nB：我看了这个（ ）就过去帮你。"
                },
                {
                    "num": 30,
                    "zh": "A：你做的这个菜真好吃，你是怎么做的？\nB：很（ ），先把羊肉放进去，再放些牛奶和菜，等半个小时就做好了。",
                    "py": "A: Nǐ zuò de zhè ge cài zhēn hǎochī, nǐ shì zěnme zuò de?\nB: Hěn ( ), xiān bǎ yángròu fàng jìnqu, zài fàng xiē niúnǎi hé cài, děng bàn ge xiǎoshí jiù zuò hǎo le.",
                    "vi": "A: Món này bạn nấu ngon tuyệt, bạn làm thế nào vậy?\nB: Rất (đơn giản), trước tiên cho thịt cừu vào, sau đó cho thêm ít sữa tươi và rau, đợi nửa tiếng là nấu xong rồi.",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D: 简单</strong> (đơn giản): Hướng dẫn nấu ăn chỉ vài bước cơ bản nên rất đơn giản.",
                    "sentence": "A：你做的这个菜真好吃，你是怎么做的？\nB：很（ ），先把羊肉放进去，再放些牛奶和菜，等半个小时就做好了。"
                }
            ],
            "words": {
                "A": {
                    "zh": "打扫",
                    "py": "dǎsǎo",
                    "vi": "quét dọn, làm vệ sinh"
                },
                "B": {
                    "zh": "然后",
                    "py": "ránhòu",
                    "vi": "sau đó, tiếp theo"
                },
                "C": {
                    "zh": "节目",
                    "py": "jiémù",
                    "vi": "tiết mục, chương trình"
                },
                "D": {
                    "zh": "简单",
                    "py": "jiǎndān",
                    "vi": "đơn giản, dễ dàng"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "âm thanh, giọng nói (Ví dụ)"
                },
                "F": {
                    "zh": "洗澡",
                    "py": "xǐzǎo",
                    "vi": "tắm rửa"
                }
            }
        },
        "part3_31_35": [
            {
                "num": 31,
                "passage": {
                    "zh": "小时候，每年12月25号那天早上，我都能看到床上放着一件礼物。妈妈告诉我，那是前一天晚上的一个穿红衣服的老爷爷把礼物送来的。现在我懂了：其实妈妈就是那个老人，是她在睡着的时候把礼物放在我床上的。",
                    "py": "Xiǎoshíhou, měinián shí'èr yuè èrshíwǔ hào nà tiān zǎoshang, wǒ dōu néng kàndào chuáng shang fàng zhe yí jiàn lǐwù. Māma gàosu wǒ, nà shì qián yì tiān wǎnshang yí ge chuān hóng yīfu de lǎoyéye bǎ lǐwù sòng lái de. Xiànzài wǒ dǒng le: qíshí māma jiù shì nà ge lǎorén, shì tā zài wǒ shuìzháo de shíhou bǎ lǐwù fàng zài wǒ chuáng shang de.",
                    "vi": "Hồi nhỏ, sáng sớm ngày 25 tháng 12 hàng năm, tôi đều nhìn thấy trên giường đặt sẵn một món quà. Mẹ bảo tôi rằng, đó là một ông lão mặc áo đỏ đã mang quà đến vào đêm hôm trước. Bây giờ tôi đã hiểu ra: thực ra mẹ chính là ông lão ấy, mẹ đã lén đặt món quà lên giường khi tôi đang say giấc."
                },
                "question": {
                    "zh": "我现在明白，礼物：",
                    "py": "Wǒ xiànzài míngbai, lǐwù:",
                    "vi": "Bây giờ tôi đã hiểu ra, món quà đó:"
                },
                "options": {
                    "A": {
                        "zh": "是妈妈送来的",
                        "py": "shì māma sòng lái de",
                        "vi": "Là do mẹ tặng"
                    },
                    "B": {
                        "zh": "是老爷爷送来的",
                        "py": "shì lǎoyéye sòng lái de",
                        "vi": "Là do ông lão tặng"
                    },
                    "C": {
                        "zh": "是我爷爷送来的",
                        "py": "shì wǒ yéye sòng lái de",
                        "vi": "Là do ông nội tôi tặng"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Tác giả nhận ra '其实妈妈就是那个老人' (thực ra mẹ chính là ông già Noel đã để lại món quà)."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "有很多人问什么时候吃水果比较健康，在今天的《健康123》节目里，我来告诉大家怎么吃水果对身体最好。其实，上午吃水果最健康，晚饭后和睡觉前最好不要吃。吃水果的时间应该在饭前1到2小时。当然，一定要把水果洗干净再吃。",
                    "py": "Yǒu hěn duō rén wèn shénme shíhou chī shuǐguǒ bǐjiào jiànkāng, zài jīntiān de «Jiànkāng 123» jiémù li, wǒ lái gàosu dàjiā zěnme chī shuǐguǒ duì shēntǐ zuì hǎo. Qíshí, shàngwǔ chī shuǐguǒ zuì jiànkāng, wǎnfàn hòu hé shuìjiào qián zuì hǎo bú yào chī. Chī shuǐguǒ de shíjiān yīnggāi zài fàn qián yī dào èr xiǎoshí. Dāngrán, yídìng yào bǎ shuǐguǒ xǐ gānjìng zài chī.",
                    "vi": "Có rất nhiều người hỏi ăn hoa quả vào lúc nào thì tốt cho sức khỏe, trong chương trình «Sức khỏe 123» hôm nay, tôi xin chia sẻ với mọi người cách ăn hoa quả có lợi nhất cho cơ thể. Thực tế, ăn hoa quả vào buổi sáng là tốt nhất, sau bữa tối và trước khi đi ngủ tốt nhất là không nên ăn. Thời gian ăn hoa quả nên là trước bữa ăn từ 1 đến 2 tiếng. Đương nhiên, nhất định phải rửa thật sạch hoa quả rồi mới ăn."
                },
                "question": {
                    "zh": "什么时候吃水果最好？",
                    "py": "Shénme shíhou chī shuǐguǒ zuì hǎo?",
                    "vi": "Ăn hoa quả vào lúc nào là tốt nhất?"
                },
                "options": {
                    "A": {
                        "zh": "午饭前1-2小时",
                        "py": "wǔfàn qián yī dào èr xiǎoshí",
                        "vi": "Trước bữa trưa 1-2 tiếng (trước bữa ăn)"
                    },
                    "B": {
                        "zh": "晚饭后1-2小时",
                        "py": "wǎnfàn hòu yī dào èr xiǎoshí",
                        "vi": "Sau bữa tối 1-2 tiếng"
                    },
                    "C": {
                        "zh": "睡觉前1-2小时",
                        "py": "shuìjiào qián yī dào èr xiǎoshí",
                        "vi": "Trước khi ngủ 1-2 tiếng"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn nêu '吃水果的时间应该在饭前1到2小时' (nên ăn trước bữa ăn 1-2 giờ) và không nên ăn sau bữa tối hay trước khi ngủ."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "你一定喝过茶，也吃过水果。但你喝过水果茶吗？自己做过水果茶吗？自己做的比外边买的健康得多。其实做水果茶很简单，先把茶放进杯子，再放一些热水，然后把小块儿水果放进去，等一会儿就能喝了。",
                    "py": "Nǐ yídìng hē guo chá, yě chī guo shuǐguǒ. Dàn nǐ hē guo shuǐguǒ chá ma? Zìjǐ zuò guo shuǐguǒ chá ma? Zìjǐ zuò de bǐ wàibian mǎi de jiànkāng de duō. Qíshí zuò shuǐguǒ chá hěn jiǎndān, xiān bǎ chá fàng jìn bēizi, zài fàng yìxiē rèshuǐ, ránhòu bǎ xiǎo kuàir shuǐguǒ fàng jìnqu, děng yíhuìr jiù néng hē le.",
                    "vi": "Bạn chắc hẳn từng uống trà, cũng từng ăn hoa quả. Nhưng bạn đã uống trà hoa quả bao giờ chưa? Đã tự tay làm trà hoa quả chưa? Tự mình làm thì lành mạnh và tốt cho sức khỏe hơn mua ở ngoài nhiều. Thực ra làm trà hoa quả rất đơn giản, trước tiên thả trà vào ly, thêm vào một chút nước nóng, sau đó cho các miếng hoa quả cắt nhỏ vào, đợi một lát là có thể thưởng thức rồi."
                },
                "question": {
                    "zh": "做水果茶：",
                    "py": "Zuò shuǐguǒ chá:",
                    "vi": "Tự làm trà hoa quả:"
                },
                "options": {
                    "A": {
                        "zh": "不容易",
                        "py": "bù róngyì",
                        "vi": "Không dễ dàng"
                    },
                    "B": {
                        "zh": "比外边买的健康",
                        "py": "bǐ wàibian mǎi de jiànkāng",
                        "vi": "Tốt cho sức khỏe hơn mua ở ngoài"
                    },
                    "C": {
                        "zh": "要用大块水果",
                        "py": "yào yòng dà kuài shuǐguǒ",
                        "vi": "Phải dùng hoa quả miếng to"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Đoạn văn khẳng định: '自己做的比外边买的健康得多' (tự làm trà hoa quả tốt cho sức khỏe hơn mua bên ngoài nhiều)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "今天真把我累坏了。我们说好了今天搬家，没想到丈夫突然有事出国。新家在四楼，我只好打电话给搬家公司，请他们把桌椅、电视、电脑都搬上去。等他们走了，我又一个人把每个房间都打扫干净。看了看表，已经晚上9点了。",
                    "py": "Jīntiān zhēn bǎ wǒ lèi huài le. Wǒmen shuō hǎo le jīntiān bānjiā, méi xiǎngdào zhàngfu tūrán yǒushì chūguó. Xīn jiā zài sì lóu, wǒ zhǐhǎo dǎ diànhuà gěi bānjiā gōngsī, qǐng tāmen bǎ zhuō yǐ, diànshì, diànnǎo dōu bān shàngqu. Děng tāmen zǒu le, wǒ yòu yí ge rén bǎ měi ge fángjiān dōu dǎsǎo gānjìng. Kàn le kàn biǎo, yǐjīng wǎnshang jiǔ diǎn le.",
                    "vi": "Hôm nay thật làm tôi mệt lử cả người. Vợ chồng đã hẹn nhau hôm nay chuyển nhà, ai ngờ chồng đột nhiên có việc gấp phải xuất ngoại. Nhà mới ở tận tầng bốn, tôi đành gọi điện cho công ty chuyển nhà, nhờ họ khiêng bàn ghế, tivi, máy tính lên. Đợi họ đi rồi, tôi lại một mình cặm cụi quét dọn từng căn phòng sạch sẽ. Nhìn lại đồng hồ, đã 9 giờ tối mất rồi."
                },
                "question": {
                    "zh": "今天搬家，我：",
                    "py": "Jīntiān bānjiā, wǒ:",
                    "vi": "Hôm nay chuyển nhà, tôi:"
                },
                "options": {
                    "A": {
                        "zh": "请搬家公司帮忙",
                        "py": "qǐng bānjiā gōngsī bāngmáng",
                        "vi": "Nhờ công ty chuyển nhà giúp đỡ"
                    },
                    "B": {
                        "zh": "没打扫房间",
                        "py": "méi dǎsǎo fángjiān",
                        "vi": "Không dọn dẹp phòng"
                    },
                    "C": {
                        "zh": "给丈夫打电话帮忙",
                        "py": "gěi zhàngfu dǎ diànhuà bāngmáng",
                        "vi": "Gọi điện cho chồng về giúp"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người phụ nữ kể: '我只好打电话给搬家公司，请他们把桌椅、电视、电脑都搬上去' (gọi công ty chuyển nhà đến phụ khuân vác)."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "方阿姨的丈夫每天回家都做一样的事：先吃饭，再洗澡，然后从冰箱里拿出一瓶酒，坐在电视前，边看节目边喝。他说，这样的生活是最舒服的。但是方阿姨说，这样的生活是最累的，因为她要把饭做好，还要把杯子、盘子和衣服都洗干净。",
                    "py": "Fāng āyí de zhàngfu měitiān huíjiā dōu zuò yíyàng de shì: xiān chīfàn, zài xǐzǎo, ránhòu cóng bīngxiāng li ná chū yì píng jiǔ, zuò zài diànshì qián, biān kàn jiémù biān hē. Tā shuō, zhèyàng de shēnghuó shì zuì shūfu de. Dànshì Fāng āyí shuō, zhèyàng de shēnghuó shì zuì lèi de, yīnwèi tā yào bǎ fàn zuò hǎo, hái yào bǎ bēizi, pánzi hé yīfu dōu xǐ gānjìng.",
                    "vi": "Chồng của dì Phương ngày nào về đến nhà cũng làm đúng một chuỗi việc: ăn cơm trước, rồi đi tắm, sau đó lấy ra một chai rượu từ tủ lạnh, ngồi trước tivi vừa xem chương trình vừa uống. Chú bảo cuộc sống như thế là thảnh thơi thoải mái nhất. Nhưng dì Phương lại bảo cuộc sống như vậy là mệt mỏi nhất trần đời, bởi vì dì phải nấu cơm tươm tất, lại còn phải rửa sạch cốc chén, đĩa ăn và giặt sạch quần áo."
                },
                "question": {
                    "zh": "方阿姨每天：",
                    "py": "Fāng āyí měitiān:",
                    "vi": "Dì Phương mỗi ngày đều:"
                },
                "options": {
                    "A": {
                        "zh": "都要喝点儿酒",
                        "py": "dōu yào hē diǎnr jiǔ",
                        "vi": "Đều uống chút rượu"
                    },
                    "B": {
                        "zh": "到了家就吃饭",
                        "py": "dào le jiā jiù chīfàn",
                        "vi": "Về đến nhà là ăn cơm"
                    },
                    "C": {
                        "zh": "做饭、洗盘子和杯子",
                        "py": "zuòfàn, xǐ pánzi hé bēizi",
                        "vi": "Nấu cơm, rửa đĩa và cốc chén"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Dì Phương ngày nào cũng phải vất vả '把饭做好，还要把杯子、盘子和衣服都洗干净' (nấu cơm, rửa cốc chén đĩa và giặt đồ)."
            }
        ]
    },
    "tab3_writing": {
        "part1_36_40": [
            {
                "num": 36,
                "chunks": [
                    "把",
                    "大家",
                    "请",
                    "书",
                    "出来",
                    "拿"
                ],
                "ans": "请大家把书拿出来。",
                "py": "Qǐng dàjiā bǎ shū ná chūlái.",
                "vi": "Xin mời mọi người hãy lấy sách ra.",
                "grammar": "Câu chữ 把 kết hợp bổ ngữ xu hướng phức: Thỉnh cầu (请) + Chủ ngữ (大家) + 把 + Tân ngữ (书) + Động từ (拿) + Bổ ngữ xu hướng (出来)."
            },
            {
                "num": 37,
                "chunks": [
                    "写",
                    "名字",
                    "然后",
                    "应该",
                    "先",
                    "做题"
                ],
                "ans": "应该先写名字然后做题。",
                "py": "Yīnggāi xiān xiě míngzi ránhòu zuò tí.",
                "vi": "Nên viết tên trước rồi sau đó mới làm bài.",
                "grammar": "Cấu trúc trình tự thời gian: Năng nguyện (应该) + 先 + Động từ 1 (写名字) + 然后 + Động từ 2 (做题)."
            },
            {
                "num": 38,
                "chunks": [
                    "干净",
                    "把",
                    "房间",
                    "快",
                    "打扫"
                ],
                "ans": "快把房间打扫干净。",
                "py": "Kuài bǎ fángjiān dǎsǎo gānjìng.",
                "vi": "Mau quét dọn phòng cho sạch sẽ đi.",
                "grammar": "Câu chữ 把 dạng mệnh lệnh giục giã: Phó từ (快) + 把 + Tân ngữ (房间) + Động từ (打扫) + Bổ ngữ kết quả (干净)."
            },
            {
                "num": 39,
                "chunks": [
                    "再",
                    "教",
                    "读音",
                    "先",
                    "汉字",
                    "教",
                    "老师"
                ],
                "ans": "老师先教汉字再教读音。",
                "py": "Lǎoshī xiān jiāo hànzì zài jiāo dùyīn.",
                "vi": "Thầy giáo dạy chữ Hán trước rồi mới dạy cách đọc.",
                "grammar": "Cấu trúc thứ tự hành động nối tiếp: Chủ ngữ (老师) + 先 + Động từ 1 (教汉字) + 再 + Động từ 2 (教读音)."
            },
            {
                "num": 40,
                "chunks": [
                    "可以",
                    "你",
                    "小",
                    "关",
                    "一点儿",
                    "电视声音",
                    "把",
                    "吗"
                ],
                "ans": "你可以把电视声音关小一点儿吗？",
                "py": "Nǐ kěyǐ bǎ diànshì shēngyīn guān xiǎo yìdiǎnr ma?",
                "vi": "Bạn có thể vặn nhỏ tiếng tivi lại một chút được không?",
                "grammar": "Câu hỏi chữ 把 mang ngữ khí thỉnh cầu lịch sự: Chủ ngữ (你) + Có thể (可以) + 把 + Tân ngữ (电视声音) + Động từ (关) + Bổ ngữ trạng thái/kết quả (小一点儿) + 吗?"
            }
        ],
        "part2_41_45": [
            {
                "num": 41,
                "sentence": "你把房间打扫得真干（ 净 ）！",
                "pinyin": "jìng",
                "ans": "净",
                "hanviet": "Tịnh",
                "compound": "干净 (gānjìng: sạch sẽ)",
                "vi": "Bạn quét dọn căn phòng thật là sạch sẽ!"
            },
            {
                "num": 42,
                "sentence": "水果就在（ 冰 ）箱里，你把它们都拿出来吧。",
                "pinyin": "bīng",
                "ans": "冰",
                "hanviet": "Băng",
                "compound": "冰箱 (bīngxiāng: tủ lạnh)",
                "vi": "Hoa quả ở ngay trong tủ lạnh đấy, bạn mang hết ra ngoài đi nhé."
            },
            {
                "num": 43,
                "sentence": "你先去洗个（ 澡 ），然后出来吃饭。",
                "pinyin": "zǎo",
                "ans": "澡",
                "hanviet": "Táo",
                "compound": "洗澡 (xǐzǎo: tắm rửa)",
                "vi": "Con đi tắm trước một cái đi, rồi ra ngoài ăn cơm."
            },
            {
                "num": 44,
                "sentence": "外边在刮大（ 风 ），我们别出去了，在家看电视吧。",
                "pinyin": "fēng",
                "ans": "风",
                "hanviet": "Phong",
                "compound": "刮风 (guāfēng: gió thổi, nổi gió)",
                "vi": "Bên ngoài đang nổi gió to lắm, chúng mình đừng đi ra ngoài nữa, ở nhà xem tivi thôi."
            },
            {
                "num": 45,
                "sentence": "其实，做饭很（ 简 ）单，主要是要有兴趣。",
                "pinyin": "jiǎn",
                "ans": "简",
                "hanviet": "Giản",
                "compound": "简单 (jiǎndān: đơn giản)",
                "vi": "Thực ra nấu ăn rất đơn giản, chủ yếu là cần phải có niềm đam mê yêu thích."
            }
        ]
    },
    "tab4_textbook": {
        "vocab": [
            {
                "id": 1,
                "num": 1,
                "zh": "打扫",
                "py": "dǎsǎo",
                "pos": "động từ",
                "vi": "quét dọn, làm vệ sinh",
                "eg": "请把教室打扫一下。"
            },
            {
                "id": 2,
                "num": 2,
                "zh": "干净",
                "py": "gānjìng",
                "pos": "tính từ",
                "vi": "sạch sẽ",
                "eg": "洗得干干净净。"
            },
            {
                "id": 3,
                "num": 3,
                "zh": "然后",
                "py": "ránhòu",
                "pos": "liên từ",
                "vi": "sau đó, tiếp theo",
                "eg": "先吃饭，然后再去看电影。"
            },
            {
                "id": 4,
                "num": 4,
                "zh": "冰箱",
                "py": "bīngxiāng",
                "pos": "danh từ",
                "vi": "tủ lạnh",
                "eg": "把饮料放进冰箱里。"
            },
            {
                "id": 5,
                "num": 5,
                "zh": "洗澡",
                "py": "xǐzǎo",
                "pos": "động từ",
                "vi": "tắm, tắm rửa",
                "eg": "天热了，每天都要洗澡。"
            },
            {
                "id": 6,
                "num": 6,
                "zh": "节目",
                "py": "jiémù",
                "pos": "danh từ",
                "vi": "tiết mục, chương trình",
                "eg": "今晚的电视节目很精彩。"
            },
            {
                "id": 7,
                "num": 7,
                "zh": "月亮",
                "py": "yuèliang",
                "pos": "danh từ",
                "vi": "mặt trăng",
                "eg": "中秋节的月亮特别圆。"
            },
            {
                "id": 8,
                "num": 8,
                "zh": "像",
                "py": "xiàng",
                "pos": "động từ/tính từ",
                "vi": "giống như, tựa như",
                "eg": "这只小猫长得像小老虎。"
            },
            {
                "id": 9,
                "num": 9,
                "zh": "盘子",
                "py": "pánzi",
                "pos": "danh từ",
                "vi": "cái đĩa",
                "eg": "桌子上放着几个水果盘子。"
            },
            {
                "id": 10,
                "num": 10,
                "zh": "刮风",
                "py": "guāfēng",
                "pos": "động từ",
                "vi": "nổi gió, gió thổi",
                "eg": "外面突然刮起了大风。"
            },
            {
                "id": 11,
                "num": 11,
                "zh": "叔叔",
                "py": "shūshu",
                "pos": "danh từ",
                "vi": "chú (em trai bố, chú bác)",
                "eg": "叔叔送给我一辆自行车。"
            },
            {
                "id": 12,
                "num": 12,
                "zh": "阿姨",
                "py": "āyí",
                "pos": "danh từ",
                "vi": "dì, cô, bác gái",
                "eg": "邻居李阿姨非常热情。"
            },
            {
                "id": 13,
                "num": 13,
                "zh": "声音",
                "py": "shēngyīn",
                "pos": "danh từ",
                "vi": "âm thanh, tiếng, giọng",
                "eg": "他说话的声音真好听。"
            },
            {
                "id": 14,
                "num": 14,
                "zh": "故事",
                "py": "gùshi",
                "pos": "danh từ",
                "vi": "câu chuyện",
                "eg": "奶奶给我讲了一个有趣的故事。"
            },
            {
                "id": 15,
                "num": 15,
                "zh": "菜单",
                "py": "càidān",
                "pos": "danh từ",
                "vi": "thực đơn",
                "eg": "服务员，请给我们一份菜单。"
            },
            {
                "id": 16,
                "num": 16,
                "zh": "简单",
                "py": "jiǎndān",
                "pos": "tính từ",
                "vi": "đơn giản, dễ dàng",
                "eg": "这道题非常简单。"
            },
            {
                "id": 17,
                "num": 17,
                "zh": "香蕉",
                "py": "xiāngjiāo",
                "pos": "danh từ",
                "vi": "quả chuối",
                "eg": "香蕉又甜又软。"
            }
        ],
        "grammar": [
            {
                "title": "Câu chữ “把” kết hợp bổ ngữ xu hướng (把字句 2)",
                "structure": "Chủ ngữ + 把 + Tân ngữ + Động từ + Bổ ngữ xu hướng (上/下/进/出/回/过/起 + 来/去)",
                "explanation": "Câu chữ 把 kết hợp với bổ ngữ xu hướng biểu thị thông qua động tác làm cho người hoặc vật chuyển dịch vị trí theo một hướng nhất định (hướng về phía người nói dùng “来”, hướng xa người nói dùng “去”).",
                "examples": [
                    {
                        "zh": "你把水果拿过来。",
                        "py": "Nǐ bǎ shuǐguǒ ná guòlái.",
                        "vi": "Cậu hãy mang đĩa hoa quả lại đây."
                    },
                    {
                        "zh": "老师把书拿进教室去了。",
                        "py": "Lǎoshī bǎ shū ná jìn jiàoshì qù le.",
                        "vi": "Thầy giáo đã mang sách vào trong lớp học rồi."
                    },
                    {
                        "zh": "快把雨伞带回去吧。",
                        "py": "Kuài bǎ yǔsǎn dài huíqù ba.",
                        "vi": "Mau mang ô về nhà đi nhé."
                    }
                ]
            },
            {
                "title": "Cấu trúc biểu thị trình tự thời gian: “先……，再 / 然后……”",
                "structure": "Chủ ngữ + 先 + Hành động 1 + 再 / 然后 + Hành động 2",
                "explanation": "Dùng để nối kết các hành động diễn ra theo trình tự trước - sau liên tiếp: hoàn thành hành động thứ nhất rồi mới tiếp tục làm hành động thứ hai. Có thể kết hợp cả ba: “先……，再……，然后……”.",
                "examples": [
                    {
                        "zh": "我们先看椅子，再看桌子，然后去吃饭。",
                        "py": "Wǒmen xiān kàn yǐzi, zài kàn zhuōzi, ránhòu qù chīfàn.",
                        "vi": "Chúng ta trước xem ghế, rồi xem bàn, sau đó đi ăn cơm."
                    },
                    {
                        "zh": "你先去洗个澡，然后出来吃饭。",
                        "py": "Nǐ xiān qù xǐ ge zǎo, ránhòu chūlái chīfàn.",
                        "vi": "Con hãy đi tắm trước một cái, rồi ra ăn cơm nhé."
                    },
                    {
                        "zh": "回家以后，我先做作业，再玩电脑游戏。",
                        "py": "Huíjiā yǐhòu, wǒ xiān zuò zuòyè, zài wán diànnǎo yóuxì.",
                        "vi": "Sau khi về nhà, em làm bài tập trước rồi mới chơi game trên máy tính."
                    }
                ]
            }
        ],
        "expansion_and_idiom": {
            "word_expansion": [
                {
                    "word": "打扫",
                    "py": "dǎsǎo",
                    "meaning": "quét dọn, làm vệ sinh sạch sẽ"
                },
                {
                    "word": "拿过来",
                    "py": "ná guòlai",
                    "meaning": "mang lại đây, cầm qua đây"
                },
                {
                    "word": "拿出来",
                    "py": "ná chūlai",
                    "meaning": "lấy ra, mang ra ngoài"
                }
            ],
            "proverb": {
                "zh": "饭后百步走，活到九十九",
                "py": "Fàn hòu bǎi bù zǒu, huó dào jiǔshíjiǔ",
                "vi": "Ăn xong đi dạo trăm bước, sống thọ đến chín mươi chín tuổi (Ý nói thói quen đi bộ nhẹ nhàng sau bữa ăn rất có lợi cho tiêu hóa và sức khỏe trường thọ)."
            }
        },
        "polyphonic": [
            {
                "char": "好",
                "sounds": [
                    {
                        "py": "hǎo",
                        "meaning": "tốt, đẹp, hay (tính từ)",
                        "example": "好人 (hǎorén), 很好 (hěn hǎo)"
                    },
                    {
                        "py": "hào",
                        "meaning": "thích, ham chuộng (động từ)",
                        "example": "爱好 (àihào), 好学 (hàoxué)"
                    }
                ]
            },
            {
                "char": "空",
                "sounds": [
                    {
                        "py": "kōng",
                        "meaning": "trống không, rỗng",
                        "example": "天空 (tiānkōng), 空间 (kōngjiān)"
                    },
                    {
                        "py": "kòng",
                        "meaning": "thời gian rảnh rỗi, chỗ trống",
                        "example": "有空儿 (yǒu kòngr), 抽空 (chōukòng)"
                    }
                ]
            }
        ]
    },
    "quiz_data": {
        "1": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: '突然刮大风了，把伞都刮跑了' (gió to thổi bay mất ô) tương ứng hình C."
        },
        "2": {
            "ans": "E",
            "explain": "Đáp án đúng là <strong>E</strong>: '你怎么把冰箱里的东西都吃完了' (ăn hết đồ trong tủ lạnh) tương ứng hình E."
        },
        "3": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: '先把杯子洗完然后再洗盘子' (rửa cốc chén và đĩa) tương ứng hình F."
        },
        "4": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người phục vụ chào mời cá tươi và khách xem thực đơn ('先看看菜单然后再点菜') tương ứng hình A."
        },
        "5": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: '今天我来给你们讲故事' (cháu kể chuyện cho ông bà nghe) tương ứng hình B."
        },
        "6": {
            "ans": "√",
            "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Người bố đưa con đi học bằng tàu điện ngầm ('我只好带他坐地铁')."
        },
        "7": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Đoạn văn chỉ nói tác giả thích tiếng hát của dì Thường, không nói giọng dì rất to."
        },
        "8": {
            "ans": "√",
            "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Chú Phương rất mê chương trình dạy nấu ăn và tự mình vào bếp làm đãi mọi người ('爱看教做饭的节目')."
        },
        "9": {
            "ans": "√",
            "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Tiểu Chu luôn dọn dẹp văn phòng sạch sẽ trước khi về ('先把办公室打扫干净，然后才回家')."
        },
        "10": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Chú Phương và dì Bạch lấy đồ ra mời và cho mang về, không phải tác giả mang nhiều đồ đến."
        },
        "11": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nữ nhận xét chuối để lâu lắm rồi ('放了很久了'), tức là không còn tươi (不新鲜)."
        },
        "12": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ khen vẽ gấu trúc đẹp y như thật ('画得真好，像真的一样'), tức là vẽ rất giống (画得很像)."
        },
        "13": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người mẹ cho biết hồi nhỏ con gái giống mình ('小时候像我')."
        },
        "14": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Hai người đang tra từ điển tìm hiểu xem chữ có mấy âm đọc ('几个读音'), tức là muốn biết chữ này đọc thế nào (这个字怎么读)."
        },
        "15": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nữ bận rửa bát đĩa nên nhờ: '你把电视声音开大一点儿' (bật to tiếng tivi lên)."
        },
        "16": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Chuẩn bị xong mọi thứ, hai người mặc quần áo rồi xuống lầu đón khách ('快把衣服穿好，我们下去吧')."
        },
        "17": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nam chạy qua lái xe lại đón người nữ ('我先过去把车开过来')."
        },
        "18": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nam nhắc vặn nhỏ tiếng tivi để con trai ôn thi ('把电视声音关小点儿，儿子明天考试')."
        },
        "19": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Hai người đang cùng đi chọn mua bàn ghế mới ('今天把桌子椅子都一起换了吧')."
        },
        "20": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nữ bảo vặn nhỏ tiếng nhạc vì muốn yên tĩnh một lúc ('你别把声音开那么大，我想安静一会儿')."
        },
        "21": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Trả lời lịch trình đưa con đi học, giặt đồ rồi mới đi làm ('你送完孩子就来办公室吗？')."
        },
        "22": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D</strong>: Hướng dẫn thứ tự nấu ăn ('先放牛奶，1分钟以后再放鸡蛋')."
        },
        "23": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: Bố đồng ý qua đón con sau giờ học ('爸爸，下午你来接我吧')."
        },
        "24": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Học sinh hỏi số chữ khi làm bài tập viết truyện ('老师，这个故事要写多少个字？')."
        },
        "25": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Nhân viên chuẩn bị xong danh sách người dự họp ('好的，周经理，我已经把名单准备好了')."
        },
        "26": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B: 然后</strong> (sau đó): Biểu thị trình tự nối tiếp sau '先……'."
        },
        "27": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A: 打扫</strong> (quét dọn): Cụm '打扫干净' (quét dọn sạch sẽ)."
        },
        "28": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F: 洗澡</strong> (tắm): Trời nóng về nhà đi tắm rửa trước."
        },
        "29": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C: 节目</strong> (chương trình): Xem xong tiết mục này rồi sang phụ giúp."
        },
        "30": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D: 简单</strong> (đơn giản): Hướng dẫn nấu ăn chỉ vài bước cơ bản."
        },
        "31": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Nhận ra mẹ chính là người tặng quà ('其实妈妈就是那个老人')."
        },
        "32": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Ăn hoa quả tốt nhất là trước bữa ăn 1-2 tiếng ('在饭前1到2小时')."
        },
        "33": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Trà hoa quả tự làm lành mạnh và tốt cho sức khỏe hơn mua ở ngoài ('自己做的比外边买的健康得多')."
        },
        "34": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Nhờ dịch vụ chuyển nhà khiêng bàn ghế, tivi, máy tính ('请他们把桌椅、电视、电脑都搬上去')."
        },
        "35": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Dì Phương ngày nào cũng phải vất vả nấu cơm, dọn dẹp và rửa cốc chén bát đĩa ('做饭、洗盘子和杯子')."
        }
    }
}
