# -*- coding: utf-8 -*-
"""
Build Engine for HSK 3 Pre-Study Web Lessons
Transforms extracted lesson data into a standalone, ultra-rich interactive web page.
Follows strict pedagogical standards and the Sunshine Yellow design system.
"""

import sys
import os
import json
import re
import importlib.util

# Ensure utf-8 output in Windows console
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.join(BASE_DIR, "core")
DATA_DIR = os.path.join(BASE_DIR, "data")
TEMPLATE_PATH = os.path.join(CORE_DIR, "template_prestudy_master.html")

LESSON_TITLES = [
    (1, "周末你有什么打算？", "Cuối tuần bạn có dự định gì?"),
    (2, "他什么时候回来？", "Khi nào anh ấy về?"),
    (3, "桌子上放着很多饮料", "Trên bàn để rất nhiều đồ uống"),
    (4, "她总是笑着跟客人说话", "Cô ấy luôn cười nói với khách"),
    (5, "我最近越来越胖了", "Dạo này em ngày càng béo ra"),
    (6, "怎么突然找不到了", "Sao tự nhiên lại không tìm thấy"),
    (7, "我跟他都认识五年了", "Tôi và anh ấy quen nhau 5 năm rồi"),
    (8, "你去哪儿我就去哪儿", "Em đi đâu anh đi theo đó"),
    (9, "她的汉语说得跟中国人一样好", "Tiếng Trung của cô ấy nói hay như người Trung Quốc"),
    (10, "数学比历史难多了", "Toán khó hơn Lịch sử nhiều"),
    (11, "别忘了把空调关了", "Đừng quên tắt máy điều hòa"),
    (12, "把重要的东西放在我这儿吧", "Hãy để những thứ quan trọng ở chỗ tôi"),
    (13, "我是走回来的", "Tôi đi bộ về đấy"),
    (14, "你把水果拿过来", "Em mang hoa quả qua đây"),
    (15, "其他都没什么问题", "Những thứ khác đều không vấn đề gì"),
    (16, "我现在累得想睡觉", "Bây giờ tôi mệt đến mức chỉ muốn ngủ"),
    (17, "谁都有办法看好病", "Ai cũng có cách chữa khỏi bệnh"),
    (18, "我相信他们会同意的", "Tôi tin rằng họ sẽ đồng ý"),
    (19, "你没看出来吗？", "Bạn không nhận ra à?"),
    (20, "我被他影响了", "Tôi bị anh ấy ảnh hưởng")
]

def get_pos_badge_style(pos):
    """Return distinct colorful styles for parts of speech"""
    pos_lower = pos.lower()
    if "danh" in pos_lower:
        return 'background:#ecfdf5; color:#065f46; border:1px solid #a7f3d0;'
    elif "động" in pos_lower:
        return 'background:#fff7ed; color:#9a3412; border:1px solid #fed7aa;'
    elif "tính" in pos_lower:
        return 'background:#faf5ff; color:#6b21a8; border:1px solid #e9d5ff;'
    elif "liên" in pos_lower:
        return 'background:#fefce8; color:#854d0e; border:1px solid #fef08a;'
    elif "phó" in pos_lower:
        return 'background:#f0f9ff; color:#075985; border:1px solid #bae6fd;'
    elif "lượng" in pos_lower:
        return 'background:#fff1f2; color:#9f1239; border:1px solid #fecdd3;'
    else:
        return 'background:#fef3c7; color:#b45309; border:1px solid #fde68a;'

