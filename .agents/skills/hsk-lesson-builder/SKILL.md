---
name: hsk-lesson-builder
description: >-
  Xây dựng ứng dụng web tương tác (HTML5/CSS/JS) chuẩn cao cấp cho các bài học tiếng Trung HSK (HSK 1 đến HSK 6).
  Kích hoạt kỹ năng này khi người dùng yêu cầu tạo trang web học tập, luyện nghe, bài đọc, bài viết, từ vựng hoặc ngữ pháp cho các bài học tiếp theo (Bài 2, Bài 3, v.v.).
---

# HSK Lesson Builder (Quy trình chuẩn hóa chi tiết xây dựng Web học HSK tương tác)

Tài liệu này là **quy chuẩn kỹ thuật và nội dung bắt buộc** khi xây dựng trang web tương tác cho các bài học HSK 3 (từ Bài 1 đến Bài 20), được đúc kết từ phiên bản chuẩn hoàn thiện của **Bài 1** (`New folder/index.html` và `HSK3_Bai1_LuyenNghe.html`).

---

## 1. Cấu trúc thư mục & Quy chuẩn tài nguyên mỗi bài học

Mỗi bài học phải được đóng gói độc lập với đầy đủ tài nguyên cần thiết:

```text
e:\HSK3/
├── server.py                        # Máy chủ HTTP Range 206 (phục vụ tua audio tức thì)
├── chay_web_server.bat              # File kích hoạt server cổng 8000 cho điện thoại/iPad
├── char_dict_full.json              # Kho từ điển gốc 4.000+ chữ Hán
├── Bai_XX/ (hoặc folder bài học)
│   ├── index.html                   # Ứng dụng web Single-Page hoàn chỉnh của bài học
│   ├── audio.mp3                    # File âm thanh MP3 tương ứng của bài học đó
│   ├── pic_A.png                    # Tranh A cắt từ Sách bài tập (Phần 1 nghe)
│   ├── pic_B.png                    # Tranh B cắt từ Sách bài tập
│   ├── pic_C.png                    # Tranh C cắt từ Sách bài tập
│   ├── pic_D.png                    # Tranh D cắt từ Sách bài tập (hoặc tranh ví dụ)
│   ├── pic_E.png                    # Tranh E cắt từ Sách bài tập
│   └── pic_F.png                    # Tranh F cắt từ Sách bài tập
└── HSK3_BaiXX_LuyenNghe.html        # File web tại thư mục gốc để mở trực tiếp
```

> [!IMPORTANT]
> **TÀI NGUYÊN BẮT BUỘC RIÊNG BIỆT CHO MỖI BÀI HỌC:**
> 1. **File nghe (`audio.mp3`):** Mỗi bài có file nghe riêng trích xuất từ đĩa nghe giáo trình HSK 3.
> 2. **Bộ ảnh tranh (`pic_A.png` đến `pic_F.png`):** Phải dùng PyMuPDF (`fitz`) mở file `HSK-3-BT.pdf`, tìm đúng trang bài tập nghe Phần 1 của bài đó, cắt chính xác 6 ô tranh (A, B, C, D, E, F) và lưu ảnh chất lượng cao vào thư mục bài học.
> 3. **Xác định mốc giây nghe:** Nghe trước file `audio.mp3` để lấy chính xác 5 mốc thời gian (Mở đầu, Phần 1, Phần 2, Phần 3, Phần 4).

---

## 2. Chi tiết cấu trúc 4 Tab & Từng câu hỏi (Từ Câu 1 đến Câu 45)

---

### TAB 1: 🎧 BÀI NGHE (听力 - 20 câu trắc nghiệm tương tác)

> [!CAUTION]
> **NGUYÊN TẮC VÀNG CỦA BÀI NGHE:**  
> **Tuyệt đối KHÔNG hiển thị trước đáp án.** Người học phải tự nghe, tự bấm chọn chip, bấm nút `[Kiểm tra]` mới hiển thị phản hồi Đúng/Sai, và có nút `[Làm lại]` để xóa chọn làm lại.

> [!CRITICAL]
> **CẤM TUYỆT ĐỐI TRUYỀN CHUỖI ĐÁP ÁN & GIẢI THÍCH VÀO THẺ ONCLICK:**
> 1. Nút kiểm tra tất cả các câu nghe (1-20) BẮT BUỘC dùng: `<button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>`.
> 2. **TUYỆT ĐỐI CẤM** truyền chuỗi tiếng Việt hoặc nháy đơn/kép vào HTML `onclick="checkQuiz(1, 'A', '...')"` vì sẽ gây lỗi Javascript `SyntaxError: Unexpected identifier` khiến nút kiểm tra bị liệt hoàn toàn.
> 3. Toàn bộ đáp án (`ans`) và lời giải thích (`explain`) từ câu 1 đến câu 35 bắt buộc được khai báo tập trung trong đối tượng JavaScript `QUIZ_DATA`.

#### A. Thanh Audio & Mốc thời gian nhảy đoạn:
* Thẻ audio chuẩn nạp trước metadata:
  ```html
  <audio id="main-audio" controls preload="auto" src="audio.mp3">
    Trình duyệt của bạn không hỗ trợ phát âm thanh.
  </audio>
  ```
* 5 nút nhảy đoạn tương ứng với file MP3 của bài học:
  ```html
  <div class="jump-buttons">
    <button class="jump-btn" onclick="jumpAudio(0, this)">▶ 00:00 Mở đầu</button>
    <button class="jump-btn" onclick="jumpAudio(t1, this)">▶ mm:ss Phần 1 (1-5)</button>
    <button class="jump-btn" onclick="jumpAudio(t2, this)">▶ mm:ss Phần 2 (6-10)</button>
    <button class="jump-btn" onclick="jumpAudio(t3, this)">▶ mm:ss Phần 3 (11-15)</button>
    <button class="jump-btn" onclick="jumpAudio(t4, this)">▶ mm:ss Phần 4 (16-20)</button>
  </div>
  ```
* Nút được bấm sẽ tự động có class `.active` sáng đèn viền cyan `#38bdf8`.

---

#### B. Phần 1: 第 1 - 5 题 (5 câu đối thoại & tranh minh họa A - F)
* **Yêu cầu đề bài:** `听对话，选择与对话内容一致的图片 (Nghe đối thoại, chọn tranh tương ứng A - F):`
* **Lưới 6 tranh minh họa:**
  ```html
  <div class="pics-grid">
    <div class="pic-item"><img src="pic_A.png" alt="Tranh A"><div class="pic-label">Hình A: [Hành động/Nội dung]</div></div>
    <div class="pic-item"><img src="pic_B.png" alt="Tranh B"><div class="pic-label">Hình B: [Hành động/Nội dung]</div></div>
    <div class="pic-item"><img src="pic_C.png" alt="Tranh C"><div class="pic-label">Hình C: [Hành động/Nội dung]</div></div>
    <div class="pic-item"><img src="pic_D.png" alt="Tranh D"><div class="pic-label">Hình D: [Hành động/Nội dung]</div></div>
    <div class="pic-item"><img src="pic_E.png" alt="Tranh E"><div class="pic-label">Hình E: [Hành động/Nội dung]</div></div>
    <div class="pic-item"><img src="pic_F.png" alt="Tranh F"><div class="pic-label">Hình F: [Hành động/Nội dung]</div></div>
  </div>
  ```

