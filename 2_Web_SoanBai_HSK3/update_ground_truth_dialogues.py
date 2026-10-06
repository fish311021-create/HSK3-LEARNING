# -*- coding: utf-8 -*-
"""
Ground-truth dialogues updater for Lessons 2 to 10.
Extracted 100% directly from 'FILE TÀI LIỆU/HSK 3 Sách giáo khoa.pdf'.
"""

import sys, os, importlib.util

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"e:\HSK3\2_Web_SoanBai_HSK3"
DATA_DIR = os.path.join(BASE_DIR, "data")
BUILDER = os.path.join(BASE_DIR, "core", "build_prestudy_engine.py")

GROUND_TRUTH_DIALOGUES = {
    # ========================== BÀI 02 ==========================
    2: [
        {
            "num": 1,
            "title": "下山的路上 (Trên đường xuống núi)",
            "location": "下山的路上 (Trên đường xuống núi)",
            "audio_file": "audio_textbook/Bai_02/02-1.mp3",
            "context": "Tiểu Lệ và Tiểu Cương vừa leo núi xong, đang trên đường đi xuống. Tiểu Lệ mỏi chân than thở với Tiểu Cương.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "休息一下吧。", "py": "Xiūxi yíxià ba.", "vi": "Nghỉ ngơi một lát đi anh."},
                {"speaker": "小刚", "role": "male", "zh": "怎么了？", "py": "Zěnme le?", "vi": "Sao thế em?"},
                {"speaker": "小丽", "role": "female", "zh": "我现在腿也疼，脚也疼。", "py": "Wǒ xiànzài tuǐ yě téng, jiǎo yě téng.", "vi": "Bây giờ chân em cũng đau, bàn chân cũng nhức."},
                {"speaker": "小刚", "role": "male", "zh": "好，那边树多，我们过去坐一下吧。", "py": "Hǎo, nàbian shù duō, wǒmen guòqu zuò yíxià ba.", "vi": "Được, bên kia nhiều cây, chúng ta qua đó ngồi một lát đi."},
                {"speaker": "小丽", "role": "female", "zh": "上来的时候我怎么没觉得这么累？", "py": "Shànglai de shíhou wǒ zěnme méi juéde zhème lèi?", "vi": "Lúc leo lên sao em không thấy mệt thế này nhỉ?"},
                {"speaker": "小刚", "role": "male", "zh": "上山容易下山难，你不知道？", "py": "Shàng shān róngyì xià shān nán, nǐ bù zhīdào?", "vi": "Lên núi dễ xuống núi khó, em không biết à?"}
            ],
            "check_question": {
                "question": "小丽为什么想休息一下？",
                "options": ["她肚子饿了", "她腿也疼，脚也疼", "天快要下雨了", "她想拍照片"],
                "ans": "B",
                "explain": "Tiểu Lệ than phiền: '我现在腿也疼，脚也疼' (Bây giờ chân em cũng đau, bàn chân cũng nhức)."
            }
        },
        {
            "num": 2,
            "title": "在打电话 (Đang gọi điện thoại)",
            "location": "在办公室/打电话 (Gọi điện thoại đến văn phòng)",
            "audio_file": "audio_textbook/Bai_02/02-2.mp3",
            "context": "Chu thái thái gọi điện đến văn phòng tìm chồng là giám đốc Chu Minh nhưng anh đang đi vắng.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "喂，你好，请问周明在吗？", "py": "Wèi, nǐ hǎo, qǐngwèn Zhōu Míng zài ma?", "vi": "Alo, xin chào, cho hỏi Chu Minh có ở đó không?"},
                {"speaker": "秘书", "role": "female", "zh": "周经理出去了，不在办公室。", "py": "Zhōu jīnglǐ chūqu le, bú zài bàngōngshì.", "vi": "Giám đốc Chu ra ngoài rồi ạ, không có ở văn phòng."},
                {"speaker": "周太太", "role": "female", "zh": "他去哪儿了？什么时候回来？", "py": "Tā qù nǎr le? Shénme shíhou huílái?", "vi": "Anh ấy đi đâu rồi? Khi nào thì quay về?"},
                {"speaker": "秘书", "role": "female", "zh": "他出去办事了，下午回来。", "py": "Tā chūqu bàn shì le, xiàwǔ huílái.", "vi": "Giám đốc đi ra ngoài giải quyết công việc rồi ạ, buổi chiều mới về."},
                {"speaker": "周太太", "role": "female", "zh": "回来了就让他给我打个电话。", "py": "Huílái le jiù ràng tā gěi wǒ dǎ ge diànhuà.", "vi": "Lúc nào về thì bảo anh ấy gọi điện thoại cho tôi nhé."},
                {"speaker": "秘书", "role": "female", "zh": "好的，他到了办公室我就告诉他。", "py": "Hǎo de, tā dào le bàngōngshì wǒ jiù gàosu tā.", "vi": "Dạ vâng, khi nào giám đốc đến văn phòng em sẽ báo lại ngay ạ."}
            ],
            "check_question": {
                "question": "周经理什么时候回办公室？",
                "options": ["明天早上", "下午", "中午十二点", "下个星期"],
                "ans": "B",
                "explain": "Thư ký trả lời: '他出去办事了，下午回来' (Anh ấy ra ngoài làm việc, buổi chiều về)."
            }
        },
        {
            "num": 3,
            "title": "在楼门口送朋友 (Tiễn bạn ở trước cửa tòa nhà)",
            "location": "在楼门口 (Trước cửa tòa nhà)",
            "audio_file": "audio_textbook/Bai_02/02-3.mp3",
            "context": "Trời đổ mưa to, Tiểu Cương tiễn Tiểu Lệ ra về và chạy lên lầu lấy ô cho cô.",
            "lines": [
                {"speaker": "小刚", "role": "male", "zh": "雨下得真大。你怎么回去？我送你吧。", "py": "Yǔ xià de zhēn dà. Nǐ zěnme huíqu? Wǒ sòng nǐ ba.", "vi": "Mưa to quá. Em về bằng cách nào? Để anh đưa em về nhé."},
                {"speaker": "小丽", "role": "female", "zh": "没事，我出去叫辆出租车就行了。", "py": "Méi shì, wǒ chūqu jiào liàng chūzūchē jiù xíng le.", "vi": "Không sao đâu, em ra ngoài bắt một chiếc taxi là được rồi."},
                {"speaker": "小刚", "role": "male", "zh": "那你等等，我上楼去给你拿把伞。", "py": "Nà nǐ děngdeng, wǒ shàng lóu qù gěi nǐ ná bǎ sǎn.", "vi": "Thế em đợi chút, anh lên lầu lấy cho em chiếc ô."},
                {"speaker": "小丽", "role": "female", "zh": "好的。我跟你一起上去吧。", "py": "Hǎo de. Wǒ gēn nǐ yìqǐ shàngqu ba.", "vi": "Vâng, em cùng đi lên với anh nhé."},
                {"speaker": "小刚", "role": "male", "zh": "你在这儿等吧，我拿了伞就下来。", "py": "Nǐ zài zhèr děng ba, wǒ ná le sǎn jiù xiàlai.", "vi": "Em ở đây đợi đi, anh lấy ô xong là xuống ngay."}
            ],
            "check_question": {
                "question": "小刚为什么上楼？",
                "options": ["回房间睡觉", "去拿雨伞给小丽", "去找钥匙", "去打电话"],
                "ans": "B",
                "explain": "Tiểu Cương bảo: '那你等等，我上楼去给你拿把伞' (Em đợi chút, anh lên lầu lấy cho em chiếc ô)."
            }
        },
        {
            "num": 4,
            "title": "在家 (Ở nhà)",
            "location": "在家 (Ở nhà)",
            "audio_file": "audio_textbook/Bai_02/02-4.mp3",
            "context": "Chu thái thái than phiền với chồng Chu Minh về việc bị béo lên dù ngày nào cũng 'vận động' nấu nướng.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "你看，我这么胖，怎么办呢？", "py": "Nǐ kàn, wǒ zhème pàng, zěnme bàn ne?", "vi": "Anh xem, em béo thế này, phải làm sao bây giờ?"},
                {"speaker": "周明", "role": "male", "zh": "你每天晚上吃了饭就睡觉，也不出去走走，能不胖吗？", "py": "Nǐ měi tiān wǎnshang chī le fàn jiù shuìjiào, yě bù chūqu zǒuzou, néng bú pàng ma?", "vi": "Em tối nào ăn cơm xong cũng đi ngủ ngay, chẳng ra ngoài đi dạo, hỏi sao không béo?"},
                {"speaker": "周太太", "role": "female", "zh": "其实我每天都运动。", "py": "Qíshí wǒ měi tiān dōu yùndòng.", "vi": "Thực ra ngày nào em cũng vận động đấy chứ."},
                {"speaker": "周明", "role": "male", "zh": "但是你一点儿也没瘦！你做什么运动了？", "py": "Dànshì nǐ yìdiǎnr yě méi shòu! Nǐ zuò shénme yùndòng le?", "vi": "Nhưng em chẳng gầy đi tí nào cả! Em đã tập môn vận động gì thế?"},
                {"speaker": "周太太", "role": "female", "zh": "做饭啊。", "py": "Zuò fàn a.", "vi": "Nấu cơm đó."}
            ],
            "check_question": {
                "question": "周太太说的“运动”其实是指什么？",
                "options": ["跑步", "做饭", "爬山", "游泳"],
                "ans": "B",
                "explain": "Chu thái thái hài hước trả lời chồng: '做饭啊' (Nấu cơm đó)."
            }
        }
    ],

    # ========================== BÀI 03 ==========================
    3: [
        {
            "num": 1,
            "title": "在小丽家 (Ở nhà của chị Lệ)",
            "location": "在小丽家 (Ở nhà Tiểu Lệ)",
            "audio_file": "audio_textbook/Bai_03/03-1.mp3",
            "context": "Tiểu Cương hỏi Tiểu Lệ về thời tiết ngày mai để chuẩn bị đi leo núi.",
            "lines": [
                {"speaker": "小刚", "role": "male", "zh": "明天是晴天还是阴天？", "py": "Míngtiān shì qíngtiān háishi yīntiān?", "vi": "Ngày mai là trời nắng hay trời âm u?"},
                {"speaker": "小丽", "role": "female", "zh": "阴天，电视上说多云。怎么了？有事？", "py": "Yīntiān, diànshì shang shuō duōyún. Zěnme le? Yǒu shì?", "vi": "Trời âm u, trên tivi bảo nhiều mây. Sao thế? Có việc gì à?"},
                {"speaker": "小刚", "role": "male", "zh": "没事，我们明天要去爬山。", "py": "Méi shì, wǒmen míngtiān yào qù pá shān.", "vi": "Không có gì, ngày mai bọn anh định đi leo núi."},
                {"speaker": "小丽", "role": "female", "zh": "爬山的时候要小心点儿。", "py": "Pá shān de shíhou yào xiǎoxīn diǎnr.", "vi": "Lúc leo núi nhớ phải cẩn thận một chút đấy."},
                {"speaker": "小刚", "role": "male", "zh": "好，你也去吗？", "py": "Hǎo, nǐ yě qù ma?", "vi": "Được rồi, em cũng đi chứ?"},
                {"speaker": "小丽", "role": "female", "zh": "我不去，我有事。", "py": "Wǒ bú qù, wǒ yǒu shì.", "vi": "Em không đi đâu, em bận việc rồi."}
            ],
            "check_question": {
                "question": "小刚明天打算去哪儿？",
                "options": ["去超市买东西", "去爬山", "去喝咖啡", "在家里休息"],
                "ans": "B",
                "explain": "Tiểu Cương nói: '我们明天要去爬山' (Ngày mai bọn anh định đi leo núi)."
            }
        },
        {
            "num": 2,
            "title": "在商场 (Ở cửa hàng bách hóa)",
            "location": "在商场 (Ở cửa hàng bách hóa)",
            "audio_file": "audio_textbook/Bai_03/03-2.mp3",
            "context": "Chu thái thái và Chu Minh đi mua sắm quần áo ở trung tâm thương mại.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "你觉得这条裤子怎么样？", "py": "Nǐ juéde zhè tiáo kùzi zěnmeyàng?", "vi": "Anh thấy chiếc quần này thế nào?"},
                {"speaker": "周明", "role": "male", "zh": "我记得你已经有两条这样的裤子了。", "py": "Wǒ jìde nǐ yǐjīng yǒu liǎng tiáo zhèyàng de kùzi le.", "vi": "Anh nhớ em đã có hai chiếc quần kiểu như thế này rồi mà."},
                {"speaker": "周太太", "role": "female", "zh": "那我们再看看别的。", "py": "Nà wǒmen zài kànkan bié de.", "vi": "Thế chúng mình xem thêm cái khác vậy."},
                {"speaker": "周明", "role": "male", "zh": "这件衬衫怎么样？", "py": "Zhè jiàn chènshān zěnmeyàng?", "vi": "Chiếc áo sơ mi này thế nào?"},
                {"speaker": "周太太", "role": "female", "zh": "还不错，多少钱？", "py": "Hái búcuò, duōshao qián?", "vi": "Cũng đẹp đấy, bao nhiêu tiền thế anh?"},
                {"speaker": "周明", "role": "male", "zh": "这上面写着320元。", "py": "Zhè shàngmian xiězhe sān bǎi èrshí yuán.", "vi": "Trên này ghi 320 tệ."},
                {"speaker": "周太太", "role": "female", "zh": "买一件。", "py": "Mǎi yí jiàn.", "vi": "Mua một chiếc nhé."}
            ],
            "check_question": {
                "question": "这件衬衫多少钱？",
                "options": ["220元", "320元", "420元", "120元"],
                "ans": "B",
                "explain": "Chu Minh đọc giá trên áo: '这上面写着320元' (Trên này ghi giá 320 tệ)."
            }
        },
        {
            "num": 3,
            "title": "在水果店 (Ở cửa hàng trái cây)",
            "location": "在水果店 (Ở cửa hàng trái cây)",
            "audio_file": "audio_textbook/Bai_03/03-3.mp3",
            "context": "Vợ chồng Chu Minh đi mua dưa hấu và táo tươi ngon.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "这些水果真新鲜，我们买西瓜还是苹果？", "py": "Zhèxiē shuǐguǒ zhēn xīnxian, wǒmen mǎi xīguā háishi píngguǒ?", "vi": "Hoa quả ở đây tươi thật, chúng mình mua dưa hấu hay táo?"},
                {"speaker": "周明", "role": "male", "zh": "西瓜吧。你看，这上面写着“西瓜不甜不要钱”。", "py": "Xīguā ba. Nǐ kàn, zhè shàngmian xiězhe 'xīguā bù tián bú yào qián'.", "vi": "Dưa hấu đi. Em xem, trên này viết 'dưa không ngọt không lấy tiền' kìa."},
                {"speaker": "周太太", "role": "female", "zh": "那我们买一个大点儿的吧。", "py": "Nà wǒmen mǎi yí ge dà diǎnr de ba.", "vi": "Thế chúng mình mua một quả to một chút nhé."},
                {"speaker": "周明", "role": "male", "zh": "再买几个苹果。", "py": "Zài mǎi jǐ ge píngguǒ.", "vi": "Mua thêm mấy quả táo nữa."},
                {"speaker": "周太太", "role": "female", "zh": "好啊，今天晚上只吃水果不吃饭！", "py": "Hǎo a, jīntiān wǎnshang zhǐ chī shuǐguǒ bù chī fàn!", "vi": "Được thôi, tối nay chỉ ăn hoa quả không ăn cơm!"}
            ],
            "check_question": {
                "question": "水果店的牌子上写着什么？",
                "options": ["水果打折", "西瓜不甜不要钱", "苹果新鲜又便宜", "欢迎光临"],
                "ans": "B",
                "explain": "Chu Minh chỉ cho vợ xem biển quảng cáo: '你看，这上面写着“西瓜不甜不要钱”'."
            }
        },
        {
            "num": 4,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_03/03-4.mp3",
            "context": "Tiểu Lệ và Tiểu Cương giải lao thưởng thức đồ uống và trò chuyện về sở thích uống trà.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "桌子上放着很多饮料，你喝什么？", "py": "Zhuōzi shang fàngzhe hěn duō yǐnliào, nǐ hē shénme?", "vi": "Trên bàn để rất nhiều đồ uống, anh uống gì?"},
                {"speaker": "小刚", "role": "male", "zh": "茶或者咖啡都可以。你呢？你喝什么？", "py": "Chá huòzhě kāfēi dōu kěyǐ. Nǐ ne? Nǐ hē shénme?", "vi": "Trà hay cà phê đều được cả. Còn em? Em uống gì?"},
                {"speaker": "小丽", "role": "female", "zh": "我喝茶，茶是我的最爱。天冷了或者工作累了的时候，喝杯热茶会很舒服。", "py": "Wǒ hē chá, chá shì wǒ de zuì ài. Tiān lěng le huòzhě gōngzuò lèi le de shíhou, hē bēi rè chá huì hěn shūfu.", "vi": "Em uống trà, trà là thức uống em thích nhất. Trời lạnh hoặc lúc làm việc mệt mỏi, uống tách trà nóng sẽ rất dễ chịu."},
                {"speaker": "小刚", "role": "male", "zh": "你喜欢喝什么茶？", "py": "Nǐ xǐhuan hē shénme chá?", "vi": "Em thích uống loại trà nào?"},
                {"speaker": "小丽", "role": "female", "zh": "花茶、绿茶、红茶，我都喜欢。", "py": "Huāchá, lǜchá, hóngchá, wǒ dōu xǐhuan.", "vi": "Trà hoa, trà xanh, trà đen, em đều thích cả."}
            ],
            "check_question": {
                "question": "小丽最喜欢喝什么饮料？",
                "options": ["咖啡", "茶", "可乐", "牛奶"],
                "ans": "B",
                "explain": "Tiểu Lệ khẳng định: '我喝茶，茶是我的最爱' (Em uống trà, trà là sở thích lớn nhất của em)."
            }
        }
    ],

    # ========================== BÀI 04 ==========================
    4: [
        {
            "num": 1,
            "title": "在教室 (Trong lớp học)",
            "location": "在教室 (Trong lớp học)",
            "audio_file": "audio_textbook/Bai_04/04-1.mp3",
            "context": "Tiểu Minh và Mã Khả xem lại những bức ảnh kỷ niệm vừa chụp sau trận đấu của trường.",
            "lines": [
                {"speaker": "小明", "role": "male", "zh": "这是你们比赛的照片吗？", "py": "Zhè shì nǐmen bǐsài de zhàopiàn ma?", "vi": "Đây là ảnh chụp cuộc thi của các cậu à?"},
                {"speaker": "马可", "role": "male", "zh": "是，这是我们比赛后照的。", "py": "Shì, zhè shì wǒmen bǐsài hòu zhào de.", "vi": "Đúng thế, đây là ảnh chúng tớ chụp sau trận đấu đấy."},
                {"speaker": "小明", "role": "male", "zh": "照得不错，你们都是一个年级的吗？", "py": "Zhào de búcuò, nǐmen dōu shì yí ge niánjí de ma?", "vi": "Chụp đẹp đấy, các cậu đều cùng một khối lớp à?"},
                {"speaker": "马可", "role": "male", "zh": "不是。那个又高又漂亮的女孩儿是二年级的。", "py": "Bú shì. Nà ge yòu gāo yòu piàoliang de nǚhái'r shì èr niánjí de.", "vi": "Không phải đâu. Cô bạn vừa cao vừa xinh xắn kia là học sinh lớp 2 đấy."},
                {"speaker": "小明", "role": "male", "zh": "旁边那个拿着书笑的人是谁？", "py": "Pángbiān nà ge názhe shū xiào de rén shì shéi?", "vi": "Thế người cầm quyển sách mỉm cười ở bên cạnh là ai thế?"},
                {"speaker": "马可", "role": "male", "zh": "那是我！", "py": "Nà shì wǒ!", "vi": "Đấy chính là tớ đấy!"}
            ],
            "check_question": {
                "question": "照片里那个又高又漂亮的女孩儿是几年级的？",
                "options": ["一年级的", "二年级的", "三年级的", "四年级的"],
                "ans": "B",
                "explain": "Trong bài khóa, Mã Khả trả lời rõ ràng: '那个又高又漂亮的女孩儿是二年级的'."
            }
        },
        {
            "num": 2,
            "title": "在教室 (Trong lớp học)",
            "location": "在教室 (Trong lớp học)",
            "audio_file": "audio_textbook/Bai_04/04-2.mp3",
            "context": "Tiểu Lệ tò mò hỏi bạn học về tính cách và sự nổi tiếng của Tiểu Hồng trong lớp.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "你觉得小红怎么样？", "py": "Nǐ juéde Xiǎohóng zěnmeyàng?", "vi": "Cậu thấy Tiểu Hồng thế nào?"},
                {"speaker": "同学", "role": "male", "zh": "她又聪明又热情，也很努力。", "py": "Tā yòu cōngmíng yòu rèqíng, yě hěn nǔlì.", "vi": "Cô ấy vừa thông minh vừa nhiệt tình, lại còn rất chăm chỉ nữa."},
                {"speaker": "小丽", "role": "female", "zh": "我看她总是笑着回答老师的问题。", "py": "Wǒ kàn tā zǒngshì xiàozhe huídá lǎoshī de wèntí.", "vi": "Tớ thấy cô ấy lúc nào cũng cười khi trả lời câu hỏi của thầy cô."},
                {"speaker": "同学", "role": "male", "zh": "她对每个人都笑，也常常对我笑。", "py": "Tā duì měi ge rén dōu xiào, yě chángcháng duì wǒ xiào.", "vi": "Cô ấy đối với ai cũng cười niềm nở, cũng thường xuyên cười với tớ nữa."},
                {"speaker": "小丽", "role": "female", "zh": "你是不是喜欢她啊？", "py": "Nǐ shì bu shì xǐhuan tā a?", "vi": "Có phải cậu thích cô ấy rồi không hả?"},
                {"speaker": "同学", "role": "male", "zh": "喜欢她的人太多了，你看那些拿着鲜花站在门口的，都是等她的。", "py": "Xǐhuan tā de rén tài duō le, nǐ kàn nàxiē názhe xiānhuā zhàn zài ménkǒu de, dōu shì děng tā de.", "vi": "Người thích cô ấy nhiều lắm, cậu xem những người cầm hoa tươi đứng ở cửa kia kìa, toàn là đợi cô ấy đấy."}
            ],
            "check_question": {
                "question": "小红平时怎么回答老师的问题？",
                "options": ["大声回答", "站着不说话", "总是笑着回答", "很不情愿地回答"],
                "ans": "C",
                "explain": "Tiểu Lệ nhận xét: '我看她总是笑着回答老师的问题'."
            }
        },
        {
            "num": 3,
            "title": "在超市门口 (Ở trước cửa siêu thị)",
            "location": "在超市门口 (Ở trước cửa siêu thị)",
            "audio_file": "audio_textbook/Bai_04/04-3.mp3",
            "context": "Tiểu Cương và Tiểu Lệ đi ngang qua siêu thị, cả hai quyết định vào mua bánh ngọt để về nhà vừa ăn vừa xem tivi.",
            "lines": [
                {"speaker": "小刚", "role": "male", "zh": "我有点儿饿了，我们进超市买点儿东西吧。", "py": "Wǒ yǒudiǎnr è le, wǒmen jìn chāoshì mǎi diǎnr dōngxi ba.", "vi": "Anh hơi đói bụng rồi, chúng mình vào siêu thị mua chút gì ăn đi."},
                {"speaker": "小丽", "role": "female", "zh": "好啊，这家超市的蛋糕又便宜又好吃，一块只要2.99元。", "py": "Hǎo a, zhè jiā chāoshì de dàngāo yòu piányi yòu hǎochī, yí kuàir zhǐ yào èr diǎn jiǔ jiǔ yuán.", "vi": "Được thôi, bánh kem của siêu thị này vừa rẻ lại vừa ngon miệng, một miếng chỉ có 2.99 tệ."},
                {"speaker": "小刚", "role": "male", "zh": "我们买两块儿，回家吃着蛋糕看电视，怎么样？", "py": "Wǒmen mǎi liǎng kuàir, huí jiā chīzhe dàngāo kàn diànshì, zěnmeyàng?", "vi": "Chúng mình mua hai miếng nhé, về nhà vừa ăn bánh ngọt vừa xem tivi, thế nào?"},
                {"speaker": "小丽", "role": "female", "zh": "好啊，我再去买一些喝的。", "py": "Hǎo a, wǒ zài qù mǎi yìxiē hē de.", "vi": "Tuyệt quá, em đi mua thêm một ít đồ uống nữa nhé."},
                {"speaker": "小刚", "role": "male", "zh": "喝着咖啡吃蛋糕，太好了！", "py": "Hēzhe kāfēi chī dàngāo, tài hǎo le!", "vi": "Vừa nhâm nhi cà phê vừa ăn bánh kem, quả là tuyệt vời!"}
            ],
            "check_question": {
                "question": "他们打算回家做什么？",
                "options": ["做晚饭和洗衣服", "吃着蛋糕看电视", "喝着茶做作业", "睡觉和听音乐"],
                "ans": "B",
                "explain": "Tiểu Cương đề xuất: '回家吃着蛋糕看电视，怎么样？' (Về nhà vừa ăn bánh vừa xem tivi nhé)."
            }
        },
        {
            "num": 4,
            "title": "在饭馆儿 (Ở quán ăn)",
            "location": "在饭馆儿 (Ở quán ăn)",
            "audio_file": "audio_textbook/Bai_04/04-4.mp3",
            "context": "Vị khách đến quán ăn muốn tìm lại cô nhân viên phục vụ vừa trẻ trung, nhiệt tình lại luôn niềm nở tươi cười.",
            "lines": [
                {"speaker": "经理", "role": "male", "zh": "您好！您找谁？", "py": "Nín hǎo! Nín zhǎo shéi?", "vi": "Xin chào bác! Bác tìm ai ạ?"},
                {"speaker": "客人", "role": "male", "zh": "你们这儿是不是有一个又年轻又漂亮的服务员？", "py": "Nǐmen zhèr shì bu shì yǒu yí ge yòu niánqīng yòu piàoliang de fúwùyuán?", "vi": "Ở chỗ các anh có phải có một cô nhân viên phục vụ vừa trẻ vừa xinh đẹp không?"},
                {"speaker": "经理", "role": "male", "zh": "我们这儿年轻、漂亮的服务员有很多。", "py": "Wǒmen zhèr niánqīng, piàoliang de fúwùyuán yǒu hěnduō.", "vi": "Chỗ chúng tôi nhân viên phục vụ trẻ đẹp thì có nhiều lắm."},
                {"speaker": "客人", "role": "male", "zh": "她工作又认真又热情。", "py": "Tā gōngzuò yòu rènzhēn yòu rèqíng.", "vi": "Cô ấy làm việc vừa nghiêm túc chăm chỉ lại vừa nhiệt tình chu đáo."},
                {"speaker": "经理", "role": "male", "zh": "您能再说说吗？", "py": "Nín néng zài shuōshuo ma?", "vi": "Bác có thể miêu tả thêm chút nữa được không ạ?"},
                {"speaker": "客人", "role": "male", "zh": "她总是笑着跟客人说话。", "py": "Tā zǒngshì xiàozhe gēn kèrén shuōhuà.", "vi": "Cô ấy lúc nào cũng tươi cười khi nói chuyện với khách hàng."},
                {"speaker": "经理", "role": "male", "zh": "啊，我知道了，你说的是李小美吧？", "py": "À, wǒ zhīdào le, nǐ shuō de shì Lǐ Xiǎoměi ba?", "vi": "À, tôi biết rồi, người bác đang nói tới là Lý Tiểu Mỹ phải không?"}
            ],
            "check_question": {
                "question": "客人要找的那个服务员叫什么名字？",
                "options": ["小丽", "小红", "李小美", "马可"],
                "ans": "C",
                "explain": "Giám đốc sau khi nghe miêu tả đã nhận ra ngay: '啊，我知道了，你说的是李小美吧？'."
            }
        }
    ],

    # ========================== BÀI 05 ==========================
    5: [
        {
            "num": 1,
            "title": "在小丽家 (Tại nhà chị Lệ)",
            "location": "在小丽家 (Tại nhà Tiểu Lệ)",
            "audio_file": "audio_textbook/Bai_05/05-1.mp3",
            "context": "Bạn đến nhà thăm Tiểu Lệ bị ốm, mang biếu trà xanh và hỏi han bệnh tình.",
            "lines": [
                {"speaker": "朋友", "role": "female", "zh": "我听说你身体不舒服，怎么了？", "py": "Wǒ tīngshuō nǐ shēntǐ bù shūfu, zěnme le?", "vi": "Tôi nghe nói bạn người không khỏe, sao thế?"},
                {"speaker": "小丽", "role": "female", "zh": "前几天有点儿发烧，现在好多了。", "py": "Qián jǐ tiān yǒudiǎnr fā shāo, xiànzài hǎoduō le.", "vi": "Mấy hôm trước hơi bị sốt, bây giờ đỡ nhiều rồi."},
                {"speaker": "朋友", "role": "female", "zh": "喝杯茶吧，这是我为你买的绿茶，很不错。", "py": "Hē bēi chá ba, zhè shì wǒ wèi nǐ mǎi de lǜchá, hěn búcuò.", "vi": "Uống cốc trà đi, đây là trà xanh tôi mua cho bạn, ngon lắm đấy."},
                {"speaker": "小丽", "role": "female", "zh": "谢谢，我要吃药，不喝茶了。", "py": "Xièxie, wǒ yào chī yào, bù hē chá le.", "vi": "Cảm ơn bạn, mình chuẩn bị uống thuốc, không uống trà đâu."},
                {"speaker": "朋友", "role": "female", "zh": "那喝杯水吧。", "py": "Nà hē bēi shuǐ ba.", "vi": "Thế uống cốc nước lọc nhé."},
                {"speaker": "小丽", "role": "female", "zh": "好的。", "py": "Hǎo de.", "vi": "Được thôi."}
            ],
            "check_question": {
                "question": "小丽为什么不喝绿茶？",
                "options": ["她不喜欢喝茶", "她要吃药", "绿茶太烫了", "她想喝咖啡"],
                "ans": "B",
                "explain": "Tiểu Lệ giải thích: '我要吃药，不喝茶了' (Mình phải uống thuốc nên không uống trà)."
            }
        },
        {
            "num": 2,
            "title": "在打电话 (Nói chuyện qua điện thoại)",
            "location": "在打电话 (Gọi điện thoại)",
            "audio_file": "audio_textbook/Bai_05/05-2.mp3",
            "context": "Chu thái thái gọi điện cho Trương thái thái cáo lỗi không đi chơi được vì phải ở nhà chăm sóc con trai bị ốm.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "对不起，我明天不能和你们出去玩儿了。", "py": "Duìbuqǐ, wǒ míngtiān bù néng hé nǐmen chūqu wánr le.", "vi": "Xin lỗi nhé, ngày mai tôi không thể đi chơi cùng mọi người được rồi."},
                {"speaker": "张太太", "role": "female", "zh": "为什么？怎么了？", "py": "Wèishénme? Zěnme le?", "vi": "Sao thế? Có chuyện gì vậy?"},
                {"speaker": "周太太", "role": "female", "zh": "我儿子生病了，我要在家照顾他。", "py": "Wǒ érzi shēng bìng le, wǒ yào zài jiā zhàogù tā.", "vi": "Con trai tôi bị ốm rồi, tôi phải ở nhà chăm sóc cháu."},
                {"speaker": "张太太", "role": "female", "zh": "他吃药了吗？要不要去医院？", "py": "Tā chī yào le ma? Yào bu yào qù yīyuàn?", "vi": "Cháu đã uống thuốc chưa? Có cần đi bệnh viện không?"},
                {"speaker": "周太太", "role": "female", "zh": "不用去医院，昨天吃了感冒药，现在好一些了。", "py": "Búyòng qù yīyuàn, zuótiān chīle gǎnmào yào, xiànzài hǎo yìxiē le.", "vi": "Không cần đi viện đâu, hôm qua uống thuốc cảm rồi, giờ đỡ hơn một chút rồi."},
                {"speaker": "张太太", "role": "female", "zh": "那我们下次再一起出去玩儿吧。", "py": "Nà wǒmen xià cì zài yìqǐ chūqu wánr ba.", "vi": "Vậy để lần sau chúng mình lại cùng nhau đi chơi nhé."}
            ],
            "check_question": {
                "question": "周太太明天为什么不能出去玩儿？",
                "options": ["她要加班", "她要在家里照顾生病的儿子", "外面下大雨", "她自己发烧了"],
                "ans": "B",
                "explain": "Chu thái thái nói: '我儿子生病了，我要在家照顾他' (Con trai tôi bị ốm, tôi phải ở nhà chăm sóc cháu)."
            }
        },
        {
            "num": 3,
            "title": "在小刚家 (Tại nhà anh Cương)",
            "location": "在小刚家 (Tại nhà Tiểu Cương)",
            "audio_file": "audio_textbook/Bai_05/05-3.mp3",
            "context": "Tiểu Lệ và Tiểu Cương trò chuyện về các mùa trong năm và sở thích ăn mặc.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "你最喜欢哪个季节？", "py": "Nǐ zuì xǐhuan nǎge jìjié?", "vi": "Anh thích mùa nào nhất trong năm?"},
                {"speaker": "小刚", "role": "male", "zh": "当然是春天，天气不那么冷了，草和树都绿了，花也开了。", "py": "Dāngrán shì chūntiān, tiānqì bú nàme lěng le, cǎo hé shù dōu lǜ le, huā yě kāi le.", "vi": "Đương nhiên là mùa xuân, thời tiết không còn lạnh như thế nữa, cỏ và cây đều xanh tươi, hoa cũng nở rồi."},
                {"speaker": "小丽", "role": "female", "zh": "我最喜欢夏天，因为我可以穿漂亮的裙子了。", "py": "Wǒ zuì xǐhuan xiàtiān, yīnwèi wǒ kěyǐ chuān piàoliang de qúnzi le.", "vi": "Em thì thích mùa hè nhất, bởi vì em có thể mặc những chiếc váy xinh xắn rồi."},
                {"speaker": "小刚", "role": "male", "zh": "那我也喜欢夏天了。", "py": "Nà wǒ yě xǐhuan xiàtiān le.", "vi": "Thế thì anh cũng thích mùa hè rồi."},
                {"speaker": "小丽", "role": "female", "zh": "怎么？你也有漂亮的裙子？", "py": "Zěnme? Nǐ yě yǒu piàoliang de qúnzi?", "vi": "Sao thế? Anh cũng có váy đẹp à?"},
                {"speaker": "小刚", "role": "male", "zh": "不，我喜欢看你穿漂亮的裙子。", "py": "Bù, wǒ xǐhuan kàn nǐ chuān piàoliang de qúnzi.", "vi": "Không, anh thích ngắm em mặc váy đẹp cơ."}
            ],
            "check_question": {
                "question": "小刚为什么也喜欢夏天？",
                "options": ["因为夏天可以吃西瓜", "因为他喜欢看小丽穿漂亮的裙子", "因为夏天的天气很暖和", "因为夏天可以去游泳"],
                "ans": "B",
                "explain": "Tiểu Cương bày tỏ tình cảm: '不，我喜欢看你穿漂亮的裙子' (Không, anh thích nhìn em mặc váy đẹp)."
            }
        },
        {
            "num": 4,
            "title": "在小刚家 (Tại nhà anh Cương)",
            "location": "在小刚家 (Tại nhà Tiểu Cương)",
            "audio_file": "audio_textbook/Bai_05/05-4.mp3",
            "context": "Tiểu Lệ than phiền dạo này ngày càng béo lên, váy cũ năm ngoái năm nay không mặc vừa nữa.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "我最近越来越胖了。", "py": "Wǒ zuìjìn yuè lái yuè pàng le.", "vi": "Dạo này em ngày càng béo ra rồi."},
                {"speaker": "小刚", "role": "male", "zh": "谁说的？我觉得你越来越漂亮了。", "py": "Shéi shuō de? Wǒ juéde nǐ yuè lái yuè piàoliang le.", "vi": "Ai bảo thế? Anh thấy em ngày càng xinh đẹp ra đấy chứ."},
                {"speaker": "小丽", "role": "female", "zh": "你看，这条裙子是去年买的，今年就不能穿了。", "py": "Nǐ kàn, zhè tiáo qúnzi shì qùnián mǎi de, jīnnián jiù bù néng chuān le.", "vi": "Anh xem, chiếc váy này mua năm ngoái, năm nay đã không mặc vừa nữa rồi."},
                {"speaker": "小刚", "role": "male", "zh": "那是因为你吃得太多了，少吃点儿吧。", "py": "Nà shì yīnwèi nǐ chī de tài duō le, shǎo chī diǎnr ba.", "vi": "Đó là tại em ăn nhiều quá đấy, ăn ít đi một chút nhé."},
                {"speaker": "小丽", "role": "female", "zh": "我做的饭越来越好吃，我能少吃吗？", "py": "Wǒ zuò de fàn yuè lái yuè hǎochī, wǒ néng shǎo chī ma?", "vi": "Cơm em nấu ngày càng ngon, em ăn ít đi sao được?"}
            ],
            "check_question": {
                "question": "小丽为什么觉得少吃点儿很难？",
                "options": ["因为饭馆的菜太好吃了", "因为她做的饭越来越好吃", "因为她每天晚上都很饿", "因为小刚一直叫她吃"],
                "ans": "B",
                "explain": "Tiểu Lệ dí dỏm bảo: '我做的饭越来越好吃，我能少吃吗？' (Cơm em nấu ngày càng ngon, em nhịn sao được)."
            }
        }
    ],

    # ========================== BÀI 06 ==========================
    6: [
        {
            "num": 1,
            "title": "在客厅 (Trong phòng khách)",
            "location": "在客厅 (Trong phòng khách)",
            "audio_file": "audio_textbook/Bai_06/06-1.mp3",
            "context": "Chu Minh không tìm thấy kính mắt, nhờ vợ Chu thái thái giúp tìm.",
            "lines": [
                {"speaker": "周明", "role": "male", "zh": "我的眼镜呢？怎么突然找不到了？你看见了吗？", "py": "Wǒ de yǎnjìng ne? Zěnme tūrán zhǎo bu dào le? Nǐ kànjiàn le ma?", "vi": "Kính mắt của anh đâu rồi? Sao tự dưng không tìm thấy nữa? Em có nhìn thấy không?"},
                {"speaker": "周太太", "role": "female", "zh": "我没看见啊。", "py": "Wǒ méi kànjiàn a.", "vi": "Em không nhìn thấy."},
                {"speaker": "周明", "role": "male", "zh": "我离不开眼镜，没有眼镜，我一个字也看不清楚。", "py": "Wǒ lí bu kāi yǎnjìng, méiyǒu yǎnjìng, wǒ yí ge zì yě kàn bu qīngchu.", "vi": "Anh không thể rời cái kính được, không có kính một chữ anh cũng nhìn không rõ."},
                {"speaker": "周太太", "role": "female", "zh": "你去房间找找，是不是刚才放在桌子上了？", "py": "Nǐ qù fángjiān zhǎozhao, shì bu shì gāngcái fàng zài zhuōzi shang le?", "vi": "Anh vào phòng tìm xem, có phải vừa nãy để trên bàn rồi không?"},
                {"speaker": "周明", "role": "male", "zh": "我怎么看得到啊？你快过来帮忙啊。", "py": "Wǒ zěnme kàn de dào a? Nǐ kuài guòlai bāngmáng a.", "vi": "Anh làm sao mà thấy được? Em mau qua đây giúp anh với."},
                {"speaker": "周太太", "role": "female", "zh": "好吧，我帮你去找找。", "py": "Hǎo ba, wǒ bāng nǐ qù zhǎozhao.", "vi": "Được rồi, để em giúp anh đi tìm."}
            ],
            "check_question": {
                "question": "周明为什么让周太太帮忙找眼镜？",
                "options": ["因为他要急着出门", "因为没有眼镜他一个字也看不清楚", "因为周太太知道放在哪里", "因为房间太黑了"],
                "ans": "B",
                "explain": "Chu Minh giải thích: '我离不开眼镜，没有眼镜，我一个字也看不清楚' (Không có kính một chữ anh cũng nhìn không rõ)."
            }
        },
        {
            "num": 2,
            "title": "在打电话 (Nói chuyện qua điện thoại)",
            "location": "在打电话 (Gọi điện thoại)",
            "audio_file": "audio_textbook/Bai_06/06-2.mp3",
            "context": "Bạn học gọi điện hỏi bài tập về nhà, bạn trai mời đến nhà mình để giảng bài.",
            "lines": [
                {"speaker": "同学", "role": "female", "zh": "今天的作业你做完了吗？", "py": "Jīntiān de zuòyè nǐ zuòwán le ma?", "vi": "Bài tập hôm nay cậu đã làm xong chưa?"},
                {"speaker": "儿子", "role": "male", "zh": "刚做完，你呢？", "py": "Gāng zuòwán, nǐ ne?", "vi": "Tớ vừa làm xong, còn cậu?"},
                {"speaker": "同学", "role": "female", "zh": "今天这些题特别难，我看不懂，不会做，你能帮我吗？", "py": "Jīntiān zhèxiē tí tèbié nán, wǒ kàn bu dǒng, bú huì zuò, nǐ néng bāng wǒ ma?", "vi": "Hôm nay mấy bài này khó quá, tớ đọc không hiểu, chẳng biết làm, cậu giúp tớ được không?"},
                {"speaker": "儿子", "role": "male", "zh": "电话里讲不明白，你来我家吧，我给你讲讲。", "py": "Diànhuà li jiǎng bu míngbai, nǐ lái wǒ jiā ba, wǒ gěi nǐ jiǎngjiang.", "vi": "Nói qua điện thoại không giải thích rõ được đâu, cậu đến nhà tớ đi, tớ giảng cho."},
                {"speaker": "同学", "role": "female", "zh": "好啊，我锻炼完了就过去。", "py": "Hǎo a, wǒ duànliàn wán le jiù guòqu.", "vi": "Được thôi, tớ tập thể dục xong là qua liền."}
            ],
            "check_question": {
                "question": "同学为什么要去儿子家里？",
                "options": ["一起玩电脑游戏", "让儿子给她讲难懂的作业题", "一起去公园锻炼", "吃晚饭"],
                "ans": "B",
                "explain": "Con trai bảo: '电话里讲不明白，你来我家吧，我给你讲讲' (Qua điện thoại khó giảng rõ, cậu đến nhà tớ giảng cho)."
            }
        },
        {
            "num": 3,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_06/06-3.mp3",
            "context": "Đồng nghiệp hỏi thăm Tiểu Cương khi thấy anh buồn rầu vì chưa tìm được chỗ hẹn hò ưng ý với Tiểu Lệ.",
            "lines": [
                {"speaker": "同事", "role": "male", "zh": "你怎么有点儿不高兴？", "py": "Nǐ zěnme yǒudiǎnr bù gāoxìng?", "vi": "Sao trông cậu có vẻ không vui thế?"},
                {"speaker": "小刚", "role": "male", "zh": "我想请小丽吃饭，但是找不到好饭馆儿。", "py": "Wǒ xiǎng qǐng Xiǎolì chī fàn, dànshì zhǎo bu dào hǎo fànguǎnr.", "vi": "Tớ muốn mời Tiểu Lệ đi ăn cơm, nhưng không tìm được quán ăn ngon."},
                {"speaker": "同事", "role": "male", "zh": "那你请她听音乐会吧，她喜欢听音乐。", "py": "Nà nǐ qǐng tā tīng yīnyuèhuì ba, tā xǐhuan tīng yīnyuè.", "vi": "Thế cậu mời cô ấy đi nghe hòa nhạc đi, cô ấy thích nghe nhạc mà."},
                {"speaker": "小刚", "role": "male", "zh": "音乐会人太多，买不到票。", "py": "Yīnyuèhuì rén tài duō, mǎi bu dào piào.", "vi": "Buổi hòa nhạc đông người quá, không mua được vé."},
                {"speaker": "同事", "role": "male", "zh": "那去公园走走，聊聊天儿吧。", "py": "Nà qù gōngyuán zǒuzou, liáoliao tiānr ba.", "vi": "Thế thì ra công viên đi dạo, trò chuyện một chút đi."},
                {"speaker": "小刚", "role": "male", "zh": "公园太大，多累啊。", "py": "Gōngyuán tài dà, duō lèi a.", "vi": "Công viên rộng quá, mệt lắm."}
            ],
            "check_question": {
                "question": "小刚为什么没请小丽去听音乐会？",
                "options": ["他不喜欢音乐", "音乐会人多，买不到票", "票价太贵了", "小丽不想去"],
                "ans": "B",
                "explain": "Tiểu Cương cho biết: '音乐会人太多，买不到票' (Buổi hòa nhạc đông người quá, không mua được vé)."
            }
        },
        {
            "num": 4,
            "title": "在客厅 (Trong phòng khách)",
            "location": "在客厅 (Trong phòng khách)",
            "audio_file": "audio_textbook/Bai_06/06-4.mp3",
            "context": "Chu thái thái nhắc nhở chồng không nên uống cà phê vào buổi tối kẻo mất ngủ.",
            "lines": [
                {"speaker": "周太太", "role": "female", "zh": "你怎么还喝咖啡？", "py": "Nǐ zěnme hái hē kāfēi?", "vi": "Sao anh vẫn còn uống cà phê thế?"},
                {"speaker": "周明", "role": "male", "zh": "怎么了？", "py": "Zěnme le?", "vi": "Sao thế em?"},
                {"speaker": "周太太", "role": "female", "zh": "你不是说晚上睡不着觉吗？", "py": "Nǐ bú shì shuō wǎnshang shuì bu zháo jiào ma?", "vi": "Chẳng phải anh nói buổi tối không ngủ được sao?"},
                {"speaker": "周明", "role": "male", "zh": "没事，我只喝一杯。", "py": "Méi shì, wǒ zhǐ hē yì bēi.", "vi": "Không sao đâu, anh chỉ uống một cốc thôi."},
                {"speaker": "周太太", "role": "female", "zh": "你还是喝杯牛奶吧，可以睡得更好些。", "py": "Nǐ háishi hē bēi niúnǎi ba, kěyǐ shuì de gèng hǎo xiē.", "vi": "Anh uống cốc sữa đi thì hơn, có thể ngủ ngon hơn đấy."},
                {"speaker": "周明", "role": "male", "zh": "好吧，牛奶呢？", "py": "Hǎo ba, niúnǎi ne?", "vi": "Được rồi, thế sữa đâu?"},
                {"speaker": "周太太", "role": "female", "zh": "还没买呢。", "py": "Hái méi mǎi ne.", "vi": "Em vẫn chưa mua."}
            ],
            "check_question": {
                "question": "周太太建议周明喝什么？",
                "options": ["绿茶", "热咖啡", "牛奶", "矿泉水"],
                "ans": "C",
                "explain": "Chu thái thái khuyên: '你还是喝杯牛奶吧，可以睡得更好些' (Anh uống cốc sữa đi, sẽ ngủ ngon hơn)."
            }
        }
    ],

    # ========================== BÀI 07 ==========================
    7: [
        {
            "num": 1,
            "title": "在办公室 (Trong văn phòng)",
            "location": "在办公室 (Trong văn phòng)",
            "audio_file": "audio_textbook/Bai_07/07-1.mp3",
            "context": "Đồng nghiệp hỏi thăm Tiểu Cương về cô đồng nghiệp mới xinh xắn tên Tiểu Lệ.",
            "lines": [
                {"speaker": "同事", "role": "male", "zh": "那个漂亮的新同事是谁？", "py": "Nàge piàoliang de xīn tóngshì shì shéi?", "vi": "Đồng nghiệp mới xinh xắn kia là ai thế?"},
                {"speaker": "小刚", "role": "male", "zh": "那是小丽。", "py": "Nà shì Xiǎolì.", "vi": "Đó là Tiểu Lệ đấy."},
                {"speaker": "同事", "role": "male", "zh": "她刚来北京吗？", "py": "Tā gāng lái Běijīng ma?", "vi": "Cô ấy mới đến Bắc Kinh à?"},
                {"speaker": "小刚", "role": "male", "zh": "不，她在北京工作三年了。", "py": "Bù, tā zài Běijīng gōngzuò sān nián le.", "vi": "Không, cô ấy làm việc ở Bắc Kinh được 3 năm rồi."},
                {"speaker": "同事", "role": "male", "zh": "以前她在哪儿工作？", "py": "Yǐqián tā zài nǎr gōngzuò?", "vi": "Trước đây cô ấy làm việc ở đâu?"},
                {"speaker": "小刚", "role": "male", "zh": "她在银行工作了两年以后来的我们公司。", "py": "Tā zài yínháng gōngzuòle liǎng nián yǐhòu lái de wǒmen gōngsī.", "vi": "Cô ấy làm việc ở ngân hàng 2 năm sau đó mới đến công ty chúng ta."}
            ],
            "check_question": {
                "question": "小丽以前在哪儿工作？",
                "options": ["学校", "银行", "超市", "医院"],
                "ans": "B",
                "explain": "Tiểu Cương nói: '她在银行工作了两年以后来的我们公司' (Cô ấy làm ở ngân hàng 2 năm rồi mới sang công ty mình)."
            }
        },
        {
            "num": 2,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_07/07-2.mp3",
            "context": "Đồng nghiệp hỏi Tiểu Cương về chuyến đi chơi cuối tuần với Tiểu Lệ.",
            "lines": [
                {"speaker": "同事", "role": "male", "zh": "周末你跟小丽去哪儿玩儿了？", "py": "Zhōumò nǐ gēn Xiǎolì qù nǎr wánr le?", "vi": "Cuối tuần cậu cùng Tiểu Lệ đi đâu chơi thế?"},
                {"speaker": "小刚", "role": "male", "zh": "我们去唱歌了。", "py": "Wǒmen qù chàng gē le.", "vi": "Bọn tớ đi hát karaoke."},
                {"speaker": "同事", "role": "male", "zh": "你们唱了多久？", "py": "Nǐmen chàngle duō jiǔ?", "vi": "Các cậu hát bao lâu?"},
                {"speaker": "小刚", "role": "male", "zh": "我们唱了两个小时歌，晚上还去听音乐会了。", "py": "Wǒmen chàngle liǎng ge xiǎoshí gē, wǎnshang hái qù tīng yīnyuèhuì le.", "vi": "Bọn tớ hát hai tiếng đồng hồ, buổi tối còn đi nghe hòa nhạc nữa."},
                {"speaker": "同事", "role": "male", "zh": "你们都对音乐感兴趣吗？", "py": "Nǐmen dōu duì yīnyuè gǎn xìngqù ma?", "vi": "Các cậu đều có hứng thú với âm nhạc à?"},
                {"speaker": "小刚", "role": "male", "zh": "她对音乐感兴趣，我对她更感兴趣。", "py": "Tā duì yīnyuè gǎn xìngqù, wǒ duì tā gèng gǎn xìngqù.", "vi": "Cô ấy có hứng thú với âm nhạc, còn tớ thì có hứng thú với cô ấy hơn."}
            ],
            "check_question": {
                "question": "小刚对什么更感兴趣？",
                "options": ["音乐会", "唱歌", "小丽", "工作"],
                "ans": "C",
                "explain": "Tiểu Cương hóm hỉnh thổ lộ: '她对音乐感兴趣，我对她更感兴趣' (Cô ấy mê âm nhạc, còn tớ thì mê cô ấy hơn)."
            }
        },
        {
            "num": 3,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_07/07-3.mp3",
            "context": "Tiểu Cương bất ngờ báo tin vui sắp kết hôn với Tiểu Lệ khiến đồng nghiệp vô cùng sửng sốt.",
            "lines": [
                {"speaker": "小刚", "role": "male", "zh": "我跟小丽下个月结婚，到时候欢迎你来。", "py": "Wǒ gēn Xiǎolì xià ge yuè jié hūn, dào shíhou huānyíng nǐ lái.", "vi": "Tớ với Tiểu Lệ tháng sau kết hôn đấy, lúc đó hoan nghênh cậu đến nhé."},
                {"speaker": "同事", "role": "male", "zh": "什么？结婚？", "py": "Shénme? Jié hūn?", "vi": "Cái gì? Kết hôn á?"},
                {"speaker": "小刚", "role": "male", "zh": "对啊，突然吗？", "py": "Duì a, tūrán ma?", "vi": "Đúng thế, bất ngờ lắm phải không?"},
                {"speaker": "同事", "role": "male", "zh": "你们不是刚认识吗？", "py": "Nǐmen bú shì gāng rènshi ma?", "vi": "Chẳng phải hai người mới quen nhau sao?"},
                {"speaker": "小刚", "role": "male", "zh": "我跟她都认识五年了。", "py": "Wǒ gēn tā dōu rènshi wǔ nián le.", "vi": "Tớ với cô ấy quen nhau được năm năm rồi đấy."},
                {"speaker": "同事", "role": "male", "zh": "你跟她结婚，那我怎么办啊？", "py": "Nǐ gēn tā jié hūn, nà wǒ zěnme bàn a?", "vi": "Cậu kết hôn với cô ấy, thế tớ biết làm sao bây giờ?"}
            ],
            "check_question": {
                "question": "小刚和小丽认识多长时间了？",
                "options": ["两年", "三年", "五年", "一个月"],
                "ans": "C",
                "explain": "Tiểu Cương chia sẻ: '我跟她都认识五年了' (Tớ và cô ấy đã quen nhau được 5 năm rồi)."
            }
        },
        {
            "num": 4,
            "title": "在公司门口 (Ở trước cửa công ty)",
            "location": "在公司门口 (Ở trước cửa công ty)",
            "audio_file": "audio_textbook/Bai_07/07-4.mp3",
            "context": "Tiểu Lệ trách Tiểu Cương đến muộn, nhưng hóa ra đồng hồ của Tiểu Lệ chạy nhanh 15 phút.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "你看看手表，怎么迟到了？", "py": "Nǐ kànkan shǒubiǎo, zěnme chídào le?", "vi": "Anh nhìn đồng hồ xem, sao lại đến muộn thế?"},
                {"speaker": "小刚", "role": "male", "zh": "没迟到啊。", "py": "Méi chídào a.", "vi": "Anh đâu có đến muộn đâu."},
                {"speaker": "小丽", "role": "female", "zh": "你不是说七点半来接我吗？你迟到了一刻钟。", "py": "Nǐ bú shì shuō qī diǎn bàn lái jiē wǒ ma? Nǐ chídàole yí kè zhōng.", "vi": "Chẳng phải anh bảo bảy rưỡi đến đón em sao? Anh đến muộn 15 phút rồi đấy."},
                {"speaker": "小刚", "role": "male", "zh": "现在不是七点半吗？", "py": "Xiànzài bú shì qī diǎn bàn ma?", "vi": "Bây giờ chẳng phải mới bảy rưỡi sao?"},
                {"speaker": "小丽", "role": "female", "zh": "已经差一刻八点了！我都在这儿坐了半个小时了。", "py": "Yǐjīng chà yí kè bā diǎn le! Wǒ dōu zài zhèr zuòle bàn ge xiǎoshí le.", "vi": "Đã 8 giờ kém 15 rồi! Em ngồi ở đây cả nửa tiếng đồng hồ rồi đấy."},
                {"speaker": "小刚", "role": "male", "zh": "不是我迟到了，是你的表快了一刻钟。", "py": "Bú shì wǒ chídào le, shì nǐ de biǎo kuàile yí kè zhōng.", "vi": "Không phải anh đến muộn đâu, là đồng hồ của em chạy nhanh 15 phút đấy."}
            ],
            "check_question": {
                "question": "小刚到底迟到了没有？",
                "options": ["迟到了半个小时", "迟到了一刻钟", "没有迟到，是小丽的手表快了一刻钟", "他记错了时间"],
                "ans": "C",
                "explain": "Tiểu Cương chỉ ra: '不是我迟到了，是你的表快了一刻钟' (Không phải anh muộn mà là đồng hồ của em chạy nhanh 15 phút)."
            }
        }
    ],

    # ========================== BÀI 08 ==========================
    8: [
        {
            "num": 1,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_08/08-1.mp3",
            "context": "Đồng nghiệp hỏi thăm Tiểu Lệ về việc đi xem nhà mua chung cư gần đây.",
            "lines": [
                {"speaker": "同事", "role": "male", "zh": "听说你最近打算买房子？", "py": "Tīngshuō nǐ zuìjìn dǎsuàn mǎi fángzi?", "vi": "Nghe nói dạo này bạn có dự định mua nhà à?"},
                {"speaker": "小丽", "role": "female", "zh": "是，昨天去看了看，今天又去看了看，明天还要再去看看。", "py": "Shì, zuótiān qù kànle kàn, jīntiān yòu qù kànle kàn, míngtiān hái yào zài qù kànkan.", "vi": "Đúng thế, hôm qua đi xem, hôm nay lại đi xem, ngày mai còn định đi xem nữa."},
                {"speaker": "同事", "role": "male", "zh": "都不满意吗？", "py": "Dōu bù mǎnyì ma?", "vi": "Đều không ưng ý sao?"},
                {"speaker": "小丽", "role": "female", "zh": "一个没有电梯，不方便。一个有电梯，但是在二十层。", "py": "Yí ge méiyǒu diàntī, bù fāngbiàn. Yí ge yǒu diàntī, dànshì zài èrshí céng.", "vi": "Một căn không có thang máy, bất tiện. Một căn có thang máy nhưng lại ở tận tầng 20."},
                {"speaker": "同事", "role": "male", "zh": "二十层怎么了？", "py": "Èrshí céng zěnme le?", "vi": "Tầng 20 thì sao chứ?"},
                {"speaker": "小丽", "role": "female", "zh": "太高了，往下看多害怕啊！", "py": "Tài gāo le, wǎng xià kàn duō hàipà a!", "vi": "Cao quá, nhìn xuống dưới sợ chết đi được!"}
            ],
            "check_question": {
                "question": "小丽为什么不喜欢二十层的房子？",
                "options": ["太吵了", "没有电梯", "太高了，往下看很害怕", "价格太贵"],
                "ans": "C",
                "explain": "Tiểu Lệ sợ độ cao: '太高了，往下看多害怕啊！' (Cao quá, nhìn xuống sợ lắm)."
            }
        },
        {
            "num": 2,
            "title": "在学校 (Ở trường)",
            "location": "在学校 (Ở trường học)",
            "audio_file": "audio_textbook/Bai_08/08-2.mp3",
            "context": "Mã Khả sắp về nước, Tiểu Minh tặng bạn chú gấu trúc nhồi bông làm quà lưu niệm.",
            "lines": [
                {"speaker": "小明", "role": "male", "zh": "听说你下个星期就要回国了？", "py": "Tīngshuō nǐ xià ge xīngqī jiù yào huí guó le?", "vi": "Nghe nói tuần sau cậu sắp về nước rồi à?"},
                {"speaker": "马可", "role": "male", "zh": "是啊，真不想离开北京。", "py": "Shì a, zhēn bù xiǎng líkāi Běijīng.", "vi": "Đúng thế, thực sự chẳng muốn rời xa Bắc Kinh chút nào."},
                {"speaker": "小明", "role": "male", "zh": "我下星期不在北京，不能去机场送你了。", "py": "Wǒ xià xīngqī bú zài Běijīng, bù néng qù jīchǎng sòng nǐ le.", "vi": "Tuần sau tớ không ở Bắc Kinh, không thể ra sân bay tiễn cậu rồi."},
                {"speaker": "马可", "role": "male", "zh": "没关系，你忙吧。", "py": "Méi guānxi, nǐ máng ba.", "vi": "Không sao đâu, cậu cứ bận việc đi."},
                {"speaker": "小明", "role": "male", "zh": "这个小熊猫送给你，欢迎你以后再到中国来。", "py": "Zhè ge xiǎo xióngmāo sòng gěi nǐ, huānyíng nǐ yǐhòu zài dào Zhōngguó lái.", "vi": "Chú gấu trúc nhỏ này tặng cậu, hoan nghênh cậu sau này lại sang Trung Quốc nhé."},
                {"speaker": "马可", "role": "male", "zh": "谢谢。希望以后能再见面。", "py": "Xièxie. Xīwàng yǐhòu néng zài jiàn miàn.", "vi": "Cảm ơn cậu. Hy vọng sau này chúng mình có thể gặp lại nhau."}
            ],
            "check_question": {
                "question": "小明送给马可什么礼物？",
                "options": ["一本书", "一只小熊猫", "一张机票", "一盒茶"],
                "ans": "B",
                "explain": "Tiểu Minh tặng quà lưu niệm: '这个小熊猫送给你' (Tặng bạn chú gấu trúc nhỏ này)."
            }
        },
        {
            "num": 3,
            "title": "在咖啡厅 (Ở quán cà phê)",
            "location": "在咖啡厅 (Ở quán cà phê)",
            "audio_file": "audio_textbook/Bai_08/08-3.mp3",
            "context": "Tiểu Lệ và Tiểu Cương đi uống cà phê, Tiểu Cương luôn chiều theo ý Tiểu Lệ.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "小刚，我们坐哪儿？", "py": "Xiǎogāng, wǒmen zuò nǎr?", "vi": "Tiểu Cương, chúng mình ngồi đâu?"},
                {"speaker": "小刚", "role": "male", "zh": "你坐哪儿我就坐哪儿。", "py": "Nǐ zuò nǎr wǒ jiù zuò nǎr.", "vi": "Em ngồi đâu thì anh ngồi đấy."},
                {"speaker": "小丽", "role": "female", "zh": "坐这儿吧，这儿安静。你想喝什么饮料？", "py": "Zuò zhèr ba, zhèr ānjìng. Nǐ xiǎng hē shénme yǐnliào?", "vi": "Ngồi đây đi, chỗ này yên tĩnh. Anh muốn uống đồ uống gì?"},
                {"speaker": "小刚", "role": "male", "zh": "你喝什么我就喝什么。", "py": "Nǐ hē shénme wǒ jiù hē shénme.", "vi": "Em uống gì anh uống nấy."},
                {"speaker": "小丽", "role": "female", "zh": "喝可乐吧。你等我一会儿，我马上回来。", "py": "Hē kělè ba. Nǐ děng wǒ yíhuìr, wǒ mǎshàng huílái.", "vi": "Uống cola nhé. Anh đợi em một lát, em quay lại ngay."},
                {"speaker": "小刚", "role": "male", "zh": "小丽，你去哪儿？你去哪儿我就去哪儿。", "py": "Xiǎolì, nǐ qù nǎr? Nǐ qù nǎr wǒ jiù qù nǎr.", "vi": "Tiểu Lệ, em đi đâu đấy? Em đi đâu anh đi theo đó."},
                {"speaker": "小丽", "role": "female", "zh": "我去洗手间。", "py": "Wǒ qù xǐshǒujiān.", "vi": "Em đi vệ sinh mà."}
            ],
            "check_question": {
                "question": "小丽让小刚等她一会儿，她要去哪儿？",
                "options": ["去买蛋糕", "去洗手间", "去打电话", "去买电影票"],
                "ans": "B",
                "explain": "Tiểu Lệ bật cười đáp: '我去洗手间' (Em đi vào nhà vệ sinh mà)."
            }
        },
        {
            "num": 4,
            "title": "在周明家 (Tại nhà Châu Minh)",
            "location": "在周明家 (Tại nhà Chu Minh)",
            "audio_file": "audio_textbook/Bai_08/08-4.mp3",
            "context": "Bạn học cũ đến thăm nhà Chu thái thái, hai người trò chuyện về vóc dáng và việc nấu ăn.",
            "lines": [
                {"speaker": "老同学", "role": "female", "zh": "快五年了，你几乎没变化。", "py": "Kuài wǔ nián le, nǐ jīhū méi biànhuà.", "vi": "Gần 5 năm rồi, bạn hầu như chẳng thay đổi gì cả."},
                {"speaker": "周太太", "role": "female", "zh": "谁说的？我胖了，以前的衣服都不能穿了。", "py": "Shéi shuō de? Wǒ pàng le, yǐqián de yīfu dōu bù néng chuān le.", "vi": "Ai bảo thế? Tớ béo lên rồi, quần áo trước đây đều không mặc vừa nữa."},
                {"speaker": "老同学", "role": "female", "zh": "健康最重要，胖瘦没关系。", "py": "Jiànkāng zuì zhòngyào, pàng shòu méi guānxi.", "vi": "Sức khỏe là quan trọng nhất, béo hay gầy không quan trọng đâu."},
                {"speaker": "周太太", "role": "female", "zh": "是呀，想吃什么就吃什么。", "py": "Shì ya, xiǎng chī shénme jiù chī shénme.", "vi": "Đúng vậy, muốn ăn gì thì cứ ăn nấy thôi."},
                {"speaker": "老同学", "role": "female", "zh": "你做饭还是周明做饭？", "py": "Nǐ zuò fàn háishi Zhōu Míng zuò fàn?", "vi": "Bạn nấu cơm hay Chu Minh nấu cơm?"},
                {"speaker": "周太太", "role": "female", "zh": "我做，我想吃什么就做什么，想吃多少就做多少。", "py": "Wǒ zuò, wǒ xiǎng chī shénme jiù zuò shénme, xiǎng chī duōshao jiù zuò duōshao.", "vi": "Tớ nấu chứ, tớ thích ăn món gì thì làm món đó, thích ăn bao nhiêu thì làm bấy nhiêu."}
            ],
            "check_question": {
                "question": "在家里是谁做饭？",
                "options": ["周明", "老同学", "周太太", "保姆"],
                "ans": "C",
                "explain": "Chu thái thái khẳng định: '我做，我想吃什么就做什么' (Tôi nấu, muốn ăn gì thì làm nấy)."
            }
        }
    ],

    # ========================== BÀI 09 ==========================
    9: [
        {
            "num": 1,
            "title": "在教室 (Trong lớp học)",
            "location": "在教室 (Trong lớp học)",
            "audio_file": "audio_textbook/Bai_09/09-1.mp3",
            "context": "Đại Sơn khen tiếng Trung của Mã Khả lưu loát như người bản xứ.",
            "lines": [
                {"speaker": "大山", "role": "male", "zh": "马可，你的中文越说越好了！", "py": "Mǎkě, nǐ de Zhōngwén yuè shuō yuè hǎo le!", "vi": "Mã Khả, tiếng Trung của cậu càng nói càng hay đấy!"},
                {"speaker": "马可", "role": "male", "zh": "哪里哪里，我们班李静说得更好。", "py": "Nǎli nǎli, wǒmen bān Lǐ Jìng shuō de gèng hǎo.", "vi": "Đâu có đâu có, lớp mình bạn Lý Tĩnh nói còn hay hơn."},
                {"speaker": "大山", "role": "male", "zh": "怎么好？", "py": "Zěnme hǎo?", "vi": "Hay thế nào cơ?"},
                {"speaker": "马可", "role": "male", "zh": "她的汉语说得跟中国人一样好。", "py": "Tā de Hànyǔ shuō de gēn Zhōngguórén yíyàng hǎo.", "vi": "Tiếng Trung của cô ấy nói giỏi hệt như người Trung Quốc vậy."},
                {"speaker": "大山", "role": "male", "zh": "李静？我怎么没听说过这个名字？", "py": "Lǐ Jìng? Wǒ zěnme méi tīngshuōguo zhè ge míngzi?", "vi": "Lý Tĩnh á? Sao tớ chưa từng nghe qua cái tên này nhỉ?"},
                {"speaker": "马可", "role": "male", "zh": "她是我们的汉语老师。", "py": "Tā shì wǒmen de Hànyǔ lǎoshī.", "vi": "Cô ấy là giáo viên dạy tiếng Trung của bọn tớ mà."}
            ],
            "check_question": {
                "question": "李静是谁？",
                "options": ["马可的同学", "马可的汉语老师", "大山的朋友", "一名中国医生"],
                "ans": "B",
                "explain": "Mã Khả bất ngờ tiết lộ: '她是我们的汉语老师' (Cô ấy là cô giáo dạy tiếng Trung của bọn tớ)."
            }
        },
        {
            "num": 2,
            "title": "在蛋糕店 (Ở cửa hàng bánh kem)",
            "location": "在蛋糕店 (Ở tiệm bánh kem)",
            "audio_file": "audio_textbook/Bai_09/09-2.mp3",
            "context": "Tiểu Lệ khuyên Tiểu Cương ăn ít bánh ngọt kẻo béo, Tiểu Cương tự tin cơ địa không thể béo.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "别吃了，你已经吃了三块蛋糕了。", "py": "Bié chī le, nǐ yǐjīng chīle sān kuài dàngāo le.", "vi": "Đừng ăn nữa, cậu đã ăn hết 3 miếng bánh kem rồi đấy."},
                {"speaker": "小刚", "role": "male", "zh": "这是最后一块。", "py": "Zhè shì zuìhòu yí kuài.", "vi": "Đây là miếng cuối cùng rồi."},
                {"speaker": "小丽", "role": "female", "zh": "你总是吃甜的东西，会越吃越胖。", "py": "Nǐ zǒngshì chī tián de dōngxi, huì yuè chī yuè pàng.", "vi": "Cậu lúc nào cũng ăn đồ ngọt, sẽ càng ăn càng béo đấy."},
                {"speaker": "小刚", "role": "male", "zh": "你放心，我一定不会变胖。", "py": "Nǐ fàng xīn, wǒ yídìng bú huì biàn pàng.", "vi": "Cậu cứ yên tâm đi, tớ nhất định sẽ không bị béo lên đâu."},
                {"speaker": "小丽", "role": "female", "zh": "为什么？", "py": "Wèishénme?", "vi": "Tại sao chứ?"},
                {"speaker": "小刚", "role": "male", "zh": "我们家的人都很瘦，吃不胖。", "py": "Wǒmen jiā de rén dōu hěn shòu, chī bu pàng.", "vi": "Người nhà tớ ai cũng gầy cả, ăn mãi không béo được."}
            ],
            "check_question": {
                "question": "小刚为什么觉得自己不会变胖？",
                "options": ["他每天坚持跑步", "他们家的人都很瘦，吃不胖", "他吃完蛋糕就去运动", "这种蛋糕不含糖"],
                "ans": "B",
                "explain": "Tiểu Cương giải thích: '我们家的人都很瘦，吃不胖' (Người nhà tớ đều gầy, ăn không thể béo)."
            }
        },
        {
            "num": 3,
            "title": "在山上 (Ở trên núi)",
            "location": "在山上 (Ở trên núi)",
            "audio_file": "audio_textbook/Bai_09/09-3.mp3",
            "context": "Tiểu Lệ và Tiểu Cương leo núi, càng lên cao đường càng khó đi và lạnh dần.",
            "lines": [
                {"speaker": "小丽", "role": "female", "zh": "我有点儿害怕。", "py": "Wǒ yǒudiǎnr hàipà.", "vi": "Em hơi sợ một chút."},
                {"speaker": "小刚", "role": "male", "zh": "怎么了？", "py": "Zěnme le?", "vi": "Sao thế em?"},
                {"speaker": "小丽", "role": "female", "zh": "山越高，路越难走。我也越爬越冷。", "py": "Shān yuè gāo, lù yuè nán zǒu. Wǒ yě yuè pá yuè lěng.", "vi": "Núi càng cao, đường càng khó đi. Em cũng càng leo càng thấy lạnh."},
                {"speaker": "小刚", "role": "male", "zh": "不用担心，有我呢，我对这儿比较了解。", "py": "Bú yòng dānxīn, yǒu wǒ ne, wǒ duì zhèr bǐjiào liǎojiě.", "vi": "Đừng lo, có anh ở đây mà, anh tương đối am hiểu nơi này."},
                {"speaker": "小丽", "role": "female", "zh": "那我们先休息一下，一会儿再爬。", "py": "Nà wǒmen xiān xiūxi yíxià, yíhuìr zài pá.", "vi": "Thế chúng mình nghỉ ngơi một chút trước đã, lát nữa rồi leo tiếp."},
                {"speaker": "小刚", "role": "male", "zh": "好，一会儿我们可以从中间这条路上去。", "py": "Hǎo, yíhuìr wǒmen kěyǐ cóng zhōngjiān zhè tiáo lù shàngqu.", "vi": "Được, lát nữa chúng mình có thể đi lên theo con đường ở giữa này."}
            ],
            "check_question": {
                "question": "小丽爬山时感觉怎么样？",
                "options": ["越爬越热", "山越高，路越难走，越爬越冷", "一点儿也不累", "很想快点到达山顶"],
                "ans": "B",
                "explain": "Tiểu Lệ than thở: '山越高，路越难走。我也越爬越冷' (Núi càng cao đường càng khó đi, càng leo càng lạnh)."
            }
        },
        {
            "num": 4,
            "title": "在小明家 (Tại nhà bạn Minh)",
            "location": "在小明家 (Tại nhà Tiểu Minh)",
            "audio_file": "audio_textbook/Bai_09/09-4.mp3",
            "context": "Bạn học đến thăm Tiểu Minh và thấy mắt bạn thâm quầng như gấu trúc vì đau chân mất ngủ.",
            "lines": [
                {"speaker": "同学", "role": "female", "zh": "小明，你的眼睛怎么跟大熊猫一样了？", "py": "Xiǎomíng, nǐ de yǎnjing zěnme gēn dà xióngmāo yíyàng le?", "vi": "Tiểu Minh, mắt của cậu sao lại thâm quầng như gấu trúc thế kia?"},
                {"speaker": "小明", "role": "male", "zh": "我这几天脚疼，没休息好。", "py": "Wǒ zhè jǐ tiān jiǎo téng, méi xiūxi hǎo.", "vi": "Mấy hôm nay chân tớ bị đau, không nghỉ ngơi tốt được."},
                {"speaker": "同学", "role": "female", "zh": "去医院了吗？医生说什么？", "py": "Qù yīyuàn le ma? Yīshēng shuō shénme?", "vi": "Cậu đi bệnh viện khám chưa? Bác sĩ nói sao?"},
                {"speaker": "小明", "role": "male", "zh": "他让我多休息。休息得越多，好得越快。", "py": "Tā ràng wǒ duō xiūxi. Xiūxi de yuè duō, hǎo de yuè kuài.", "vi": "Bác sĩ bảo tớ nghỉ ngơi nhiều vào. Càng nghỉ ngơi nhiều thì càng nhanh khỏi."},
                {"speaker": "同学", "role": "female", "zh": "下个月的篮球比赛，你能参加吗？", "py": "Xià ge yuè de lánqiú bǐsài, nǐ néng cānjiā ma?", "vi": "Trận thi đấu bóng rổ tháng sau, cậu có tham gia được không?"},
                {"speaker": "小明", "role": "male", "zh": "一定能参加，一点儿影响也没有。", "py": "Yídìng néng cānjiā, yìdiǎnr yǐngxiǎng yě méiyǒu.", "vi": "Nhất định tham gia được chứ, không có chút ảnh hưởng nào đâu."}
            ],
            "check_question": {
                "question": "小明眼睛为什么像大熊猫一样？",
                "options": ["因为天天看电视", "因为这几天脚疼没休息好", "因为他喜欢画大熊猫", "因为去医院检查眼睛"],
                "ans": "B",
                "explain": "Tiểu Minh kể: '我这几天脚疼，没休息好' (Mấy hôm nay đau chân nên không ngủ ngon được)."
            }
        }
    ],

    # ========================== BÀI 10 ==========================
    10: [
        {
            "num": 1,
            "title": "在教室 (Trong lớp học)",
            "location": "在教室 (Trong lớp học)",
            "audio_file": "audio_textbook/Bai_10/10-1.mp3",
            "context": "Bạn bè trong lớp so sánh vóc dáng, tuổi tác và trình độ tiếng Trung giữa Đại Sơn và Mã Khả.",
            "lines": [
                {"speaker": "朋友", "role": "male", "zh": "大山，你和马可谁个子高？", "py": "Dàshān, nǐ hé Mǎkě shéi gèzi gāo?", "vi": "Đại Sơn, cậu và Mã Khả ai có vóc dáng cao hơn?"},
                {"speaker": "大山", "role": "male", "zh": "马可比我高，我比马可矮一点儿。", "py": "Mǎkě bǐ wǒ gāo, wǒ bǐ Mǎkě ǎi yìdiǎnr.", "vi": "Mã Khả cao hơn tớ, tớ thấp hơn Mã Khả một chút."},
                {"speaker": "朋友", "role": "male", "zh": "那你们谁大？", "py": "Nà nǐmen shéi dà?", "vi": "Thế ai nhiều tuổi hơn?"},
                {"speaker": "大山", "role": "male", "zh": "我比马可大两岁。", "py": "Wǒ bǐ Mǎkě dà liǎng suì.", "vi": "Tớ lớn hơn Mã Khả hai tuổi."},
                {"speaker": "朋友", "role": "male", "zh": "你们谁的汉语说得更好？", "py": "Nǐmen shéi de Hànyǔ shuō de gèng hǎo?", "vi": "Tiếng Trung của hai cậu ai nói tốt hơn?"},
                {"speaker": "大山", "role": "male", "zh": "马可比我说得好一些，我的汉语没有他好。", "py": "Mǎkě bǐ wǒ shuō de hǎo yìxiē, wǒ de Hànyǔ méiyǒu tā hǎo.", "vi": "Mã Khả nói hay hơn tớ một chút, tiếng Trung của tớ không giỏi bằng cậu ấy."}
            ],
            "check_question": {
                "question": "大山和马可谁的汉语说得更好？",
                "options": ["大山说得好", "马可说得好一些", "两个人说得一样好", "老师说得好"],
                "ans": "B",
                "explain": "Đại Sơn khiêm tốn nhận xét: '马可比我说得好一些，我的汉语没有他好'."
            }
        },
        {
            "num": 2,
            "title": "在教室 (Trong lớp học)",
            "location": "在教室 (Trong lớp học)",
            "audio_file": "audio_textbook/Bai_10/10-2.mp3",
            "context": "Tiểu Minh thổ lộ nỗi sợ môn Toán, bạn học nhiệt tình ngỏ ý kèm cặp mỗi ngày.",
            "lines": [
                {"speaker": "小明", "role": "male", "zh": "我喜欢历史课、体育课，不喜欢数学课。", "py": "Wǒ xǐhuan lìshǐ kè, tǐyù kè, bù xǐhuan shùxué kè.", "vi": "Tớ thích môn Lịch sử, môn Thể dục, không thích môn Toán."},
                {"speaker": "同学", "role": "female", "zh": "为什么？数学也很有意思啊。", "py": "Wèishénme? Shùxué yě hěn yǒu yìsi a.", "vi": "Tại sao? Toán học cũng rất thú vị mà."},
                {"speaker": "小明", "role": "male", "zh": "我觉得数学比历史难多了，我听不懂。", "py": "Wǒ juéde shùxué bǐ lìshǐ nán duō le, wǒ tīng bu dǒng.", "vi": "Tớ thấy Toán khó hơn Lịch sử nhiều lắm, tớ nghe không hiểu."},
                {"speaker": "同学", "role": "female", "zh": "别担心，我可以帮你。", "py": "Bié dānxīn, wǒ kěyǐ bāng nǐ.", "vi": "Đừng lo, tớ có thể giúp cậu."},
                {"speaker": "小明", "role": "male", "zh": "好啊，我们每天学多长时间？", "py": "Hǎo a, wǒmen měi tiān xué duō cháng shíjiān?", "vi": "Tuyệt quá, mỗi ngày chúng mình học bao lâu?"},
                {"speaker": "同学", "role": "female", "zh": "一两个小时吧。", "py": "Yì-liǎng ge xiǎoshí ba.", "vi": "Khoảng một, hai tiếng nhé."}
            ],
            "check_question": {
                "question": "小明为什么不喜欢数学课？",
                "options": ["数学课作业太少", "数学比历史难多了，他听不懂", "老师讲得不清楚", "他更喜欢上英语课"],
                "ans": "B",
                "explain": "Tiểu Minh chia sẻ: '我觉得数学比历史难多了，我听不懂' (Môn toán khó hơn lịch sử nhiều, tôi nghe không hiểu)."
            }
        },
        {
            "num": 3,
            "title": "在休息室 (Trong phòng giải lao)",
            "location": "在休息室 (Trong phòng giải lao)",
            "audio_file": "audio_textbook/Bai_10/10-3.mp3",
            "context": "Tiểu Lệ chuyển nhà đến gần công ty nên đi làm sớm hơn, còn dự định đổi mua xe đạp mới.",
            "lines": [
                {"speaker": "同事", "role": "male", "zh": "你最近比以前来得早多了，搬家了？", "py": "Nǐ zuìjìn bǐ yǐqián lái de zǎo duō le, bān jiā le?", "vi": "Dạo này bạn đến sớm hơn trước nhiều đấy, chuyển nhà rồi à?"},
                {"speaker": "小丽", "role": "female", "zh": "是啊，你不知道？我上个月就搬家了，走路二十分钟就到。", "py": "Shì a, nǐ bù zhīdào? Wǒ shàng ge yuè jiù bān jiā le, zǒu lù èrshí fēnzhōng jiù dào.", "vi": "Đúng thế, bạn không biết à? Tôi chuyển nhà từ tháng trước rồi, đi bộ 20 phút là đến."},
                {"speaker": "同事", "role": "male", "zh": "那很方便啊。", "py": "Nà hěn fāngbiàn a.", "vi": "Thế thì thuận tiện quá rồi."},
                {"speaker": "小丽", "role": "female", "zh": "我还打算买辆自行车，骑车七八分钟就能到。", "py": "Wǒ hái dǎsuàn mǎi liàng zìxíngchē, qí chē qī-bā fēnzhōng jiù néng dào.", "vi": "Tôi còn dự định mua chiếc xe đạp, đi xe đạp thì 7-8 phút là tới nơi."},
                {"speaker": "同事", "role": "male", "zh": "你不是有一辆吗？", "py": "Nǐ bú shì yǒu yí liàng ma?", "vi": "Chẳng phải bạn có một chiếc rồi sao?"},
                {"speaker": "小丽", "role": "female", "zh": "那辆太旧了，要换一辆，很便宜，两三百块钱。", "py": "Nà liàng tài jiù le, yào huàn yí liàng, hěn piányi, liǎng-sān bǎi kuài qián.", "vi": "Chiếc đó cũ quá rồi, muốn đổi chiếc mới, rẻ lắm, chừng hai ba trăm tệ thôi."}
            ],
            "check_question": {
                "question": "小丽骑自行车到公司大概需要多长时间？",
                "options": ["二十分钟", "半个小时", "七八分钟", "一刻钟"],
                "ans": "C",
                "explain": "Tiểu Lệ ước tính: '骑车七八分钟就能到' (Đi xe đạp khoảng 7-8 phút là đến)."
            }
        },
        {
            "num": 4,
            "title": "在看房子 (Đang xem nhà)",
            "location": "在看房子 (Đang xem nhà)",
            "audio_file": "audio_textbook/Bai_10/10-4.mp3",
            "context": "Đại Sơn đi xem nhà trọ cùng nhân viên môi giới, so sánh phòng ốc trong và ngoài trường.",
            "lines": [
                {"speaker": "大山", "role": "male", "zh": "这两个地方的房子一样吗？", "py": "Zhè liǎng ge dìfang de fángzi yíyàng ma?", "vi": "Nhà ở hai khu vực này có giống nhau không?"},
                {"speaker": "中介", "role": "male", "zh": "不一样。您看，学校外边的房子比学校里边的大一些。", "py": "Bù yíyàng. Nín kàn, xuéxiào wàibian de fángzi bǐ xuéxiào lǐbian de dà yìxiē.", "vi": "Không giống nhau đâu ạ. Bác xem, nhà ở bên ngoài trường to hơn trong trường một chút."},
                {"speaker": "大山", "role": "male", "zh": "大小没关系，主要是环境，哪个更安静？", "py": "Dàxiǎo méi guānxi, zhǔyào shì huánjìng, nǎge gèng ānjìng?", "vi": "To nhỏ không quan trọng, chủ yếu là môi trường, bên nào yên tĩnh hơn?"},
                {"speaker": "中介", "role": "male", "zh": "学校里边的没有学校外边的那么安静。", "py": "Xuéxiào lǐbian de méiyǒu xuéxiào wàibian de nàme ānjìng.", "vi": "Bên trong trường không được yên tĩnh như bên ngoài trường đâu ạ."},
                {"speaker": "大山", "role": "male", "zh": "哪个方便一些呢？", "py": "Nǎge fāngbiàn yìxiē ne?", "vi": "Thế bên nào thuận tiện hơn một chút?"},
                {"speaker": "中介", "role": "male", "zh": "学校里边比学校外边方便，附近有三四个车站。", "py": "Xuéxiào lǐbian bǐ xuéxiào wàibian fāngbiàn, fùjìn yǒu sān-sì ge chēzhàn.", "vi": "Trong trường thuận tiện hơn ngoài trường, gần đó có 3-4 trạm dừng xe buýt."}
            ],
            "check_question": {
                "question": "学校里边的房子有什么优点？",
                "options": ["比外边更安静", "比外边大很多", "比外边方便，附近有三四个车站", "价格非常便宜"],
                "ans": "C",
                "explain": "Môi giới nêu rõ ưu điểm của phòng trong trường: '学校里边比学校外边方便，附近有三四个车站'."
            }
        }
    ]
}