def render_vocab_cards(vocab_list):
    cards_html = []
    for item in vocab_list:
        num = item.get("num", 1)
        zh = item.get("zh", "")
        py = item.get("py", "")
        hv = item.get("hv", "")
        pos = item.get("pos", "")
        vi = item.get("vi", "")
        radicals = item.get("radicals", "")
        eg1 = item.get("eg1", {})
        eg2 = item.get("eg2", {})
        expansion = item.get("expansion", "")

        pos_style = get_pos_badge_style(pos)

        card = f"""
          <div class="vocab-card" id="vocab-card-{num}">
            <div class="vocab-top">
              <div>
                <span class="vocab-hanzi" onclick="openVocabModal({num - 1})" title="👆 Bấm vào để phóng to">{zh}</span>
              </div>
              <div class="vocab-meta">
                <span class="vocab-py">{py}</span>
                <span class="vocab-hv">{hv}</span>
              </div>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
              <span class="vocab-pos" style="{pos_style}">{pos}</span>
              <div style="display:flex; gap:6px;">
                <button class="btn-tool btn-zoom" onclick="event.stopPropagation(); openVocabModal({num - 1})" title="Phóng to thẻ từ vựng này">🔍 Phóng to</button>
                <button class="btn-tool" onclick="speakText('{zh}')" title="Nghe phát âm chuẩn">🔊 Phát âm</button>
              </div>
            </div>

            <div class="vocab-meaning">🎯 {vi}</div>

            <details class="vocab-details">
              <summary>💡 Bấm xem chiết tự nhớ chữ</summary>
              <div class="vocab-details-content">
                <strong>💡 Chiết tự:</strong> {radicals}
              </div>
            </details>

            <div class="vocab-examples">
              <div class="example-line">
                <div class="example-zh">1. {eg1.get('zh', '')}</div>
                <div class="example-py">{eg1.get('py', '')}</div>
                <div class="example-vi">👉 {eg1.get('vi', '')}</div>
              </div>
              <div class="example-line">
                <div class="example-zh">2. {eg2.get('zh', '')}</div>
                <div class="example-py">{eg2.get('py', '')}</div>
                <div class="example-vi">👉 {eg2.get('vi', '')}</div>
              </div>
              {f'<div style="font-size:13px; color:#4338ca; background:#eef2ff; padding:8px 12px; border-radius:8px; border-left:3px solid #6366f1;"><strong>⭐ Mở rộng:</strong> {expansion}</div>' if expansion else ''}
            </div>

            <div class="stroke-player-wrapper">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-size:12.5px; font-weight:700; color:#64748b;">✍️ Cách viết Hán tự:</span>
                <button class="btn-tool" onclick="playStrokeAnim('{num}', '{zh}', this)">▶ Xem thứ tự nét</button>
              </div>
              <div id="stroke-anim-{num}" class="stroke-anim-container">
                <div id="stroke-chars-{num}" style="display:flex; justify-content:center; gap:8px; flex-wrap:wrap;"></div>
                <div style="margin-top:8px; display:flex; justify-content:center; gap:8px;">
                  <button class="btn-tool" style="font-size:11px;" onclick="replayStrokeAnim('{num}')">🔄 Chạy lại nét</button>
                  <button class="btn-tool" style="font-size:11px;" onclick="closeStrokeAnim('{num}')">✖ Đóng</button>
                </div>
              </div>
            </div>
          </div>
        """
        cards_html.append(card)
    return "\n".join(cards_html)