> [!CAUTION]
> **QUY CHUẨN BẮT BUỘC PHẦN 1 NGHE (CÂU 1 - 5):**
> 1. Mỗi câu có thẻ card: `<div class="card" id="card-{{NUM}}">`.
> 2. Lượt thoại phải gồm 3 dòng: Chữ Hán (`.interactive-text`), Phiên âm (`.pinyin-line`), Dịch nghĩa (`.trans-line`).
> 3. Lưới chọn gồm 6 chip A - F dùng `.options-grid.grid-pics-options` (hoặc `.options-grid`).
> 4. Cụm nút thao tác `.quiz-actions` và hộp giải thích `.sentence-trans-box` có `id="transbox-{{NUM}}"`.

* **Mẫu HTML chuẩn từng câu (Câu 1 $\rightarrow$ Câu 5):**
```html
<div class="card" id="card-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="speaker-line">
    <span class="speaker male">男:</span>
    <span class="interactive-text">{{LINE1_ZH}}</span>
    <span class="pinyin-line">{{LINE1_PY}}</span>
    <span class="trans-line">{{LINE1_VI}}</span>
  </div>
  <div class="speaker-line">
    <span class="speaker female">女:</span>
    <span class="interactive-text">{{LINE2_ZH}}</span>
    <span class="pinyin-line">{{LINE2_PY}}</span>
    <span class="trans-line">{{LINE2_VI}}</span>
  </div>
  <div class="options-grid grid-pics-options">
    <div class="option-chip" onclick="selectOption({{NUM}}, 'A')"><span class="chip-letter">A</span> Hình A: {{LABEL_A}}</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'B')"><span class="chip-letter">B</span> Hình B: {{LABEL_B}}</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'C')"><span class="chip-letter">C</span> Hình C: {{LABEL_C}}</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'D')"><span class="chip-letter">D</span> Hình D: {{LABEL_D}}</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'E')"><span class="chip-letter">E</span> Hình E: {{LABEL_E}}</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'F')"><span class="chip-letter">F</span> Hình F: {{LABEL_F}}</div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>
    <button class="btn-reset" onclick="resetQuiz({{NUM}})">Làm lại</button>
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans({{NUM}})">👁 Dịch câu &amp; Giải thích</button>
  </div>
  <div class="sentence-trans-box" id="transbox-{{NUM}}">
    <div class="sentence-pinyin-full">{{FULL_PINYIN}}</div>
    <strong>Dịch nghĩa:</strong> {{FULL_TRANS}}<br>
    <strong>Giải thích:</strong> Đáp án đúng là <strong>{{CORRECT_VAL}}</strong>: {{EXPLAIN_ANALYSIS}}
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

#### C. Phần 2: 第 6 - 10 题 (5 câu đoạn văn ngắn & phán đoán Đúng [ √ ] / Sai [ × ])
* **Yêu cầu đề bài:** `听短文或对话，判断对错 (Nghe đoạn văn hoặc câu nói, phán đoán Đúng [ √ ] hay Sai [ × ]):`

> [!CAUTION]
> **QUY CHUẨN BẮT BUỘC PHẦN 2 NGHE (CÂU 6 - 10):**
> 1. Mỗi câu có thẻ card: `<div class="card" id="card-{{NUM}}">`.
> 2. Đoạn nghe gồm lời thoại nhân vật kèm `.pinyin-line` và `.trans-line`.
> 3. Câu nhận định BẮT BUỘC có ký hiệu `★` phía trước (bọc trong `.listening-statement.interactive-text`).
> 4. Lưới lựa chọn BẮT BUỘC dùng `.options-grid.grid-true-false` gồm đúng 2 chip:
>    `<div class="option-chip" onclick="selectOption({{NUM}}, '√')"><span class="chip-letter">√</span> Đúng (√)</div>`
>    `<div class="option-chip" onclick="selectOption({{NUM}}, '×')"><span class="chip-letter">×</span> Sai (×)</div>`
> 5. **CẤM TUYỆT ĐỐI** truyền `'true'` hoặc `'false'` vào `selectOption`! Bắt buộc dùng `'√'` và `'×'`.
> 6. Nút kiểm tra dùng `<button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>`.
> 7. Hộp giải thích chỉ rõ sự tương đồng (chọn Đúng √) hoặc điểm mâu thuẫn (chọn Sai ×).

* **Mẫu HTML chuẩn từng câu (Câu 6 $\rightarrow$ Câu 10):**
```html
<div class="card" id="card-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="speaker-line">
    <span class="interactive-text">{{PASSAGE_ZH}}</span>
    <span class="pinyin-line">{{PASSAGE_PY}}</span>
    <span class="trans-line">{{PASSAGE_VI}}</span>
  </div>
  <div class="listening-statement">
    <span class="interactive-text">&bull; ★ {{STATEMENT_ZH}}</span>
    <span class="pinyin-line">{{STATEMENT_PY}}</span>
    <span class="trans-line">{{STATEMENT_VI}}</span>
  </div>
  <div class="options-grid grid-true-false">
    <div class="option-chip" onclick="selectOption({{NUM}}, '√')"><span class="chip-letter">√</span> Đúng (√)</div>
    <div class="option-chip" onclick="selectOption({{NUM}}, '×')"><span class="chip-letter">×</span> Sai (×)</div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>
    <button class="btn-reset" onclick="resetQuiz({{NUM}})">Làm lại</button>
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans({{NUM}})">👁 Dịch câu &amp; Giải thích</button>
  </div>
  <div class="sentence-trans-box" id="transbox-{{NUM}}">
    <div class="sentence-pinyin-full">{{FULL_PINYIN}}</div>
    <strong>Dịch đối chiếu:</strong> Lời thoại: "{{PASSAGE_VI}}" vs Nhận định: "{{STATEMENT_VI}}"<br>
    <strong>Giải thích:</strong> Đáp án đúng là <strong>{{CORRECT_VAL}}</strong>: {{EXPLAIN_ANALYSIS}}
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

#### D. Phần 3: 第 11 - 15 题 (5 câu đối thoại ngắn 2 lượt & chọn đáp án A, B, C)
* **Yêu cầu đề bài:** `听短对话，选择正确答案 (Nghe đối thoại ngắn 2 lượt, chọn đáp án đúng A, B, C):`

> [!CAUTION]
> **QUY CHUẨN BẮT BUỘC PHẦN 3 NGHE (CÂU 11 - 15):**
> 1. Mỗi câu có thẻ card: `<div class="card" id="card-{{NUM}}">`.
> 2. Gồm 2 lượt thoại đối đáp nam - nữ.
> 3. Câu hỏi người dẫn BẮT BUỘC bắt đầu bằng `问:` hoặc `问：` (bọc trong `.listening-question`).
> 4. Lưới lựa chọn BẮT BUỘC dùng `.options-grid.grid-abc` gồm 3 chip A, B, C.
> 5. CHIP LỰA CHỌN CHỈ HIỂN THỊ CHỮ HÁN trong `<span class="interactive-text">`, TUYỆT ĐỐI không hiển thị sẵn pinyin hay dịch nghĩa tiếng Việt trong chip.

