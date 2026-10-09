# -*- coding: utf-8 -*-
"""
Build Engine for HSK 3 Pre-Study Web Lessons (AI Multimodal Edition - 2.1)
Transforms extracted lesson data into an ultra-rich interactive web page with Gemini Flash Vision AI Assistant.
Follows strict pedagogical standards, Sunshine Yellow design system, and Zero Demo Buttons rule.
"""

import sys
import os
import json
import re
import importlib.util
import shutil

# Ensure utf-8 output in Windows console
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE_DIR = os.path.join(BASE_DIR, "core")
DATA_DIR = os.path.join(BASE_DIR, "data")
TEMPLATE_PATH = os.path.join(CORE_DIR, "template_prestudy_ai_master.html")

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

            <div class="stroke-box">
              <button class="btn-tool" style="width:100%; font-size:12px; font-weight:700;" onclick="toggleStrokeAnim('{num}', '{zh}')">✍️ Xem cách viết từng nét chữ Hán</button>
              <div id="stroke-anim-{num}" class="stroke-anim-container" style="display:none;">
                <div id="writer-{num}" style="display:inline-block; border:1.5px dashed #f59e0b; border-radius:12px; background:#fff; padding:6px;"></div>
                <div style="margin-top:8px; display:flex; gap:8px; justify-content:center;">
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
    for idx, d in enumerate(dialogues_list):
        d_num = d.get("num") or d.get("id") or (idx + 1)
        title = d.get("title", "")
        location = d.get("location", "")
        audio_file = d.get("audio_file") or d.get("audio_src") or f"audio_textbook/Bai_{lesson_id:02d}/{lesson_id:02d}-{d_num}.mp3"
        context = d.get("context", "")
        lines = d.get("lines", [])
        cq = d.get("check_question") or d.get("quiz") or {}

        # Build lines
        lines_html = []
        for l_idx, line in enumerate(lines):
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

        # AI Assistant Box for this dialogue (Zero demo buttons rule)
        ai_box_html = f"""
          <!-- AI QUESTION ASSISTANT FOR DIALOGUE {d_num} -->
          <div class="ai-qa-box" id="aiQaBox-{d_num}">
            <div class="ai-qa-header">
              <div class="ai-qa-title">
                <span>📸 🤖 Trợ Lý AI: Chụp Ảnh Câu Hỏi Của Giáo Viên (Bài Khóa {d_num})</span>
              </div>
              <div style="display:flex; gap:8px; align-items:center;">
                <span class="ai-qa-badge">✨ Gemini Multimodal</span>
                <button class="btn-ai-settings" onclick="openGeminiSettings()" title="Cài đặt Google Gemini API Key">⚙️ Cài đặt API Key</button>
              </div>
            </div>
            
            <p class="ai-qa-desc">
              Chụp ảnh slide chiếu, bảng đen hoặc phiếu bài tập giáo viên vừa giao. AI sẽ nhận diện câu hỏi, đối chiếu bài khóa gốc <strong>{title}</strong> và hướng dẫn bạn trả lời từng câu chuẩn ngữ pháp HSK 3!
            </p>

            <div class="ai-upload-area" id="aiUploadArea-{d_num}" onclick="document.getElementById('aiFileInput-{d_num}').click()" ondragover="handleAiDragOver(event, {d_num})" ondragleave="handleAiDragLeave(event, {d_num})" ondrop="handleAiDrop(event, {d_num})">
              <div style="font-size:30px; margin-bottom:6px;">📸 📁 📋</div>
              <div style="font-size:14.5px; font-weight:700; color:#1e293b;">Bấm vào đây để chọn ảnh hoặc Dán ảnh từ Clipboard (Ctrl + V)</div>
              <div style="font-size:12.5px; color:#64748b; margin-top:4px;">Nhận diện được chữ in slide, màn hình máy chiếu nghiêng và chữ viết tay</div>

              <input type="file" id="aiFileInput-{d_num}" accept="image/*" style="display:none;" onchange="handleAiFileSelect(event, {d_num})">
              <input type="file" id="aiCameraInput-{d_num}" accept="image/*" capture="environment" style="display:none;" onchange="handleAiFileSelect(event, {d_num})">

              <div class="ai-upload-actions" onclick="event.stopPropagation()">
                <button class="btn-ai-action btn-ai-camera" onclick="document.getElementById('aiCameraInput-{d_num}').click()">
                  📷 Chụp Ảnh Ngay
                </button>
                <button class="btn-ai-action btn-ai-file" onclick="document.getElementById('aiFileInput-{d_num}').click()">
                  📁 Tải File Ảnh
                </button>
              </div>
            </div>

            <!-- Preview box -->
            <div class="ai-preview-box" id="aiPreviewBox-{d_num}">
              <div class="ai-preview-inner">
                <img id="aiPreviewImg-{d_num}" class="ai-preview-img" src="" alt="Ảnh câu hỏi">
                <div class="ai-preview-info">
                  <div id="aiPreviewName-{d_num}" class="ai-preview-filename" style="font-weight:700; color:#0f172a;">ảnh_cau_hoi.jpg</div>
                  <div id="aiPreviewSize-{d_num}" class="ai-preview-filesize" style="font-size:11.5px; color:#64748b;">Đã sẵn sàng phân tích</div>
                </div>
              </div>
              <div class="ai-preview-actions">
                <button class="btn-tool" style="color:#ef4444; border-color:#fca5a5; background:#fef2f2; padding:8px 14px; font-weight:700;" onclick="clearAiImage({d_num})">✖ Bỏ ảnh</button>
                <button class="btn-ai-action btn-ai-camera" style="font-weight:800; padding:10px 20px; font-size:14px;" onclick="analyzeQuestionWithAI({d_num})">🚀 Bắt Đầu Phân Tích</button>
              </div>
            </div>

            <!-- Optional manual text input -->
            <div class="ai-text-override-box">
              <details style="font-size:13px; color:#64748b;">
                <summary style="cursor:pointer; font-weight:600;">✍️ Hoặc tự gõ/dán câu hỏi văn bản nếu không muốn chụp ảnh</summary>
                <div style="display:flex; gap:8px; margin-top:8px;">
                  <input type="text" id="aiManualInput-{d_num}" class="ai-text-override-input" placeholder="Ví dụ: Đề bài hoặc câu hỏi của giáo viên...">
                  <button class="btn-tool" style="font-weight:700;" onclick="analyzeManualTextWithAI({d_num})">Phân tích</button>
                </div>
              </details>
            </div>

            <!-- Loading scanner -->
            <div class="ai-loading-scan" id="aiLoadingScan-{d_num}">
              <div style="font-weight:800; font-size:14.5px; color:#b45309;">
                🔍 AI đang quét ảnh, nhận diện Hán tự &amp; đối chiếu bài khóa gốc...
              </div>
              <div class="ai-scan-bar">
                <div class="ai-scan-progress"></div>
              </div>
            </div>

            <!-- Results Panel -->
            <div class="ai-result-panel" id="aiResultPanel-{d_num}"></div>
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

          {ai_box_html}
        </div>
        """
        dialogues_html.append(d_card)

    return "\n".join(dialogues_html)

