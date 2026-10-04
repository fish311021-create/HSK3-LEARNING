# -*- coding: utf-8 -*-
LESSON_DATA = {
    "lesson_info": {
        "id": 12,
        "title_zh": "把重要的东西放在我这儿吧。",
        "title_py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr ba.",
        "title_vi": "Hãy để những thứ quan trọng ở chỗ tôi nhé.",
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
            "time": 180,
            "label": "▶ 03:00 Phần 2 (6-10)"
        },
        {
            "time": 430,
            "label": "▶ 07:10 Phần 3 (11-15)"
        },
        {
            "time": 710,
            "label": "▶ 11:50 Phần 4 (16-20)"
        }
    ],
    "tab1_listening": {
        "part1_pictures": [
            {
                "id": "A",
                "file": "pic_A.png",
                "label": "Hình A: Khoang máy bay với tiếp viên và hành khách (飞机马上起飞 / 关上手机)"
            },
            {
                "id": "B",
                "file": "pic_B.png",
                "label": "Hình B: Hàng va li xếp ngay ngắn (行李箱 / 放到上面)"
            },
            {
                "id": "C",
                "file": "pic_C.png",
                "label": "Hình C: Tấm bảng viết chữ Hán '说普通话 写规范字' (黑板上的字 / 查字典)"
            },
            {
                "id": "D",
                "file": "pic_D.png",
                "label": "Hình D (Ví dụ): Nhân viên nữ nghe điện thoại (打电话)"
            },
            {
                "id": "E",
                "file": "pic_E.png",
                "label": "Hình E: Cô gái ngồi xe lăn tắm nắng trong công viên (腿好点儿了吗 / 太阳不错)"
            },
            {
                "id": "F",
                "file": "pic_F.png",
                "label": "Hình F: Chàng trai mặc vest xem đồng hồ khi gọi điện thoại (会议开始了 / 迟到)"
            }
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你的腿好点儿了吗？",
                        "py": "Nǐ de tuǐ hǎodiǎnr le ma?",
                        "vi": "Chân của bạn đã đỡ hơn chút nào chưa?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "还有点儿疼。今天太阳不错，你带我出去吧。",
                        "py": "Hái yǒudiǎnr téng. Jīntiān tàiyáng búcuò, nǐ dài wǒ chūqù ba.",
                        "vi": "Vẫn còn hơi đau. Hôm nay trời nắng đẹp, bạn đưa tôi ra ngoài nhé."
                    }
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Nhắc tới chân đau cần đưa ra ngoài tắm nắng ('你的腿好点儿了吗', '今天太阳不错，你带我出去吧'), tương ứng hình E cô gái ngồi xe lăn."
            },
            {
                "num": 2,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "能帮我把这些行李箱放到上面吗？我搬不动。",
                        "py": "Néng bāng wǒ bǎ zhèxiē xínglixiāng fàngdào shàngmiàn ma? Wǒ bān bu dòng.",
                        "vi": "Có thể giúp tôi chuyển những chiếc vali này lên phía trên không? Tôi nhấc không nổi."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "可以，我来搬吧。",
                        "py": "Kěyǐ, wǒ lái bān ba.",
                        "vi": "Được chứ, để tôi chuyển cho."
                    }
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Nhắc tới '这些行李箱' (những chiếc vali này), tương ứng hình B các chiếc vali hành lý."
            },
            {
                "num": 3,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "对不起先生，飞机马上就要起飞了，请您关上手机。",
                        "py": "Duìbuqǐ xiānsheng, fēijī mǎshàng jiù yào qǐfēi le, qǐng nín guānshang shǒujī.",
                        "vi": "Xin lỗi thưa ông, máy bay sắp cất cánh rồi, xin ông vui lòng tắt điện thoại."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "好的，我知道了。",
                        "py": "Hǎo de, wǒ zhīdào le.",
                        "vi": "Vâng, tôi biết rồi."
                    }
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Tiếp viên nhắc nhở máy bay chuẩn bị cất cánh ('飞机马上就要起飞了'), tương ứng hình A khoang máy bay."
            },
            {
                "num": 4,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "黑板上的那个字怎么读？",
                        "py": "Hēibǎn shang de nà ge zì zěnme dú?",
                        "vi": "Chữ kia trên bảng đen đọc thế nào?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我也不认识，我查一下字典，找到了告诉你。",
                        "py": "Wǒ yě bú rènshi, wǒ chá yíxià zìdiǎn, zhǎodào le gàosù nǐ.",
                        "vi": "Tôi cũng không biết chữ đó, để tôi tra từ điển xem, tìm thấy sẽ bảo bạn."
                    }
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Hỏi cách đọc chữ trên bảng đen ('黑板上的那个字怎么读'), tương ứng hình C tấm bảng viết chữ."
            },
            {
                "num": 5,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "会议早就开始了，你怎么现在还没来？",
                        "py": "Huìyì zǎojiù kāishǐ le, nǐ zěnme xiànzài hái méi lái?",
                        "vi": "Cuộc họp đã bắt đầu từ lâu rồi, sao đến giờ anh vẫn chưa tới?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "别生气，我十分钟就到。",
                        "py": "Bié shēngqì, wǒ shí fēnzhōng jiù dào.",
                        "vi": "Đừng giận nhé, 10 phút nữa tôi đến ngay."
                    }
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Gọi điện giục đi họp muộn ('会议早就开始了', '我十分钟就到'), tương ứng hình F chàng trai xem đồng hồ khi gọi điện."
            }
        ],
        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {
                    "zh": "我的包忘在出租车上了，钱包、手机和护照都在里面。",
                    "py": "Wǒ de bāo wàng zài chūzūchē shang le, qiánbāo, shǒujī hé hùzhào dōu zài lǐmiàn.",
                    "vi": "Túi của tôi bị để quên trên xe taxi rồi, ví tiền, điện thoại và hộ chiếu đều ở bên trong."
                },
                "statement": {
                    "zh": "他是出租车司机。",
                    "py": "Tā shì chūzūchē sījī.",
                    "vi": "Anh ấy là tài xế taxi."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người nói là hành khách để quên đồ trên taxi, không phải tài xế lái xe taxi."
            },
            {
                "num": 7,
                "passage": {
                    "zh": "我很喜欢画画儿，但是没有人教过我，我都是自己学的。你看，这个小狗就是我画的，可爱吗？",
                    "py": "Wǒ hěn xǐhuan huàhuàr, dànshì méiyǒu rén jiāoguo wǒ, wǒ dōu shì zìjǐ xué de. Nǐ kàn, zhè ge xiǎogǒu jiù shì wǒ huà de, kě'ài ma?",
                    "vi": "Tôi rất thích vẽ tranh, nhưng chưa từng có ai dạy tôi cả, tôi đều tự học đấy. Bạn nhìn xem, chú cún con này là do tôi vẽ đấy, đáng yêu không?"
                },
                "statement": {
                    "zh": "他不喜欢跟老师学画画儿。",
                    "py": "Tā bù xǐhuan gēn lǎoshī xué huàhuàr.",
                    "vi": "Anh ấy không thích học vẽ với giáo viên."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Đoạn văn nói vì không có ai dạy nên tự học ('没有人教过我，我都是自己学的'), chứ không phải là không thích học với thầy cô."
            },
            {
                "num": 8,
                "passage": {
                    "zh": "老师，您昨天讲的那几个题，我今天就忘了，您能再教我一次吗？",
                    "py": "Lǎoshī, nín zuótiān jiǎng de nà jǐ ge tí, wǒ jīntiān jiù wàng le, nín néng zài jiāo wǒ yí cì ma?",
                    "vi": "Thưa thầy, mấy bài toán hôm qua thầy giảng hôm nay em đã quên mất rồi, thầy có thể dạy lại cho em một lần nữa không ạ?"
                },
                "statement": {
                    "zh": "老师昨天没讲明白。",
                    "py": "Lǎoshī zuótiān méi jiǎng míngbai.",
                    "vi": "Hôm qua thầy giáo giảng không rõ ràng."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Học sinh hôm nay quên mất ('我今天就忘了') chứ không phải do thầy giảng không rõ."
            },
            {
                "num": 9,
                "passage": {
                    "zh": "爸爸找了很长时间都没找到他的护照，我今天上午帮他洗衣服的时候，在他那条蓝色的裤子里找到了。",
                    "py": "Bàba zhǎo le hěn cháng shíjiān dōu méi zhǎodào tā de hùzhào, wǒ jīntiān shàngwǔ bāng tā xǐ yīfu de shíhou, zài tā nà tiáo lánsè de kùzi lǐ zhǎodào le.",
                    "vi": "Bố tìm rất lâu mà vẫn không thấy hộ chiếu đâu, sáng nay lúc tôi giặt quần áo giúp bố đã tìm thấy trong túi chiếc quần màu xanh lam của ông."
                },
                "statement": {
                    "zh": "爸爸洗衣服的时候发现了护照。",
                    "py": "Bàba xǐ yīfu de shíhou fāxiàn le hùzhào.",
                    "vi": "Bố lúc giặt quần áo đã phát hiện ra hộ chiếu."
                },
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người con giặt đồ giúp bố rồi tìm thấy ('我今天上午帮他洗衣服的时候...找到了'), chứ không phải người bố giặt đồ."
            },
            {
                "num": 10,
                "passage": {
                    "zh": "我们需要换新的桌子和椅子，你什么时候有时间跟我一起去看看？",
                    "py": "Wǒmen xūyào huàn xīn de zhuōzi hé yǐzi, nǐ shénme shíhou yǒu shíjiān gēn wǒ yìqǐ qù kànkan?",
                    "vi": "Chúng ta cần đổi bàn và ghế mới rồi, khi nào bạn có thời gian đi cùng tôi đi xem nhé?"
                },
                "statement": {
                    "zh": "桌子和椅子都旧了。",
                    "py": "Zhuōzi hé yǐzi dōu jiù le.",
                    "vi": "Bàn và ghế đều đã cũ rồi."
                },
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Cần đổi bàn ghế mới ('换新的桌子和椅子') đồng nghĩa bàn ghế hiện tại đã cũ."
            }
        ],
        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "喂，我已经到公园西门了，你是在北门吗？我过去找你吧。",
                        "py": "Wèi, wǒ yǐjīng dào gōngyuán xīmén le, nǐ shì zài běimén ma? Wǒ guòqù zhǎo nǐ ba.",
                        "vi": "A-lô, tôi đã đến cổng tây công viên rồi, bạn đang ở cổng bắc à? Tôi đi qua đó tìm bạn nhé."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你别过来了，我快到西门了。",
                        "py": "Nǐ bié guòlái le, wǒ kuài dào xīmén le.",
                        "vi": "Bạn đừng qua nữa, tôi sắp tới cổng tây rồi."
                    }
                ],
                "question": {
                    "zh": "女的现在在哪儿？",
                    "py": "Nǚ de xiànzài zài nǎr?",
                    "vi": "Người nữ hiện tại đang ở đâu?"
                },
                "options": {
                    "A": {
                        "zh": "公园里边",
                        "py": "Gōngyuán lǐbian",
                        "vi": "Bên trong công viên"
                    },
                    "B": {
                        "zh": "公园西门",
                        "py": "Gōngyuán xīmén",
                        "vi": "Cổng tây công viên"
                    },
                    "C": {
                        "zh": "公园北门",
                        "py": "Gōngyuán běimén",
                        "vi": "Cổng bắc công viên"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ nói '我快到西门了' (tôi sắp tới cổng tây rồi), nghĩa là cô ấy đang đi trong công viên tiến về phía cổng tây."
            },
            {
                "num": 12,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "我决定从明天开始，每天跑一千米。",
                        "py": "Wǒ juédìng cóng míngtiān kāishǐ, měitiān pǎo yìqiān mǐ.",
                        "vi": "Tôi quyết định bắt đầu từ ngày mai, mỗi ngày chạy bộ 1.000 mét."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "真的吗？太阳从西边出来了。",
                        "py": "Zhēn de ma? Tàiyáng cóng xībian chūlái le.",
                        "vi": "Thật thế sao? Mặt trời mọc đằng tây rồi đấy à."
                    }
                ],
                "question": {
                    "zh": "男的是什么意思？",
                    "py": "Nán de shì shénme yìsi?",
                    "vi": "Ý của người nam là gì?"
                },
                "options": {
                    "A": {
                        "zh": "太阳从西边出来",
                        "py": "Tàiyáng cóng xībian chūlái",
                        "vi": "Mặt trời mọc từ phía tây"
                    },
                    "B": {
                        "zh": "女的不可能每天跑步",
                        "py": "Nǚ de bù kěnéng měitiān pǎobù",
                        "vi": "Người nữ không thể nào chạy bộ mỗi ngày"
                    },
                    "C": {
                        "zh": "明天要跑一千米",
                        "py": "Míngtiān yào pǎo yìqiān mǐ",
                        "vi": "Ngày mai phải chạy 1.000 mét"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: '太阳从西边出来了' là cách nói ẩn dụ châm biếm, biểu thị điều đó là khó tin hoặc người nữ không thể kiên trì chạy bộ mỗi ngày."
            },
            {
                "num": 13,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "护照放在行李箱里了吗？",
                        "py": "Hùzhào fàng zài xínglixiāng lǐ le ma?",
                        "vi": "Hộ chiếu đã để trong vali chưa?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "没有，在我包里呢，这样拿着比较方便。",
                        "py": "Méiyǒu, zài wǒ bāo lǐ ne, zhèyàng ná zhe bǐjiào fāngbiàn.",
                        "vi": "Chưa, ở trong túi xách của em này, để thế này cầm cho tiện."
                    }
                ],
                "question": {
                    "zh": "护照在哪儿？",
                    "py": "Hùzhào zài nǎr?",
                    "vi": "Hộ chiếu đang ở đâu?"
                },
                "options": {
                    "A": {
                        "zh": "行李箱里",
                        "py": "Xínglixiāng lǐ",
                        "vi": "Trong vali"
                    },
                    "B": {
                        "zh": "包里",
                        "py": "Bāo lǐ",
                        "vi": "Trong túi xách"
                    },
                    "C": {
                        "zh": "手里",
                        "py": "Shǒu lǐ",
                        "vi": "Trong tay"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ trả lời trực tiếp: '在我包里呢' (ở trong túi xách của em)."
            },
            {
                "num": 14,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "请问，学校附近有中国银行吗？",
                        "py": "Qǐngwèn, xuéxiào fùjìn yǒu Zhōngguó Yínháng ma?",
                        "vi": "Xin hỏi, gần trường học có Ngân hàng Trung Quốc không ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "有，出了西门向左走两百米就能看见。",
                        "py": "Yǒu, chū le xīmén xiàng zuǒ zǒu liǎngbǎi mǐ jiù néng kànjiàn.",
                        "vi": "Có đấy, ra khỏi cổng tây rẽ trái đi 200 mét là thấy ngay."
                    }
                ],
                "question": {
                    "zh": "女的要去哪儿？",
                    "py": "Nǚ de yào qù nǎr?",
                    "vi": "Người nữ muốn đi đâu?"
                },
                "options": {
                    "A": {
                        "zh": "学校",
                        "py": "Xuéxiào",
                        "vi": "Trường học"
                    },
                    "B": {
                        "zh": "银行",
                        "py": "Yínháng",
                        "vi": "Ngân hàng"
                    },
                    "C": {
                        "zh": "西门",
                        "py": "Xīmén",
                        "vi": "Cổng tây"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ hỏi đường đến '中国银行' (Ngân hàng Trung Quốc)."
            },
            {
                "num": 15,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "火车站离这儿很远，坐车不太方便，我开车送你去。",
                        "py": "Huǒchēzhàn lí zhèr hěn yuǎn, zuòchē bú tài fāngbiàn, wǒ kāichē sòng nǐ qù.",
                        "vi": "Ga tàu cách đây khá xa, đi xe không tiện lắm, tôi lái xe đưa bạn đi nhé."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "不用了，谢谢你，我还是自己打出租车去吧。",
                        "py": "Bú yòng le, xièxie nǐ, wǒ háishì zìjǐ dǎ chūzūchē qù ba.",
                        "vi": "Không cần đâu, cảm ơn bạn nhé, tôi tự bắt taxi đi là được rồi."
                    }
                ],
                "question": {
                    "zh": "男的打算怎么去火车站？",
                    "py": "Nán de dǎsuan zěnme qù huǒchēzhàn?",
                    "vi": "Người nam dự định đến ga tàu bằng cách nào?"
                },
                "options": {
                    "A": {
                        "zh": "开车",
                        "py": "Kāichē",
                        "vi": "Lái xe"
                    },
                    "B": {
                        "zh": "打车",
                        "py": "Dǎchē",
                        "vi": "Bắt taxi"
                    },
                    "C": {
                        "zh": "坐公共汽车",
                        "py": "Zuò gōnggòng qìchē",
                        "vi": "Đi xe buýt"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nam từ chối đi nhờ xe và nói '我还是自己打出租车去吧' (tự bắt taxi đi)."
            }
        ],
        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "这是你画的吗？",
                        "py": "Zhè shì nǐ huà de ma?",
                        "vi": "Bức này là do bạn vẽ à?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "太阳是我画的，小猫是妹妹画的。",
                        "py": "Tàiyáng shì wǒ huà de, xiǎomāo shì mèimei huà de.",
                        "vi": "Mặt trời là tôi vẽ, còn chú mèo con là em gái tôi vẽ."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "真好看。画好了吗？",
                        "py": "Zhēn hǎokàn. Huà hǎo le ma?",
                        "vi": "Đẹp thật đấy. Đã vẽ xong chưa?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "还没有，我想在这儿再画点儿花儿。",
                        "py": "Hái méiyǒu, wǒ xiǎng zài zhèr zài huà diǎnr huār.",
                        "vi": "Vẫn chưa xong, tôi muốn vẽ thêm ít hoa vào chỗ này nữa."
                    }
                ],
                "question": {
                    "zh": "女的还准备画什么？",
                    "py": "Nǚ de hái zhǔnbèi huà shénme?",
                    "vi": "Người nữ còn chuẩn bị vẽ thêm cái gì?"
                },
                "options": {
                    "A": {
                        "zh": "太阳",
                        "py": "Tàiyáng",
                        "vi": "Mặt trời"
                    },
                    "B": {
                        "zh": "小猫",
                        "py": "Xiǎomāo",
                        "vi": "Mèo con"
                    },
                    "C": {
                        "zh": "花儿",
                        "py": "Huār",
                        "vi": "Những bông hoa"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nữ nói '我想在这儿再画点儿花儿' (tôi muốn vẽ thêm ít hoa vào đây)."
            },
            {
                "num": 17,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "吃好了吗？要不要再来点儿米饭？",
                        "py": "Chī hǎo le ma? Yào bu yào zài lái diǎnr mǐfàn?",
                        "vi": "Anh ăn no chưa? Có muốn thêm chút cơm nữa không?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "不吃了。家里还有西瓜吗？",
                        "py": "Bù chī le. Jiālǐ hái yǒu xīguā ma?",
                        "vi": "Không ăn nữa. Trong nhà còn dưa hấu không em?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "还有半个，你自己拿吧。",
                        "py": "Hái yǒu bàn ge, nǐ zìjǐ ná ba.",
                        "vi": "Còn nửa quả, anh tự lấy nhé."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "好的。",
                        "py": "Hǎo de.",
                        "vi": "Được rồi."
                    }
                ],
                "question": {
                    "zh": "关于男的，可以知道什么？",
                    "py": "Guānyú nán de, kěyǐ zhīdào shénme?",
                    "vi": "Về người nam, chúng ta biết được điều gì?"
                },
                "options": {
                    "A": {
                        "zh": "帮女的拿西瓜",
                        "py": "Bāng nǚ de ná xīguā",
                        "vi": "Lấy dưa hấu giúp người nữ"
                    },
                    "B": {
                        "zh": "想再吃点儿米饭",
                        "py": "Xiǎng zài chī diǎnr mǐfàn",
                        "vi": "Muốn ăn thêm cơm"
                    },
                    "C": {
                        "zh": "想吃点儿西瓜",
                        "py": "Xiǎng chī diǎnr xīguā",
                        "vi": "Muốn ăn chút dưa hấu"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Người nam hỏi '家里还有西瓜吗' và đi lấy ăn, chứng tỏ muốn ăn dưa hấu."
            },
            {
                "num": 18,
                "dialogue": [
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "喂，是小马吗？",
                        "py": "Wèi, shì Xiǎomǎ ma?",
                        "vi": "A-lô, Tiểu Mã phải không?"
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "是我，周经理，您有什么事？",
                        "py": "Shì wǒ, Zhōu jīnglǐ, nín yǒu shénme shì?",
                        "vi": "Dạ em đây giám đốc Chu, ngài có việc gì dặn dò ạ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "我明天十点要去火车站接个人。",
                        "py": "Wǒ míngtiān shí diǎn yào qù huǒchēzhàn jiē ge rén.",
                        "vi": "Ngày mai 10 giờ tôi cần ra ga tàu đón một người."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "好的，我知道了，我让司机明天九点前到楼下等您。",
                        "py": "Hǎo de, wǒ zhīdào le, wǒ ràng sījī míngtiān jiǔ diǎn qián dào lóuxià děng nín.",
                        "vi": "Vâng em hiểu rồi, em sẽ bảo tài xế trước 9 giờ ngày mai có mặt dưới sảnh đợi ngài."
                    }
                ],
                "question": {
                    "zh": "男的明天要做什么？",
                    "py": "Nán de míngtiān yào zuò shénme?",
                    "vi": "Ngày mai người nam sẽ làm gì?"
                },
                "options": {
                    "A": {
                        "zh": "去接人",
                        "py": "Qù jiē rén",
                        "vi": "Đi đón người"
                    },
                    "B": {
                        "zh": "坐火车",
                        "py": "Zuò huǒchē",
                        "vi": "Đi tàu hỏa"
                    },
                    "C": {
                        "zh": "找司机",
                        "py": "Zhǎo sījī",
                        "vi": "Tìm tài xế"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nam nói rõ: '我明天十点要去火车站接个人' (mai tôi ra ga đón người)."
            },
            {
                "num": 19,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你会骑自行车吗？",
                        "py": "Nǐ huì qí zìxíngchē ma?",
                        "vi": "Anh biết đi xe đạp không?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "当然，我以前经常骑车去上课。",
                        "py": "Dāngrán, wǒ yǐqián jīngcháng qí chē qù shàngkè.",
                        "vi": "Tất nhiên rồi, trước đây tôi thường xuyên đạp xe đi học."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "那你教教我吧，我一直想学。",
                        "py": "Nà nǐ jiāojiao wǒ ba, wǒ yìzhí xiǎng xué.",
                        "vi": "Thế anh dạy em với nhé, em vẫn luôn muốn học."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "可以啊，你什么时候有时间？",
                        "py": "Kěyǐ a, nǐ shénme shíhou yǒu shíjiān?",
                        "vi": "Được chứ, khi nào em có thời gian?"
                    }
                ],
                "question": {
                    "zh": "男的要做什么？",
                    "py": "Nán de yào zuò shénme?",
                    "vi": "Người nam sẽ làm việc gì?"
                },
                "options": {
                    "A": {
                        "zh": "骑车去上课",
                        "py": "Qí chē qù shàngkè",
                        "vi": "Đạp xe đi học"
                    },
                    "B": {
                        "zh": "教女的骑车",
                        "py": "Jiāo nǚ de qí chē",
                        "vi": "Dạy người nữ đi xe đạp"
                    },
                    "C": {
                        "zh": "学骑自行车",
                        "py": "Xué qí zìxíngchē",
                        "vi": "Học đi xe đạp"
                    }
                },
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nhờ '那你教教我吧', người nam đồng ý dạy cô ấy đạp xe."
            },
            {
                "num": 20,
                "dialogue": [
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "你怎么才来？都八点一刻了。",
                        "py": "Nǐ zěnme cái lái? Dōu bā diǎn yí kè le.",
                        "vi": "Sao bây giờ anh mới đến? Đã 8 giờ 15 rồi đấy."
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "对不起，来机场的路上才发现没带护照。",
                        "py": "Duìbuqǐ, lái jīchǎng de lùshang cái fāxiàn méi dài hùzhào.",
                        "vi": "Xin lỗi nhé, trên đường đến sân bay anh mới phát hiện quên mang hộ chiếu."
                    },
                    {
                        "role": "female",
                        "speaker": "女",
                        "zh": "出门的时候你怎么不好好看看呢？",
                        "py": "Chūmén de shíhou nǐ zěnme bù hǎohǎo kànkan ne?",
                        "vi": "Lúc ra khỏi cửa sao anh không kiểm tra cho kỹ chứ?"
                    },
                    {
                        "role": "male",
                        "speaker": "男",
                        "zh": "你一直给我打电话，我很着急就出了问题。",
                        "py": "Nǐ yìzhí gěi wǒ dǎ diànhuà, wǒ hěn zháojí jiù chū le wèntí.",
                        "vi": "Em cứ gọi điện thoại liên tục, anh vội quá nên mới xảy ra sự cố."
                    }
                ],
                "question": {
                    "zh": "男的怎么了？",
                    "py": "Nán de zěnme le?",
                    "vi": "Người nam bị làm sao?"
                },
                "options": {
                    "A": {
                        "zh": "来机场晚了",
                        "py": "Lái jīchǎng wǎn le",
                        "vi": "Đến sân bay bị muộn"
                    },
                    "B": {
                        "zh": "找不到护照了",
                        "py": "Zhǎo bú dào hùzhào le",
                        "vi": "Không tìm thấy hộ chiếu"
                    },
                    "C": {
                        "zh": "忘了给女的打电话",
                        "py": "Wàng le gěi nǚ de dǎ diànhuà",
                        "vi": "Quên gọi điện cho người nữ"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người nữ trách '你怎么才来？都八点一刻了' vì người nam đến sân bay muộn."
            }
        ]
    },
    "tab2_reading": {
        "part1_21_25": {
            "options": {
                "A": {
                    "zh": "你怎么现在才给周经理写信？",
                    "py": "Nǐ zěnme xiànzài cái gěi Zhōu jīnglǐ xiěxìn?",
                    "vi": "Sao bây giờ bạn mới viết thư cho giám đốc Chu?"
                },
                "B": {
                    "zh": "我想学画画儿，你帮我找一个老师教我吧。",
                    "py": "Wǒ xiǎng xué huàhuàr, nǐ bāng wǒ zhǎo yí ge lǎoshī jiāo wǒ ba.",
                    "vi": "Tôi muốn học vẽ, bạn tìm giúp tôi một giáo viên dạy tôi với."
                },
                "C": {
                    "zh": "请问您需要什么帮助吗？",
                    "py": "Qǐngwèn nín xūyào shénme bāngzhù ma?",
                    "vi": "Xin hỏi quý khách có cần trợ giúp gì không ạ?"
                },
                "D": {
                    "zh": "你看桌子下边的那个箱子里有没有？",
                    "py": "Nǐ kàn zhuōzi xiàbian de nà ge xiāngzi lǐ yǒu méiyǒu?",
                    "vi": "Bạn xem trong chiếc hộp ở dưới gầm bàn có không?"
                },
                "E": {
                    "zh": "当然。我们先坐公共汽车，然后换地铁。",
                    "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.",
                    "vi": "Đương nhiên rồi. Chúng mình đi xe buýt trước, sau đó đổi sang tàu điện ngầm. (Ví dụ)"
                },
                "F": {
                    "zh": "我担心路上车太多，不好走。",
                    "py": "Wǒ dānxīn lùshang chē tài duō, bù hǎo zǒu.",
                    "vi": "Tôi lo trên đường xe cộ đông đúc quá, khó đi."
                }
            },
            "questions": [
                {
                    "num": 21,
                    "zh": "我找不到行李箱了，您帮我找找吧。",
                    "py": "Wǒ zhǎo bú dào xínglixiāng le, nín bāng wǒ zhǎozhao ba.",
                    "vi": "Tôi không tìm thấy vali hành lý của mình nữa, ngài giúp tôi tìm với.",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C</strong>: Đáp lại lời hỏi han cần giúp đỡ của nhân viên ('请问您需要什么帮助吗')."
                },
                {
                    "num": 22,
                    "zh": "飞机十点才起飞，你怎么现在就要走？",
                    "py": "Fēijī shí diǎn cái qǐfēi, nǐ zěnme xiànzài jiù yào zǒu?",
                    "vi": "10 giờ máy bay mới cất cánh, sao bây giờ bạn đã muốn đi rồi?",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F</strong>: Giải thích đi sớm vì sợ tắc đường ('我担心路上车太多，不好走')."
                },
                {
                    "num": 23,
                    "zh": "你想学画画儿，真是太阳从西边出来了。",
                    "py": "Nǐ xiǎng xué huàhuàr, zhēn shì tàiyáng cóng xībian chūlái le.",
                    "vi": "Bạn mà lại muốn học vẽ tranh, thật đúng là mặt trời mọc đằng tây rồi.",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B</strong>: Đáp lại nguyện vọng muốn học vẽ ('我想学画画儿，你帮我找一个老师教我吧')."
                },
                {
                    "num": 24,
                    "zh": "你把我的护照放在哪儿了？",
                    "py": "Nǐ bǎ wǒ de hùzhào fàng zài nǎr le?",
                    "vi": "Bạn để hộ chiếu của tôi ở đâu rồi?",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D</strong>: Hướng dẫn tìm trong hộp dưới bàn ('你看桌子下边的那个箱子里有没有')."
                },
                {
                    "num": 25,
                    "zh": "对不起，小丽才把他的电子邮箱告诉我。",
                    "py": "Duìbuqǐ, Xiǎolì cái bǎ tā de diànzǐ yóuxiāng gàosù wǒ.",
                    "vi": "Xin lỗi nhé, Tiểu Lệ vừa mới cho tôi địa chỉ email của ông ấy.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A</strong>: Giải thích lý do bây giờ mới viết thư ('你怎么现在才给周经理写信')."
                }
            ]
        },
        "part2_26_30": {
            "options": {
                "A": {
                    "zh": "司机",
                    "py": "sījī",
                    "vi": "tài xế, lái xe"
                },
                "B": {
                    "zh": "起飞",
                    "py": "qǐfēi",
                    "vi": "cất cánh"
                },
                "C": {
                    "zh": "发现",
                    "py": "fāxiàn",
                    "vi": "phát hiện, nhận ra"
                },
                "D": {
                    "zh": "自己",
                    "py": "zìjǐ",
                    "vi": "tự mình, bản thân"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "tiếng, giọng nói (Ví dụ)"
                },
                "F": {
                    "zh": "包",
                    "py": "bāo",
                    "vi": "túi, bao, bọc"
                }
            },
            "questions": [
                {
                    "num": 26,
                    "zh": "我回来了，真累啊，帮我把（ ）放在桌子上吧。",
                    "py": "Wǒ huílái le, zhēn lèi a, bāng wǒ bǎ ( ) fàng zài zhuōzi shang ba.",
                    "vi": "Tôi về rồi đây, mệt thật đấy, để giúp chiếc (túi xách) lên bàn hộ tôi với.",
                    "ans": "F",
                    "explain": "Đáp án đúng là <strong>F: 包</strong> (túi xách).",
                    "sentence": "我回来了，真累啊，帮我把（ ）放在桌子上吧。"
                },
                {
                    "num": 27,
                    "zh": "你给（ ）打个电话，让他下午三点来接我。",
                    "py": "Nǐ gěi ( ) dǎ ge diànhuà, ràng tā xiàwǔ sān diǎn lái jiē wǒ.",
                    "vi": "Bạn gọi điện thoại cho (tài xế), bảo anh ấy 3 giờ chiều đến đón tôi nhé.",
                    "ans": "A",
                    "explain": "Đáp án đúng là <strong>A: 司机</strong> (bác tài xế).",
                    "sentence": "你给（ ）打个电话，让他下午三点来接我。"
                },
                {
                    "num": 28,
                    "zh": "我（ ）你最近总是上课睡觉，你晚上几点睡啊？",
                    "py": "Wǒ ( ) nǐ zuìjìn zǒngshì shàngkè shuìjiào, nǐ wǎnshang jǐ diǎn shuì a?",
                    "vi": "Tôi (nhận thấy) dạo gần đây bạn toàn ngủ gật trong giờ học, buổi tối mấy giờ bạn mới ngủ thế?",
                    "ans": "C",
                    "explain": "Đáp án đúng là <strong>C: 发现</strong> (nhận thấy, phát hiện ra).",
                    "sentence": "我（ ）你最近总是上课睡觉，你晚上几点睡啊？"
                },
                {
                    "num": 29,
                    "zh": "A：我们的飞机几点（ ）？\nB：下午三点四十分，还有一个小时。",
                    "py": "A: Wǒmen de fēijī jǐ diǎn ( )?\nB: Xiàwǔ sān diǎn sìshí fēn, hái yǒu yí ge xiǎoshí.",
                    "vi": "A: Chuyến bay của chúng ta mấy giờ (cất cánh)?\nB: 3 giờ 40 phút chiều, còn một tiếng nữa.",
                    "ans": "B",
                    "explain": "Đáp án đúng là <strong>B: 起飞</strong> (máy bay cất cánh).",
                    "sentence": "A：我们的飞机几点（ ）？\nB：下午三点四十分，还有一个小时。"
                },
                {
                    "num": 30,
                    "zh": "A：你帮我把衣服洗了吧。\nB：这些都是你的衣服，你（ ）洗吧。",
                    "py": "A: Nǐ bāng wǒ bǎ yīfu xǐ le ba.\nB: Zhèxiē dōu shì nǐ de yīfu, nǐ ( ) xǐ ba.",
                    "vi": "A: Bạn giặt quần áo giúp tôi nhé.\nB: Chỗ này toàn là quần áo của bạn, bạn (tự mình) đi mà giặt.",
                    "ans": "D",
                    "explain": "Đáp án đúng là <strong>D: 自己</strong> (tự mình làm).",
                    "sentence": "A：你帮我把衣服洗了吧。\nB：这些都是你的衣服，你（ ）洗吧。"
                }
            ],
            "words": {
                "A": {
                    "zh": "司机",
                    "py": "sījī",
                    "vi": "tài xế, lái xe"
                },
                "B": {
                    "zh": "起飞",
                    "py": "qǐfēi",
                    "vi": "cất cánh"
                },
                "C": {
                    "zh": "发现",
                    "py": "fāxiàn",
                    "vi": "phát hiện, nhận ra"
                },
                "D": {
                    "zh": "自己",
                    "py": "zìjǐ",
                    "vi": "tự mình, bản thân"
                },
                "E": {
                    "zh": "声音",
                    "py": "shēngyīn",
                    "vi": "tiếng, giọng nói (Ví dụ)"
                },
                "F": {
                    "zh": "包",
                    "py": "bāo",
                    "vi": "túi, bao, bọc"
                }
            }
        },
        "part3_31_35": [
            {
                "num": 31,
                "passage": {
                    "zh": "有个词语叫“老小孩儿”，意思是人老了有时候跟小孩儿一样，容易高兴，也容易生气。",
                    "py": "Yǒu ge cíyǔ jiào \"lǎoxiǎoháir\", yìsi shì rén lǎo le yǒushíhou gēn xiǎoháir yíyàng, róngyì gāoxìng, yě róngyì shēngqì.",
                    "vi": "Có một từ ngữ gọi là \"đứa trẻ già\", ý nói con người khi về già đôi lúc tính nết y hệt trẻ con, dễ vui vẻ mà cũng rất dễ giận dỗi."
                },
                "question": {
                    "zh": "根据这段话，可以知道老人：",
                    "py": "Gēnjù zhè duàn huà, kěyǐ zhīdào lǎorén:",
                    "vi": "Căn cứ vào đoạn văn trên, người già:"
                },
                "options": {
                    "A": {
                        "zh": "总是生气",
                        "py": "Zǒngshì shēngqì",
                        "vi": "Luôn luôn tức giận"
                    },
                    "B": {
                        "zh": "很喜欢小孩儿",
                        "py": "Hěn xǐhuan xiǎoháir",
                        "vi": "Rất thích trẻ con"
                    },
                    "C": {
                        "zh": "有些地方跟小孩儿一样",
                        "py": "Yǒuxiē dìfang gēn xiǎoháir yíyàng",
                        "vi": "Có những điểm giống như trẻ con"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: '有时候跟小孩儿一样' nghĩa là có những điểm tính cách giống trẻ con."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "妻子今天不舒服，我把她送到了医院，医生看了以后说没有大的问题，可能是最近工作太忙、太累了，让 occurrences在家里休息几天。",
                    "py": "Qīzi jīntiān bù shūfu, wǒ bǎ tā sòngdào le yīyuàn, yīshēng kàn le yǐhòu shuō méiyǒu dà de wèntí, kěnéng shì zuìjìn gōngzuò tài máng, tài lèi le, ràng zài jiālǐ xiūxi jǐ tiān.",
                    "vi": "Vợ tôi hôm nay thấy người không khỏe, tôi đã đưa cô ấy đến bệnh viện, bác sĩ khám xong bảo không có vấn đề gì lớn, có thể do dạo này công việc bận rộn, mệt mỏi quá, dặn cô ấy nên ở nhà nghỉ ngơi vài hôm."
                },
                "question": {
                    "zh": "妻子：",
                    "py": "Qīzi:",
                    "vi": "Người vợ:"
                },
                "options": {
                    "A": {
                        "zh": "需要休息",
                        "py": "Xūyào xiūxi",
                        "vi": "Cần phải nghỉ ngơi"
                    },
                    "B": {
                        "zh": "自己去医院了",
                        "py": "Zìjǐ qù yīyuàn le",
                        "vi": "Tự đi bệnh viện một mình"
                    },
                    "C": {
                        "zh": "已经休息几天了",
                        "py": "Yǐjīng xiūxi jǐ tiān le",
                        "vi": "Đã nghỉ ngơi vài ngày rồi"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Bác sĩ khuyên '在家里休息几天' (nghỉ ngơi vài hôm ở nhà) vì làm việc quá sức."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "我是新来的司机，姓高，您叫我小高就可以了。来，把您的行李箱给我，我放在车的后边。您带好护照和机票了吗？我们现在就去机场。",
                    "py": "Wǒ shì xīn lái de sījī, xìng Gāo, nín jiào wǒ Xiǎogāo jiù kěyǐ le. Lái, bǎ nín de xínglixiāng gěi wǒ, wǒ fàng zài chē de hòubian. Nín dàihǎo hùzhào hé jīpiào le ma? Wǒmen xiànzài jiù qù jīchǎng.",
                    "vi": "Tôi là tài xế mới đến, họ Cao, ngài cứ gọi tôi là Tiểu Cao là được rồi. Nào, đưa vali hành lý của ngài cho tôi, tôi cất vào cốp sau xe. Ngài đã mang theo đầy đủ hộ chiếu và vé máy bay chưa ạ? Bây giờ chúng ta đi sân bay luôn nhé."
                },
                "question": {
                    "zh": "小高：",
                    "py": "Xiǎogāo:",
                    "vi": "Tiểu Cao:"
                },
                "options": {
                    "A": {
                        "zh": "要去坐飞机",
                        "py": "Yào qù zuò fēijī",
                        "vi": "Sắp đi máy bay"
                    },
                    "B": {
                        "zh": "在机场工作",
                        "py": "Zài jīchǎng gōngzuò",
                        "vi": "Làm việc tại sân bay"
                    },
                    "C": {
                        "zh": "是一个司机",
                        "py": "Shì yí ge sījī",
                        "vi": "Là một tài xế lái xe"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Tiểu Cao tự giới thiệu: '我是新来的司机' (tôi là tài xế mới đến)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "周明是我爸爸的同学，也是他现在的同事。我小的时候，他有时候带我出去玩儿，还教会了我游泳。明天是他的生日，我要去给他买一个大的蛋糕。",
                    "py": "Zhōu Míng shì wǒ bàba de tóngxué, yě shì tā xiànzài de tóngshì. Wǒ xiǎo de shíhou, tā yǒushíhou dài wǒ chūqù wánr, hái jiāohuì le wǒ yóuyǒng. Míngtiān shì tā de shēngrì, wǒ yào qù gěi tā mǎi yí ge dà de dàngāo.",
                    "vi": "Chu Minh là bạn học của bố tôi, cũng là đồng nghiệp hiện tại của bố. Hồi tôi còn bé, chú ấy thỉnh thoảng dẫn tôi ra ngoài chơi, lại còn dạy tôi biết bơi nữa. Ngày mai là sinh nhật của chú ấy, tôi sẽ đi mua tặng chú một chiếc bánh kem thật to."
                },
                "question": {
                    "zh": "周明：",
                    "py": "Zhōu Míng:",
                    "vi": "Chu Minh:"
                },
                "options": {
                    "A": {
                        "zh": "是我的同学",
                        "py": "Shì wǒ de tóngxué",
                        "vi": "Là bạn học của tôi"
                    },
                    "B": {
                        "zh": "喜欢游泳",
                        "py": "Xǐhuan yóuyǒng",
                        "vi": "Thích bơi lội"
                    },
                    "C": {
                        "zh": "明天过生日",
                        "py": "Míngtiān guò shēngrì",
                        "vi": "Ngày mai đón sinh nhật"
                    }
                },
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Đoạn văn nêu: '明天是他的生日' (ngày mai là sinh nhật của ông ấy)."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "有的事儿就是很有意思，我昨天才发现，你给小张介绍的男朋友是我妻子以前的同事。我们以前见过面，还一起吃过饭，那个时候我就想把他介绍给小张。",
                    "py": "Yǒude shìr jiù shì hěn yǒu yìsi, wǒ zuótiān cái fāxiàn, nǐ gěi Xiǎozhāng jièshào de nánpéngyou shì wǒ qīzi yǐqián de tóngshì. Wǒmen yǐqián jiànguo miàn, hái yìqǐ chīguo fàn, nà ge shíhou wǒ jiù xiǎng bǎ tā jièshào gěi Xiǎozhāng.",
                    "vi": "Có những việc thật là thú vị, hôm qua tôi mới phát hiện ra, chàng trai bạn giới thiệu cho Tiểu Trương chính là đồng nghiệp cũ của vợ tôi. Trước đây chúng tôi từng gặp mặt, còn từng ăn cơm cùng nhau nữa, hồi đó tôi đã muốn giới thiệu anh ấy cho Tiểu Trương rồi."
                },
                "question": {
                    "zh": "小张的男朋友是我妻子：",
                    "py": "Xiǎozhāng de nánpéngyou shì wǒ qīzi:",
                    "vi": "Bạn trai của Tiểu Trương là người thế nào đối với vợ tôi?"
                },
                "options": {
                    "A": {
                        "zh": "以前的同事",
                        "py": "Yǐqián de tóngshì",
                        "vi": "Đồng nghiệp trước đây"
                    },
                    "B": {
                        "zh": "以前的丈夫",
                        "py": "Yǐqián de zhàngfu",
                        "vi": "Chồng trước đây"
                    },
                    "C": {
                        "zh": "以前的男朋友",
                        "py": "Yǐqián de nánpéngyou",
                        "vi": "Bạn trai trước đây"
                    }
                },
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn viết: '是我妻子以前的同事' (là đồng nghiệp cũ của vợ tôi)."
            }
        ]
    },
    "tab3_writing": {
        "part1_36_40": [
            {
                "num": 36,
                "chunks": [
                    "护照",
                    "桌子上",
                    "放到",
                    "请把"
                ],
                "ans": "请把护照放到桌子上。",
                "py": "Qǐng bǎ hùzhào fàngdào zhuōzi shang.",
                "vi": "Xin hãy đặt hộ chiếu lên trên bàn.",
                "grammar": "Cấu trúc câu chữ 把 biểu thị sự dịch chuyển vị trí: Chủ ngữ (ngầm hiểu) + 请把 + Tân ngữ (护照) + Động từ (放) + Bổ ngữ kết quả/vị trí (到桌子上)."
            },
            {
                "num": 37,
                "chunks": [
                    "需要",
                    "笔记本",
                    "买个",
                    "电脑",
                    "我"
                ],
                "ans": "我需要买个笔记本电脑。",
                "py": "Wǒ xūyào mǎi ge bǐjìběndiànnǎo.",
                "vi": "Tôi cần mua một chiếc máy tính xách tay.",
                "grammar": "Cấu trúc: Chủ ngữ (我) + Động từ năng nguyện (需要) + Động từ (买) + Lượng từ (个) + Tân ngữ (笔记本电脑)."
            },
            {
                "num": 38,
                "chunks": [
                    "写字",
                    "黑板上",
                    "在",
                    "你习惯",
                    "吗"
                ],
                "ans": "你习惯在黑板上写字吗？",
                "py": "Nǐ xíguàn zài hēibǎn shang xiězì ma?",
                "vi": "Bạn có quen viết chữ trên bảng đen không?",
                "grammar": "Cấu trúc câu hỏi: Chủ ngữ (你) + Động từ (习惯) + Giới từ chỉ nơi chốn (在黑板上) + Hành động (写字) + 吗?"
            },
            {
                "num": 39,
                "chunks": [
                    "超市",
                    "自己",
                    "吧",
                    "你",
                    "去"
                ],
                "ans": "你自己去超市吧。",
                "py": "Nǐ zìjǐ qù chāoshì ba.",
                "vi": "Bạn tự mình đi siêu thị đi nhé.",
                "grammar": "Cấu trúc câu cầu khiến: Chủ ngữ (你) + Đại từ tự thân (自己) + Động từ (去) + Tân ngữ (超市) + Ngữ khí từ (吧)."
            },
            {
                "num": 40,
                "chunks": [
                    "起飞",
                    "半个小时",
                    "还有",
                    "就",
                    "了",
                    "飞机"
                ],
                "ans": "飞机还有半个小时就起飞了。",
                "py": "Fēijī hái yǒu bàn ge xiǎoshí jiù qǐfēi le.",
                "vi": "Máy bay còn nửa tiếng nữa là cất cánh rồi.",
                "grammar": "Cấu trúc biểu thị sự việc sắp xảy ra: Chủ ngữ (飞机) + 还有 + Thời gian (半个小时) + 就 + Động từ (起飞) + 了."
            }
        ],
        "part2_41_45": [
            {
                "num": 41,
                "sentence": "今天没有（ 太 ）阳，天气很冷。",
                "pinyin": "tài",
                "ans": "太",
                "hanviet": "Thái",
                "compound": "太阳 (tàiyáng: mặt trời)",
                "vi": "Hôm nay không có mặt trời, thời tiết rất lạnh."
            },
            {
                "num": 42,
                "sentence": "地铁站（ 西 ）边有一个咖啡店。",
                "pinyin": "xī",
                "ans": "西",
                "hanviet": "Tây",
                "compound": "西边 (xībian: phía tây)",
                "vi": "Phía tây của ga tàu điện ngầm có một quán cà phê."
            },
            {
                "num": 43,
                "sentence": "请你把（ 包 ）给我。",
                "pinyin": "bāo",
                "ans": "包",
                "hanviet": "Bao",
                "compound": "包 (bāo: chiếc túi, bao bọc)",
                "vi": "Xin bạn đưa chiếc túi cho tôi."
            },
            {
                "num": 44,
                "sentence": "老师今天教我们（ 画 ）小猫。",
                "pinyin": "huà",
                "ans": "画",
                "hanviet": "Họa",
                "compound": "画 (huà: vẽ tranh)",
                "vi": "Thầy giáo hôm nay dạy chúng tôi vẽ chú mèo con."
            },
            {
                "num": 45,
                "sentence": "这个（ 行 ）李箱是谁的？",
                "pinyin": "xíng",
                "ans": "行",
                "hanviet": "Hành",
                "compound": "行李箱 (xínglixiāng: vali hành lý)",
                "vi": "Chiếc vali hành lý này là của ai thế?"
            }
        ]
    },
    "tab4_textbook": {
        "vocab": [
            {
                "id": 1,
                "num": 1,
                "zh": "放",
                "py": "fàng",
                "pos": "động từ",
                "vi": "đặt, để, thả",
                "eg": "把书放在桌子上。"
            },
            {
                "id": 2,
                "num": 2,
                "zh": "半",
                "py": "bàn",
                "pos": "số từ",
                "vi": "nửa, rưỡi",
                "eg": "我等了半个小时。"
            },
            {
                "id": 3,
                "num": 3,
                "zh": "关",
                "py": "guān",
                "pos": "động từ",
                "vi": "đóng, tắt",
                "eg": "请把手机关上。"
            },
            {
                "id": 4,
                "num": 4,
                "zh": "拿",
                "py": "ná",
                "pos": "động từ",
                "vi": "cầm, lấy",
                "eg": "你拿好护照。"
            },
            {
                "id": 5,
                "num": 5,
                "zh": "包",
                "py": "bāo",
                "pos": "danh từ",
                "vi": "túi, giỏ, bọc",
                "eg": "我的包在车上。"
            },
            {
                "id": 6,
                "num": 6,
                "zh": "发现",
                "py": "fāxiàn",
                "pos": "động từ",
                "vi": "phát hiện, nhận ra",
                "eg": "我发现他生病了。"
            },
            {
                "id": 7,
                "num": 7,
                "zh": "护照",
                "py": "hùzhào",
                "pos": "danh từ",
                "vi": "hộ chiếu",
                "eg": "出国要带护照。"
            },
            {
                "id": 8,
                "num": 8,
                "zh": "起飞",
                "py": "qǐfēi",
                "pos": "động từ",
                "vi": "cất cánh",
                "eg": "飞机马上就要起飞了。"
            },
            {
                "id": 9,
                "num": 9,
                "zh": "司机",
                "py": "sījī",
                "pos": "danh từ",
                "vi": "tài xế, lái xe",
                "eg": "出租车司机很热情。"
            },
            {
                "id": 10,
                "num": 10,
                "zh": "教",
                "py": "jiāo",
                "pos": "động từ",
                "vi": "dạy dỗ, giảng dạy",
                "eg": "他教我们汉语。"
            },
            {
                "id": 11,
                "num": 11,
                "zh": "画",
                "py": "huà",
                "pos": "động từ/danh từ",
                "vi": "vẽ / bức tranh",
                "eg": "我想学画中国画。"
            },
            {
                "id": 12,
                "num": 12,
                "zh": "需要",
                "py": "xūyào",
                "pos": "động từ/danh từ",
                "vi": "cần, nhu cầu",
                "eg": "你需要什么帮助吗？"
            },
            {
                "id": 13,
                "num": 13,
                "zh": "黑板",
                "py": "hēibǎn",
                "pos": "danh từ",
                "vi": "bảng đen",
                "eg": "老师在黑板上写字。"
            },
            {
                "id": 14,
                "num": 14,
                "zh": "行李箱",
                "py": "xínglixiāng",
                "pos": "danh từ",
                "vi": "vali hành lý",
                "eg": "把行李箱拿到楼上去。"
            }
        ],
        "grammar": [
            {
                "title": "Câu chữ “把” (2) - Bổ ngữ kết quả chỉ nơi chốn / vị trí (在 / 到 / 给)",
                "structure": "Chủ ngữ + 把 + Tân ngữ + Động từ + 在 / 到 / 给 + Nơi chốn / Người nhận",
                "explanation": "Khi hành động tác động làm đối tượng thay đổi vị trí đến một nơi cụ thể hoặc chuyển giao cho một người nào đó, ta dùng cấu trúc câu chữ “把” kết hợp với các giới từ kết quả như: '在' (ở tại đâu), '到' (đến đâu), '给' (cho ai).",
                "examples": [
                    {
                        "zh": "把重要的东西放在我这儿吧。",
                        "py": "Bǎ zhòngyào de dōngxi fàng zài wǒ zhèr ba.",
                        "vi": "Hãy để những thứ quan trọng ở chỗ tôi nhé."
                    },
                    {
                        "zh": "我把护照放到包里了。",
                        "py": "Wǒ bǎ hùzhào fàngdào bāo lǐ le.",
                        "vi": "Tôi đã cất hộ chiếu vào trong túi rồi."
                    },
                    {
                        "zh": "请把那本书递给我。",
                        "py": "Qǐng bǎ nà běn shū dì gěi wǒ.",
                        "vi": "Làm ơn chuyền cuốn sách kia cho tôi."
                    }
                ]
            },
            {
                "title": "Phó từ “才” biểu thị sự việc diễn ra muộn hoặc khó khăn",
                "structure": "Thời gian / Điều kiện + 才 + Động từ",
                "explanation": "Phó từ “才” đặt trước động từ nhằm nhấn mạnh hành động hoặc trạng thái xảy ra muộn màng, tốn nhiều thời gian hoặc không hề dễ dàng theo nhận định chủ quan của người nói.",
                "examples": [
                    {
                        "zh": "飞机十点才起飞，你怎么现在就走？",
                        "py": "Fēijī shí diǎn cái qǐfēi, nǐ zěnme xiànzài jiù zǒu?",
                        "vi": "10 giờ máy bay mới cất cánh, sao bây giờ bạn đã đi?"
                    },
                    {
                        "zh": "他昨天晚上十二点才睡觉。",
                        "py": "Tā zuótiān wǎnshang shí'èr diǎn cái shuìjiào.",
                        "vi": "Tối qua 12 giờ anh ấy mới đi ngủ."
                    },
                    {
                        "zh": "我找了半天，才找到我的护照。",
                        "py": "Wǒ zhǎo le bàntiān, cái zhǎodào wǒ de hùzhào.",
                        "vi": "Tôi tìm nửa ngày trời mới thấy được hộ chiếu của mình."
                    }
                ]
            }
        ],
        "expansion_and_idiom": {
            "word_expansion": [
                {
                    "word": "画册",
                    "py": "huàcè",
                    "meaning": "tập tranh ảnh, sách tranh minh họa"
                },
                {
                    "word": "黑板报",
                    "py": "hēibǎnbào",
                    "meaning": "báo tường viết phấn trên bảng"
                },
                {
                    "word": "司机师傅",
                    "py": "sījī shīfu",
                    "meaning": "bác tài xế (cách gọi kính trọng trong xã hội)"
                }
            ],
            "proverb": {
                "zh": "太阳从西边出来了",
                "py": "Tàiyáng cóng xībian chūlái le",
                "vi": "Mặt trời mọc đằng tây rồi (Dùng để châm biếm hoặc bày tỏ ngạc nhiên trước một sự việc hy hữu, gần như không thể tin là đối phương lại làm)."
            }
        },
        "polyphonic": [
            {
                "char": "行",
                "sounds": [
                    {
                        "py": "xíng",
                        "meaning": "đi lại, được, hành động",
                        "example": "行李 (xíngli), 行人 (xíngrén), 不行 (bùxíng)"
                    },
                    {
                        "py": "háng",
                        "meaning": "hàng lối, ngành nghề kinh doanh, ngân hàng",
                        "example": "银行 (yínháng), 行业 (hángyè)"
                    }
                ]
            },
            {
                "char": "教",
                "sounds": [
                    {
                        "py": "jiāo",
                        "meaning": "dạy dỗ, truyền thụ kiến thức (động từ)",
                        "example": "教书 (jiāoshū), 教汉语 (jiāo Hànyǔ)"
                    },
                    {
                        "py": "jiào",
                        "meaning": "giáo dục, tôn giáo, phòng học (danh từ)",
                        "example": "教室 (jiàoshì), 教育 (jiàoyù)"
                    }
                ]
            }
        ]
    },
    "quiz_data": {
        "1": {
            "ans": "E",
            "explain": "Đáp án đúng là <strong>E</strong>: Nhắc tới '腿好点儿了吗', '今天太阳不错带我出去' tương ứng hình E cô gái ngồi xe lăn ngoài trời."
        },
        "2": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Nhờ '把这些行李箱放到上面' (chuyển vali lên trên) tương ứng hình B những chiếc vali hành lý."
        },
        "3": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: '飞机马上就要起飞了，请关上手机' tương ứng hình A khoang máy bay hành khách."
        },
        "4": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Hỏi '黑板上的那个字怎么读' tương ứng hình C tấm bảng viết chữ Hán."
        },
        "5": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: '会议早就开始了，你怎么还没来' tương ứng hình F người xem đồng hồ khi gọi điện thoại."
        },
        "6": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Để quên đồ trên taxi là hành khách đi xe, không phải tài xế ('他是出租车司机')."
        },
        "7": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Tự học vì không có ai dạy ('没有人教过我'), không phải không thích học với thầy giáo."
        },
        "8": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Do học sinh hôm nay quên bài ('我今天就忘了'), không phải do thầy giảng không rõ."
        },
        "9": {
            "ans": "×",
            "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Người con giặt đồ giúp bố rồi tìm thấy hộ chiếu ('我今天上午帮他洗衣服的时候...找到了')."
        },
        "10": {
            "ans": "√",
            "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Cần đổi bàn ghế mới ('我们需要换新的桌子和椅子') đồng nghĩa bàn ghế hiện tại đã cũ."
        },
        "11": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Nói '我快到西门了' (sắp tới cổng tây) nghĩa là đang đi bên trong công viên tiến ra."
        },
        "12": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: '太阳从西边出来了' là câu nói bóng gió châm biếm người nữ không thể kiên trì chạy bộ mỗi ngày."
        },
        "13": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nói rõ: '没有，在我包里呢' (hộ chiếu ở trong túi xách)."
        },
        "14": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ hỏi đường đi '中国银行' (Ngân hàng Trung Quốc)."
        },
        "15": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nam từ chối đi nhờ và bảo '我还是自己打出租车去吧' (tự bắt taxi)."
        },
        "16": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nữ nói '我想在这儿再画点儿花儿' (muốn vẽ thêm hoa)."
        },
        "17": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Người nam hỏi dưa hấu và đi lấy ăn, biểu thị muốn ăn dưa hấu ('想吃点儿西瓜')."
        },
        "18": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nam nói rõ: '我明天十点要去火车站接个人' (mai đi đón người ở ga)."
        },
        "19": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nhờ dạy đi xe đạp và người nam đồng ý dạy cô ấy ('教女的骑车')."
        },
        "20": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Người nữ quở trách '你怎么才来？都八点一刻了' vì người nam đến sân bay muộn."
        },
        "21": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Nhờ tìm hành lý đáp lại lời hỏi han '请问您需要什么帮助吗'."
        },
        "22": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F</strong>: Đi sớm vì lo sợ tắc đường '我担心路上车太多，不好走'."
        },
        "23": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B</strong>: Mặt trời mọc đằng tây đáp lại nguyện vọng học vẽ '我想学画画儿，你帮我找一个老师教我吧'."
        },
        "24": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D</strong>: Chỉ vị trí hộ chiếu '你看桌子下边的那个箱子里有没有'."
        },
        "25": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Giải thích lý do viết thư muộn '你怎么现在才给周经理写信'."
        },
        "26": {
            "ans": "F",
            "explain": "Đáp án đúng là <strong>F: 包</strong> (túi xách)."
        },
        "27": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A: 司机</strong> (bác tài xế đón)."
        },
        "28": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C: 发现</strong> (nhận thấy, phát hiện ra)."
        },
        "29": {
            "ans": "B",
            "explain": "Đáp án đúng là <strong>B: 起飞</strong> (máy bay cất cánh)."
        },
        "30": {
            "ans": "D",
            "explain": "Đáp án đúng là <strong>D: 自己</strong> (tự mình giặt)."
        },
        "31": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: '老小孩儿' có nghĩa người già tính nết đôi lúc giống hệt trẻ con ('有些地方跟小孩儿一样')."
        },
        "32": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Bác sĩ khuyên vợ cần nghỉ ngơi ở nhà vài ngày ('在家里休息几天')."
        },
        "33": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Tiểu Cao tự giới thiệu '我是新来的司机' (là tài xế mới)."
        },
        "34": {
            "ans": "C",
            "explain": "Đáp án đúng là <strong>C</strong>: Đoạn văn nêu '明天是他的生日' (ngày mai là sinh nhật của Chu Minh)."
        },
        "35": {
            "ans": "A",
            "explain": "Đáp án đúng là <strong>A</strong>: Đoạn văn viết bạn trai Tiểu Trương '是我妻子以前的同事' (đồng nghiệp cũ của vợ tôi)."
        }
    }
}