* **Mẫu HTML chuẩn từng câu (Câu 11 $\rightarrow$ Câu 15):**
```html
<div class="card" id="card-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="speaker-line">
    <span class="speaker male">男:</span>
    <span class="interactive-text">{{LINE1_ZH}}</span>
    <span class="pinyin-line">{{LINE1_PY}}</span>
    <span class="trans-line">{{LINE1_VI}}</span>
  </div>
  <div class="speaker-line">
    <span class="speaker female">女:</span>
    <span class="interactive-text">{{LINE2_ZH}}</span>
    <span class="pinyin-line">{{LINE2_PY}}</span>
    <span class="trans-line">{{LINE2_VI}}</span>
  </div>
  <div class="listening-question">
    <span class="interactive-text">问: {{QUESTION_ZH}}</span>
    <span class="pinyin-line">{{QUESTION_PY}}</span>
    <span class="trans-line">{{QUESTION_VI}}</span>
  </div>
  <div class="options-grid grid-abc">
    <div class="option-chip" onclick="selectOption({{NUM}}, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">{{OPT_A}}</span></div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">{{OPT_B}}</span></div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">{{OPT_C}}</span></div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>
    <button class="btn-reset" onclick="resetQuiz({{NUM}})">Làm lại</button>
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans({{NUM}})">👁 Dịch câu &amp; Giải thích</button>
  </div>
  <div class="sentence-trans-box" id="transbox-{{NUM}}">
    <div class="sentence-pinyin-full">{{FULL_PINYIN}}</div>
    <strong>Dịch câu hỏi &amp; các lựa chọn:</strong><br>
    &bull; Câu hỏi: {{QUESTION_VI}}<br>
    &bull; A. {{OPT_A}} ({{OPT_A_PY}}): {{OPT_A_VI}}<br>
    &bull; B. {{OPT_B}} ({{OPT_B_PY}}): {{OPT_B_VI}}<br>
    &bull; C. {{OPT_C}} ({{OPT_C_PY}}): {{OPT_C_VI}}<br>
    <strong>Giải thích:</strong> Đáp án đúng là <strong>{{CORRECT_VAL}}</strong>: {{EXPLAIN_ANALYSIS}}
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

#### E. Phần 4: 第 16 - 20 题 (5 câu đối thoại dài 4 lượt & chọn đáp án A, B, C)
* **Yêu cầu đề bài:** `听长对话，选择正确答案 (Nghe đối thoại dài 4 lượt, chọn đáp án đúng A, B, C):`

> [!CAUTION]
> **QUY CHUẨN BẮT BUỘC PHẦN 4 NGHE (CÂU 16 - 20):**
> 1. Mỗi câu có thẻ card: `<div class="card" id="card-{{NUM}}">`.
> 2. Gồm 4 lượt thoại đối đáp luân phiên giữa Nam và Nữ (mỗi lượt đầy đủ 3 dòng Hán, Pinyin, Dịch).
> 3. Câu hỏi người dẫn BẮT BUỘC có `问:` hoặc `问：` (bọc trong `.listening-question`).
> 4. Lưới lựa chọn BẮT BUỘC dùng `.options-grid.grid-abc` gồm 3 chip A, B, C (chữ Hán bọc trong `interactive-text`).
> 5. Hộp giải thích dịch chi tiết câu hỏi, dịch từng lựa chọn và phân tích mạch hội thoại dẫn đến đáp án đúng.

* **Mẫu HTML chuẩn từng câu (Câu 16 $\rightarrow$ Câu 20):**
```html
<div class="card" id="card-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="speaker-line">
    <span class="speaker male">男:</span>
    <span class="interactive-text">{{LINE1_ZH}}</span>
    <span class="pinyin-line">{{LINE1_PY}}</span>
    <span class="trans-line">{{LINE1_VI}}</span>
  </div>
  <div class="speaker-line">
    <span class="speaker female">女:</span>
    <span class="interactive-text">{{LINE2_ZH}}</span>
    <span class="pinyin-line">{{LINE2_PY}}</span>
    <span class="trans-line">{{LINE2_VI}}</span>
  </div>
  <div class="speaker-line">
    <span class="speaker male">男:</span>
    <span class="interactive-text">{{LINE3_ZH}}</span>
    <span class="pinyin-line">{{LINE3_PY}}</span>
    <span class="trans-line">{{LINE3_VI}}</span>
  </div>
  <div class="speaker-line">
    <span class="speaker female">女:</span>
    <span class="interactive-text">{{LINE4_ZH}}</span>
    <span class="pinyin-line">{{LINE4_PY}}</span>
    <span class="trans-line">{{LINE4_VI}}</span>
  </div>
  <div class="listening-question">
    <span class="interactive-text">问: {{QUESTION_ZH}}</span>
    <span class="pinyin-line">{{QUESTION_PY}}</span>
    <span class="trans-line">{{QUESTION_VI}}</span>
  </div>
  <div class="options-grid grid-abc">
    <div class="option-chip" onclick="selectOption({{NUM}}, 'A')"><span class="chip-letter">A</span> <span class="interactive-text">{{OPT_A}}</span></div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'B')"><span class="chip-letter">B</span> <span class="interactive-text">{{OPT_B}}</span></div>
    <div class="option-chip" onclick="selectOption({{NUM}}, 'C')"><span class="chip-letter">C</span> <span class="interactive-text">{{OPT_C}}</span></div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkQuiz({{NUM}})">Kiểm tra</button>
    <button class="btn-reset" onclick="resetQuiz({{NUM}})">Làm lại</button>
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans({{NUM}})">👁 Dịch câu &amp; Giải thích</button>
  </div>
  <div class="sentence-trans-box" id="transbox-{{NUM}}">
    <div class="sentence-pinyin-full">{{FULL_PINYIN}}</div>
    <strong>Dịch câu hỏi &amp; các lựa chọn:</strong><br>
    &bull; Câu hỏi: {{QUESTION_VI}}<br>
    &bull; A. {{OPT_A}} ({{OPT_A_PY}}): {{OPT_A_VI}}<br>
    &bull; B. {{OPT_B}} ({{OPT_B_PY}}): {{OPT_B_VI}}<br>
    &bull; C. {{OPT_C}} ({{OPT_C_PY}}): {{OPT_C_VI}}<br>
    <strong>Giải thích:</strong> Đáp án đúng là <strong>{{CORRECT_VAL}}</strong>: {{EXPLAIN_ANALYSIS}}
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

### TAB 2: 📖 BÀI ĐỌC (阅读 - 15 câu trắc nghiệm tương tác)

#### A. Phần 1: 第 21 - 25 题 (Ghép câu đối ứng phù hợp A - F)

> [!CRITICAL]
> **QUY CHUẨN ĐỊNH DẠNG CHIP CÂU 21 - 25 (CHỐNG LỖI LẶP CHỮ CÁI):**
> 1. Phải có khung tham khảo `.reading-ref-box` chứa đầy đủ 6 câu đối ứng A – F (câu ví dụ mẫu có class `.is-example`).
> 2. Ở từng câu 21 – 25, lưới lựa chọn BẮT BUỘC dùng class `.options-grid.grid-letters` (độ rộng chip 65px).
> 3. Cấu trúc mỗi chip BẮT BUỘC duy nhất là:
>    `<div class="option-chip" onclick="selectOption('{{NUM}}', 'A')" data-q="{{NUM}}" data-val="A"><span class="chip-letter">A</span> A</div>`
>    **CẤM TUYỆT ĐỐI:**
>    - CẤM thêm ngoặc vuông hoặc ngoặc đơn: `[A] A`, `(A) A`, hoặc `[A]`.
>    - CẤM lặp lại chữ cái trong text nội dung (ví dụ: `<span>A</span> [A] A` làm xuất hiện 3 lần chữ A: `(A) [A] A`).
>    - CẤM nhét cả câu văn dài vào chip. Duy nhất format `<span class="chip-letter">A</span> A`.