def extract_dialogue_contexts(dialogues_list):
    """Generate clean DIALOGUE_CONTEXTS object for Gemini System Prompts"""
    contexts = {}
    for idx, d in enumerate(dialogues_list):
        d_num = d.get("num") or d.get("id") or (idx + 1)
        title = d.get("title", "")
        lines = d.get("lines", [])
        dialogue_text = "\n".join([f"{l.get('speaker', '')}：{l.get('zh', '')}" for l in lines])
        contexts[d_num] = {
            "num": d_num,
            "title": title,
            "text": dialogue_text
        }
    return json.dumps(contexts, ensure_ascii=False, indent=2)

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

        rules_li = "".join([f"<li>{r}</li>" for r in rules])
        eg_html = []
        for eg in examples:
            eg_html.append(f"""
              <div class="grammar-example-item">
                <div class="g-zh">{eg.get('zh', '')}</div>
                <div class="g-py">{eg.get('py', '')}</div>
                <div class="g-vi">👉 {eg.get('vi', '')}</div>
                {f'<div class="g-note">💡 {eg.get("note")}</div>' if eg.get('note') else ''}
              </div>
            """)

        comp_html = ""
        if comparison_table:
            if isinstance(comparison_table, dict):
                headers = comparison_table.get("headers", [])
                rows_data = comparison_table.get("rows", [])
                th_html = "".join([f"<th>{h}</th>" for h in headers])
                tr_html = []
                for r in rows_data:
                    tds = []
                    for idx, cell in enumerate(r):
                        if idx == 0:
                            tds.append(f"<td><strong>{cell}</strong></td>")
                        elif idx == 1:
                            tds.append(f"<td style='color:#b45309; font-weight:700;'>{cell}</td>")
                        else:
                            tds.append(f"<td>{cell}</td>")
                    tr_html.append(f"<tr>{''.join(tds)}</tr>")
                comp_html = f"""
                  <div style="overflow-x:auto; margin:16px 0;">
                    <table class="comparison-table">
                      <thead><tr>{th_html}</tr></thead>
                      <tbody>{"".join(tr_html)}</tbody>
                    </table>
                  </div>
                """
            elif isinstance(comparison_table, list):
                rows = []
                for row in comparison_table:
                    if isinstance(row, dict):
                        rows.append(f"""
                          <tr>
                            <td><strong>{row.get('feature', '')}</strong></td>
                            <td style="color:#b45309; font-weight:700;">{row.get('col1', '')}</td>
                            <td style="color:#0284c7; font-weight:700;">{row.get('col2', '')}</td>
                          </tr>
                        """)
                    elif isinstance(row, list):
                        tds = "".join([f"<td>{c}</td>" for c in row])
                        rows.append(f"<tr>{tds}</tr>")
                comp_html = f"""
                  <div style="overflow-x:auto; margin:16px 0;">
                    <table class="comparison-table">
                      <thead>
                        <tr>
                          <th>Đặc điểm so sánh</th>
                          <th>Cột 1</th>
                          <th>Cột 2</th>
                        </tr>
                      </thead>
                      <tbody>{"".join(rows)}</tbody>
                    </table>
                  </div>
                """

        g_card = f"""
          <div class="grammar-card">
            <h3 class="grammar-title">⚡ Điểm {g_id}: {title}</h3>
            <div class="grammar-formula">{formula}</div>
            <p style="font-size:14px; color:#475569; margin-bottom:12px;">{desc}</p>
            <ul class="grammar-rules">
              {rules_li}
            </ul>
            {comp_html}
            <div style="font-weight:700; font-size:14px; color:#0f172a; margin:14px 0 8px;">Ví dụ thực hành:</div>
            <div class="grammar-examples">
              {"".join(eg_html)}
            </div>
            {f'<div class="grammar-traps"><strong>⚠️ Bẫy đề thi HSK 3 cần lưu ý:</strong><br>{traps}</div>' if traps else ''}
          </div>
        """
        grammar_html.append(g_card)

    return "\n".join(grammar_html)