def render_dialogues(dialogues_list, lesson_id):
    dialogues_html = []
    for d in dialogues_list:
        d_num = d.get("num", 1)
        title = d.get("title", "")
        location = d.get("location", "")
        audio_file = d.get("audio_file") or d.get("audio_src") or f"audio_textbook/Bai_{lesson_id:02d}/{lesson_id:02d}-{d_num}.mp3"
        context = d.get("context", "")
        lines = d.get("lines", [])
        cq = d.get("check_question") or d.get("quiz") or {}

        # Build lines
        lines_html = []
        for l_idx, line in enumerate(lines):
            role = line.get("role", "female")
            speaker = line.get("speaker", "")
            zh = line.get("zh", "")
            py = line.get("py", "")
            vi = line.get("vi", "")
            analysis = line.get("analysis") or f"Từ vựng trọng điểm & phát âm chuẩn câu thoại."
            badge_id = f"acc-d{d_num}-l{l_idx}"

            line_box = f"""
              <div class="d-line">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                  <span class="d-speaker">👤 {speaker}</span>
                  <button class="btn-tool" style="font-size:11px; padding:2px 8px;" onclick="speakText('{zh}')">🔊 Nghe câu</button>
                </div>
                <div class="d-zh">{zh}</div>
                <div class="d-py">{py}</div>
                <div class="d-vi">{vi}</div>
                <div class="d-analysis">💡 {analysis}</div>
                <div class="shadowing-box">
                  <button class="btn-mic" onclick="startShadowing('{zh}', '{badge_id}', this)">🎙️ Luyện Shadowing câu này</button>
                  <span class="accuracy-badge" id="{badge_id}"></span>
                </div>
              </div>
            """
            lines_html.append(line_box)

        # Build check question
        q_text = cq.get("question") or cq.get("q") or ""
        options = cq.get("options", [])
        ans = cq.get("ans", "A")
        explain = cq.get("explain", "")

        opt_buttons = []
        for o_idx, opt in enumerate(options):
            if isinstance(opt, dict):
                opt_letter = opt.get("key", chr(65 + o_idx))
                opt_label = f"{opt.get('zh', '')} ({opt.get('py', '')}) - {opt.get('vi', '')}" if opt.get('vi') else opt.get('zh', '')
            else:
                opt_letter = chr(65 + o_idx)
                opt_label = str(opt)
            opt_buttons.append(f"""
              <button class="quiz-opt" onclick="selectDialogueCheck('{d_num}', '{opt_letter}', this)">
                <strong>{opt_letter}.</strong> {opt_label}
              </button>
            """)

        cq_html = f"""
          <div style="margin-top:18px; background:#fffbeb; border:1px solid #fde68a; border-radius:14px; padding:16px;">
            <div style="font-weight:800; font-size:14.5px; color:#92400e; margin-bottom:10px;">
              ❓ Câu hỏi hiểu bài: {q_text}
            </div>
            <div class="quiz-options" style="display:grid; grid-template-columns:1fr 1fr; gap:8px;">
              {"".join(opt_buttons)}
            </div>
            <div style="margin-top:10px; display:flex; gap:10px; align-items:center;">
              <button class="nav-btn btn-arena" style="padding:6px 14px; font-size:13px;" onclick="checkDialogueQuiz('{d_num}', '{ans}')">Kiểm tra đáp án</button>
              <div id="d-exp-{d_num}" style="display:none; font-size:13px; font-weight:600; padding:6px 12px; border-radius:8px;">
                💡 <strong>Giải thích:</strong> {explain}
              </div>
            </div>
          </div>
        """

        d_card = f"""
        <div class="dialogue-card" id="dialogue-{d_num}">
          <div class="dialogue-header">
            <div>
              <span style="font-size:12px; font-weight:800; background:#fef3c7; color:#92400e; padding:3px 10px; border-radius:12px; text-transform:uppercase;">BÀI KHÓA {d_num}</span>
              <h3 class="dialogue-title" style="margin-top:4px;">{title}</h3>
            </div>
            <span style="font-size:12.5px; font-weight:700; background:#f1f5f9; color:#475569; padding:4px 12px; border-radius:10px;">📍 {location}</span>
          </div>

          <div class="dialogue-audio-box">
            <div style="font-size:12px; font-weight:700; color:#b45309; margin-bottom:6px; display:flex; align-items:center; gap:6px;">
              <span>🎧 Audio chuẩn Sách Giáo Khoa ({lesson_id:02d}-{d_num}.mp3):</span>
            </div>
            <audio controls preload="none" src="../{audio_file}"></audio>
          </div>

          <div class="dialogue-context">
            <strong>Ngữ cảnh hội thoại:</strong> {context}
          </div>

          <div class="dialogue-lines">
            {"".join(lines_html)}
          </div>

          {cq_html}
        </div>
        """
        dialogues_html.append(d_card)

    return "\n".join(dialogues_html)