* **Mẫu HTML chuẩn của Khung tham khảo A - F:**
```html
<div class="reading-ref-box">
  <div class="reading-ref-title">DANH SÁCH CÁC CÂU LỰA CHỌN (A - F):</div>
  <div class="reading-ref-item">
    <span class="chip-letter">A</span>
    <div>
      <span class="interactive-text">[Câu tiếng Trung A]</span>
      <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
      <div class="sentence-trans-box">
        <div class="sentence-pinyin-full">[Pinyin]</div>
        <div>[Dịch nghĩa tiếng Việt]</div>
      </div>
    </div>
  </div>
  <!-- Các câu B, C, D, E, F tương tự; câu ví dụ có thêm class .is-example -->
</div>
```

* **Mẫu HTML chuẩn từng câu (Câu 21 $\rightarrow$ Câu 25):**
```html
<div class="card" id="q-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="interactive-text">{{QUESTION_SENTENCE}}</div>
  <div class="sentence-footer">
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
    <div class="sentence-trans-box">
      <div class="sentence-pinyin-full">{{SENTENCE_PINYIN}}</div>
      <div>{{SENTENCE_TRANS}}</div>
    </div>
  </div>
  <!-- Lưới chip chữ cái gọn gàng chuẩn 65px -->
  <div class="options-grid grid-letters">
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'A')" data-q="{{NUM}}" data-val="A"><span class="chip-letter">A</span> A</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'B')" data-q="{{NUM}}" data-val="B"><span class="chip-letter">B</span> B</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'C')" data-q="{{NUM}}" data-val="C"><span class="chip-letter">C</span> C</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'D')" data-q="{{NUM}}" data-val="D"><span class="chip-letter">D</span> D</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'E')" data-q="{{NUM}}" data-val="E"><span class="chip-letter">E</span> E</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'F')" data-q="{{NUM}}" data-val="F"><span class="chip-letter">F</span> F</div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkAnswer('{{NUM}}')">Kiểm tra đáp án</button>
    <button class="btn-reset" onclick="resetAnswer('{{NUM}}')">Làm lại</button>
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

#### B. Phần 2: 第 26 - 30 题 (Điền từ vào chỗ trống A - F)

> [!CAUTION]
> **QUY CHUẨN BẮT BUỘC PHẦN 2 ĐỌC (CÂU 26 - 30):**
> 1. Phải có khung Ngân hàng từ vựng `.reading-vocab-box` chứa lưới `.reading-vocab-grid` với các thẻ `.reading-vocab-card`.
> 2. Đề bài phải có chỗ trống `<span id="blank-display-{{NUM}}" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>`.
> 3. Lưới lựa chọn BẮT BUỘC dùng `.options-grid.grid-vocab` (`max-width: 550px`) và truyền tham số điền từ `selectOption('{{NUM}}', 'A', '{{WORD}}')` để khi click từ vựng tự động điền vào chỗ trống!

* **Mẫu HTML chuẩn của Khung Ngân hàng từ vựng A - F:**
```html
<div class="reading-vocab-box">
  <div class="reading-vocab-title">NGÂN HÀNG TỪ VỰNG:</div>
  <div class="reading-vocab-grid">
    <div class="reading-vocab-card">
      <span class="chip-letter">A</span> <strong class="interactive-text">[Từ vựng A]</strong> <span style="font-size:12px; color:#94a3b8;">([pinyin]: [nghĩa])</span>
    </div>
    <!-- Các từ B, C, D, E, F tương tự -->
  </div>
</div>
```

* **Mẫu HTML chuẩn từng câu (Câu 26 $\rightarrow$ Câu 30):**
```html
<div class="card" id="q-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="interactive-text">{{SENTENCE_PRE}} <span id="blank-display-{{NUM}}" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span> {{SENTENCE_POST}}</div>
  <div class="sentence-footer">
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
    <div class="sentence-trans-box">
      <div class="sentence-pinyin-full">{{SENTENCE_PINYIN}}</div>
      <div>{{SENTENCE_TRANS}}</div>
    </div>
  </div>
  <!-- Lưới chip từ vựng gọn gàng chuẩn 90px có điền từ tự động -->
  <div class="options-grid grid-vocab">
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'A', '{{WORD_A}}')" data-q="{{NUM}}" data-val="A"><span class="chip-letter">A</span> {{WORD_A}}</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'B', '{{WORD_B}}')" data-q="{{NUM}}" data-val="B"><span class="chip-letter">B</span> {{WORD_B}}</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'C', '{{WORD_C}}')" data-q="{{NUM}}" data-val="C"><span class="chip-letter">C</span> {{WORD_C}}</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'D', '{{WORD_D}}')" data-q="{{NUM}}" data-val="D"><span class="chip-letter">D</span> {{WORD_D}}</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'E', '{{WORD_E}}')" data-q="{{NUM}}" data-val="E"><span class="chip-letter">E</span> {{WORD_E}}</div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'F', '{{WORD_F}}')" data-q="{{NUM}}" data-val="F"><span class="chip-letter">F</span> {{WORD_F}}</div>
  </div>
  <div class="quiz-actions">
    <button class="btn-check" onclick="checkAnswer('{{NUM}}')">Kiểm tra đáp án</button>
    <button class="btn-reset" onclick="resetAnswer('{{NUM}}')">Làm lại</button>
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```

---

#### C. Phần 3: 第 31 - 35 题 (Đọc hiểu đoạn văn ngắn & chọn A, B, C)
* **Khung mẫu HTML bắt buộc (Canonical Template) - Tuyệt đối không được giản lược:**
```html
<div class="card" id="q-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="reading-passage-box interactive-text">
    {{PARAGRAPH}}
  </div>

  <div class="reading-question-title interactive-text">
    &bull; {{QUESTION}}:
  </div>

  <!-- Lựa chọn đáp án A, B, C (CHỈ HIỂN THỊ CHỮ HÁN THEO QUY CHUẨN) -->
  <div class="options-grid" style="margin-top: 14px;">
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'A')" data-q="{{NUM}}" data-val="A">
      <span class="chip-letter">A</span>
      <div><span class="interactive-text" style="font-size: 17px;">{{OPT_A}}</span></div>
    </div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'B')" data-q="{{NUM}}" data-val="B">
      <span class="chip-letter">B</span>
      <div><span class="interactive-text" style="font-size: 17px;">{{OPT_B}}</span></div>
    </div>
    <div class="option-chip" onclick="selectOption('{{NUM}}', 'C')" data-q="{{NUM}}" data-val="C">
      <span class="chip-letter">C</span>
      <div><span class="interactive-text" style="font-size: 17px;">{{OPT_C}}</span></div>
    </div>
  </div>

  <!-- Hộp dịch phải nằm trong .sentence-footer ĐẶT PHÍA TRÊN .quiz-actions -->
  <div class="sentence-footer">
    <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
    <div class="sentence-trans-box">
      <div class="sentence-pinyin-full">{{PARAGRAPH_PINYIN}}</div>
      <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> {{PARAGRAPH_TRANS}}</div>
      <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
        <strong>Dịch các lựa chọn:</strong><br>
        &bull; <strong>A. {{OPT_A}}</strong> ({{OPT_A_PINYIN}}): {{OPT_A_TRANS}}<br>
        &bull; <strong>B. {{OPT_B}}</strong> ({{OPT_B_PINYIN}}): {{OPT_B_TRANS}}<br>
        &bull; <strong>C. {{OPT_C}}</strong> ({{OPT_C_PINYIN}}): {{OPT_C_TRANS}}<br>
      </div>
    </div>
  </div>

  <div class="quiz-actions">
    <button class="btn-check" onclick="checkAnswer('{{NUM}}')">Kiểm tra đáp án</button>
    <button class="btn-reset" onclick="resetAnswer('{{NUM}}')">Làm lại</button>
  </div>
  <div class="feedback-box" id="feedback-{{NUM}}"></div>
