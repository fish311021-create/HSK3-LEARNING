# -*- coding: utf-8 -*-
"""
Dữ liệu Soạn Bài Chuẩn Hóa - Bài 03: 桌子上放着很多饮料
(Trên bàn để rất nhiều đồ uống)
Được khai thác trực tiếp từ Sách Giáo Khoa HSK 3 chuẩn quốc tế
"""

LESSON_DATA = {
    "lesson_info": {
        "id": 3,
        "title_zh": "桌子上放着很多饮料",
        "title_py": "Zhuōzi shang fàngzhe hěnduō yǐnliào",
        "title_vi": "Trên bàn để rất nhiều đồ uống",
        "subtitle": "Khai phá từ vựng, chiết tự, bút thuận, 4 bài khóa SGK & ngữ pháp câu chữ '着'",
        "exam_web_url": "../../1_Web_LuyenThi_HSK3/Bai_03/index.html"
    },

    # 17 TỪ VỰNG CHUẨN SGK BÀI 3
    "vocab": [
        {
            "num": 1,
            "zh": "还是",
            "py": "háishì",
            "hv": "Hoàn thị",
            "pos": "Liên từ",
            "vi": "Hay là, hoặc là (dùng trong câu hỏi lựa chọn)",
            "radicals": "Bộ Nhật (日 - mặt trời) + Chữ Bất (不) trong '还'; Bộ Nhật (日) + Sơ (疋) trong '是'.",
            "stroke_info": "还 (7 nét), 是 (9 nét). Viết 还: ngang gập, phẩy, chấm, bộ quai xước sau cùng.",
            "eg1": {"zh": "你喝咖啡还是喝茶？", "py": "Nǐ hē kāfēi háishì hē chá?", "vi": "Bạn uống cà phê hay là uống trà?"},
            "eg2": {"zh": "我们今天去爬山还是明天去？", "py": "Wǒmen jīntiān qù páshān háishì míngtiān qù?", "vi": "Chúng ta đi leo núi hôm nay hay là ngày mai đi?"},
            "expansion": "还是...吧 (Hay là... đi - dùng để biểu thị quyết định sau khi cân nhắc)."
        },
        {
            "num": 2,
            "zh": "爬山",
            "py": "páshān",
            "hv": "Bà sơn",
            "pos": "Động từ ly hợp",
            "vi": "Leo núi, đi bộ đường núi",
            "radicals": "爬: Bộ Trảo (爪 - móng vuốt) + chữ Ba (巴); 山: Bộ Sơn (núi non).",
            "stroke_info": "爬 (8 nét), 山 (3 nét). Chữ 山: sổ giữa trước, sổ gập, sổ phải.",
            "eg1": {"zh": "周末我们一起去爬山吧。", "py": "Zhōumò wǒmen yìqǐ qù páshān ba.", "vi": "Cuối tuần chúng mình cùng đi leo núi nhé."},
            "eg2": {"zh": "爬山不仅能锻炼身体，还能看风景。", "py": "Páshān bùjǐn néng duànliàn shēntǐ, hái néng kàn fēngjǐng.", "vi": "Leo núi không những rèn luyện sức khỏe mà còn ngắm được cảnh đẹp."},
            "expansion": "去爬山 (đi leo núi), 爬上山顶 (leo lên đỉnh núi)."
        },
        {
            "num": 3,
            "zh": "小心",
            "py": "xiǎoxīn",
            "hv": "Tiểu tâm",
            "pos": "Tính từ / Động từ",
            "vi": "Cẩn thận, chú ý cẩn mật",
            "radicals": "小: Bộ Tiểu (nhỏ bé); 心: Bộ Tâm (trái tim, tâm trí).",
            "stroke_info": "小 (3 nét: sổ móc giữa, 2 chấm hai bên); 心 (4 nét).",
            "eg1": {"zh": "路上车多，要小心点儿。", "py": "Lùshang chē duō, yào xiǎoxīn diǎnr.", "vi": "Trên đường nhiều xe, phải cẩn thận một chút đấy."},
            "eg2": {"zh": "下雪了，小心路滑。", "py": "Xià xuě le, xiǎoxīn lù huá.", "vi": "Tuyết rơi rồi, cẩn thận đường trơn."},
            "expansion": "小心一点儿 (cẩn thận một chút), 小心地 + Động từ (làm gì một cách cẩn thận)."
        },
        {
            "num": 4,
            "zh": "条",
            "py": "tiáo",
            "hv": "Điều",
            "pos": "Lượng từ",
            "vi": "Chiếc, con, sợi, dải (vật dài, uốn lượn)",
            "radicals": "Bao gồm chữ Phách/Trĩ (夂) ở trên và Bộ Mộc (木) ở dưới.",
            "stroke_info": "7 nét: phẩy, ngang gập phẩy, mác, sổ, phẩy, chấm.",
            "eg1": {"zh": "他买了一条新裤子。", "py": "Tā mǎi le yì tiáo xīn kùzi.", "vi": "Anh ấy đã mua một chiếc quần mới."},
            "eg2": {"zh": "河里有一条大鱼。", "py": "Hé lǐ yǒu yì tiáo dà yú.", "vi": "Dưới sông có một con cá lớn."},
            "expansion": "一条裤子 (chiếc quần), 一条鱼 (con cá), 一条河 (dòng sông), 一条路 (con đường)."
        },
        {
            "num": 5,
            "zh": "裤子",
            "py": "kùzi",
            "hv": "Khố tử",
            "pos": "Danh từ",
            "vi": "Quần",
            "radicals": "Bộ Y (衤 - trang phục quần áo) + Chữ Khố (库 - nhà kho).",
            "stroke_info": "裤 (12 nét): Bộ Y bên trái, bên phải là Quảng (广) và Xa (车).",
            "eg1": {"zh": "这条裤子长短正合适。", "py": "Zhè tiáo kùzi chángduǎn zhèng héshì.", "vi": "Chiếc quần này độ dài vừa vặn luôn."},
            "eg2": {"zh": "服务员，请帮我拿一条黑色的裤子。", "py": "Fúwùyuán, qǐng bāng wǒ ná yì tiáo hēisè de kùzi.", "vi": "Phục vụ ơi, lấy giúp tôi một chiếc quần màu đen với."},
            "expansion": "穿裤子 (mặc quần), 牛仔裤 (quần bò/jean), 短裤 (quần soóc/quần đùi)."
        },
        {
            "num": 6,
            "zh": "记得",
            "py": "jìde",
            "hv": "Ký đắc",
            "pos": "Động từ",
            "vi": "Nhớ, còn ghi nhớ trong đầu",
            "radicals": "记: Bộ Ngôn (讠) + Chữ Kỷ (己); 得: Bộ Xích (彳) + Nhật (日) + Thốn (寸).",
            "stroke_info": "记 (5 nét), 得 (11 nét). Phân biệt 记得 (còn nhớ) với 想 (nhớ nhung/muốn).",
            "eg1": {"zh": "我还记得我们第一次见面的地方。", "py": "Wǒ hái jìde wǒmen dì-yī cì jiànmiàn de dìfang.", "vi": "Tôi vẫn nhớ nơi lần đầu tiên chúng mình gặp nhau."},
            "eg2": {"zh": "你不记得他的电话号码了吗？", "py": "Nǐ bù jìde tā de diànhuà hàomǎ le ma?", "vi": "Bạn không nhớ số điện thoại của anh ấy nữa à?"},
            "expansion": "记不清 (nhớ không rõ), 记本 (sổ ghi chép)."
        },
        {
            "num": 7,
            "zh": "衬衫",
            "py": "chènshān",
            "hv": "Sấn sam",
            "pos": "Danh từ",
            "vi": "Áo sơ mi",
            "radicals": "Cả hai chữ đều có Bộ Y (衤 - trang phục vải vóc).",
            "stroke_info": "衬 (8 nét: bộ Y + chữ Thốn 寸), 衫 (8 nét: bộ Y + 3 nét phẩy Sam 彡).",
            "eg1": {"zh": "穿白衬衫看起来很精神。", "py": "Chuān bái chènshān kàn qǐlái hěn jīngshen.", "vi": "Mặc áo sơ mi trắng trông rất sáng sủa tinh anh."},
            "eg2": {"zh": "那件衬衫有点儿贵，但是质量很好。", "py": "Nà jiàn chènshān yǒudiǎnr guì, dànshì zhìliàng hěn hǎo.", "vi": "Chiếc áo sơ mi đó hơi đắt một chút nhưng chất lượng rất tốt."},
            "expansion": "一件衬衫 (một chiếc áo sơ mi - dùng lượng từ 件 jiàn)."
        },
        {
            "num": 8,
            "zh": "元",
            "py": "yuán",
            "hv": "Nguyên",
            "pos": "Lượng từ tiền tệ",
            "vi": "Đồng Nhân dân tệ (văn viết, bằng 块 kuài trong khẩu ngữ)",
            "radicals": "Bộ Nhất (一) ở trên + Chữ Nhi (儿) ở dưới.",
            "stroke_info": "4 nét: ngang trên, ngang dưới dài hơn, phẩy, sổ gập móc.",
            "eg1": {"zh": "这本书一共三十元。", "py": "Zhè běn shū yígòng sānshí yuán.", "vi": "Cuốn sách này tổng cộng ba mươi tệ."},
            "eg2": {"zh": "这件衣服五十块（元）。", "py": "Zhè jiàn yīfu wǔshí kuài (yuán).", "vi": "Bộ quần áo này giá 50 tệ."},
            "expansion": "一元钱 (1 tệ tiền), 美元 (đô la Mỹ), 欧元 (đồng Euro)."
        },
        {
            "num": 9,
            "zh": "新鲜",
            "py": "xīnxiān",
            "hv": "Tân tiên",
            "pos": "Tính từ",
            "vi": "Tươi ngon (hoa quả, thức ăn), trong lành (không khí)",
            "radicals": "新: Thân (亲) + Cân (斤 - cái búa rìu); 鲜: Ngư (鱼 - cá) + Dương (羊 - cừu). Cá và dê kết hợp thành vị tươi ngon!",
            "stroke_info": "新 (13 nét), 鲜 (14 nét).",
            "eg1": {"zh": "早晨山上的空气很新鲜。", "py": "Zǎochén shānshang de kōngqì hěn xīnxiān.", "vi": "Buổi sáng không khí trên núi rất trong lành."},
            "eg2": {"zh": "这些苹果是今天刚买的，非常新鲜。", "py": "Zhèxiē píngguǒ shì jīntiān gāng mǎi de, fēicháng xīnxiān.", "vi": "Mấy quả táo này vừa mua hôm nay, rất tươi ngon."},
            "expansion": "新鲜水果 (hoa quả tươi), 新鲜空气 (không khí trong lành)."
        },
        {
            "num": 10,
            "zh": "甜",
            "py": "tián",
            "hv": "Điềm",
            "pos": "Tính từ",
            "vi": "Ngọt ngào, có vị ngọt",
            "radicals": "Bộ Thiệt (舌 - cái lưỡi) bên trái + Bộ Cam (甘 - vị ngọt) bên phải. Lưỡi nếm vị ngọt!",
            "stroke_info": "11 nét: Bộ Thiệt 6 nét + Bộ Cam 5 nét.",
            "eg1": {"zh": "这个西瓜真甜。", "py": "Zhè ge xīguā zhēn tián.", "vi": "Quả dưa hấu này ngọt thật đấy."},
            "eg2": {"zh": "我不喜欢吃太甜的蛋糕。", "py": "Wǒ bù xǐhuan chī tài tián de dàngāo.", "vi": "Tôi không thích ăn bánh kem ngọt quá."},
            "expansion": "甜品 (món tráng miệng ngọt), 甜言蜜语 (lời nói ngọt ngào mật ngọt)."
        },
        {
            "num": 11,
            "zh": "只",
            "py": "zhǐ",
            "hv": "Chỉ",
            "pos": "Phó từ",
            "vi": "Chỉ, duy chỉ có",
            "radicals": "Bộ Khẩu (口 - cái miệng) ở trên + Bộ Bát (八) ở dưới.",
            "stroke_info": "5 nét. Chú ý: Là chữ đa âm tự (Phó từ zhǐ: chỉ; Lượng từ zhī: con, chiếc).",
            "eg1": {"zh": "我只有一个姐姐。", "py": "Wǒ zhǐ yǒu yí ge jiějie.", "vi": "Tôi chỉ có một người chị gái thôi."},
            "eg2": {"zh": "他只要了一杯水，什么也没吃。", "py": "Tā zhǐ yào le yì bēi shuǐ, shénme yě méi chī.", "vi": "Anh ấy chỉ gọi một cốc nước, chẳng ăn gì cả."},
            "expansion": "只有 (chỉ có), 只要 (chỉ cần), 只能 (chỉ có thể)."
        },
        {
            "num": 12,
            "zh": "放",
            "py": "fàng",
            "hv": "Phóng",
            "pos": "Động từ",
            "vi": "Đặt, để, đặt để tại chỗ",
            "radicals": "Bộ Phương (方 - phương hướng) bên trái + Bộ Phộc (攵 - đánh khẽ/động tác) bên phải.",
            "stroke_info": "8 nét: 方 (4 nét) + 攵 (4 nét).",
            "eg1": {"zh": "请把手机放在桌子上。", "py": "Qǐng bǎ shǒujī fàng zài zhuōzi shang.", "vi": "Xin vui lòng đặt điện thoại lên bàn."},
            "eg2": {"zh": "桌子上放着很多书和饮料。", "py": "Zhuōzi shang fàngzhe hěnduō shū hé yǐnliào.", "vi": "Trên bàn đang để rất nhiều sách và đồ uống."},
            "expansion": "放假 (nghỉ lễ/nghỉ phép), 放心 (yên tâm), 放下 (đặt xuống)."
        },
        {
            "num": 13,
            "zh": "饮料",
            "py": "yǐnliào",
            "hv": "Ẩm liệu",
            "pos": "Danh từ",
            "vi": "Đồ uống, thức uống các loại",
            "radicals": "饮: Bộ Thực (饣 - ăn uống) + Chữ Khiếm (欠); 料: Chữ Mễ (米) + Chữ Đẩu (斗).",
            "stroke_info": "饮 (7 nét), 料 (10 nét).",
            "eg1": {"zh": "冰箱里有很多冷饮料。", "py": "Bīngxiāng lǐ yǒu hěnduō lěng yǐnliào.", "vi": "Trong tủ lạnh có rất nhiều đồ uống lạnh."},
            "eg2": {"zh": "你想喝点儿什么饮料？", "py": "Nǐ xiǎng hē diǎnr shénme yǐnliào?", "vi": "Bạn muốn uống chút đồ uống gì nào?"},
            "expansion": "热饮料 (đồ uống nóng), 碳酸饮料 (nước ngọt có ga)."
        },
        {
            "num": 14,
            "zh": "或者",
            "py": "huòzhě",
            "hv": "Hoặc giả",
            "pos": "Liên từ",
            "vi": "Hoặc, hoặc là (dùng trong câu khẳng định/trần thuật)",
            "radicals": "或: Bộ Qua (戈 - vũ khí) bao bọc; 者: Bộ Lão (耂) + Bộ Nhật (日).",
            "stroke_info": "或 (8 nét), 者 (8 nét). Trọng tâm so sánh với 还是 háishì!",
            "eg1": {"zh": "星期天我常看书或者听音乐。", "py": "Xīngqītiān wǒ cháng kànshū huòzhě tīng yīnyuè.", "vi": "Chủ nhật tôi thường đọc sách hoặc nghe nhạc."},
            "eg2": {"zh": "你明天或者后天来都可以。", "py": "Nǐ míngtiān huòzhě hòutiān lái dōu kěyǐ.", "vi": "Bạn ngày mai hoặc ngày kia đến đều được cả."},
            "expansion": "A 或者 B 都行 (A hoặc B đều được)."
        },
        {
            "num": 15,
            "zh": "舒服",
            "py": "shūfu",
            "hv": "Thư phục",
            "pos": "Tính từ",
            "vi": "Thoải mái, dễ chịu, khỏe khoắn",
            "radicals": "舒: Chữ Xá (舍) + Chữ Dư (予); 服: Bộ Nguyệt (月) + Chữ Phục (𠬝).",
            "stroke_info": "舒 (12 nét), 服 (8 nét: đọc thanh nhẹ 'fu').",
            "eg1": {"zh": "吹着凉风真舒服。", "py": "Chuīzhe liángfēng zhēn shūfu.", "vi": "Được gió mát thổi qua thật là dễ chịu."},
            "eg2": {"zh": "我今天身体有点儿不舒服，想请假。", "py": "Wǒ jīntiān shēntǐ yǒudiǎnr bù shūfu, xiǎng qǐngjià.", "vi": "Hôm nay người tôi hơi không được khỏe, muốn xin nghỉ phép."},
            "expansion": "不舒服 (khó chịu, trong người thấy ốm)."
        },
        {
            "num": 16,
            "zh": "花",
            "py": "huā",
            "hv": "Hoa",
            "pos": "Danh từ / Động từ",
            "vi": "Hoa, bông hoa (Danh từ); Tiêu xài thời gian/tiền bạc (Động từ)",
            "radicals": "Bộ Thảo đầu (艹 - cây cỏ hoa lá) ở trên + Chữ Hóa (化) ở dưới.",
            "stroke_info": "7 nét: ngang, 2 nét sổ của Thảo đầu, phẩy, sổ đứng, phẩy gập.",
            "eg1": {"zh": "公园里的花开了，真漂亮。", "py": "Gōngyuán lǐ de huā kāi le, zhēn piàoliang.", "vi": "Hoa trong công viên đã nở rồi, đẹp thật đấy."},
            "eg2": {"zh": "买这件衣服花了我两百元。", "py": "Mǎi zhè jiàn yīfu huā le wǒ liǎng bǎi yuán.", "vi": "Mua bộ quần áo này tốn của tôi hai trăm tệ."},
            "expansion": "开花 (nở hoa), 花钱 (tiêu tiền), 花时间 (tốn thời gian)."
        },
        {
            "num": 17,
            "zh": "绿",
            "py": "lǜ",
            "hv": "Lục",
            "pos": "Tính từ",
            "vi": "Xanh lá cây, xanh lục",
            "radicals": "Bộ Mịch (纟 - sợi tơ) bên trái + Chữ Lục (录) bên phải. Nhuộm sợi tơ màu lục!",
            "stroke_info": "11 nét: 纟 (3 nét) + 录 (8 nét). Phát âm âm 'ü' tròn môi.",
            "eg1": {"zh": "春天草地变得很绿。", "py": "Chūntiān cǎodì biàn de hěn lǜ.", "vi": "Mùa xuân bãi cỏ trở nên rất xanh tươi."},
            "eg2": {"zh": "窗外是一片绿色的树林。", "py": "Chuāngwài shì yí piàn lǜsè de shùlín.", "vi": "Ngoài cửa sổ là một rặng cây xanh mướt."},
            "expansion": "绿茶 (trà xanh), 绿草 (cỏ xanh), 绿色 (màu xanh lá)."
        }
    ],

    # CẶP NỐI TỪ CHO GAME 2 CỘT
    "matching_pairs": [
        {"zh": "还是", "vi": "hay là (câu hỏi)", "py": "háishì"},
        {"zh": "爬山", "vi": "leo núi", "py": "páshān"},
        {"zh": "小心", "vi": "cẩn thận", "py": "xiǎoxīn"},
        {"zh": "条", "vi": "chiếc, con (lượng từ)", "py": "tiáo"},
        {"zh": "裤子", "vi": "quần", "py": "kùzi"},
        {"zh": "记得", "vi": "nhớ, ghi nhớ", "py": "jìde"},
        {"zh": "衬衫", "vi": "áo sơ mi", "py": "chènshān"},
        {"zh": "元", "vi": "đồng nhân dân tệ", "py": "yuán"},
        {"zh": "新鲜", "vi": "tươi ngon, trong lành", "py": "xīnxiān"},
        {"zh": "甜", "vi": "ngọt ngào", "py": "tián"},
        {"zh": "只", "vi": "chỉ, duy chỉ có", "py": "zhǐ"},
        {"zh": "放", "vi": "đặt, để", "py": "fàng"},
        {"zh": "饮料", "vi": "đồ uống", "py": "yǐnliào"},
        {"zh": "或者", "vi": "hoặc là (câu khẳng định)", "py": "huòzhě"},
        {"zh": "舒服", "vi": "dễ chịu, thoải mái", "py": "shūfu"},
        {"zh": "花", "vi": "hoa / tiêu xài", "py": "huā"},
        {"zh": "绿", "vi": "xanh lá cây", "py": "lǜ"}
    ],

    # 4 BÀI KHÓA SGK KÈM AUDIO THẬT VÀ PHÂN TÍCH TỪNG CÂU
    "dialogues": [
        {
            "num": 1,
            "title": "在家喝茶 (Ở nhà uống trà)",
            "location": "在家 (Tại nhà)",
            "audio_file": "audio_textbook/Bai_03/03-1.mp3",
            "context": "Hai người bạn đang ở nhà trò chuyện về kế hoạch đi chơi cuối tuần và đồ uống giải khát.",
            "lines": [
                {"role": "female", "speaker": "小丽", "zh": "明天是晴天还是阴天？", "py": "Míngtiān shì qíngtiān háishì yīntiān?", "vi": "Ngày mai là ngày nắng hay ngày âm u vậy?", "analysis": "Dùng liên từ '还是' để hỏi lựa chọn giữa hai khả năng: trời nắng (晴天) hay u ám (阴天)."},
                {"role": "male", "speaker": "小刚", "zh": "阴天，电视上说多云。怎么了？有事？", "py": "Yīntiān, diànshì shang shuō duōyún. Zěnme le? Yǒu shì?", "vi": "Trời âm u, trên tivi bảo nhiều mây. Sao thế? Có việc gì à?", "analysis": "Cụm từ '电视上' (trên tivi). Câu hỏi ngắn thân mật '怎么了？有事？'."},
                {"role": "female", "speaker": "小丽", "zh": "没事，我们明天要去爬山。", "py": "Méi shì, wǒmen míngtiān yào qù páshān.", "vi": "Không có gì, mai bọn mình định đi leo núi.", "analysis": "Động từ '要' biểu thị dự định sắp thực hiện; từ mới '爬山' (leo núi)."},
                {"role": "male", "speaker": "小刚", "zh": "爬山的时候要小心点儿。", "py": "Páshān de shíhou yào xiǎoxīn diǎnr.", "vi": "Lúc leo núi thì phải cẩn thận một chút nhé.", "analysis": "Cấu trúc '...的时候' (lúc/khi...); tính từ '小心' làm vị ngữ có '点儿' làm bổ ngữ mức độ nhẹ nhàng khuyên nhủ."},
                {"role": "female", "speaker": "小丽", "zh": "好，你也去吗？", "py": "Hǎo, nǐ yě qù ma?", "vi": "Được rồi, cậu cũng đi chứ?"},
                {"role": "male", "speaker": "小刚", "zh": "我不去，我有事。", "py": "Wǒ bú qù, wǒ yǒu shì.", "vi": "Tớ không đi đâu, tớ có việc bận rồi."}
            ],
            "check_question": {
                "question": "小丽明天打算做什么？ (Tiểu Lệ ngày mai dự định làm gì?)",
                "options": ["在家看电视", "去爬山", "去买衣服", "去喝咖啡"],
                "ans": "B",
                "explain": "Trong bài tiểu Lệ nói: '我们明天要去爬山' (Ngày mai chúng tôi định đi leo núi)."
            }
        },
        {
            "num": 2,
            "title": "在商场买衣服 (Mua quần áo ở trung tâm thương mại)",
            "location": "在商场 (Ở trung tâm thương mại)",
            "audio_file": "audio_textbook/Bai_03/03-2.mp3",
            "context": "Tiểu Cương và Tiểu Lệ đi mua sắm quần áo, Tiểu Cương thử áo sơ mi và xin ý kiến Tiểu Lệ.",
            "lines": [
                {"role": "male", "speaker": "小刚", "zh": "你觉得这条裤子怎么样？", "py": "Nǐ juéde zhè tiáo kùzi zěnmeyàng?", "vi": "Em thấy chiếc quần này thế nào?", "analysis": "Lượng từ '条' dùng cho '裤子'; câu hỏi ý kiến '...怎么样?'."},
                {"role": "female", "speaker": "小丽", "zh": "我记得你已经有两条这样的裤子了。", "py": "Wǒ jìde nǐ yǐjīng yǒu liǎng tiáo zhèyàng de kùzi le.", "vi": "Em nhớ là anh đã có hai chiếc quần như thế này rồi mà.", "analysis": "Động từ '记得' (ghi nhớ); cấu trúc '已经...了' (đã... rồi); '两条' (hai chiếc)."},
                {"role": "male", "speaker": "小刚", "zh": "那我们再看看别的新衣服吧。", "py": "Nà wǒmen zài kànkan bié de xīn yīfu ba.", "vi": "Thế thì chúng mình xem tiếp quần áo mới khác đi.", "analysis": "Phó từ '再' biểu thị hành động tiếp diễn trong tương lai; lặp lại động từ '看看'."},
                {"role": "female", "speaker": "小丽", "zh": "这件衬衫怎么样？", "py": "Zhè jiàn chènshān zěnmeyàng?", "vi": "Chiếc áo sơ mi này thế nào?", "analysis": "Lượng từ của áo sơ mi là '件' (jiàn), không dùng '条'!"},
                {"role": "male", "speaker": "小刚", "zh": "还不错，多少钱一件？", "py": "Hái búcuò, duōshao qián yí jiàn?", "vi": "Cũng khá đấy, bao nhiêu tiền một chiếc vậy?", "analysis": "Thành ngữ khẩu ngữ '还不错' (cũng khá/không tồi). Hỏi giá: '多少钱...?'"},
                {"role": "female", "speaker": "小丽", "zh": "这上面写着三百二十元。", "py": "Zhè shàngmiàn xiězhe sānbǎi èrshí yuán.", "vi": "Trên này ghi là ba trăm hai mươi tệ.", "analysis": "CÂU CHỮ '着': '这上面' (vị trí) + '写着' (động từ kèm 着) + '三百二十元' (nội dung hiển thị)."},
                {"role": "male", "speaker": "小刚", "zh": "买一件。", "py": "Mǎi yí jiàn.", "vi": "Mua một chiếc nhé."}
            ],
            "check_question": {
                "question": "那件衬衫多少钱？ (Chiếc áo sơ mi đó giá bao nhiêu tiền?)",
                "options": ["两百元", "三百元", "三百二十元", "四百元"],
                "ans": "C",
                "explain": "Tiểu Lệ đọc trên mác áo: '这上面写着三百二十元' (Trên này ghi 320 tệ)."
            }
        },
        {
            "num": 3,
            "title": "在水果摊买水果 (Mua hoa quả ở quầy trái cây)",
            "location": "在水果摊 (Tại quầy hoa quả)",
            "audio_file": "audio_textbook/Bai_03/03-3.mp3",
            "context": "Khách hàng trò chuyện với người bán hoa quả về độ ngọt và tươi ngon của dưa hấu và táo.",
            "lines": [
                {"role": "male", "speaker": "周太太", "zh": "这些西瓜真新鲜，甜不甜？", "py": "Zhèxiē xīguā zhēn xīnxiān, tián bu tián?", "vi": "Mấy quả dưa hấu này tươi ngon thật, có ngọt không đấy?", "analysis": "Tính từ '新鲜' (tươi); câu hỏi chính phản '甜不甜' (ngọt hay không ngọt)."},
                {"role": "female", "speaker": "售货员", "zh": "不甜不要钱。您要大的还是小的？", "py": "Bù tián bú yào qián. Nín yào dà de háishì xiǎo de?", "vi": "Không ngọt không lấy tiền ạ. Bác muốn quả to hay quả nhỏ?", "analysis": "Cách chào mời nổi tiếng: '不甜不要钱'. Câu hỏi lựa chọn với '还是'."},
                {"role": "male", "speaker": "周太太", "zh": "买个大的吧。苹果怎么样？", "py": "Mǎi ge dà de ba. Píngguǒ zěnmeyàng?", "vi": "Mua một quả to đi. Thế còn táo thì sao?", "analysis": "Tỉnh lược lượng từ '个' (买个大的); chuyển hướng chủ đề hỏi về táo."},
                {"role": "female", "speaker": "售货员", "zh": "苹果也很好，又大又甜，还很便宜。", "py": "Píngguǒ yě hěn hǎo, yòu dà yòu tián, hái hěn piányi.", "vi": "Táo cũng rất ngon bác ạ, vừa to lại vừa ngọt, lại còn rất rẻ nữa.", "analysis": "Cấu trúc song hành '又...又...' (vừa... vừa...): 又大又甜 (vừa to vừa ngọt)."}
            ],
            "check_question": {
                "question": "售货员觉得苹果怎么样？ (Người bán hàng thấy táo thế nào?)",
                "options": ["不太甜", "有点儿贵", "又大又甜还便宜", "不新鲜"],
                "ans": "C",
                "explain": "Người bán hàng khen: '苹果也很好，又大又甜，还很便宜'."
            }
        },
        {
            "num": 4,
            "title": "在休息室 (Ở phòng nghỉ)",
            "location": "在休息室 (Tại phòng nghỉ ngơi)",
            "audio_file": "audio_textbook/Bai_03/03-4.mp3",
            "context": "Hai đồng nghiệp cùng ngồi nghỉ ngơi uống nước, ngắm nhìn khung cảnh thư thái ngoài cửa sổ.",
            "lines": [
                {"role": "female", "speaker": "小丽", "zh": "桌子上放着很多饮料，你喝什么？", "py": "Zhuōzi shang fàngzhe hěnduō yǐnliào, nǐ hē shénme?", "vi": "Trên bàn để rất nhiều đồ uống, bạn uống gì nào?", "analysis": "CÂU TỒN HIỆN CHỦ ĐẠO CỦA BÀI: '桌子上' (Nơi chốn) + '放着' (Động từ + 着) + '很多饮料' (Tân ngữ vật thể)."},
                {"role": "male", "speaker": "小刚", "zh": "茶或者咖啡都可以。你呢？你喝什么？", "py": "Chá huòzhě kāfēi dōu kěyǐ. Nǐ ne? Nǐ hē shénme?", "vi": "Trà hoặc là cà phê đều được cả. Còn cậu? Cậu uống gì?", "analysis": "PHÂN BIỆT '或者': Đây là câu trần thuật khẳng định nên DÙNG '或者', KHÔNG DÙNG '还是'!"},
                {"role": "female", "speaker": "小丽", "zh": "我喝茶，茶是我的最爱。天冷了或者累了的时候，喝杯热茶很舒服。", "py": "Wǒ hē chá, chá shì wǒ de zuì ài. Tiān lěng le huòzhě lèi le de shíhou, hē bēi rè chá hěn shūfu.", "vi": "Tớ uống trà, trà là món tớ mê nhất. Khi trời trở lạnh hoặc khi thấy mệt mỏi, được uống ly trà nóng thì thật dễ chịu.", "analysis": "Dùng '或者' nối hai trạng thái: '天冷了或者累了的时候'; tính từ '舒服' (thoải mái)."},
                {"role": "male", "speaker": "小刚", "zh": "你看，窗外放着很多花，草也绿了，真漂亮。", "py": "Nǐ kàn, chuāngwài fàngzhe hěnduō huā, cǎo yě lǜ le, zhēn piàoliang.", "vi": "Cậu nhìn xem, ngoài cửa sổ đặt bao nhiêu là hoa, cỏ cũng xanh mướt rồi, đẹp thật đấy.", "analysis": "Thêm một câu tồn hiện: '窗外放着很多花' (Ngoài cửa sổ đang đặt rất nhiều hoa)."}
            ],
            "check_question": {
                "question": "小刚想喝什么？ (Tiểu Cương muốn uống gì?)",
                "options": ["只要冷饮", "只喝牛奶", "茶或者咖啡都可以", "什么都不喝"],
                "ans": "C",
                "explain": "Tiểu Cương trả lời rõ ràng: '茶或者咖啡都可以' (Trà hoặc cà phê đều được cả)."
            }
        }
    ],

    # XƯỞNG NGỮ PHÁP (GRAMMAR LAB) VÀ BÀI TẬP BẪY ĐỀ THI
    "grammar": [
        {
            "id": 1,
            "title": "Câu Tồn Hiện với Động từ + “着” (存现句)",
            "formula": "Từ chỉ Nơi chốn / Vị trí + Động từ + 着 + (Số lượng / Hình dung từ) + Danh từ",
            "desc": "Dùng để biểu thị ở một địa điểm nào đó đang tồn tại hoặc đang duy trì trạng thái của một vật thể hay người.",
            "key_rules": [
                "1. Từ đầu câu PHẢI là từ chỉ nơi chốn (như: 桌子上, 门前, 墙上, 窗外).",
                "2. Động từ thường là động từ chỉ tư thế/trạng thái tĩnh: 放 (đặt), 挂 (treo), 坐 (ngồi), 站 (đứng), 躺 (nằm), 开 (mở).",
                "3. Dạng phủ định: Thêm '没' hoặc '没有' trước động từ, và BỎ số từ/lượng từ (Ví dụ: 桌子上没放饮料)."
            ],
            "examples": [
                {"zh": "桌子上放着很多饮料。", "py": "Zhuōzi shang fàngzhe hěnduō yǐnliào.", "vi": "Trên bàn đang để rất nhiều đồ uống."},
                {"zh": "墙上挂着一张中国地图。", "py": "Qiáng shang guàzhe yì zhāng Zhōngguó dìtú.", "vi": "Trên tường đang treo một tấm bản đồ Trung Quốc."},
                {"zh": "门开着呢，请进吧。", "py": "Mén kāizhe ne, qǐng jìn ba.", "vi": "Cửa đang mở đấy, xin mời vào."}
            ],
            "traps": "BẪY HSK 3: Không được thêm từ '在' trước nơi chốn nếu muốn dùng câu tồn hiện thuần túy (Sai: 在桌子上放着书 ➔ Đúng: 桌子上放着书)."
        },
        {
            "id": 2,
            "title": "Phân Biệt Cặp Từ Dễ Nhầm Lẫn: “还是” vs “或者”",
            "formula": "Câu hỏi / Phân vân: A 还是 B ?  |  Câu trần thuật / Khẳng định: A 或者 B .",
            "desc": "Cả hai từ đều mang nghĩa tương đương 'hoặc, hay là' trong tiếng Việt, nhưng ngữ cảnh sử dụng hoàn toàn trái ngược nhau.",
            "comparison_table": [
                {"criteria": "Loại câu sử dụng", "haishi": "Chỉ dùng trong CÂU HỎI hoặc mệnh đề mang tính nghi vấn", "huozhe": "Dùng trong CÂU KHẲNG ĐỊNH, câu trần thuật"},
                {"criteria": "Dấu hiệu nhận biết", "haishi": "Thường kết thúc bằng dấu chấm hỏi '?' hoặc từ nghi vấn (不知道, 想想)", "huozhe": "Kết thúc bằng dấu chấm '.', biểu thị phương án nào cũng được"},
                {"criteria": "Ví dụ chuẩn", "haishi": "你喝茶还是喝咖啡？ (Bạn uống trà hay cà phê?)", "huozhe": "茶或者咖啡都可以。 (Trà hoặc cà phê đều được.)"}
            ],
            "traps": "BẪY ĐẶC BIỆT: Khi trong câu trần thuật có cụm từ chỉ sự phân vân nghi vấn như '我不知道 / 我还没想好' thì vẫn PHẢI DÙNG '还是' (Ví dụ: 我不知道他是中国人还是日本人)."
        }
    ],

    # MINI QUIZ KIỂM TRA NGỮ PHÁP (5 CÂU)
    "mini_quiz": [
        {
            "id": 1,
            "q": "桌子上______很多新鲜的水果。",
            "options": ["A. 放了", "B. 放着", "C. 放过", "D. 正在放"],
            "ans": "B",
            "explain": "Câu tồn hiện miêu tả trạng thái tĩnh của đồ vật ở một vị trí dùng cấu trúc: Nơi chốn + Động từ + 着 + Danh từ."
        },
        {
            "id": 2,
            "q": "你打算今天去买衬衫______明天去？",
            "options": ["A. 或者", "B. 还是", "C. 但是", "D. 因为"],
            "ans": "B",
            "explain": "Câu hỏi lựa chọn kết thúc bằng dấu hỏi '?' bắt buộc dùng liên từ '还是' (hay là)."
        },
        {
            "id": 3,
            "q": "周末我常在宿舍听音乐______看电影。",
            "options": ["A. 还是", "B. 或者", "C. 而且", "D. 可是"],
            "ans": "B",
            "explain": "Đây là câu trần thuật kể về thói quen cuối tuần, diễn tả hai khả năng đều được, nên phải dùng '或者'."
        },
        {
            "id": 4,
            "q": "我不知道明天是晴天______阴天。",
            "options": ["A. 或者", "B. 还有", "C. 还是", "D. 那么"],
            "ans": "C",
            "explain": "Mặc dù câu kết thúc bằng dấu chấm, nhưng có cụm từ nghi vấn '我不知道' (tôi không biết liệu rằng...), biểu thị sự phân vân lựa chọn nên bắt buộc dùng '还是'."
        },
        {
            "id": 5,
            "q": "Câu nào sau đây đúng ngữ pháp câu tồn hiện?",
            "options": [
                "A. 墙上挂着一张中国地图。",
                "B. 在墙上挂着一张中国地图。",
                "C. 墙上挂一张中国地图着。",
                "D. 墙上是一张中国地图挂着。"
            ],
            "ans": "A",
            "explain": "Câu tồn hiện chuẩn: Từ chỉ vị trí đứng đầu (không cần '在') + Động từ + 着 + Cụm danh từ."
        }
    ]
}