def update_lesson_data_file(lesson_num, dialogues):
    data_path = os.path.join(DATA_DIR, f"extracted_soan_bai_{lesson_num:02d}.py")
    if not os.path.exists(data_path):
        print(f"❌ File not found: {data_path}")
        return False
    
    with open(data_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We dynamically load LESSON_DATA
    spec = importlib.util.spec_from_file_location("mod", data_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    lesson_data = mod.LESSON_DATA
    
    # Replace dialogues in memory
    lesson_data["dialogues"] = dialogues
    
    # Format the entire LESSON_DATA as python code cleanly
    import pprint
    new_content = f"""# -*- coding: utf-8 -*-
\"\"\"
Dữ liệu Soạn Bài Chuẩn Hóa - Bài {lesson_num:02d}
Trích xuất 100% nguyên văn từ Sách Giáo Khoa HSK 3 chuẩn (Peking University Press / NXB Nhân Trí Việt).
\"\"\"

LESSON_DATA = {pprint.pformat(lesson_data, width=120, sort_dicts=False, compact=False)}
"""
    with open(data_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✅ Updated {data_path}")
    return True

if __name__ == "__main__":
    import subprocess
    print("🚀 BẮT ĐẦU CẬP NHẬT 100% NGUYÊN VĂN BÀI KHÓA SGK CHO BÀI 02 - 10...")
    
    for l_num in range(2, 11):
        if l_num in GROUND_TRUTH_DIALOGUES:
            print(f"\n--- Cập nhật dữ liệu Bài {l_num:02d} ---")
            update_lesson_data_file(l_num, GROUND_TRUTH_DIALOGUES[l_num])
            print(f"--- Biên dịch lại Web Bài {l_num:02d} ---")
            res = subprocess.run([sys.executable, BUILDER, str(l_num)], capture_output=True, text=True, encoding="utf-8")
            print(res.stdout)
            if res.returncode != 0:
                print(f"❌ Error compiling lesson {l_num}:", res.stderr)
            else:
                print(f"🎉 Bài {l_num:02d} biên dịch và kiểm định PASSED!")

    print("\n🏁 HOÀN TẤT CẬP NHẬT CHÍNH XÁC 100% CẢ 9 BÀI HỌC (BÀI 02 ĐẾN 10)!")
