# -*- coding: utf-8 -*-
"""
Universal Lesson Page Builder Engine
Builds 100% compliant interactive web lessons from extracted_bai_XX.py
using core/template_master.html and validates against core/validate_lesson.py
"""

import sys, os, json, re, shutil
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def parse_abc_options(opts):
    if isinstance(opts, dict):
        a_zh = opts.get('A', {}).get('zh', '') if isinstance(opts.get('A'), dict) else str(opts.get('A', ''))
        b_zh = opts.get('B', {}).get('zh', '') if isinstance(opts.get('B'), dict) else str(opts.get('B', ''))
        c_zh = opts.get('C', {}).get('zh', '') if isinstance(opts.get('C'), dict) else str(opts.get('C', ''))
        a_py = opts.get('A', {}).get('py', '') if isinstance(opts.get('A'), dict) else ''
        b_py = opts.get('B', {}).get('py', '') if isinstance(opts.get('B'), dict) else ''
        c_py = opts.get('C', {}).get('py', '') if isinstance(opts.get('C'), dict) else ''
        a_vi = opts.get('A', {}).get('vi', '') if isinstance(opts.get('A'), dict) else ''
        b_vi = opts.get('B', {}).get('vi', '') if isinstance(opts.get('B'), dict) else ''
        c_vi = opts.get('C', {}).get('vi', '') if isinstance(opts.get('C'), dict) else ''
    elif isinstance(opts, list):
        a_zh = opts[0].get('zh', '') if len(opts) > 0 and isinstance(opts[0], dict) else (str(opts[0]) if len(opts) > 0 else '')
        b_zh = opts[1].get('zh', '') if len(opts) > 1 and isinstance(opts[1], dict) else (str(opts[1]) if len(opts) > 1 else '')
        c_zh = opts[2].get('zh', '') if len(opts) > 2 and isinstance(opts[2], dict) else (str(opts[2]) if len(opts) > 2 else '')
        a_py = opts[0].get('py', '') if len(opts) > 0 and isinstance(opts[0], dict) else ''
        b_py = opts[1].get('py', '') if len(opts) > 1 and isinstance(opts[1], dict) else ''
        c_py = opts[2].get('py', '') if len(opts) > 2 and isinstance(opts[2], dict) else ''
        a_vi = opts[0].get('vi', '') if len(opts) > 0 and isinstance(opts[0], dict) else ''
        b_vi = opts[1].get('vi', '') if len(opts) > 1 and isinstance(opts[1], dict) else ''
        c_vi = opts[2].get('vi', '') if len(opts) > 2 and isinstance(opts[2], dict) else ''
    else:
        a_zh = b_zh = c_zh = a_py = b_py = c_py = a_vi = b_vi = c_vi = ''
    return {
        'A': {'zh': a_zh, 'py': a_py, 'vi': a_vi},
        'B': {'zh': b_zh, 'py': b_py, 'vi': b_vi},
        'C': {'zh': c_zh, 'py': c_py, 'vi': c_vi}
    }

