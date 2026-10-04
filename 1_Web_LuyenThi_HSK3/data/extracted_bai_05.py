# -*- coding: utf-8 -*-
"""
Dữ liệu chuẩn bị Bài 05: 我最近越来越胖了。
Sẵn sàng đưa vào template_master.html
"""

LESSON_DATA = {
    "lesson_info": {
        "id": 5,
        "title_zh": "我最近越来越胖了。",
        "title_py": "Wǒ zuìjìn yuè lái yuè pàng le.",
        "title_vi": "Dạo này em ngày càng béo ra.",
        "audio_file": "audio.mp3"
    },
    
    "audio_jump": [
        {"time": 0, "label": "▶ 00:00 Mở đầu"},
        {"time": 40, "label": "▶ 00:40 Phần 1 (1-5)"},
        {"time": 180, "label": "▶ 03:00 Phần 2 (6-10)"},
        {"time": 400, "label": "▶ 06:40 Phần 3 (11-15)"},
        {"time": 660, "label": "▶ 11:00 Phần 4 (16-20)"}
    ],

    "tab1_listening": {
        "part1_pictures": [
            {"id": "A", "file": "pic_A.png", "label": "Hình A: Bác sĩ khám bệnh (看病 / 医生)"},
            {"id": "B", "file": "pic_B.png", "label": "Hình B: Người ngồi xe lăn nói chuyện (坐轮椅 / 照顾)"},
            {"id": "C", "file": "pic_C.png", "label": "Hình C: Những bông hoa nở (花)"},
            {"id": "D", "file": "pic_D.png", "label": "Hình D (Ví dụ): Gọi điện thoại (打电话)"},
            {"id": "E", "file": "pic_E.png", "label": "Hình E: Thử và mua quần áo (买衣服 / 裙子)"},
            {"id": "F", "file": "pic_F.png", "label": "Hình F: Cả nhà dạo chơi trên bãi cỏ (在草地上 / 运动)"}
        ],
        "questions_1_to_5": [
            {
                "num": 1,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "树和草都绿了，天气真好，在草地上坐坐。", "py": "Shù hé cǎo dōu lǜ le, tiānqì zhēn hǎo, zài cǎodì shang zuòzuo.", "vi": "Cây và cỏ đều xanh rồi, thời tiết thật đẹp, ra bãi cỏ ngồi chút đi."}
                ],
                "ans": "F",
                "explain": "Đáp án đúng là <strong>F</strong>: Nhắc trực tiếp đến '树和草都绿了' (cây cỏ đều xanh) và '在草地上坐坐' (ngồi trên bãi cỏ)."
            },
            {
                "num": 2,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "这条裤子怎么样？", "py": "Zhè tiáo kùzi zěnmeyàng?", "vi": "Chiếc quần này thế nào?"},
                    {"role": "male", "speaker": "男", "zh": "你已经有那么多裤子了，买条裙子吧。", "py": "Nǐ yǐjīng yǒu nàme duō kùzi le, mǎi tiáo qúnzi ba.", "vi": "Em đã có nhiều quần thế rồi, mua chiếc váy đi."}
                ],
                "ans": "E",
                "explain": "Đáp án đúng là <strong>E</strong>: Đối thoại mua quần áo và khuyên '买条裙子吧' (mua váy đi)."
            },
            {
                "num": 3,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你要做什么？我来帮你吧。", "py": "Nǐ yào zuò shénme? Wǒ lái bāng nǐ ba.", "vi": "Bà muốn làm gì? Để cháu giúp bà nhé."},
                    {"role": "female", "speaker": "女", "zh": "不用帮，我一个人可以，谢谢你。", "py": "Bú yòng bāng, wǒ yí ge rén kěyǐ, xièxie nǐ.", "vi": "Không cần giúp đâu, một mình bà được rồi, cảm ơn cháu."}
                ],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Cảnh chăm sóc, đề nghị giúp đỡ người già ngồi xe lăn."
            },
            {
                "num": 4,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "春天到了，花儿都开了。", "py": "Chūntiān dào le, huār dōu kāi le.", "vi": "Mùa xuân đến rồi, hoa đều nở rộ rồi."},
                    {"role": "female", "speaker": "女", "zh": "是啊，你看它们开得多好。", "py": "Shì a, nǐ kàn tāmen kāi de duō hǎo.", "vi": "Đúng vậy, anh nhìn xem chúng nở đẹp biết bao."}
                ],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Nhắc đến mùa xuân và '花儿都开了' (hoa nở)."
            },
            {
                "num": 5,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "医生，我怎么了？", "py": "Yīshēng, wǒ zěnme le?", "vi": "Bác sĩ ơi, tôi bị làm sao thế?"},
                    {"role": "male", "speaker": "男", "zh": "你有点儿感冒，我给你开点儿药。", "py": "Nǐ yǒudiǎnr gǎnmào, wǒ gěi nǐ kāi diǎnr yào.", "vi": "Chị bị cảm một chút, tôi kê cho chị ít thuốc nhé."}
                ],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Bác sĩ khám bệnh kê thuốc ('医生', '有点儿感冒', '开点儿药')."
            }
        ],

        "questions_6_to_10": [
            {
                "num": 6,
                "passage": {"zh": "最近天气越来越冷，还总是下雨。", "py": "Zuìjìn tiānqì yuè lái yuè lěng, hái zǒngshì xià yǔ.", "vi": "Dạo này thời tiết ngày càng lạnh, lại còn luôn mưa nữa."},
                "statement": {"zh": "这几天的天气不太好。", "py": "Zhè jǐ tiān de tiānqì bú tài hǎo.", "vi": "Thời tiết mấy hôm nay không tốt lắm."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: Vừa lạnh vừa mưa suốt chứng tỏ thời tiết không tốt."
            },
            {
                "num": 7,
                "passage": {"zh": "我感冒好了，明天你不用来照顾我了。", "py": "Wǒ gǎnmào hǎo le, míngtiān nǐ bú yòng lái zhàogù wǒ le.", "vi": "Tôi khỏi cảm rồi, ngày mai bạn không cần đến chăm sóc tôi nữa đâu."},
                "statement": {"zh": "现在他的病好了。", "py": "Xiànzài tā de bìng hǎo le.", "vi": "Bây giờ bệnh của anh ấy đã khỏi rồi."},
                "ans": "√",
                "explain": "Đáp án đúng là <strong>Đúng (√)</strong>: '我感冒好了' nghĩa là bệnh đã khỏi."
            },
            {
                "num": 8,
                "passage": {"zh": "小方最近越来越胖，去年买的裙子都不能穿了。", "py": "Xiǎofāng zuìjìn yuè lái yuè pàng, qùnián mǎi de qúnzi dōu bù néng chuān le.", "vi": "Tiểu Phương dạo này ngày càng béo ra, váy mua năm ngoái đều không mặc được nữa."},
                "statement": {"zh": "小方现在比去年瘦。", "py": "Xiǎofāng xiànzài bǐ qùnián shòu.", "vi": "Tiểu Phương bây giờ gầy hơn năm ngoái."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Tiểu Phương ngày càng béo (越来越胖), chứ không phải gầy hơn."
            },
            {
                "num": 9,
                "passage": {"zh": "我儿子最近瘦了，工作太忙，没时间吃饭。", "py": "Wǒ érzi zuìjìn shòu le, gōngzuò tài máng, méi shíjiān chī fàn.", "vi": "Con trai tôi dạo này gầy đi, công việc bận quá, không có thời gian ăn cơm."},
                "statement": {"zh": "儿子不想吃饭，所以瘦了。", "py": "Érzi bù xiǎng chī fàn, suǒyǐ shòu le.", "vi": "Con trai không muốn ăn cơm nên bị gầy đi."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Gầy vì bận không có thời gian ăn (没时间吃饭), chứ không phải vì 'không muốn ăn' (不想吃饭)."
            },
            {
                "num": 10,
                "passage": {"zh": "天气越来越热，大家穿得越来越少。", "py": "Tiānqì yuè lái yuè rè, dàjiā chuān de yuè lái yuè shǎo.", "vi": "Thời tiết ngày càng nóng, mọi người mặc ngày càng ít."},
                "statement": {"zh": "冬天快到了。", "py": "Dōngtiān kuài dào le.", "vi": "Mùa đông sắp đến rồi."},
                "ans": "×",
                "explain": "Đáp án đúng là <strong>Sai (×)</strong>: Trời ngày càng nóng và mặc đồ mỏng chứng tỏ mùa hè sắp tới, không phải mùa đông."
            }
        ],

        "questions_11_to_15": [
            {
                "num": 11,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "医生，我的病用吃药吗？", "py": "Yīshēng, wǒ de bìng yòng chī yào ma?", "vi": "Bác sĩ ơi, bệnh của tôi có cần uống thuốc không?"},
                    {"role": "male", "speaker": "男", "zh": "不用吃药，回家多喝些水，多吃些水果。", "py": "Bú yòng chī yào, huí jiā duō hē xiē shuǐ, duō chī xiē shuǐguǒ.", "vi": "Không cần uống thuốc, về nhà uống nhiều nước vào, ăn nhiều hoa quả nhé."}
                ],
                "question": {"zh": "问：男的让女的做什么？", "py": "Wèn: Nán de ràng nǚ de zuò shénme?", "vi": "Hỏi: Người nam bảo người nữ làm gì?"},
                "options": ["吃药", "多喝水", "少吃水果"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Bác sĩ khuyên '多喝些水' (uống nhiều nước)."
            },
            {
                "num": 12,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "听说你最近不舒服，好些了吗？", "py": "Tīngshuō nǐ zuìjìn bù shūfu, hǎoxiē le ma?", "vi": "Nghe nói dạo này bạn không khỏe, đã đỡ chút nào chưa?"},
                    {"role": "female", "speaker": "女", "zh": "昨天发烧，头也越来越疼。", "py": "Zuótiān fāshāo, tóu yě yuè lái yuè téng.", "vi": "Hôm qua bị sốt, đầu cũng ngày càng đau."}
                ],
                "question": {"zh": "问：女的现在怎么样了？", "py": "Wèn: Nǚ de xiànzài zěnmeyàng le?", "vi": "Hỏi: Người nữ bây giờ thế nào rồi?"},
                "options": ["越来越好", "不发烧了", "还在生病"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Đầu ngày càng đau và sốt, chứng tỏ vẫn đang bị ốm (还在生病)."
            },
            {
                "num": 13,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "上次我为你介绍的那个女朋友怎么样？", "py": "Shàng cì wǒ wèi nǐ jièshào de nà ge nǚpéngyou zěnmeyàng?", "vi": "Bạn gái lần trước tôi giới thiệu cho bạn thế nào rồi?"},
                    {"role": "male", "speaker": "男", "zh": "人很不错，又聪明又漂亮，谢谢你。", "py": "Rén hěn búcuò, yòu cōngmíng yòu piàoliang, xièxie nǐ.", "vi": "Người rất tuyệt, vừa thông minh lại vừa xinh đẹp, cảm ơn bạn nhé."}
                ],
                "question": {"zh": "问：男的为什么说谢谢？", "py": "Wèn: Nán de wèishénme shuō xièxie?", "vi": "Hỏi: Vì sao người nam lại nói lời cảm ơn?"},
                "options": ["女的很聪明", "女的很不错", "女的给他介绍的女朋友很好"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Vì bạn gái được giới thiệu rất tốt nên nam cảm ơn người mai mối."
            },
            {
                "num": 14,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "我觉得汉语越来越难了。", "py": "Wǒ juéde Hànyǔ yuè lái yuè nán le.", "vi": "Tôi thấy tiếng Hán ngày càng khó."},
                    {"role": "female", "speaker": "女", "zh": "是吗？我怎么觉得越来越容易，也越来越有意思呀。", "py": "Shì ma? Wǒ zěnme juéde yuè lái yuè róngyì, yě yuè lái yuè yǒu yìsi ya.", "vi": "Thế à? Sao tôi lại thấy ngày càng dễ và ngày càng thú vị nhỉ."}
                ],
                "question": {"zh": "问：女的觉得汉语怎么样？", "py": "Wèn: Nǚ de juéde Hànyǔ zěnmeyàng?", "vi": "Hỏi: Người nữ cảm thấy tiếng Hán thế nào?"},
                "options": ["越来越不容易", "越来越容易", "越来越没意思"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Người nữ nói '越来越容易' (ngày càng dễ)."
            },
            {
                "num": 15,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "你不是发烧了吗？怎么还来上班？", "py": "Nǐ bú shì fāshāo le ma? Zěnme hái lái shàngbān?", "vi": "Chẳng phải bạn bị sốt sao? Sao vẫn đi làm thế này?"},
                    {"role": "male", "speaker": "男", "zh": "我吃了药，好些了。", "py": "Wǒ chī le yào, hǎoxiē le.", "vi": "Tôi uống thuốc rồi, đỡ hơn nhiều rồi."}
                ],
                "question": {"zh": "问：男的现在怎么样了？", "py": "Wèn: Nán de xiànzài zěnmeyàng le?", "vi": "Hỏi: Người nam bây giờ thế nào?"},
                "options": ["越来越好", "没来上班", "不用吃药了"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Đã uống thuốc và đỡ hơn, bệnh đang tiến triển tốt lên (越来越好)."
            }
        ],

        "questions_16_to_20": [
            {
                "num": 16,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "我喜欢三月，因为天气不那么冷了。", "py": "Wǒ xǐhuan sān yuè, yīnwèi tiānqì bú nàme lěng le.", "vi": "Tôi thích tháng ba, vì thời tiết không còn quá lạnh nữa."},
                    {"role": "male", "speaker": "男", "zh": "我喜欢五月，草和树都绿了，花也开了。", "py": "Wǒ xǐhuan wǔ yuè, cǎo hé shù dōu lǜ le, huā yě kāi le.", "vi": "Tôi thích tháng năm, cỏ cây đều xanh tươi, hoa cũng nở rộ."},
                    {"role": "female", "speaker": "女", "zh": "我也喜欢六月，大家不用穿冬天的衣服了。", "py": "Wǒ yě xǐhuan liù yuè, dàjiā bú yòng chuān dōngtiān de yīfu le.", "vi": "Tôi cũng thích tháng sáu, mọi người không cần mặc quần áo mùa đông nữa."},
                    {"role": "male", "speaker": "男", "zh": "我喜欢一月、二月、七月和八月，因为不用去上课了。", "py": "Wǒ xǐhuan yī yuè, èr yuè, qī yuè hé bā yuè, yīnwèi bú yòng qù shàngkè le.", "vi": "Tôi thích tháng một, tháng hai, tháng bảy và tháng tám, vì không cần phải đi học."}
                ],
                "question": {"zh": "问：男的为什么喜欢七月和八月？", "py": "Wèn: Nán de wèishénme xǐhuan qī yuè hé bā yuè?", "vi": "Hỏi: Vì sao người nam thích tháng 7 và tháng 8?"},
                "options": ["天气不那么冷了", "草和树都绿了", "没有课了"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Vì nghỉ hè không phải đến lớp ('不用去上课了' = 没有课了)."
            },
            {
                "num": 17,
                "dialogue": [
                    {"role": "female", "speaker": "女", "zh": "现在天长了，这是什么意思？", "py": "Xiànzài tiān cháng le, zhè shì shénme yìsi?", "vi": "Bây giờ 'tiān cháng le', câu này có nghĩa là gì vậy?"},
                    {"role": "male", "speaker": "男", "zh": "天长了就是天黑得越来越晚。", "py": "Tiān cháng le jiù shì tiān hēi de yuè lái yuè wǎn.", "vi": "'Tiān cháng le' nghĩa là trời tối càng ngày càng muộn."},
                    {"role": "female", "speaker": "女", "zh": "我懂了，就是白天的时间越来越长了。", "py": "Wǒ dǒng le, jiù shì báitiān de shíjiān yuè lái yuè cháng le.", "vi": "Tôi hiểu rồi, tức là thời gian ban ngày ngày càng dài ra."},
                    {"role": "male", "speaker": "男", "zh": "对。", "py": "Duì.", "vi": "Đúng rồi."}
                ],
                "question": {"zh": "问：“天长了”是什么意思？", "py": "Wèn: “Tiān cháng le” shì shénme yìsi?", "vi": "Hỏi: 'Tiān cháng le' có ý nghĩa là gì?"},
                "options": ["天黑了", "白天没有时间", "天黑得晚了"],
                "ans": "C",
                "explain": "Đáp án đúng là <strong>C</strong>: Giải thích trực tiếp '天黑得越来越晚' (trời tối muộn hơn)."
            },
            {
                "num": 18,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "今天好些了吗？", "py": "Jīntiān hǎoxiē le ma?", "vi": "Hôm nay đã đỡ hơn chút nào chưa?"},
                    {"role": "female", "speaker": "女", "zh": "这几天一直吃药，现在好些了，腿也不疼了。", "py": "Zhè jǐ tiān yìzhí chī yào, xiànzài hǎoxiē le, tuǐ yě bù téng le.", "vi": "Mấy hôm nay uống thuốc suốt, giờ đỡ hơn rồi, chân cũng không đau nữa."},
                    {"role": "male", "speaker": "男", "zh": "那不用再吃药了。", "py": "Nà bú yòng zài chī yào le.", "vi": "Thế thì không cần uống thuốc nữa đâu."},
                    {"role": "female", "speaker": "女", "zh": "太好了，谢谢您！", "py": "Tài hǎo le, xièxie nín!", "vi": "Tốt quá rồi, cảm ơn bác sĩ!"}
                ],
                "question": {"zh": "问：这两个人可能是什么关系？", "py": "Wèn: Zhè liǎng ge rén kěnéng shì shénme guānxi?", "vi": "Hỏi: Hai người này có khả năng là mối quan hệ gì?"},
                "options": ["男女朋友", "医生和病人", "丈夫和妻子"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Hỏi thăm diễn biến đau chân, uống thuốc và xưng hô lịch sự là Bác sĩ và bệnh nhân."
            },
            {
                "num": 19,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "你看，天晴了，这么快就不下雨了，我们出去吧。", "py": "Nǐ kàn, tiān qíng le, zhème kuài jiù bú xià yǔ le, wǒmen chūqù ba.", "vi": "Em nhìn kìa, trời tạnh rồi, tạnh mưa nhanh thật, chúng mình ra ngoài đi."},
                    {"role": "female", "speaker": "女", "zh": "好啊，带孩子们去外边买些花回来。", "py": "Hǎo a, dài háizimen qù wàibian mǎi xiē huā huílái.", "vi": "Được thôi, dẫn mấy đứa nhỏ ra ngoài mua ít hoa về."},
                    {"role": "male", "speaker": "男", "zh": "好，我去叫他们。", "py": "Hǎo, wǒ qù jiào tāmen.", "vi": "Được, anh đi gọi chúng nó."}
                ],
                "question": {"zh": "问：他们要做什么？", "py": "Wèn: Tāmen yào zuò shénme?", "vi": "Hỏi: Họ chuẩn bị làm gì?"},
                "options": ["买花", "看花", "看雨"],
                "ans": "A",
                "explain": "Đáp án đúng là <strong>A</strong>: Người vợ nói '带孩子们去外边买些花回来' (dẫn các con ra ngoài mua hoa về)."
            },
            {
                "num": 20,
                "dialogue": [
                    {"role": "male", "speaker": "男", "zh": "我要买裤子了，这条裤子现在已经不能穿了。", "py": "Wǒ yào mǎi kùzi le, zhè tiáo kùzi xiànzài yǐjīng bù néng chuān le.", "vi": "Anh phải mua quần mới rồi, chiếc quần này giờ không mặc vừa nữa."},
                    {"role": "female", "speaker": "女", "zh": "你瘦了吗？", "py": "Nǐ shòu le ma?", "vi": "Anh gầy đi à?"},
                    {"role": "male", "speaker": "男", "zh": "什么呀，我要买条大一号的。", "py": "Shénme ya, wǒ yào mǎi tiáo dà yí hào de.", "vi": "Gầy đâu mà gầy, anh phải mua cái cỡ to hơn một số đấy."},
                    {"role": "female", "speaker": "女", "zh": "你现在吃得越来越多，也不运动，能不胖吗？", "py": "Nǐ xiànzài chī de yuè lái yuè duō, yě bú yùndòng, néng bú pàng ma?", "vi": "Giờ anh ăn ngày càng nhiều, lại chẳng chịu vận động, bảo sao không béo ra?"}
                ],
                "question": {"zh": "问：男的有什么问题？", "py": "Wèn: Nán de yǒu shénme wèntí?", "vi": "Hỏi: Người nam có vấn đề gì?"},
                "options": ["瘦了", "胖了", "吃得少了"],
                "ans": "B",
                "explain": "Đáp án đúng là <strong>B</strong>: Ăn nhiều không tập thể dục, quần chật phải mua cỡ to hơn là do bị béo lên (胖了)."
            }
        ]
    },

    "tab2_reading": {
        "part1": {
            "options": [
                {"id": "A", "zh": "要来客人了，我出去买点儿水果吧。", "py": "Yào lái kèrén le, wǒ chūqù mǎi diǎnr shuǐguǒ ba.", "vi": "Sắp có khách đến rồi, tôi ra ngoài mua ít hoa quả nhé."},
                {"id": "B", "zh": "当然是春天。", "py": "Dāngrán shì chūntiān.", "vi": "Tất nhiên là mùa xuân rồi."},
                {"id": "C", "zh": "你今天觉得怎么样？还发烧吗？", "py": "Nǐ jīntiān juéde zěnmeyàng? Hái fāshāo ma?", "vi": "Hôm nay bạn thấy thế nào? Còn sốt không?"},
                {"id": "D", "zh": "我们快回家去吧。", "py": "Wǒmen kuài huí jiā qù ba.", "vi": "Chúng mình mau về nhà thôi."},
                {"id": "E", "zh": "当然。我们先坐公共汽车，然后换地铁。", "py": "Dāngrán. Wǒmen xiān zuò gōnggòng qìchē, ránhòu huàn dìtiě.", "vi": "Đương nhiên rồi. Chúng ta trước tiên đi xe buýt, sau đó đổi sang tàu điện ngầm."},
                {"id": "F", "zh": "谢谢你照顾我，我的腿越来越好了。", "py": "Xièxie nǐ zhàogù wǒ, wǒ de tuǐ yuè lái yuè hǎo le.", "vi": "Cảm ơn bạn đã chăm sóc tôi, chân của tôi ngày càng đỡ hơn rồi."}
            ],
            "questions": [
                {"num": 21, "zh": "天越来越黑，快要下雨了。", "py": "Tiān yuè lái yuè hēi, kuàiyào xià yǔ le.", "vi": "Trời ngày càng tối sầm, sắp mưa rồi.", "ans": "D", "explain": "Trời sắp mưa nên phản ứng hợp lý là mau chóng về nhà (我们快回家去吧)."},
                {"num": 22, "zh": "你最喜欢什么季节？", "py": "Nǐ zuì xǐhuan shénme jìjié?", "vi": "Bạn thích mùa nào nhất?", "ans": "B", "explain": "Hỏi mùa yêu thích nhất trả lời là mùa xuân (当然是春天)."},
                {"num": 23, "zh": "我吃了药，也喝了很多水，现在不发烧了。", "py": "Wǒ chī le yào, yě hē le hěn duō shuǐ, xiànzài bù fāshāo le.", "vi": "Tôi đã uống thuốc, cũng đã uống rất nhiều nước, giờ không sốt nữa.", "ans": "C", "explain": "Trả lời về tình trạng sốt đáp lại câu hỏi còn sốt không (你今天觉得怎么样？还发烧吗？)."},
                {"num": 24, "zh": "不用去，家里还有一些苹果和西瓜。", "py": "Bú yòng qù, jiā li hái yǒu yìxiē píngguǒ hé xīguā.", "vi": "Không cần đi đâu, ở nhà vẫn còn ít táo và dưa hấu.", "ans": "A", "explain": "Khuyên không cần đi vì nhà còn trái cây đáp lại ý định ra ngoài mua trái cây (要来客人了，我出去买点儿水果吧)."},
                {"num": 25, "zh": "别这么客气。", "py": "Bié zhème kèqi.", "vi": "Đừng khách sáo thế.", "ans": "F", "explain": "'Đừng khách sáo' đáp lại lời cảm ơn chăm sóc (谢谢你照顾我，我的腿越来越好了)."}
            ]
        },

        "part2": {
            "vocab_bank": [
                {"id": "A", "zh": "照顾", "py": "zhàogù", "vi": "chăm sóc"},
                {"id": "B", "zh": "当然", "py": "dāngrán", "vi": "đương nhiên"},
                {"id": "C", "zh": "最近", "py": "zuìjìn", "vi": "dạo này"},
                {"id": "D", "zh": "裙子", "py": "qúnzi", "vi": "chiếc váy"},
                {"id": "E", "zh": "声音", "py": "shēngyīn", "vi": "giọng nói (Ví dụ)"},
                {"id": "F", "zh": "为", "py": "wèi", "vi": "vì, cho"}
            ],
            "questions": [
                {"num": 26, "prefix": "这是我（ ", "suffix": " ）你买的蛋糕，你看看，喜欢吗？", "py": "Zhè shì wǒ ( wèi ) nǐ mǎi de dàngāo, nǐ kànkan, xǐhuan ma?", "vi": "Đây là bánh kem tôi mua cho bạn, bạn xem thử xem, có thích không?", "ans": "F", "word": "为", "explain": "Cấu trúc giới từ '为 + tân ngữ + động từ': 为你买 (mua cho bạn)."},
                {"num": 27, "prefix": "下个星期我不在家，你能帮我（ ", "suffix": " ）一下我的小狗吗？", "py": "Xià ge xīngqī wǒ bú zài jiā, nǐ néng bāng wǒ ( zhàogù ) yíxià wǒ de xiǎogǒu ma?", "vi": "Tuần sau tôi không có ở nhà, bạn có thể giúp tôi chăm sóc chú cún một chút không?", "ans": "A", "word": "照顾", "explain": "Động từ chăm sóc thú cưng: 照顾一下小狗."},
                {"num": 28, "prefix": "这条（ ", "suffix": " ）是去年我生日的时候妈妈给我买的。", "py": "Zhè tiáo ( qúnzi ) shì qùnián wǒ shēngrì de shíhou māma gěi wǒ mǎi de.", "vi": "Chiếc váy này là mẹ mua cho tôi vào dịp sinh nhật năm ngoái.", "ans": "D", "word": "裙子", "explain": "Lượng từ '条' đi kèm với danh từ trang phục '裙子' (chiếc váy)."},
                {"num": 29, "prefix": "A: 你怎么瘦了？是不是（ ", "suffix": " ）工作太忙了？<br>B: 我一点儿也没瘦，很多人都说我胖了。", "py": "A: Nǐ zěnme shòu le? Shì bú shì ( zuìjìn ) gōngzuò tài máng le?<br>B: Wǒ yìdiǎnr yě méi shòu, hěn duō rén dōu shuō wǒ pàng le.", "vi": "A: Sao bạn gầy đi thế? Có phải dạo này công việc bận quá không?<br>B: Tôi chẳng gầy tí nào, nhiều người còn bảo tôi béo ra đấy.", "ans": "C", "word": "最近", "explain": "Từ chỉ thời gian '最近' (dạo này/gần đây)."},
                {"num": 30, "prefix": "A: 今天晚上你想不想跟我一起去看电影？<br>B: （ ", "suffix": " ）想去，我们什么时候走？", "py": "A: Jīntiān wǎnshang nǐ xiǎng bu xiǎng gēn wǒ yìqǐ qù kàn diànyǐng?<br>B: ( Dāngrán ) xiǎng qù, wǒmen shénme shíhou zǒu?", "vi": "A: Tối nay bạn có muốn đi xem phim cùng tôi không?<br>B: Đương nhiên muốn đi rồi, khi nào chúng ta xuất phát?", "ans": "B", "word": "当然", "explain": "Phó từ khẳng định '当然' (đương nhiên, tất nhiên)."}
            ]
        },

        "part3": [
            {
                "num": 31,
                "passage": {
                    "zh": "北京一年有四个季节，我最喜欢春天。北京的春天是绿色的，因为树绿了，草地也都绿了，天气不那么冷了，花也开了。这么漂亮的季节，你不喜欢吗？",
                    "py": "Běijīng yì nián yǒu sì ge jìjié, wǒ zuì xǐhuan chūntiān. Běijīng de chūntiān shì lǜsè de, yīnwèi shù lǜ le, cǎodì yě dōu lǜ le, tiānqì bú nàme lěng le, huā yě kāi le. Zhème piàoliang de jìjié, nǐ bù xǐhuan ma?",
                    "vi": "Bắc Kinh một năm có bốn mùa, tôi thích nhất mùa xuân. Mùa xuân Bắc Kinh mang màu xanh lá, bởi cây cối đã xanh, bãi cỏ cũng xanh rì, trời không còn lạnh như trước, hoa cũng đua nở. Mùa tươi đẹp thế này, bạn không thích sao?"
                },
                "question": {"zh": "★ 北京的春天：", "py": "★ Běijīng de chūntiān:", "vi": "★ Mùa xuân ở Bắc Kinh:"},
                "options": [
                    {"id": "A", "zh": "天气非常冷", "py": "tiānqì fēicháng lěng", "vi": "thời tiết rất lạnh"},
                    {"id": "B", "zh": "花还没开", "py": "huā hái méi kāi", "vi": "hoa vẫn chưa nở"},
                    {"id": "C", "zh": "树和草都绿了", "py": "shù hé cǎo dōu lǜ le", "vi": "cây và cỏ đều đã xanh tươi"}
                ],
                "ans": "C",
                "explain": "Đoạn văn viết: '因为树绿了，草地也都绿了' nên đáp án đúng là C."
            },
            {
                "num": 32,
                "passage": {
                    "zh": "现在的“小胖子”越来越多了，因为现在的孩子吃得越来越多，越来越不爱运动。吃饭的时候不爱吃菜，只爱吃肉，还喜欢吃甜的，这样当然会越来越胖了。",
                    "py": "Xiànzài de “xiǎopàngzi” yuè lái yuè duō le, yīnwèi xiànzài de háizi chī de yuè lái yuè duō, yuè lái yuè bú ài yùndòng. Chī fàn de shíhou bú ài chī cài, zhǐ ài chī ròu, hái xǐhuan chī tián de, zhèyàng dāngrán huì yuè lái yuè pàng le.",
                    "vi": "Hiện nay các 'bé béo phì' ngày càng nhiều, vì trẻ em ngày nay ăn ngày càng nhiều, ngày càng lười vận động. Khi ăn cơm thì không thích ăn rau, chỉ thích ăn thịt, lại còn thích ăn đồ ngọt, như thế đương nhiên sẽ ngày càng béo."
                },
                "question": {"zh": "★ “小胖子”们：", "py": "★ “Xiǎopàngzi” men:", "vi": "★ Những đứa trẻ béo phì:"},
                "options": [
                    {"id": "A", "zh": "爱吃菜", "py": "ài chī cài", "vi": "thích ăn rau"},
                    {"id": "B", "zh": "爱吃肉", "py": "ài chī ròu", "vi": "thích ăn thịt"},
                    {"id": "C", "zh": "爱运动", "py": "ài yùndòng", "vi": "thích vận động"}
                ],
                "ans": "B",
                "explain": "Đoạn văn viết rõ: '不爱吃菜，只爱吃肉' (không thích ăn rau, chỉ thích ăn thịt)."
            },
            {
                "num": 33,
                "passage": {
                    "zh": "中国人一年四季都喜欢喝茶。中国有很多种茶，有红茶，也有绿茶，还有花茶。茶是中国人非常爱喝的饮料。",
                    "py": "Zhōngguó rén yì nián sì jì dōu xǐhuan hē chá. Zhōngguó yǒu hěn duō zhǒng chá, yǒu hóngchá, yě yǒu lǜchá, hái yǒu huāchá. Chá shì Zhōngguó rén fēicháng ài hē de yǐnliào.",
                    "vi": "Người Trung Quốc quanh năm bốn mùa đều thích uống trà. Trung Quốc có rất nhiều loại trà, có hồng trà, trà xanh, lại có cả trà hoa. Trà là thức uống mà người Trung Quốc vô cùng yêu thích."
                },
                "question": {"zh": "★ 中国人觉得茶：", "py": "★ Zhōngguó rén juéde chá:", "vi": "★ Người Trung Quốc cảm thấy trà:"},
                "options": [
                    {"id": "A", "zh": "是红色的", "py": "shì hóngsè de", "vi": "có màu đỏ"},
                    {"id": "B", "zh": "很好喝", "py": "hěn hǎohē", "vi": "rất ngon"},
                    {"id": "C", "zh": "很贵", "py": "hěn guì", "vi": "rất đắt"}
                ],
                "ans": "B",
                "explain": "Người Trung Quốc quanh năm đều thích uống trà ('非常爱喝的饮料'), chứng tỏ họ thấy trà rất ngon (很好喝)."
            },
            {
                "num": 34,
                "passage": {
                    "zh": "很多女孩儿晚上不吃饭，只吃水果，白天吃得也很少。她们说这样可以瘦一点儿，可以穿漂亮的裙子。其实，不吃饭对身体不好。晚上可以少吃一点儿，但不能不吃，也不能吃得太晚。",
                    "py": "Hěn duō nǚháir wǎnshang bù chī fàn, zhǐ chī shuǐguǒ, báitiān chī de yě hěn shǎo. Tāmen shuō zhèyàng kěyǐ shòu yìdiǎnr, kěyǐ chuān piàoliang de qúnzi. Qíshí, bù chī fàn duì shēntǐ bù hǎo. Wǎnshang kěyǐ shǎo chī yìdiǎnr, dàn bù néng bù chī, yě bù néng chī de tài wǎn.",
                    "vi": "Nhiều cô gái buổi tối không ăn cơm, chỉ ăn trái cây, ban ngày ăn cũng rất ít. Họ nói làm thế có thể gầy đi một chút, mặc được váy đẹp. Thực ra, nhịn ăn không tốt cho cơ thể. Buổi tối có thể ăn ít đi một chút, nhưng không được không ăn, cũng không được ăn quá muộn."
                },
                "question": {"zh": "★ 根据这段话，可以知道：", "py": "★ Gēnjù zhè duàn huà, kěyǐ zhīdào:", "vi": "★ Căn cứ vào đoạn văn, có thể biết:"},
                "options": [
                    {"id": "A", "zh": "不吃饭对身体不好", "py": "bù chī fàn duì shēntǐ bù hǎo", "vi": "nhịn ăn không tốt cho cơ thể"},
                    {"id": "B", "zh": "晚上可以不吃饭", "py": "wǎnshang kěyǐ bù chī fàn", "vi": "buổi tối có thể không ăn"},
                    {"id": "C", "zh": "白天可以不吃饭", "py": "báitiān kěyǐ bù chī fàn", "vi": "ban ngày có thể không ăn"}
                ],
                "ans": "A",
                "explain": "Đoạn văn khẳng định trực tiếp: '其实，不吃饭对身体不好' (Thực ra, nhịn ăn không tốt cho cơ thể)."
            },
            {
                "num": 35,
                "passage": {
                    "zh": "你知道生病的时候怎么吃药吗？有人用茶水吃药，有人用热牛奶吃药。其实，吃药的时候用热水是最好的。药，你吃对了吗？",
                    "py": "Nǐ zhīdào shēngbìng de shíhou zěnme chī yào ma? Yǒu rén yòng cháshuǐ chī yào, yǒu rén yòng rè niúnǎi chī yào. Qíshí, chī yào de shíhou yòng rèshuǐ shì zuì hǎo de. Yào, nǐ chī duì le ma?",
                    "vi": "Bạn có biết khi bị ốm phải uống thuốc thế nào không? Có người uống thuốc bằng nước trà, có người lại uống bằng sữa nóng. Thực ra, khi uống thuốc dùng nước ấm là tốt nhất. Thuốc, bạn đã uống đúng cách chưa?"
                },
                "question": {"zh": "★ 吃药的时候要用：", "py": "★ Chī yào de shíhou yào yòng:", "vi": "★ Khi uống thuốc nên dùng:"},
                "options": [
                    {"id": "A", "zh": "热茶水", "py": "rè cháshuǐ", "vi": "nước trà nóng"},
                    {"id": "B", "zh": "热牛奶", "py": "rè niúnǎi", "vi": "sữa nóng"},
                    {"id": "C", "zh": "热水", "py": "rèshuǐ", "vi": "nước ấm/nóng"}
                ],
                "ans": "C",
                "explain": "Đoạn văn nêu rõ: '其实，吃药的时候用热水是最好的' (uống bằng nước ấm/nước sôi để nguội là tốt nhất)."
            }
        ]
    },

    "tab3_writing": {
        "part1": [
            {
                "num": 36,
                "chunks": ["外边的", "绿", "草", "都", "了"],
                "ans": "外边的草都绿了。",
                "py": "Wàibian de cǎo dōu lǜ le.",
                "vi": "Cỏ ở bên ngoài đều đã xanh rồi.",
                "grammar": "Chủ ngữ (外边的草) + Phó từ (都) + Tính từ (绿) + 了 (biến hóa)."
            },
            {
                "num": 37,
                "chunks": ["好", "现在", "我的病", "了"],
                "ans": "现在我的病好了。",
                "py": "Xiànzài wǒ de bìng hǎo le.",
                "vi": "Bây giờ bệnh của tôi đã khỏi rồi.",
                "grammar": "Trạng từ thời gian (现在) + Chủ ngữ (我的病) + Vị ngữ (好) + 了 (biến hóa)."
            },
            {
                "num": 38,
                "chunks": ["热", "越来越", "天气", "最近"],
                "ans": "最近天气越来越热。",
                "py": "Zuìjìn tiānqì yuè lái yuè rè.",
                "vi": "Dạo này thời tiết ngày càng nóng.",
                "grammar": "Thời gian (最近) + Chủ ngữ (天气) + 越来越 + Tính từ (热)."
            },
            {
                "num": 39,
                "chunks": ["越来越", "雨", "大", "下得"],
                "ans": "雨下得越来越大。",
                "py": "Yǔ xià de yuè lái yuè dà.",
                "vi": "Mưa rơi ngày càng to.",
                "grammar": "Cấu trúc bổ ngữ trạng thái: Động từ + 得 + 越来越 + Tính từ (雨下得越来越大)."
            },
            {
                "num": 40,
                "chunks": ["漂亮", "越来越", "现在", "我妹妹"],
                "ans": "现在我妹妹越来越漂亮。",
                "py": "Xiànzài wǒ mèimei yuè lái yuè piàoliang.",
                "vi": "Bây giờ em gái tôi ngày càng xinh đẹp.",
                "grammar": "Thời gian (现在) + Chủ ngữ (我妹妹) + 越来越 + Tính từ (漂亮)."
            }
        ],

        "part2": [
            {
                "num": 41,
                "sentence": "听说你（ fā ）烧了，我来看看你。",
                "pinyin": "fā",
                "ans": "发",
                "hanviet": "Phát",
                "compound": "发烧 (fāshāo): phát sốt, bị sốt",
                "vi": "Nghe nói bạn bị sốt rồi, tôi qua thăm bạn đây."
            },
            {
                "num": 42,
                "sentence": "今天是周末，不（ yòng ）去公司上班。",
                "pinyin": "yòng",
                "ans": "用",
                "hanviet": "Dụng",
                "compound": "不用 (bú yòng): không cần, không phải",
                "vi": "Hôm nay là cuối tuần, không cần phải đến công ty đi làm."
            },
            {
                "num": 43,
                "sentence": "你觉得哪个（ jì ）节去南方最好？",
                "pinyin": "jì",
                "ans": "季",
                "hanviet": "Quý",
                "compound": "季节 (jìjié): mùa, tiết trời",
                "vi": "Bạn thấy mùa nào đi miền Nam là tuyệt nhất?"
            },
            {
                "num": 44,
                "sentence": "大家都说北京的（ chūn ）天是最漂亮的。",
                "pinyin": "chūn",
                "ans": "春",
                "hanviet": "Xuân",
                "compound": "春天 (chūntiān): mùa xuân",
                "vi": "Mọi người đều nói mùa xuân ở Bắc Kinh là đẹp nhất."
            },
            {
                "num": 45,
                "sentence": "你说我今天穿裤子还是穿（ qún ）子？",
                "pinyin": "qún",
                "ans": "裙",
                "hanviet": "Quần",
                "compound": "裙子 (qúnzi): chiếc váy",
                "vi": "Cậu bảo hôm nay tớ nên mặc quần hay mặc váy?"
            }
        ]
    },

    "tab4_textbook": {
        "vocab": [
            {"id": 1, "zh": "发烧", "py": "fāshāo", "pos": "động từ", "vi": "phát sốt, bị sốt"},
            {"id": 2, "zh": "为", "py": "wèi", "pos": "giới từ", "vi": "vì, cho"},
            {"id": 3, "zh": "照顾", "py": "zhàogù", "pos": "động từ", "vi": "chăm sóc, săn sóc"},
            {"id": 4, "zh": "用", "py": "yòng", "pos": "động từ/phó từ", "vi": "dùng, cần phải"},
            {"id": 5, "zh": "感冒", "py": "gǎnmào", "pos": "động từ/danh từ", "vi": "bị cảm, cảm cúm"},
            {"id": 6, "zh": "季节", "py": "jìjié", "pos": "danh từ", "vi": "mùa trong năm"},
            {"id": 7, "zh": "当然", "py": "dāngrán", "pos": "phó từ", "vi": "đương nhiên, tất nhiên"},
            {"id": 8, "zh": "春(天)", "py": "chūn (tiān)", "pos": "danh từ", "vi": "mùa xuân"},
            {"id": 9, "zh": "草", "py": "cǎo", "pos": "danh từ", "vi": "cỏ"},
            {"id": 10, "zh": "夏(天)", "py": "xià (tiān)", "pos": "danh từ", "vi": "mùa hè"},
            {"id": 11, "zh": "裙子", "py": "qúnzi", "pos": "danh từ", "vi": "chiếc váy"},
            {"id": 12, "zh": "最近", "py": "zuìjìn", "pos": "danh từ", "vi": "dạo này, gần đây"},
            {"id": 13, "zh": "越", "py": "yuè", "pos": "phó từ", "vi": "càng (ngày càng)"}
        ],

        "grammar": [
            {
                "title": "1. Trợ từ ngữ khí “了” biểu thị sự thay đổi (变化)",
                "structure": "Câu trần thuật + 了",
                "explanation": "Trợ từ “了” đặt ở cuối câu biểu thị tình hình đã nảy sinh sự thay đổi hoặc xuất hiện trạng thái mới so với trước đây.",
                "examples": [
                    {"zh": "春天来了，草绿了。", "py": "Chūntiān lái le, cǎo lǜ le.", "vi": "Mùa xuân đến rồi, cỏ đã xanh rồi."},
                    {"zh": "我现在不想去了。", "py": "Wǒ xiànzài bù xiǎng qù le.", "vi": "Bây giờ tôi không muốn đi nữa rồi (trước đó muốn đi)."},
                    {"zh": "这条裙子现在不能穿了。", "py": "Zhè tiáo qúnzi xiànzài bù néng chuān le.", "vi": "Chiếc váy này bây giờ không mặc vừa nữa rồi."}
                ]
            },
            {
                "title": "2. Cấu trúc “越来越……” biểu thị mức độ tăng dần",
                "structure": "Chủ ngữ + 越来越 + Tính từ / Động từ tâm lý (+ 了)",
                "explanation": "Biểu thị mức độ của sự vật, hành động thay đổi sâu sắc hoặc tăng dần theo thời gian (ngày càng... hơn).",
                "examples": [
                    {"zh": "我最近越来越胖了。", "py": "Wǒ zuìjìn yuè lái yuè pàng le.", "vi": "Dạo này em ngày càng béo ra."},
                    {"zh": "天气越来越冷了。", "py": "Tiānqì yuè lái yuè lěng le.", "vi": "Thời tiết ngày càng lạnh hơn."},
                    {"zh": "汉语越来越有意思了。", "py": "Hànyǔ yuè lái yuè yǒu yìsi le.", "vi": "Tiếng Hán ngày càng thú vị hơn."}
                ]
            }
        ],

        "expansion_and_idiom": {
            "hanzi_knowledge": {
                "type": "会意字 (Chữ hội ý)",
                "characters": [
                    {"char": "明", "pinyin": "míng", "explain": "日 (mặt trời) + 月 (mặt trăng) ghép lại biểu thị ánh sáng rực rỡ, sáng sủa, rõ ràng."},
                    {"char": "休", "pinyin": "xiū", "explain": "亻 (người) tựa vào 木 (gốc cây) biểu thị sự nghỉ ngơi."},
                    {"char": "从", "pinyin": "cóng", "explain": "Hai người đi theo nhau (người trước người sau), nghĩa là đi theo, từ đâu đến."},
                    {"char": "看", "pinyin": "kàn", "explain": "手 (tay) che trên 目 (mắt) để nhìn xa, nghĩa là trông, nhìn, xem."}
                ]
            },
            "word_expansion": [
                {"word": "听说", "py": "tīngshuō", "meaning": "nghe nói (听: nghe + 说: nói)"},
                {"word": "有点儿", "py": "yǒudiǎnr", "meaning": "hơi hơi, một chút (有: có + 点儿: điểm/chút)"},
                {"word": "草地", "py": "cǎodì", "meaning": "bãi cỏ, thảm cỏ (草: cỏ + 地: đất, bãi)"}
            ],
            "proverb": {
                "zh": "药到病除",
                "py": "Yào dào bìng chú",
                "vi": "Thuốc uống vào hết bệnh ngay (Thuốc tới bệnh trừ). Ý chỉ phương thuốc hiệu nghiệm, bệnh tật tiêu tán tức thì."
            }
        },

        "polyphonic": [
            {
                "char": "发",
                "sounds": [
                    {"py": "fā", "meaning": "phát ra, bị (bệnh)", "example": "发烧 (fāshāo), 发现 (fāxiàn)"},
                    {"py": "fà", "meaning": "tóc", "example": "头发 (tóufa)"}
                ]
            },
            {
                "char": "为",
                "sounds": [
                    {"py": "wèi", "meaning": "vì, cho (giới từ chỉ mục đích/đối tượng)", "example": "为你 (wèi nǐ), 为什么 (wèishénme)"},
                    {"py": "wéi", "meaning": "làm, là (động từ)", "example": "作为 (zuòwéi), 成为 (chéngwéi)"}
                ]
            }
        ]
    },

    "quiz_data": {
        "1": {"ans": "F", "explain": "F: Nhắc trực tiếp đến '树和草都绿了' (cây cỏ đều xanh) và '在草地上坐坐' (ngồi trên bãi cỏ)."},
        "2": {"ans": "E", "explain": "E: Đối thoại mua quần áo và khuyên '买条裙子吧' (mua váy đi)."},
        "3": {"ans": "B", "explain": "B: Cảnh chăm sóc, đề nghị giúp đỡ người già ngồi xe lăn."},
        "4": {"ans": "C", "explain": "C: Nhắc đến mùa xuân và '花儿都开了' (hoa nở)."},
        "5": {"ans": "A", "explain": "A: Bác sĩ khám bệnh kê thuốc ('医生', '有点儿感冒', '开点儿药')."},
        "6": {"ans": "√", "explain": "Đúng (√): Vừa lạnh vừa mưa suốt chứng tỏ thời tiết không tốt."},
        "7": {"ans": "√", "explain": "Đúng (√): '我感冒好了' nghĩa là bệnh đã khỏi."},
        "8": {"ans": "×", "explain": "Sai (×): Tiểu Phương ngày càng béo (越来越胖), chứ không phải gầy hơn."},
        "9": {"ans": "×", "explain": "Sai (×): Gầy vì bận không có thời gian ăn (没时间吃饭), chứ không phải vì 'không muốn ăn'."},
        "10": {"ans": "×", "explain": "Sai (×): Trời ngày càng nóng và mặc đồ mỏng chứng tỏ mùa hè sắp tới, không phải mùa đông."},
        "11": {"ans": "B", "explain": "B: Bác sĩ khuyên '多喝些水' (uống nhiều nước)."},
        "12": {"ans": "C", "explain": "C: Đầu ngày càng đau và sốt, chứng tỏ vẫn đang bị ốm (还在生病)."},
        "13": {"ans": "C", "explain": "C: Vì bạn gái được giới thiệu rất tốt nên nam cảm ơn người mai mối."},
        "14": {"ans": "B", "explain": "B: Người nữ nói '越来越容易' (ngày càng dễ)."},
        "15": {"ans": "A", "explain": "A: Đã uống thuốc và đỡ hơn, bệnh đang tiến triển tốt lên (越来越好)."},
        "16": {"ans": "C", "explain": "C: Vì nghỉ hè không phải đến lớp ('不用去上课了' = 没有课了)."},
        "17": {"ans": "C", "explain": "C: Giải thích trực tiếp '天黑得越来越晚' (trời tối muộn hơn)."},
        "18": {"ans": "B", "explain": "B: Đoán quan hệ khám bệnh kê đơn và hỏi thăm tiến triển sức khỏe là Bác sĩ và bệnh nhân."},
        "19": {"ans": "A", "explain": "A: Người vợ nói '带孩子们去外边买些花回来' (dẫn các con ra ngoài mua hoa về)."},
        "20": {"ans": "B", "explain": "B: Ăn nhiều không tập thể dục, quần chật phải mua cỡ to hơn là do bị béo lên (胖了)."},
        "21": {"ans": "D", "explain": "D: Trời sắp mưa nên phản ứng hợp lý là mau chóng về nhà (我们快回家去吧)."},
        "22": {"ans": "B", "explain": "B: Hỏi mùa yêu thích nhất trả lời là mùa xuân (当然是春天)."},
        "23": {"ans": "C", "explain": "C: Trả lời về tình trạng sốt đáp lại câu hỏi còn sốt không (你今天觉得怎么样？还发烧吗？)."},
        "24": {"ans": "A", "explain": "A: Khuyên không cần đi vì nhà còn trái cây đáp lại ý định ra ngoài mua trái cây (要来客人了，我出去买点儿水果吧)."},
        "25": {"ans": "F", "explain": "F: 'Đừng khách sáo' đáp lại lời cảm ơn chăm sóc (谢谢你照顾我，我的腿越来越好了)."},
        "26": {"ans": "F", "explain": "F: Cấu trúc giới từ '为 + tân ngữ + động từ': 为你买 (mua cho bạn)."},
        "27": {"ans": "A", "explain": "A: Động từ chăm sóc thú cưng: 照顾一下小狗."},
        "28": {"ans": "D", "explain": "D: Lượng từ '条' đi kèm với danh từ trang phục '裙子' (chiếc váy)."},
        "29": {"ans": "C", "explain": "C: Từ chỉ thời gian '最近' (dạo này/gần đây)."},
        "30": {"ans": "B", "explain": "B: Phó từ khẳng định '当然' (đương nhiên, tất nhiên)."},
        "31": {"ans": "C", "explain": "C: Đoạn văn viết: '因为树绿了，草地也都绿了' nên đáp án đúng là C."},
        "32": {"ans": "B", "explain": "B: Đoạn văn viết rõ: '不爱吃菜，只爱吃肉' (không thích ăn rau, chỉ thích ăn thịt)."},
        "33": {"ans": "B", "explain": "B: Người Trung Quốc quanh năm đều thích uống trà ('非常爱喝的饮料'), chứng tỏ họ thấy trà rất ngon (很好喝)."},
        "34": {"ans": "A", "explain": "A: Đoạn văn khẳng định trực tiếp: '其实，不吃饭对身体不好' (Thực ra, nhịn ăn không tốt cho cơ thể)."},
        "35": {"ans": "C", "explain": "C: Đoạn văn nêu rõ: '其实，吃药的时候用热水是最好的' (uống bằng nước ấm/nước sôi để nguội là tốt nhất)."}
    }
}
