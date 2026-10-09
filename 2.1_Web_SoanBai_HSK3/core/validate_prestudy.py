# -*- coding: utf-8 -*-
"""
Validation Engine for HSK 3 Pre-Study Web Lessons
Ensures 100% compliance with pedagogical, interactive, and UX standards.
Incorporates all lessons learned and anti-pattern prevention from Web Luyện Thi.
"""

import sys, os, re

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def validate_prestudy_file(file_path):
    print(f"\n==========================================")
    print(f"VALIDATING PRE-STUDY LESSON: {file_path}")
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
        warnings.append("Khuyến nghị sử dụng màu chủ đạo tone Vàng Tươi (như #f59e0b, #fbbf24, #eab308) theo yêu cầu thiết kế tươi sáng.")

    # 3. Check High-Readability Font & Typography Standard
    if "Noto Sans SC" not in content:
        errors.append("Thiếu phông chữ hình học độ nét cao 'Noto Sans SC' (chống mờ nhòe nét ngang trên màn hình LCD)!")
    if "--zh-title-size" not in content or "--zh-example-size" not in content:
        warnings.append("Khuyến nghị khai báo biến CSS typography chuyên biệt cho chữ Hán (--zh-title-size, --zh-example-size).")
    
    # 4. Check Global Font Scaler (A / A+ / A++)
    if "font-size-ctrl" not in content or "setFontScale" not in content:
        errors.append("Thiếu bộ điều khiển phóng to cỡ chữ toàn cục (.font-size-ctrl / setFontScale)!")
    if "font-scale-large" not in content or "font-scale-xlarge" not in content:
        errors.append("Thiếu các class CSS tỷ lệ cỡ chữ (font-scale-large, font-scale-xlarge)!")

    # 5. Check Ultra Focus Vocab Modal
    if 'id="vocabModal"' not in content and "id='vocabModal'" not in content:
        errors.append("Thiếu Thẻ Phóng To Siêu Nét - Ultra Focus Modal (#vocabModal)!")
    if "openVocabModal" not in content or "closeVocabModal" not in content:
        errors.append("Thiếu hàm điều khiển Ultra Focus Modal (openVocabModal / closeVocabModal)!")
    if "ArrowRight" not in content or "Escape" not in content:
        warnings.append("Khuyến nghị hỗ trợ đầy đủ phím tắt bàn phím (ArrowRight, ArrowLeft, Escape, Space) cho Ultra Focus Modal.")

    # 6. Check MODULE 1: Vocabulary & Hanzi Stroke Animation (100% SGK Ground Truth)
    if 'id="tab-vocab"' not in content and "id='tab-vocab'" not in content:
        errors.append("Thiếu Tab 1 Từ Vựng (#tab-vocab)!")
    else:
        # Check vocab cards count against textbook standard
        card_count = len(re.findall(r'class=["\']vocab-card["\']', content))
        m_les = re.search(r'BÀI\s*(\d{1,2})', content, re.IGNORECASE)
        if m_les:
            les_num = int(m_les.group(1))
            EXPECTED_COUNTS = {
                1: 15, 2: 18, 3: 17, 4: 16, 5: 13,
                6: 15, 7: 12, 8: 17, 9: 13, 10: 15,
                11: 19, 12: 14, 13: 15, 14: 17, 15: 21
            }
            exp_count = EXPECTED_COUNTS.get(les_num)
            if exp_count is not None and card_count != exp_count:
                errors.append(f"Module 1 Từ Vựng: Số lượng thẻ từ vựng không khớp SGK gốc! Hiện có {card_count} thẻ, SGK chuẩn Bài {les_num:02d} yêu cầu đúng {exp_count} từ!")

        stroke_count = len(re.findall(r'stroke-anim|playStrokeAnim|hanzi-writer', content))
        if stroke_count < 10:
            errors.append(f"Module 1: Số lượng khung chạy cách viết Hán tự chưa đủ (hiện có {stroke_count}, yêu cầu tối thiểu 10)!")

    # 7. Check MODULE 2: 3 Subtabs, Flashcard 3D, Matching Game & Radical Lego Studio
    if 'id="tab-games"' not in content and "id='tab-games'" not in content:
        errors.append("Thiếu Tab 2 Luyện Tập & Minigames (#tab-games)!")
    else:
        # Check subtabs
        if 'btnSubtabFC' not in content or 'btnSubtabMatch' not in content or 'btnSubtabAssembly' not in content:
            errors.append("Module 2: Thiếu cụm 3 nút chuyển Subtab (Flashcard 3D, Game Nối từ, Xưởng Ghép Chữ)!")
        
        # Subtab 1: Flashcard 3D
        if 'flashcard' not in content or 'flipFlashcard' not in content:
            errors.append("Module 2: Thiếu tính năng Flashcard 3D lật thẻ (.flashcard / flipFlashcard)!")
        
        # Subtab 2: 2-Column Matching Game
        if 'matching-game' not in content and 'matching-game-board' not in content and 'game-matching' not in content:
            errors.append("Module 2: Thiếu Minigame Nối từ 2 cột (.matching-game-board)!")
        if 'btnToggleGamePinyin' not in content:
            errors.append("Module 2 Game: Thiếu nút bấm Bật/Tắt Pinyin (#btnToggleGamePinyin)!")
        
        # Subtab 3: Xưởng Ghép Chữ Hán (Radical Lego Studio)
        if 'id="subtab-assembly"' not in content and "id='subtab-assembly'" not in content:
            errors.append("Module 2: Thiếu Subtab 3 Xưởng Ghép Chữ Hán (#subtab-assembly)!")
        if 'asmSlotsContainer' not in content or 'asmPoolGrid' not in content:
            errors.append("Module 2 Ghép Chữ: Thiếu bàn ghép linh kiện (#asmSlotsContainer) hoặc kho linh kiện (#asmPoolGrid)!")
        if 'btnCheckAssembly' not in content or 'checkAssembly' not in content:
            errors.append("Module 2 Ghép Chữ: Thiếu nút kiểm tra ghép chữ (btnCheckAssembly / checkAssembly)!")
        
        # Check Replay Bug Anti-Pattern: asmPlayArea vs asmVictoryView separation
        if 'asmPlayArea' not in content or 'asmVictoryView' not in content:
            errors.append("Module 2 Ghép Chữ: Vi phạm kiến trúc Replay! Phải tách biệt #asmPlayArea và #asmVictoryView để tránh lỗi ghi đè DOM làm hỏng bàn ghép khi chơi lại!")
        
        # Check Anti-Rote Random Shuffle (Fisher-Yates)
        if 'shuffleArray' not in content and 'Math.random' not in content:
            errors.append("Module 2 Ghép Chữ: Thiếu thuật toán xáo trộn câu hỏi và linh kiện (chống học vẹt vị trí)!")

    # 8. Check MODULE 3: 4 Dialogues & AI Shadowing (100% SGK Ground Truth)
    if 'id="tab-dialogues"' not in content and "id='tab-dialogues'" not in content:
        errors.append("Thiếu Tab 3 Bài Khóa (#tab-dialogues)!")
    else:
        # Check audio tags
        audio_srcs = re.findall(r'<audio[^>]*src="([^"]*audio_textbook[^"]*)"', content)
        if len(audio_srcs) < 4:
            errors.append(f"Module 3: Thiếu file âm thanh thật cho 4 bài khóa (hiện chỉ phát hiện {len(audio_srcs)}/4 thẻ audio trỏ tới audio_textbook)!")
        
        # Verify physical audio files exist on disk
        file_dir = os.path.dirname(os.path.abspath(file_path))
        for src in audio_srcs:
            # Resolve relative src
            real_audio_path = os.path.normpath(os.path.join(file_dir, src))
            if not os.path.exists(real_audio_path):
                errors.append(f"Module 3 Audio: File âm thanh không tồn tại trên ổ đĩa: {src} -> {real_audio_path}")
            elif os.path.getsize(real_audio_path) < 5000:
                errors.append(f"Module 3 Audio: File âm thanh có dung lượng quá nhỏ hoặc rỗng ({os.path.getsize(real_audio_path)} bytes): {src}")

        # Check dialogue lines & speakers
        dialogue_cards = len(re.findall(r'class=["\']dialogue-card["\']', content))
        if dialogue_cards < 4:
            errors.append(f"Module 3: Số lượng bài khóa chưa đủ (hiện có {dialogue_cards}/4 bài khóa)!")
        
        d_lines = len(re.findall(r'class=["\']d-line["\']', content))
        if d_lines < 15:
            errors.append(f"Module 3: Tổng số câu thoại trong 4 bài khóa quá ít ({d_lines} câu, chuẩn SGK HSK 3 cần tối thiểu 16-24 câu)!")

        if 'startShadowing' not in content and 'webkitSpeechRecognition' not in content and 'SpeechRecognition' not in content:
            errors.append("Module 3: Thiếu tính năng AI Shadowing / Luyện đọc nhận diện giọng nói (Microphone)!")
        if 'selectDialogueCheck' not in content or 'checkDialogueQuiz' not in content:
            warnings.append("Khuyến nghị có câu hỏi trắc nghiệm kiểm tra hiểu bài cuối mỗi bài khóa.")

    # 9. Check MODULE 4: Grammar Lab & Mini Quiz
    if 'id="tab-grammar"' not in content and "id='tab-grammar'" not in content:
        errors.append("Thiếu Tab 4 Ngữ Pháp (#tab-grammar)!")
    if 'grammar-formula' not in content and 'formula-box' not in content:
        errors.append("Module 4: Thiếu khung hiển thị công thức ngữ pháp trực quan (.grammar-formula)!")
    if 'mini-quiz' not in content and 'grammar-quiz' not in content:
        errors.append("Module 4: Thiếu bài tập trắc nghiệm nhanh kiểm tra ngữ pháp!")

    # 10. Check Navigation & Anti-Pattern: Single Topbar Rule
    topbar_count = len(re.findall(r'class=["\']topbar-nav["\']', content))
    if topbar_count == 0:
        errors.append("Thiếu thanh điều hướng Topbar (.topbar-nav)!")
    elif topbar_count > 1:
        errors.append(f"Vi phạm quy tắc Anti-Pattern: Phát hiện {topbar_count} thanh topbar-nav (chỉ được có đúng 1 thanh điều hướng duy nhất)!")

    if '1_Web_LuyenThi_HSK3' not in content:
        errors.append("Thiếu đường link Topbar kết nối 1-click sang Web Luyện Thi (1_Web_LuyenThi_HSK3)!")
    if 'kiem_tra_tu_vung.html' not in content:
        errors.append("Thiếu đường link kết nối sang Đấu Trường Kiểm Tra Từ Vựng (kiem_tra_tu_vung.html)!")
    if 'prev-btn' not in content or 'next-btn' not in content:
        errors.append("Thiếu cụm nút bấm chuyển nhanh bài học (prev-btn / next-btn) trên Topbar!")

    # Summary
    if errors:
        print(f"❌ PRE-STUDY VALIDATION FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"   - {e}")
        return False
    else:
        print("🎉 ALL PRE-STUDY CHECKS PASSED (100% COMPLIANT)!")
        if warnings:
            print(f"⚠️  {len(warnings)} warning(s):")
            for w in warnings:
                print(f"   - {w}")
        return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '2_Web_SoanBai_HSK3/Bai_03/index.html'
    success = validate_prestudy_file(target)
    sys.exit(0 if success else 1)