def build_lesson(lesson_num):
    lesson_str = f"{lesson_num:02d}"
    print(f"\n==========================================")
    print(f"BUILDING LESSON {lesson_num} (Bai_{lesson_str})")
    print(f"==========================================")

    # 1. Import lesson data
    mod_name = f"data.extracted_bai_{lesson_str}"
    mod = __import__(mod_name, fromlist=['LESSON_DATA'])
    data = mod.LESSON_DATA

    info = data['lesson_info']
    audio_jumps = data['audio_jump']
    t1 = data['tab1_listening']
    t2 = data['tab2_reading']
    t3 = data['tab3_writing']
    t4 = data['tab4_textbook']
    quiz_data = data['quiz_data']

    # 2. Read Master Template
    with open('core/template_master.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # 3. Audio Jump Buttons
    jump_btn_lines = []
    for aj in audio_jumps:
        jump_btn_lines.append(f'          <button class="jump-btn" onclick="jumpAudio({aj["time"]})">{aj["label"]}</button>')
    jump_buttons_html = "\n".join(jump_btn_lines)

    # 4. TAB 1: LISTENING (1 - 20)
    t1_blocks = []
    t1_blocks.append('''      <div class="global-toolbar">
        <button class="tool-btn active" id="btnTogglePinyin" onclick="toggleGlobalPinyin()">Ẩn / Hiện Pinyin</button>
        <button class="tool-btn active" id="btnToggleTrans" onclick="toggleGlobalTrans()">Ẩn / Hiện Dịch Nghĩa</button>
      </div>''')

    # Part 1 (Q1-5)
    p1_pics = t1['part1_pictures']
    p1_grid = ['        <div class="pics-grid">']
    for p in p1_pics:
        p1_grid.append(f'          <div class="pic-item"><img src="{p["file"]}" alt="Tranh {p["id"]}"><div class="pic-label">{p["label"]}</div></div>')
    p1_grid.append('        </div>')

    t1_p1_html = [
        '      <!-- PHẦN 1: CÂU 1 - 5 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第一部分: 第 1 - 5 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">5 câu đối thoại &amp; tranh minh họa</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 听对话，选择与对话内容一致的图片 (Nghe đối thoại, chọn tranh tương ứng A - F):</p>',
        "\n".join(p1_grid),
        '''        <!-- Ví dụ mẫu -->
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
        </div>'''
    ]

    for q in t1['questions_1_to_5']:
        qnum = q['num']
        dlg_lines = []
        full_py_list = []
        full_vi_list = []
        for line in q['dialogue']:
            speaker_cls = "female" if line.get("role") == "female" else "male"
            speaker_name = line.get("speaker", "男" if speaker_cls == "male" else "女")
            dlg_lines.append(f'''          <div class="speaker-line">
            <span class="speaker {speaker_cls}">{speaker_name}:</span>
            <span class="interactive-text">{line["zh"]}</span>
            <span class="pinyin-line">{line["py"]}</span>
            <span class="trans-line">{line["vi"]}</span>
          </div>''')
            full_py_list.append(line["py"])
            full_vi_list.append(f'{speaker_name}: "{line["vi"]}"')

        full_py = " ".join(full_py_list)
        full_vi = " | ".join(full_vi_list)

        t1_p1_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="card-{qnum}">
          <span class="card-num">Câu {qnum}</span>
{chr(10).join(dlg_lines)}
          <div class="options-grid">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A')"><span class="chip-letter">A</span> Hình A</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B')"><span class="chip-letter">B</span> Hình B</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C')"><span class="chip-letter">C</span> Hình C</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'D')"><span class="chip-letter">D</span> Hình D</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'E')"><span class="chip-letter">E</span> Hình E</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'F')"><span class="chip-letter">F</span> Hình F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz({qnum})">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz({qnum})">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans({qnum})">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-{qnum}">
            <div class="sentence-pinyin-full">{full_py}</div>
            <strong>Dịch nghĩa:</strong> {full_vi}<br>
            <strong>Giải thích:</strong> {q["explain"]}
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t1_p1_html.append('      </section>')
    t1_blocks.append("\n".join(t1_p1_html))

    # Part 2 (Q6-10)
    t1_p2_html = [
        '      <!-- PHẦN 2: CÂU 6 - 10 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第二部分: 第 6 - 10 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Phán đoán Đúng (√) hoặc Sai (×)</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 听短文或对话，判断对错 (Nghe câu nói/đoạn văn, phán đoán câu nhận định ★ là Đúng [ √ ] hay Sai [ × ]):</p>',
        '''        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="interactive-text">为了让自己更健康，他每天都花一个小时去锻炼身体。</span>
            <span class="pinyin-line">Wèile ràng zìjǐ gèng jiànkāng, tā měitiān dōu huā yí ge xiǎoshí qù duànliàn shēntǐ.</span>
            <span class="trans-line">Để bản thân khỏe mạnh hơn, mỗi ngày anh ấy đều dành ra một tiếng để rèn luyện thân thể.</span>
          </div>
          <div class="listening-statement">
            <span class="interactive-text">&bull; ★ 他希望自己很健康。</span>
            <span class="pinyin-line">Tā xīwàng zìjǐ hěn jiànkāng.</span>
            <span class="trans-line">Anh ấy hy vọng bản thân thật khỏe mạnh.</span>
          </div>
          <div class="options-grid grid-true-false" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip selected"><span class="chip-letter">√</span> Đúng (√)</div>
          </div>
        </div>'''
    ]

    for q in t1['questions_6_to_10']:
        qnum = q['num']
        psg = q['passage']
        stm = q['statement']
        t1_p2_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="card-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="speaker-line">
            <span class="interactive-text">{psg["zh"]}</span>
            <span class="pinyin-line">{psg["py"]}</span>
            <span class="trans-line">{psg["vi"]}</span>
          </div>
          <div class="listening-statement">
            <span class="interactive-text">&bull; ★ {stm["zh"]}</span>
            <span class="pinyin-line">{stm["py"]}</span>
            <span class="trans-line">{stm["vi"]}</span>
          </div>
          <div class="options-grid grid-true-false">
            <div class="option-chip" onclick="selectOption('{qnum}', '√')"><span class="chip-letter">√</span> Đúng (√)</div>
            <div class="option-chip" onclick="selectOption('{qnum}', '×')"><span class="chip-letter">×</span> Sai (×)</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz({qnum})">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz({qnum})">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans({qnum})">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-{qnum}">
            <div class="sentence-pinyin-full">{psg["py"]} ★ {stm["py"]}</div>
            <strong>Dịch đối chiếu:</strong> Lời thoại: "{psg["vi"]}" vs Nhận định: "{stm["vi"]}"<br>
            <strong>Giải thích:</strong> {q["explain"]}
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t1_p2_html.append('      </section>')
    t1_blocks.append("\n".join(t1_p2_html))

    # Part 3 (Q11-15)
    t1_p3_html = [
        '      <!-- PHẦN 3: CÂU 11 - 15 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第三部分: 第 11 - 15 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Hội thoại ngắn (2 lượt lời)</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 听短对话，选择正确答案 (Nghe đối thoại ngắn 2 lượt lời, chọn đáp án đúng A, B hoặc C):</p>',
        '''        <!-- Ví dụ mẫu -->
        <div class="card" style="border-left: 3px solid #64748b;">
          <span class="card-num" style="background:#64748b;">Ví dụ</span>
          <div class="speaker-line">
            <span class="speaker male">男:</span>
            <span class="interactive-text">小王，帮我开一下门，好吗？谢谢！</span>
            <span class="pinyin-line">Xiǎo Wáng, bāng wǒ kāi yíxià mén, hǎo ma? Xièxie!</span>
            <span class="trans-line">Tiểu Vương, mở giúp tôi cái cửa được không? Cảm ơn nhé!</span>
          </div>
          <div class="speaker-line">
            <span class="speaker female">女:</span>
            <span class="interactive-text">没问题，您去超市了？买这么多东西。</span>
            <span class="pinyin-line">Méi wèntí, nín qù chāoshì le? Mǎi zhème duō dōngxi.</span>
            <span class="trans-line">Không có gì ạ, anh vừa đi siêu thị về à? Mua nhiều đồ thế.</span>
          </div>
          <div class="listening-question">
            <span class="interactive-text">问: 刚才男的做社么了？</span>
            <span class="pinyin-line">Wèn: Gāngcái nán de zuò shénme le?</span>
            <span class="trans-line">Hỏi: Vừa nãy người nam đã làm gì?</span>
          </div>
          <div class="options-grid grid-abc" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip"><span class="chip-letter">A</span> 买东西</div>
            <div class="option-chip selected"><span class="chip-letter">B</span> 去超市 √</div>
            <div class="option-chip"><span class="chip-letter">C</span> 开门</div>
          </div>
        </div>'''
    ]

    for q in t1['questions_11_to_15']:
        qnum = q['num']
        dlg_lines = []
        full_py_list = []
        for line in q['dialogue']:
            speaker_cls = "female" if line.get("role") == "female" else "male"
            speaker_name = line.get("speaker", "男" if speaker_cls == "male" else "女")
            dlg_lines.append(f'''          <div class="speaker-line">
            <span class="speaker {speaker_cls}">{speaker_name}:</span>
            <span class="interactive-text">{line["zh"]}</span>
            <span class="pinyin-line">{line["py"]}</span>
            <span class="trans-line">{line["vi"]}</span>
          </div>''')
            full_py_list.append(line["py"])

        ques = q['question']
        opts = q['options']
        ques_zh = ques["zh"] if (ques["zh"].startswith("问:") or ques["zh"].startswith("问：")) else f'问: {ques["zh"]}'
        ques_py = ques["py"] if ques["py"].lower().startswith("wèn") else f'Wèn: {ques["py"]}'
        ques_vi = ques["vi"] if ques["vi"].lower().startswith("hỏi") else f'Hỏi: {ques["vi"]}'
        full_py_list.append(ques_py)

        abc_opts = parse_abc_options(opts)

        t1_p3_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="card-{qnum}">
          <span class="card-num">Câu {qnum}</span>
{chr(10).join(dlg_lines)}
          <div class="listening-question">
            <span class="interactive-text">{ques_zh}</span>
            <span class="pinyin-line">{ques_py}</span>
            <span class="trans-line">{ques_vi}</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A')"><span class="chip-letter">A</span> <span class="interactive-text">{abc_opts['A']['zh']}</span></div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B')"><span class="chip-letter">B</span> <span class="interactive-text">{abc_opts['B']['zh']}</span></div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C')"><span class="chip-letter">C</span> <span class="interactive-text">{abc_opts['C']['zh']}</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz({qnum})">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz({qnum})">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans({qnum})">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-{qnum}">
            <div class="sentence-pinyin-full">{" ".join(full_py_list)}</div>
            <strong>Dịch câu hỏi &amp; các lựa chọn:</strong><br>
            &bull; Câu hỏi: {ques_vi}<br>
            &bull; A. {abc_opts['A']['zh']}{" (" + abc_opts['A']['py'] + ")" if abc_opts['A']['py'] else ""}{": " + abc_opts['A']['vi'] if abc_opts['A']['vi'] else ""}<br>
            &bull; B. {abc_opts['B']['zh']}{" (" + abc_opts['B']['py'] + ")" if abc_opts['B']['py'] else ""}{": " + abc_opts['B']['vi'] if abc_opts['B']['vi'] else ""}<br>
            &bull; C. {abc_opts['C']['zh']}{" (" + abc_opts['C']['py'] + ")" if abc_opts['C']['py'] else ""}{": " + abc_opts['C']['vi'] if abc_opts['C']['vi'] else ""}<br>
            <strong>Giải thích:</strong> {q["explain"]}
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t1_p3_html.append('      </section>')
    t1_blocks.append("\n".join(t1_p3_html))

    # Part 4 (Q16-20)
    t1_p4_html = [
        '      <!-- PHẦN 4: CÂU 16 - 20 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第四部分: 第 16 - 20 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Đối thoại dài (4 lượt lời)</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 听长对话，选择正确答案 (Nghe đối thoại dài 4 lượt lời, chọn đáp án đúng A, B hoặc C):</p>',
        '''        <!-- Ví dụ mẫu -->
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
          <div class="listening-question">
            <span class="interactive-text">问: 男的在做什么？</span>
            <span class="pinyin-line">Nán de zài zuò shénme?</span>
            <span class="trans-line">Hỏi: Người nam đang làm gì?</span>
          </div>
          <div class="options-grid grid-abc" style="pointer-events:none; margin-top:10px;">
            <div class="option-chip"><span class="chip-letter">A</span> 洗澡</div>
            <div class="option-chip"><span class="chip-letter">B</span> 吃饭</div>
            <div class="option-chip selected"><span class="chip-letter">C</span> 看电视 √</div>
          </div>
        </div>'''
    ]

    for q in t1['questions_16_to_20']:
        qnum = q['num']
        dlg_lines = []
        full_py_list = []
        for line in q['dialogue']:
            speaker_cls = "female" if line.get("role") == "female" else "male"
            speaker_name = line.get("speaker", "男" if speaker_cls == "male" else "女")
            dlg_lines.append(f'''          <div class="speaker-line">
            <span class="speaker {speaker_cls}">{speaker_name}:</span>
            <span class="interactive-text">{line["zh"]}</span>
            <span class="pinyin-line">{line["py"]}</span>
            <span class="trans-line">{line["vi"]}</span>
          </div>''')
            full_py_list.append(line["py"])

        ques = q['question']
        opts = q['options']
        ques_zh = ques["zh"] if (ques["zh"].startswith("问:") or ques["zh"].startswith("问：")) else f'问: {ques["zh"]}'
        ques_py = ques["py"] if ques["py"].lower().startswith("wèn") else f'Wèn: {ques["py"]}'
        ques_vi = ques["vi"] if ques["vi"].lower().startswith("hỏi") else f'Hỏi: {ques["vi"]}'
        full_py_list.append(ques_py)

        abc_opts = parse_abc_options(opts)

        t1_p4_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="card-{qnum}">
          <span class="card-num">Câu {qnum}</span>
{chr(10).join(dlg_lines)}
          <div class="listening-question">
            <span class="interactive-text">{ques_zh}</span>
            <span class="pinyin-line">{ques_py}</span>
            <span class="trans-line">{ques_vi}</span>
          </div>
          <div class="options-grid grid-abc">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A')"><span class="chip-letter">A</span> <span class="interactive-text">{abc_opts['A']['zh']}</span></div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B')"><span class="chip-letter">B</span> <span class="interactive-text">{abc_opts['B']['zh']}</span></div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C')"><span class="chip-letter">C</span> <span class="interactive-text">{abc_opts['C']['zh']}</span></div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkQuiz({qnum})">Kiểm tra</button>
            <button class="btn-reset" onclick="resetQuiz({qnum})">Làm lại</button>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans({qnum})">👁 Dịch câu &amp; Giải thích</button>
          </div>
          <div class="sentence-trans-box" id="transbox-{qnum}">
            <div class="sentence-pinyin-full">{" ".join(full_py_list)}</div>
            <strong>Dịch câu hỏi &amp; các lựa chọn:</strong><br>
            &bull; Câu hỏi: {ques_vi}<br>
            &bull; A. {abc_opts['A']['zh']}{" (" + abc_opts['A']['py'] + ")" if abc_opts['A']['py'] else ""}{": " + abc_opts['A']['vi'] if abc_opts['A']['vi'] else ""}<br>
            &bull; B. {abc_opts['B']['zh']}{" (" + abc_opts['B']['py'] + ")" if abc_opts['B']['py'] else ""}{": " + abc_opts['B']['vi'] if abc_opts['B']['vi'] else ""}<br>
            &bull; C. {abc_opts['C']['zh']}{" (" + abc_opts['C']['py'] + ")" if abc_opts['C']['py'] else ""}{": " + abc_opts['C']['vi'] if abc_opts['C']['vi'] else ""}<br>
            <strong>Giải thích:</strong> {q["explain"]}
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t1_p4_html.append('      </section>')
    t1_blocks.append("\n".join(t1_p4_html))

    tab1_content = "\n\n".join(t1_blocks)

    # ==============================================================================
    # 5. TAB 2: READING (21 - 35)
    # ==============================================================================
    t2_blocks = []

    # Part 1 (Q21-25)
    part1_data = t2.get('part1') or t2.get('part1_21_25')
    r_opts_raw = part1_data.get('options', [])
    if isinstance(r_opts_raw, dict):
        r_opts = [{'id': k, 'zh': v['zh'], 'py': v.get('py', ''), 'vi': v.get('vi', '')} for k, v in r_opts_raw.items()]
    else:
        r_opts = r_opts_raw

    ref_items = []
    for ro in r_opts:
        ref_items.append(f'''        <div class="reading-ref-item">
          <span class="chip-letter">{ro["id"]}</span>
          <div>
            <span class="interactive-text">{ro["zh"]}</span>
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)" style="margin-left:8px; padding:2px 8px; font-size:11px;">👁 Dịch</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">{ro["py"]}</div>
              <div>{ro["vi"]}</div>
            </div>
          </div>
        </div>''')

    t2_p1_html = [
        '      <!-- PHẦN 1: CÂU 21 - 25 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第一部分: 第 21 - 25 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Ghép câu đối ứng phù hợp (A - F)</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 选择合适的句子填空 (Chọn câu đối ứng phù hợp nhất A - F cho từng câu bên dưới):</p>',
        '        <div class="reading-ref-box">',
        '          <div class="reading-ref-title">DANH SÁCH CÁC CÂU LỰA CHỌN (A - F):</div>',
        "\n".join(ref_items),
        '        </div>'
    ]

    for q in part1_data.get('questions', []):
        qnum = q['num']
        q_zh = q.get('zh') or q.get('sentence', '')
        q_py = q.get('py') or q.get('pinyin', '')
        q_vi = q.get('vi') or q.get('trans', '')
        t2_p1_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="q-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="interactive-text">{q_zh}</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">{q_py}</div>
              <div>{q_vi}</div>
            </div>
          </div>
          <div class="options-grid grid-letters">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A')" data-q="{qnum}" data-val="A"><span class="chip-letter">A</span> A</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B')" data-q="{qnum}" data-val="B"><span class="chip-letter">B</span> B</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C')" data-q="{qnum}" data-val="C"><span class="chip-letter">C</span> C</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'D')" data-q="{qnum}" data-val="D"><span class="chip-letter">D</span> D</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'E')" data-q="{qnum}" data-val="E"><span class="chip-letter">E</span> E</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'F')" data-q="{qnum}" data-val="F"><span class="chip-letter">F</span> F</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('{qnum}')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('{qnum}')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t2_p1_html.append('      </section>')
    t2_blocks.append("\n".join(t2_p1_html))

    # Part 2 (Q26-30)
    part2_data = t2.get('part2') or t2.get('part2_26_30', {})
    vb_raw = part2_data.get('words') or part2_data.get('vocab_bank') or part2_data.get('options', {})
    if isinstance(vb_raw, dict):
        vb_list = [{'id': k, 'zh': v['zh'], 'py': v.get('py', ''), 'vi': v.get('vi', '')} for k, v in vb_raw.items()]
    else:
        vb_list = vb_raw

    vb_cards = []
    vb_map = {}
    for vb in vb_list:
        vb_map[vb['id']] = vb['zh']
        vb_cards.append(f'''          <div class="reading-vocab-card">
            <span class="chip-letter">{vb["id"]}</span> <strong class="interactive-text">{vb["zh"]}</strong> <span style="font-size:12px; color:#94a3b8;">({vb["py"]}: {vb["vi"]})</span>
          </div>''')

    t2_p2_html = [
        '      <!-- PHẦN 2: CÂU 26 - 30 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第二部分: 第 26 - 30 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Điền từ vào chỗ trống (A - F)</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 选词填空 (Chọn từ vựng phù hợp trong ngân hàng từ A - F điền vào chỗ trống):</p>',
        '        <div class="reading-vocab-box">',
        '          <div class="reading-vocab-title">NGÂN HÀNG TỪ VỰNG:</div>',
        '          <div class="reading-vocab-grid">',
        "\n".join(vb_cards),
        '          </div>',
        '        </div>'
    ]

    for q in part2_data.get('questions', []):
        qnum = q['num']
        blank_span = f'<span id="blank-display-{qnum}" style="color:#38bdf8; font-weight:bold; text-decoration: underline; padding: 0 8px;">( ? )</span>'
        st = q.get('sentence') or q.get('zh', '')
        if st:
            for placeholder in ['（……）', '(……)', '（...）', '（  ）', '（ ）', '( ... )', '（）', '()']:
                if placeholder in st:
                    st = st.replace(placeholder, blank_span)
                    break
            else:
                if '……' in st:
                    st = st.replace('……', blank_span)
                elif '...' in st:
                    st = st.replace('...', blank_span)
                elif '（' in st and '）' in st:
                    st = re.sub(r'（[^）]*）', blank_span, st)
                elif '(' in st and ')' in st:
                    st = re.sub(r'\([^\)]*\)', blank_span, st)
            sentence_display = st
        else:
            pre = q.get('prefix', '')
            suf = q.get('suffix', '')
            sentence_display = f"{pre} {blank_span} {suf}"

        t2_p2_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="q-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="interactive-text">{sentence_display}</div>
          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch cả câu</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">{q["py"]}</div>
              <div>{q["vi"]}</div>
            </div>
          </div>
          <div class="options-grid grid-vocab">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A', '{vb_map.get("A", "")}')" data-q="{qnum}" data-val="A"><span class="chip-letter">A</span> {vb_map.get("A", "")}</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B', '{vb_map.get("B", "")}')" data-q="{qnum}" data-val="B"><span class="chip-letter">B</span> {vb_map.get("B", "")}</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C', '{vb_map.get("C", "")}')" data-q="{qnum}" data-val="C"><span class="chip-letter">C</span> {vb_map.get("C", "")}</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'D', '{vb_map.get("D", "")}')" data-q="{qnum}" data-val="D"><span class="chip-letter">D</span> {vb_map.get("D", "")}</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'E', '{vb_map.get("E", "")}')" data-q="{qnum}" data-val="E"><span class="chip-letter">E</span> {vb_map.get("E", "")}</div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'F', '{vb_map.get("F", "")}')" data-q="{qnum}" data-val="F"><span class="chip-letter">F</span> {vb_map.get("F", "")}</div>
          </div>
          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('{qnum}')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('{qnum}')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t2_p2_html.append('      </section>')
    t2_blocks.append("\n".join(t2_p2_html))

    # Part 3 (Q31-35)
    part3_data = t2.get('part3') or t2.get('part3_31_35')
    t2_p3_html = [
        '      <!-- PHẦN 3: CÂU 31 - 35 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第三部分: 第 31 - 35 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Đọc hiểu đoạn văn ngắn &amp; chọn A, B, C</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 阅读短文，选择正确答案 (Đọc đoạn văn ngắn, chọn câu trả lời đúng A, B hoặc C):</p>'
    ]

    for q in part3_data:
        qnum = q['num']
        psg = q['passage']
        ques = q['question']
        opts = q['options']

        if isinstance(opts, dict):
            opt_a = opts.get('A', {})
            opt_b = opts.get('B', {})
            opt_c = opts.get('C', {})
        else:
            opt_a = next((o for o in opts if o.get('id') == 'A'), {})
            opt_b = next((o for o in opts if o.get('id') == 'B'), {})
            opt_c = next((o for o in opts if o.get('id') == 'C'), {})

        t2_p3_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="q-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="reading-passage-box interactive-text">
            {psg["zh"]}
          </div>

          <div class="reading-question-title interactive-text">
            &bull; {ques["zh"]}:
          </div>

          <div class="options-grid" style="margin-top: 14px;">
            <div class="option-chip" onclick="selectOption('{qnum}', 'A')" data-q="{qnum}" data-val="A">
              <span class="chip-letter">A</span>
              <div><span class="interactive-text" style="font-size: 17px;">{opt_a.get("zh", "")}</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'B')" data-q="{qnum}" data-val="B">
              <span class="chip-letter">B</span>
              <div><span class="interactive-text" style="font-size: 17px;">{opt_b.get("zh", "")}</span></div>
            </div>
            <div class="option-chip" onclick="selectOption('{qnum}', 'C')" data-q="{qnum}" data-val="C">
              <span class="chip-letter">C</span>
              <div><span class="interactive-text" style="font-size: 17px;">{opt_c.get("zh", "")}</span></div>
            </div>
          </div>

          <div class="sentence-footer">
            <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Dịch đoạn văn &amp; các lựa chọn</button>
            <div class="sentence-trans-box">
              <div class="sentence-pinyin-full">{psg["py"]}</div>
              <div style="margin-bottom: 8px;"><strong>Dịch đoạn văn:</strong> {psg["vi"]}</div>
              <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 6px; font-size: 13px;">
                <strong>Dịch các lựa chọn:</strong><br>
                &bull; <strong>A. {opt_a.get("zh", "")}</strong> ({opt_a.get("py", "")}): {opt_a.get("vi", "")}<br>
                &bull; <strong>B. {opt_b.get("zh", "")}</strong> ({opt_b.get("py", "")}): {opt_b.get("vi", "")}<br>
                &bull; <strong>C. {opt_c.get("zh", "")}</strong> ({opt_c.get("py", "")}): {opt_c.get("vi", "")}<br>
              </div>
            </div>
          </div>

          <div class="quiz-actions">
            <button class="btn-check" onclick="checkAnswer('{qnum}')">Kiểm tra đáp án</button>
            <button class="btn-reset" onclick="resetAnswer('{qnum}')">Làm lại</button>
          </div>
          <div class="feedback-box" id="feedback-{qnum}"></div>
        </div>''')

    t2_p3_html.append('      </section>')
    t2_blocks.append("\n".join(t2_p3_html))

    tab2_content = "\n\n".join(t2_blocks)

    # ==============================================================================
    # 6. TAB 3: WRITING (36 - 45)
    # ==============================================================================
    t3_blocks = []

    # Part 1 (Q36-40)
    part1_w = t3.get('part1') or t3.get('part1_36_40', [])
    t3_p1_html = [
        '      <!-- PHẦN 1: CÂU 36 - 40 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第一部分: 第 36 - 40 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Sắp xếp từ ngữ thành câu hoàn chỉnh</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 连词成句 (Sắp xếp các cụm từ ngữ rời rạc thành câu hoàn chỉnh đúng ngữ pháp):</p>'
    ]

    for q in part1_w:
        qnum = q['num']
        chunks_display = " / ".join(q["chunks"]) if isinstance(q["chunks"], list) else str(q["chunks"])
        t3_p1_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="q-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="writing-scramble-text interactive-text">{chunks_display}</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem đáp án câu đúng &amp; dịch</button>
          <div class="sentence-trans-box">
            <div class="writing-correct-answer interactive-text">{q["ans"]}</div>
            <div class="sentence-pinyin-full">{q["py"]}</div>
            <div>{q["vi"]}</div>
            <div style="font-size:12px; color:#94a3b8; margin-top:4px;">&bull; Ghi chú: {q["grammar"]}</div>
          </div>
        </div>''')

    t3_p1_html.append('      </section>')
    t3_blocks.append("\n".join(t3_p1_html))

    # Part 2 (Q41-45)
    part2_w = t3.get('part2') or t3.get('part2_41_45', [])
    t3_p2_html = [
        '      <!-- PHẦN 2: CÂU 41 - 45 -->',
        '      <section class="section-card">',
        '        <div class="section-header">',
        '          <div class="section-title"><span>第二部分: 第 41 - 45 题</span></div>',
        '          <span style="font-size:13px; color:var(--accent);">Nhìn Pinyin điền chữ Hán</span>',
        '        </div>',
        '        <p class="section-desc">Yêu cầu: 看拼音写汉字 (Nhìn phiên âm Pinyin điền chữ Hán chính xác vào chỗ trống):</p>'
    ]

    for q in part2_w:
        qnum = q['num']
        ans = q.get('ans', '')
        pinyin = q.get('pinyin', '')
        sentence = q.get('sentence', '')
        full_st = q.get('full_sentence', sentence.replace(f'（{pinyin}）', ans).replace(f'（ {ans} ）', ans).replace(f'（{ans}）', ans))
        t3_p2_html.append(f'''        <!-- Câu {qnum} -->
        <div class="card" id="q-{qnum}">
          <span class="card-num">Câu {qnum}</span>
          <div class="writing-fill-sentence interactive-text">
            {sentence}
          </div>
          <div style="font-size:13px; color:var(--text-sub); margin-bottom:8px;">{q["vi"]}</div>
          <button class="btn-trans-toggle" onclick="toggleSentenceTrans(this)">👁 Xem chữ Hán &amp; dịch</button>
          <div class="sentence-trans-box">
            <div>Chữ Hán cần điền: <span class="writing-target-hanzi interactive-text">{ans}</span> <span class="sentence-pinyin-full">({pinyin})</span> - Hán Việt: {q.get("hanviet", "")}</div>
            <div style="margin-top:4px;">&bull; Từ ghép / Cụm từ: <strong>{q.get("compound", "")}</strong>.</div>
            <div style="margin-top:4px; font-weight:bold; color:#cbd5e1;">{full_st}</div>
          </div>
        </div>''')

    t3_p2_html.append('      </section>')
    t3_blocks.append("\n".join(t3_p2_html))

    tab3_content = "\n\n".join(t3_blocks)

    # ==============================================================================
    # 7. TAB 4: SÁCH GIÁO KHOA (TỪ VỰNG & NGỮ PHÁP)
    # ==============================================================================
    t4_blocks = []

    # Section 1: Vocab table
    vocab_rows = []
    for v in t4['vocab']:
        vocab_rows.append(f'''        <tr>
          <td>{v["id"]}</td>
          <td><strong class="interactive-text">{v["zh"]}</strong></td>
          <td style="color:#38bdf8; font-weight:600;">{v["py"]}</td>
          <td style="color:#94a3b8;">{v["pos"]}</td>
          <td>{v["vi"]}</td>
        </tr>''')

    t4_sec1 = f'''      <!-- PHẦN 1: BẢNG TỪ VỰNG MỚI (生词) -->
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
{"".join(vocab_rows)}          </tbody>
        </table>
      </section>'''
    t4_blocks.append(t4_sec1)

    # Section 2: Grammar
    gm_cards = []
    for idx, gm in enumerate(t4['grammar'], 1):
        eg_items = []
        for eg in gm.get('examples', []):
            eg_items.append(f'''        <div class="example-item">
          <div class="interactive-text">{eg["zh"]}</div>
          <div class="sentence-pinyin-full">{eg["py"]}</div>
          <div style="font-size:13px; color:#94a3b8;">{eg["vi"]}</div>
        </div>''')

        gm_cards.append(f'''      <div class="grammar-card">
        <div class="grammar-title"><span>{idx}. {gm["title"]}</span></div>
        <div class="grammar-formula">Công thức: {gm["structure"]}</div>
        <p style="font-size:14px; color:#cbd5e1; margin-bottom:12px;">{gm["explanation"]}</p>
{"".join(eg_items)}      </div>''')

    t4_sec2 = f'''      <!-- PHẦN 2: TRỌNG ĐIỂM NGỮ PHÁP (注释) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>注释: TRỌNG ĐIỂM NGỮ PHÁP CHÍNH THỨC</span></div>
          <span style="font-size:13px; color:var(--accent);">Phân tích &amp; Ví dụ SGK</span>
        </div>
{"".join(gm_cards)}
      </section>'''
    t4_blocks.append(t4_sec2)

    # Section 3: Word expansion & Proverb
    exp = t4.get('expansion_and_idiom', {})
    hk = exp.get('hanzi_knowledge') or t4.get('hanzi_knowledge', {})
    exp_cards = []

    # Hanzi knowledge cards (if any)
    for c in hk.get('characters', []):
        exp_cards.append(f'''        <div class="extended-vocab-card">
          <div class="interactive-text" style="font-size:22px; font-weight:bold; color:#38bdf8;">{c["char"]} ({c["pinyin"]})</div>
          <div style="font-size:13px; color:#cbd5e1; margin-top:4px;">{c["explain"]}</div>
        </div>''')

    # Word expansion cards
    we_list = exp.get('word_expansion') or t4.get('word_expansion', [])
    for we in we_list:
        exp_cards.append(f'''        <div class="extended-vocab-card">
          <div class="interactive-text" style="font-size:17px; font-weight:bold; color:#38bdf8;">{we["word"]} ({we["py"]})</div>
          <div style="font-size:13px; color:#cbd5e1; margin-top:4px;">{we["meaning"]}</div>
        </div>''')

    prv = exp.get('proverb') or t4.get('idiom') or t4.get('proverb', {})
    prv_html = ""
    if prv:
        prv_html = f'''        <div class="card" style="margin-top:16px; border-left:4px solid #f59e0b; background:rgba(245,158,11,0.06);">
          <div style="font-size:14px; font-weight:bold; color:#f59e0b; margin-bottom:6px;">TỤC NGỮ TRUYỀN THỐNG (俗语):</div>
          <div class="interactive-text" style="font-size:20px; font-weight:bold; color:#fff;">{prv.get("zh", "")}</div>
          <div class="sentence-pinyin-full" style="color:#fbbf24;">{prv.get("py", "")}</div>
          <div style="font-size:14px; color:#cbd5e1; margin-top:6px;">{prv.get("vi", "")}</div>
        </div>'''

    t4_sec3 = f'''      <!-- PHẦN 3: CÁCH GHÉP TỪ CŨ TẠO TỪ MỚI & TỤC NGỮ (旧字新词 & 俗语) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>旧字新词 &amp; 俗语: MỞ RỘNG VỐN TỪ &amp; TỤC NGỮ</span></div>
        </div>
        <div class="extended-vocab-grid">
{"".join(exp_cards)}        </div>
{prv_html}
      </section>'''
    t4_blocks.append(t4_sec3)

    # Section 4: Polyphonic characters
    poly_list = t4.get('polyphonic', [])
    poly_cards = []
    multitone_dict = {}
    for p in poly_list:
        char = p['char']
        sounds = p.get('sounds', [])
        multitone_dict[char] = []
        sound_lines = []
        for s in sounds:
            multitone_dict[char].append({
                "py": s.get("py", ""),
                "vi": f'{s.get("meaning", "")} ({s.get("example", "")})'
            })
            sound_lines.append(f'''          <div style="font-size:13px; margin-top:6px;">
            &bull; Âm: <span style="color:#38bdf8; font-weight:bold;">{s.get("py", "")}</span>: {s.get("meaning", "")} (Ví dụ: <span class="interactive-text">{s.get("example", "")}</span>)
          </div>''')

        poly_cards.append(f'''        <div class="poly-card">
          <div class="interactive-text" style="font-size:24px; font-weight:bold; color:#fbbf24;">{char}</div>
{"".join(sound_lines)}
        </div>''')

    t4_sec4 = f'''      <!-- PHẦN 4: CHUYÊN ĐỀ CHỮ ĐA ÂM TỰ (多音字) -->
      <section class="section-card">
        <div class="section-header">
          <div class="section-title"><span>多音字: CHUYÊN ĐỀ CHỮ ĐA ÂM TỰ TRONG BÀI</span></div>
        </div>
        <div class="poly-card-grid">
{"".join(poly_cards)}        </div>
      </section>'''
    t4_blocks.append(t4_sec4)

    tab4_content = "\n\n".join(t4_blocks)

    # ==============================================================================
    # 8. DICTIONARY COMPILATION & ZERO MISSING CHARACTERS
    # ==============================================================================
    master_dict = {}
    # Load base dictionary from previous lessons
    for prev_l in range(1, 8):
        p_prev = f'Bai_{prev_l:02d}/index.html'
        if os.path.exists(p_prev):
            try:
                with open(p_prev, 'r', encoding='utf-8') as f:
                    c_prev = f.read()
                m_d = re.search(r'const DICT = (\{.*?\});', c_prev)
                if m_d:
                    master_dict.update(json.loads(m_d.group(1)))
            except Exception:
                pass

    if os.path.exists('data/dictionary_full.js'):
        with open('data/dictionary_full.js', 'r', encoding='utf-8') as f:
            c_df = f.read()
        m_df = re.search(r'window\.DICT\s*=\s*(\{.*?\});', c_df, re.DOTALL)
        if m_df:
            try:
                master_dict.update(json.loads(m_df.group(1)))
            except Exception as e:
                print('Warning loading dictionary_full.js:', e)

    # Add all new vocabulary from Tab 4
    for v in t4.get('vocab', []):
        w = v['zh']
        master_dict[w] = {
            "py": v["py"],
            "hv": "",
            "vi": f'{v["vi"]} ({v["pos"]})'
        }

    # Add word expansions
    for we in we_list:
        master_dict[we["word"]] = {
            "py": we["py"],
            "hv": "",
            "vi": we["meaning"]
        }

    # Add proverbs
    if prv and prv.get("zh"):
        master_dict[prv["zh"]] = {
            "py": prv["py"],
            "hv": "",
            "vi": prv["vi"]
        }

    # Add polyphonic characters flag
    for char in multitone_dict:
        if char in master_dict:
            master_dict[char]["poly"] = multitone_dict[char]
        else:
            master_dict[char] = {
                "py": multitone_dict[char][0]["py"],
                "hv": "",
                "vi": multitone_dict[char][0]["vi"],
                "poly": multitone_dict[char]
            }

    # Assemble HTML Page
    output = template
    output = output.replace('{{LESSON_NUM}}', str(info['id']))
    output = output.replace('{{LESSON_TITLE}}', info['title_zh'])
    output = output.replace('{{LESSON_SUBTITLE}}', f"{info['title_py']} - {info['title_vi']}")
    output = output.replace('{{AUDIO_SRC}}', 'audio.mp3')
    output = output.replace('{{AUDIO_JUMP_BUTTONS}}', jump_buttons_html)
    output = output.replace('{{TAB1_CONTENT}}', tab1_content)
    output = output.replace('{{TAB2_CONTENT}}', tab2_content)
    output = output.replace('{{TAB3_CONTENT}}', tab3_content)
    output = output.replace('{{TAB4_CONTENT}}', tab4_content)
    output = output.replace('{{MULTITONE_JSON}}', json.dumps(multitone_dict, ensure_ascii=False))
    output = output.replace('{{QUIZ_DATA_JSON}}', json.dumps(quiz_data, ensure_ascii=False))

    # Check missing Chinese characters across all interactive-text
    all_chars = set(re.findall(r'[\u4e00-\u9fa5]', output))
    missing_chars = [c for c in all_chars if c not in master_dict]
    if missing_chars:
        print(f"Adding {len(missing_chars)} missing characters to DICT...")
        try:
            import pypinyin
            for c in missing_chars:
                py_c = pypinyin.pinyin(c, style=pypinyin.Style.TONE)[0][0]
                master_dict[c] = {"py": py_c, "hv": "", "vi": f"Chữ Hán: {c}"}
        except Exception:
            for c in missing_chars:
                master_dict[c] = {"py": "", "hv": "", "vi": f"Chữ Hán: {c}"}

    output = output.replace('{{DICT_JSON}}', json.dumps(master_dict, ensure_ascii=False))

    # 9. Create target directory and write files
    target_dir = f"Bai_{lesson_str}"
    os.makedirs(target_dir, exist_ok=True)

    # Copy pictures
    pics_src_dir = f"scratch/bai_{lesson_str}/pics"
    if os.path.exists(pics_src_dir):
        for pf in os.listdir(pics_src_dir):
            if pf.endswith('.png'):
                shutil.copy2(os.path.join(pics_src_dir, pf), os.path.join(target_dir, pf))
        print(f"Copied pictures from {pics_src_dir} to {target_dir}")

    # Copy audio
    audio_src = f"audio/{lesson_str}.mp3"
    if os.path.exists(audio_src):
        shutil.copy2(audio_src, os.path.join(target_dir, "audio.mp3"))
        print(f"Copied {audio_src} to {target_dir}/audio.mp3")

    # Write Bai_XX/index.html
    target_index = os.path.join(target_dir, "index.html")
    with open(target_index, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Saved {target_index} ({len(output)} bytes)")

    # Also write HSK3_BaiXX_LuyenNghe.html at root (per SKILL.md line 32)
    root_html = f"HSK3_Bai{lesson_num}_LuyenNghe.html"
    root_output = output.replace('src="audio.mp3"', f'src="Bai_{lesson_str}/audio.mp3"')
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        root_output = root_output.replace(f'src="pic_{letter}.png"', f'src="Bai_{lesson_str}/pic_{letter}.png"')
    root_output = root_output.replace('../Bai_', 'Bai_')
    with open(root_html, 'w', encoding='utf-8') as f:
        f.write(root_output)
    print(f"Saved root shortcut: {root_html}")

    # 10. Run validation
    from core.validate_lesson import validate_lesson_file
    is_valid = validate_lesson_file(target_index)
    if is_valid:
        print(f"🎉 LESSON {lesson_num} SUCCESSFULLY BUILT AND 100% VALIDATED!")
    else:
        print(f"❌ LESSON {lesson_num} VALIDATION FAILED!")

    return is_valid

if __name__ == '__main__':
    lessons_to_build = [5, 6, 7]
    if len(sys.argv) > 1:
        lessons_to_build = [int(x) for x in sys.argv[1:]]

    all_passed = True
    for ln in lessons_to_build:
        passed = build_lesson(ln)
        if not passed:
            all_passed = False

    print("\n==========================================")
    if all_passed:
        print("ALL REQUESTED LESSONS BUILT & 100% VALIDATED!")
    else:
        print("SOME LESSONS FAILED VALIDATION! CHECK LOGS.")
    print("==========================================")
