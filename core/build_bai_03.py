import sys, os, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Read Master Template
with open('core/template_master.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Jump buttons for Bài 3
jump_buttons = '''          <button class="jump-btn" onclick="jumpAudio(0)">▶ 00:00 Mở đầu</button>
          <button class="jump-btn" onclick="jumpAudio(40)">▶ 00:40 Phần 1 (1-5)</button>
          <button class="jump-btn" onclick="jumpAudio(190)">▶ 03:10 Phần 2 (6-10)</button>
          <button class="jump-btn" onclick="jumpAudio(430)">▶ 07:10 Phần 3 (11-15)</button>
          <button class="jump-btn" onclick="jumpAudio(675)">▶ 11:15 Phần 4 (16-20)</button>'''

# TAB 1: BÀI NGHE
tab1_content = '''      <div class="global-toolbar">
        <button class="tool-btn active" id="btnTogglePinyin" onclick="toggleGlobalPinyin()">Ẩn / Hiện Pinyin</button>
        <button class="tool-btn active" id="btnToggleTrans" onclick="toggleGlobalTrans()">Ẩn / Hiện Dịch Nghĩa</button>
      </div>

      <!-- PHẦN 1 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 1 - 5 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại &amp; tranh minh họa</span>
        </div>
        <p class="section-desc">Yêu cầu: 听对话，选择与对话内容一致的图片 (Nghe đối thoại, chọn tranh tương ứng A - F):</p>

        <!-- Tranh ảnh A-F -->
        <div class="pics-grid">
          <div class="pic-item"><img src="pic_A.png" alt="Tranh A"><div class="pic-label">Hình A: Áo sơ mi treo móc (衬衫)</div></div>
          <div class="pic-item"><img src="pic_B.png" alt="Tranh B"><div class="pic-label">Hình B: Canh / Đồ uống (汤 / 饮料)</div></div>
          <div class="pic-item"><img src="pic_C.png" alt="Tranh C"><div class="pic-label">Hình C: Đĩa hoa quả (水果)</div></div>
          <div class="pic-item"><img src="pic_D.png" alt="Tranh D"><div class="pic-label">Hình D (Ví dụ): Gọi điện thoại (打电话)</div></div>
          <div class="pic-item"><img src="pic_E.png" alt="Tranh E"><div class="pic-label">Hình E: Vali / Sân bay (坐飞机 / 出差)</div></div>
          <div class="pic-item"><img src="pic_F.png" alt="Tranh F"><div class="pic-label">Hình F: Chiếc quần tây (一条裤子)</div></div>
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
            <span class="interactive-text">这条裤子怎么样？</span>
            <span class="pinyin-line">Zhè tiáo kùzi zěnmeyàng?</span>
            <span class="trans-line">Chiếc quần này thế nào?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我觉得有点儿长。</span>
            <span class="pinyin-line">Wǒ juéde yǒudiǎnr cháng.</span>
            <span class="trans-line">Anh thấy hơi dài một chút.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(1, 'A')"><span class="chip-letter">A</span> Hình A: Áo sơ mi</div>
            <div class="option-chip" onclick="selectOption(1, 'B')"><span class="chip-letter">B</span> Hình B: Canh/Đồ uống</div>
            <div class="option-chip" onclick="selectOption(1, 'C')"><span class="chip-letter">C</span> Hình C: Đĩa hoa quả</div>
            <div class="option-chip" onclick="selectOption(1, 'D')"><span class="chip-letter">D</span> Hình D: Gọi điện thoại</div>
            <div class="option-chip" onclick="selectOption(1, 'E')"><span class="chip-letter">E</span> Hình E: Vali/Sân bay</div>
            <div class="option-chip" onclick="selectOption(1, 'F')"><span class="chip-letter">F</span> Hình F: Chiếc quần</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(1)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(1)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(1)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-1">
            <div class="sentence-pinyin-full">Nǚ: Zhè tiáo kùzi zěnmeyàng? - Nán: Wǒ juéde yǒudiǎnr cháng.</div>
            <strong>Dịch nghĩa:</strong> Nữ: Chiếc quần này thế nào? - Nam: Anh thấy hơi dài một chút.<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>F</strong>: Nhắc trực tiếp đến "这条裤子" (chiếc quần này).
          </div>
          <div class="feedback-box" id="feedback-1"></div>
        </div>

        <!-- Câu 2 -->
        <div class="card" id="card-2">
          <span class="card-num">Câu 2</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你想喝点儿什么？茶还是咖啡？</span>
            <span class="pinyin-line">Nǐ xiǎng hē diǎnr shénme? Chá háishì kāfēi?</span>
            <span class="trans-line">Em muốn uống chút gì? Trà hay cà phê?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">给我一杯茶吧。</span>
            <span class="pinyin-line">Gěi wǒ yì bēi chá ba.</span>
            <span class="trans-line">Cho em một cốc trà nhé.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(2, 'A')"><span class="chip-letter">A</span> Hình A: Áo sơ mi</div>
            <div class="option-chip" onclick="selectOption(2, 'B')"><span class="chip-letter">B</span> Hình B: Canh/Đồ uống</div>
            <div class="option-chip" onclick="selectOption(2, 'C')"><span class="chip-letter">C</span> Hình C: Đĩa hoa quả</div>
            <div class="option-chip" onclick="selectOption(2, 'D')"><span class="chip-letter">D</span> Hình D: Gọi điện thoại</div>
            <div class="option-chip" onclick="selectOption(2, 'E')"><span class="chip-letter">E</span> Hình E: Vali/Sân bay</div>
            <div class="option-chip" onclick="selectOption(2, 'F')"><span class="chip-letter">F</span> Hình F: Chiếc quần</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(2)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(2)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(2)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-2">
            <div class="sentence-pinyin-full">Nán: Nǐ xiǎng hē diǎnr shénme? Chá háishì kāfēi? - Nǚ: Gěi wǒ yì bēi chá ba.</div>
            <strong>Dịch nghĩa:</strong> Nam: Em muốn uống chút gì? Trà hay cà phê? - Nữ: Cho em một cốc trà nhé.<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>B</strong>: Hỏi đồ uống và gọi một cốc trà.
          </div>
          <div class="feedback-box" id="feedback-2"></div>
        </div>

        <!-- Câu 3 -->
        <div class="card" id="card-3">
          <span class="card-num">Câu 3</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">先生，这些衣服都是您的吗？</span>
            <span class="pinyin-line">Xiānsheng, zhèxiē yīfu dōu shì nín de ma?</span>
            <span class="trans-line">Thưa ông, những bộ quần áo này đều là của ông sao?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">是，一共六件衬衫。</span>
            <span class="pinyin-line">Shì, yígòng liù jiàn chènshān.</span>
            <span class="trans-line">Đúng vậy, tổng cộng 6 chiếc áo sơ mi.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(3, 'A')"><span class="chip-letter">A</span> Hình A: Áo sơ mi</div>
            <div class="option-chip" onclick="selectOption(3, 'B')"><span class="chip-letter">B</span> Hình B: Canh/Đồ uống</div>
            <div class="option-chip" onclick="selectOption(3, 'C')"><span class="chip-letter">C</span> Hình C: Đĩa hoa quả</div>
            <div class="option-chip" onclick="selectOption(3, 'D')"><span class="chip-letter">D</span> Hình D: Gọi điện thoại</div>
            <div class="option-chip" onclick="selectOption(3, 'E')"><span class="chip-letter">E</span> Hình E: Vali/Sân bay</div>
            <div class="option-chip" onclick="selectOption(3, 'F')"><span class="chip-letter">F</span> Hình F: Chiếc quần</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(3)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(3)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(3)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-3">
            <div class="sentence-pinyin-full">Nǚ: Xiānsheng, zhèxiē yīfu dōu shì nín de ma? - Nán: Shì, yígòng liù jiàn chènshān.</div>
            <strong>Dịch nghĩa:</strong> Nữ: Thưa ông, những bộ quần áo này đều là của ông sao? - Nam: Vâng, tổng cộng sáu chiếc áo sơ mi.<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>A</strong>: Bức tranh các chiếc áo sơ mi treo trên móc.
          </div>
          <div class="feedback-box" id="feedback-3"></div>
        </div>

        <!-- Câu 4 -->
        <div class="card" id="card-4">
          <span class="card-num">Câu 4</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">下午我们买点儿水果吧。</span>
            <span class="pinyin-line">Xiàwǔ wǒmen mǎi diǎnr shuǐguǒ ba.</span>
            <span class="trans-line">Chiều nay chúng mình đi mua ít hoa quả nhé.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">好啊，家里只有一个苹果了。</span>
            <span class="pinyin-line">Hǎo a, jiā li zhǐ yǒu yí ge píngguǒ le.</span>
            <span class="trans-line">Được thôi, ở nhà chỉ còn mỗi một quả táo thôi.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(4, 'A')"><span class="chip-letter">A</span> Hình A: Áo sơ mi</div>
            <div class="option-chip" onclick="selectOption(4, 'B')"><span class="chip-letter">B</span> Hình B: Canh/Đồ uống</div>
            <div class="option-chip" onclick="selectOption(4, 'C')"><span class="chip-letter">C</span> Hình C: Đĩa hoa quả</div>
            <div class="option-chip" onclick="selectOption(4, 'D')"><span class="chip-letter">D</span> Hình D: Gọi điện thoại</div>
            <div class="option-chip" onclick="selectOption(4, 'E')"><span class="chip-letter">E</span> Hình E: Vali/Sân bay</div>
            <div class="option-chip" onclick="selectOption(4, 'F')"><span class="chip-letter">F</span> Hình F: Chiếc quần</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(4)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(4)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(4)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-4">
            <div class="sentence-pinyin-full">Nán: Xiàwǔ wǒmen mǎi diǎnr shuǐguǒ ba. - Nǚ: Hǎo a, jiā li zhǐ yǒu yí ge píngguǒ le.</div>
            <strong>Dịch nghĩa:</strong> Nam: Chiều nay chúng mình mua ít hoa quả nhé. - Nữ: Được thôi, ở nhà chỉ còn mỗi quả táo.<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>C</strong>: Tranh hoa quả trái cây tươi.
          </div>
          <div class="feedback-box" id="feedback-4"></div>
        </div>

        <!-- Câu 5 -->
        <div class="card" id="card-5">
          <span class="card-num">Câu 5</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你什么时候去北京？</span>
            <span class="pinyin-line">Nǐ shénme shíhou qù Běijīng?</span>
            <span class="trans-line">Khi nào anh đi Bắc Kinh?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">明天上午的飞机。</span>
            <span class="pinyin-line">Míngtiān shàngwǔ de fēijī.</span>
            <span class="trans-line">Chuyến bay sáng mai.</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(5, 'A')"><span class="chip-letter">A</span> Hình A: Áo sơ mi</div>
            <div class="option-chip" onclick="selectOption(5, 'B')"><span class="chip-letter">B</span> Hình B: Canh/Đồ uống</div>
            <div class="option-chip" onclick="selectOption(5, 'C')"><span class="chip-letter">C</span> Hình C: Đĩa hoa quả</div>
            <div class="option-chip" onclick="selectOption(5, 'D')"><span class="chip-letter">D</span> Hình D: Gọi điện thoại</div>
            <div class="option-chip" onclick="selectOption(5, 'E')"><span class="chip-letter">E</span> Hình E: Vali/Sân bay</div>
            <div class="option-chip" onclick="selectOption(5, 'F')"><span class="chip-letter">F</span> Hình F: Chiếc quần</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(5)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(5)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(5)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-5">
            <div class="sentence-pinyin-full">Nǚ: Nǐ shénme shíhou qù Běijīng? - Nán: Míngtiān shàngwǔ de fēijī.</div>
            <strong>Dịch nghĩa:</strong> Nữ: Khi nào anh đi Bắc Kinh? - Nam: Máy bay sáng ngày mai.<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>E</strong>: Bức tranh người kéo vali lên máy bay đi công tác/du lịch.
          </div>
          <div class="feedback-box" id="feedback-5"></div>
        </div>
      </section>

      <!-- PHẦN 2 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 6 - 10 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu nhận định &amp; phán đoán Đúng/Sai (√ / ×)</span>
        </div>
        <p class="section-desc">Yêu cầu: 听句子，判断对错 (Nghe câu nói, phán đoán đúng sai dựa vào nội dung câu nhận định):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="interactive-text">为了让自己更健康，他每天都花一个小时去锻炼身体。</span>
            <span class="pinyin-line">Wèile ràng zìjǐ gèng jiànkāng, tā měitiān dōu huā yí ge xiǎoshí qù duànliàn shēntǐ.</span>
            <span class="trans-line">Để bản thân khỏe mạnh hơn, anh ấy ngày nào cũng dành một tiếng đi rèn luyện thân thể.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 他希望自己很健康。</span> (Anh ấy hy vọng mình khỏe mạnh.)
          </div>
          <div class="options-grid grid-true-false" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">√</span> Đúng (√)</div>
          </div>
        </div>

        <!-- Câu 6 -->
        <div class="card" id="card-6">
          <span class="card-num">Câu 6</span>
          <div class="speaker-line">
            <span class="interactive-text">那个女孩儿是我的同班同学，她叫白雪，学习很好。</span>
            <span class="pinyin-line">Nàge nǚháir shì wǒ de tóngbān tóngxué, tā jiào Bái Xuě, xuéxí hěn hǎo.</span>
            <span class="trans-line">Cô bé kia là bạn học cùng lớp tôi, tên là Bạch Tuyết, học rất giỏi.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 他不认识那个女孩儿。</span> (Anh ấy không quen biết cô bé kia.)
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption(6, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption(6, '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(6)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(6)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(6)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-6">
            <div class="sentence-pinyin-full">Nàge nǚháir shì wǒ de tóngbān tóngxué, tā jiào Bái Xuě, xuéxí hěn hǎo.</div>
            <strong>Dịch nghĩa:</strong> Cô gái kia là bạn học cùng lớp của tôi, tên là Bạch Tuyết, học lực rất tốt.<br>
            <strong>Giải thích:</strong> Đáp án là <strong>× Sai</strong>: Vì là bạn cùng lớp biết rõ họ tên nên không thể nói là không quen biết.
          </div>
          <div class="feedback-box" id="feedback-6"></div>
        </div>

        <!-- Câu 7 -->
        <div class="card" id="card-7">
          <span class="card-num">Câu 7</span>
          <div class="speaker-line">
            <span class="interactive-text">这条裤子虽然有点儿贵，但是比去年买的那条便宜多了。</span>
            <span class="pinyin-line">Zhè tiáo kùzi suīrán yǒudiǎnr guì, dànshì bǐ qùnián mǎi de nà tiáo piányi duō le.</span>
            <span class="trans-line">Chiếc quần này tuy hơi đắt một chút, nhưng rẻ hơn chiếc mua năm ngoái nhiều.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 这条裤子现在便宜得多。</span> (Chiếc quần này bây giờ rẻ hơn nhiều.)
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption(7, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption(7, '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(7)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(7)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(7)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-7">
            <div class="sentence-pinyin-full">Zhè tiáo kùzi suīrán yǒudiǎnr guì, dànshì bǐ qùnián mǎi de nà tiáo piányi duō le.</div>
            <strong>Dịch nghĩa:</strong> Chiếc quần này tuy hơi đắt, nhưng rẻ hơn chiếc mua năm ngoái nhiều.<br>
            <strong>Giải thích:</strong> Đáp án là <strong>√ Đúng</strong>: Câu nói xác nhận quần này rẻ hơn chiếc năm ngoái nhiều.
          </div>
          <div class="feedback-box" id="feedback-7"></div>
        </div>

        <!-- Câu 8 -->
        <div class="card" id="card-8">
          <span class="card-num">Câu 8</span>
          <div class="speaker-line">
            <span class="interactive-text">我喜欢一边跑步一边听音乐，这样觉得不累。</span>
            <span class="pinyin-line">Wǒ xǐhuan yìbiān pǎobù yìbiān tīng yīnyuè, zhèyàng juéde bú lèi.</span>
            <span class="trans-line">Tôi thích vừa chạy bộ vừa nghe nhạc, như vậy cảm thấy không mệt.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 运动时可以听歌。</span> (Lúc vận động có thể nghe bài hát.)
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption(8, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption(8, '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(8)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(8)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(8)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-8">
            <div class="sentence-pinyin-full">Wǒ xǐhuan yìbiān pǎobù yìbiān tīng yīnyuè, zhèyàng juéde bú lèi.</div>
            <strong>Dịch nghĩa:</strong> Tôi thích vừa chạy bộ vừa nghe nhạc, như thế cảm thấy không mệt.<br>
            <strong>Giải thích:</strong> Đáp án là <strong>√ Đúng</strong>: Chạy bộ là vận động thể thao, người nói thích nghe nhạc khi chạy bộ.
          </div>
          <div class="feedback-box" id="feedback-8"></div>
        </div>

        <!-- Câu 9 -->
        <div class="card" id="card-9">
          <span class="card-num">Câu 9</span>
          <div class="speaker-line">
            <span class="interactive-text">你去超市买点儿鲜奶吧，就在进门右边放着。</span>
            <span class="pinyin-line">Nǐ qù chāoshì mǎi diǎnr xiānnǎi ba, jiù zài jìnmén yòubian fàngzhe.</span>
            <span class="trans-line">Bạn đi siêu thị mua chút sữa tươi nhé, để ngay bên phải cửa vào đấy.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 他不知道鲜奶在哪儿。</span> (Anh ấy không biết sữa tươi ở đâu.)
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption(9, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption(9, '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(9)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(9)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(9)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-9">
            <div class="sentence-pinyin-full">Nǐ qù chāoshì mǎi diǎnr xiānnǎi ba, jiù zài jìnmén yòubian fàngzhe.</div>
            <strong>Dịch nghĩa:</strong> Cậu đi siêu thị mua ít sữa tươi đi, đặt ngay ở bên phải cửa vào ấy.<br>
            <strong>Giải thích:</strong> Đáp án là <strong>× Sai</strong>: Người nói biết rất chính xác vị trí đặt sữa tươi.
          </div>
          <div class="feedback-box" id="feedback-9"></div>
        </div>

        <!-- Câu 10 -->
        <div class="card" id="card-10">
          <span class="card-num">Câu 10</span>
          <div class="speaker-line">
            <span class="interactive-text">医生让她多吃新鲜蔬菜，少吃肉，但是她还是只喜欢吃肉。</span>
            <span class="pinyin-line">Yīshēng ràng tā duō chī xīnxiān shūcài, shǎo chī ròu, dànshì tā háishì zhǐ xǐhuan chī ròu.</span>
            <span class="trans-line">Bác sĩ bảo cô ấy ăn nhiều rau tươi, bớt ăn thịt, nhưng cô ấy vẫn chỉ thích ăn thịt.</span>
          </div>
          <div class="statement-box" style="margin: 10px 0 6px; font-weight: 700; color: #fbbf24;">
            <span class="interactive-text">★ 她菜吃得很少。</span> (Cô ấy ăn rất ít rau.)
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption(10, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption(10, '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(10)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(10)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(10)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-10">
            <div class="sentence-pinyin-full">Yīshēng ràng tā duō chī xīnxiān shūcài, shǎo chī ròu, dànshì tā háishì zhǐ xǐhuan chī ròu.</div>
            <strong>Dịch nghĩa:</strong> Bác sĩ bảo cô ấy ăn nhiều rau xanh tươi, ăn ít thịt thôi, nhưng cô ấy vẫn chỉ thích ăn thịt.<br>
            <strong>Giải thích:</strong> Đáp án là <strong>√ Đúng</strong>: Vì chỉ thích ăn thịt nên rau ăn rất ít.
          </div>
          <div class="feedback-box" id="feedback-10"></div>
        </div>
      </section>

      <!-- PHẦN 3 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第三部分: 第 11 - 15 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại ngắn &amp; chọn đáp án A, B, C</span>
        </div>
        <p class="section-desc">Yêu cầu: 听短对话，选择正确答案 (Nghe đối thoại ngắn 2 lượt, chọn đáp án đúng A, B, C):</p>

        <!-- Câu 11 -->
        <div class="card" id="card-11">
          <span class="card-num">Câu 11</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">今天爬山你觉得累吗？</span>
            <span class="pinyin-line">Jīntiān páshān nǐ juéde lèi ma?</span>
            <span class="trans-line">Hôm nay leo núi bạn có thấy mệt không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">不累，就是脚有点儿疼。</span>
            <span class="pinyin-line">Bú lèi, jiù shì jiǎo yǒudiǎnr téng.</span>
            <span class="trans-line">Không mệt, chỉ là chân hơi đau một chút.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">男的怎么了？</span>
            <span class="pinyin-line">Nánde zěnme le?</span>
            <span class="trans-line">Người nam bị làm sao?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(11, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">脚不舒服</span></div>
            <div class="option-chip" onclick="selectOption(11, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">想看电视</span></div>
            <div class="option-chip" onclick="selectOption(11, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">想玩儿游戏</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(11)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(11)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(11)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-11">
            <div class="sentence-pinyin-full">Nǚ: Jīntiān páshān nǐ juéde lèi ma? - Nán: Bú lèi, jiù shì jiǎo yǒudiǎnr téng. - Wèn: Nánde zěnme le?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Hôm nay leo núi anh có mệt không? - Nam: Không mệt, chỉ là chân hơi đau. - Hỏi: Người nam sao thế?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>A</strong>: "脚有点儿疼" đồng nghĩa với "脚不舒服".
          </div>
          <div class="feedback-box" id="feedback-11"></div>
        </div>

        <!-- Câu 12 -->
        <div class="card" id="card-12">
          <span class="card-num">Câu 12</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">这里的西瓜真甜，你要吃一块儿吗？</span>
            <span class="pinyin-line">Zhèlǐ de xīguā zhēn tián, nǐ yào chī yí kuàir ma?</span>
            <span class="trans-line">Dưa hấu ở đây ngọt thật, em muốn ăn một miếng không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">太冰了，我肚子有点儿不舒服，不想吃。</span>
            <span class="pinyin-line">Tài bīng le, wǒ dùzi yǒudiǎnr bù shūfu, bù xiǎng chī.</span>
            <span class="trans-line">Lạnh quá, bụng em hơi khó chịu, không muốn ăn.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">女的为什么不吃西瓜？</span>
            <span class="pinyin-line">Nǚde wèishénme bù chī xīguā?</span>
            <span class="trans-line">Vì sao người nữ không ăn dưa hấu?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(12, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">不太甜</span></div>
            <div class="option-chip" onclick="selectOption(12, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">要睡觉</span></div>
            <div class="option-chip" onclick="selectOption(12, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">太冷了</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(12)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(12)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(12)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-12">
            <div class="sentence-pinyin-full">Nán: Zhèlǐ de xīguā zhēn tián, nǐ yào chī yí kuàir ma? - Nǚ: Tài bīng le, wǒ dùzi yǒudiǎnr bù shūfu, bù xiǎng chī. - Wèn: Nǚde wèishénme bù chī xīguā?</div>
            <strong>Dịch nghĩa:</strong> Nam: Dưa hấu ở đây ngọt lắm, em muốn ăn một miếng không? - Nữ: Lạnh quá, bụng em hơi khó chịu, không muốn ăn. - Hỏi: Vì sao người nữ không ăn dưa hấu?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>C</strong>: "太冰了" ứng với "太冷了".
          </div>
          <div class="feedback-box" id="feedback-12"></div>
        </div>

        <!-- Câu 13 -->
        <div class="card" id="card-13">
          <span class="card-num">Câu 13</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">这件白衬衫脏了，你换一件吧。</span>
            <span class="pinyin-line">Zhè jiàn bái chènshān zāng le, nǐ huàn yí jiàn ba.</span>
            <span class="trans-line">Chiếc áo sơ mi trắng này bẩn rồi, anh thay chiếc khác đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好，你帮我洗一下，我穿那件红的。</span>
            <span class="pinyin-line">Hǎo, nǐ bāng wǒ xǐ yíxià, wǒ chuān nà jiàn hóng de.</span>
            <span class="trans-line">Được, em giặt giúp anh nhé, anh mặc chiếc màu đỏ kia.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">女的要做什么？</span>
            <span class="pinyin-line">Nǚde yào zuò shénme?</span>
            <span class="trans-line">Người nữ phải làm gì?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(13, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">买裤子</span></div>
            <div class="option-chip" onclick="selectOption(13, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">洗衬衫</span></div>
            <div class="option-chip" onclick="selectOption(13, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">拿裤子</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(13)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(13)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(13)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-13">
            <div class="sentence-pinyin-full">Nǚ: Zhè jiàn bái chènshān zāng le, nǐ huàn yí jiàn ba. - Nán: Hǎo, nǐ bāng wǒ xǐ yíxià, wǒ chuān nà jiàn hóng de. - Wèn: Nǚde yào zuò shénme?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Cái áo sơ mi trắng này bẩn rồi, anh thay cái khác đi. - Nam: Được, em giặt giúp anh nhé, anh mặc cái màu đỏ kia. - Hỏi: Người nữ sẽ làm gì?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>B</strong>: Giặt áo sơ mi cho nam.
          </div>
          <div class="feedback-box" id="feedback-13"></div>
        </div>

        <!-- Câu 14 -->
        <div class="card" id="card-14">
          <span class="card-num">Câu 14</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">喂，小丽，明天是星期六，你上午有事吗？</span>
            <span class="pinyin-line">Wèi, Xiǎolì, míngtiān shì xīngqīliù, nǐ shàngwǔ yǒu shì ma?</span>
            <span class="trans-line">Alo, Tiểu Lệ, ngày mai là thứ Bảy, sáng mai bạn có bận việc gì không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">对不起，你打错了，这里没有小丽。</span>
            <span class="pinyin-line">Duìbuqǐ, nǐ dǎ cuò le, zhèlǐ méiyǒu Xiǎolì.</span>
            <span class="trans-line">Xin lỗi, bạn gọi nhầm số rồi, ở đây không có ai là Tiểu Lệ cả.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">男的怎么了？</span>
            <span class="pinyin-line">Nánde zěnme le?</span>
            <span class="trans-line">Người nam bị làm sao?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(14, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">找他去上课</span></div>
            <div class="option-chip" onclick="selectOption(14, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">不小心打错了</span></div>
            <div class="option-chip" onclick="selectOption(14, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">上午有事</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(14)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(14)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(14)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-14">
            <div class="sentence-pinyin-full">Nán: Wèi, Xiǎolì, míngtiān shì xīngqīliù, nǐ shàngwǔ yǒu shì ma? - Nǚ: Duìbuqǐ, nǐ dǎ cuò le, zhèlǐ méiyǒu Xiǎolì. - Wèn: Nánde zěnme le?</div>
            <strong>Dịch nghĩa:</strong> Nam: Alo, Tiểu Lệ, ngày mai thứ Bảy, sáng cậu bận việc gì không? - Nữ: Xin lỗi, cậu gọi nhầm rồi, ở đây không có Tiểu Lệ. - Hỏi: Người nam sao thế?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>B</strong>: Người nam gọi nhầm điện thoại.
          </div>
          <div class="feedback-box" id="feedback-14"></div>
        </div>

        <!-- Câu 15 -->
        <div class="card" id="card-15">
          <span class="card-num">Câu 15</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">桌子上面放着一杯热咖啡，是小丽的还是你的？</span>
            <span class="pinyin-line">Zhuōzi shàngmian fàngzhe yì bēi rè kāfēi, shì Xiǎolì de háishì nǐ de?</span>
            <span class="trans-line">Trên bàn đang để một cốc cà phê nóng, là của Tiểu Lệ hay của anh vậy?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">我不喝咖啡，小丽刚才放在那儿的。</span>
            <span class="pinyin-line">Wǒ bù hē kāfēi, Xiǎolì gāngcái fàng zài nàr de.</span>
            <span class="trans-line">Anh không uống cà phê, Tiểu Lệ vừa nãy đặt ở đó đấy.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">咖啡是谁的？</span>
            <span class="pinyin-line">Kāfēi shì shéi de?</span>
            <span class="trans-line">Cốc cà phê là của ai?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(15, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">男的的</span></div>
            <div class="option-chip" onclick="selectOption(15, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">女的的</span></div>
            <div class="option-chip" onclick="selectOption(15, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">小丽的</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(15)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(15)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(15)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-15">
            <div class="sentence-pinyin-full">Nǚ: Zhuōzi shàngmian fàngzhe yì bēi rè kāfēi, shì Xiǎolì de háishì nǐ de? - Nán: Wǒ bù hē kāfēi, Xiǎolì gāngcái fàng zài nàr de. - Wèn: Kāfēi shì shéi de?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Trên bàn để cốc cà phê nóng, của Tiểu Lệ hay của anh? - Nam: Anh không uống cà phê, Tiểu Lệ vừa đặt ở đó. - Hỏi: Cà phê của ai?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>C</strong>: Cà phê là của Tiểu Lệ.
          </div>
          <div class="feedback-box" id="feedback-15"></div>
        </div>
      </section>

      <!-- PHẦN 4 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第四部分: 第 16 - 20 题</span></div>
          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại dài 4 lượt &amp; chọn đáp án A, B, C</span>
        </div>
        <p class="section-desc">Yêu cầu: 听长对话，选择正确答案 (Nghe đối thoại dài 4 lượt, chọn đáp án đúng A, B, C):</p>

        <!-- Câu 16 -->
        <div class="card" id="card-16">
          <span class="card-num">Câu 16</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">你今天穿得真帅，这件衬衫是新买的？</span>
            <span class="pinyin-line">Nǐ jīntiān chuān de zhēn shuài, zhè jiàn chènshān shì xīn mǎi de?</span>
            <span class="trans-line">Hôm nay anh mặc đẹp trai thật đấy, chiếc áo sơ mi này mới mua à?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">不是，我去年买的。</span>
            <span class="pinyin-line">Bú shì, wǒ qùnián mǎi de.</span>
            <span class="trans-line">Không phải, anh mua từ năm ngoái rồi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">多少钱一件？</span>
            <span class="pinyin-line">Duōshao qián yí jiàn?</span>
            <span class="trans-line">Bao nhiêu tiền một chiếc vậy?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">两百块。</span>
            <span class="pinyin-line">Liǎng bǎi kuài.</span>
            <span class="trans-line">Hai trăm tệ.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">他们在说什么？</span>
            <span class="pinyin-line">Tāmen zài shuō shénme?</span>
            <span class="trans-line">Họ đang nói về cái gì?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(16, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">衬衫</span></div>
            <div class="option-chip" onclick="selectOption(16, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">裤子</span></div>
            <div class="option-chip" onclick="selectOption(16, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">饮料</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(16)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(16)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(16)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-16">
            <div class="sentence-pinyin-full">Nǚ: Nǐ jīntiān chuān de zhēn shuài, zhè jiàn chènshān shì xīn mǎi de? - Nán: Bú shì, wǒ qùnián mǎi de. - Nǚ: Duōshao qián yí jiàn? - Nán: Liǎng bǎi kuài. - Wèn: Tāmen zài shuō shénme?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Hôm nay anh mặc bảnh bao quá, áo sơ mi này mới mua à? - Nam: Không, anh mua năm ngoái. - Nữ: Bao nhiêu tiền một chiếc? - Nam: Hai trăm tệ. - Hỏi: Họ đang nói về cái gì?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>A</strong>: Áo sơ mi (衬衫).
          </div>
          <div class="feedback-box" id="feedback-16"></div>
        </div>

        <!-- Câu 17 -->
        <div class="card" id="card-17">
          <span class="card-num">Câu 17</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你怎么着急地找东西呢？</span>
            <span class="pinyin-line">Nǐ zěnme zháojí de zhǎo dōngxi ne?</span>
            <span class="trans-line">Sao em tìm đồ cuống cuồng lên thế?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">我记得我的手机放在桌子上了，怎么找不到了？</span>
            <span class="pinyin-line">Wǒ jìde wǒ de shǒujī fàng zài zhuōzi shang le, zěnme zhǎobúdào le?</span>
            <span class="trans-line">Em nhớ là đã để điện thoại trên bàn rồi, sao giờ lại tìm không thấy?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">你看看衣服口袋里有没有？</span>
            <span class="pinyin-line">Nǐ kànkan yīfu kǒudài li yǒu méiyǒu?</span>
            <span class="trans-line">Em xem trong túi áo có không?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">哎呀，在裤子口袋里呢。</span>
            <span class="pinyin-line">Āiyā, zài kùzi kǒudài li ne.</span>
            <span class="trans-line">Ái chà, nằm trong túi quần này.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">女的刚才在找什么？</span>
            <span class="pinyin-line">Nǚde gāngcái zài zhǎo shénme?</span>
            <span class="trans-line">Người nữ vừa nãy đang tìm cái gì?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(17, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">有问题问他</span></div>
            <div class="option-chip" onclick="selectOption(17, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">找手机</span></div>
            <div class="option-chip" onclick="selectOption(17, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">她很着急</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(17)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(17)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(17)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-17">
            <div class="sentence-pinyin-full">Nán: Nǐ zěnme zháojí de zhǎo dōngxi ne? - Nǚ: Wǒ jìde wǒ de shǒujī fàng zài zhuōzi shang le, zěnme zhǎobúdào le? - Nán: Nǐ kànkan yīfu kǒudài li yǒu méiyǒu? - Nǚ: Āiyā, zài kùzi kǒudài li ne. - Wèn: Nǚde gāngcái zài zhǎo shénme?</div>
            <strong>Dịch nghĩa:</strong> Nam: Sao em tìm đồ cuống lên thế? - Nữ: Em nhớ để điện thoại trên bàn, sao tìm không thấy? - Nam: Em xem túi áo có không? - Nữ: Ái chà, ở trong túi quần này. - Hỏi: Người nữ vừa rồi tìm cái gì?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>B</strong>: Tìm điện thoại di động (找手机).
          </div>
          <div class="feedback-box" id="feedback-17"></div>
        </div>

        <!-- Câu 18 -->
        <div class="card" id="card-18">
          <span class="card-num">Câu 18</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">外面天气真热，快喝点儿水吧。</span>
            <span class="pinyin-line">Wàimiàn tiānqì zhēn rè, kuài hē diǎnr shuǐ ba.</span>
            <span class="trans-line">Thời tiết bên ngoài nóng thật, mau uống chút nước đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">有没有冰绿茶？</span>
            <span class="pinyin-line">Yǒu méiyǒu bīng lǜchá?</span>
            <span class="trans-line">Có trà xanh ướp lạnh không em?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">没有，冰箱里放着西瓜，吃点儿西瓜吧。</span>
            <span class="pinyin-line">Méiyǒu, bīngxiāng li fàngzhe xīguā, chī diǎnr xīguā ba.</span>
            <span class="trans-line">Không có rồi, trong tủ lạnh có dưa hấu, ăn chút dưa hấu nhé.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">也好，西瓜很甜。</span>
            <span class="pinyin-line">Yě hǎo, xīguā hěn tián.</span>
            <span class="trans-line">Cũng được, dưa hấu rất ngọt.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">男的想喝什么？</span>
            <span class="pinyin-line">Nánde xiǎng hē shénme?</span>
            <span class="trans-line">Người nam muốn uống gì?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(18, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">绿茶</span></div>
            <div class="option-chip" onclick="selectOption(18, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">水果</span></div>
            <div class="option-chip" onclick="selectOption(18, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">饮料</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(18)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(18)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(18)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-18">
            <div class="sentence-pinyin-full">Nǚ: Wàimiàn tiānqì zhēn rè, kuài hē diǎnr shuǐ ba. - Nán: Yǒu méiyǒu bīng lǜchá? - Nǚ: Méiyǒu, bīngxiāng li fàngzhe xīguā, chī diǎnr xīguā ba. - Nán: Yě hǎo, xīguā hěn tián. - Wèn: Nánde xiǎng hē shénme?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Ngoài trời nóng lắm, mau uống chút nước đi. - Nam: Có trà xanh lạnh không? - Nữ: Không có, tủ lạnh có dưa hấu, ăn chút dưa hấu nhé. - Nam: Cũng được, dưa hấu rất ngọt. - Hỏi: Người nam muốn uống gì?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>A</strong>: Trà xanh (绿茶).
          </div>
          <div class="feedback-box" id="feedback-18"></div>
        </div>

        <!-- Câu 19 -->
        <div class="card" id="card-19">
          <span class="card-num">Câu 19</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">今天星期一，你怎么没去上学？</span>
            <span class="pinyin-line">Jīntiān xīngqīyī, nǐ zěnme méi qù shàngxué?</span>
            <span class="trans-line">Hôm nay thứ Hai, sao con không đi học?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">我发烧了，头很疼。</span>
            <span class="pinyin-line">Wǒ fāshāo le, tóu hěn téng.</span>
            <span class="trans-line">Con bị sốt rồi, đầu đau lắm.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">去医院看医生了吗？</span>
            <span class="pinyin-line">Qù yīyuàn kàn yīshēng le ma?</span>
            <span class="trans-line">Đã đi bệnh viện khám bác sĩ chưa?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">妈妈上午带我去了，医生让我多喝水，多休息。</span>
            <span class="pinyin-line">Māma shàngwǔ dài wǒ qù le, yīshēng ràng wǒ duō hē shuǐ, duō xiūxi.</span>
            <span class="trans-line">Sáng nay mẹ đưa con đi rồi, bác sĩ bảo con uống nhiều nước, nghỉ ngơi nhiều.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">女的怎么了？</span>
            <span class="pinyin-line">Nǚde zěnme le?</span>
            <span class="trans-line">Người nữ bị làm sao?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(19, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">不想去上学</span></div>
            <div class="option-chip" onclick="selectOption(19, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">觉得累</span></div>
            <div class="option-chip" onclick="selectOption(19, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">不舒服</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(19)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(19)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(19)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-19">
            <div class="sentence-pinyin-full">Nán: Jīntiān xīngqīyī, nǐ zěnme méi qù shàngxué? - Nǚ: Wǒ fāshāo le, tóu hěn téng. - Nán: Qù yīyuàn kàn yīshēng le ma? - Nǚ: Māma shàngwǔ dài wǒ qù le, yīshēng ràng wǒ duō hē shuǐ, duō xiūxi. - Wèn: Nǚde zěnme le?</div>
            <strong>Dịch nghĩa:</strong> Nam: Hôm nay thứ Hai sao con không đi học? - Nữ: Con bị sốt, đầu đau lắm. - Nam: Đi viện khám chưa? - Nữ: Sáng mẹ đưa con đi rồi, bác sĩ bảo uống nhiều nước, nghỉ ngơi. - Hỏi: Người nữ sao thế?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>C</strong>: Người nữ không khỏe (不舒服).
          </div>
          <div class="feedback-box" id="feedback-19"></div>
        </div>

        <!-- Câu 20 -->
        <div class="card" id="card-20">
          <span class="card-num">Câu 20</span>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">中午我们去吃牛肉面，怎么样？</span>
            <span class="pinyin-line">Zhōngwǔ wǒmen qù chī niúròumiàn, zěnmeyàng?</span>
            <span class="trans-line">Trưa nay chúng mình đi ăn mì bò nhé?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">这里的牛肉面不新鲜，换一家吧。</span>
            <span class="pinyin-line">Zhèlǐ de niúròumiàn bù xīnxiān, huàn yì jiā ba.</span>
            <span class="trans-line">Mì bò ở đây không tươi, đổi quán khác đi.</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">那去前面那家饭馆吃米饭？</span>
            <span class="pinyin-line">Nà qù qiánmian nà jiā fànguǎn chī mǐfàn?</span>
            <span class="trans-line">Vậy đến quán ăn phía trước ăn cơm nhé?</span>
          </div>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">好啊，走吧。</span>
            <span class="pinyin-line">Hǎo a, zǒu ba.</span>
            <span class="trans-line">Được thôi, đi nào.</span>
          </div>
          <div class="speaker-line" style="margin-top:6px; color:#fbbf24;">
            <span class="speaker" style="color:#fbbf24;">问:</span>
            <span class="interactive-text">男的觉得这里的牛肉面怎么样？</span>
            <span class="pinyin-line">Nánde juéde zhèlǐ de niúròumiàn zěnmeyàng?</span>
            <span class="trans-line">Người nam thấy mì bò ở đây thế nào?</span>
          </div>
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption(20, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">牛肉不新鲜</span></div>
            <div class="option-chip" onclick="selectOption(20, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">没有牛肉了</span></div>
            <div class="option-chip" onclick="selectOption(20, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">要吃米饭</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz(20)">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz(20)">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(20)">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-20">
            <div class="sentence-pinyin-full">Nǚ: Zhōngwǔ wǒmen qù chī niúròumiàn, zěnmeyàng? - Nán: Zhèlǐ de niúròumiàn bù xīnxiān, huàn yì jiā ba. - Nǚ: Nà qù qiánmian nà jiā fànguǎn chī mǐfàn? - Nán: Hǎo a, zǒu ba. - Wèn: Nánde juéde zhèlǐ de niúròumiàn zěnmeyàng?</div>
            <strong>Dịch nghĩa:</strong> Nữ: Trưa mình đi ăn mì bò nhé? - Nam: Mì bò ở đây không tươi, đổi quán khác đi. - Nữ: Vậy đến quán đằng trước ăn cơm? - Nam: Được đấy, đi thôi. - Hỏi: Người nam thấy mì bò ở đây thế nào?<br>
            <strong>Giải thích:</strong> Đáp án đúng là <strong>A</strong>: Thịt bò không tươi (牛肉不新鲜).
          </div>
          <div class="feedback-box" id="feedback-20"></div>
        </div>
      </section>'''

# TAB 2: BÀI ĐỌC
tab2_content = '''      <!-- PHẦN 1: CÂU 21-25 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 21 - 25 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Ghép câu đối thoại phù hợp (A - F)</span>
        </div>
        <p class="section-desc">Yêu cầu: 选择合适的问题或答句 (Chọn câu hỏi hoặc câu trả lời phù hợp với câu cho sẵn):</p>

        <!-- Danh sách các câu A-F -->
        <div class="reading-ref-box">
          <div class="reading-ref-title">DANH SÁCH CÁC CÂU LỰA CHỌN (A - F):</div>
          
          <div class="reading-ref-item">
            <span class="chip-letter">A</span>
            <div>
              <span class="interactive-text" style="font-size:16px;">我今天不舒服，觉得很累。</span>
              <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
              <div class="sentence-trans-box"><div class="sentence-pinyin-full">Wǒ jīntiān bù shūfu, juéde hěn lèi.</div><div>Hôm nay tôi không được khỏe, cảm thấy rất mệt mỏi.</div></div>
            </div>
          </div>

          <div class="reading-ref-item">
            <span class="chip-letter">B</span>
            <div>
              <span class="interactive-text" style="font-size:16px;">你还认识我吗？我们在中国见过。</span>
              <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
              <div class="sentence-trans-box"><div class="sentence-pinyin-full">Nǐ hái rènshi wǒ ma? Wǒmen zài Zhōngguó jiàn guo.</div><div>Bạn còn nhận ra tôi không? Chúng mình từng gặp nhau ở Trung Quốc rồi đấy.</div></div>
            </div>
          </div>

          <div class="reading-ref-item">
            <span class="chip-letter">C</span>
            <div>
              <span class="interactive-text" style="font-size:16px;">你喜欢吃红苹果还是绿苹果？</span>
              <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
              <div class="sentence-trans-box"><div class="sentence-pinyin-full">Nǐ xǐhuan chī hóng píngguǒ háishì lǜ píngguǒ?</div><div>Bạn thích ăn táo đỏ hay là táo xanh?</div></div>
            </div>
          </div>

          <div class="reading-ref-item">
            <span class="chip-letter">D</span>
            <div>
              <span class="interactive-text" style="font-size:16px;">妈妈，我下课回来了。</span>
              <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
              <div class="sentence-trans-box"><div class="sentence-pinyin-full">Māma, wǒ xiàkè huílái le.</div><div>Mẹ ơi, con tan học về rồi ạ.</div></div>
            </div>
          </div>

          <div class="reading-ref-item is-example">
            <span class="chip-letter">E</span>
            <div>
              <span class="interactive-text" style="font-size:16px; color:#94a3b8;">当然。我们先坐公共汽车，然后换地铁。 (Ví dụ mẫu)</span>
            </div>
          </div>

          <div class="reading-ref-item">
            <span class="chip-letter">F</span>
            <div>
              <span class="interactive-text" style="font-size:16px;">上面写着二十元一把。</span>
              <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
              <div class="sentence-trans-box"><div class="sentence-pinyin-full">Shàngmian xiězhe èrshí yuán yì bǎ.</div><div>Bên trên có ghi 20 tệ một chiếc.</div></div>
            </div>
          </div>
        </div>

        <!-- Câu 21 -->
        <div class="card" id="q-21">
          <span class="card-num">Câu 21</span>
          <div class="interactive-text">今天你怎么了？一直在睡觉。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Jīntiān nǐ zěnme le? Yìzhí zài shuìjiào.</div>
              <div>Hôm nay cậu sao thế? Cứ ngủ suốt từ nãy đến giờ.</div>
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
          <div class="interactive-text">啊，对，我记得你，你瘦了。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Ā, duì, wǒ jìde nǐ, nǐ shòu le.</div>
              <div>A, đúng rồi, tôi nhớ ra bạn rồi, bạn gầy đi đấy.</div>
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
          <div class="interactive-text">桌子上放着饮料，你先喝点儿吧。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhuōzi shang fàngzhe yǐnliào, nǐ xiān hē diǎnr ba.</div>
              <div>Trên bàn có để đồ uống đấy, con uống một chút trước đi.</div>
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
          <div class="interactive-text">我喜欢吃红苹果，我觉得红苹果甜。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Wǒ xǐhuan chī hóng píngguǒ, wǒ juéde hóng píngguǒ tián.</div>
              <div>Tôi thích ăn táo đỏ, tôi thấy táo đỏ ngọt hơn.</div>
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
          <div class="interactive-text">这种雨伞多少钱一把？</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhè zhǒng yǔsǎn duōshao qián yì bǎ?</div>
              <div>Loại ô/dù này bao nhiêu tiền một chiếc vậy?</div>
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

      <!-- PHẦN 2: CÂU 26-30 -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 26 - 30 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Chọn từ ngữ thích hợp điền vào chỗ trống</span>
        </div>
        <p class="section-desc">Yêu cầu: 选词填空 (Chọn từ thích hợp điền vào chỗ trống A - F):</p>

        <!-- Ngân hàng từ vựng A-F -->
        <div class="reading-vocab-box">
          <div class="reading-vocab-title">NGÂN HÀNG TỪ VỰNG:</div>
          <div class="reading-vocab-grid">
            <div class="reading-vocab-card"><span class="chip-letter">A</span> <strong class="interactive-text">裤子</strong> <span style="font-size:12px; color:#94a3b8;">(kùzi: chiếc quần)</span></div>
            <div class="reading-vocab-card"><span class="chip-letter">B</span> <strong class="interactive-text">或者</strong> <span style="font-size:12px; color:#94a3b8;">(huòzhě: hoặc là)</span></div>
            <div class="reading-vocab-card"><span class="chip-letter">C</span> <strong class="interactive-text">还是</strong> <span style="font-size:12px; color:#94a3b8;">(háishi: hay là)</span></div>
            <div class="reading-vocab-card"><span class="chip-letter">D</span> <strong class="interactive-text">记得</strong> <span style="font-size:12px; color:#94a3b8;">(jìde: nhớ)</span></div>
            <div class="reading-vocab-card is-example"><span class="chip-letter">E</span> <strong class="interactive-text">声音</strong> <span style="font-size:12px; color:#94a3b8;">(shēngyīn: âm thanh - Ví dụ)</span></div>
            <div class="reading-vocab-card"><span class="chip-letter">F</span> <strong class="interactive-text">小心</strong> <span style="font-size:12px; color:#94a3b8;">(xiǎoxīn: cẩn thận)</span></div>
          </div>
        </div>

        <!-- Câu 26 -->
        <div class="card" id="q-26">
          <span class="card-num">Câu 26</span>
          <div class="interactive-text">老师，我们今天复习第三课 <span id="blank-display-26" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 学习第四课？</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Lǎoshī, wǒmen jīntiān fùxí dì-sān kè háishì xuéxí dì-sì kè?</div>
              <div>Thưa thầy/cô, hôm nay chúng ta ôn tập bài 3 hay là học bài 4 ạ?</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('26', 'A', '裤子')" data-q="26" data-val="A"><span class="chip-letter">A</span> 裤子</div>
            <div class="option-chip" onclick="selectOption('26', 'B', '或者')" data-q="26" data-val="B"><span class="chip-letter">B</span> 或者</div>
            <div class="option-chip" onclick="selectOption('26', 'C', '还是')" data-q="26" data-val="C"><span class="chip-letter">C</span> 还是</div>
            <div class="option-chip" onclick="selectOption('26', 'D', '记得')" data-q="26" data-val="D"><span class="chip-letter">D</span> 记得</div>
            <div class="option-chip" onclick="selectOption('26', 'F', '小心')" data-q="26" data-val="F"><span class="chip-letter">F</span> 小心</div>
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
          <div class="interactive-text">周末你是不是要带学生去爬山？穿这条 <span id="blank-display-27" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 吧。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhōumò nǐ shì bú shì yào dài xuésheng qù páshān? Chuān zhè tiáo kùzi ba.</div>
              <div>Cuối tuần bạn có phải dẫn học sinh đi leo núi không? Hãy mặc chiếc quần này nhé.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('27', 'A', '裤子')" data-q="27" data-val="A"><span class="chip-letter">A</span> 裤子</div>
            <div class="option-chip" onclick="selectOption('27', 'B', '或者')" data-q="27" data-val="B"><span class="chip-letter">B</span> 或者</div>
            <div class="option-chip" onclick="selectOption('27', 'C', '还是')" data-q="27" data-val="C"><span class="chip-letter">C</span> 还是</div>
            <div class="option-chip" onclick="selectOption('27', 'D', '记得')" data-q="27" data-val="D"><span class="chip-letter">D</span> 记得</div>
            <div class="option-chip" onclick="selectOption('27', 'F', '小心')" data-q="27" data-val="F"><span class="chip-letter">F</span> 小心</div>
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
          <div class="interactive-text">这杯饮料很热，喝的时候 <span id="blank-display-28" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 点儿。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhè bēi yǐnliào hěn rè, hē de shíhou xiǎoxīn diǎnr.</div>
              <div>Cốc thức uống này nóng lắm, lúc uống bạn nhớ cẩn thận một chút nhé.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('28', 'A', '裤子')" data-q="28" data-val="A"><span class="chip-letter">A</span> 裤子</div>
            <div class="option-chip" onclick="selectOption('28', 'B', '或者')" data-q="28" data-val="B"><span class="chip-letter">B</span> 或者</div>
            <div class="option-chip" onclick="selectOption('28', 'C', '还是')" data-q="28" data-val="C"><span class="chip-letter">C</span> 还是</div>
            <div class="option-chip" onclick="selectOption('28', 'D', '记得')" data-q="28" data-val="D"><span class="chip-letter">D</span> 记得</div>
            <div class="option-chip" onclick="selectOption('28', 'F', '小心')" data-q="28" data-val="F"><span class="chip-letter">F</span> 小心</div>
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
          <div class="interactive-text">A: 你想喝点儿什么茶？<br>B: 花茶 <span id="blank-display-29" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 绿茶都行。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">A: Nǐ xiǎng hē diǎnr shénme chá? B: Huāchá huòzhě lǜchá dōu xíng.</div>
              <div>A: Cậu muốn uống trà gì nào? B: Trà hoa hoặc trà xanh đều được cả.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('29', 'A', '裤子')" data-q="29" data-val="A"><span class="chip-letter">A</span> 裤子</div>
            <div class="option-chip" onclick="selectOption('29', 'B', '或者')" data-q="29" data-val="B"><span class="chip-letter">B</span> 或者</div>
            <div class="option-chip" onclick="selectOption('29', 'C', '还是')" data-q="29" data-val="C"><span class="chip-letter">C</span> 还是</div>
            <div class="option-chip" onclick="selectOption('29', 'D', '记得')" data-q="29" data-val="D"><span class="chip-letter">D</span> 记得</div>
            <div class="option-chip" onclick="selectOption('29', 'F', '小心')" data-q="29" data-val="F"><span class="chip-letter">F</span> 小心</div>
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
          <div class="interactive-text">A: 经理旁边坐着一个人，你知道是谁吗？<br>B: 你不 <span id="blank-display-30" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> 了？那是小周啊，去年来过。</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">A: Jīnglǐ pángbiān zuòzhe yí ge rén, nǐ zhīdào shì shéi ma? B: Nǐ bù jìde le? Nà shì Xiǎo Zhōu a, qùnián lái guo.</div>
              <div>A: Bên cạnh giám đốc có một người đang ngồi, bạn biết là ai không? B: Bạn không nhớ nữa à? Đó là Tiểu Chu đấy, năm ngoái từng đến rồi.</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('30', 'A', '裤子')" data-q="30" data-val="A"><span class="chip-letter">A</span> 裤子</div>
            <div class="option-chip" onclick="selectOption('30', 'B', '或者')" data-q="30" data-val="B"><span class="chip-letter">B</span> 或者</div>
            <div class="option-chip" onclick="selectOption('30', 'C', '还是')" data-q="30" data-val="C"><span class="chip-letter">C</span> 还是</div>
            <div class="option-chip" onclick="selectOption('30', 'D', '记得')" data-q="30" data-val="D"><span class="chip-letter">D</span> 记得</div>
            <div class="option-chip" onclick="selectOption('30', 'F', '小心')" data-q="30" data-val="F"><span class="chip-letter">F</span> 小心</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('30')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('30')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-30"></div>
        </div>
      </section>

      <!-- PHẦN 3: CÂU 31-35 (CANONICAL TEMPLATE WITH FULL PINYIN) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第三部分: 第 31 - 35 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Đọc đoạn văn và chọn câu trả lời đúng (A, B, C)</span>
        </div>

        <p class="section-desc">
          💡 <strong>Lưu ý:</strong> Các lựa chọn A, B, C mặc định chỉ hiển thị chữ Hán. Bạn có thể rê chuột vào từng chữ để tra từ điển, hoặc bấm <strong>"👁 Dịch đoạn văn &amp; các lựa chọn"</strong> khi cần kiểm tra nghĩa và phiên âm pinyin.
        </p>

        <!-- Câu 31 -->
        <div class="card" id="q-31">
          <span class="card-num">Câu 31</span>
          <div class="reading-passage-box interactive-text">
            这条裤子是去年过生日时我哥送我的，只穿了一次，就没再穿，一直放在这里。
          </div>

          <div class="reading-question-title interactive-text">
            &bull; 这条裤子：
          </div>

          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('31', 'A')" data-q="31" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">是绿色的</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('31', 'B')" data-q="31" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">没穿过几次</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('31', 'C')" data-q="31" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">是我买的</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhè tiáo kùzi shì qùnián guò shēngrì shí wǒ gē sòng wǒ de, zhǐ chuān le yí cì, jiù méi zài chuān, yìzhí fàng zài zhèlǐ.</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> Chiếc quần này là anh trai tặng tôi vào dịp sinh nhật năm ngoái, mới mặc đúng một lần rồi không mặc nữa, cứ để mãi ở đây.</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 是绿色的</strong> (shì lǜsè de): có màu xanh lá cây<br>
                &bull; <strong>B. 没穿过几次</strong> (méi chuānguo jǐ cì): chưa mặc mấy lần<br>
                &bull; <strong>C. 是我买的</strong> (shì wǒ mǎi de): là do tôi mua<br>
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
            多吃新鲜的苹果对身体好，早上和上午是吃苹果最好的时间。
          </div>

          <div class="reading-question-title interactive-text">
            &bull; 我们应该：
          </div>

          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('32', 'A')" data-q="32" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">晚上吃苹果</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('32', 'B')" data-q="32" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">上午吃苹果</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('32', 'C')" data-q="32" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">身体好的时候吃苹果</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Duō chī xīnxiān de píngguǒ duì shēntǐ hǎo, zǎoshang hé shàngwǔ shì chī píngguǒ zuì hǎo de shíjiān.</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> Ăn nhiều táo tươi rất tốt cho sức khỏe, buổi sáng và buổi trưa là thời gian ăn táo tốt nhất.</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 晚上吃苹果</strong> (wǎnshang chī píngguǒ): buổi tối ăn táo<br>
                &bull; <strong>B. 上午吃苹果</strong> (shàngwǔ chī píngguǒ): buổi sáng/trưa ăn táo<br>
                &bull; <strong>C. 身体好的时候吃苹果</strong> (shēntǐ hǎo de shíhou chī píngguǒ): lúc khỏe mạnh thì ăn táo<br>
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
            我先生不爱吃西瓜，你也不爱吃，西瓜那么好吃，又那么甜，为什么你们会不喜欢呢？
          </div>

          <div class="reading-question-title interactive-text">
            &bull; 她：
          </div>

          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('33', 'A')" data-q="33" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">爱吃西瓜</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('33', 'B')" data-q="33" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">不喜欢吃甜的</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('33', 'C')" data-q="33" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">没买西瓜</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Wǒ xiānsheng bú ài chī xīguā, nǐ yě bú ài chī, xīguā nàme hǎochī, yòu nàme tián, wèishénme nǐmen huì bù xǐhuan ne?</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> Chồng tôi không thích ăn dưa hấu, bạn cũng không thích ăn, dưa hấu ngon như thế, lại ngọt như thế, tại sao hai người lại có thể không thích cơ chứ?</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 爱吃西瓜</strong> (ài chī xīguā): thích ăn dưa hấu<br>
                &bull; <strong>B. 不喜欢吃甜的</strong> (bù xǐhuan chī tián de): không thích ăn đồ ngọt<br>
                &bull; <strong>C. 没买西瓜</strong> (méi mǎi xīguā): không mua dưa hấu<br>
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
            我们的办公室里放着很多吃的东西，下午工作累了的时候，大家都会吃点儿。
          </div>

          <div class="reading-question-title interactive-text">
            &bull; 我们下午：
          </div>

          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('34', 'A')" data-q="34" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">去买吃的东西</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('34', 'B')" data-q="34" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">只吃东西不工作</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('34', 'C')" data-q="34" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">累了就吃点儿东西</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Wǒmen de bàngōngshì li fàngzhe hěnduō chī de dōngxi, xiàwǔ gōngzuò lèi le de shíhou, dàjiā dōu huì chī diǎnr.</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> Trong văn phòng của chúng tôi để rất nhiều đồ ăn, buổi chiều khi làm việc mệt mỏi, mọi người đều sẽ ăn một chút.</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 去买吃的东西</strong> (qù mǎi chī de dōngxi): đi mua đồ ăn<br>
                &bull; <strong>B. 只吃东西不工作</strong> (zhǐ chī dōngxi bù gōngzuò): chỉ ăn đồ ăn chứ không làm việc<br>
                &bull; <strong>C. 累了就吃点儿东西</strong> (lèi le jiù chī diǎnr dōngxi): mệt là sẽ ăn một chút đồ<br>
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
            周六周日我们事情不多，喜欢和学生们去爬爬山，或者打打篮球，有时候也会在家里看书。
          </div>

          <div class="reading-question-title interactive-text">
            &bull; 我们：
          </div>

          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('35', 'A')" data-q="35" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">周末工作很忙</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('35', 'B')" data-q="35" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">周末喜欢去爬山</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('35', 'C')" data-q="35" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">每天在家看书</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">Zhōuliù zhōurì wǒmen shìqing bù duō, xǐhuan hé xuéshengmen qù pápa shān, huòzhě dǎda lánqiú, yǒushíhou yě huì zài jiā li kàn shū.</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> Thứ Bảy Chủ Nhật việc của chúng tôi không nhiều, thích cùng học sinh đi leo núi, hoặc chơi bóng rổ, có lúc cũng ở nhà đọc sách.</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. 周末工作很忙</strong> (zhōumò gōngzuò hěn máng): cuối tuần công việc rất bận<br>
                &bull; <strong>B. 周末喜欢去爬山</strong> (zhōumò xǐhuan qù páshān): cuối tuần thích đi leo núi<br>
                &bull; <strong>C. 每天在家看书</strong> (měitiān zài jiā kàn shū): ngày nào cũng ở nhà đọc sách<br>
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

# TAB 3: BÀI VIẾT
tab3_content = '''      <!-- PHẦN 1: SẮP XẾP CÂU (36-40) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第一部分: 第 36 - 40 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Sắp xếp các từ ngữ để tạo thành câu hoàn chỉnh</span>
        </div>
        <p class="section-desc">Yêu cầu: 连词成句 (Dựa vào ngữ pháp đã học, sắp xếp các cụm từ xáo trộn thành câu đúng):</p>

        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">小船 / 上 / 一 / 河 / 条 / 有</div>
          <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">河上有一条小船。</div>
          <div class="sentence-pinyin-full">Hé shang yǒu yì tiáo xiǎochuán.</div>
          <div style="font-size:13px; color:var(--text-sub);">Trên sông có một con thuyền nhỏ.</div>
        </div>

        <!-- Câu 36 -->
        <div class="card">
          <span class="card-num">Câu 36</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">放着 / 裤子 / 床上 / 一条</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">床上放着一条裤子。</div>
            <div class="sentence-pinyin-full">Chuáng shang fàngzhe yì tiáo kùzi.</div>
            <div>Trên giường có để một chiếc quần.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Câu tồn tại [Từ chỉ vị trí: 床上] + [Động từ: 放着] + [Cụm danh từ: 一条裤子].</div>
          </div>
        </div>

        <!-- Câu 37 -->
        <div class="card">
          <span class="card-num">Câu 37</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">的时候 / 要 / 小心点儿 / 爬山</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">爬山的时候要小心点儿。</div>
            <div class="sentence-pinyin-full">Páshān de shíhou yào xiǎoxīn diǎnr.</div>
            <div>Lúc leo núi cần phải cẩn thận một chút.</div>
          </div>
        </div>

        <!-- Câu 38 -->
        <div class="card">
          <span class="card-num">Câu 38</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">穿了 / 一件 / 我记得 / 白衬衫 / 他</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">我记得他穿了一件白衬衫。</div>
            <div class="sentence-pinyin-full">Wǒ jìde tā chuān le yí jiàn bái chènshān.</div>
            <div>Tôi nhớ là anh ấy đã mặc một chiếc áo sơ mi trắng.</div>
          </div>
        </div>

        <!-- Câu 39 -->
        <div class="card">
          <span class="card-num">Câu 39</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">红茶 / 想喝 / 绿茶 / 还是 / 你</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">你想喝红茶还是绿茶？</div>
            <div class="sentence-pinyin-full">Nǐ xiǎng hē hóngchá háishì lǜchá?</div>
            <div>Bạn muốn uống hồng trà hay là trà xanh?</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Câu hỏi lựa chọn dùng 还是 (A 还是 B?).</div>
          </div>
        </div>

        <!-- Câu 40 -->
        <div class="card">
          <span class="card-num">Câu 40</span>
          <div class="interactive-text" style="margin-bottom:8px; color:#cbd5e1;">还是 / 他想买 / 裤子 / 衬衫 / 我不知道</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="interactive-text" style="font-size: 17px; font-weight: bold; color: #86efac;">我不知道他想买衬衫还是裤子。</div>
            <div class="sentence-pinyin-full">Wǒ bù zhīdào tā xiǎng mǎi chènshān háishì kùzi.</div>
            <div>Tôi không biết là anh ấy muốn mua áo sơ mi hay là quần nữa.</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ngữ pháp: Mệnh đề danh ngữ mang tính nghi vấn lồng bên trong câu dùng 还是.</div>
          </div>
        </div>
      </section>

      <!-- PHẦN 2: NHÌN PHIÊN ÂM ĐIỀN CHỮ HÁN (41-45) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>第二部分: 第 41 - 45 题</span></div>
          <span style="font-size:13px; color:var(--accent);">Nhìn phiên âm Pinyin điền chữ Hán</span>
        </div>
        <p class="section-desc">Yêu cầu: 看拼音，写汉字 (Căn cứ vào phiên âm pinyin trong ngoặc đơn để điền chữ Hán chính xác):</p>

        <!-- Câu 41 -->
        <div class="card">
          <span class="card-num">Câu 41</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            我想喝点儿（ yǐn ）料。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Tôi muốn uống một chút thức uống.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">饮</span> <span class="sentence-pinyin-full">(yǐn)</span> - Hán Việt: Ẩm</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>饮料</strong> (yǐnliào: đồ uống, thức uống).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">我想喝点儿饮料。 (Wǒ xiǎng hē diǎnr yǐnliào.)</div>
          </div>
        </div>

        <!-- Câu 42 -->
        <div class="card">
          <span class="card-num">Câu 42</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            水很热，喝的时候小（ xīn ）点儿。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Nước nóng lắm, lúc uống hãy cẩn thận một chút nhé.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">心</span> <span class="sentence-pinyin-full">(xīn)</span> - Hán Việt: Tâm</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>小心</strong> (xiǎoxīn: cẩn thận, chú ý).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">水很热，喝的时候小心点儿。 (Shuǐ hěn rè, hē de shíhou xiǎoxīn diǎnr.)</div>
          </div>
        </div>

        <!-- Câu 43 -->
        <div class="card">
          <span class="card-num">Câu 43</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            一（ tiáo ）裤子三百元。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Một chiếc quần giá ba trăm tệ.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">条</span> <span class="sentence-pinyin-full">(tiáo)</span> - Hán Việt: Điều</div>
            <div style="margin-top:4px;">&bull; Lượng từ: Dùng cho quần, váy, cá, con đường: <strong>一条裤子</strong> (một chiếc quần).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">一条裤子三百元。 (Yì tiáo kùzi sān bǎi yuán.)</div>
          </div>
        </div>

        <!-- Câu 44 -->
        <div class="card">
          <span class="card-num">Câu 44</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            我觉得胖或（ zhě ）瘦没关系。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Tôi thấy béo hay gầy đều không sao cả.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">者</span> <span class="sentence-pinyin-full">(zhě)</span> - Hán Việt: Giả</div>
            <div style="margin-top:4px;">&bull; Từ ghép: <strong>或者</strong> (huòzhě: hoặc là, hay là).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">我觉得胖或者瘦没关系。 (Wǒ juéde pàng huòzhě shòu méi guānxi.)</div>
          </div>
        </div>

        <!-- Câu 45 -->
        <div class="card">
          <span class="card-num">Câu 45</span>
          <div class="interactive-text" style="margin-bottom:8px; font-size:17px;">
            我不喜欢这个（ tián ）面包。
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">Tôi không thích chiếc bánh mì ngọt này.</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="interactive-text" style="font-size: 22px; font-weight: bold; color: #86efac;">甜</span> <span class="sentence-pinyin-full">(tián)</span> - Hán Việt: Điềm</div>
            <div style="margin-top:4px;">&bull; Tính từ: Ngọt (ngược nghĩa với 苦: đắng, 酸: chua): <strong>甜面包</strong> (bánh mì ngọt).</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">我不喜欢这个甜面包。 (Wǒ bù xǐhuan zhè ge tián miànbāo.)</div>
          </div>
        </div>
      </section>'''

# TAB 4: TỪ VỰNG & NGỮ PHÁP (SGK)
tab4_content = '''      <!-- PHẦN 1: 17 TỪ MỚI CHÍNH THỨC SGK -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>生词: 17 Từ mới Sách Giáo Khoa (Trang 37 - 38)</span></div>
          <span style="font-size:13px; color:var(--accent);">HSK 3 Sách Giáo Khoa &bull; Bài 3</span>
        </div>
        <p class="section-desc">Toàn bộ 17 từ vựng mới chính thức của Bài 3 kèm từ loại, pinyin và nghĩa tiếng Việt chuẩn xác:</p>

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
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">还是</td>
              <td style="color: #38bdf8; font-weight: 600;">háishi</td>
              <td style="color: #a78bfa; font-size: 13px;">liên từ</td>
              <td>hay, hay là (dùng trong câu hỏi lựa chọn: A 还是 B?)</td>
            </tr>
            <tr>
              <td>2</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">爬山</td>
              <td style="color: #38bdf8; font-weight: 600;">pá shān</td>
              <td style="color: #a78bfa; font-size: 13px;">động từ</td>
              <td>leo núi (động từ li hợp: 爬了山, 爬过山)</td>
            </tr>
            <tr>
              <td>3</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">小心</td>
              <td style="color: #38bdf8; font-weight: 600;">xiǎoxīn</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ / đgt</td>
              <td>cẩn thận, chú ý (小心点儿, 要小心)</td>
            </tr>
            <tr>
              <td>4</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">条</td>
              <td style="color: #38bdf8; font-weight: 600;">tiáo</td>
              <td style="color: #a78bfa; font-size: 13px;">lượng từ</td>
              <td>chiếc, con, cái (dùng cho vật dài, uốn lượn: quần, váy, cá, sông)</td>
            </tr>
            <tr>
              <td>5</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">裤子</td>
              <td style="color: #38bdf8; font-weight: 600;">kùzi</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>quần (一条裤子: một chiếc quần)</td>
            </tr>
            <tr>
              <td>6</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">记得</td>
              <td style="color: #38bdf8; font-weight: 600;">jìde</td>
              <td style="color: #a78bfa; font-size: 13px;">động từ</td>
              <td>nhớ, còn nhớ (我记得: tôi nhớ; 不记得: không nhớ)</td>
            </tr>
            <tr>
              <td>7</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">衬衫</td>
              <td style="color: #38bdf8; font-weight: 600;">chènshān</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>áo sơ mi (一件衬衫: một chiếc áo sơ mi)</td>
            </tr>
            <tr>
              <td>8</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">元</td>
              <td style="color: #38bdf8; font-weight: 600;">yuán</td>
              <td style="color: #a78bfa; font-size: 13px;">lượng từ</td>
              <td>đồng tệ (đơn vị tiền tệ chính thức, văn nói dùng 块)</td>
            </tr>
            <tr>
              <td>9</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">新鲜</td>
              <td style="color: #38bdf8; font-weight: 600;">xīnxiān</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>tươi, tươi mới (đồ ăn, hoa quả, không khí trong lành)</td>
            </tr>
            <tr>
              <td>10</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">甜</td>
              <td style="color: #38bdf8; font-weight: 600;">tián</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>ngọt (西瓜真甜: dưa hấu ngọt thật; vị ngọt)</td>
            </tr>
            <tr>
              <td>11</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">只</td>
              <td style="color: #38bdf8; font-weight: 600;">zhǐ</td>
              <td style="color: #a78bfa; font-size: 13px;">phó từ</td>
              <td>chỉ, duy chỉ (chỉ ăn dưa hấu: 只吃西瓜; chỉ có: 只有)</td>
            </tr>
            <tr>
              <td>12</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">放</td>
              <td style="color: #38bdf8; font-weight: 600;">fàng</td>
              <td style="color: #a78bfa; font-size: 13px;">động từ</td>
              <td>đặt, để (放着: đang để/có để; 放在桌子上)</td>
            </tr>
            <tr>
              <td>13</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">饮料</td>
              <td style="color: #38bdf8; font-weight: 600;">yǐnliào</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>đồ uống, thức uống, nước giải khát</td>
            </tr>
            <tr>
              <td>14</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">或者</td>
              <td style="color: #38bdf8; font-weight: 600;">huòzhě</td>
              <td style="color: #a78bfa; font-size: 13px;">liên từ</td>
              <td>hoặc, hoặc là (dùng trong câu trần thuật lựa chọn)</td>
            </tr>
            <tr>
              <td>15</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">舒服</td>
              <td style="color: #38bdf8; font-weight: 600;">shūfu</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>dễ chịu, thoải mái (很舒服; 不舒服: khó chịu, bị ốm)</td>
            </tr>
            <tr>
              <td>16</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">花</td>
              <td style="color: #38bdf8; font-weight: 600;">huā</td>
              <td style="color: #a78bfa; font-size: 13px;">danh từ</td>
              <td>hoa (bông hoa, hoa tươi; 花茶: trà hoa)</td>
            </tr>
            <tr>
              <td>17</td>
              <td class="interactive-text" style="font-size: 19px; font-weight: bold; color: #fff;">绿</td>
              <td style="color: #38bdf8; font-weight: 600;">lǜ</td>
              <td style="color: #a78bfa; font-size: 13px;">tính từ</td>
              <td>màu xanh lá cây (绿茶: trà xanh; 绿苹果: táo xanh)</td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- PHẦN 2: 3 CHỦ ĐIỂM NGỮ PHÁP CHÍNH THỨC SGK -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>注释: 3 Điểm Ngữ Pháp Trọng Tâm SGK (Trang 39 - 40)</span></div>
          <span style="font-size:13px; color:var(--accent);">Quy tắc &amp; Ví dụ nguyên bản</span>
        </div>

        <!-- Ngữ pháp 1 -->
        <div class="grammar-card">
          <div class="grammar-title">1. Phân biệt câu hỏi lựa chọn “还是” và câu trần thuật lựa chọn “或者”</div>
          <div class="grammar-formula">
            Câu hỏi: A + 还是 + B ?<br>
            Câu trần thuật: A + 或者 + B
          </div>
          <div class="grammar-desc">
            Cả <strong>“还是”</strong> và <strong>“或者”</strong> đều được dùng để biểu thị sự lựa chọn giữa các phương án. Tuy nhiên:<br>
            &bull; <strong>“还是”</strong> thông thường được dùng trong <strong>câu nghi vấn (câu hỏi)</strong>.<br>
            &bull; <strong>“或者”</strong> được dùng trong <strong>câu trần thuật (câu kể)</strong>.<br>
            &bull; <em>Lưu ý đặc biệt:</em> Đối với câu trần thuật nhưng có chứa mệnh đề con mang tính chất nghi vấn thì mệnh đề con đó vẫn bắt buộc dùng <strong>“还是”</strong> (ví dụ câu 5, 6, 7 bên dưới).
          </div>
          <div style="font-size: 13px; color: var(--text-sub); margin-bottom: 8px; font-weight: bold;">Các câu ví dụ chuẩn SGK:</div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(1) 你要喝咖啡还是喝茶？</div>
            <div class="example-pinyin">Nǐ yào hē kāfēi háishì hē chá?</div>
            <div class="example-vi">Bạn muốn uống cà phê hay là uống trà? (Câu hỏi lựa chọn)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(2) 明天是晴天还是阴天？</div>
            <div class="example-pinyin">Míngtiān shì qíngtiān háishì yīntiān?</div>
            <div class="example-vi">Ngày mai là trời nắng hay trời râm? (Câu hỏi lựa chọn)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(3) 今天晚上吃米饭或者面条都可以。</div>
            <div class="example-pinyin">Jīntiān wǎnshang chī mǐfàn huòzhě miàntiáo dōu kěyǐ.</div>
            <div class="example-vi">Tối nay ăn cơm hay mì sợi đều được. (Câu trần thuật)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(4) 天冷了或者工作累了的时候，喝杯热茶会很舒服。</div>
            <div class="example-pinyin">Tiān lěng le huòzhě gōngzuò lèi le de shíhou, hē bēi rè chá huì hěn shūfu.</div>
            <div class="example-vi">Lúc trời trở lạnh hoặc khi công việc mệt mỏi, uống cốc trà nóng sẽ rất dễ chịu. (Câu trần thuật)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(5) 周太太40岁还是50岁，我们不知道。</div>
            <div class="example-pinyin">Zhōu tàitai sìshí suì háishì wǔshí suì, wǒmen bù zhīdào.</div>
            <div class="example-vi">Bà Chu 40 tuổi hay 50 tuổi, chúng tôi không biết rõ. (Mệnh đề nghi vấn trong câu trần thuật)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(6) 我不知道这个人是男的还是女的。</div>
            <div class="example-pinyin">Wǒ bù zhīdào zhè ge rén shì nán de háishì nǚ de.</div>
            <div class="example-vi">Tôi không biết người này là nam hay nữ.</div>
          </div>
        </div>

        <!-- Ngữ pháp 2 -->
        <div class="grammar-card">
          <div class="grammar-title">2. Cách diễn đạt sự tồn tại: Câu tồn tại với trợ từ “着” (存在的表达)</div>
          <div class="grammar-formula">
            Khẳng định: Từ/cụm từ chỉ vị trí + Động từ + 着 + Số từ + Lượng từ + Danh từ<br>
            Phủ định: Từ/cụm từ chỉ vị trí + 没 + Động từ (着) + Danh từ (không có số lượng)
          </div>
          <div class="grammar-desc">
            Trong tiếng Hán, cấu trúc <strong>“Từ chỉ vị trí + Động từ + 着 + Cụm danh từ”</strong> được dùng để biểu thị ở một địa điểm nào đó đang tồn tại hoặc duy trì trạng thái của một người hay vật.<br>
            &bull; Động từ thường là động từ chỉ tư thế, động tác duy trì như: <strong>放 (đặt), 写 (viết), 坐 (ngồi), 住 (ở), 站 (đứng), 拿 (cầm)</strong>.<br>
            &bull; Cụm danh từ thường là sự vật <em>chưa xác định</em> (như 一本书, 几个人; không dùng 这本书, 那个人).<br>
            &bull; <strong>Dạng phủ định:</strong> Thêm <strong>“没”</strong> trước động từ. Đặc biệt khi phủ định, phía trước danh từ <em>không dùng số từ và lượng từ</em> nữa.
          </div>
          <div style="font-size: 13px; color: var(--text-sub); margin-bottom: 8px; font-weight: bold;">Bảng đối chiếu Khẳng định vs Phủ định:</div>
          <div class="example-item">
            <div class="interactive-text" style="color:#86efac; font-weight:600;">(+) 桌子上放着很多饮料。</div>
            <div class="example-pinyin">Zhuōzi shang fàngzhe hěnduō yǐnliào. (Trên bàn đang để rất nhiều thức uống.)</div>
            <div class="interactive-text" style="color:#f87171; font-weight:600; margin-top:4px;">(-) 桌子上没放着饮料。</div>
            <div class="example-pinyin">Zhuōzi shang méi fàngzhe yǐnliào. (Trên bàn không để đồ uống.)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#86efac; font-weight:600;">(+) 上面写着 320 元。</div>
            <div class="example-pinyin">Shàngmian xiězhe sān bǎi èrshí yuán. (Phía trên có ghi 320 tệ.)</div>
            <div class="interactive-text" style="color:#f87171; font-weight:600; margin-top:4px;">(-) 上面没写着多少钱。</div>
            <div class="example-pinyin">Shàngmian méi xiězhe duōshao qián. (Bên trên không có ghi bao nhiêu tiền.)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#86efac; font-weight:600;">(+) 我家楼上住着一个老师。</div>
            <div class="example-pinyin">Wǒ jiā lóu shang zhùzhe yí ge lǎoshī. (Tầng trên nhà tôi có một giáo viên đang ở.)</div>
            <div class="interactive-text" style="color:#f87171; font-weight:600; margin-top:4px;">(-) 我家楼上没住着老师。</div>
            <div class="example-pinyin">Wǒ jiā lóu shang méi zhùzhe lǎoshī. (Tầng trên nhà tôi không có giáo viên nào ở.)</div>
          </div>
        </div>

        <!-- Ngữ pháp 3 -->
        <div class="grammar-card">
          <div class="grammar-title">3. Trợ động từ “会” biểu thị khả năng trong tương lai (助动词 “会”)</div>
          <div class="grammar-formula">
            Chủ ngữ + 会 + Động từ / Cụm tính từ + (的)
          </div>
          <div class="grammar-desc">
            Trợ động từ <strong>“会”</strong> được dùng trong câu để biểu thị <strong>khả năng</strong> xảy ra của một sự việc, hành động trong tương lai hoặc đưa ra sự dự đoán, suy đoán chắc chắn.<br>
            Cuối câu thường có thể thêm trợ từ <strong>“的”</strong> để tăng ngữ khí khẳng định.
          </div>
          <div style="font-size: 13px; color: var(--text-sub); margin-bottom: 8px; font-weight: bold;">Các câu ví dụ chuẩn SGK:</div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(1) 你穿得那么少，会感冒的。</div>
            <div class="example-pinyin">Nǐ chuān de nàme shǎo, huì gǎnmào de.</div>
            <div class="example-vi">Bạn mặc phong phanh thế kia, sẽ bị cảm lạnh đấy. (Dự đoán khả năng)</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(2) 别担心，我会照顾好自己。</div>
            <div class="example-pinyin">Bié dānxīn, wǒ huì zhàogù hǎo zìjǐ.</div>
            <div class="example-vi">Đừng lo lắng, con/em sẽ biết tự chăm sóc tốt cho bản thân.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(3) 你不给他打电话吗？他会不高​​兴的。</div>
            <div class="example-pinyin">Nǐ bù gěi tā dǎ diànhuà ma? Tā huì bù gāoxìng de.</div>
            <div class="example-vi">Cậu không gọi điện thoại cho anh ấy à? Anh ấy sẽ không vui đâu.</div>
          </div>
          <div class="example-item">
            <div class="interactive-text" style="color:#fff; font-weight:600;">(4) 喝杯热茶会很舒服。</div>
            <div class="example-pinyin">Hē bēi rè chá huì hěn shūfu.</div>
            <div class="example-vi">Uống một cốc trà nóng sẽ cảm thấy rất dễ chịu.</div>
          </div>
        </div>
      </section>

      <!-- PHẦN 3: GHÉP TỪ CŨ TẠO TỪ MỚI & TỤC NGỮ TRUYỀN THỐNG -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>汉字与俗语: Ghép từ cũ tạo từ mới &amp; Tục ngữ (Trang 43 - 44)</span></div>
          <span style="font-size:13px; color:var(--accent);">Mở rộng kiến thức ngôn ngữ SGK</span>
        </div>

        <!-- Mở rộng chữ Hán -->
        <div style="margin-bottom: 20px;">
          <h4 style="color:#38bdf8; margin-bottom: 10px; font-size:15px;">1. 旧字新词: Cách thành lập từ mới từ các chữ Hán đã học</h4>
          <p class="section-desc">Cơ chế tư duy cấu tạo từ ghép trong tiếng Trung giúp ghi nhớ từ vựng siêu nhanh:</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">新鲜 + 牛奶 &rarr; 鲜奶</div>
              <div style="color: #38bdf8; font-size: 13px;">xiān nǎi</div>
              <div style="font-size: 13px; color: var(--text-sub);">Sữa tươi (rút gọn từ 新鲜: tươi và 牛奶: sữa bò).</div>
            </div>
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">冷 + 饮料 &rarr; 冷饮</div>
              <div style="color: #38bdf8; font-size: 13px;">lěng yǐn</div>
              <div style="font-size: 13px; color: var(--text-sub);">Đồ uống lạnh, thức uống giải khát mát lạnh (冷: lạnh + 饮料: thức uống).</div>
            </div>
            <div class="card" style="margin-bottom:0; border-left: 3px solid #38bdf8;">
              <div class="interactive-text" style="font-size: 16px; font-weight: bold; color: #fff;">上边 + 前面 &rarr; 上面</div>
              <div style="color: #38bdf8; font-size: 13px;">shàng mian</div>
              <div style="font-size: 13px; color: var(--text-sub);">Phía trên, bên trên (thay thế cho 上边).</div>
            </div>
          </div>
        </div>

        <!-- Tục ngữ truyền thống -->
        <div>
          <h4 style="color:#fbbf24; margin-bottom: 10px; font-size:15px;">2. 俗语: Tục ngữ Trung Hoa truyền thống</h4>
          <div class="card" style="border-left: 3px solid #fbbf24; background: rgba(251, 191, 36, 0.05);">
            <div class="interactive-text" style="font-size: 20px; font-weight: bold; color: #fbbf24;">茶好客常来</div>
            <div class="sentence-pinyin-full" style="color: #fde68a;">Chá hǎo kè cháng lái.</div>
            <div style="margin: 8px 0; font-size: 14px; color: #fff;">
              <strong>Dịch nghĩa đen:</strong> Trà mà thơm ngon thì khách sẽ thường xuyên lui tới thăm.
            </div>
            <div style="font-size: 13px; color: var(--text-sub); line-height: 1.6;">
              <strong>Ý nghĩa và ứng dụng:</strong> Câu tục ngữ mang nghĩa: chỉ cần chất lượng đồ vật/hàng hóa hoặc trà đãi khách thực sự thơm ngon chất lượng, thì khách hàng hay bạn bè sẽ tự khắc yêu thích và ghé lại thường xuyên. Trong kinh doanh, câu này ví von cho triết lý "hữu xạ tự nhiên hương", chú trọng chất lượng sản phẩm là cốt lõi.
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
        <p class="section-desc">Các chữ Hán có nhiều âm đọc quan trọng xuất hiện trong bài 3:</p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
          <!-- Chữ 着 -->
          <div class="card" style="border-top: 3px solid #f59e0b;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="interactive-text" style="font-size: 24px; font-weight: bold; color: #f59e0b;">着</span>
              <span style="font-size:12px; color:var(--text-sub);">Hán Việt: Trứ / Trước</span>
            </div>
            <div style="font-size: 13px; margin-bottom: 6px;">
              <span style="color:#38bdf8; font-weight:bold;">1. [ zhe ]</span>: Trợ từ động thái biểu thị trạng thái đang diễn ra hoặc duy trì (như: <strong>放着</strong> - đang đặt, <strong>坐着</strong> - đang ngồi, <strong>看着</strong> - đang nhìn).
            </div>
            <div style="font-size: 13px;">
              <span style="color:#38bdf8; font-weight:bold;">2. [ zháo ]</span>: Động từ biểu thị đạt được mục đích, cảm thụ (như: <strong>着急</strong> - sốt ruột, lo lắng; <strong>睡着</strong> - ngủ thiếp đi).
            </div>
          </div>

          <!-- Chữ 只 -->
          <div class="card" style="border-top: 3px solid #f59e0b;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="interactive-text" style="font-size: 24px; font-weight: bold; color: #f59e0b;">只</span>
              <span style="font-size:12px; color:var(--text-sub);">Hán Việt: Chỉ / Chích</span>
            </div>
            <div style="font-size: 13px; margin-bottom: 6px;">
              <span style="color:#38bdf8; font-weight:bold;">1. [ zhǐ ]</span>: Phó từ mang nghĩa là "chỉ" (như: <strong>只有一个</strong> - chỉ có một cái, <strong>只想</strong> - chỉ muốn, <strong>只要</strong> - chỉ cần).
            </div>
            <div style="font-size: 13px;">
              <span style="color:#38bdf8; font-weight:bold;">2. [ zhī ]</span>: Lượng từ dùng cho loài chim, con thú, hoặc một chiếc trong đôi (như: <strong>一只鸟</strong> - một con chim, <strong>一只手</strong> - một bàn tay).
            </div>
          </div>
        </div>
      </section>'''

# QUIZ_DATA
quiz_data = {
    "1": {"ans": "F", "explain": "Hai người đang bàn luận về chiếc quần (这条裤子), người nam chê hơi dài -> Hình F."},
    "2": {"ans": "B", "explain": "Cô gái gọi một cốc trà (一杯茶) -> Hình B: Bát canh/thức uống."},
    "3": {"ans": "A", "explain": "Người nam xác nhận có 6 chiếc áo sơ mi (一共六件衬衫) -> Hình A: Hàng áo sơ mi treo móc."},
    "4": {"ans": "C", "explain": "Rủ nhau đi mua hoa quả vì ở nhà chỉ còn 1 quả táo (买点儿水果/一个苹果) -> Hình C: Đĩa hoa quả."},
    "5": {"ans": "E", "explain": "Nam đi Bắc Kinh bằng máy bay sáng mai (明天上午的飞机) -> Hình E: Người đàn ông kéo vali cạnh máy bay."},
    "6": {"ans": "×", "explain": "Trong bài nói đó là bạn cùng lớp (同班同学), biết rõ tên là Bạch Tuyết và học rất giỏi -> Nhận định 'không quen biết' là Sai."},
    "7": {"ans": "√", "explain": "Trong bài so sánh: '比去年买的那条便宜多了' (rẻ hơn chiếc năm ngoái mua nhiều) -> Đúng."},
    "8": {"ans": "√", "explain": "Trong bài nói: '一边跑步一边听音乐' (vừa chạy bộ vừa nghe nhạc) -> Đúng."},
    "9": {"ans": "×", "explain": "Trong bài người nói chỉ dẫn rất rõ ràng: '就在进门右边放着' (để ngay bên phải cửa vào) -> Nhận định không biết là Sai."},
    "10": {"ans": "√", "explain": "Trong bài nói: '只喜欢吃肉' (chỉ thích ăn thịt) mặc dù bác sĩ khuyên ăn rau -> Nhận định cô ấy ăn rất ít rau là Đúng."},
    "11": {"ans": "A", "explain": "Nam nói '脚有点儿疼' (chân hơi đau) -> Chân không thoải mái (脚不舒服) -> Đáp án A."},
    "12": {"ans": "C", "explain": "Nữ bảo '太冰了' (quá lạnh/băng) nên bụng khó chịu không muốn ăn -> Đáp án C (太冷了)."},
    "13": {"ans": "B", "explain": "Nam nhờ '你帮我洗一下' chiếc áo sơ mi trắng bị bẩn -> Nữ phải giặt áo sơ mi (洗衬衫) -> Đáp án B."},
    "14": {"ans": "B", "explain": "Nữ nói '对不起，你打错了' (xin lỗi bạn gọi nhầm số rồi) -> Nam vô tình gọi nhầm máy (不小心打错了) -> Đáp án B."},
    "15": {"ans": "C", "explain": "Nam trả lời rõ ràng: '小丽刚才放在那儿的' (Tiểu Lệ vừa nãy đặt ở đó) -> Cà phê là của Tiểu Lệ -> Đáp án C."},
    "16": {"ans": "A", "explain": "Họ đang khen và hỏi giá của chiếc áo sơ mi (这件衬衫) -> Đáp án A."},
    "17": {"ans": "B", "explain": "Nữ nói '我记得我的手机放在桌子上了' -> Cô ấy đang tìm chiếc điện thoại (找手机) -> Đáp án B."},
    "18": {"ans": "A", "explain": "Nam hỏi '有没有冰绿茶？' -> Người nam muốn uống trà xanh (绿茶) -> Đáp án A."},
    "19": {"ans": "C", "explain": "Nữ bảo '我发烧了，头很疼' (con bị sốt, đau đầu) -> Cô ấy bị ốm/không khỏe (不舒服) -> Đáp án C."},
    "20": {"ans": "A", "explain": "Nam nói '这里的牛肉面不新鲜' -> Thịt bò không tươi -> Đáp án A."},
    "21": {"ans": "A", "explain": "Đáp án đúng là A. Câu 21 hỏi: '今天你怎么了？一直在睡觉' (Hôm nay cậu sao thế? Ngủ suốt) -> Đáp lại bằng A: '我今天不舒服，觉得很累' (Hôm nay tôi không khỏe, thấy rất mệt)."},
    "22": {"ans": "B", "explain": "Đáp án đúng là B. Câu 22 đáp: '啊，对，我记得你，你瘦了' (A, đúng rồi, tôi nhớ bạn rồi, bạn gầy đi) -> Phù hợp với câu B: '你还认识我吗？我们在中国见过' (Bạn còn nhận ra tôi không? Chúng mình từng gặp ở Trung Quốc)."},
    "23": {"ans": "D", "explain": "Đáp án đúng là D. Câu 23 nói: '桌子上放着饮料，你先喝点儿吧' (Trên bàn để đồ uống đấy, con uống trước đi) -> Phù hợp với câu D: '妈妈，我下课回来了' (Mẹ ơi, con tan học về rồi)."},
    "24": {"ans": "C", "explain": "Đáp án đúng là C. Câu 24 đáp: '我喜欢吃红苹果，我觉得红苹果甜' (Tôi thích ăn táo đỏ vì táo đỏ ngọt) -> Đáp lại câu hỏi C: '你喜欢吃红苹果还是绿苹果？' (Bạn thích ăn táo đỏ hay táo xanh?)."},
    "25": {"ans": "F", "explain": "Đáp án đúng là F. Câu 25 hỏi: '这种雨伞多少钱一把？' (Loại dù này bao nhiêu tiền một chiếc?) -> Đáp lại bằng F: '上面写着二十元一把' (Bên trên có ghi 20 tệ một chiếc)."},
    "26": {"ans": "C", "explain": "Đáp án đúng là C (还是: hay là). Dùng trong câu hỏi lựa chọn giữa '复习第三课' (ôn bài 3) hay '学习第四课' (học bài 4)."},
    "27": {"ans": "A", "explain": "Đáp án đúng là A (裤子: chiếc quần). Đi liền sau lượng từ '条' và động từ '穿' (mặc chiếc quần này đi leo núi)."},
    "28": {"ans": "F", "explain": "Đáp án đúng là F (小心: cẩn thận). Đồ uống rất nóng nên khi uống phải '小心点儿' (cẩn thận một chút)."},
    "29": {"ans": "B", "explain": "Đáp án đúng là B (或者: hoặc là). Dùng trong câu trần thuật lựa chọn '花茶或者绿茶都行' (trà hoa hoặc trà xanh đều được)."},
    "30": {"ans": "D", "explain": "Đáp án đúng là D (记得: nhớ). Kết hợp với phủ định thành '不记得了' (bạn không nhớ nữa à?)."},
    "31": {"ans": "B", "explain": "Đáp án đúng là B (没穿过几次: chưa mặc mấy lần). Trong bài nêu: '只穿了一次，就没再穿' (mới mặc đúng một lần rồi không mặc nữa)."},
    "32": {"ans": "B", "explain": "Đáp án đúng là B (上午吃苹果: ăn táo vào buổi sáng/trưa). Trong bài nêu: '早上和上午是吃苹果最好的时间' (buổi sáng và buổi trưa là thời gian ăn táo tốt nhất)."},
    "33": {"ans": "A", "explain": "Đáp án đúng là A (爱吃西瓜: thích ăn dưa hấu). Người nói khen dưa hấu ngon và ngọt, thắc mắc tại sao mọi người lại không thích dưa hấu."},
    "34": {"ans": "C", "explain": "Đáp án đúng là C (累了就吃点儿东西: mệt là ăn chút đồ ăn). Trong bài nêu: '下午工作累了的时候，大家都会吃点儿' (chiều làm việc mệt là mọi người đều ăn chút đồ)."},
    "35": {"ans": "B", "explain": "Đáp án đúng là B (周末喜欢去爬山: cuối tuần thích đi leo núi). Trong bài nêu: '周六周日我们事情不多，喜欢和学生们去爬爬山' (thứ Bảy Chủ Nhật việc không nhiều, thích cùng học sinh đi leo núi)."}
}

# MULTITONE
multitone = {
    "着": [
        {"py": "zhe", "vi": "Trợ từ ngữ thái biểu thị duy trì trạng thái (放着, 坐着, 拿着)"},
        {"py": "zháo", "vi": "Động từ đạt kết quả, cảm xúc (着急: sốt ruột, 睡着: ngủ say)"}
    ],
    "只": [
        {"py": "zhǐ", "vi": "Phó từ: chỉ, duy chỉ (只有, 只要, 只吃)"},
        {"py": "zhī", "vi": "Lượng từ: con vật, một chiếc trong đôi (一只鸟, 一只手)"}
    ],
    "会": [
        {"py": "huì", "vi": "Động từ năng nguyện: biết (会说), sẽ (会下雨), hội nghị (开会)"},
        {"py": "kuài", "vi": "Kế toán (会计)"}
    ]
}

# Import base dictionary from Bai_01 / Bai_02 and add Lesson 3 words
with open('Bai_02/index.html', 'r', encoding='utf-8') as f:
    c_b2 = f.read()

m_dict = re.search(r'const DICT = (\{.*?\});', c_b2)
base_dict = json.loads(m_dict.group(1)) if m_dict else {}

# Add Lesson 3 specific characters & words
l3_dict_additions = {
    "饮": {"py": "yǐn", "hv": "Ẩm", "vi": "Uống (trong 饮料, 冷饮)"},
    "料": {"py": "liào", "hv": "Liệu", "vi": "Nguyên liệu, thức liệu (trong 饮料, 材料)"},
    "裤": {"py": "kù", "hv": "Khố", "vi": "Quần (trong 裤子)"},
    "衫": {"py": "shān", "hv": "Sâm", "vi": "Áo mỏng (trong 衬衫)"},
    "衬": {"py": "chèn", "hv": "Sấn", "vi": "Lót, đệm (trong 衬衫)"},
    "甜": {"py": "tián", "hv": "Điềm", "vi": "Ngọt, vị ngọt"},
    "鲜": {"py": "xiān", "hv": "Tiên", "vi": "Tươi, mới (trong 新鲜, 鲜奶)"},
    "舒": {"py": "shū", "hv": "Thư", "vi": "Thư thả, thoải mái (trong 舒服)"},
    "服": {"py": "fu", "hv": "Phục", "vi": "Dễ chịu (舒服); quần áo (衣服)"},
    "绿": {"py": "lǜ", "hv": "Lục", "vi": "Màu xanh lá cây (绿茶, 绿苹果)"},
    "花": {"py": "huā", "hv": "Hoa", "vi": "Bông hoa; hoa văn; tiêu xài (花钱)"},
    "放": {"py": "fàng", "hv": "Phóng", "vi": "Đặt, để, thả (放着, 放学)"},
    "记": {"py": "jì", "hv": "Kí", "vi": "Ghi nhớ, nhớ (记得, 忘记)"},
    "得": {"py": "de", "hv": "Đắc", "vi": "Trợ từ kết cấu (跑得快); nhớ (记得)", "poly": True},
    "元": {"py": "yuán", "hv": "Nguyên", "vi": "Đồng tệ; đầu tiên (元旦)"},
    "或": {"py": "huò", "hv": "Hoặc", "vi": "Hoặc là (或者)"},
    "爬": {"py": "pá", "hv": "Ba", "vi": "Bò, trèo, leo (爬山)"},
    "山": {"py": "shān", "hv": "Sơn", "vi": "Núi, ngọn núi (爬山, 高山)"},
    "桌": {"py": "zhuō", "hv": "Trác", "vi": "Bàn, chiếc bàn (桌子)"},
    "心": {"py": "xīn", "hv": "Tâm", "vi": "Tim, lòng, ý tứ (小心, 开心)"},
    "冷": {"py": "lěng", "hv": "Lãnh", "vi": "Lạnh, buốt (冷饮, 太冷)"},
    "奶": {"py": "nǎi", "hv": "Nãi", "vi": "Sữa (牛奶, 鲜奶)"},
    "白": {"py": "bái", "hv": "Bạch", "vi": "Màu trắng (白衬衫, 白雪)"},
    "雪": {"py": "xuě", "hv": "Tuyết", "vi": "Tuyết, bông tuyết (白雪, 下雪)"},
    "条": {"py": "tiáo", "hv": "Điều", "vi": "Chiếc, sợi, con (lượng từ quần, cá, sông)"},
    "只": {"py": "zhǐ", "hv": "Chỉ / Chích", "vi": "Chỉ (zhǐ: 只有); con (zhī: 一只鸟)", "poly": True},
    "着": {"py": "zhe", "hv": "Trứ / Trước", "vi": "Trợ từ duy trì trạng thái (zhe); sốt ruột (zháo: 着急)", "poly": True},
    "脏": {"py": "zāng", "hv": "Tạng", "vi": "Bẩn, dơ dáy (衬衫脏了)"},
    "换": {"py": "huàn", "hv": "Hoán", "vi": "Đổi, thay đổi (换一件, 换车)"},
    "帅": {"py": "shuài", "hv": "Soái", "vi": "Đẹp trai, tuấn tú (穿得真帅)"},
    "客": {"py": "kè", "hv": "Khách", "vi": "Khách, khách khứa (茶好客常来, 客人)"},
    "常": {"py": "cháng", "hv": "Thường", "vi": "Thường xuyên, luôn luôn (常常, 常来)"},
    "冰": {"py": "bīng", "hv": "Băng", "vi": "Băng, đá lạnh (太冰了, 冰箱)"},
    "肚": {"py": "dù", "hv": "Đỗ", "vi": "Bụng, dạ dày (肚子)"},
    "箱": {"py": "xiāng", "hv": "Tương", "vi": "Hòm, rương, tủ (冰箱: tủ lạnh)"},
    "发": {"py": "fā", "hv": "Phát", "vi": "Phát ra, bị sốt (发烧, 发现)"},
    "烧": {"py": "shāo", "hv": "Thiêu", "vi": "Sốt, đốt cháy (发烧)"},
    "头": {"py": "tóu", "hv": "Đầu", "vi": "Đầu, cái đầu (头疼)"},
    "瘦": {"py": "shòu", "hv": "Sấu", "vi": "Gầy, ốm (你瘦了; ngược nghĩa với 胖)"},
    "袋": {"py": "dài", "hv": "Đại", "vi": "Túi, bao (口袋: túi áo/quần)"},
    "口": {"py": "kǒu", "hv": "Khẩu", "vi": "Miệng, túi (口袋)"},
    "疼": {"py": "téng", "hv": "Đông", "vi": "Đau, nhức (头疼, 脚疼)"},
    "晴": {"py": "qíng", "hv": "Tình", "vi": "Trời nắng, tạnh ráo (晴天)"},
    "阴": {"py": "yīn", "hv": "Âm", "vi": "Trời râm, u ám (阴天)"},
    "云": {"py": "yún", "hv": "Vân", "vi": "Mây (多云: nhiều mây)"},
    "菜": {"py": "cài", "hv": "Thái", "vi": "Rau, món ăn (新鲜蔬菜)"},
    "蔬": {"py": "shū", "hv": "Sơ", "vi": "Rau củ (蔬菜)"},
    "面": {"py": "miàn", "hv": "Diện / Miến", "vi": "Mặt; mì sợi (上面, 牛肉面)"},
    "红": {"py": "hóng", "hv": "Hồng", "vi": "Màu đỏ (红茶, 红苹果)"},
    "船": {"py": "chuán", "hv": "Thuyền", "vi": "Thuyền, tàu (小船)"},
    "河": {"py": "hé", "hv": "Hà", "vi": "Sông, dòng sông (河上)"},
    "床": {"py": "chuáng", "hv": "Sàng", "vi": "Giường (床上)"},
    "蓝": {"py": "lán", "hv": "Lam", "vi": "Màu xanh da trời, bóng rổ (篮球)"},
    "球": {"py": "qiú", "hv": "Cầu", "vi": "Bóng, quả cầu (打篮球)"},
    "篮": {"py": "lán", "hv": "Lam", "vi": "Rổ, giỏ (篮球)"}
}

base_dict.update(l3_dict_additions)

# Fill Template
output = template
output = output.replace('{{LESSON_NUM}}', '3')
output = output.replace('{{LESSON_TITLE}}', '桌子上放着很多饮料')
output = output.replace('{{LESSON_SUBTITLE}}', 'Trên bàn có rất nhiều thức uống (There are many drinks on the table)')
output = output.replace('{{AUDIO_SRC}}', 'audio.mp3')
output = output.replace('{{AUDIO_JUMP_BUTTONS}}', jump_buttons)
output = output.replace('{{TAB1_CONTENT}}', tab1_content)
output = output.replace('{{TAB2_CONTENT}}', tab2_content)
output = output.replace('{{TAB3_CONTENT}}', tab3_content)
output = output.replace('{{TAB4_CONTENT}}', tab4_content)
output = output.replace('{{DICT_JSON}}', json.dumps(base_dict, ensure_ascii=False))
output = output.replace('{{MULTITONE_JSON}}', json.dumps(multitone, ensure_ascii=False))
output = output.replace('{{QUIZ_DATA_JSON}}', json.dumps(quiz_data, ensure_ascii=False))

# Write Bai_03/index.html
with open('Bai_03/index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print('Successfully generated Bai_03/index.html via Master Template! Size:', len(output))