</div>
```
> [!CAUTION]
> **QUY TẮC BẮT BUỘC VỚI CÂU 31 - 35:**
> 1. Mỗi phương án A, B, C trong hộp dịch bắt buộc phải có đầy đủ: **Chữ Hán + Phiên âm Pinyin trong ngoặc đơn `(...)` + Bản dịch nghĩa tiếng Việt**. Tuyệt đối không được viết tắt thành một dòng thô sơ không có pinyin.
> 2. Thẻ `<div class="sentence-footer">` bắt buộc phải đặt **phía trên** `<div class="quiz-actions">`, không được nhét vào trong `quiz-actions`.

---

### TAB 3: ✍️ BÀI VIẾT (书写 - 10 câu)

#### A. Phần 1: 第 36 - 40 题 (Sắp xếp các từ ngữ rời rạc thành câu hoàn chỉnh)

* **Mẫu HTML chuẩn từng câu (Câu 36 $\rightarrow$ Câu 40):**
```html
<div class="card" id="q-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="writing-scramble-text interactive-text">{{SCRAMBLED_WORDS}}</div>
  <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
  <div class="sentence-trans-box">
    <div class="writing-correct-answer interactive-text">{{CORRECT_SENTENCE}}</div>
    <div class="sentence-pinyin-full">{{SENTENCE_PINYIN}}</div>
    <div>{{SENTENCE_TRANS}}</div>
    <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ghi chú: {{GRAMMAR_NOTE}}</div>
  </div>
</div>
```

---

#### B. Phần 2: 第 41 - 45 题 (Nhìn phiên âm Pinyin điền chữ Hán vào chỗ trống)

* **Mẫu HTML chuẩn từng câu (Câu 41 $\rightarrow$ Câu 45):**
```html
<div class="card" id="q-{{NUM}}">
  <span class="card-num">Câu {{NUM}}</span>
  <div class="writing-fill-sentence interactive-text">
    {{SENTENCE_WITH_PINYIN_BLANK}}
  </div>
  <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">{{SENTENCE_TRANS_HINT}}</div>
  <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
  <div class="sentence-trans-box">
    <div>Chữ Hán cần điền: <span class="writing-target-hanzi interactive-text">{{TARGET_HANZI}}</span> <span class="sentence-pinyin-full">({{TARGET_PINYIN}})</span> - Hán Việt: {{TARGET_HV}}</div>
    <div style="margin-top:4px;">&bull; Từ ghép / Cụm từ: <strong>{{COMPOUND_WORD}}</strong> ({{COMPOUND_MEANING}}).</div>
    <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">{{FULL_SENTENCE}} ({{FULL_PINYIN}})</div>
  </div>
</div>
```

---

### TAB 4: 📚 TỪ VỰNG & NGỮ PHÁP (Sách Giáo Khoa)

> [!IMPORTANT]
> **NGUỒN DỮ LIỆU BẮT BUỘC:**
> Toàn bộ nội dung Tab 4 bắt buộc phải lấy chính xác từ file **`FILE TÀI LIỆU/HSK 3 Sách giáo khoa.pdf`** tương ứng với bài học đang triển khai:
> - Tra cứu số trang bài học tại **Mục lục (Trang 8 - 9 của file PDF)**.
> - Ví dụ: Bài 1 (Trang 17 - 25), Bài 2 (Trang 27 - 35), Bài 3 (Trang 36 - 44), v.v.
> - Tuyệt đối không để sót hoặc dùng lại nội dung của bài học trước.

Tab 4 tập trung trọng tâm vào Từ vựng & Ngữ pháp, bao gồm **4 phần chuẩn mực** (không bao gồm nội dung Bài khóa):

#### A. Bảng Từ Mới Chính Thức (生词) & Danh Từ Riêng (专有名词)
* Lấy toàn bộ từ mới xuất hiện trong SGK của bài (Ví dụ: Bài 1 có 15 từ, Bài 2 có 18 từ + 2 danh từ riêng).
* Bảng tra cứu đẹp mắt, gồm 5 cột chuẩn:
  1. **STT:** Số thứ tự từ mới trong bài (1, 2, 3...).
  2. **Chữ Hán:** Bọc trong `interactive-text` để có thể rê chuột/chạm tra từ điển tooltip.
  3. **Pinyin:** Kèm thanh điệu chuẩn quốc tế (màu xanh dương nổi bật).
  4. **Từ loại:** Danh từ (名/dt.), Động từ (动/đgt.), Tính từ (形/tt.), Phó từ (副/phó.), Lượng từ (量/lượng.), Trợ từ (助), v.v.
  5. **Nghĩa tiếng Việt:** Dịch nghĩa sát giáo trình kèm sắc thái biểu đạt.
* Danh từ riêng (专有名词): Trình bày rõ họ tên nhân vật hoặc địa danh trong bài (Ví dụ: `周` - họ Chu, `周明` - Chu Minh).

#### B. Trọng Điểm Ngữ Pháp Chính Thức (注释)
* Trích xuất đầy đủ toàn bộ các điểm ngữ pháp chính thức trong SGK của bài (từ 2 đến 4 chủ điểm ngữ pháp):
  - Tên cấu trúc và công thức ngữ pháp rõ ràng.
  - Phân tích chi tiết ý nghĩa ngữ pháp, bản chất và quy tắc áp dụng (đặc biệt là quy tắc vị trí tân ngữ nơi chốn vs tân ngữ sự vật đối với bổ ngữ xu hướng, hoặc quy tắc 2 chủ ngữ đối với cấu trúc nối tiếp).
  - Toàn bộ các câu ví dụ minh họa chuẩn trong SGK kèm phiên âm Pinyin và dịch nghĩa tiếng Việt.
  - (Nếu có) Các mẫu câu hỏi phản vấn hoặc các trường hợp ngoại lệ.

#### C. Mở Rộng Ghép Từ Cũ Tạo Từ Mới (旧字新词) & Tục Ngữ (俗语)
* Trích xuất chính xác từ trang cuối cùng của bài học trong SGK:
  - **旧字新词 (Cách thành lập từ mới):** Giải thích cách kết hợp các chữ Hán đã học để tạo thành từ vựng mới (Ví dụ: `办公室 + 大楼 → 办公楼`, `外边 + 出去 → 外出`, `中午 + 睡觉 → 午觉`).
  - **俗语 (Tục ngữ truyền thống):** Trích dẫn câu tục ngữ trong bài kèm phiên âm Pinyin, giải thích ý nghĩa đen, nghĩa bóng và bài học sức khỏe/đời sống (Ví dụ: `饭后百步走，活到九十九`).

#### D. Chuyên Đề Chữ Đa Âm Tự (多音字)
* Tổng hợp các chữ trong bài có từ 2 cách phát âm trở lên (như `把` (bǎ / bà), `行` (xíng / háng), `得`, `好`, `着`, v.v.):
  - Trình bày dạng thẻ kính hiện đại:
    - **Âm 1:** Pinyin, ý nghĩa, từ ghép ví dụ.
    - **Âm 2:** Pinyin, ý nghĩa, từ ghép ví dụ.

* **Mẫu HTML chuẩn cấu trúc 4 Phần của Tab 4 (Canonical Structure):**
```html
<!-- PHẦN 1: BẢNG TỪ VỰNG MỚI (生词) -->
<section class="section-card">
  <div class="section-header">
    <div class="section-title"><span>生词: BẢNG TỪ VỰNG MỚI CHÍNH THỨC</span></div>
    <span style="font-size:13px; color:var(--accent);">Tra cứu chuẩn 5 cột</span>
  </div>
  <table class="vocab-table">
    <thead>
      <tr>
        <th style="width:40px;">STT</th>
        <th style="width:120px;">Chữ Hán</th>
        <th style="width:140px;">Phiên âm</th>
        <th style="width:90px;">Từ loại</th>
        <th>Nghĩa tiếng Việt &amp; Ngữ cảnh</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td><strong class="interactive-text">[Chữ Hán]</strong></td>
        <td style="color:#38bdf8; font-weight:600;">[pinyin]</td>
        <td style="color:#94a3b8;">[từ loại]</td>
        <td>[Nghĩa tiếng Việt]</td>
      </tr>
      <!-- Các từ vựng tiếp theo -->
    </tbody>
  </table>