def render_grammar(grammar_list):
    grammar_html = []
    for g in grammar_list:
        g_id = g.get("id", 1)
        title = g.get("title", "")
        formula = g.get("formula", "")
        desc = g.get("desc", "")
        rules = g.get("key_rules", [])
        examples = g.get("examples", [])
        comparison_table = g.get("comparison_table", [])
        traps = g.get("traps", "")

        rules_html = ""
        if rules:
            r_items = "".join([f"<li style='margin-bottom:6px;'>{r}</li>" for r in rules])
            rules_html = f"""
              <div style="margin-bottom:14px;">
                <h4 style="font-size:14.5px; font-weight:800; color:#0f172a; margin-bottom:8px;">📌 Quy tắc then chốt:</h4>
                <ul style="padding-left:20px; font-size:14px; color:#334155; line-height:1.6;">
                  {r_items}
                </ul>
              </div>
            """

        table_html = ""
        if comparison_table:
            if isinstance(comparison_table, dict):
                headers = comparison_table.get("headers", ["Tiêu chí", "Phương án 1", "Phương án 2"])
                c_rows = comparison_table.get("rows", [])
                th_html = "".join([f'<th style="padding:10px 14px; border:1px solid #fde68a;">{h}</th>' for h in headers])
                tr_list = []
                for r in c_rows:
                    if isinstance(r, list):
                        tds = []
                        for idx, cell in enumerate(r):
                            bg = "#f8fafc" if idx == 0 else ("#fffdf5" if idx % 2 == 1 else "#f0f9ff")
                            color = "#0f172a" if idx == 0 else ("#b45309" if idx % 2 == 1 else "#0284c7")
                            weight = "700" if idx == 0 else "600"
                            tds.append(f'<td style="padding:10px 14px; font-weight:{weight}; color:{color}; background:{bg}; border:1px solid #e2e8f0;">{cell}</td>')
                        tr_list.append(f'<tr>{"".join(tds)}</tr>')
                table_html = f"""
                  <div style="overflow-x:auto; margin-bottom:16px;">
                    <table style="width:100%; border-collapse:collapse; font-size:13.5px; text-align:left;">
                      <thead>
                        <tr style="background:#fef3c7; color:#78350f;">
                          {th_html}
                        </tr>
                      </thead>
                      <tbody>
                        {"".join(tr_list)}
                      </tbody>
                    </table>
                  </div>
                """
            elif isinstance(comparison_table, list):
                rows = []
                for row in comparison_table:
                    if isinstance(row, dict):
                        rows.append(f"""
                          <tr>
                            <td style="padding:10px 14px; font-weight:700; background:#f8fafc; border:1px solid #e2e8f0;">{row.get('criteria', '')}</td>
                            <td style="padding:10px 14px; color:#b45309; font-weight:600; border:1px solid #e2e8f0; background:#fffdf5;">{row.get('haishi', '')}</td>
                            <td style="padding:10px 14px; color:#0284c7; font-weight:600; border:1px solid #e2e8f0; background:#f0f9ff;">{row.get('huozhe', '')}</td>
                          </tr>
                        """)
                table_html = f"""
                  <div style="overflow-x:auto; margin-bottom:16px;">
                    <table style="width:100%; border-collapse:collapse; font-size:13.5px; text-align:left;">
                      <thead>
                        <tr style="background:#fef3c7; color:#78350f;">
                          <th style="padding:10px 14px; border:1px solid #fde68a;">Tiêu chí</th>
                          <th style="padding:10px 14px; border:1px solid #fde68a;">还是 (háishì) - Câu hỏi / Phân vân</th>
                          <th style="padding:10px 14px; border:1px solid #fde68a;">或者 (huòzhě) - Câu khẳng định</th>
                        </tr>
                      </thead>
                      <tbody>
                        {"".join(rows)}
                      </tbody>
                    </table>
                  </div>
                """

        egs_html = ""
        if examples:
            e_items = []
            for eg in examples:
                e_items.append(f"""
                  <div class="example-line" style="margin-bottom:8px;">
                    <div class="example-zh">🔹 {eg.get('zh', '')}</div>
                    <div style="font-size:12.5px; color:#d97706; font-weight:600;">{eg.get('py', '')}</div>
                    <div class="example-vi">👉 {eg.get('vi', '')}</div>
                  </div>
                """)
            egs_html = f"""
              <div style="margin-bottom:14px;">
                <h4 style="font-size:14.5px; font-weight:800; color:#0f172a; margin-bottom:8px;">🌟 Câu ví dụ thực hành:</h4>
                {"".join(e_items)}
              </div>
            """

        traps_html = f"""
          <div class="grammar-traps">
            <strong>⚠️ BẪY ĐỀ THI HSK CẦN TRÁNH:</strong><br>
            {traps}
          </div>
        """

        g_card = f"""
        <div class="grammar-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <h3 class="grammar-title">Ngữ pháp {g_id}: {title}</h3>
            <span style="font-size:12px; font-weight:800; background:#fef3c7; color:#92400e; padding:3px 10px; border-radius:12px;">TRỌNG ĐIỂM HSK 3</span>
          </div>
          
          <div class="grammar-formula">
            <span style="font-size:12px; color:#b45309; text-transform:uppercase; letter-spacing:0.5px; display:block; margin-bottom:4px;">📐 CÔNG THỨC VÀNG:</span>
            {formula}
          </div>

          <p style="font-size:14.5px; color:#334155; margin-bottom:14px;">{desc}</p>

          {rules_html}
          {table_html}
          {egs_html}
          {traps_html}
        </div>
        """
        grammar_html.append(g_card)

    return "\n".join(grammar_html)

