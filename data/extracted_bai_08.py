# -*- coding: utf-8 -*-
LESSON_DATA = {
    "lesson_info": {
        "id": 8,
        "title_zh": "你去哪儿我就去哪儿。",
        "title_py": "Nǐ qù nǎr wǒ jiù qù nǎr.",
        "title_vi": "Em đi đâu thì anh đi đến đó.",
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
            "time": 185,
            "label": "▶ 03:05 Phần 2 (6-10)"
        },
        {
            "time": 425,
            "label": "▶ 07:05 Phần 3 (11-15)"
        },
        {
            "time": 695,
            "label": "▶ 11:35 Phần 4 (16-20)"
        }
    ],
    "tab1_listening": {
        "part1_pictures": [
            {
                "id": "A",
                "file": "pic_A.png",
                "label": "Hình A: Cô gái ngủ nướng trên giường (睡觉 / 还没起床)"
            },
            {
                "id": "B",
                "file": "pic_B.png",
                "label": "Hình B: Hai chú gấu trúc đáng yêu (大熊猫 / 可爱)"
            },
            {
                "id": "C",
                "file": "pic_C.png",
                "label": "Hình C: Cặp đôi cầm bản đồ tìm đường (迷路 / 走错 / 马上就到)"
            },
            {
                "id": "D",
                "file": "pic_D.png",
                "label": "Hình D (Ví dụ): Nhân viên nữ nghe điện thoại (打电话)"
            },
            {
                "id": "E",
                "file": "pic_E.png",
                "label": "Hình E: Tòa nhà chung cư cao tầng (15层 / 电梯 / 房子)"
            },
            {
                "id": "F",
                "file": "pic_F.png",
                "label": "Hình F: Chàng trai đeo thử gọng kính mới (眼镜 / 变化很大 / 满意)"
            }
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "十五层太高了，我都害怕向下看了。",
                        "py": "Shíwǔ céng tài gāo le, wǒ dōu hàipà xiàng xià kàn le.",
                        "vi": "Tầng 15 cao quá, tôi sợ nhìn xuống dưới lắm rồi."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我明白了，那我们看看别的房子。",
                        "py": "Wǒ míngbai le, nà wǒmen kànkan bié de fángzi.",
                        "vi": "Tôi hiểu rồi, vậy chúng ta xem căn nhà khác nhé."
                    }
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Nhắc tới '十五层太高了' (tầng 15 cao quá), '看看别的房子' (xem căn nhà khác) phù hợp với hình tòa nhà chung cư cao tầng."
            },
            {
                "num": 2,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我是第一次来看大熊猫。",
                        "py": "Wǒ shì dì-yī cì lái kàn dàxióngmāo.",
                        "vi": "Đây là lần đầu tiên tôi đến ngắm gấu trúc."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我也是，你看这些大熊猫多可爱啊。",
                        "py": "Wǒ yě shì, nǐ kàn zhèxiē dàxióngmāo duō kě'ài a.",
                        "vi": "Tôi cũng vậy, bạn nhìn xem những chú gấu trúc này đáng yêu biết bao."
                    }
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Nhắc trực tiếp tới '大熊猫' (gấu trúc) và '多可爱啊' (thật đáng yêu)."
            },
            {
                "num": 3,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "都九点一刻了，你怎么还不起床？",
                        "py": "Dōu jiǔ diǎn yí kè le, nǐ zěnme hái bù qǐchuáng?",
                        "vi": "Đã 9 giờ 15 rồi, sao anh vẫn chưa dậy thế?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "星期天又不上班，你也不让我多睡一会儿。",
                        "py": "Xīngqītiān yòu bú shàngbān, nǐ yě bú ràng wǒ duō shuì yíhuìr.",
                        "vi": "Chủ nhật có phải đi làm đâu, em cũng chẳng cho anh ngủ nướng thêm một lát."
                    }
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ giục dậy ('还不起床'), người nam muốn ngủ nướng thêm ('多睡一会儿'), phù hợp hình cô gái nằm ngủ nướng."
            },
            {
                "num": 4,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我们是不是走错了？怎么还没到？",
                        "py": "Wǒmen shì bu shì zǒu cuò le? Zěnme hái méi dào?",
                        "vi": "Có phải chúng ta đi nhầm đường rồi không? Sao vẫn chưa tới nơi?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "别着急，就在前面，马上就到了。",
                        "py": "Bié zháojí, jiù zài qiánmiàn, mǎshàng jiù dào le.",
                        "vi": "Đừng vội, ngay phía trước thôi, sắp tới nơi rồi."
                    }
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Đối thoại lạc đường tìm đường ('走错了', '就在前面，马上就到了'), tương ứng với hình hai người cầm bản đồ."
            },
            {
                "num": 5,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "眼镜怎么样？你觉得满意吗？",
                        "py": "Yǎnjìng zěnmeyàng? Nǐ juéde mǎnyì ma?",
                        "vi": "Kính mắt thế nào? Bạn cảm thấy hài lòng không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "还不错，你看我的变化很大。",
                        "py": "Hái búcuò, nǐ kàn wǒ de biànhuà hěn dà.",
                        "vi": "Cũng khá ổn, bạn nhìn xem tôi thay đổi nhiều lắm."
                    }
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Đang thử kính mắt mới ('眼镜怎么样', '变化很大'), tương ứng hình chàng trai đeo kính."
            }
        ],
        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {
                    "zh": "以前周经理的办公室在一层，最近他搬到了六层，开始坐电梯了。",
                    "py": "Yǐqián Zhōu jīnglǐ de bàngōngshì zài yī céng, zuìjìn tā bāndào le liù céng, kāishǐ zuò diàntī le.",
                    "vi": "Trước đây phòng làm việc của giám đốc Chu ở tầng 1, dạo gần đây ông ấy chuyển lên tầng 6, bắt đầu đi thang máy rồi."
                },
                "statement": {
                    "zh": "周经理换办公室了。",
                    "py": "Zhōu jīnglǐ huàn bàngōngshì le.",
                    "vi": "Giám đốc Chu đã đổi phòng làm việc."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đoạn văn nêu rõ từ tầng 1 chuyển lên tầng 6 ('搬到了六层'), tức là đã đổi văn phòng."
            },
            {
                "num": 7,
                "passage": {
                    "zh": "我明天就回国了，以后不能总跟你见面了，有事请给我电话吧。",
                    "py": "Wǒ míngtiān jiù huíguó le, yǐhòu bù néng zǒng gēn nǐ jiànmiàn le, yǒu shì qǐng gěi wǒ diànhuà ba.",
                    "vi": "Ngày mai tôi về nước rồi, sau này không thể thường xuyên gặp bạn nữa, có việc gì hãy gọi điện thoại cho tôi nhé."
                },
                "statement": {
                    "zh": "他们以前总是见面。",
                    "py": "Tāmen yǐqián zǒngshì jiànmiàn.",
                    "vi": "Họ trước đây thường xuyên gặp mặt."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Câu '以后不能总跟你见面了' (sau này không thể luôn gặp nhau nữa) thể hiện trước đây họ thường xuyên gặp mặt."
            },
            {
                "num": 8,
                "passage": {
                    "zh": "我喜欢自学，没事的时候找一个安静的地方读一本好书是我最大的快乐。",
                    "py": "Wǒ xǐhuan zìxué, méi shì de shíhou zhǎo yí ge ānjìng de dìfang dú yì běn hǎo shū shì wǒ zuì dà de kuàilè.",
                    "vi": "Tôi thích tự học, lúc rảnh rỗi tìm một nơi yên tĩnh đọc một cuốn sách hay là niềm vui lớn nhất của tôi."
                },
                "statement": {
                    "zh": "他喜欢安静的地方。",
                    "py": "Tā xǐhuan ānjìng de dìfang.",
                    "vi": "Anh ấy thích nơi yên tĩnh."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Đoạn văn nói '找一个安静的地方...是我最大的快乐', hoàn toàn khớp với câu nhận định."
            },
            {
                "num": 9,
                "passage": {
                    "zh": "不好意思小姐，这个电梯只到十层，您去十二层要坐右边那个电梯。",
                    "py": "Bù hǎoyìsi xiǎojiě, zhè ge diàntī zhǐ dào shí céng, nín qù shí'èr céng yào zuò yòubian nà ge diàntī.",
                    "vi": "Xin lỗi cô, thang máy này chỉ lên tầng 10 thôi, cô muốn lên tầng 12 thì phải đi thang máy bên phải kia."
                },
                "statement": {
                    "zh": "那位小姐要去十层。",
                    "py": "Nà wèi xiǎojiě yào qù shí céng.",
                    "vi": "Cô gái đó muốn lên tầng 10."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Cô gái muốn lên tầng 12 ('您去十二层'), thang máy này chỉ đến tầng 10 nên nhân viên nhắc đi thang khác."
            },
            {
                "num": 10,
                "passage": {
                    "zh": "603房间的客人刚才打电话来说洗手间有问题，你去看一下吧。",
                    "py": "Liù líng sān fángjiān de kèrén gāngcái dǎ diànhuà lái shuō xǐshǒujiān yǒu wèntí, nǐ qù kàn yíxià ba.",
                    "vi": "Khách phòng 603 vừa mới gọi điện bảo nhà vệ sinh có vấn đề, bạn qua xem một chút đi."
                },
                "statement": {
                    "zh": "他现在在洗手间。",
                    "py": "Tā xiànzài zài xǐshǒujiān.",
                    "vi": "Anh ấy bây giờ đang ở trong nhà vệ sinh."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người nói đang bảo người nghe '你去看一下吧' (bạn đi xem thử đi), anh ấy chưa ở trong nhà vệ sinh."
            }
        ],
        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我想再喝一杯可乐。",
                        "py": "Wǒ xiǎng zài hē yì bēi kělè.",
                        "vi": "Em muốn uống thêm một ly cô-ca nữa."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "再喝一杯你晚上就别想睡觉了。",
                        "py": "Zài hē yì bēi nǐ wǎnshang jiù bié xiǎng shuìjiào le.",
                        "vi": "Uống thêm ly nữa thì tối nay em khỏi ngủ luôn đấy."
                    }
                ],
                "question": {
                    "zh": "男的是什么意思？",
                    "py": "Nán de shì shénme yìsi?",
                    "vi": "Người nam có ý gì?"
                },
                "options": {
                    "A": {
                        "zh": "不让女的喝可乐",
                        "py": "Bú ràng nǚ de hē kělè",
                        "vi": "Không cho người nữ uống cô-ca"
                    },
                    "B": {
                        "zh": "不让女的睡觉",
                        "py": "Bú ràng nǚ de shuìjiào",
                        "vi": "Không cho người nữ đi ngủ"
                    },
                    "C": {
                        "zh": "不想喝可乐",
                        "py": "Bù xiǎng hē kělè",
                        "vi": "Không muốn uống cô-ca"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam cảnh báo uống nữa sẽ mất ngủ, nhằm khuyên ngăn không để người nữ uống thêm cô-ca."
            },
            {
                "num": 12,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "别害怕，只是感冒，休息两天就好了。",
                        "py": "Bié hàipà, zhǐshì gǎnmào, xiūxi liǎng tiān jiù hǎo le.",
                        "vi": "Đừng sợ, chỉ là cảm cúm thôi, nghỉ ngơi hai hôm là khỏi rồi."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "那我让妈妈来照顾我几天。",
                        "py": "Nà wǒ ràng māma lái zhàogù wǒ jǐ tiān.",
                        "vi": "Vậy em bảo mẹ đến chăm sóc em mấy hôm."
                    }
                ],
                "question": {
                    "zh": "关于女的，可以知道什么？",
                    "py": "Guānyú nǚ de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nữ, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "想休息",
                        "py": "Xiǎng xiūxi",
                        "vi": "Muốn nghỉ ngơi"
                    },
                    "B": {
                        "zh": "感冒了",
                        "py": "Gǎnmào le",
                        "vi": "Bị cảm rồi"
                    },
                    "C": {
                        "zh": "要照顾妈妈",
                        "py": "Yào zhàogù māma",
                        "vi": "Phải chăm sóc mẹ"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam an ủi '只是感冒' (chỉ là bị cảm thôi), chứng tỏ người nữ bị cảm cúm."
            },
            {
                "num": 13,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "小姐，请问这儿有人吗？我可以坐这儿吗？",
                        "py": "Xiǎojiě, qǐngwèn zhèr yǒu rén ma? Wǒ kěyǐ zuò zhèr ma?",
                        "vi": "Cô ơi, xin hỏi chỗ này có ai ngồi chưa? Tôi có thể ngồi đây không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "不好意思，我朋友去洗手间了，一会儿就回来。",
                        "py": "Bù hǎoyìsi, wǒ péngyou qù xǐshǒujiān le, yíhuìr jiù huílái.",
                        "vi": "Thật ngại quá, bạn tôi đi vệ sinh rồi, một lát nữa sẽ quay lại."
                    }
                ],
                "question": {
                    "zh": "女的是什么意思？",
                    "py": "Nǚ de shì shénme yìsi?",
                    "vi": "Người nữ có ý gì?"
                },
                "options": {
                    "A": {
                        "zh": "她要去洗手间",
                        "py": "Tā yào qù xǐshǒujiān",
                        "vi": "Cô ấy muốn đi vệ sinh"
                    },
                    "B": {
                        "zh": "这儿有人",
                        "py": "Zhèr yǒu rén",
                        "vi": "Chỗ này đã có người"
                    },
                    "C": {
                        "zh": "男的可以坐这儿",
                        "py": "Nán de kěyǐ zuò zhèr",
                        "vi": "Người nam có thể ngồi đây"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Bạn của cô ấy đi vệ sinh một lát quay lại, nghĩa là chỗ này đã có người ngồi."
            },
            {
                "num": 14,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我儿子又没考好，真着急。",
                        "py": "Wǒ érzi yòu méi kǎo hǎo, zhēn zháojí.",
                        "vi": "Con trai tôi lại thi không tốt rồi, sốt ruột thật đấy."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "孩子身体健康是最重要的。",
                        "py": "Háizi shēntǐ jiànkāng shì zuì zhòngyào de.",
                        "vi": "Sức khỏe của con trẻ mới là quan trọng nhất."
                    }
                ],
                "question": {
                    "zh": "女的为什么着急？",
                    "py": "Nǚ de wèishénme zháojí?",
                    "vi": "Tại sao người nữ lại sốt ruột lo lắng?"
                },
                "options": {
                    "A": {
                        "zh": "儿子身体不健康",
                        "py": "Érzi shēntǐ bù jiànkāng",
                        "vi": "Con trai sức khỏe không tốt"
                    },
                    "B": {
                        "zh": "儿子学习不好",
                        "py": "Érzi xuéxí bù hǎo",
                        "vi": "Con trai học không tốt (kết quả kém)"
                    },
                    "C": {
                        "zh": "儿子没去考试",
                        "py": "Érzi méi qù kǎoshì",
                        "vi": "Con trai không đi thi"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nói '我儿子又没考好' (con trai lại thi không tốt), phản ánh việc học tập chưa tốt."
            },
            {
                "num": 15,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "明天要去面试，这两条裙子你穿哪条？",
                        "py": "Míngtiān yào qù miànshì, zhè liǎng tiáo qúnzi nǐ chuān nǎ tiáo?",
                        "vi": "Ngày mai phải đi phỏng vấn rồi, trong hai chiếc váy này bạn mặc chiếc nào?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "哪条好看我就穿哪条。你再帮我拿一下那件白衬衫。",
                        "py": "Nǎ tiáo hǎokàn wǒ jiù chuān nǎ tiáo. Nǐ zài bāng wǒ ná yíxià nà jiàn bái chènshān.",
                        "vi": "Chiếc nào đẹp thì tôi mặc chiếc đó. Bạn lấy thêm giúp tôi chiếc áo sơ mi trắng kia với."
                    }
                ],
                "question": {
                    "zh": "女的明天做什么？",
                    "py": "Nǚ de míngtiān zuò shénme?",
                    "vi": "Ngày mai người nữ làm việc gì?"
                },
                "options": {
                    "A": {
                        "zh": "买裙子",
                        "py": "Mǎi qúnzi",
                        "vi": "Mua váy"
                    },
                    "B": {
                        "zh": "面试",
                        "py": "Miànshì",
                        "vi": "Đi phỏng vấn"
                    },
                    "C": {
                        "zh": "买衬衫",
                        "py": "Mǎi chènshān",
                        "vi": "Mua áo sơ mi"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: '明天要去面试' nêu rõ mục đích chuẩn bị trang phục là để đi phỏng vấn tuyển dụng."
            }
        ],
        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你也来这儿买东西啊？",
                        "py": "Nǐ yě lái zhèr mǎi dōngxi a?",
                        "vi": "Bạn cũng đến đây mua đồ à?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "是啊，这家超市的东西很便宜。好久不见，我们找个地方坐坐？",
                        "py": "Shì a, zhè jiā chāoshì de dōngxi hěn piányi. Hǎojiǔ bú jiàn, wǒmen zhǎo ge dìfang zuòzuo?",
                        "vi": "Đúng thế, đồ siêu thị này rẻ lắm. Lâu ngày không gặp, tụi mình tìm chỗ ngồi chút đi?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好啊，下了电梯有一个咖啡馆，我们去那儿吧。",
                        "py": "Hǎo a, xià le diàntī yǒu yí ge kāfēiguǎn, wǒmen qù nàr ba.",
                        "vi": "Được chứ, đi xuống thang máy có quán cà phê, chúng ta ra đó nhé."
                    }
                ],
                "question": {
                    "zh": "他们要去哪儿？",
                    "py": "Tāmen yào qù nǎr?",
                    "vi": "Họ định đi đâu?"
                },
                "options": {
                    "A": {
                        "zh": "咖啡馆",
                        "py": "Kāfēiguǎn",
                        "vi": "Quán cà phê"
                    },
                    "B": {
                        "zh": "电梯那儿",
                        "py": "Diàntī nàr",
                        "vi": "Chỗ thang máy"
                    },
                    "C": {
                        "zh": "超市",
                        "py": "Chāoshì",
                        "vi": "Siêu thị"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ gợi ý '下了电梯有一个咖啡馆，我们去那儿吧' (xuống thang máy có quán cà phê, chúng ta ra đó nhé)."
            },
            {
                "num": 17,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你吃药了吗？",
                        "py": "Nǐ chī yào le ma?",
                        "vi": "Em uống thuốc chưa?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "还没有，我吃完饭再吃。",
                        "py": "Hái méiyǒu, wǒ chī wán fàn zài chī.",
                        "vi": "Vẫn chưa, em ăn cơm xong rồi mới uống."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "今天我们吃面条？",
                        "py": "Jīntiān wǒmen chī miàntiáo?",
                        "vi": "Hôm nay chúng mình ăn mì nhé?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "是，吃鸡蛋面，马上就好。",
                        "py": "Shì, chī jīdànmiàn, mǎshàng jiù hǎo.",
                        "vi": "Vâng, ăn mì trứng, sắp xong ngay rồi."
                    }
                ],
                "question": {
                    "zh": "他们今天吃什么？",
                    "py": "Tāmen jīntiān chī shénme?",
                    "vi": "Hôm nay họ ăn món gì?"
                },
                "options": {
                    "A": {
                        "zh": "药",
                        "py": "Yào",
                        "vi": "Thuốc"
                    },
                    "B": {
                        "zh": "面条",
                        "py": "Miàntiáo",
                        "vi": "Mì sợi"
                    },
                    "C": {
                        "zh": "鸡蛋",
                        "py": "Jīdàn",
                        "vi": "Trứng gà"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Cả hai thống nhất ăn mì trứng ('吃鸡蛋面' / '吃面条')."
            },
            {
                "num": 18,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你好，我的雨伞可能忘在你们饭店了。",
                        "py": "Nǐhǎo, wǒ de yǔsǎn kěnéng wàng zài nǐmen fàndiàn le.",
                        "vi": "Chào cô, chiếc ô của tôi có thể bỏ quên ở nhà hàng của các bạn rồi."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "您的雨伞是什么颜色的？",
                        "py": "Nín de yǔsǎn shì shénme yánsè de?",
                        "vi": "Chiếc ô của quý khách màu gì ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "黑色的。",
                        "py": "Hēisè de.",
                        "vi": "Màu đen."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "是这个吗？我们在洗手间里看到的。",
                        "py": "Shì zhè ge ma? Wǒmen zài xǐshǒujiān lǐ kàndào de.",
                        "vi": "Có phải cái này không? Chúng tôi nhìn thấy ở trong nhà vệ sinh đấy."
                    }
                ],
                "question": {
                    "zh": "男的为什么去饭店？",
                    "py": "Nán de wèishénme qù fàndiàn?",
                    "vi": "Tại sao người nam lại đến nhà hàng?"
                },
                "options": {
                    "A": {
                        "zh": "去洗手间",
                        "py": "Qù xǐshǒujiān",
                        "vi": "Đi nhà vệ sinh"
                    },
                    "B": {
                        "zh": "找雨伞",
                        "py": "Zhǎo yǔsǎn",
                        "vi": "Tìm chiếc ô để quên"
                    },
                    "C": {
                        "zh": "去吃饭",
                        "py": "Qù chīfàn",
                        "vi": "Đi ăn cơm"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam quay lại nhà hàng vì để quên ô ('我的雨伞可能忘在你们饭店了')."
            },
            {
                "num": 19,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我们一起吃个饭吧？",
                        "py": "Wǒmen yìqǐ chī ge fàn ba?",
                        "vi": "Chúng mình cùng đi ăn bữa cơm nhé?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好啊，哪天吃？",
                        "py": "Hǎo a, nǎ tiān chī?",
                        "vi": "Được chứ, ăn hôm nào thế?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "那明天中午老地方见？",
                        "py": "Nà míngtiān zhōngwǔ lǎo dìfang jiàn?",
                        "vi": "Vậy trưa mai gặp nhau ở chỗ cũ nhé?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好的，明天见。",
                        "py": "Hǎo de, míngtiān jiàn.",
                        "vi": "Được, mai gặp nhé."
                    }
                ],
                "question": {
                    "zh": "关于女的，可以知道什么？",
                    "py": "Guānyú nǚ de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nữ, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "明天中午不忙",
                        "py": "Míngtiān zhōngwǔ bù máng",
                        "vi": "Trưa mai không bận (rảnh rỗi)"
                    },
                    "B": {
                        "zh": "不想跟男的吃饭",
                        "py": "Bù xiǎng gēn nán de chīfàn",
                        "vi": "Không muốn đi ăn với người nam"
                    },
                    "C": {
                        "zh": "不知道哪天吃饭",
                        "py": "Bù zhīdào nǎ tiān chīfàn",
                        "vi": "Không biết ăn cơm hôm nào"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Khi người nam hẹn trưa mai ở chỗ cũ, người nữ đồng ý ngay chứng tỏ trưa mai cô ấy rảnh (không bận)."
            },
            {
                "num": 20,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你这次汉语考得怎么样？",
                        "py": "Nǐ zhè cì hànyǔ kǎo de zěnmeyàng?",
                        "vi": "Kỳ thi tiếng Hán lần này bạn làm bài thế nào?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我考得不太好，我只会做第一题，汉字几乎一个都不会写。",
                        "py": "Wǒ kǎo de bú tài hǎo, wǒ zhǐ huì zuò dì-yī tí, hànzì jīhū yí ge dōu bú huì xiě.",
                        "vi": "Tôi thi không tốt lắm, tôi chỉ biết làm câu đầu tiên, chữ Hán hầu như chẳng biết viết chữ nào."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "别着急，慢慢来。",
                        "py": "Bié zháojí, mànmàn lái.",
                        "vi": "Đừng vội, từ từ sẽ tiến bộ thôi."
                    }
                ],
                "question": {
                    "zh": "关于女的，可以知道什么？",
                    "py": "Guānyú nǚ de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nữ, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "考得很好",
                        "py": "Kǎo de hěn hǎo",
                        "vi": "Thi rất tốt"
                    },
                    "B": {
                        "zh": "不会写汉字",
                        "py": "Bú huì xiě hànzì",
                        "vi": "Không biết viết chữ Hán"
                    },
                    "C": {
                        "zh": "一个题都不会",
                        "py": "Yí ge tí dōu bú huì",
                        "vi": "Một câu cũng không biết làm"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ tự nói '汉字几乎一个都不会写' (chữ Hán hầu như chẳng biết viết chữ nào)."
            }
        ]
    },
    "tab2_reading": {
        "part1_21_25": {
            "options": {
                "A": {
                    "zh": "你下课以后去哪儿学习？",
                    "py": "Nǐ xiàkè yǐhòu qù nǎr xuéxí?",
                    "vi": "Tan học xong bạn đi đâu học?"
                },
                "B": {
                    "zh": "周末你有什么打算？",
                    "py": "Zhōumò nǐ yǒu shénme dǎsuan?",
                    "vi": "Cuối tuần bạn có dự định gì?"
                },
                "C": {
                    "zh": "听说你最近打算买房子了？",
                    "py": "Tīngshuō nǐ zuìjìn dǎsuan mǎi fángzi le?",
                    "vi": "Nghe nói dạo này bạn định mua nhà à?"
                },
                "D": {
                    "zh": "可能吃的东西有问题，不太舒服。",
                    "py": "Kěnéng chī de dōngxi yǒu wèntí, bú tài shūfu.",
                    "vi": "Có thể đồ ăn có vấn đề, tôi thấy không được khỏe lắm."
                },
                "E": {
                    "zh": "当然。我们先坐公共汽车，然后换地铁。",
                    "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.",
                    "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi tàu điện ngầm. (Ví dụ)"
                },
                "F": {
                    "zh": "那我们再买几块吧。",
                    "py": "Nà wǒmen zài mǎi jǐ kuài ba.",
                    "vi": "Vậy chúng mình mua thêm mấy miếng nữa đi."
                }
            },
            "questions": [
                {
                    "num": 21,
                    "zh": "你怎么又去洗手间啊？",
                    "py": "Nǐ zěnme yòu qù xǐshǒujiān a?",
                    "vi": "Sao bạn lại đi nhà vệ sinh nữa thế?",
                    "ans": "D",
                    "explain": "Ghép với <strong>D</strong>: Hỏi tại sao lại đi vệ sinh liên tục, trả lời do đồ ăn có vấn đề làm bụng dạ khó chịu."
                },
                {
                    "num": 22,
                    "zh": "这种蛋糕很甜，孩子们很喜欢。",
                    "py": "Zhè zhǒng dàngāo hěn tián, háizimen hěn xǐhuan.",
                    "vi": "Loại bánh ngọt này rất ngọt, bọn trẻ con thích lắm.",
                    "ans": "F",
                    "explain": "Ghép với <strong>F</strong>: Bánh ngon bọn trẻ thích, nên đề nghị mua thêm mấy miếng nữa ('那我们再买几块吧')."
                },
                {
                    "num": 23,
                    "zh": "是啊，看了很多，但是都不太满意。",
                    "py": "Shì a, kàn le hěn duō, dànshì dōu bú tài mǎnyì.",
                    "vi": "Đúng vậy, xem nhiều nơi rồi nhưng đều không hài lòng lắm.",
                    "ans": "C",
                    "explain": "Ghép với <strong>C</strong>: Trả lời cho câu hỏi nghe nói gần đây định mua nhà ('听说你最近打算买房子了？')."
                },
                {
                    "num": 24,
                    "zh": "我要去跟几个老朋友见面。",
                    "py": "Wǒ yào qù gēn jǐ ge lǎo péngyou jiànmiàn.",
                    "vi": "Tôi định đi gặp mấy người bạn cũ.",
                    "ans": "B",
                    "explain": "Ghép với <strong>B</strong>: Trả lời cho câu hỏi cuối tuần có kế hoạch gì ('周末你有什么打算？')."
                },
                {
                    "num": 25,
                    "zh": "哪儿安静我就去哪儿。",
                    "py": "Nǎr ānjìng wǒ jiù qù nǎr.",
                    "vi": "Chỗ nào yên tĩnh thì tôi đi chỗ đó.",
                    "ans": "A",
                    "explain": "Ghép với <strong>A</strong>: Trả lời cho câu hỏi tan học xong đi đâu học bằng cấu trúc lặp đại từ nghi vấn ('哪儿...就去哪儿')."
                }
            ]
        },
        "part2_26_30": {
            "words": {
                "A": {
                    "zh": "电梯",
                    "py": "diàntī",
                    "vi": "thang máy"
                },
                "B": {
                    "zh": "洗手间",
                    "py": "xǐshǒujiān",
                    "vi": "nhà vệ sinh"
                },
                "C": {
                    "zh": "几乎",
                    "py": "jīhū",
                    "vi": "hầu như, gần như"
                },
                "D": {
                    "zh": "重要",
                    "py": "zhòngyào",
                    "vi": "quan trọng"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "âm thanh, giọng nói (Ví dụ)"
                },
                "F": {
                    "zh": "又",
                    "py": "yòu",
                    "vi": "lại (phó từ diễn tả hành động lặp lại)"
                }
            },
            "questions": [
                {
                    "num": 26,
                    "sentence": "你等我一会儿，我去一下（……），马上回来。",
                    "py": "Nǐ děng wǒ yíhuìr, wǒ qù yíxià (……), mǎshàng huílái.",
                    "vi": "Bạn đợi tôi một lát, tôi đi (nhà vệ sinh) một chút, sẽ về ngay.",
                    "ans": "B",
                    "explain": "Chọn <strong>B. 洗手间</strong>: Cụm từ thông dụng '去一下洗手间' (đi vệ sinh một lát)."
                },
                {
                    "num": 27,
                    "sentence": "他（……）每天都要去公园锻炼一个小时。",
                    "py": "Tā (……) měitiān dōu yào qù gōngyuán duànliàn yí ge xiǎoshí.",
                    "vi": "Anh ấy (hầu như) ngày nào cũng ra công viên tập luyện một tiếng đồng hồ.",
                    "ans": "C",
                    "explain": "Chọn <strong>C. 几乎</strong>: Phó từ '几乎每天' biểu thị tần suất gần như tuyệt đối mỗi ngày."
                },
                {
                    "num": 28,
                    "sentence": "（……）里人太多了，我们别坐了。",
                    "py": "(……) lǐ rén tài duō le, wǒmen bié zuò le.",
                    "vi": "Trong (thang máy) đông người quá rồi, chúng ta đừng đi nữa.",
                    "ans": "A",
                    "explain": "Chọn <strong>A. 电梯</strong>: '电梯里人太多了' và hành động '别坐了' (đừng đi/ngồi thang máy)."
                },
                {
                    "num": 29,
                    "sentence": "A: 今天晚上你（……）要去听音乐会？\nB: 是啊，我现在对音乐非常感兴趣。",
                    "py": "A: Jīntiān wǎnshang nǐ (……) yào qù tīng yīnyuèhuì?\nB: Shì a, wǒ xiànzài duì yīnyuè fēicháng gǎn xìngqù.",
                    "vi": "A: Tối nay bạn (lại) đi nghe hòa nhạc à?\nB: Đúng thế, bây giờ mình vô cùng hứng thú với âm nhạc.",
                    "ans": "F",
                    "explain": "Chọn <strong>F. 又</strong>: Phó từ '又' đứng trước động từ thể hiện hành động lặp lại thường xuyên."
                },
                {
                    "num": 30,
                    "sentence": "A: 我觉得我越来越胖了，以后我不吃晚饭了。\nB: 其实胖点儿或者瘦点儿都没关系，健康最（……）。",
                    "py": "A: Wǒ juéde wǒ yuè lái yuè pàng le, yǐhòu wǒ bù chī wǎnfàn le.\nB: Qíshí pàng diǎnr huòzhě shòu diǎnr dōu méi guānxi, jiànkāng zuì (……).",
                    "vi": "A: Mình thấy mình ngày càng béo ra rồi, sau này mình không ăn tối nữa.\nB: Thực ra béo hay gầy một chút cũng chẳng sao, sức khỏe là (quan trọng) nhất.",
                    "ans": "D",
                    "explain": "Chọn <strong>D. 重要</strong>: '健康最重要' là cấu trúc thành ngữ/cụm từ chuẩn: sức khỏe là quan trọng nhất."
                }
            ]
        },
        "part3_31_35": [
            {
                "num": 31,
                "passage": {
                    "zh": "“再见”是一个很有意思的词，“再见”的意思是“再一次见面”，所以人们离开时说“再见”，是希望以后再见面。",
                    "py": "“Zàijiàn” shì yí ge hěn yǒu yìsi de cí, “zàijiàn” de yìsi shì “zài yí cì jiànmiàn”, suǒyǐ rénmen líkāi shí shuō “zàijiàn”, shì xīwàng yǐhòu zài jiànmiàn.",
                    "vi": "'Tạm biệt' là một từ rất thú vị, ý nghĩa của 'tạm biệt' (tái kiến) chính là 'gặp mặt thêm một lần nữa', vì vậy mọi người khi rời đi nói 'tạm biệt' là hy vọng sau này sẽ gặp lại nhau."
                },
                "question": {
                    "zh": "什么时候说“再见”？",
                    "py": "Shénme shíhou shuō “zàijiàn”?",
                    "vi": "Khi nào thì nói lời 'tạm biệt'?"
                },
                "options": {
                    "A": {
                        "zh": "离开",
                        "py": "líkāi",
                        "vi": "Khi rời đi"
                    },
                    "B": {
                        "zh": "见面",
                        "py": "jiànmiàn",
                        "vi": "Khi gặp mặt"
                    },
                    "C": {
                        "zh": "上课",
                        "py": "shàngkè",
                        "vi": "Khi vào học"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn viết rõ ràng: '所以人们离开时说“再见”' (vì vậy khi mọi người rời đi sẽ nói tạm biệt)."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "我男朋友的家虽然不大，但是住着很舒服，楼里很安静，还有电梯，他很喜欢他现在的家。",
                    "py": "Wǒ nánpéngyou de jiā suīrán bú dà, dànshì zhùzhe hěn shūfu, lóu lǐ hěn ānjìng, hái yǒu diàntī, tā hěn xǐhuan tā xiànzài de jiā.",
                    "vi": "Nhà bạn trai tôi tuy không lớn nhưng ở rất dễ chịu, trong tòa nhà rất yên tĩnh, lại có thang máy, anh ấy rất thích ngôi nhà hiện tại của mình."
                },
                "question": {
                    "zh": "男朋友觉得他的家怎么样？",
                    "py": "Nánpéngyou juéde tā de jiā zěnmeyàng?",
                    "vi": "Bạn trai cảm thấy nhà của anh ấy thế nào?"
                },
                "options": {
                    "A": {
                        "zh": "不舒服",
                        "py": "bù shūfu",
                        "vi": "Không thoải mái"
                    },
                    "B": {
                        "zh": "太小了",
                        "py": "tài xiǎo le",
                        "vi": "Quá nhỏ"
                    },
                    "C": {
                        "zh": "很满意",
                        "py": "hěn mǎnyì",
                        "vi": "Rất hài lòng"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Dù nhà không to nhưng '住着很舒服', '他很喜欢他现在的家' đồng nghĩa với '很满意' (rất hài lòng)."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "女孩子都喜欢穿裙子，爱唱歌、跳舞，但是我哥的女儿不是这样，她对运动很感兴趣，还喜欢玩儿电脑游戏，我几乎没见她穿过裙子。",
                    "py": "Nǚháizi dōu xǐhuan chuān qúnzi, ài chànggē, tiàowǔ, dànshì wǒ gē de nǚ'ér bú shì zhèyàng, tā duì yùndòng hěn gǎn xìngqù, hái xǐhuan wánr diànnǎo yóuxì, wǒ jīhū méi jiàn tā chuānguo qúnzi.",
                    "vi": "Con gái đều thích mặc váy, thích hát múa, nhưng con gái anh trai tôi lại không như vậy, cháu rất hứng thú với thể thao, còn thích chơi trò chơi máy tính, tôi hầu như chưa từng thấy cháu mặc váy."
                },
                "question": {
                    "zh": "哥哥的女儿：",
                    "py": "Gēge de nǚ'ér:",
                    "vi": "Con gái của người anh trai:"
                },
                "options": {
                    "A": {
                        "zh": "喜欢唱歌",
                        "py": "xǐhuan chànggē",
                        "vi": "Thích ca hát"
                    },
                    "B": {
                        "zh": "很少穿裙子",
                        "py": "hěn shǎo chuān qúnzi",
                        "vi": "Rất ít khi mặc váy"
                    },
                    "C": {
                        "zh": "不爱运动",
                        "py": "bú ài yùndòng",
                        "vi": "Không thích thể thao"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: '我几乎没见她穿过裙子' (tôi hầu như chưa thấy cháu mặc váy bao giờ) tương đương với '很少穿裙子'."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "丈夫最近很忙，没有时间去运动，又胖了几斤。他打算忙完这几天，就去跑步和游泳。",
                    "py": "Zhàngfu zuìjìn hěn máng, méiyǒu shíjiān qù yùndòng, yòu pàng le jǐ jīn. Tā dǎsuan máng wán zhè jǐ tiān, jiù qù pǎobù hé yóuyǒng.",
                    "vi": "Chồng dạo này rất bận, không có thời gian tập thể thao, lại béo thêm mấy cân. Anh ấy dự định sau mấy ngày bận rộn này sẽ đi chạy bộ và bơi lội."
                },
                "question": {
                    "zh": "丈夫最近：",
                    "py": "Zhàngfu zuìjìn:",
                    "vi": "Người chồng gần đây:"
                },
                "options": {
                    "A": {
                        "zh": "变化不大",
                        "py": "biànhuà bú dà",
                        "vi": "Thay đổi không nhiều"
                    },
                    "B": {
                        "zh": "身体不健康",
                        "py": "shēntǐ bù jiànkāng",
                        "vi": "Sức khỏe không tốt"
                    },
                    "C": {
                        "zh": "很少锻炼",
                        "py": "hěn shǎo duànliàn",
                        "vi": "Rất ít tập luyện"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: '没有时间去运动' nghĩa là gần đây rất ít khi rèn luyện thể dục ('很少锻炼')."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "你要明白，想让每个人都喜欢你是几乎不可能的，所以做事情不要害怕别人不满意，最重要的就是你很满意。",
                    "py": "Nǐ yào míngbai, xiǎng ràng měi ge rén dōu xǐhuan nǐ shì jīhū bù kěnéng de, suǒyǐ zuò shìqing bú yào hàipà biérén bù mǎnyì, zuì zhòngyào de jiù shì nǐ hěn mǎnyì.",
                    "vi": "Bạn cần hiểu rằng, muốn làm cho mọi người đều thích mình là điều gần như không thể, vì thế làm việc đừng sợ người khác không hài lòng, điều quan trọng nhất là chính bạn cảm thấy hài lòng."
                },
                "question": {
                    "zh": "做事情，最重要的是：",
                    "py": "Zuò shìqing, zuì zhòngyào de shì:",
                    "vi": "Khi làm việc, điều quan trọng nhất là:"
                },
                "options": {
                    "A": {
                        "zh": "让每个人都喜欢你",
                        "py": "ràng měi ge rén dōu xǐhuan nǐ",
                        "vi": "Làm cho mọi người đều thích bạn"
                    },
                    "B": {
                        "zh": "不害怕别人",
                        "py": "bú hàipà biérén",
                        "vi": "Không sợ người khác"
                    },
                    "C": {
                        "zh": "你觉得做得很好",
                        "py": "nǐ juéde zuò de hěn hǎo",
                        "vi": "Chính bản thân bạn cảm thấy làm tốt/hài lòng"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Trong bài nêu '最重要的就是你很满意' (quan trọng nhất là bạn rất hài lòng với thành quả của mình), tương đương với '你觉得做得很好'."
            }
        ]
    },
    "tab3_writing": {
        "part1_36_40": [
            {
                "num": 36,
                "chunks": [
                    "健康",
                    "就",
                    "吃什么",
                    "我",
                    "什么东西"
                ],
                "ans": "什么东西健康我就吃什么。",
                "py": "Shénme dōngxi jiànkāng wǒ jiù chī shénme.",
                "vi": "Thứ gì tốt cho sức khỏe thì tôi ăn thứ đó.",
                "grammar": "Cấu trúc đại từ nghi vấn quan hệ tương ứng: '什么... 就 + Động từ + 什么'."
            },
            {
                "num": 37,
                "chunks": [
                    "又",
                    "你",
                    "不满意了",
                    "怎么"
                ],
                "ans": "你怎么又不满意了？",
                "py": "Nǐ zěnme yòu bù mǎnyì le?",
                "vi": "Sao bạn lại không hài lòng nữa rồi?",
                "grammar": "Phó từ '又' đứng trước động từ/hình dung từ phủ định '不满意', diễn tả sự việc tiêu cực lặp lại."
            },
            {
                "num": 38,
                "chunks": [
                    "熊猫",
                    "再",
                    "看一次",
                    "我想",
                    "去"
                ],
                "ans": "我想再去看一次熊猫。",
                "py": "Wǒ xiǎng zài qù kàn yí cì xióngmāo.",
                "vi": "Tôi muốn đi xem gấu trúc thêm một lần nữa.",
                "grammar": "Động từ năng nguyện '想' + phó từ '再' biểu thị hành động dự định lặp lại trong tương lai."
            },
            {
                "num": 39,
                "chunks": [
                    "离婚",
                    "很多",
                    "瘦了",
                    "以后",
                    "她"
                ],
                "ans": "离婚以后她瘦了很多。",
                "py": "Líhūn yǐhòu tā shòu le hěn duō.",
                "vi": "Sau khi ly hôn cô ấy đã gầy đi rất nhiều.",
                "grammar": "Mệnh đề thời gian '...以后' đứng đầu câu hoặc sau chủ ngữ; '很多' làm bổ ngữ mức độ sau tính từ."
            },
            {
                "num": 40,
                "chunks": [
                    "坐电梯",
                    "上去",
                    "我们",
                    "吧"
                ],
                "ans": "我们坐电梯上去吧。",
                "py": "Wǒmen zuò diàntī shàngqu ba.",
                "vi": "Chúng ta đi thang máy lên đi.",
                "grammar": "Câu liên động: Phương thức '坐电梯' + hành động bổ ngữ xu hướng '上去'."
            }
        ],
        "part2_41_45": [
            {
                "num": 41,
                "sentence": "房间里很（ 安 ）静，我很满意。",
                "pinyin": "ān",
                "ans": "安",
                "hanviet": "An",
                "compound": "安静 (ānjìng - yên tĩnh)",
                "vi": "Trong phòng rất yên tĩnh, tôi rất hài lòng."
            },
            {
                "num": 42,
                "sentence": "太晚了，我有点儿害（ 怕 ），你送我回家吧。",
                "pinyin": "pà",
                "ans": "怕",
                "hanviet": "Phạ",
                "compound": "害怕 (hàipà - sợ hãi)",
                "vi": "Muộn quá rồi, tôi thấy hơi sợ, bạn đưa tôi về nhà nhé."
            },
            {
                "num": 43,
                "sentence": "你住的楼里有（ 电 ）梯吗？",
                "pinyin": "diàn",
                "ans": "电",
                "hanviet": "Điện",
                "compound": "电梯 (diàntī - thang máy)",
                "vi": "Trong tòa nhà bạn ở có thang máy không?"
            },
            {
                "num": 44,
                "sentence": "下课以后我（ 马 ）上回家吃饭。",
                "pinyin": "mǎ",
                "ans": "马",
                "hanviet": "Mã",
                "compound": "马上 (mǎshàng - ngay lập tức)",
                "vi": "Tan học xong tôi lập tức về nhà ăn cơm."
            },
            {
                "num": 45,
                "sentence": "你觉得工作和健康，哪个更（ 重 ）要？",
                "pinyin": "zhòng",
                "ans": "重",
                "hanviet": "Trọng",
                "compound": "重要 (zhòngyào - quan trọng)",
                "vi": "Bạn thấy công việc và sức khỏe, cái nào quan trọng hơn?"
            }
        ]
    },
    "tab4_textbook": {
        "vocab": [
            {
                "num": 1,
                "zh": "又",
                "py": "yòu",
                "pos": "phó từ",
                "vi": "lại (hành động đã lặp lại)",
                "eg": {
                    "zh": "你怎么又迟到了？",
                    "py": "Nǐ zěnme yòu chídào le?",
                    "vi": "Sao bạn lại đi muộn nữa rồi?"
                },
                "id": 1
            },
            {
                "num": 2,
                "zh": "满意",
                "py": "mǎnyì",
                "pos": "tính từ",
                "vi": "hài lòng, vừa ý",
                "eg": {
                    "zh": "经理对这个工作很满意。",
                    "py": "Jīnglǐ duì zhè ge gōngzuò hěn mǎnyì.",
                    "vi": "Giám đốc rất hài lòng với công việc này."
                },
                "id": 2
            },
            {
                "num": 3,
                "zh": "电梯",
                "py": "diàntī",
                "pos": "danh từ",
                "vi": "thang máy",
                "eg": {
                    "zh": "我们坐电梯上楼吧。",
                    "py": "Wǒmen zuò diàntī shàng lóu ba.",
                    "vi": "Chúng ta đi thang máy lên lầu đi."
                },
                "id": 3
            },
            {
                "num": 4,
                "zh": "层",
                "py": "céng",
                "pos": "lượng từ",
                "vi": "tầng, lớp",
                "eg": {
                    "zh": "我家住在六层。",
                    "py": "Wǒ jiā zhù zài liù céng.",
                    "vi": "Nhà tôi ở tầng 6."
                },
                "id": 4
            },
            {
                "num": 5,
                "zh": "害怕",
                "py": "hàipà",
                "pos": "động từ/tính từ",
                "vi": "sợ hãi",
                "eg": {
                    "zh": "小狗别害怕，有我呢。",
                    "py": "Xiǎogǒu bié hàipà, yǒu wǒ ne.",
                    "vi": "Cún con đừng sợ, có ta đây."
                },
                "id": 5
            },
            {
                "num": 6,
                "zh": "熊猫",
                "py": "xióngmāo",
                "pos": "danh từ",
                "vi": "gấu trúc",
                "eg": {
                    "zh": "中国的大熊猫非常可爱。",
                    "py": "Zhōngguó de dàxióngmāo fēicháng kě'ài.",
                    "vi": "Gấu trúc Trung Quốc vô cùng đáng yêu."
                },
                "id": 6
            },
            {
                "num": 7,
                "zh": "见面",
                "py": "jiànmiàn",
                "pos": "động từ ly hợp",
                "vi": "gặp mặt",
                "eg": {
                    "zh": "明天我们老地方见个面吧。",
                    "py": "Míngtiān wǒmen lǎo dìfang jiàn ge miàn ba.",
                    "vi": "Ngày mai chúng mình gặp mặt ở chỗ cũ nhé."
                },
                "id": 7
            },
            {
                "num": 8,
                "zh": "安静",
                "py": "ānjìng",
                "pos": "tính từ",
                "vi": "yên tĩnh",
                "eg": {
                    "zh": "图书馆里非常安静。",
                    "py": "Túshūguǎn lǐ fēicháng ānjìng.",
                    "vi": "Trong thư viện vô cùng yên tĩnh."
                },
                "id": 8
            },
            {
                "num": 9,
                "zh": "可乐",
                "py": "kělè",
                "pos": "danh từ",
                "vi": "cô-ca",
                "eg": {
                    "zh": "我想喝一杯冰可乐。",
                    "py": "Wǒ xiǎng hē yì bēi bīng kělè.",
                    "vi": "Tôi muốn uống một ly cô-ca đá."
                },
                "id": 9
            },
            {
                "num": 10,
                "zh": "一会儿",
                "py": "yíhuìr",
                "pos": "danh từ/lượng từ",
                "vi": "một lát, chốc lát",
                "eg": {
                    "zh": "请您在这儿等我一会儿。",
                    "py": "Qǐng nín zài zhèr děng wǒ yíhuìr.",
                    "vi": "Xin ngài đợi tôi ở đây một lát."
                },
                "id": 10
            },
            {
                "num": 11,
                "zh": "马上",
                "py": "mǎshàng",
                "pos": "phó từ",
                "vi": "ngay lập tức",
                "eg": {
                    "zh": "你先吃，我马上就来。",
                    "py": "Nǐ xiān chī, wǒ mǎshàng jiù lái.",
                    "vi": "Bạn ăn trước đi, tôi đến ngay đây."
                },
                "id": 11
            },
            {
                "num": 12,
                "zh": "洗手间",
                "py": "xǐshǒujiān",
                "pos": "danh từ",
                "vi": "nhà vệ sinh",
                "eg": {
                    "zh": "请问洗手间在哪里？",
                    "py": "Qǐngwèn xǐshǒujiān zài nǎlǐ?",
                    "vi": "Xin hỏi nhà vệ sinh ở đâu ạ?"
                },
                "id": 12
            },
            {
                "num": 13,
                "zh": "老",
                "py": "lǎo",
                "pos": "tính từ",
                "vi": "cũ, già, lâu năm",
                "eg": {
                    "zh": "他是我的老朋友了。",
                    "py": "Tā shì wǒ de lǎo péngyou le.",
                    "vi": "Anh ấy là bạn cũ của tôi rồi."
                },
                "id": 13
            },
            {
                "num": 14,
                "zh": "几乎",
                "py": "jīhū",
                "pos": "phó từ",
                "vi": "hầu như, gần như",
                "eg": {
                    "zh": "全班同学几乎都及格了。",
                    "py": "Quán bān tóngxué jīhū dōu jígé le.",
                    "vi": "Cả lớp hầu như đều đã qua kỳ thi."
                },
                "id": 14
            },
            {
                "num": 15,
                "zh": "变化",
                "py": "biànhuà",
                "pos": "danh từ/động từ",
                "vi": "thay đổi, biến đổi",
                "eg": {
                    "zh": "这几年北京的变化真大。",
                    "py": "Zhè jǐ nián Běijīng de biànhuà zhēn dà.",
                    "vi": "Mấy năm nay Bắc Kinh thay đổi thật lớn."
                },
                "id": 15
            },
            {
                "num": 16,
                "zh": "健康",
                "py": "jiànkāng",
                "pos": "tính từ/danh từ",
                "vi": "khỏe mạnh, sức khỏe",
                "eg": {
                    "zh": "身体健康比什么都重要。",
                    "py": "Shēntǐ jiànkāng bǐ shénme dōu zhòngyào.",
                    "vi": "Sức khỏe thể chất quan trọng hơn bất cứ thứ gì."
                },
                "id": 16
            },
            {
                "num": 17,
                "zh": "重要",
                "py": "zhòngyào",
                "pos": "tính từ",
                "vi": "quan trọng",
                "eg": {
                    "zh": "今天有一个重要的会议。",
                    "py": "Jīntiān yǒu yí ge zhòngyào de huìyì.",
                    "vi": "Hôm nay có một cuộc họp quan trọng."
                },
                "id": 17
            }
        ],
        "grammar": [
            {
                "title": "So sánh phó từ “又” và “再”",
                "structure": "又 + Động từ (Đã xảy ra) / 再 + Động từ (Tương lai)",
                "explanation": "Cả hai đều biểu thị hành động lặp lại, tuy nhiên: “又” thường dùng cho hành động/trạng thái lặp lại đã xảy ra hoặc quy luật lặp lại tất yếu; “再” dùng cho hành động lặp lại chưa xảy ra (sẽ làm trong tương lai).",
                "examples": [
                    {
                        "zh": "昨天买了一条裤子，今天又买了一条。",
                        "py": "Zuótiān mǎi le yì tiáo kùzi, jīntiān yòu mǎi le yì tiáo.",
                        "vi": "Hôm qua mua một chiếc quần, hôm nay lại mua thêm một chiếc nữa. (Đã xảy ra)"
                    },
                    {
                        "zh": "今天没听懂，明天我再听一遍。",
                        "py": "Jīntiān méi tīngdǒng, míngtiān wǒ zài tīng yí biàn.",
                        "vi": "Hôm nay nghe chưa hiểu, ngày mai tôi sẽ nghe lại một lần nữa. (Tương lai)"
                    },
                    {
                        "zh": "你怎么又迟到了？",
                        "py": "Nǐ zěnme yòu chídào le?",
                        "vi": "Sao bạn lại đi muộn nữa rồi? (Đã xảy ra)"
                    }
                ]
            },
            {
                "title": "Đại từ nghi vấn dùng linh hoạt biểu thị sự tương ứng (疑问代词活用 1)",
                "structure": "Mệnh đề điều kiện (Đại từ nghi vấn) + 就 + Mệnh đề kết quả (Đại từ nghi vấn)",
                "explanation": "Sử dụng cùng một đại từ nghi vấn (哪儿, 什么, 谁, 怎么, 什么时候...) trong hai mệnh đề, mệnh đề trước nêu điều kiện, mệnh đề sau dùng “就” dẫn ra kết quả tương ứng: điều kiện thế nào thì kết quả làm đúng như thế.",
                "examples": [
                    {
                        "zh": "你去哪儿我就去哪儿。",
                        "py": "Nǐ qù nǎr wǒ jiù qù nǎr.",
                        "vi": "Em đi đâu thì anh đi đến đó."
                    },
                    {
                        "zh": "什么东西健康我就吃什么。",
                        "py": "Shénme dōngxi jiànkāng wǒ jiù chī shénme.",
                        "vi": "Thứ gì tốt cho sức khỏe thì tôi ăn thứ đó."
                    },
                    {
                        "zh": "谁想去谁就去吧。",
                        "py": "Shéi xiǎng qù shéi jiù qù ba.",
                        "vi": "Ai muốn đi thì người đó đi nhé."
                    }
                ]
            }
        ],
        "word_expansion": [
            {
                "formula": "见面 + 考试 → 面试",
                "py": "miànshì",
                "vi": "Phỏng vấn (gặp mặt trực tiếp để sát hạch, khảo thí)",
                "eg": "明天上午我要去一家外企面试。(Sáng mai tôi phải đi phỏng vấn tại một doanh nghiệp nước ngoài.)"
            },
            {
                "formula": "自己 + 学习 → 自学",
                "py": "zìxué",
                "vi": "Tự học (bản thân tự giác học tập, nghiên cứu)",
                "eg": "我喜欢自学，在家里自学了三年汉语。(Tôi thích tự học, đã tự học tiếng Trung 3 năm ở nhà.)"
            },
            {
                "formula": "离开 + 结婚 → 离婚",
                "py": "líhūn",
                "vi": "Ly hôn (chấm dứt quan hệ hôn nhân)",
                "eg": "离婚以后，她全身心投入到工作中。(Sau khi ly hôn, cô ấy dốc hết tâm trí vào công việc.)"
            }
        ],
        "idiom": {
            "proverb_zh": "站得高，看得远",
            "proverb_py": "Zhàn de gāo, kàn de yuǎn",
            "proverb_vi": "Đứng càng cao, nhìn càng xa",
            "story_vi": "Câu tục ngữ bắt nguồn từ bài thơ nổi tiếng 'Đăng Quán Tước Lâu' của Vương Chi Hoán: 'Dục cùng thiên lý mục, cánh thượng nhất tầng lâu' (Muốn ngắm trọn ngàn dặm, hãy lên thêm một tầng lầu). Nghĩa bóng khuyên con người trong học tập và cuộc sống muốn có cái nhìn bao quát, sâu sắc và toàn diện thì phải không ngừng nâng cao trình độ, tầm nhìn và vị thế của bản thân."
        },
        "polyphonic": [
            {
                "char": "地",
                "sounds": [
                    {
                        "py": "dì",
                        "meaning": "mặt đất, đất đai, địa phương (danh từ)",
                        "example": "土地 (tǔdì), 地方 (dìfang)"
                    },
                    {
                        "py": "de",
                        "meaning": "trợ từ kết cấu đặt trước động từ chỉ trạng thái",
                        "example": "慢慢地走 (mànmàn de zǒu), 高兴地说 (gāoxìng de shuō)"
                    }
                ]
            },
            {
                "char": "会",
                "sounds": [
                    {
                        "py": "huì",
                        "meaning": "biết qua học hỏi; hội họp, cuộc họp",
                        "example": "学会 (xuéhuì), 开会 (kāihuì)"
                    },
                    {
                        "py": "kuài",
                        "meaning": "kế toán, tính toán sổ sách",
                        "example": "会计 (kuàijì)"
                    }
                ]
            }
        ],
        "expansion_and_idiom": {
            "word_expansion": [
                {
                    "word": "面试",
                    "py": "miànshì",
                    "meaning": "phỏng vấn tuyển dụng (见面: gặp mặt + 考试: khảo thí)"
                },
                {
                    "word": "自学",
                    "py": "zìxué",
                    "meaning": "tự học (自己: bản thân + 学习: học tập)"
                },
                {
                    "word": "离婚",
                    "py": "líhūn",
                    "meaning": "ly hôn (离开: rời bỏ + 结婚: kết hôn)"
                }
            ],
            "proverb": {
                "zh": "站得高，看得远",
                "py": "Zhàn de gāo, kàn de yuǎn",
                "vi": "Đứng càng cao, nhìn càng xa (Muốn có tầm nhìn rộng mở, thấy rõ mọi việc thì phải nâng cao tầm mắt, trình độ và vị thế của bản thân)."
            }
        }
    },
    "quiz_data": {
        "1": {
            "type": "pic_select",
            "ans": "E",
            "explain": "Đáp án <strong>E</strong>: Nhắc tới '十五层太高了' và '看看别的房子', tương ứng hình tòa chung cư 15 tầng."
        },
        "2": {
            "type": "pic_select",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: '大熊猫多可爱啊', tương ứng hình hai chú gấu trúc ăn trúc."
        },
        "3": {
            "type": "pic_select",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: '怎么还不起床', '多睡一会儿', tương ứng hình cô gái ngủ nướng trên giường."
        },
        "4": {
            "type": "pic_select",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '是不是走错了', '就在前面马上就到了', tương ứng hình cặp đôi xem bản đồ tìm đường."
        },
        "5": {
            "type": "pic_select",
            "ans": "F",
            "explain": "Đáp án <strong>F</strong>: '眼镜怎么样', '变化很大', tương ứng hình chàng trai đeo kính mới."
        },
        "6": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: Chuyển văn phòng từ tầng 1 lên tầng 6 nghĩa là đã đổi văn phòng ('换办公室')."
        },
        "7": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: '以后不能总跟你见面了' cho thấy trước đây hai người thường xuyên gặp mặt."
        },
        "8": {
            "type": "true_false",
            "ans": "√",
            "explain": "Đáp án <strong>Đúng (√)</strong>: '找一个安静的地方读一本好书是我最大的快乐' chứng tỏ anh ấy thích nơi yên tĩnh."
        },
        "9": {
            "type": "true_false",
            "ans": "×",
            "explain": "Đáp án <strong>Sai (×)</strong>: Cô gái muốn lên tầng 12 ('您去十二层'), thang máy này chỉ lên tầng 10."
        },
        "10": {
            "type": "true_false",
            "ans": "×",
            "explain": "Đáp án <strong>Sai (×)</strong>: Người nói bảo anh ấy đi kiểm tra phòng 603, anh ấy chưa ở trong nhà vệ sinh."
        },
        "11": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Người nam cảnh báo uống nữa sẽ mất ngủ để không cho người nữ uống thêm cô-ca."
        },
        "12": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Người nam bảo '只是感冒，休息两天就好了', người nữ bị cảm cúm."
        },
        "13": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Bạn của cô ấy đi vệ sinh một lát sẽ quay lại, nghĩa là chỗ này đã có người."
        },
        "14": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Người nữ sốt ruột vì con trai lại thi cử không tốt ('又没考好')."
        },
        "15": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: '明天要去面试' cho biết mục đích chuẩn bị váy áo là để đi phỏng vấn."
        },
        "16": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: '下了电梯有一个咖啡馆，我们去那儿吧', hai người rủ nhau ra quán cà phê."
        },
        "17": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Hai người nói '吃鸡蛋面，马上就好', hôm nay họ ăn mì sợi."
        },
        "18": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Người nam quay lại nhà hàng vì để quên chiếc ô màu đen."
        },
        "19": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Người nữ nhận lời hẹn ăn trưa mai ở chỗ cũ, chứng tỏ trưa mai cô ấy không bận."
        },
        "20": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Người nữ tự nhận '汉字几乎一个都不会写' (hầu như không biết viết chữ Hán)."
        },
        "21": {
            "type": "matching",
            "ans": "D",
            "explain": "Đáp án <strong>D</strong>: Hỏi tại sao lại đi vệ sinh liên tục, trả lời do đồ ăn có vấn đề làm bụng dạ khó chịu."
        },
        "22": {
            "type": "matching",
            "ans": "F",
            "explain": "Đáp án <strong>F</strong>: Bánh ngọt ngon bọn trẻ rất thích, đề nghị mua thêm mấy miếng nữa."
        },
        "23": {
            "type": "matching",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Trả lời cho câu hỏi nghe nói gần đây định mua nhà, xem nhiều nơi nhưng chưa vừa ý."
        },
        "24": {
            "type": "matching",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: Trả lời cho dự định cuối tuần là đi gặp mấy người bạn cũ."
        },
        "25": {
            "type": "matching",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: Trả lời câu hỏi tan học đi đâu học bằng cấu trúc '哪儿安静我就去哪儿'."
        },
        "26": {
            "type": "word_fill",
            "ans": "B",
            "explain": "Đáp án <strong>B. 洗手间</strong>: '去一下洗手间' (đi vệ sinh một chút)."
        },
        "27": {
            "type": "word_fill",
            "ans": "C",
            "explain": "Đáp án <strong>C. 几乎</strong>: '几乎每天' (gần như mỗi ngày đều ra công viên tập thể dục)."
        },
        "28": {
            "type": "word_fill",
            "ans": "A",
            "explain": "Đáp án <strong>A. 电梯</strong>: '电梯里人太多了' (trong thang máy đông người quá)."
        },
        "29": {
            "type": "word_fill",
            "ans": "F",
            "explain": "Đáp án <strong>F. 又</strong>: '你又要去听音乐会' (bạn lại đi nghe hòa nhạc à)."
        },
        "30": {
            "type": "word_fill",
            "ans": "D",
            "explain": "Đáp án <strong>D. 重要</strong>: '健康最重要' (sức khỏe là quan trọng nhất)."
        },
        "31": {
            "type": "single_choice",
            "ans": "A",
            "explain": "Đáp án <strong>A</strong>: '人们离开时说“再见”' (mọi người nói tạm biệt khi rời đi)."
        },
        "32": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: Dù nhà không to nhưng ở rất dễ chịu, anh ấy rất thích ngôi nhà -> '很满意'."
        },
        "33": {
            "type": "single_choice",
            "ans": "B",
            "explain": "Đáp án <strong>B</strong>: '几乎没见她穿过裙子' tương đương với '很少穿裙子' (rất hiếm khi mặc váy)."
        },
        "34": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '没有时间去运动' nghĩa là dạo này rất ít tập luyện ('很少锻炼')."
        },
        "35": {
            "type": "single_choice",
            "ans": "C",
            "explain": "Đáp án <strong>C</strong>: '最重要的就是你很满意' tương đương với '你觉得做得很好' (chính mình thấy hài lòng/làm tốt)."
        }
    }
}