</section>

<!-- PHẦN 2: TRỌNG ĐIỂM NGỮ PHÁP (注释) -->
<section class="section-card">
  <div class="section-header">
    <div class="section-title"><span>注释: TRỌNG ĐIỂM NGỮ PHÁP CHÍNH THỨC</span></div>
    <span style="font-size:13px; color:var(--accent);">Phân tích &amp; Ví dụ SGK</span>
  </div>
  <div class="grammar-point-box">
    <div class="grammar-title"><span>1. [Tên điểm ngữ pháp 1]</span></div>
    <div class="grammar-formula">Công thức: [Cấu trúc]</div>
    <p style="font-size:14px; color:#cbd5e1; margin-bottom:12px;">[Giải thích quy tắc ngữ pháp...]</p>
    <div class="grammar-example-item">
      <div class="interactive-text">[Câu ví dụ chữ Hán]</div>
      <div class="sentence-pinyin-full">[Pinyin câu ví dụ]</div>
      <div style="font-size:13px; color:#94a3b8;">[Dịch nghĩa câu ví dụ]</div>
    </div>
  </div>
</section>

<!-- PHẦN 3: CÁCH GHÉP TỪ CŨ TẠO TỪ MỚI & TỤC NGỮ (旧字新词 & 俗语) -->
<section class="section-card">
  <div class="section-header">
    <div class="section-title"><span>旧字新词 &amp; 俗语: MỞ RỘNG VỐN TỪ &amp; TỤC NGỮ</span></div>
  </div>
  <div class="extended-vocab-grid">
    <div class="extended-vocab-card">
      <div class="interactive-text" style="font-size:16px; font-weight:bold; color:#38bdf8;">[Từ A] + [Từ B] &rarr; [Từ Mới]</div>
      <div style="font-size:13px; color:#cbd5e1; margin-top:4px;">[Giải thích ý nghĩa và phân tích cấu tạo từ]</div>
    </div>
  </div>
</section>

<!-- PHẦN 4: CHUYÊN ĐỀ CHỮ ĐA ÂM TỰ (多音字) -->
<section class="section-card">
  <div class="section-header">
    <div class="section-title"><span>多音字: CHUYÊN ĐỀ CHỮ ĐA ÂM TỰ TRONG BÀI</span></div>
  </div>
  <div class="poly-card-grid">
    <div class="poly-card">
      <div class="interactive-text" style="font-size:22px; font-weight:bold; color:#fbbf24;">[Chữ Đa Âm]</div>
      <div style="font-size:13px; margin-top:6px;">&bull; Âm 1: <span style="color:#38bdf8; font-weight:bold;">[py1]</span>: [Nghĩa &amp; ví dụ]</div>
      <div style="font-size:13px; margin-top:4px;">&bull; Âm 2: <span style="color:#f59e0b; font-weight:bold;">[py2]</span>: [Nghĩa &amp; ví dụ]</div>
    </div>
  </div>
</section>

> [!CRITICAL]
> **QUY CHUẨN BẮT BUỘC TOÀN DIỆN CHO TAB 4:**
> 1. **TUYỆT ĐỐI KHÔNG CÓ .global-toolbar:** Thanh công cụ Ẩn/Hiện Pinyin và Dịch nghĩa chỉ thuộc về các Tab luyện thi (Tab 1, 2, 3). Tab 4 không chứa thanh này.
> 2. **CẤM DÙNG CLASS TỰ CHẾ HOẶC BIẾN CSS LẠ:**
>    - CẤM các class tự bịa: `.grammar-box`, `.pos-tag`, `.vocab-bank`, `.ref-table`, `.ref-row`.
>    - CẤM các biến CSS không tồn tại: `var(--bg-main)`, `var(--border-color)`, `var(--text-muted)`.
> 3. **BỘ CLASS CHUẨN ĐỒNG BỘ 100%:**
>    - Phần 1 (生词): Bảng 5 cột dùng `.vocab-table`.
>    - Phần 2 (注释): Dùng `.grammar-card` (hoặc `.grammar-point-box`), `.grammar-title`, `.grammar-formula`, `.example-item` (hoặc `.grammar-example-item`).
>    - Phần 3 (旧字新词 & 俗语): Dùng `.extended-vocab-grid`, `.extended-vocab-card` (hoặc `.card`).
>    - Phần 4 (多音字): Dùng `.poly-card-grid`, `.poly-card`.
> 4. **CẤM NỘI DUNG BÀI KHÓA SGK:** Tab 4 CHỈ CHỨA 4 phần trên, không đưa bài khóa đọc/đối thoại SGK vào Tab 4.
> 5. **ĐỘ PHỦ TỪ ĐIỂN 100%:** Toàn bộ chữ Hán trong Tab 4 (từ mới, ví dụ ngữ pháp, tục ngữ, chữ đa âm) bắt buộc phải được bổ sung vào bộ từ điển `DICT`.

---

## 3. Quy chuẩn Menu 3 Gạch (Sidebar Drawer Navigation)

Nút menu ☰ luôn nằm cố định ở góc trên bên trái header:
```html
<button class="btn-hamburger" id="btnHamburger" onclick="toggleDrawer()" title="Danh sách 20 bài học">
  <span></span><span></span><span></span>
</button>
<div class="drawer-overlay" id="drawerOverlay" onclick="closeDrawer()"></div>
<aside class="sidebar-drawer" id="sidebarDrawer">
  <div class="drawer-header">
    <h3>DANH SÁCH 20 BÀI HỌC HSK 3</h3>
    <button class="btn-close-drawer" onclick="closeDrawer()">✕</button>
  </div>
  <div class="drawer-search-box">
    <input type="text" id="searchLessonInput" placeholder="Tìm kiếm bài học..." oninput="filterDrawerLessons()">
  </div>
  <div class="drawer-content" id="drawerLessonList"></div>
</aside>
```
* **Dữ liệu 20 bài học:** Một mảng JavaScript chứa đầy đủ 20 bài (`LESSONS_LIST = [{ id: 1, zh: "周末你有什么打算", vi: "Cuối tuần bạn có dự định gì?", url: "..." }, ...]`).
* Bài đang học tự động được gán class `.active` với nhãn `Đang học`.
* Bấm vào overlay nền mờ hoặc nhấn phím `Escape` sẽ tự động đóng menu.

---

## 4. Chuẩn JavaScript & Ngăn ngừa lỗi xung đột

> [!CAUTION]
> **CẢNH BÁO QUAN TRỌNG VỀ PHẠM VI BIẾN:**
> 1. Tuyệt đối **KHÔNG khai báo biến `userAnswers` hai lần** bằng từ khóa `const` hoặc `let`.
> 2. Mọi hàm xử lý trắc nghiệm phải dùng chung một bộ điều khiển duy nhất dưới đây.