def render_mini_quiz(mini_quiz_list):
    quiz_html = []
    for q in mini_quiz_list:
        q_id = q.get("id", 1)
        question = q.get("q", "")
        py = q.get("py", "")
        vi = q.get("vi", "")
        options = q.get("options", [])
        ans = q.get("ans", "A")
        explain = q.get("explain", "")

        opt_buttons = []
        for opt in options:
            if isinstance(opt, dict):
                opt_key = opt.get("key", "A")
                opt_zh = opt.get("zh", "")
                opt_py = opt.get("py", "")
                opt_vi = opt.get("vi", "")
            else:
                opt_str = str(opt)
                opt_key = opt_str[:1]
                opt_zh = opt_str[2:].strip() if len(opt_str) > 2 else opt_str
                opt_py = ""
                opt_vi = ""

            py_html = f'<span class="quiz-opt-py">({opt_py})</span>' if opt_py else ''
            vi_html = f'<div class="quiz-vi-toggle">👉 {opt_vi}</div>' if opt_vi else ''

            opt_buttons.append(f"""
              <button class="quiz-opt" onclick="selectQuizOpt('{q_id}', '{opt_key}', this)">
                <div class="quiz-opt-main">
                  <strong style="color:#d97706; font-size:15px;">{opt_key}.</strong>
                  <span class="quiz-opt-zh">{opt_zh}</span>
                  {py_html}
                </div>
                {vi_html}
              </button>
            """)

        py_line = f'<div class="quiz-q-py">{py}</div>' if py else ''
        vi_line = f'<div class="quiz-vi-toggle" style="background:#fef3c7; color:#92400e; font-weight:600; padding:6px 10px; border-radius:6px; margin-top:6px;">👉 Dịch nghĩa câu hỏi: {vi}</div>' if vi else ''

        card = f"""
        <div class="quiz-card mini-quiz grammar-quiz" id="quiz-card-{q_id}">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:10px; gap:8px;">
            <div class="quiz-q" style="margin-bottom:0; flex:1;">
              <div><strong>Câu {q_id}:</strong> {question}</div>
              {py_line}
              {vi_line}
            </div>
            <button class="btn-tool" style="font-size:11px; padding:3px 8px; flex-shrink:0;" onclick="this.closest('.quiz-card').querySelectorAll('.quiz-vi-toggle').forEach(el => el.style.display = (el.style.display === 'block' ? 'none' : 'block'));" title="Xem dịch nghĩa câu này">👁 Dịch câu này</button>
          </div>
          <div class="quiz-options">
            {"".join(opt_buttons)}
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px; flex-wrap:wrap; gap:8px;">
            <button class="nav-btn btn-arena" style="padding:6px 16px; font-size:13px;" onclick="checkMiniQuiz('{q_id}', '{ans}')">Kiểm tra kết quả</button>
            <span style="font-size:12px; color:#64748b;">Chọn phương án rồi bấm kiểm tra</span>
          </div>
          <div class="quiz-explain" id="quiz-exp-{q_id}">
            <strong>Đáp án đúng: {ans}</strong><br>
            💡 {explain}
          </div>
        </div>
        """
        quiz_html.append(card)

    return "\n".join(quiz_html)

