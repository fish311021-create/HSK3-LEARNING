# -*- coding: utf-8 -*-
"""
Build Engine for HSK 3 Pre-Study Web Lessons
Transforms extracted lesson data into a standalone, ultra-rich interactive web page.
Follows strict pedagogical standards and the Sunshine Yellow design system.
"""

import sys
import os
import json
import importlib.util

# Ensure utf-8 output in Windows console
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.join(BASE_DIR, "core")
DATA_DIR = os.path.join(BASE_DIR, "data")
TEMPLATE_PATH = os.path.join(CORE_DIR, "template_prestudy_master.html")

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
        stroke_info = item.get("stroke_info", "")
        eg1 = item.get("eg1", {})
        eg2 = item.get("eg2", {})
        expansion = item.get("expansion", "")

        pos_style = get_pos_badge_style(pos)

        card = f"""
          <div class="vocab-card" id="vocab-card-{num}">
            <div class="vocab-top">
              <div>
                <span class="vocab-hanzi">{zh}</span>
              </div>
              <div class="vocab-meta">
                <span class="vocab-py">{py}</span>
                <span class="vocab-hv">{hv}</span>
              </div>
            </div>
            
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:10px;">
              <span class="vocab-pos" style="{pos_style}">{pos}</span>
              <button class="btn-tool" onclick="speakText('{zh}')" title="Nghe phát âm chuẩn">🔊 Phát âm</button>
            </div>

            <div class="vocab-meaning">🎯 {vi}</div>

            <div class="vocab-breakdown">
              <div style="margin-bottom:4px;"><strong>💡 Chiết tự:</strong> {radicals}</div>
              <div><strong>✍️ Nét bút:</strong> {stroke_info}</div>
            </div>

            <div class="vocab-examples">
              <div class="example-line">
                <div class="example-zh">1. {eg1.get('zh', '')}</div>
                <div style="font-size:12px; color:#d97706; font-weight:600;">{eg1.get('py', '')}</div>
                <div class="example-vi">👉 {eg1.get('vi', '')}</div>
              </div>
              <div class="example-line">
                <div class="example-zh">2. {eg2.get('zh', '')}</div>
                <div style="font-size:12px; color:#d97706; font-weight:600;">{eg2.get('py', '')}</div>
                <div class="example-vi">👉 {eg2.get('vi', '')}</div>
              </div>
              {f'<div style="font-size:12.5px; color:#4338ca; background:#eef2ff; padding:6px 10px; border-radius:8px; border-left:3px solid #6366f1;"><strong>⭐ Mở rộng:</strong> {expansion}</div>' if expansion else ''}
            </div>

            <div class="canvas-container">
              <div class="canvas-label">
                <span>✍️ Ô mễ tập viết: <strong>{zh}</strong></span>
                <span style="font-size:11px; color:#94a3b8;">Dùng chuột / tay để viết</span>
              </div>
              <canvas class="hanzi-canvas" id="canvas-vocab-{num}" width="160" height="160"></canvas>
              <div class="canvas-tools">
                <button class="btn-tool" onclick="clearCanvas('canvas-vocab-{num}')">🗑️ Xóa viết lại</button>
                <button class="btn-tool" onclick="speakText('{zh}')">🔊 Nghe mẫu</button>
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
        audio_file = d.get("audio_file", "")
        context = d.get("context", "")
        lines = d.get("lines", [])
        cq = d.get("check_question", {})

        # Build lines
        lines_html = []
        for l_idx, line in enumerate(lines):
            role = line.get("role", "female")
            speaker = line.get("speaker", "")
            zh = line.get("zh", "")
            py = line.get("py", "")
            vi = line.get("vi", "")
            analysis = line.get("analysis", "")
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
        q_text = cq.get("question", "")
        options = cq.get("options", [])
        ans = cq.get("ans", "A")
        explain = cq.get("explain", "")

        opt_buttons = []
        for o_idx, opt in enumerate(options):
            opt_letter = chr(65 + o_idx)
            opt_buttons.append(f"""
              <button class="quiz-opt" onclick="selectDialogueCheck('{d_num}', '{opt_letter}', this)">
                <strong>{opt_letter}.</strong> {opt}
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
              <span>🎧 Audio chuẩn Sách Giáo Khoa (03-{d_num}.mp3):</span>
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
            rows = []
            for row in comparison_table:
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
        options = q.get("options", [])
        ans = q.get("ans", "A")
        explain = q.get("explain", "")

        opt_buttons = []
        for opt in options:
            opt_letter = opt[:1]
            opt_buttons.append(f"""
              <button class="quiz-opt" onclick="selectQuizOpt('{q_id}', '{opt_letter}', this)">
                {opt}
              </button>
            """)

        card = f"""
        <div class="quiz-card mini-quiz grammar-quiz" id="quiz-card-{q_id}">
          <div class="quiz-q">Câu {q_id}: {question}</div>
          <div class="quiz-options">
            {"".join(opt_buttons)}
          </div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-top:12px;">
            <button class="nav-btn btn-arena" style="padding:6px 16px; font-size:13px;" onclick="checkMiniQuiz('{q_id}', '{ans}')">Kiểm tra kết quả</button>
            <span style="font-size:12.5px; color:#64748b;">Chọn đáp án đúng rồi bấm kiểm tra</span>
          </div>
          <div class="quiz-explain" id="quiz-exp-{q_id}">
            <strong>Đáp án đúng: {ans}</strong><br>
            💡 {explain}
          </div>
        </div>
        """
        quiz_html.append(card)

    return "\n".join(quiz_html)

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

    # Replace placeholders
    content = template.replace("{{LESSON_NUM}}", f"{lesson_num:02d}")
    content = content.replace("{{LESSON_TITLE_ZH}}", info.get("title_zh", ""))
    content = content.replace("{{LESSON_TITLE_VI}}", info.get("title_vi", ""))
    content = content.replace("{{LESSON_TITLE_PY}}", info.get("title_py", ""))
    content = content.replace("{{LESSON_SUBTITLE}}", info.get("subtitle", ""))
    content = content.replace("{{EXAM_WEB_URL}}", info.get("exam_web_url", f"../../1_Web_LuyenThi_HSK3/Bai_{lesson_num:02d}/index.html"))
    content = content.replace("{{VOCAB_CARDS_HTML}}", vocab_cards_html)
    content = content.replace("{{DIALOGUES_HTML}}", dialogues_html)
    content = content.replace("{{GRAMMAR_HTML}}", grammar_html)
    content = content.replace("{{MINI_QUIZ_HTML}}", mini_quiz_html)
    content = content.replace("{{VOCAB_JSON}}", vocab_json)
    content = content.replace("{{MATCHING_JSON}}", matching_json)

    # Add dialogue quiz JS helper
    extra_dialogue_js = """
    // DIALOGUE QUIZ HELPER
    const userDialogueAnswers = {};
    function selectDialogueCheck(dNum, optKey, btn) {
      userDialogueAnswers[dNum] = optKey;
      btn.parentElement.querySelectorAll('.quiz-opt').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    }
    function checkDialogueQuiz(dNum, correctAns) {
      const selected = userDialogueAnswers[dNum];
      if (!selected) {
        alert("Vui lòng chọn một phương án!");
        return;
      }
      const exp = document.getElementById(`d-exp-${dNum}`);
      exp.style.display = 'block';
      if (selected === correctAns) {
        exp.style.background = '#dcfce7';
        exp.style.color = '#166534';
      } else {
        exp.style.background = '#fee2e2';
        exp.style.color = '#991b1b';
      }
    }
    """
    content = content.replace("// INITIALIZATION", extra_dialogue_js + "\n    // INITIALIZATION")

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