def render_mini_quiz(mini_quiz_list):
    quiz_html = []
    for q_idx, q in enumerate(mini_quiz_list):
        q_id = q.get("id", q_idx + 1)
        question = q.get("question", "")
        py = q.get("py", "")
        vi = q.get("vi", "")
        options = q.get("options", [])
        ans = q.get("ans", "A")
        explain = q.get("explain", "")

        opt_buttons = []
        for o_idx, opt in enumerate(options):
            opt_letter = chr(65 + o_idx)
            if isinstance(opt, dict):
                opt_letter = opt.get("key", opt_letter)
                opt_zh = opt.get("zh", "")
                opt_py = opt.get("py", "")
                opt_vi = opt.get("vi", "")
                opt_text = f"<strong>{opt_letter}.</strong> {opt_zh} <span style='color:#b45309; font-size:12px;'>({opt_py})</span>"
                if opt_vi:
                    opt_text += f" - <span style='color:#64748b; font-size:12px;'>{opt_vi}</span>"
            else:
                opt_text = f"<strong>{opt_letter}.</strong> {opt}"

            opt_buttons.append(f"""
              <button class="quiz-btn" onclick="selectQuizAnswer({q_id}, '{opt_letter}', this)">
                {opt_text}
              </button>
            """)

        q_item = f"""
          <div class="quiz-item" id="quiz-item-{q_id}">
            <div class="quiz-q-zh">{q_id}. {question}</div>
            <div class="quiz-q-py">{py}</div>
            <div class="quiz-q-vi quiz-trans" id="quiz-trans-{q_id}">Dịch nghĩa: {vi}</div>
            <div style="margin-top:6px; margin-bottom:12px;">
              <button class="btn-tool" style="font-size:11px; padding:3px 10px;" onclick="toggleSingleQuizTrans({q_id})">👁 Dịch câu này</button>
            </div>
            <div class="quiz-options-grid">
              {"".join(opt_buttons)}
            </div>
            <div style="margin-top:12px; display:flex; gap:10px; align-items:center;">
              <button class="nav-btn btn-arena" style="padding:6px 14px; font-size:13px;" onclick="checkSingleQuiz({q_id}, '{ans}')">Kiểm tra kết quả</button>
              <div id="quiz-exp-{q_id}" class="quiz-explain" style="display:none;">
                💡 <strong>Giải thích:</strong> {explain}
              </div>
            </div>
          </div>
        """
        quiz_html.append(q_item)

    return "\n".join(quiz_html)