def generate_fallback_assembly_puzzles(vocab_list):
    """
    Tự động sinh câu đố Xưởng Ghép Chữ Hán dự phòng nếu bài học chưa có assembly_puzzles thủ công.
    Đảm bảo minigame luôn hoạt động đầy đủ 100% không bị rỗng.
    """
    puzzles = []
    all_chars = []
    for item in vocab_list:
        clean = re.sub(r'[^\u4e00-\u9fa5]', '', item.get("zh", ""))
        for c in clean:
            if c not in all_chars:
                all_chars.append(c)

    distractor_pool = ["日", "月", "木", "氵", "亻", "心", "口", "辶", "女", "土", "艹", "扌", "火"]

    for idx, item in enumerate(vocab_list):
        zh = item.get("zh", "")
        py = item.get("py", "")
        vi = item.get("vi", "")
        radicals = item.get("radicals", "")
        eg = item.get("eg1", {}).get("zh", "")
        clean_chars = [c for c in zh if '\u4e00' <= c <= '\u9fa5']
        if not clean_chars:
            continue

        if len(clean_chars) >= 2:
            parts = [{"char": c, "name": f"Chữ {c}"} for c in clean_chars[:2]]
        else:
            parts = [{"char": clean_chars[0], "name": f"Chữ {clean_chars[0]}"}]

        chosen_distractors = []
        for d in distractor_pool + all_chars:
            if d not in [p["char"] for p in parts] and d not in [cd["char"] for cd in chosen_distractors]:
                chosen_distractors.append({"char": d, "name": f"Bộ/Chữ {d}"})
                if len(chosen_distractors) >= 2:
                    break

        puzzles.append({
            "id": idx + 1,
            "target_zh": zh,
            "py": py,
            "vi": vi,
            "parts": parts,
            "distractors": chosen_distractors,
            "story": radicals if radicals else f"Chữ Hán: {zh} ({py}) nghĩa là: {vi}",
            "example": eg if eg else f"Ví dụ với {zh}."
        })
    return puzzles

