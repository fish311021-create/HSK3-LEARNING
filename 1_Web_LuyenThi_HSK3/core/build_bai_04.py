# -*- coding: utf-8 -*-
"""
Build Bài 04 - Cô ấy luôn cười khi nói chuyện với khách hàng (她总是笑着跟客人说话。)
Standard HSK 3 Lesson Page Generator
Strictly 100% compliant with core/template_master.html and core/validate_lesson.py
"""

import sys, os, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Read Master Template
with open('core/template_master.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Jump buttons for Bài 4
jump_buttons = '''          <button class="jump-btn" onclick="jumpAudio(0)">▶ 00:00 Mở đầu</button>
          <button class="jump-btn" onclick="jumpAudio(40)">▶ 00:40 Phần 1 (1-5)</button>
          <button class="jump-btn" onclick="jumpAudio(205)">▶ 03:25 Phần 2 (6-10)</button>
          <button class="jump-btn" onclick="jumpAudio(430)">▶ 07:10 Phần 3 (11-15)</button>
          <button class="jump-btn" onclick="jumpAudio(670)">▶ 11:10 Phần 4 (16-20)</button>'''

# ==============================================================================
# TAB 1: BÀI NGHE (LISTENING: Q1 - Q20)
# ==============================================================================
tab1_content = '''      <div class="global-toolbar">
        <button class="tool-btn active" id="btnTogglePinyin" onclick="toggleGlobalPinyin()">Ẩn / Hiện Pinyin</button>
        <button class="tool-btn active" id="btnToggleTrans" onclick="toggleGlobalTrans()">Ẩn / Hiện Dịch Nghĩa</button>
      </div>

      <!-- PHẦN 1: CÂU 1 - 5 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 1 - 5 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại &amp; tranh minh họa</span>
        </div>
        <p class="section-desc">Yêu cầu: 听对话，选择与对话内容一致的图片 (Nghe đối thoại, chọn tranh tương ứng A - F):</p>

        <!-- Tranh ảnh A-F -->
        <div class="pics-grid">
          <div class="pic-item"><img src="pic_A.png" alt="Tranh A"><div class="pic-label">Hình A: Siêu thị mua dưa hấu (超市买西瓜)</div></div>
          <div class="pic-item"><img src="pic_B.png" alt="Tranh B"><div class="pic-label">Hình B: Bánh ngọt sinh nhật / Bé gái cười (吃蛋糕 / 笑着)</div></div>
          <div class="pic-item"><img src="pic_C.png" alt="Tranh C"><div class="pic-label">Hình C: Xem thi đấu bóng đá (看足球比赛)</div></div>
          <div class="pic-item"><img src="pic_D.png" alt="Tranh D"><div class="pic-label">Hình D (Ví dụ): Gọi điện thoại (打电话)</div></div>
          <div class="pic-item"><img src="pic_E.png" alt="Tranh E"><div class="pic-label">Hình E: Đứng nói chuyện ở văn phòng (站着说话)</div></div>
          <div class="pic-item"><img src="pic_F.png" alt="Tranh F"><div class="pic-label">Hình F: Hai bạn gái xem ảnh (看照片)</div></div>
        </div>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">喂，请问张经理在吗？</span>
            <span class="pinyin-line">Wèi, qǐngwèn Zhāng jīnglǐ zài ma?</span>
            <span class="trans-line">Alo, xin hỏi giám đốc Trương có ở đó không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">他正在开会，您半个小时以后再打，好吗？</span>
            <span class="pinyin-line">Tā zhèngzài kāihuì, nín bàn ge xiǎoshí yǐhòu zài dǎ, hǎo ma?</span>
            <span class="trans-line">Ông ấy đang họp, khoảng nửa tiếng nữa bạn gọi lại được không?</span>
          </div>
          <div class="options-grid" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">D</span> Hình D: Gọi điện thoại (打电话) √</div>
          </div>
        </div>

        <!-- Câu 1 -->
        <div class="card" id="card-1">
          <span class="card-num">Câu 1</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你去做什么？</span>
            <span class="pinyin-line">Nǐ qù zuò shénme?</span>
            <span class="trans-line">Bạn đi làm gì đấy?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我去看足球比赛。</span>
            <span class="pinyin-line">Wǒ qù kàn zúqiú bǐsài.</span>
            <span class="trans-line">Tôi đi xem trận thi đấu bóng đá.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('1', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('1', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('1', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('1', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('1', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('1', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(1)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(1)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-1"></div>
        </div>

        <!-- Câu 2 -->
        <div class="card" id="card-2">
          <span class="card-num">Câu 2</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">那两个笑着看照片的女孩是谁？</span>
            <span class="pinyin-line">Nà liǎng ge xiàozhe kàn zhàopiàn de nǚhái shì shéi?</span>
            <span class="trans-line">Hai cô bạn gái đang cười xem ảnh kia là ai thế?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">那是我妹妹和她的好朋友。</span>
            <span class="pinyin-line">Nà shì wǒ mèimei hé tā de hǎo péngyou.</span>
            <span class="trans-line">Đó là em gái tôi và bạn thân của em ấy.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('2', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('2', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('2', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('2', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('2', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('2', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(2)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(2)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-2"></div>
        </div>

        <!-- Câu 3 -->
        <div class="card" id="card-3">
          <span class="card-num">Câu 3</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我太饿了，我想吃块蛋糕。</span>
            <span class="pinyin-line">Wǒ tài è le, wǒ xiǎng chī kuài dàngāo.</span>
            <span class="trans-line">Tôi đói quá rồi, tôi muốn ăn một miếng bánh ngọt.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">别吃了，我们去吃饭吧。</span>
            <span class="pinyin-line">Bié chī le, wǒmen qù chī fàn ba.</span>
            <span class="trans-line">Đừng ăn nữa, chúng mình đi ăn cơm thôi.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('3', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('3', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('3', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('3', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('3', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('3', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(3)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(3)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-3"></div>
        </div>

        <!-- Câu 4 -->
        <div class="card" id="card-4">
          <span class="card-num">Câu 4</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你怎么总是站着？快坐吧。</span>
            <span class="pinyin-line">Nǐ zěnme zǒngshì zhànzhe? Kuài zuò ba.</span>
            <span class="trans-line">Sao anh lúc nào cũng đứng thế? Mau ngồi xuống đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我吃了两块蛋糕，现在不想坐着。</span>
            <span class="pinyin-line">Wǒ chī le liǎng kuài dàngāo, xiànzài bù xiǎng zuòzhe.</span>
            <span class="trans-line">Anh ăn hai miếng bánh ngọt rồi, bây giờ không muốn ngồi.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('4', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('4', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('4', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('4', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('4', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('4', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(4)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(4)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-4"></div>
        </div>

        <!-- Câu 5 -->
        <div class="card" id="card-5">
          <span class="card-num">Câu 5</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我记得那家超市的西瓜又甜又新鲜。</span>
            <span class="pinyin-line">Wǒ jìde nà jiā chāoshì de xīguā yòu tián yòu xīnxiān.</span>
            <span class="trans-line">Tôi nhớ dưa hấu ở siêu thị đó vừa ngọt vừa tươi ngon.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">我们去看看吧。</span>
            <span class="pinyin-line">Wǒmen qù kànkan ba.</span>
            <span class="trans-line">Chúng mình đi xem thử đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好，走吧。</span>
            <span class="pinyin-line">Hǎo, zǒu ba.</span>
            <span class="trans-line">Được, đi thôi.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('5', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('5', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('5', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('5', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('5', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('5', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(5)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(5)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-5"></div>
        </div>
      </section>

      <!-- PHẦN 2: CÂU 6 - 10 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 6 - 10 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Phán đoán Đúng (√) hoặc Sai (×)</span>
        </div>
        <p class="section-desc">Yêu cầu: 听句子，判断对错 (Nghe câu nói và phán đoán câu nhận định ★ là Đúng hay Sai):</p>

        <!-- Ví dụ 1 -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ 1</span>
          <div class="speaker-line">
            <span class="interactive-text">为了让自己更健康，他每天都花一个小时去锻炼身体。</span>
            <span class="pinyin-line">Wèile ràng zìjǐ gèng jiànkāng, tā měitiān dōu huā yí ge xiǎoshí qù duànliàn shēntǐ.</span>
            <span class="trans-line">Để bản thân khỏe mạnh hơn, mỗi ngày anh ấy đều dành ra một tiếng để rèn luyện thân thể.</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">他希望自己很健康。</span>
            <span class="pinyin-line">Tā xīwàng zìjǐ hěn jiànkāng.</span>
            <span class="trans-line">Anh ấy hy vọng bản thân thật khỏe mạnh.</span>
          </div>
          <div class="options-grid grid-true-false" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">√</span> Đúng (√)</div>
          </div>
        </div>

        <!-- Ví dụ 2 -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ 2</span>
          <div class="speaker-line">
            <span class="interactive-text">今天我想早点儿回家。看了看手表，才5点。过了一会儿再看表，还是5点，我这才发现我的手表不走了。</span>
            <span class="pinyin-line">Jīntiān wǒ xiǎng zǎodiǎnr huíjiā. Kànlekan shǒubiǎo, cái 5 diǎn. Guòle yíhuìr zài kàn biǎo, háishì 5 diǎn, wǒ zhè cái fāxiàn wǒ de shǒubiǎo bù zǒu le.</span>
            <span class="trans-line">Hôm nay tôi muốn về nhà sớm chút. Nhìn đồng hồ mới 5 giờ. Lát sau nhìn lại vẫn là 5 giờ, tôi mới phát hiện đồng hồ đã chết máy.</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">那块儿手表不是他的。</span>
            <span class="pinyin-line">Nà kuàir shǒubiǎo bú shì tā de.</span>
            <span class="trans-line">Chiếc đồng hồ đó không phải của anh ấy.</span>
          </div>
          <div class="options-grid grid-true-false" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected" style="border-color:#ef4444; color:#ef4444;"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
        </div>

        <!-- Câu 6 -->
        <div class="card" id="card-6">
          <span class="card-num">Câu 6</span>
          <div class="speaker-line">
            <span class="interactive-text">这几天你总是不爱吃东西，是不是不舒服啊？</span>
            <span class="pinyin-line">Zhè jǐ tiān nǐ zǒngshì bú ài chī dōngxi, shì bu shì bù shūfu a?</span>
            <span class="trans-line">Mấy ngày nay con lúc nào cũng không chịu ăn đồ ăn, có phải không khỏe trong người không?</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">这几天他吃得很少。</span>
            <span class="pinyin-line">Zhè jǐ tiān tā chī de hěn shǎo.</span>
            <span class="trans-line">Mấy ngày nay bạn ấy ăn rất ít.</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('6', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('6', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(6)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(6)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-6"></div>
        </div>

        <!-- Câu 7 -->
        <div class="card" id="card-7">
          <span class="card-num">Câu 7</span>
          <div class="speaker-line">
            <span class="interactive-text">他又聪明又努力，老师的问题他都会回答。</span>
            <span class="pinyin-line">Tā yòu cōngming yòu nǔlì, lǎoshī de wèntí tā dōu huì huídá.</span>
            <span class="trans-line">Cậu ấy vừa thông minh lại vừa nỗ lực, câu hỏi của thầy cô cậu ấy đều biết trả lời.</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">他学习很好。</span>
            <span class="pinyin-line">Tā xuéxí hěn hǎo.</span>
            <span class="trans-line">Cậu ấy học rất giỏi.</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('7', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('7', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(7)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(7)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-7"></div>
        </div>

        <!-- Câu 8 -->
        <div class="card" id="card-8">
          <span class="card-num">Câu 8</span>
          <div class="speaker-line">
            <span class="interactive-text">你知道我手机里还有多少钱吗？还有1元1角1分，三个“1”。</span>
            <span class="pinyin-line">Nǐ zhīdào wǒ shǒujī li hái yǒu duōshao qián ma? Hái yǒu yì yuán yì jiǎo yì fēn, sān ge “yī”.</span>
            <span class="trans-line">Cậu có biết trong điện thoại mình còn bao nhiêu tiền không? Còn 1 tệ 1 hào 1 xu, đúng 3 con số 1.</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">他手机里钱不多了。</span>
            <span class="pinyin-line">Tā shǒujī li qián bù duō le.</span>
            <span class="trans-line">Tiền trong điện thoại cậu ấy không còn nhiều nữa.</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('8', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('8', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(8)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(8)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-8"></div>
        </div>

        <!-- Câu 9 -->
        <div class="card" id="card-9">
          <span class="card-num">Câu 9</span>
          <div class="speaker-line">
            <span class="interactive-text">妈妈很热情，总是帮助人，所以大家有问题都会来找她。</span>
            <span class="pinyin-line">Māma hěn rèqíng, zǒngshì bāngzhù rén, suǒyǐ dàjiā yǒu wèntí dōu huì lái zhǎo tā.</span>
            <span class="trans-line">Mẹ rất nhiệt tình, lúc nào cũng giúp đỡ mọi người, cho nên mọi người có việc gì khúc mắc đều đến nhờ mẹ.</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">妈妈现在有问题。</span>
            <span class="pinyin-line">Māma xiànzài yǒu wèntí.</span>
            <span class="trans-line">Hiện tại mẹ đang gặp phải vấn đề.</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('9', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('9', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(9)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(9)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-9"></div>
        </div>

        <!-- Câu 10 -->
        <div class="card" id="card-10">
          <span class="card-num">Câu 10</span>
          <div class="speaker-line">
            <span class="interactive-text">同学们，谁能告诉我这个句子是什么意思？</span>
            <span class="pinyin-line">Tóngxuémen, shéi néng gàosù wǒ zhè ge jùzi shì shénme yìsi?</span>
            <span class="trans-line">Các em học sinh, ai có thể nói cho thầy biết câu này có nghĩa là gì không?</span>
          </div>
          <div class="speaker-line statement">
            <span class="statement-tag">★</span>
            <span class="interactive-text">他在请人回答问题。</span>
            <span class="pinyin-line">Tā zài qǐng rén huídá wèntí.</span>
            <span class="trans-line">Thầy đang mời mọi người trả lời câu hỏi.</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('10', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('10', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(10)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(10)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-10"></div>
        </div>
      </section>

      <!-- PHẦN 3: CÂU 11 - 15 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第三部分: 第 11 - 15 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Đối thoại ngắn (2 lượt lời)</span>
        </div>
        <p class="section-desc">Yêu cầu: 听短对话，选择正确答案 (Nghe đối thoại ngắn và chọn đáp án chính xác A, B hoặc C):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">小王，帮我开一下门，好吗？谢谢！</span>
            <span class="pinyin-line">Xiǎo Wáng, bāng wǒ kāi yíxià mén, hǎo ma? Xièxie!</span>
            <span class="trans-line">Tiểu Vương, giúp tôi mở cửa một lát được không? Cảm ơn nhé!</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">没问题。您去超市了？买了这么多东西。</span>
            <span class="pinyin-line">Méi wèntí. Nín qù chāoshì le? Mǎi le zhème duō dōngxi.</span>
            <span class="trans-line">Không có vấn đề gì ạ. Bác vừa đi siêu thị về sao? Mua nhiều đồ thế này.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">男的想让小王做什么？</span>
            <span class="pinyin-line">Nán de xiǎng ràng Xiǎo Wáng zuò shénme?</span>
            <span class="trans-line">Người nam muốn nhờ Tiểu Vương làm gì?</span>
          </div>
          <div class="options-grid grid-abc" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">A</span> 开门 √</div>
            <div class="option-chip"><span class="chip-letter">B</span> 拿东西</div>
            <div class="option-chip"><span class="chip-letter">C</span> 去超市买东西</div>
          </div>
        </div>

        <!-- Câu 11 -->
        <div class="card" id="card-11">
          <span class="card-num">Câu 11</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你怎么总是听着音乐写作业？别听了，认真写吧。</span>
            <span class="pinyin-line">Nǐ zěnme zǒngshì tīngzhe yīnyuè xiě zuòyè? Bié tīng le, rènzhēn xiě ba.</span>
            <span class="trans-line">Sao em lúc nào cũng nghe nhạc khi làm bài tập thế? Đừng nghe nữa, tập trung làm đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">没关系，你看我写的都对。</span>
            <span class="pinyin-line">Méi guānxi, nǐ kàn wǒ xiě de dōu duì.</span>
            <span class="trans-line">Không sao đâu mà, chị xem em làm đều đúng cả đấy thôi.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">女的让男的做什么？</span>
            <span class="pinyin-line">Nǚ de ràng nán de zuò shénme?</span>
            <span class="trans-line">Người nữ muốn người nam làm gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('11', 'A')"><span class="chip-letter">A</span> 认真写作业</div>
            <div class="option-chip" onclick="selectOption('11', 'B')"><span class="chip-letter">B</span> 认真听音乐</div>
            <div class="option-chip" onclick="selectOption('11', 'C')"><span class="chip-letter">C</span> 听着音乐写作业</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(11)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(11)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-11"></div>
        </div>

        <!-- Câu 12 -->
        <div class="card" id="card-12">
          <span class="card-num">Câu 12</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你打电话有什么事吗？</span>
            <span class="pinyin-line">Nǐ dǎ diànhuà yǒu shénme shì ma?</span>
            <span class="trans-line">Em gọi điện có chuyện gì thế?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">家里有人来做客，你下了班就回来吧。</span>
            <span class="pinyin-line">Jiā li yǒu rén lái zuòkè, nǐ xià le bān jiù huílái ba.</span>
            <span class="trans-line">Nhà mình có khách đến chơi, anh tan làm thì về nhà ngay nhé.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">女的让男的做什么？</span>
            <span class="pinyin-line">Nǚ de ràng nán de zuò shénme?</span>
            <span class="trans-line">Người nữ bảo người nam làm gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('12', 'A')"><span class="chip-letter">A</span> 打电话</div>
            <div class="option-chip" onclick="selectOption('12', 'B')"><span class="chip-letter">B</span> 去做客</div>
            <div class="option-chip" onclick="selectOption('12', 'C')"><span class="chip-letter">C</span> 回家</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(12)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(12)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-12"></div>
        </div>

        <!-- Câu 13 -->
        <div class="card" id="card-13">
          <span class="card-num">Câu 13</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">下课了，同学们都去哪儿啊？</span>
            <span class="pinyin-line">Xiàkè le, tóngxuémen dōu qù nǎr a?</span>
            <span class="trans-line">Tan học rồi, các bạn cùng lớp đều đi đâu thế nhỉ?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">今天下午有篮球比赛，我们要去看球赛。</span>
            <span class="pinyin-line">Jīntiān xiàwǔ yǒu lánqiú bǐsài, wǒmen yào qù kàn qiúsài.</span>
            <span class="trans-line">Chiều nay có trận đấu bóng rổ, chúng mình đi xem trận đấu bóng.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">同学们要做什么？</span>
            <span class="pinyin-line">Tóngxuémen yào zuò shénme?</span>
            <span class="trans-line">Các bạn học sinh dự định làm gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('13', 'A')"><span class="chip-letter">A</span> 去比赛</div>
            <div class="option-chip" onclick="selectOption('13', 'B')"><span class="chip-letter">B</span> 看比赛</div>
            <div class="option-chip" onclick="selectOption('13', 'C')"><span class="chip-letter">C</span> 去上课</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(13)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(13)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-13"></div>
        </div>

        <!-- Câu 14 -->
        <div class="card" id="card-14">
          <span class="card-num">Câu 14</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你真的要去国外上学？</span>
            <span class="pinyin-line">Nǐ zhēnde yào qù guówài shàngxué?</span>
            <span class="trans-line">Cậu thật sự muốn ra nước ngoài du học sao?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">是啊，我爸妈也想让我去，说年轻的时候多出去走走很好。</span>
            <span class="pinyin-line">Shì a, wǒ bà mā yě xiǎng ràng wǒ qù, shuō niánqīng de shíhou duō chūqu zǒuzou hěn hǎo.</span>
            <span class="trans-line">Đúng vậy, bố mẹ mình cũng muốn mình đi, bảo rằng lúc còn trẻ ra ngoài trải nghiệm nhiều rất tốt.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">关于女的，可以知道什么？</span>
            <span class="pinyin-line">Guānyú nǚ de, kěyǐ zhīdào shénme?</span>
            <span class="trans-line">Về người nữ, ta có thể biết được điều gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('14', 'A')"><span class="chip-letter">A</span> 跟爸妈一起出国</div>
            <div class="option-chip" onclick="selectOption('14', 'B')"><span class="chip-letter">B</span> 要去国外上学</div>
            <div class="option-chip" onclick="selectOption('14', 'C')"><span class="chip-letter">C</span> 总是出去走</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(14)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(14)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-14"></div>
        </div>

        <!-- Câu 15 -->
        <div class="card" id="card-15">
          <span class="card-num">Câu 15</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">请你来回答这个问题，好吗？</span>
            <span class="pinyin-line">Qǐng nǐ lái huídá zhè ge wèntí, hǎo ma?</span>
            <span class="trans-line">Mời bạn trả lời câu hỏi này được không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">对不起，你说得太快了，我没听懂你的问题。</span>
            <span class="pinyin-line">Duìbuqǐ, nǐ shuō de tài kuài le, wǒ méi tīngdǒng nǐ de wèntí.</span>
            <span class="trans-line">Xin lỗi, bạn nói nhanh quá, tôi chưa nghe hiểu câu hỏi của bạn.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">关于女的，可以知道什么？</span>
            <span class="pinyin-line">Guānyú nǚ de, kěyǐ zhīdào shénme?</span>
            <span class="trans-line">Về người nữ, ta có thể biết được điều gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('15', 'A')"><span class="chip-letter">A</span> 说话很快</div>
            <div class="option-chip" onclick="selectOption('15', 'B')"><span class="chip-letter">B</span> 都听懂了</div>
            <div class="option-chip" onclick="selectOption('15', 'C')"><span class="chip-letter">C</span> 不能回答</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(15)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(15)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-15"></div>
        </div>
      </section>

      <!-- PHẦN 4: CÂU 16 - 20 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第四部分: 第 16 - 20 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Đối thoại dài (4 lượt lời)</span>
        </div>
        <p class="section-desc">Yêu cầu: 听长对话，选择正确答案 (Nghe đối thoại dài 4 lượt lời và chọn đáp án chính xác A, B hoặc C):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">晚饭做好了，准备吃饭了。</span>
            <span class="pinyin-line">Wǎnfàn zuòhǎo le, zhǔnbèi chī fàn le.</span>
            <span class="trans-line">Cơm tối nấu xong rồi, chuẩn bị ăn cơm thôi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">等一会儿，比赛还有三分钟就结束了。</span>
            <span class="pinyin-line">Děng yíhuìr, bǐsài hái yǒu sān fēnzhōng jiù jiéshù le.</span>
            <span class="trans-line">Chờ một lát, trận đấu còn 3 phút nữa là kết thúc rồi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">快点儿吧，一起吃，菜冷了就不好吃了。</span>
            <span class="pinyin-line">Kuài diǎnr ba, yìqǐ chī, cài lěng le jiù bù hǎochī le.</span>
            <span class="trans-line">Nhanh lên nào, ăn cùng nhau đi, đồ ăn nguội rồi thì không ngon nữa đâu.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你先吃，我马上就看完了。</span>
            <span class="pinyin-line">Nǐ xiān chī, wǒ mǎshàng jiù kànwán le.</span>
            <span class="trans-line">Em ăn trước đi, anh xem xong ngay đây.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">男的在做什么？</span>
            <span class="pinyin-line">Nán de zài zuò shénme?</span>
            <span class="trans-line">Người nam đang làm gì?</span>
          </div>
          <div class="options-grid grid-abc" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip"><span class="chip-letter">A</span> 洗澡</div>
            <div class="option-chip"><span class="chip-letter">B</span> 吃饭</div>
            <div class="option-chip selected"><span class="chip-letter">C</span> 看电视 √</div>
          </div>
        </div>

        <!-- Câu 16 -->
        <div class="card" id="card-16">
          <span class="card-num">Câu 16</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你儿子上学了吗？现在几年级？</span>
            <span class="pinyin-line">Nǐ érzi shàngxué le ma? Xiànzài jǐ niánjí?</span>
            <span class="trans-line">Con trai anh đi học chưa? Hiện tại học lớp mấy rồi?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">他现在二年级。</span>
            <span class="pinyin-line">Tā xiànzài èr niánjí.</span>
            <span class="trans-line">Cháu hiện tại học lớp hai.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">学习怎么样？</span>
            <span class="pinyin-line">Xuéxí zěnmeyàng?</span>
            <span class="trans-line">Việc học tập thế nào?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">还可以，很努力，每天都复习写作业。</span>
            <span class="pinyin-line">Hái kěyǐ, hěn nǔlì, měitiān dōu fùxí xiě zuòyè.</span>
            <span class="trans-line">Cũng được lắm, rất chăm chỉ, ngày nào cũng ôn tập và làm bài tập.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">关于儿子，可以知道什么？</span>
            <span class="pinyin-line">Guānyú érzi, kěyǐ zhīdào shénme?</span>
            <span class="trans-line">Về người con trai, ta có thể biết được điều gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('16', 'A')"><span class="chip-letter">A</span> 学习很认真</div>
            <div class="option-chip" onclick="selectOption('16', 'B')"><span class="chip-letter">B</span> 现在三年级</div>
            <div class="option-chip" onclick="selectOption('16', 'C')"><span class="chip-letter">C</span> 总是不写作业</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(16)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(16)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-16"></div>
        </div>

        <!-- Câu 17 -->
        <div class="card" id="card-17">
          <span class="card-num">Câu 17</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">这是你小时候的照片吗？真漂亮！</span>
            <span class="pinyin-line">Zhè shì nǐ xiǎoshíhou de zhàopiàn ma? Zhēn piàoliang!</span>
            <span class="trans-line">Đây là ảnh lúc nhỏ của em à? Xinh thật đấy!</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">是啊，漂亮吧？</span>
            <span class="pinyin-line">Shì a, piàoliang ba?</span>
            <span class="trans-line">Vâng ạ, xinh đúng không anh?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">很漂亮。是什么时候照的？</span>
            <span class="pinyin-line">Hěn piàoliang. Shì shénme shíhou zhào de?</span>
            <span class="trans-line">Rất xinh. Chụp lúc nào thế em?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">小学五年级。你看我那时多瘦啊。</span>
            <span class="pinyin-line">Xiǎoxué wǔ niánjí. Nǐ kàn wǒ nà shí duō shòu a.</span>
            <span class="trans-line">Lúc học lớp năm tiểu học. Anh xem hồi đó em gầy thế nào kìa.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">关于女的，可以知道什么？</span>
            <span class="pinyin-line">Guānyú nǚ de, kěyǐ zhīdào shénme?</span>
            <span class="trans-line">Về người nữ, ta có thể biết được điều gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('17', 'A')"><span class="chip-letter">A</span> 现在胖了</div>
            <div class="option-chip" onclick="selectOption('17', 'B')"><span class="chip-letter">B</span> 正在照相</div>
            <div class="option-chip" onclick="selectOption('17', 'C')"><span class="chip-letter">C</span> 现在上小学五年级</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(17)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(17)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-17"></div>
        </div>

        <!-- Câu 18 -->
        <div class="card" id="card-18">
          <span class="card-num">Câu 18</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">站着吃蛋糕的那个人是谁？</span>
            <span class="pinyin-line">Zhànzhe chī dàngāo de nà ge rén shì shéi?</span>
            <span class="trans-line">Người đang đứng ăn bánh ngọt kia là ai thế?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我们公司新来的年轻人，小周。</span>
            <span class="pinyin-line">Wǒmen gōngsī xīn lái de niánqīng rén, Xiǎo Zhōu.</span>
            <span class="trans-line">Người trẻ tuổi mới đến công ty chúng mình, Tiểu Chu.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">什么？他姓什么？</span>
            <span class="pinyin-line">Shénme? Tā xìng shénme?</span>
            <span class="trans-line">Hả? Anh ấy họ gì?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">姓周。小周又漂亮又热情，以后有时间我介绍你们认识一下。</span>
            <span class="pinyin-line">Xìng Zhōu. Xiǎo Zhōu yòu piàoliang yòu rèqíng, yǐhòu yǒu shíjiān wǒ jièshào nǐmen rènshi yíxià.</span>
            <span class="trans-line">Họ Chu. Tiểu Chu vừa xinh đẹp lại vừa nhiệt tình, sau này có thời gian anh sẽ giới thiệu cho các em làm quen.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">关于小周，可以知道什么？</span>
            <span class="pinyin-line">Guānyú Xiǎo Zhōu, kěyǐ zhīdào shénme?</span>
            <span class="trans-line">Về Tiểu Chu, ta có thể biết được điều gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('18', 'A')"><span class="chip-letter">A</span> 坐着吃蛋糕</div>
            <div class="option-chip" onclick="selectOption('18', 'B')"><span class="chip-letter">B</span> 不年轻</div>
            <div class="option-chip" onclick="selectOption('18', 'C')"><span class="chip-letter">C</span> 很漂亮，也很热情</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(18)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(18)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-18"></div>
        </div>

        <!-- Câu 19 -->
        <div class="card" id="card-19">
          <span class="card-num">Câu 19</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你站那么高，小心点儿。</span>
            <span class="pinyin-line">Nǐ zhàn nàme gāo, xiǎoxīn diǎnr.</span>
            <span class="trans-line">Em đứng cao thế kia, cẩn thận chút nhé.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">好的。你看照片放在这儿怎么样？</span>
            <span class="pinyin-line">Hǎo de. Nǐ kàn zhàopiàn fàng zài zhèr zěnmeyàng?</span>
            <span class="trans-line">Được rồi ạ. Anh xem bức ảnh để ở chỗ này thế nào?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">往右边一点儿吧。</span>
            <span class="pinyin-line">Wǎng yòubian yìdiǎnr ba.</span>
            <span class="trans-line">Sang phía bên phải một chút đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">现在好了吧？</span>
            <span class="pinyin-line">Xiànzài hǎo le ba?</span>
            <span class="trans-line">Bây giờ được chưa anh?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好了。</span>
            <span class="pinyin-line">Hǎo le.</span>
            <span class="trans-line">Được rồi đấy.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">他们在做什么？</span>
            <span class="pinyin-line">Tāmen zài zuò shénme?</span>
            <span class="trans-line">Họ đang làm gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('19', 'A')"><span class="chip-letter">A</span> 爬山</div>
            <div class="option-chip" onclick="selectOption('19', 'B')"><span class="chip-letter">B</span> 问路</div>
            <div class="option-chip" onclick="selectOption('19', 'C')"><span class="chip-letter">C</span> 放照片</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(19)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(19)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-19"></div>
        </div>

        <!-- Câu 20 -->
        <div class="card" id="card-20">
          <span class="card-num">Câu 20</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">周末你别总是坐着看电视，出去运动一下吧。</span>
            <span class="pinyin-line">Zhōumò nǐ bié zǒngshì zuòzhe kàn diànshì, chūqu yùndòng yíxià ba.</span>
            <span class="trans-line">Cuối tuần anh đừng lúc nào cũng ngồi xem tivi, ra ngoài vận động chút đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好啊，我们去爬山怎么样？</span>
            <span class="pinyin-line">Hǎo a, wǒmen qù páshān zěnmeyàng?</span>
            <span class="trans-line">Được thôi, chúng mình đi leo núi thế nào?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">今天我腿疼，就去楼下走一走吧。</span>
            <span class="pinyin-line">Jīntiān wǒ tuǐ téng, jiù qù lóuxià zǒuyizǒu ba.</span>
            <span class="trans-line">Hôm nay chân em đau, thôi thì đi xuống dưới lầu đi dạo một chút vậy.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好吧，我们走着去超市买点儿菜。</span>
            <span class="pinyin-line">Hǎo ba, wǒmen zǒuzhe qù chāoshì mǎi diǎnr cài.</span>
            <span class="trans-line">Được rồi, chúng mình đi bộ đến siêu thị mua ít đồ ăn/rau nhé.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px;">
            <span class="speaker" style="color:var(--accent); font-weight:700;">问:</span>
            <span class="interactive-text">他们打算做什么？</span>
            <span class="pinyin-line">Tāmen dǎsuàn zuò shénme?</span>
            <span class="trans-line">Họ dự định làm gì?</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('20', 'A')"><span class="chip-letter">A</span> 去买菜</div>
            <div class="option-chip" onclick="selectOption('20', 'B')"><span class="chip-letter">B</span> 看电视</div>
            <div class="option-chip" onclick="selectOption('20', 'C')"><span class="chip-letter">C</span> 去爬山</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(20)">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetQuiz(20)">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-20"></div>
        </div>
      </section>'''

# ==============================================================================
# TAB 2: BÀI ĐỌC (READING: Q21 - Q35)
# ==============================================================================
tab2_content = '''      <div class="global-toolbar">
        <button class="tool-btn active" id="btnTogglePinyinReading" onclick="toggleGlobalPinyin()">Ẩn / Hiện Pinyin</button>
        <button class="tool-btn active" id="btnToggleTransReading" onclick="toggleGlobalTrans()">Ẩn / Hiện Dịch Nghĩa</button>
      </div>

      <!-- PHẦN 1: CÂU 21 - 25 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 21 - 25 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại ghép đôi</span>
        </div>
        <p class="section-desc">Yêu cầu: 选择合适的问题 / 答语 (Chọn câu đối thoại phù hợp từ danh sách gợi ý A - F):</p>

        <!-- Khung tham khảo A - F -->
        <div class="reading-ref-box">
          <div class="reading-ref-title">CÁC CÂU LỰA CHỌN (A - F):</div>
          <div class="reading-ref-item"><span class="ref-letter">A</span> 你怎么没吃我给你买的蛋糕呢？ (Sao em không ăn chiếc bánh ngọt anh mua cho em thế?)</div>
          <div class="reading-ref-item"><span class="ref-letter">B</span> 你怎么到家就坐着看电视，也不帮我做饭？ (Sao anh vừa về đến nhà là ngồi xem tivi, cũng chẳng giúp em nấu cơm?)</div>
          <div class="reading-ref-item"><span class="ref-letter">C</span> 你觉得小丽怎么样？ (Cậu thấy Tiểu Lệ thế nào?)</div>
          <div class="reading-ref-item"><span class="ref-letter">D</span> 这么晚了，你去哪儿？ (Muộn thế này rồi, cậu đi đâu đấy?)</div>
          <div class="reading-ref-item" style="opacity:0.7;"><span class="ref-letter">E</span> 当然。我们先坐公共汽车，然后换地铁。 (Ví dụ: Đương nhiên rồi. Chúng mình đi xe buýt trước, sau đó đổi sang tàu điện ngầm.)</div>
          <div class="reading-ref-item"><span class="ref-letter">F</span> 我昨天没有认真复习。 (Hôm qua mình không ôn tập cẩn thận.)</div>
        </div>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="interactive-text">例如：你知道怎么去那儿吗？</span>
            <span class="pinyin-line">Lìrú: Nǐ zhīdào zěnme qù nàr ma?</span>
            <span class="trans-line">Ví dụ: Bạn có biết làm thế nào để đi đến đó không?</span>
          </div>
          <div class="options-grid grid-letters" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">E</span> E √</div>
          </div>
        </div>

        <!-- Câu 21 -->
        <div class="card" id="q-21">
          <span class="card-num">Câu 21</span>
          <div class="interactive-text">老师的问题你怎么都不回答？</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Lǎoshī de wèntí nǐ zěnme dōu bù huídá?</div>
              <div>Câu hỏi của thầy giáo sao cậu đều không trả lời thế?</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('21', 'A')" data-q="21" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('21', 'B')" data-q="21" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('21', 'C')" data-q="21" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('21', 'D')" data-q="21" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('21', 'F')" data-q="21" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('21')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('21')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-21"></div>
        </div>

        <!-- Câu 22 -->
        <div class="card" id="q-22">
          <span class="card-num">Câu 22</span>
          <div class="interactive-text">她又聪明又热情，大家都喜欢她。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Tā yòu cōngming yòu rèqíng, dàjiā dōu xǐhuan tā.</div>
              <div>Cô ấy vừa thông minh lại vừa nhiệt tình, mọi người đều yêu mến cô ấy.</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('22', 'A')" data-q="22" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('22', 'B')" data-q="22" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('22', 'C')" data-q="22" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('22', 'D')" data-q="22" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('22', 'F')" data-q="22" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('22')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('22')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-22"></div>
        </div>

        <!-- Câu 23 -->
        <div class="card" id="q-23">
          <span class="card-num">Câu 23</span>
          <div class="interactive-text">太甜了，你吃吧。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Tài tián le, nǐ chī ba.</div>
              <div>Ngọt quá đi, anh ăn đi nhé.</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('23', 'A')" data-q="23" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('23', 'B')" data-q="23" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('23', 'C')" data-q="23" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('23', 'D')" data-q="23" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('23', 'F')" data-q="23" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('23')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('23')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-23"></div>
        </div>

        <!-- Câu 24 -->
        <div class="card" id="q-24">
          <span class="card-num">Câu 24</span>
          <div class="interactive-text">我又累又饿，你让我休息一下吧。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Wǒ yòu lèi yòu è, nǐ ràng wǒ xiūxi yíxià ba.</div>
              <div>Anh vừa mệt lại vừa đói, em để anh nghỉ ngơi một lát đi.</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('24', 'A')" data-q="24" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('24', 'B')" data-q="24" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('24', 'C')" data-q="24" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('24', 'D')" data-q="24" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('24', 'F')" data-q="24" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('24')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('24')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-24"></div>
        </div>

        <!-- Câu 25 -->
        <div class="card" id="q-25">
          <span class="card-num">Câu 25</span>
          <div class="interactive-text">有点儿饿，我去超市买点儿吃的。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Yǒudiǎnr è, wǒ qù chāoshì mǎi diǎnr chī de.</div>
              <div>Hơi đói một chút, mình đi siêu thị mua tí đồ ăn.</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('25', 'A')" data-q="25" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('25', 'B')" data-q="25" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('25', 'C')" data-q="25" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('25', 'D')" data-q="25" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('25', 'F')" data-q="25" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('25')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('25')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-25"></div>
        </div>
      </section>

      <!-- PHẦN 2: CÂU 26 - 30 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 26 - 30 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu điền từ vào chỗ trống</span>
        </div>
        <p class="section-desc">Yêu cầu: 选择合适的词语填空 (Chọn từ thích hợp trong khung điền vào chỗ trống):</p>

        <!-- Ngân hàng từ vựng A - F -->
        <div class="reading-vocab-box">
          <div class="reading-vocab-title">NGÂN HÀNG TỪ VỰNG (A - F):</div>
          <div class="reading-vocab-grid">
            <div class="reading-vocab-item"><span class="vocab-letter">A</span> <strong>努力</strong> (nǔlì - nỗ lực, chăm chỉ)</div>
            <div class="reading-vocab-item"><span class="vocab-letter">B</span> <strong>回答</strong> (huídá - trả lời)</div>
            <div class="reading-vocab-item"><span class="vocab-letter">C</span> <strong>照片</strong> (zhàopiàn - bức ảnh)</div>
            <div class="reading-vocab-item"><span class="vocab-letter">D</span> <strong>比赛</strong> (bǐsài - trận đấu, thi đấu)</div>
            <div class="reading-vocab-item" style="opacity:0.7;"><span class="vocab-letter">E</span> <strong>声音</strong> (Ví dụ: shēngyīn - âm thanh, giọng)</div>
            <div class="reading-vocab-item"><span class="vocab-letter">F</span> <strong>客人</strong> (kèrén - khách hàng, khách)</div>
          </div>
        </div>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="interactive-text">例如：她说话的 ( E ) 多好听啊！</span>
            <span class="pinyin-line">Lìrú: Tā shuōhuà de ( E ) duō hǎotīng a!</span>
            <span class="trans-line">Ví dụ: Giọng nói của cô ấy nghe hay biết bao!</span>
          </div>
          <div class="options-grid grid-vocab" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">E</span> 声音 √</div>
          </div>
        </div>

        <!-- Câu 26 -->
        <div class="card" id="q-26">
          <span class="card-num">Câu 26</span>
          <div class="interactive-text">今天晚上我晚点儿回来，跟朋友去看足球 <span id="blank-display-26" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Jīntiān wǎnshang wǒ wǎndiǎnr huílái, gēn péngyou qù kàn zúqiú bǐsài.</div>
              <div>Tối nay tôi về muộn một chút, cùng bạn đi xem thi đấu bóng đá.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('26', 'A', '努力')" data-q="26" data-val="A"><span class="chip-letter">A</span> 努力</div>
            <div class="option-chip" onclick="selectOption('26', 'B', '回答')" data-q="26" data-val="B"><span class="chip-letter">B</span> 回答</div>
            <div class="option-chip" onclick="selectOption('26', 'C', '照片')" data-q="26" data-val="C"><span class="chip-letter">C</span> 照片</div>
            <div class="option-chip" onclick="selectOption('26', 'D', '比赛')" data-q="26" data-val="D"><span class="chip-letter">D</span> 比赛</div>
            <div class="option-chip" onclick="selectOption('26', 'F', '客人')" data-q="26" data-val="F"><span class="chip-letter">F</span> 客人</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('26')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('26')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-26"></div>
        </div>

        <!-- Câu 27 -->
        <div class="card" id="q-27">
          <span class="card-num">Câu 27</span>
          <div class="interactive-text">弟弟回家就复习，学习非常 <span id="blank-display-27" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Dìdi huíjiā jiù fùxí, xuéxí fēicháng nǔlì.</div>
              <div>Em trai về đến nhà là ôn bài, học tập vô cùng chăm chỉ.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('27', 'A', '努力')" data-q="27" data-val="A"><span class="chip-letter">A</span> 努力</div>
            <div class="option-chip" onclick="selectOption('27', 'B', '回答')" data-q="27" data-val="B"><span class="chip-letter">B</span> 回答</div>
            <div class="option-chip" onclick="selectOption('27', 'C', '照片')" data-q="27" data-val="C"><span class="chip-letter">C</span> 照片</div>
            <div class="option-chip" onclick="selectOption('27', 'D', '比赛')" data-q="27" data-val="D"><span class="chip-letter">D</span> 比赛</div>
            <div class="option-chip" onclick="selectOption('27', 'F', '客人')" data-q="27" data-val="F"><span class="chip-letter">F</span> 客人</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('27')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('27')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-27"></div>
        </div>

        <!-- Câu 28 -->
        <div class="card" id="q-28">
          <span class="card-num">Câu 28</span>
          <div class="interactive-text">家里来 <span id="blank-display-28" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 了，你回来的时候去超市买点儿水果。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Jiā li lái kèrén le, nǐ huílái de shíhou qù chāoshì mǎi diǎnr shuǐguǒ.</div>
              <div>Nhà có khách đến chơi rồi, lúc con về thì ghé siêu thị mua ít hoa quả nhé.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('28', 'A', '努力')" data-q="28" data-val="A"><span class="chip-letter">A</span> 努力</div>
            <div class="option-chip" onclick="selectOption('28', 'B', '回答')" data-q="28" data-val="B"><span class="chip-letter">B</span> 回答</div>
            <div class="option-chip" onclick="selectOption('28', 'C', '照片')" data-q="28" data-val="C"><span class="chip-letter">C</span> 照片</div>
            <div class="option-chip" onclick="selectOption('28', 'D', '比赛')" data-q="28" data-val="D"><span class="chip-letter">D</span> 比赛</div>
            <div class="option-chip" onclick="selectOption('28', 'F', '客人')" data-q="28" data-val="F"><span class="chip-letter">F</span> 客人</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('28')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('28')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-28"></div>
        </div>

        <!-- Câu 29 -->
        <div class="card" id="q-29">
          <span class="card-num">Câu 29</span>
          <div class="interactive-text">
            A: 这是我们爬山的 <span id="blank-display-29" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>，你看看。<br>
            B: 这个站在你旁边的人是谁？
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">A: Zhè shì wǒmen páshān de zhàopiàn, nǐ kànkan. B: Zhè ge zhàn zài nǐ pángbiān de rén shì shéi?</div>
              <div>A: Đây là ảnh chúng mình đi leo núi, cậu xem này. B: Người đứng bên cạnh cậu là ai thế?</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('29', 'A', '努力')" data-q="29" data-val="A"><span class="chip-letter">A</span> 努力</div>
            <div class="option-chip" onclick="selectOption('29', 'B', '回答')" data-q="29" data-val="B"><span class="chip-letter">B</span> 回答</div>
            <div class="option-chip" onclick="selectOption('29', 'C', '照片')" data-q="29" data-val="C"><span class="chip-letter">C</span> 照片</div>
            <div class="option-chip" onclick="selectOption('29', 'D', '比赛')" data-q="29" data-val="D"><span class="chip-letter">D</span> 比赛</div>
            <div class="option-chip" onclick="selectOption('29', 'F', '客人')" data-q="29" data-val="F"><span class="chip-letter">F</span> 客人</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('29')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('29')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-29"></div>
        </div>

        <!-- Câu 30 -->
        <div class="card" id="q-30">
          <span class="card-num">Câu 30</span>
          <div class="interactive-text">
            A: 你觉得今天的考试怎么样？<br>
            B: 很多问题我都不会 <span id="blank-display-30" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>。
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">A: Nǐ juéde jīntiān de kǎoshì zěnmeyàng? B: Hěn duō wèntí wǒ dōu bú huì huídá.</div>
              <div>A: Cậu thấy bài thi hôm nay thế nào? B: Rất nhiều câu hỏi tôi đều không biết trả lời.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('30', 'A', '努力')" data-q="30" data-val="A"><span class="chip-letter">A</span> 努力</div>
            <div class="option-chip" onclick="selectOption('30', 'B', '回答')" data-q="30" data-val="B"><span class="chip-letter">B</span> 回答</div>
            <div class="option-chip" onclick="selectOption('30', 'C', '照片')" data-q="30" data-val="C"><span class="chip-letter">C</span> 照片</div>
            <div class="option-chip" onclick="selectOption('30', 'D', '比赛')" data-q="30" data-val="D"><span class="chip-letter">D</span> 比赛</div>
            <div class="option-chip" onclick="selectOption('30', 'F', '客人')" data-q="30" data-val="F"><span class="chip-letter">F</span> 客人</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('30')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('30')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-30"></div>
        </div>
      </section>

      <!-- PHẦN 3: CÂU 31 - 35 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第三部分: 第 31 - 35 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Đọc hiểu đoạn văn ngắn &amp; chọn đáp án</span>
        </div>
        <p class="section-desc">Yêu cầu: 阅读短文，选择正确答案 (Đọc đoạn văn ngắn, chọn câu trả lời đúng A, B hoặc C):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="reading-passage-box interactive-text">
            您是来参加今天会议的吗？您来早了一点儿，现在才八点半。您先进来坐吧。
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 会议最可能几点开始？
          </div>
          <div class="options-grid grid-abc" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip"><span class="chip-letter">A</span> 8点</div>
            <div class="option-chip"><span class="chip-letter">B</span> 8点半</div>
            <div class="option-chip selected"><span class="chip-letter">C</span> 9点 √</div>
          </div>
        </div>

        <!-- Câu 31 -->
        <div class="card" id="q-31">
          <span class="card-num">Câu 31</span>
          <div class="reading-passage-box interactive-text">
            这张照片是我姐姐11岁那年照的，那时她正在读五年级，照片上的姐姐又黑又瘦。看看现在的姐姐，又高又漂亮，大家都喜欢她。
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 姐姐：
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('31', 'A')" data-q="31" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size:17px;">现在又高又漂亮</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('31', 'B')" data-q="31" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size:17px;">很喜欢大家</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('31', 'C')" data-q="31" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size:17px;">现在读五年级</span></div>
            </div>
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhè zhāng zhàopiàn shì wǒ jiějie 11 suì nà nián zhào de, nà shí tā zhèngzài dú wǔ niánjí, zhàopiàn shang de jiějie yòu hēi yòu shòu. Kànkan xiànzài de jiějie, yòu gāo yòu piàoliang, dàjiā dōu xǐhuan tā.</div>
              <div style="margin-bottom:8px;"><strong>Dịch đoạn văn:</strong> Bức ảnh này chụp vào năm chị gái tôi 11 tuổi, hồi đó chị đang học lớp năm, chị gái trong ảnh vừa đen vừa gầy. Nhìn chị gái bây giờ xem, vừa cao vừa xinh đẹp, ai cũng yêu mến chị.</div>
              <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:6px; font-size:13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 现在又高又漂亮</strong> (Xiànzài yòu gāo yòu piàoliang): Bây giờ vừa cao vừa xinh đẹp<br>
                &bull; <strong>B. 很喜欢大家</strong> (Hěn xǐhuan dàjiā): Rất thích mọi người<br>
                &bull; <strong>C. 现在读五年级</strong> (Xiànzài dú wǔ niánjí): Hiện tại đang học lớp năm<br>
              </div>
            </div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('31')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('31')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-31"></div>
        </div>

        <!-- Câu 32 -->
        <div class="card" id="q-32">
          <span class="card-num">Câu 32</span>
          <div class="reading-passage-box interactive-text">
            3月15号早上，她正要去上班的时候，看见男朋友拿着鲜花站在门口，她一下想到了，今天是她的生日。
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 根据这段话，可以知道：
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('32', 'A')" data-q="32" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size:17px;">她那天不上班</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('32', 'B')" data-q="32" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size:17px;">男朋友要送她花</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('32', 'C')" data-q="32" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size:17px;">她记得男朋友的生日</span></div>
            </div>
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Sān yuè shíwǔ hào zǎoshang, tā zhèng yào qù shàngbān de shíhou, kànjiàn nánpéngyou názhe xiānhuā zhàn zài ménkǒu, tā yíxià xiǎngdào le, jīntiān shì tā de shēngrì.</div>
              <div style="margin-bottom:8px;"><strong>Dịch đoạn văn:</strong> Sáng ngày 15 tháng 3, khi cô ấy chuẩn bị đi làm thì nhìn thấy bạn trai đang cầm bó hoa tươi đứng ở cửa, cô ấy lập tức nhớ ra ngay, hôm nay là sinh nhật của mình.</div>
              <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:6px; font-size:13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 她那天不上班</strong> (Tā nà tiān bù shàngbān): Hôm đó cô ấy không đi làm<br>
                &bull; <strong>B. 男朋友要送她花</strong> (Nánpéngyou yào sòng tā huā): Bạn trai muốn tặng hoa cho cô ấy<br>
                &bull; <strong>C. 她记得男朋友的生日</strong> (Tā jìde nánpéngyou de shēngrì): Cô ấy nhớ sinh nhật của bạn trai<br>
              </div>
            </div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('32')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('32')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-32"></div>
        </div>

        <!-- Câu 33 -->
        <div class="card" id="q-33">
          <span class="card-num">Câu 33</span>
          <div class="reading-passage-box interactive-text">
            客人有问题的时候，她总是热情回答。客人喜欢这样的服务员，经理也喜欢这样的服务员。
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 根据这段话，可以知道：
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('33', 'A')" data-q="33" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size:17px;">客人很热情</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('33', 'B')" data-q="33" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size:17px;">大家都喜欢这个服务员</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('33', 'C')" data-q="33" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size:17px;">经理喜欢回答问题</span></div>
            </div>
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Kèrén yǒu wèntí de shíhou, tā zǒngshì rèqíng huídá. Kèrén xǐhuan zhèyàng de fúwùyuán, jīnglǐ yě xǐhuan zhèyàng de fúwùyuán.</div>
              <div style="margin-bottom:8px;"><strong>Dịch đoạn văn:</strong> Khi khách hàng có câu hỏi, cô ấy luôn nhiệt tình trả lời. Khách hàng thích nhân viên phục vụ như thế này, giám đốc cũng thích nhân viên phục vụ như vậy.</div>
              <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:6px; font-size:13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 客人很热情</strong> (Kèrén hěn rèqíng): Khách hàng rất nhiệt tình<br>
                &bull; <strong>B. 大家都喜欢这个服务员</strong> (Dàjiā dōu xǐhuan zhè ge fúwùyuán): Mọi người đều thích cô nhân viên phục vụ này<br>
                &bull; <strong>C. 经理喜欢回答问题</strong> (Jīnglǐ xǐhuan huídá wèntí): Giám đốc thích trả lời câu hỏi<br>
              </div>
            </div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('33')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('33')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-33"></div>
        </div>

        <!-- Câu 34 -->
        <div class="card" id="q-34">
          <span class="card-num">Câu 34</span>
          <div class="reading-passage-box interactive-text">
            王老师有个20岁的女儿，现在读大学三年级，又聪明又漂亮，学习也很努力。
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 王老师的女儿：
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('34', 'A')" data-q="34" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size:17px;">很年轻</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('34', 'B')" data-q="34" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size:17px;">是老师</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('34', 'C')" data-q="34" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size:17px;">喜欢笑</span></div>
            </div>
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Wáng lǎoshī yǒu ge 20 suì de nǚ'ér, xiànzài dú dàxué sān niánjí, yòu cōngming yòu piàoliang, xuéxí yě hěn nǔlì.</div>
              <div style="margin-bottom:8px;"><strong>Dịch đoạn văn:</strong> Thầy Vương có một cô con gái 20 tuổi, hiện đang học năm thứ ba đại học, vừa thông minh vừa xinh đẹp, học tập cũng rất chăm chỉ.</div>
              <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:6px; font-size:13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 很年轻</strong> (Hěn niánqīng): Rất trẻ tuổi<br>
                &bull; <strong>B. 是老师</strong> (Shì lǎoshī): Là giáo viên<br>
                &bull; <strong>C. 喜欢笑</strong> (Xǐhuan xiào): Thích cười<br>
              </div>
            </div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('34')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('34')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-34"></div>
        </div>

        <!-- Câu 35 -->
        <div class="card" id="q-35">
          <span class="card-num">Câu 35</span>
          <div class="reading-passage-box interactive-text">
            他姓高，但是长得不高，只有一米六。朋友们都说：“我们就叫你小高吧！”他笑着回答：“可以，大家都这么叫我。”
          </div>
          <div class="reading-question-title interactive-text">
            &bull; 他：
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('35', 'A')" data-q="35" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size:17px;">又高又胖</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('35', 'B')" data-q="35" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size:17px;">姓高，也长得高</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('35', 'C')" data-q="35" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size:17px;">喜欢小高这个名字</span></div>
            </div>
          </div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Tā xìng Gāo, dànshì zhǎng de bù gāo, zhǐ yǒu yì mǐ liù. Péngyoumen dōu shuō: “Wǒmen jiù jiào nǐ Xiǎo Gāo ba!” Tā xiàozhe huídá: “Kěyǐ, dàjiā dōu zhème jiào wǒ.”</div>
              <div style="margin-bottom:8px;"><strong>Dịch đoạn văn:</strong> Anh ấy họ Cao, nhưng dáng người lại không cao, chỉ cao một mét sáu. Bạn bè đều nói: "Tụi mình gọi cậu là Tiểu Cao nhé!" Anh ấy cười đáp: "Được chứ, mọi người đều gọi tớ như thế mà."</div>
              <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:6px; font-size:13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 又高又胖</strong> (Yòu gāo yòu pàng): Vừa cao vừa béo<br>
                &bull; <strong>B. 姓高，也长得高</strong> (Xìng Gāo, yě zhǎng de gāo): Họ Cao và người cũng cao<br>
                &bull; <strong>C. 喜欢小高这个名字</strong> (Xǐhuan Xiǎo Gāo zhè ge míngzi): Thích cái tên Tiểu Cao này<br>
              </div>
            </div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('35')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('35')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-35"></div>
        </div>
      </section>'''

# ==============================================================================
# TAB 3: BÀI VIẾT (WRITING: Q36 - Q45)
# ==============================================================================
tab3_content = '''      <div class="global-toolbar">
        <button class="tool-btn active" id="btnTogglePinyinWriting" onclick="toggleGlobalPinyin()">Ẩn / Hiện Pinyin</button>
        <button class="tool-btn active" id="btnToggleTransWriting" onclick="toggleGlobalTrans()">Ẩn / Hiện Dịch Nghĩa</button>
      </div>

      <!-- PHẦN 1: CÂU 36 - 40 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 36 - 40 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Sắp xếp từ ngữ thành câu hoàn chỉnh</span>
        </div>
        <p class="section-desc">Yêu cầu: 连词成句 (Sắp xếp các từ ngữ rời rạc phân cách bởi dấu '/' thành một câu đúng ngữ pháp):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">小船 / 上 / 一 / 河 / 条 / 有</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án mẫu &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">河上有一条小船。</div>
            <div class="sentence-pinyin-full">Hé shang yǒu yì tiáo xiǎochuán.</div>
            <div>Trên sông có một chiếc thuyền nhỏ.</div>
          </div>
        </div>

        <!-- Câu 36 -->
        <div class="card">
          <span class="card-num">Câu 36</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">女儿 / 聪明 / 他的 / 非常</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">他的女儿非常聪明。</div>
            <div class="sentence-pinyin-full">Tā de nǚ'ér fēicháng cōngming.</div>
            <div>Con gái của anh ấy vô cùng thông minh.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Chủ ngữ [他的女儿] + Phó từ mức độ [非常] + Vị ngữ tính từ [聪明].</div>
          </div>
        </div>

        <!-- Câu 37 -->
        <div class="card">
          <span class="card-num">Câu 37</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">服务员 / 热情 / 的 / 都很 / 这家饭馆</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">这家饭馆的服务员都很热情。</div>
            <div class="sentence-pinyin-full">Zhè jiā fànguǎn de fúwùyuán dōu hěn rèqíng.</div>
            <div>Nhân viên phục vụ của quán ăn này đều rất nhiệt tình.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Cụm chủ ngữ định tâm [这家饭馆的服务员] + [都很] + [热情].</div>
          </div>
        </div>

        <!-- Câu 38 -->
        <div class="card">
          <span class="card-num">Câu 38</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">超市 / 哪家 / 买蛋糕 / 你去</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">你去哪家超市买蛋糕？</div>
            <div class="sentence-pinyin-full">Nǐ qù nǎ jiā chāoshì mǎi dàngāo?</div>
            <div>Bạn đi siêu thị nào để mua bánh ngọt thế?</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Câu liên động: Chủ ngữ [你] + [去 + Nơi chốn: 哪家超市] + [Mục đích: 买蛋糕].</div>
          </div>
        </div>

        <!-- Câu 39 -->
        <div class="card">
          <span class="card-num">Câu 39</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">站着 / 总是 / 吃饭 / 他</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">他总是站着吃饭。</div>
            <div class="sentence-pinyin-full">Tā zǒngshì zhànzhe chī fàn.</div>
            <div>Anh ấy lúc nào cũng đứng ăn cơm.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Trạng thái đi kèm: [总是] + [V1+着: 站着] + [V2: 吃饭].</div>
          </div>
        </div>

        <!-- Câu 40 -->
        <div class="card">
          <span class="card-num">Câu 40</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">回答 / 你去 / 一下 / 客人的问题</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">你去回答一下客人的问题。</div>
            <div class="sentence-pinyin-full">Nǐ qù huídá yíxià kèrén de wèntí.</div>
            <div>Bạn qua trả lời giải đáp câu hỏi của khách hàng một lát nhé.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Câu cầu khiến: [你去] + [Động từ: 回答] + [一下] + [Tân ngữ: 客人的问题].</div>
          </div>
        </div>
      </section>

      <!-- PHẦN 2: CÂU 41 - 45 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 41 - 45 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Nhìn phiên âm Pinyin, điền chữ Hán</span>
        </div>
        <p class="section-desc">Yêu cầu: 看拼音，写汉字 (Căn cứ vào phiên âm trong ngoặc đơn, điền chữ Hán chính xác vào chỗ trống):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            没（ guān ）系，别难过，高兴点儿。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Không sao đâu, đừng buồn, vui lên chút đi.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">关</span> <span class="sentence-pinyin-full">(guān)</span> - Hán Việt: Quan</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>没关系</strong> (méi guānxi: không sao cả).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">没关系，别难过，高兴点儿。</div>
          </div>
        </div>

        <!-- Câu 41 -->
        <div class="card">
          <span class="card-num">Câu 41</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            小明，快回家吧！你家来（ kè ）人了。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Tiểu Minh, mau về nhà đi! Nhà bạn có khách đến chơi rồi kìa.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">客</span> <span class="sentence-pinyin-full">(kè)</span> - Hán Việt: Khách</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>客人</strong> (kèrén: khách khứa, khách quý).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">小明，快回家吧！你家来客（kè）人了。</div>
          </div>
        </div>

        <!-- Câu 42 -->
        <div class="card">
          <span class="card-num">Câu 42</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            周老师的儿子今年上小学三年（ jí ）。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Con trai thầy Chu năm nay lên học lớp ba tiểu học.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">级</span> <span class="sentence-pinyin-full">(jí)</span> - Hán Việt: Cấp</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>年级</strong> (niánjí: lớp, năm học).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">周老师的儿子今年上小学三年级（jí）。</div>
          </div>
        </div>

        <!-- Câu 43 -->
        <div class="card">
          <span class="card-num">Câu 43</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            他工作很（ rèn ）真，经理很喜欢他。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Anh ấy làm việc rất nghiêm túc, giám đốc rất quý anh ấy.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">认</span> <span class="sentence-pinyin-full">(rèn)</span> - Hán Việt: Nhận</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>认真</strong> (rènzhēn: nghiêm túc, cẩn thận).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">他工作很认（rèn）真，经理很喜欢他。</div>
          </div>
        </div>

        <!-- Câu 44 -->
        <div class="card">
          <span class="card-num">Câu 44</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            你看，这是我年轻时的照（ piàn ），漂亮吗？
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Cậu xem, đây là ảnh hồi trẻ của mình đấy, xinh không?</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">片</span> <span class="sentence-pinyin-full">(piàn)</span> - Hán Việt: Phiến</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>照片</strong> (zhàopiàn: bức ảnh, tấm hình).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">你看，这是我年轻时的照片（piàn），漂亮吗？</div>
          </div>
        </div>

        <!-- Câu 45 -->
        <div class="card">
          <span class="card-num">Câu 45</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            那个拿着书（ zhàn ）在门口的就是我们的老师。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Người cầm quyển sách đứng ở cửa kia chính là giáo viên của chúng tôi.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">站</span> <span class="sentence-pinyin-full">(zhàn)</span> - Hán Việt: Trạm</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>站在</strong> (zhànzài: đứng tại, đứng ở).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">那个拿着书站（zhàn）在门口的就是我们的老师。</div>
          </div>
        </div>
      </section>'''

# ==============================================================================
# TAB 4: SÁCH GIÁO KHOA (TEXTBOOK: VOCAB, GRAMMAR, WORD FORMATION, POLYPHONIC)
# Strictly NO "Bài khóa"!
# ==============================================================================
tab4_content = '''      <!-- PHẦN 1: 16 TỪ MỚI CHÍNH THỨC SGK -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>生词: 16 Từ mới Sách Giáo Khoa (Trang 48 - 49)</span></div>
          <span style="font-size:13px; color:var(--accent);">HSK 3 Sách Giáo Khoa &bull; Bài 4</span>
        </div>
        <p class="section-desc">Toàn bộ 16 từ vựng mới chính thức của Bài 4 kèm từ loại, pinyin và nghĩa tiếng Việt chuẩn xác:</p>

        <table class="vocab-table">
          <thead>
            <tr>
              <th style="width: 50px;">STT</th>
              <th>Chữ Hán</th>
              <th>Pinyin</th>
              <th>Từ loại</th>
              <th>Ý nghĩa tiếng Việt</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">比赛</td>
              <td style="color: #38bdf8; font-weight: 600;">bǐsài</td>
              <td style="color: #a78bfa; font-size: 13px;">danh / động</td>
              <td>trận thi đấu, cuộc thi; thi đấu (足球比赛: trận đấu bóng đá)</td>
            </tr>
            <tr>
              <td>2</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">照片</td>
              <td style="color: #38bdf8; font-weight: 600;">zhàopiàn</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>bức ảnh, tấm hình (一张照片: một tấm ảnh; 照照片: chụp ảnh)</td>
            </tr>
            <tr>
              <td>3</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">年级</td>
              <td style="color: #38bdf8; font-weight: 600;">niánjí</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>năm học, lớp (cấp bậc học: 二年级: lớp hai; 三年级: năm thứ ba)</td>
            </tr>
            <tr>
              <td>4</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">又</td>
              <td style="color: #38bdf8; font-weight: 600;">yòu</td>
              <td style="color: #a78bfa; font-size: 13px;">phó từ</td>
              <td>vừa... lại vừa...; lại (又大又甜: vừa to vừa ngọt; 又来: lại đến)</td>
            </tr>
            <tr>
              <td>5</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">聪明</td>
              <td style="color: #38bdf8; font-weight: 600;">cōngming</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>thông minh, sáng dạ (很聪明: rất thông minh)</td>
            </tr>
            <tr>
              <td>6</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">热情</td>
              <td style="color: #38bdf8; font-weight: 600;">rèqíng</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>nhiệt tình, niềm nở, hiếu khách (热情招待; 对人热情)</td>
            </tr>
            <tr>
              <td>7</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">努力</td>
              <td style="color: #38bdf8; font-weight: 600;">nǔlì</td>
              <td style="color: #a78bfa; font-size: 13px;">tính / động</td>
              <td>chăm chỉ, nỗ lực, cố gắng (学习努力: học tập chăm chỉ; 努力工作)</td>
            </tr>
            <tr>
              <td>8</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">总是</td>
              <td style="color: #38bdf8; font-weight: 600;">zǒngshì</td>
              <td style="color: #a78bfa; font-size: 13px;">phó từ</td>
              <td>luôn luôn, lúc nào cũng (总是笑着: lúc nào cũng cười; 总是迟到)</td>
            </tr>
            <tr>
              <td>9</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">回答</td>
              <td style="color: #38bdf8; font-weight: 600;">huídá</td>
              <td style="color: #a78bfa; font-size: 13px;">động từ</td>
              <td>trả lời, giải đáp (回答问题: trả lời câu hỏi)</td>
            </tr>
            <tr>
              <td>10</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">站</td>
              <td style="color: #38bdf8; font-weight: 600;">zhàn</td>
              <td style="color: #a78bfa; font-size: 13px;">động / danh</td>
              <td>đứng; trạm, bến (站着: đang đứng; 火车站: ga xe lửa)</td>
            </tr>
            <tr>
              <td>11</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">饿</td>
              <td style="color: #38bdf8; font-weight: 600;">è</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>đói, đói bụng (肚子饿: đói bụng; 我太饿了: tôi đói quá rồi)</td>
            </tr>
            <tr>
              <td>12</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">超市</td>
              <td style="color: #38bdf8; font-weight: 600;">chāoshì</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>siêu thị (去超市买东西: đi siêu thị mua sắm)</td>
            </tr>
            <tr>
              <td>13</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">蛋糕</td>
              <td style="color: #38bdf8; font-weight: 600;">dàngāo</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>bánh ngọt, bánh kem (一块蛋糕: một miếng bánh; 生日蛋糕: bánh sinh nhật)</td>
            </tr>
            <tr>
              <td>14</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">年轻</td>
              <td style="color: #38bdf8; font-weight: 600;">niánqīng</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>trẻ trung, trẻ tuổi (很年轻: rất trẻ; 年轻人: người trẻ tuổi)</td>
            </tr>
            <tr>
              <td>15</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">认真</td>
              <td style="color: #38bdf8; font-weight: 600;">rènzhēn</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>nghiêm túc, chăm chỉ, cẩn thận (认真学习; 认真工作)</td>
            </tr>
            <tr>
              <td>16</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">客人</td>
              <td style="color: #38bdf8; font-weight: 600;">kèrén</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>khách khứa, khách quý, khách hàng (家里来客人: nhà có khách tới)</td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- PHẦN 2: 2 CHỦ ĐIỂM NGỮ PHÁP CHÍNH THỨC SGK -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>注释: 2 Điểm Ngữ Pháp Trọng Tâm SGK (Trang 50 - 51)</span></div>
          <span style="font-size:13px; color:var(--accent);">Quy tắc &amp; Ví dụ nguyên bản</span>
        </div>

        <!-- Ngữ pháp 1 -->
        <div class="grammar-card">
          <div class="grammar-title">1. Cấu trúc miêu tả nhiều đặc điểm: “又……又……”</div>
          <div class="grammar-formula">
            Chủ ngữ + 又 + Tính từ / Động từ 1 + 又 + Tính từ / Động từ 2
          </div>
          <div class="grammar-desc">
            Cấu trúc <strong>“又……又……”</strong> dùng để liên kết hai tính từ hoặc động từ có tính chất đồng nhất (cùng mang nghĩa tích cực hoặc cùng mang nghĩa tiêu cực), biểu thị hai trạng thái/đặc điểm cùng tồn tại đồng thời (vừa... lại vừa...).<br>
            &bull; <em>Lưu ý:</em> Hai từ ghép với “又……又……” thường có cùng xu hướng ngữ nghĩa (ví dụ: 又大又甜 - vừa to vừa ngọt; không nói 又大又难吃).
          </div>
          <div style="font-size: 13px; color: var(--text-sub); margin-bottom: 8px; font-weight: bold;">Các câu ví dụ chuẩn SGK:</div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(1) 这个西瓜又大又甜。</div>
            <div class="example-pinyin">Zhè ge xīguā yòu dà yòu tián.</div>
            <div class="example-vi">Quả dưa hấu này vừa to lại vừa ngọt.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(2) 那个女孩子又聪明又漂亮。</div>
            <div class="example-pinyin">Nà ge nǚháizi yòu cōngming yòu piàoliang.</div>
            <div class="example-vi">Cô bạn gái kia vừa thông minh lại vừa xinh xắn.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(3) 她又聪明又热情，大家都喜欢她。</div>
            <div class="example-pinyin">Tā yòu cōngming yòu rèqíng, dàjiā dōu xǐhuan tā.</div>
            <div class="example-vi">Cô ấy vừa thông minh lại vừa nhiệt tình, mọi người đều yêu quý cô ấy.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(4) 我又累又饿，你让我休息一下吧。</div>
            <div class="example-pinyin">Wǒ yòu lèi yòu è, nǐ ràng wǒ xiūxi yíxià ba.</div>
            <div class="example-vi">Anh vừa mệt lại vừa đói, em để anh nghỉ ngơi một chút đi.</div>
          </div>
        </div>

        <!-- Ngữ pháp 2 -->
        <div class="grammar-card">
          <div class="grammar-title">2. Cấu trúc động tác/trạng thái đi kèm: Động từ 1 + 着 + Động từ 2</div>
          <div class="grammar-formula">
            Chủ ngữ + Động từ 1 + 着 (+ Tân ngữ 1) + Động từ 2 (+ Tân ngữ 2)
          </div>
          <div class="grammar-desc">
            Trong tiếng Hán, cấu trúc <strong>“Động từ 1 + 着 + Động từ 2”</strong> biểu thị <em>Động tác 1</em> diễn ra như phương thức, tư thế hoặc trạng thái đệm đi kèm của <em>Động tác 2</em> (làm hành động 2 trong khi duy trì tư thế hoặc trạng thái của hành động 1).<br>
            &bull; Động tác 1 thường là các động tác chỉ tư thế như: <strong>笑 (cười), 站 (đứng), 坐 (ngồi), 躺 (nằm), 拿 (cầm)</strong>.
          </div>
          <div style="font-size: 13px; color: var(--text-sub); margin-bottom: 8px; font-weight: bold;">Các câu ví dụ chuẩn SGK:</div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(1) 她总是笑着跟客人说话。</div>
            <div class="example-pinyin">Tā zǒngshì xiàozhe gēn kèrén shuōhuà.</div>
            <div class="example-vi">Cô ấy luôn mỉm cười khi nói chuyện với khách hàng. (Trạng thái cười đi kèm hành động nói chuyện)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(2) 他们站着聊天儿。</div>
            <div class="example-pinyin">Tāmen zhànzhe liáotiānr.</div>
            <div class="example-vi">Họ đứng trò chuyện. (Tư thế đứng đi kèm hành động trò chuyện)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(3) 弟弟吃着苹果看电视。</div>
            <div class="example-pinyin">Dìdi chīzhe píngguǒ kàn diànshì.</div>
            <div class="example-vi">Em trai vừa ăn táo vừa xem tivi.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(4) 你怎么总是坐着看电视，也不帮我做饭？</div>
            <div class="example-pinyin">Nǐ zěnme zǒngshì zuòzhe kàn diànshì, yě bù bāng wǒ zuò fàn?</div>
            <div class="example-vi">Sao anh lúc nào cũng ngồi xem tivi, cũng chẳng giúp em nấu cơm?</div>
          </div>
        </div>
      </section>

      <!-- PHẦN 3: GHÉP TỪ CŨ TẠO TỪ MỚI & TỤC NGỮ TRUYỀN THỐNG -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>汉字与俗语: Ghép từ cũ tạo từ mới &amp; Tục ngữ (Trang 54 - 55)</span></div>
          <span style="font-size:13px; color:var(--accent);">Mở rộng kiến thức ngôn ngữ SGK</span>
        </div>

        <!-- Mở rộng chữ Hán -->
        <div style="margin-bottom: 20px;">
          <h4 style="color:#38bdf8; margin-bottom: 10px; font-size:15px;">1. 旧字新词: Cách thành lập từ mới từ các chữ Hán đã học</h4>
          <p class="section-desc">Cơ chế tư duy cấu tạo từ ghép trong tiếng Trung giúp ghi nhớ từ vựng siêu nhanh:</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">客人 + 房间 &rarr; 客房</div>
              <div style="color: #38bdf8; font-size: 13px;">kè fáng</div>
              <div style="font-size: 13px; color: var(--text-sub);">Phòng dành cho khách, phòng khách sạn (客人: khách + 房间: phòng).</div>
            </div>
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">生日 + 蛋糕 &rarr; 生日蛋糕</div>
              <div style="color: #38bdf8; font-size: 13px;">shēngrì dàngāo</div>
              <div style="font-size: 13px; color: var(--text-sub);">Bánh sinh nhật (生日: sinh nhật + 蛋糕: bánh ngọt/bánh kem).</div>
            </div>
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">比赛 + 场地 &rarr; 赛场</div>
              <div style="color: #38bdf8; font-size: 13px;">sài chǎng</div>
              <div style="font-size: 13px; color: var(--text-sub);">Sân thi đấu, sàn đấu, đấu trường (比赛: thi đấu + 场地: sân bãi).</div>
            </div>
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">新鲜 + 花 &rarr; 鲜花</div>
              <div style="color: #38bdf8; font-size: 13px;">xiān huā</div>
              <div style="font-size: 13px; color: var(--text-sub);">Hoa tươi (新鲜: tươi mới + 花: bông hoa).</div>
            </div>
          </div>
        </div>

        <!-- Tục ngữ truyền thống -->
        <div>
          <h4 style="color:#fbbf24; margin-bottom: 10px; font-size:15px;">2. 俗语: Tục ngữ Trung Hoa truyền thống</h4>
          <div class="card" style="border-left: 3px solid #fbbf24; background: rgba(251, 191, 36, 0.05);">
            <div class="interactive-text" style="font-size: 20px; font-weight: bold; color: #fbbf24;">笑一笑，十年少；愁一愁，白了头。</div>
            <div class="sentence-pinyin-full" style="color: #fde68a;">Xiào yí xiào, shí nián shào; chóu yì chóu, bái le tóu.</div>
            <div style="margin: 8px 0; font-size: 14px; color: #fff;">
              <strong>Dịch nghĩa tiếng Việt:</strong> "Một nụ cười bằng mười thang thuốc bổ; một nỗi âu sầu bạc cả mái đầu."
            </div>
            <div style="font-size: 13px; color: var(--text-sub); line-height: 1.6;">
              <strong>Ý nghĩa và ứng dụng:</strong> Câu tục ngữ khuyên mọi người hãy luôn giữ tinh thần lạc quan, vui vẻ, nụ cười rạng rỡ trên môi sẽ giúp con người trẻ lâu, tăng cường sức khỏe và kéo dài tuổi thanh xuân; ngược lại nếu suốt ngày lo âu, rầu rĩ thì sẽ rất mau già nua, bạc cả mái đầu.
            </div>
          </div>
        </div>
      </section>

      <!-- PHẦN 4: CHỮ ĐA ÂM TỰ TRỌNG TÂM -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>多音字: Chữ đa âm tự trọng tâm trong bài</span></div>
          <span style="font-size:13px; color:var(--accent);">Phát âm &amp; Ngữ cảnh sử dụng</span>
        </div>
        <p class="section-desc">Các chữ Hán có nhiều âm đọc quan trọng xuất hiện trong Bài 4:</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
          <!-- Chữ 着 -->
          <div class="card" style="border-top: 3px solid #f59e0b;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="interactive-text" style="font-size: 24px; font-weight: bold; color: #f59e0b;">着</span>
              <span style="font-size:12px; color:var(--text-sub);">Hán Việt: Trứ / Trước</span>
            </div>
            <div style="font-size: 13px; margin-bottom: 6px;">
              <span style="color:#38bdf8; font-weight:bold;">1. [ zhe ]</span>: Trợ từ động thái biểu thị trạng thái đang tiếp diễn hoặc duy trì tư thế (như: <strong>笑着</strong> - đang cười, <strong>站着</strong> - đang đứng, <strong>拿着</strong> - đang cầm, <strong>坐着</strong> - đang ngồi).
            </div>
            <div style="font-size: 13px;">
              <span style="color:#38bdf8; font-weight:bold;">2. [ zháo ]</span>: Động từ biểu thị đạt được mục tiêu, cảm giác sốt ruột (như: <strong>着急</strong> - sốt ruột, lo lắng; <strong>睡着</strong> - ngủ thiếp đi).
            </div>
          </div>

          <!-- Chữ 长 -->
          <div class="card" style="border-top: 3px solid #f59e0b;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="interactive-text" style="font-size: 24px; font-weight: bold; color: #f59e0b;">长</span>
              <span style="font-size:12px; color:var(--text-sub);">Hán Việt: Trưởng / Trường</span>
            </div>
            <div style="font-size: 13px; margin-bottom: 6px;">
              <span style="color:#38bdf8; font-weight:bold;">1. [ zhǎng ]</span>: Động từ: sinh trưởng, lớn lên, vẻ bề ngoài (như: <strong>长大</strong> - lớn lên, <strong>长得漂亮</strong> - trông rất xinh xắn, <strong>长高</strong> - cao lên).
            </div>
            <div style="font-size: 13px;">
              <span style="color:#38bdf8; font-weight:bold;">2. [ cháng ]</span>: Tính từ: dài về khoảng cách hoặc thời gian (như: <strong>很长</strong> - rất dài, <strong>长时间</strong> - thời gian dài, <strong>长城</strong> - Vạn Lý Trường Thành).
            </div>
          </div>
        </div>
      </section>'''

# ==============================================================================
# QUIZ DATA FOR Q21 - Q35 (READING TAB)
# ==============================================================================
quiz_data = {
    "1": {"ans": "C", "explain": "Người nam nói: 我去看足球比赛 (Tôi đi xem thi đấu bóng đá), ứng với Hình C."},
    "2": {"ans": "F", "explain": "Hỏi về hai cô gái 笑着看照片 (cười xem ảnh), tương ứng với Hình F."},
    "3": {"ans": "B", "explain": "Nhắc đến 吃块蛋糕 (ăn miếng bánh ngọt), tương ứng với Hình B."},
    "4": {"ans": "E", "explain": "Nhắc đến 总是站着 (lúc nào cũng đứng nói chuyện), tương ứng với Hình E."},
    "5": {"ans": "A", "explain": "Nhắc đến 超市的西瓜 (dưa hấu ở siêu thị), tương ứng với Hình A."},
    "6": {"ans": "√", "explain": "Đúng (√). Người mẹ nói '总是不爱吃东西' (không chịu ăn đồ ăn) đồng nghĩa với việc bạn ấy ăn rất ít."},
    "7": {"ans": "√", "explain": "Đúng (√). Vừa thông minh vừa nỗ lực lại trả lời được mọi câu hỏi của giáo viên chứng tỏ cậu ấy học rất giỏi."},
    "8": {"ans": "√", "explain": "Đúng (√). Chỉ còn 1 đồng 1 hào 1 xu (khoảng 1.11 tệ) thì rõ ràng tiền trong điện thoại không còn nhiều."},
    "9": {"ans": "×", "explain": "Sai (×). Bài nghe nói '大家有问题都会来找她' (mọi người có vấn đề đều đến tìm mẹ giúp), chứ không phải mẹ có vấn đề."},
    "10": {"ans": "√", "explain": "Đúng (√). Câu '谁能告诉我...' (ai có thể nói cho thầy biết...) chính là hành động mời học sinh trả lời câu hỏi."},
    "11": {"ans": "A", "explain": "Đáp án đúng là A. Người nữ khuyên: '别听了，认真写吧' (Đừng nghe nữa, nghiêm túc làm bài tập đi)."},
    "12": {"ans": "C", "explain": "Đáp án đúng là C. Người nữ dặn: '你下了班就回来吧' (Anh tan làm thì về nhà ngay nhé)."},
    "13": {"ans": "B", "explain": "Đáp án đúng là B. Người nam đáp: '我们要去看球赛' (Chúng mình đi xem đấu bóng)."},
    "14": {"ans": "B", "explain": "Đáp án đúng là B. Người nữ xác nhận đi du học nước ngoài: '是啊，我爸妈也想让我去'."},
    "15": {"ans": "C", "explain": "Đáp án đúng là C. Người nữ không nghe hiểu câu hỏi nên không thể trả lời được (不能回答)."},
    "16": {"ans": "A", "explain": "Đáp án đúng là A. Người cha khen con trai: '很努力，每天都复习写作业' đồng nghĩa với '学习很认真'."},
    "17": {"ans": "A", "explain": "Đáp án đúng là A. Cô gái nói '你看我那时多瘦啊' (hồi đó em gầy thế nào), suy ra hiện tại cô ấy đã mập hơn (现在胖了)."},
    "18": {"ans": "C", "explain": "Đáp án đúng là C. Người nam nhận xét: '小周又漂亮又热情'."},
    "19": {"ans": "C", "explain": "Đáp án đúng là C. Đoạn thoại nhắc đến: '你看照片放在这儿怎么样？' (xem ảnh đặt ở đây thế nào), tức là họ đang chỉnh vị trí bức ảnh (放照片)."},
    "20": {"ans": "A", "explain": "Đáp án đúng là A. Người nam chốt lại: '我们走着去超市买点儿菜' (chúng mình đi bộ ra siêu thị mua ít thức ăn/rau)."},
    "21": {"ans": "F", "explain": "Đáp án đúng là F. Câu 21 hỏi: '老师的问题你怎么都不回答？' (Sao câu hỏi của thầy giáo bạn đều không trả lời?) -> Phù hợp nhất là F: '我昨天没有认真复习。' (Hôm qua mình không ôn bài cẩn thận)."},
    "22": {"ans": "C", "explain": "Đáp án đúng là C. Câu 22 nói: '她又聪明又热情，大家都喜欢她。' (Cô ấy vừa thông minh vừa nhiệt tình, mọi người đều quý) -> Đáp lại câu hỏi C: '你觉得小丽怎么样？' (Cậu thấy Tiểu Lệ thế nào?)."},
    "23": {"ans": "A", "explain": "Đáp án đúng là A. Câu 23 nói: '太甜了，你吃吧。' (Ngọt quá, anh ăn đi) -> Đáp lại câu hỏi A: '你怎么没吃我给你买的蛋糕呢？' (Sao em không ăn chiếc bánh ngọt anh mua cho em thế?)."},
    "24": {"ans": "B", "explain": "Đáp án đúng là B. Câu 24 phân trần: '我又累又饿，你让我休息一下吧。' (Anh vừa mệt lại vừa đói, em để anh nghỉ ngơi một chút đi) -> Phù hợp với câu B: '你怎么到家就坐着看电视，也不帮我做饭？' (Sao anh vừa về đến nhà là ngồi xem tivi, cũng chẳng giúp em nấu cơm?)."},
    "25": {"ans": "D", "explain": "Đáp án đúng là D. Câu 25 trả lời: '有点儿饿，我去超市买点儿吃的。' (Hơi đói một chút, mình đi siêu thị mua tí đồ ăn) -> Phù hợp với câu D: '这么晚了，你去哪儿？' (Muộn thế này rồi, cậu đi đâu đấy?)."},
    "26": {"ans": "D", "explain": "Đáp án đúng là D (比赛 - bǐsài: trận thi đấu). Kết hợp thành cụm từ '足球比赛' (trận thi đấu bóng đá)."},
    "27": {"ans": "A", "explain": "Đáp án đúng là A (努力 - nǔlì: nỗ lực, chăm chỉ). Kết hợp với động từ '学习' thành cụm '学习非常努力' (học tập vô cùng chăm chỉ)."},
    "28": {"ans": "F", "explain": "Đáp án đúng là F (客人 - kèrén: khách quý, khách khứa). Kết hợp thành cụm '家里来客人了' (nhà có khách đến chơi)."},
    "29": {"ans": "C", "explain": "Đáp án đúng là C (照片 - zhàopiàn: bức ảnh). Người A đưa cho xem và người B hỏi người đứng bên cạnh là ai, chứng tỏ đó là bức ảnh đi leo núi (爬山的照片)."},
    "30": {"ans": "B", "explain": "Đáp án đúng là B (回答 - huídá: trả lời). Kết hợp với '问题' thành '很多问题我都不会回答' (rất nhiều câu hỏi tôi đều không biết trả lời)."},
    "31": {"ans": "A", "explain": "Đáp án đúng là A (现在又高又漂亮). Đoạn văn viết: '看看现在的姐姐，又高又漂亮，大家都喜欢她。'"},
    "32": {"ans": "B", "explain": "Đáp án đúng là B (男朋友要送她花). Đoạn văn kể bạn trai cầm hoa tươi đứng ở cửa vào đúng ngày sinh nhật của cô ấy."},
    "33": {"ans": "B", "explain": "Đáp án đúng là B (大家都喜欢这个服务员). Đoạn văn nêu: '客人喜欢这样的服务员，经理也喜欢这样的服务员。'"},
    "34": {"ans": "A", "explain": "Đáp án đúng là A (很年轻). Đoạn văn nêu cô con gái mới 20 tuổi (20岁), đang học đại học năm ba nên rất trẻ."},
    "35": {"ans": "C", "explain": "Đáp án đúng là C (喜欢小高这个名字). Đoạn văn nêu anh ấy cười và vui vẻ đồng ý: '可以，大家都这么叫我。'"}
}

# MULTITONE DATA
multitone = {
    "着": [
        {"py": "zhe", "vi": "Trợ từ ngữ thái biểu thị duy trì trạng thái hoặc tư thế đi kèm (放着, 坐着, 笑着, 站着, 拿着)"},
        {"py": "zháo", "vi": "Động từ đạt kết quả, cảm xúc (着急: sốt ruột, 睡着: ngủ say)"}
    ],
    "长": [
        {"py": "zhǎng", "vi": "Động từ: sinh trưởng, lớn lên, trông vẻ ngoài (长大, 长得漂亮, 长高)"},
        {"py": "cháng", "vi": "Tính từ: dài về cự ly, khoảng cách hoặc thời gian (很长, 长时间, 长城)"}
    ],
    "只": [
        {"py": "zhǐ", "vi": "Phó từ: chỉ, duy chỉ (只有, 只要, 只有一米六)"},
        {"py": "zhī", "vi": "Lượng từ: con vật, một chiếc trong đôi (一只小狗, 一只鸟)"}
    ],
    "会": [
        {"py": "huì", "vi": "Động từ năng nguyện: biết (会说, 会回答), sẽ (会下雨), hội nghị (开会)"},
        {"py": "kuài", "vi": "Kế toán (会计)"}
    ]
}

# ==============================================================================
# DICTIONARY LOADING & EXTENSION FOR LESSON 4
# ==============================================================================
# Load base dictionary from Bai_03/index.html
with open('Bai_03/index.html', 'r', encoding='utf-8') as f:
    c_b3 = f.read()

m_dict = re.search(r'const DICT = (\{.*?\});', c_b3)
base_dict = json.loads(m_dict.group(1)) if m_dict else {}

# Specific dictionary additions for Lesson 4
l4_dict_additions = {
    "赛": {"py": "sài", "hv": "Tái", "vi": "Thi đấu, tranh tài (比赛, 球赛)"},
    "比": {"py": "bǐ", "hv": "Tỉ", "vi": "So sánh; thi đấu (比较, 比赛)"},
    "照": {"py": "zhào", "hv": "Chiếu", "vi": "Soi, chiếu; chụp ảnh (照片, 照顾)"},
    "片": {"py": "piàn", "hv": "Phiến", "vi": "Mảnh, tấm, bức (照片, 一片)"},
    "级": {"py": "jí", "hv": "Cấp", "vi": "Bậc, lớp, cấp bậc (年级, 三年级)"},
    "又": {"py": "yòu", "hv": "Hựu", "vi": "Lại; vừa... vừa... (又大又甜, 又来)"},
    "聪": {"py": "cōng", "hv": "Thông", "vi": "Thính tai; sáng dạ (聪明)"},
    "明": {"py": "míng", "hv": "Minh", "vi": "Sáng sủa; rõ ràng (聪明, 明天, 明白)"},
    "热": {"py": "rè", "hv": "Nhiệt", "vi": "Nóng; nhiệt huyết (热情, 太热)"},
    "情": {"py": "qíng", "hv": "Tình", "vi": "Tình cảm, tình ý (热情, 事情)"},
    "努": {"py": "nǔ", "hv": "Nỗ", "vi": "Cố sức, gượng (努力)"},
    "力": {"py": "lì", "hv": "Lực", "vi": "Sức lực, sức mạnh (努力, 力量)"},
    "总": {"py": "zǒng", "hv": "Tổng", "vi": "Luôn luôn; toàn bộ (总是, 总共, 总经理)"},
    "答": {"py": "dá", "hv": "Đáp", "vi": "Trả lời, đáp lại (回答, 答案)"},
    "站": {"py": "zhàn", "hv": "Trạm", "vi": "Đứng; bến, trạm xe (站着, 火车站)"},
    "饿": {"py": "è", "hv": "Ngạ", "vi": "Đói, đói bụng (肚子饿, 好饿)"},
    "超": {"py": "chāo", "hv": "Siêu", "vi": "Vượt bậc, siêu đẳng (超市, 超级)"},
    "市": {"py": "shì", "hv": "Thị", "vi": "Chợ, thị trường, thành phố (超市, 城市)"},
    "蛋": {"py": "dàn", "hv": "Đãn", "vi": "Trứng (鸡蛋, 蛋糕)"},
    "糕": {"py": "gāo", "hv": "Cao", "vi": "Bánh hấp, bánh ngọt (蛋糕, 年糕)"},
    "轻": {"py": "qīng", "hv": "Khinh", "vi": "Nhẹ; trẻ tuổi (年轻, 很轻)"},
    "认": {"py": "rèn", "hv": "Nhận", "vi": "Nhận biết; chăm chỉ (认真, 认识)"},
    "真": {"py": "zhēn", "hv": "Chân", "vi": "Thật, chân thật (认真, 真正, 真漂亮)"},
    "客": {"py": "kè", "hv": "Khách", "vi": "Khách khứa, khách hàng (客人, 请客, 客房)"},
    "瘦": {"py": "shòu", "hv": "Sấu", "vi": "Gầy, ốm (又黑又瘦)"},
    "鲜": {"py": "xiān", "hv": "Tiên", "vi": "Tươi, mới (新鲜, 鲜花)"},
    "笑": {"py": "xiào", "hv": "Tiếu", "vi": "Cười, mỉm cười (笑着, 笑一笑)"},
    "短": {"py": "duǎn", "hv": "Đoản", "vi": "Ngắn (短对话, 短文)"},
    "句": {"py": "jù", "hv": "Cú", "vi": "Câu (句子, 连词成句)"},
    "段": {"py": "duàn", "hv": "Đoạn", "vi": "Đoạn văn, quãng (短文, 一段时间)"},
    "各": {"py": "gè", "hv": "Các", "vi": "Mỗi, từng (各个, 各自)"},
    "分": {"py": "fēn", "hv": "Phân", "vi": "Phút; xu; chia phân (几分钟, 一分钱, 分开)"},
    "角": {"py": "jiǎo", "hv": "Giác", "vi": "Góc; đồng hào tiền tệ (一角钱, 三角形)"},
    "高": {"py": "gāo", "hv": "Cao", "vi": "Họ Cao; cao ráo (小高, 很高, 又高又漂亮)"},
    "差": {"py": "chà", "hv": "Sai", "vi": "Kém, thiếu hụt (差不多, 成绩差)", "poly": True},
    "绍": {"py": "shào", "hv": "Thiệu", "vi": "Nối dõi; giới thiệu (介绍)"},
    "介": {"py": "jiè", "hv": "Giới", "vi": "Ở giữa; giới thiệu (介绍)"},
    "腿": {"py": "tuǐ", "hv": "Thối", "vi": "Chân, cẳng chân (腿疼, 大腿)"},
    "疼": {"py": "téng", "hv": "Đông", "vi": "Đau, nhức (腿疼, 头疼)"},
    "运": {"py": "yùn", "hv": "Vận", "vi": "Vận động, vận chuyển (运动, 运行)"},
    "动": {"py": "dòng", "hv": "Động", "vi": "Hoạt động, cử động (运动, 动手)"},
    "甜": {"py": "tián", "hv": "Điềm", "vi": "Ngọt ngào, vị ngọt (太甜了, 又大又甜)"},
    "品": {"py": "pǐn", "hv": "Phẩm", "vi": "Vật phẩm, món đồ (甜品, 商品)"},
    "男": {"py": "nán", "hv": "Nam", "vi": "Nam giới, đàn ông (男朋友, 男生)"},
    "友": {"py": "yǒu", "hv": "Hữu", "vi": "Bạn bè (朋友, 男朋友)"},
    "房": {"py": "fáng", "hv": "Phòng", "vi": "Căn phòng, nhà (客房, 房间)"},
    "场": {"py": "chǎng", "hv": "Trường", "vi": "Sân bãi, sàn đấu (赛场, 场地)"},
    "地": {"py": "dì", "hv": "Địa", "vi": "Đất, nơi chốn (场地, 地方)"},
    "俗": {"py": "sú", "hv": "Tục", "vi": "Tục ngữ, phong tục (俗语, 风俗)"},
    "少": {"py": "shào", "hv": "Thiếu", "vi": "Trẻ tuổi (十年少); ít (shǎo)", "poly": True},
    "米": {"py": "mǐ", "hv": "Mễ", "vi": "Mét (đơn vị đo); hạt gạo (一米六, 大米)"},
    "精": {"py": "jīng", "hv": "Tinh", "vi": "Tinh hoa, xuất sắc (精彩)"},
    "彩": {"py": "cǎi", "hv": "Thải", "vi": "Màu sắc, rực rỡ (精彩, 彩色)"},
    "合": {"py": "hé", "hv": "Hợp", "vi": "Hợp tác, chụp chung (合影, 合适)"},
    "影": {"py": "yǐng", "hv": "Ảnh", "vi": "Hình bóng, tấm ảnh (合影, 电影)"},
    "全": {"py": "quán", "hv": "Toàn", "vi": "Toàn bộ, tất cả (全家, 全体)"},
    "号": {"py": "hào", "hv": "Hào / Hiệu", "vi": "Ngày; số, mã số (3月15号, 几号)"},
    "往": {"py": "wǎng", "hv": "Vãng", "vi": "Hướng về, về phía (往右边, 往前走)"}
}

base_dict.update(l4_dict_additions)

# ==============================================================================
# ASSEMBLE HTML PAGE VIA TEMPLATE MASTER
# ==============================================================================
output = template
output = output.replace('{{LESSON_NUM}}', '4')
output = output.replace('{{LESSON_TITLE}}', '她总是笑着跟客人说话。')
output = output.replace('{{LESSON_SUBTITLE}}', 'Tā zǒngshì xiàozhe gēn kèrén shuōhuà - Cô ấy luôn cười khi nói chuyện với khách hàng')
output = output.replace('{{AUDIO_SRC}}', 'audio.mp3')
output = output.replace('{{AUDIO_JUMP_BUTTONS}}', jump_buttons)
output = output.replace('{{TAB1_CONTENT}}', tab1_content)
output = output.replace('{{TAB2_CONTENT}}', tab2_content)
output = output.replace('{{TAB3_CONTENT}}', tab3_content)
output = output.replace('{{TAB4_CONTENT}}', tab4_content)
output = output.replace('{{DICT_JSON}}', json.dumps(base_dict, ensure_ascii=False))
output = output.replace('{{MULTITONE_JSON}}', json.dumps(multitone, ensure_ascii=False))
output = output.replace('{{QUIZ_DATA_JSON}}', json.dumps(quiz_data, ensure_ascii=False))

# Write to Bai_04/index.html
with open('Bai_04/index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print('Successfully generated Bai_04/index.html via Master Template!')
print('File size:', len(output), 'bytes')