```javascript
// Biến lưu trạng thái lựa chọn duy nhất trên toàn trang
const userAnswers = {};

// Hàm chọn đáp án đa năng (hỗ trợ cả Tab 1 và Tab 2)
function selectOption(qNum, value, text) {
  const qKey = String(qNum);
  userAnswers[qKey] = value;
  userAnswers[qNum] = value;
  
  // 1. Cập nhật các chip có data-q (Reading tab & unified cards)
  const chipsWithData = document.querySelectorAll(`.option-chip[data-q="${qKey}"], .option-chip[data-q="${qNum}"]`);
  if (chipsWithData.length > 0) {
    chipsWithData.forEach(c => {
      c.classList.toggle('selected', c.getAttribute('data-val') === value);
    });
  }

  // 2. Cập nhật các chip trong Listening tab
  const card = document.getElementById(`card-${qKey}`) || document.getElementById(`card-${qNum}`) || document.getElementById(`q-${qKey}`);
  if (card) {
    card.querySelectorAll('.option-chip').forEach(chip => {
      const lElem = chip.querySelector('.chip-letter');
      const l = lElem ? lElem.textContent.trim() : '';
      const chipVal = chip.getAttribute('data-val');
      const isTrueChoice = (value === '√' || value === 'true' || value === 'TRUE');
      const isFalseChoice = (value === '×' || value === 'false' || value === 'FALSE' || value === 'X');

      if (l === value || chipVal === value ||
          (isTrueChoice && (l.includes('√') || chip.textContent.includes('Đúng') || chipVal === '√')) ||
          (isFalseChoice && (l.includes('×') || l.includes('X') || chip.textContent.includes('Sai') || chipVal === '×'))) {
        chip.classList.add('selected');
      } else {
        chip.classList.remove('selected');
      }
    });
  }

  // 3. Cập nhật chỗ trống điền từ (nếu có)
  const blankDisplay = document.getElementById(`blank-display-${qKey}`) || document.getElementById(`blank-display-${qNum}`);
  if (blankDisplay) {
    blankDisplay.textContent = `( ${value} ${text || ''} )`;
    blankDisplay.style.color = '#38bdf8';
  }
}

> [!CRITICAL]
> **QUY CHUẨN BẮT BUỘC VỀ ĐỐI TƯỢNG `QUIZ_DATA` (35 CÂU 1 ĐẾN 35):**
> Toàn bộ 35 câu hỏi trắc nghiệm (Câu 1 đến Câu 35) BẮT BUỘC được cấu hình đầy đủ trong `QUIZ_DATA`:
> ```javascript
> const QUIZ_DATA = {
>   // 1 - 5: Luyện nghe Phần 1 (A-F)
>   "1": { ans: "C", explain: "Giải thích..." },
>   ...
>   // 6 - 10: Luyện nghe Phần 2 (√ hoặc ×)
>   "6": { ans: "√", explain: "Giải thích..." },
>   ...
>   // 11 - 20: Luyện nghe Phần 3 & 4 (A, B, C)
>   "11": { ans: "A", explain: "Giải thích..." },
>   ...
>   // 21 - 25: Bài đọc Phần 1 (A-F)
>   "21": { ans: "E", explain: "Giải thích..." },
>   ...
>   // 26 - 30: Bài đọc Phần 2 (A-F)
>   "26": { ans: "B", explain: "Giải thích..." },
>   ...
>   // 31 - 35: Bài đọc Phần 3 (A, B, C)
>   "31": { ans: "C", explain: "Giải thích..." }
> };
> ```
> Nhờ đó, tất cả nút kiểm tra trong HTML CHỈ CẦN gọi hàm sạch:
> `<button class="btn-check" onclick="checkQuiz(1)">Kiểm tra</button>`

// Kiểm tra đáp án chuẩn mực (tự động tra cứu trong QUIZ_DATA, hỗ trợ phán đoán Đúng/Sai)
function checkQuiz(qNum, correctAns, explanation) {
  const qKey = String(qNum);
  const userChoice = userAnswers[qKey] || userAnswers[qNum];
  const feedback = document.getElementById(`feedback-${qKey}`) || document.getElementById(`feedback-${qNum}`);
  if (!feedback) return;

  // Tra cứu tự động trong QUIZ_DATA
  if ((!correctAns || !explanation) && typeof QUIZ_DATA !== 'undefined' && (QUIZ_DATA[qKey] || QUIZ_DATA[qNum])) {
    const item = QUIZ_DATA[qKey] || QUIZ_DATA[qNum];
    correctAns = correctAns || item.ans;
    explanation = explanation || item.explain;
  }

  if (!userChoice) {
    feedback.className = 'feedback-box wrong';
    feedback.style.display = 'block';
    feedback.innerHTML = '⚠️ Vui lòng chọn một đáp án trước khi bấm kiểm tra!';
    return;
  }

  const u = String(userChoice).trim().toUpperCase();
  const c = String(correctAns || '').trim().toUpperCase();
  const isCorrect = (u === c) ||
                    ((u === 'TRUE' || u === '√' || u === 'ĐÚNG') && (c === 'TRUE' || c === '√' || c === 'ĐÚNG')) ||
                    ((u === 'FALSE' || u === '×' || u === 'X' || u === 'SAI') && (c === 'FALSE' || c === '×' || c === 'X' || c === 'SAI'));

  feedback.style.display = 'block';
  if (isCorrect) {
    feedback.className = 'feedback-box correct';
    feedback.innerHTML = `🎉 <strong>Chính xác!</strong> Đáp án đúng là <strong>${correctAns}</strong>.<br>${explanation || ''}`;
  } else {
    feedback.className = 'feedback-box wrong';
    feedback.innerHTML = `❌ <strong>Chưa chính xác!</strong> Bạn chọn <strong>${userChoice}</strong>. Đáp án đúng là <strong>${correctAns}</strong>.<br>${explanation || ''}`;
  }
}

// Hàm checkAnswer alias trỏ thẳng vào checkQuiz
function checkAnswer(qNum) {
  checkQuiz(qNum);
}

// Làm lại câu hỏi
function resetQuiz(qNum) {
  delete userAnswers[qNum];
  const card = document.getElementById(`card-${qNum}`);
  if (card) {
    card.querySelectorAll('.option-chip').forEach(chip => chip.classList.remove('selected'));
  }
  document.querySelectorAll(`.option-chip[data-q="${qNum}"]`).forEach(c => c.classList.remove('selected'));
  
  const blankDisplay = document.getElementById(`blank-display-${qNum}`);
  if (blankDisplay) {
    blankDisplay.textContent = '( ? )';
    blankDisplay.style.color = '#38bdf8';
  }
  const feedback = document.getElementById(`feedback-${qNum}`);
  if (feedback) feedback.style.display = 'none';
}
const resetAnswer = resetQuiz;

// Đóng mở bản dịch câu (Đa năng)
function toggleSentenceTrans(param) {
  if (typeof param === 'number' || typeof param === 'string') {
    const box = document.getElementById(`transbox-${param}`);
    if (box) {
      const isHidden = box.style.display === 'none' || !box.style.display;
      box.style.display = isHidden ? 'block' : 'none';
    }
  } else if (param && param.parentNode) {
    const box = param.parentNode.querySelector('.sentence-trans-box') || param.nextElementSibling;
    if (box) {
      const isHidden = box.style.display === 'none' || !box.style.display;
      box.style.display = isHidden ? 'block' : 'none';
      param.innerHTML = isHidden ? '✕ Thu gọn dịch' : '👁 Dịch cả câu';
    }
  }
}

// Nhảy mốc thời gian Audio (Chuẩn Stream & Sáng nút active)
function jumpAudio(seconds, btn) {
  const audio = document.getElementById('main-audio');
  if (!audio) return;

  document.querySelectorAll('.jump-btn').forEach(b => b.classList.remove('active'));
  if (btn) {
    btn.classList.add('active');
  } else if (window.event && window.event.currentTarget) {
    window.event.currentTarget.classList.add('active');
  }

  const doSeekAndPlay = () => {
    try {
      audio.currentTime = seconds;
      const playPromise = audio.play();
      if (playPromise !== undefined) playPromise.catch(() => {});
    } catch (e) {
      console.warn("Audio seek error:", e);
    }
  };

  if (audio.readyState >= 1) {
    doSeekAndPlay();
  } else {
    const onLoaded = () => {
      doSeekAndPlay();
      audio.removeEventListener('loadedmetadata', onLoaded);
      audio.removeEventListener('canplay', onLoaded);
    };
    audio.addEventListener('loadedmetadata', onLoaded);
    audio.addEventListener('canplay', onLoaded);
    audio.load();
  }
}
```