def build_lesson(lesson_num=3):
    print(f"\n==========================================")
    print(f"BUILDING PRE-STUDY WEB FOR LESSON {lesson_num:02d}")
    print(f"==========================================")

    data_file = os.path.join(DATA_DIR, f"extracted_soan_bai_{lesson_num:02d}.py")
    if not os.path.exists(data_file):
        print(f"❌ Data file not found: {data_file}")
        return False

    # Dynamic import of extracted data
    spec = importlib.util.spec_from_file_location("lesson_data_module", data_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    lesson_data = module.LESSON_DATA

    info = lesson_data.get("lesson_info", {})
    vocab = lesson_data.get("vocab", [])
    matching_pairs = lesson_data.get("matching_pairs", [])
    dialogues = lesson_data.get("dialogues", [])
    grammar = lesson_data.get("grammar", [])
    mini_quiz = lesson_data.get("mini_quiz", [])

    # Read master template
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # Generate components
    vocab_cards_html = render_vocab_cards(vocab)
    dialogues_html = render_dialogues(dialogues, lesson_num)
    grammar_html = render_grammar(grammar)
    mini_quiz_html = render_mini_quiz(mini_quiz)

    # Prep JSON
    vocab_json = json.dumps(vocab, ensure_ascii=False)
    matching_json = json.dumps(matching_pairs, ensure_ascii=False)
    assembly_puzzles = lesson_data.get("assembly_puzzles", [])
    if not assembly_puzzles and vocab:
        print(f"ℹ️ Chú ý: Chưa tìm thấy 'assembly_puzzles' tùy chỉnh. Đang tự động sinh {len(vocab)} câu đố ghép chữ từ từ vựng...")
        assembly_puzzles = generate_fallback_assembly_puzzles(vocab)
    assembly_json = json.dumps(assembly_puzzles, ensure_ascii=False)

    # Generate lesson dropdown options
    opts = []
    for num, zh, vi in LESSON_TITLES:
        url = "index.html" if num == lesson_num else f"../Bai_{num:02d}/index.html"
        sel = ' selected' if num == lesson_num else ''
        opts.append(f'          <option value="{url}"{sel}>Bài {num:02d}: {zh} ({vi})</option>')
    lesson_nav_options = "\n".join(opts)

    # Fast Prev / Next buttons
    if lesson_num <= 1:
        prev_btn = '<button class="nav-btn prev-btn" disabled title="Đây là bài học đầu tiên">◀ Bài trước</button>'
    else:
        prev_url = f"../Bai_{lesson_num-1:02d}/index.html"
        prev_btn = f'<a href="{prev_url}" class="nav-btn prev-btn" title="Quay lại bài {lesson_num-1:02d}">◀ Bài trước</a>'

    if lesson_num >= 20:
        next_btn = '<button class="nav-btn next-btn" disabled title="Đây là bài học cuối cùng">Bài tiếp ▶</button>'
    else:
        next_url = f"../Bai_{lesson_num+1:02d}/index.html"
        next_btn = f'<a href="{next_url}" class="nav-btn next-btn" title="Chuyển sang bài {lesson_num+1:02d}">Bài tiếp ▶</a>'

    # Replace placeholders
    content = template.replace("{{LESSON_NUM}}", f"{lesson_num:02d}")
    content = content.replace("{{LESSON_TITLE_ZH}}", info.get("title_zh", ""))
    content = content.replace("{{LESSON_TITLE_VI}}", info.get("title_vi", ""))
    content = content.replace("{{LESSON_TITLE_PY}}", info.get("title_py", ""))
    content = content.replace("{{LESSON_SUBTITLE}}", info.get("subtitle", ""))
    content = content.replace("{{EXAM_WEB_URL}}", info.get("exam_web_url", f"../../1_Web_LuyenThi_HSK3/Bai_{lesson_num:02d}/index.html"))
    content = content.replace("{{PREV_LESSON_BTN}}", prev_btn)
    content = content.replace("{{NEXT_LESSON_BTN}}", next_btn)
    content = content.replace("{{LESSON_NAV_OPTIONS}}", lesson_nav_options)
    content = content.replace("{{VOCAB_CARDS_HTML}}", vocab_cards_html)
    content = content.replace("{{DIALOGUES_HTML}}", dialogues_html)
    content = content.replace("{{GRAMMAR_HTML}}", grammar_html)
    content = content.replace("{{MINI_QUIZ_HTML}}", mini_quiz_html)
    content = content.replace("{{VOCAB_JSON}}", vocab_json)
    content = content.replace("{{MATCHING_JSON}}", matching_json)
    content = content.replace("{{ASSEMBLY_JSON}}", assembly_json)

    # Output directory
    output_dir = os.path.join(BASE_DIR, f"Bai_{lesson_num:02d}")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "index.html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ SUCCESSFULLY COMPILED: {output_file} ({len(content)} bytes)")

    # Run validator
    validator_path = os.path.join(CORE_DIR, "validate_prestudy.py")
    if os.path.exists(validator_path):
        import subprocess
        res = subprocess.run([sys.executable, validator_path, output_file], capture_output=True, text=True, encoding="utf-8")
        print(res.stdout)
        if res.returncode != 0:
            print("❌ Validation warnings/errors:", res.stderr)
            return False

    return True

if __name__ == "__main__":
    target_num = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    build_lesson(target_num)
