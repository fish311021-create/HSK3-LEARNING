# -*- coding: utf-8 -*-
"""
Validation Engine for HSK 3 Pre-Study AI Web Lessons (Edition 2.1)
Ensures 100% compliance with pedagogical, interactive, UX, and Gemini Vision AI standards.
"""

import sys
import os
import re

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def validate_prestudy_ai_file(file_path):
    print(f"\n==========================================")
    print(f"VALIDATING PRE-STUDY AI LESSON (2.1): {file_path}")
    print(f"==========================================")

    if not os.path.exists(file_path):
        print(f"❌ ERROR: File does not exist: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    warnings = []

    # 1. Check Title & Metadata
    if "<title>" not in content or "HSK 3" not in content:
        errors.append("Thiếu thẻ <title> chuẩn HSK 3!")

    # 2. Check Bright / Yellow Theme Tokens (Sunshine Gold Palette)
    if "#f59e0b" not in content and "#fbbf24" not in content and "#eab308" not in content:
        warnings.append("Khuyến nghị sử dụng màu chủ đạo tone Vàng Tươi (như #f59e0b, #fbbf24, #eab308).")

    # 3. Check High-Readability Font & Typography Standard
    if "Noto Sans SC" not in content:
        errors.append("Thiếu phông chữ hình học độ nét cao 'Noto Sans SC' (chống mờ nhòe nét ngang trên LCD)!")

    # 4. Check Global Font Scaler (A / A+ / A++)
    if "font-size-ctrl" not in content or "setFontScale" not in content:
        errors.append("Thiếu bộ điều khiển phóng to cỡ chữ toàn cục (.font-size-ctrl / setFontScale)!")

    # 5. Check Ultra Focus Vocab Modal
    if 'id="vocabModal"' not in content and "id='vocabModal'" not in content:
        errors.append("Thiếu Thẻ Phóng To Siêu Nét - Ultra Focus Modal (#vocabModal)!")

    # 6. Check MODULE 1: Vocabulary & Hanzi Stroke Animation (100% SGK Ground Truth)
    if 'id="tab-vocab"' not in content and "id='tab-vocab'" not in content:
        errors.append("Thiếu Tab 1 Từ Vựng (#tab-vocab)!")
    else:
        card_count = len(re.findall(r'class=["\']vocab-card["\']', content))
        m_les = re.search(r'BÀI\s*(\d{1,2})', content, re.IGNORECASE)
        if m_les:
            les_num = int(m_les.group(1))
            EXPECTED_COUNTS = {
                1: 15, 2: 18, 3: 17, 4: 16, 5: 13,
                6: 15, 7: 12, 8: 17, 9: 13, 10: 15,
                11: 19, 12: 14, 13: 15, 14: 17, 15: 21,
                16: 16, 17: 16, 18: 19, 19: 14, 20: 14
            }
            exp_count = EXPECTED_COUNTS.get(les_num)
            if exp_count is not None and card_count != exp_count:
                errors.append(f"Module 1 Từ Vựng: Số lượng thẻ từ vựng không khớp SGK gốc! Hiện có {card_count} thẻ, SGK Bài {les_num:02d} yêu cầu {exp_count} từ!")

    # 7. Check MODULE 2: 3 Subtabs, Flashcard 3D, Matching Game & Radical Lego Studio
    if 'id="tab-games"' not in content and "id='tab-games'" not in content:
        errors.append("Thiếu Tab 2 Luyện Tập & Minigames (#tab-games)!")
    else:
        if 'btnSubtabFC' not in content or 'btnSubtabMatch' not in content or 'btnSubtabAssembly' not in content:
            errors.append("Module 2: Thiếu cụm 3 nút chuyển Subtab (Flashcard 3D, Game Nối từ, Xưởng Ghép Chữ)!")
        if 'asmPlayArea' not in content or 'asmVictoryView' not in content:
            errors.append("Module 2 Ghép Chữ: Vi phạm kiến trúc Replay! Phải tách biệt #asmPlayArea và #asmVictoryView!")

    # 8. Check MODULE 3: 4 Dialogues & Audio files
    if 'id="tab-dialogues"' not in content and "id='tab-dialogues'" not in content:
        errors.append("Thiếu Tab 3 Bài Khóa (#tab-dialogues)!")
    else:
        dialogue_cards = len(re.findall(r'class=["\']dialogue-card["\']', content))
        if dialogue_cards < 4:
            errors.append(f"Module 3: Số lượng bài khóa chưa đủ (hiện có {dialogue_cards}/4 bài khóa)!")
        
        audio_srcs = re.findall(r'<audio[^>]*src="([^"]*audio_textbook[^"]*)"', content)
        file_dir = os.path.dirname(os.path.abspath(file_path))
        for src in audio_srcs:
            real_audio_path = os.path.normpath(os.path.join(file_dir, src))
            if not os.path.exists(real_audio_path):
                errors.append(f"Module 3 Audio: File âm thanh không tồn tại trên ổ đĩa: {src}")

    # 9. Check MODULE 4: Grammar Lab & Mini Quiz
    if 'id="tab-grammar"' not in content and "id='tab-grammar'" not in content:
        errors.append("Thiếu Tab 4 Ngữ Pháp (#tab-grammar)!")

    # ==================== AI MULTIMODAL ASSISTANT CHECKS (NEW IN 2.1) ====================
    # 10. Check gemini_config.js inclusion
    if "gemini_config.js" not in content:
        errors.append("AI Assistant: Thiếu nhúng file cấu hình gemini_config.js trong <head>!")

    # 11. Check AI Boxes across all 4 Dialogues
    for d_idx in range(1, 5):
        box_id = f'id="aiQaBox-{d_idx}"'
        if box_id not in content and f"id='aiQaBox-{d_idx}'" not in content:
            errors.append(f"AI Assistant: Thiếu khối Trợ lý AI Vision (#aiQaBox-{d_idx}) trong Bài Khóa {d_idx}!")

    # 12. Check ZERO DEMO BUTTONS Rule (User explicit requirement)
    if "btn-ai-demo" in content or "runAiDemoQuestion" in content or "Thử Câu Hỏi Mẫu" in content:
        errors.append("AI Assistant: Vi phạm quy tắc Zero Demo Buttons! Phát hiện nút hoặc hàm chạy câu hỏi mẫu giả lập (yêu cầu gỡ sạch 100%)!")

    # 13. Check AI Gemini Settings Modal
    if "geminiApiModal" not in content or "geminiApiKeyInput" not in content:
        errors.append("AI Assistant: Thiếu modal cài đặt Google Gemini API Key (#geminiApiModal / #geminiApiKeyInput)!")

    # 14. Check AI Multimodal Core Logic
    required_js_funcs = [
        "processSelectedImage",
        "analyzeQuestionWithAI",
        "analyzeManualTextWithAI",
        "renderAiResults",
        "openGeminiSettings"
    ]
    for func in required_js_funcs:
        if func not in content:
            errors.append(f"AI Assistant: Thiếu hàm xử lý cốt lõi '{func}' trong engine Javascript!")

    # 15. Check DIALOGUE_CONTEXTS Object
    if "const DIALOGUE_CONTEXTS" not in content and "let DIALOGUE_CONTEXTS" not in content:
        errors.append("AI Assistant: Thiếu đối tượng dữ liệu DIALOGUE_CONTEXTS chứa bài khóa gốc cho Gemini đối chiếu!")

    # 16. Check Pinyin Support in Results Rendering
    if "prompt_py" not in content or "quick_speech_py" not in content:
        errors.append("AI Assistant: Thiếu trường Pinyin phiên âm bắt buộc (prompt_py, quick_speech_py) cho kết quả nhận diện!")

    # 17. Check Single Topbar Rule
    topbar_count = len(re.findall(r'class=["\']topbar-nav["\']', content))
    if topbar_count != 1:
        errors.append(f"Topbar: Phát hiện {topbar_count} thanh topbar-nav (chỉ được có đúng 1 thanh điều hướng duy nhất)!")

    # Summary
    if errors:
        print(f"❌ PRE-STUDY AI VALIDATION FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"   - {e}")
        return False
    else:
        print("🎉 ALL PRE-STUDY AI CHECKS PASSED (100% COMPLIANT AI 2.1)!")
        if warnings:
            print(f"⚠️  {len(warnings)} warning(s):")
            for w in warnings:
                print(f"   - {w}")
        return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '2.1_Web_SoanBai_HSK3/Bai_03/index.html'
    success = validate_prestudy_ai_file(target)
    sys.exit(0 if success else 1)