---

## 5. Quy chuẩn Từ điển (Zero Missing Characters)

1. **Tổng hợp từ điển (`COMBINED_DICT`):**
   - Lấy cơ sở từ `char_dict_full.json` (hơn 4.000 chữ Hán thông dụng).
   - Nối thêm danh mục từ ghép 2 chữ, 3 chữ, 4 chữ và danh từ riêng xuất hiện trong bài.
   - Bổ sung cấu trúc chữ đa âm tự (`poly: [{ py: "...", vi: "..." }]`).
2. **Quy tắc kiểm tra bắt buộc:**
   - Chạy script kiểm tra quét qua 100% chữ Hán trong file HTML.
   - Nếu còn bất kỳ chữ nào chưa có trong `DICT` $\rightarrow$ Bắt buộc phải bổ sung ngay, tuyệt đối không để xảy ra tình trạng hover vào chữ không hiện nghĩa.

3. **Cấu trúc Thẻ Tooltip Tra Từ Điển (`#dict-tooltip`) - Chuẩn tuyệt đối như Bài 1 & 2:**
   HTML thẻ tooltip bắt buộc phải giữ nguyên cấu trúc flex và các class styling chuẩn mực:
   ```html
   <!-- DICTIONARY TOOLTIP -->
   <div id="dict-tooltip">
     <div class="tooltip-word">
       <span id="tt-word">字</span>
       <span class="tooltip-pinyin" id="tt-pinyin">pīnyīn</span>
       <span class="tooltip-hv" id="tt-hv">Âm HV</span>
     </div>
     <div class="tooltip-meaning" id="tt-meaning">Nghĩa tiếng Việt</div>
     <div id="tt-poly-container" style="display:none;">
       <span class="poly-badge">★ Đa âm tự (Kéo / Giữ để xem)</span>
       <div class="poly-detail-box" id="tt-poly-list"></div>
     </div>
   </div>
   ```
   > [!CRITICAL]
   > **CẤM TUYỆT ĐỐI:**
   > - CẤM thay thế bằng các thẻ `<div>` rời rạc không có class (`<div class="tt-word">`, `<div class="tt-pinyin">`...) làm vỡ cấu trúc hiển thị và mất typography của tooltip.
   > - Phải hỗ trợ cả di chuột (`mouseover`), chạm (`touchstart`), và click chuột (`click`) trên máy tính lẫn điện thoại/iPad.

---

## 6. Quy chuẩn Tổ chức Thư mục & Master Template Engine

### A. Cấu trúc thư mục chuẩn mực (Mỗi bài 1 thư mục con riêng biệt)
```
HSK3/
├── Bai_01/                          <-- Thư mục độc lập của Bài 1
│   ├── index.html                   (Ứng dụng web hoàn chỉnh của Bài 1)
│   ├── audio.mp3                    (File âm thanh bài nghe)
│   └── pic_A.png ... pic_F.png      (6 ảnh phần nghe 1-5)
│
├── Bai_02/                          <-- Thư mục độc lập của Bài 2
│   ├── index.html                   (Ứng dụng web hoàn chỉnh của Bài 2)
│   ├── audio.mp3
│   └── pic_A.png ... pic_F.png
│
├── Bai_03/ ... Bai_20/              <-- Các bài học tiếp theo
│
├── core/                            <-- KHUÔN MẪU & CÔNG CỤ TỰ ĐỘNG
│   ├── template_master.html         (Khuôn mẫu HTML bất biến từ Bài 1)
│   └── validate_lesson.py           (Công cụ quét và kiểm thử form chuẩn)
│
├── audio/                           (Kho lưu trữ audio gốc 01.mp3 - 20.mp3)
├── FILE TÀI LIỆU/                   (Sách giáo khoa & Sách bài tập PDF chuẩn)
├── chay_web_server.bat              (File chạy server cục bộ)
└── server.py                        (Server range-enabled phát audio)
```

### B. Quy trình triển khai bài học mới bất biến (Từ Bài 3 đến Bài 20)
- [ ] **1. Chuẩn bị Tài nguyên trong `Bai_XX/`:**
  - Tạo thư mục `Bai_XX/` (ví dụ: `Bai_03`).
  - Sao chép file nghe tương ứng từ `audio/XX.mp3` $\rightarrow$ `Bai_XX/audio.mp3`.
  - Mở `FILE TÀI LIỆU/HSK 3 Sách bài tập.pdf`, crop 6 hình ảnh tranh nghe Bài XX $\rightarrow$ `Bai_XX/pic_A.png` đến `pic_F.png`.
  - Đo chính xác 5 mốc thời gian Audio (Mở đầu, Phần 1, Phần 2, Phần 3, Phần 4).
- [ ] **2. Soạn Thảo & Bóc Tách Dữ Liệu:**
  - Tab 1: Soạn 20 câu nghe theo format mẫu.
  - Tab 2: Soạn 15 câu đọc (LƯU Ý ĐẶC BIỆT: Câu 31-35 bắt buộc phải có đầy đủ Chữ Hán, Phiên âm Pinyin trong ngoặc đơn và Dịch nghĩa từng lựa chọn A, B, C theo đúng Canonical Template).
  - Tab 3: Soạn 10 câu viết (5 câu sắp xếp, 5 câu điền chữ).
  - Tab 4: Lấy trực tiếp từ `FILE TÀI LIỆU/HSK 3 Sách giáo khoa.pdf` (gồm 4 phần: 1. Từ mới & Danh từ riêng, 2. Trọng điểm ngữ pháp, 3. Ghép từ cũ tạo từ mới & Tục ngữ, 4. Chữ đa âm tự; KHÔNG đưa nội dung Bài khóa).
- [ ] **3. Rót Dữ Liệu vào `core/template_master.html`:**
  - Rót dữ liệu vào các placeholder slots của `core/template_master.html`.
  - Bổ sung 100% chữ Hán vào `DICT`.
  - Xuất ra `Bai_XX/index.html`.
- [ ] **4. Thẩm định tự động bắt buộc (Linter):**
  - Chạy lệnh kiểm thử: `python core/validate_lesson.py Bai_XX/index.html`.
  - Kiểm tra kết quả: Phải đạt `100% COMPLIANT`, 0 lỗi, không sót Pinyin ở câu 31-35.
- [ ] **5. Bàn Giao Web Test:**
  - Cung cấp link `http://127.0.0.1:8000/Bai_XX/index.html` cho người dùng nghiệm thu.
