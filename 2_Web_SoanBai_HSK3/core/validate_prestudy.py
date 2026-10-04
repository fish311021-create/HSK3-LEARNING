# -*- coding: utf-8 -*-
"""
Validation Engine for HSK 3 Pre-Study Web Lessons
Ensures 100% compliance with pedagogical and interactive standards.
"""

import sys, os, re
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

    # 2. Check Bright / Yellow Theme Tokens
    if "#f59e0b" not in content and "#fbbf24" not in content and "#eab308" not in content:
        warnings.append("Khuyến nghị sử dụng màu chủ đạo tone Vàng Tươi (như #f59e0b, #fbbf24, #eab308) theo yêu cầu thiết kế tươi sáng.")

    # 3. Check MODULE 1: Vocabulary & Canvas
    if 'id="tab-vocab"' not in content and "id='tab-vocab'" not in content:
        errors.append("Thiếu Tab 1 Từ Vựng (#tab-vocab)!")
    else:
        canvas_count = len(re.findall(r'<canvas[^>]*class="[^"]*hanzi-canvas', content))
        if canvas_count < 10:
            errors.append(f"Module 1: Số lượng khung vẽ Canvas ô mễ chưa đủ (hiện có {canvas_count}, yêu cầu tối thiểu 10)!")

    # 4. Check MODULE 2: Flashcard 3D & 2-Column Matching Game
    if 'flashcard' not in content:
        errors.append("Module 2: Thiếu tính năng Flashcard 3D lật mặt!")
    if 'matching-game' not in content and 'game-matching' not in content:
        errors.append("Module 2: Thiếu Minigame Nối từ 2 cột (.matching-game)!")
    if 'btnToggleGamePinyin' not in content:
        errors.append("Module 2 Game: Thiếu nút bấm Bật/Tắt Pinyin (#btnToggleGamePinyin)!")

    # 5. Check MODULE 3: 4 Dialogues & AI Shadowing
    if 'id="tab-dialogues"' not in content and "id='tab-dialogues'" not in content:
        errors.append("Thiếu Tab 3 Bài Khóa (#tab-dialogues)!")
    else:
        audio_tags = len(re.findall(r'<audio[^>]*src="[^"]*audio_textbook', content))
        if audio_tags < 4:
            errors.append(f"Module 3: Thiếu file âm thanh thật cho 4 bài khóa (hiện chỉ phát hiện {audio_tags}/4 thẻ audio trỏ tới audio_textbook)!")
        if 'startShadowing' not in content and 'webkitSpeechRecognition' not in content and 'SpeechRecognition' not in content:
            errors.append("Module 3: Thiếu tính năng AI Shadowing / Luyện đọc nhận diện giọng nói (Microphone)!")

    # 6. Check MODULE 4: Grammar Lab & Mini Quiz
    if 'id="tab-grammar"' not in content and "id='tab-grammar'" not in content:
        errors.append("Thiếu Tab 4 Ngữ Pháp (#tab-grammar)!")
    if 'grammar-formula' not in content and 'formula-box' not in content:
        errors.append("Module 4: Thiếu khung hiển thị công thức ngữ pháp trực quan (.grammar-formula)!")
    if 'mini-quiz' not in content and 'grammar-quiz' not in content:
        errors.append("Module 4: Thiếu bài tập trắc nghiệm nhanh kiểm tra ngữ pháp!")

    # 7. Check Cross-Web Navigation (Topbar link to Exam Web)
    if '1_Web_LuyenThi_HSK3' not in content:
        errors.append("Thiếu đường link Topbar kết nối 1-click sang Web Luyện Thi (1_Web_LuyenThi_HSK3)!")
    if 'kiem_tra_tu_vung.html' not in content:
        errors.append("Thiếu đường link kết nối sang Đấu Trường Kiểm Tra Từ Vựng (kiem_tra_tu_vung.html)!")

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