def generate_fallback_assembly_puzzles(vocab_list):
    """Automatically generate radical Lego puzzles if not explicitly authored"""
    puzzles = []
    RADICAL_MAP = {
        '打算': (['扌', '丁', '竹', '目'], ['木', '日', '口']),
        '周末': (['土', '木', '一'], ['日', '月', '十']),
        '决定': (['冫', '夬', '宀', '疋'], ['氵', '口', '人']),
        '准备': (['冫', '夂', '田', '亻'], ['氵', '攵', '木']),
        '带': (['丩', '冖', '巾'], ['口', '日', '人']),
        '搬': (['扌', '舟', '殳'], ['木', '月', '几']),
        '面包': (['面', '勹', '巳'], ['麦', '口', '日']),
        '地图': (['土', '也', '囗', '冬'], ['日', '月', '木']),
        '客': (['宀', '夂', '口'], ['人', '木', '日']),
        '经理': (['纟', '巠', '王', '里'], ['木', '日', '口']),
        '绿茶': (['纟', '录', '艹', '人', '木'], ['水', '日', '月']),
        '衬衫': (['衤', '寸', '衤', '彡'], ['礻', '木', '口']),
        '元': (['一', '兀'], ['二', '人', '十']),
        '放': (['方', '攵'], ['文', '木', '日']),
        '饮料': (['饣', '欠', '米', '斗'], ['口', '日', '月']),
        '花': (['艹', '亻', '匕'], ['木', '日', '口'])
    }

    for item in vocab_list[:8]:
        zh = item.get("zh", "")
        py = item.get("py", "")
        vi = item.get("vi", "")
        hv = item.get("hv", "")

        matched_rads = None
        matched_distractors = ['木', '日', '口', '人']
        for k, v in RADICAL_MAP.items():
            if k in zh or zh in k:
                matched_rads = v[0]
                matched_distractors = v[1]
                break

        if not matched_rads:
            matched_rads = ['亻', '木', '口'][:len(zh)+1]

        puzzles.append({
            "target_zh": zh,
            "target_py": py,
            "target_vi": vi,
            "target_hv": hv,
            "slots": [{"hint": f"Nét {idx+1}"} for idx in range(len(matched_rads))],
            "correct_radicals": matched_rads,
            "distractors": matched_distractors,
            "story": f"Chữ '{zh}' ({py}) có nghĩa là '{vi}'. Hãy ghi nhớ các bộ phận cấu thành để viết chuẩn bút thuận!"
        })

    return puzzles

def build_lesson(lesson_num):
    print(f"\n========================================================")
    print(f"BUILDING HSK 3 PRE-STUDY LESSON {lesson_num:02d} (AI Multimodal 2.1)")
    print(f"========================================================")

    # Import extracted data
    data_file = os.path.join(DATA_DIR, f"extracted_soan_bai_{lesson_num:02d}.py")
    if not os.path.exists(data_file):
        print(f"❌ ERROR: Data file not found: {data_file}")
        return False

    spec = importlib.util.spec_from_file_location(f"extracted_soan_bai_{lesson_num:02d}", data_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    lesson_data = getattr(module, "LESSON_DATA", {})
    if not lesson_data:
        print(f"❌ ERROR: LESSON_DATA not found in {data_file}")
        return False

    info = lesson_data.get("lesson_info", {})
    vocab = lesson_data.get("vocab", [])
    dialogues = lesson_data.get("dialogues", [])
    grammar = lesson_data.get("grammar", [])
    mini_quiz = lesson_data.get("mini_quiz", [])
    matching_pairs = lesson_data.get("matching_pairs", [])

    # Read AI master template
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
        assembly_puzzles = generate_fallback_assembly_puzzles(vocab)
    assembly_json = json.dumps(assembly_puzzles, ensure_ascii=False)

    # Extract dialogue contexts for Gemini AI engine
    dialogue_contexts_json = extract_dialogue_contexts(dialogues)

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
    content = content.replace("{{DIALOGUE_CONTEXTS_JSON}}", dialogue_contexts_json)

    # Output directory
    output_dir = os.path.join(BASE_DIR, f"Bai_{lesson_num:02d}")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "index.html")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    # Ensure gemini_config.js exists in the lesson folder
    lesson_cfg = os.path.join(output_dir, "gemini_config.js")
    root_cfg = os.path.join(BASE_DIR, "gemini_config.js")
    if not os.path.exists(lesson_cfg) and os.path.exists(root_cfg):
        shutil.copy2(root_cfg, lesson_cfg)

    print(f"✅ SUCCESSFULLY COMPILED: {output_file} ({len(content)} bytes)")

    # Run validator
    validator_path = os.path.join(CORE_DIR, "validate_prestudy_ai.py")
    if os.path.exists(validator_path):
        import subprocess
        res = subprocess.run([sys.executable, validator_path, output_file], capture_output=True, text=True, encoding="utf-8")
        print(res.stdout)
        if res.returncode != 0:
            print("❌ Validation warnings/errors:", res.stderr)
            return False

    return True

if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "1"
    if arg == "all":
        successes = 0
        for i in range(1, 21):
            if build_lesson(i):
                successes += 1
        print(f"\n✨ Built {successes}/20 AI lessons successfully!")
    else:
        build_lesson(int(arg))
