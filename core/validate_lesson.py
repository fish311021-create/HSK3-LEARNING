import sys, os, re, json

sys.stdout.reconfigure(encoding='utf-8')

def get_card_chunk(content, q):
    """Safely extract the HTML content belonging to a single question card."""
    patterns = [
        f'id="card-{q}"',
        f'id="q-{q}"',
        f'class="card-num">Câu {q}<',
        f'class="card-num">第 {q} 题<',
        f'<!-- Câu {q} -->'
    ]
    start_idx = -1
    matched_pat = None
    for p in patterns:
        idx = content.find(p)
        if idx != -1:
            start_idx = idx
            matched_pat = p
            break
    if start_idx == -1:
        return None

    # Find the next card boundary
    next_patterns = [
        f'id="card-{q+1}"',
        f'id="q-{q+1}"',
        f'class="card-num">Câu {q+1}<',
        f'class="card-num">第 {q+1} 题<',
        f'<!-- Câu {q+1} -->',
        '</section>',
        '<!-- PHẦN',
        '<!-- ===================='
    ]
    end_idx = len(content)
    for np in next_patterns:
        n_idx = content.find(np, start_idx + len(matched_pat))
        if n_idx != -1 and n_idx < end_idx:
            end_idx = n_idx
            
    return content[start_idx:end_idx]

def validate_lesson_file(file_path):
    print(f"\n==========================================")
    print(f"VALIDATING LESSON: {file_path}")
    print(f"==========================================")
    
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File does not exist: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    warnings = []

    # ----------------------------------------------------
    # 0. Global Design System Integrity Check
    # ----------------------------------------------------
    forbidden_classes = ['ref-table', 'ref-row', 'vocab-bank', 'vocab-chip']
    for fc in forbidden_classes:
        if re.search(rf'class=["\'][^"\']*\b{fc}\b', content):
            errors.append(f"Phát hiện class tự chế không thuộc Design System chuẩn: '{fc}' (Vui lòng dùng class chuẩn trong core/template_master.html)")

    # ----------------------------------------------------
    # 1. Check all 4 Main Tabs
    # ----------------------------------------------------
    tabs = ['tab-listening', 'tab-reading', 'tab-writing', 'tab-textbook']
    for t in tabs:
        if f'id="{t}"' not in content:
            errors.append(f"Thiếu tab chính: id='{t}'")

    # ----------------------------------------------------
    # 2. Check TAB 1: LISTENING (1 - 20)
    # ----------------------------------------------------
    # Check checkQuiz button syntax (Must be zero-string clean onclick="checkQuiz(i)")
    bad_check_calls = re.findall(r'onclick="checkQuiz\((\d+)\s*,\s*[^)]+\)"', content)
    if bad_check_calls:
        errors.append(f"Tab 1: Phát hiện {len(bad_check_calls)} nút checkQuiz truyền chuỗi trực tiếp (ví dụ câu {bad_check_calls[0]}). BẮT BUỘC dùng onclick=\"checkQuiz({{NUM}})\" sạch không tham số chuỗi, toàn bộ đáp án và lời giải phải lưu trong QUIZ_DATA!")

    # Phần 1 (1-5): Phải có pics-grid và đủ 6 ảnh A-F
    if 'pics-grid' not in content and 'pic-item' not in content:
        errors.append("Tab 1 Phần 1: Thiếu khung hiển thị hình ảnh minh họa (.pics-grid)")
    else:
        for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
            if f'pic_{letter}.png' not in content and f'Hình {letter}' not in content:
                warnings.append(f"Tab 1 Phần 1: Khuyến nghị có ảnh minh họa pic_{letter}.png")

    for q in range(1, 6):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 1: Thiếu câu nghe {q} (cần card-num hoặc id='card-{q}')")
        else:
            if 'interactive-text' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu chữ Hán tra từ điển (.interactive-text)")
            if 'pinyin-line' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu dòng phiên âm Pinyin (.pinyin-line)")
            if 'trans-line' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu dòng dịch nghĩa tiếng Việt (.trans-line)")
            # 6 options A-F
            for opt in ['A', 'B', 'C', 'D', 'E', 'F']:
                if f"'{opt}'" not in chunk and f'"{opt}"' not in chunk:
                    errors.append(f"Tab 1 Câu {q}: Thiếu lựa chọn hình ảnh {opt}")
            if 'quiz-actions' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu cụm nút thao tác (.quiz-actions)")

    # Phần 2 (6-10): Phán đoán Đúng/Sai (★ và nút √ / ×)
    for q in range(6, 11):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 1: Thiếu câu nghe {q} (cần card-num hoặc id='card-{q}')")
        else:
            if '★' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu câu nhận định phán đoán (bắt buộc kèm ký hiệu ★)")
            if '√' not in chunk or ('×' not in chunk and 'X' not in chunk):
                errors.append(f"Tab 1 Câu {q}: Thiếu 2 lựa chọn Đúng (√) và Sai (×)")
            if "'true'" in chunk or '"true"' in chunk or "'false'" in chunk or '"false"' in chunk:
                errors.append(f"Tab 1 Câu {q}: Nút chọn Đúng/Sai đang truyền 'true'/'false'! BẮT BUỘC dùng selectOption({q}, '√') và selectOption({q}, '×')")
            if 'grid-true-false' not in chunk and 'repeat(2, 1fr)' not in chunk:
                warnings.append(f"Tab 1 Câu {q}: Khuyến nghị dùng class .options-grid.grid-true-false để cố định độ rộng 320px 2 cột")
            if 'quiz-actions' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu cụm nút thao tác (.quiz-actions)")

    # Phần 3 (11-15) & Phần 4 (16-20): Có câu hỏi 问 và 3 lựa chọn A, B, C
    for q in range(11, 21):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 1: Thiếu câu nghe {q} (cần card-num hoặc id='card-{q}')")
        else:
            if '问:' not in chunk and '问：' not in chunk:
                warnings.append(f"Tab 1 Câu {q}: Khuyến nghị có dòng câu hỏi người dẫn (问:)")
            # Check 3 options A, B, C
            for opt in ['A', 'B', 'C']:
                if f"'{opt}'" not in chunk and f'"{opt}"' not in chunk and f'>{opt}<' not in chunk:
                    errors.append(f"Tab 1 Câu {q}: Thiếu lựa chọn {opt}")
            if 'quiz-actions' not in chunk:
                errors.append(f"Tab 1 Câu {q}: Thiếu cụm nút thao tác (.quiz-actions)")

    # ----------------------------------------------------
    # 3. Check TAB 2: READING (21 - 35)
    # ----------------------------------------------------
    # Phần 1 (21-25): Khung tham khảo A-F
    if 'reading-ref-box' not in content and 'CÁC CÂU LỰA CHỌN' not in content:
        errors.append("Tab 2 Phần 1: Thiếu khung tham khảo Danh sách câu lựa chọn A - F (.reading-ref-box)")

    for q in range(21, 26):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 2: Thiếu câu đọc {q} (cần id='q-{q}')")
        else:
            if re.search(r'\[[A-F]\]', chunk):
                errors.append(f"Tab 2 Câu {q}: Phát hiện ký tự thừa '[A]'/'[B]'... lặp lại trong chip! Format chuẩn duy nhất là '<span class=\"chip-letter\">A</span> A'")
            chips = re.findall(r'<div class="option-chip"[^>]*>(.*?)</div>', chunk, re.DOTALL)
            for ch in chips:
                clean_ch = re.sub(r'<[^>]+>', '', ch).strip()
                if len(clean_ch) > 12:
                    errors.append(f"Tab 2 Câu {q}: Chip lựa chọn chứa cả câu văn quá dài ('{clean_ch[:20]}...'). Lựa chọn câu 21-25 BẮT BUỘC phải là chip chữ cái compact dạng '<span class=\"chip-letter\">A</span> A'!")
                    break
            if 'sentence-footer' not in chunk and 'sentence-trans-box' not in chunk:
                errors.append(f"Tab 2 Câu {q}: Thiếu hộp dịch câu (.sentence-footer / .sentence-trans-box)")

    # Phần 2 (26-30): Ngân hàng từ vựng A-F & Chỗ trống điền từ
    if 'reading-vocab-box' not in content and 'NGÂN HÀNG TỪ VỰNG' not in content:
        errors.append("Tab 2 Phần 2: Thiếu khung Ngân hàng từ vựng A - F (.reading-vocab-box)")
    else:
        v_card_count = content.count('class="reading-vocab-card"')
        if v_card_count < 5:
            errors.append(f"Tab 2 Phần 2: Thiếu thẻ từ vựng trong ngân hàng từ (hiện chỉ có {v_card_count}/6 thẻ .reading-vocab-card)!")

    for q in range(26, 31):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 2: Thiếu câu đọc {q} (cần id='q-{q}')")
        else:
            if f'blank-display-{q}' not in chunk and '( ? )' not in chunk:
                warnings.append(f"Tab 2 Câu {q}: Khuyến nghị có ô hiển thị chỗ trống điền từ blank-display-{q}")
            if 'grid-vocab' not in chunk and 'max-width: 550px' not in chunk:
                warnings.append(f"Tab 2 Câu {q}: Khuyến nghị dùng class .options-grid.grid-vocab để cố định độ rộng 550px")

            # Check that sentence is not just blank-display
            it_match = re.search(r'<div class="interactive-text">(.*?)</div>', chunk, re.DOTALL)
            if it_match:
                it_clean = re.sub(r'<[^>]+>', '', it_match.group(1)).replace('( ? )', '').strip()
                if not re.search(r'[\u4e00-\u9fa5]', it_clean):
                    errors.append(f"Tab 2 Câu {q}: Nội dung câu hỏi chữ Hán bị rỗng (chỉ có ô trống điền từ)! Cần có câu văn hoàn chỉnh.")

            # Check that option chips have actual words
            chips = re.findall(r'<div class="option-chip"[^>]*>(.*?)</div>', chunk, re.DOTALL)
            if chips:
                for ch in chips:
                    ch_clean = re.sub(r'<[^>]+>', '', ch).strip()
                    # Expect chip letter followed by Chinese word, e.g. "A 图书馆"
                    if len(ch_clean) <= 1:
                        errors.append(f"Tab 2 Câu {q}: Lựa chọn từ vựng bị thiếu chữ Hán ('{ch.strip()}'), chỉ hiển thị chữ cái A-F mà không có từ!")
                        break

    # Phần 3 (31-35): Đọc hiểu đoạn văn & Pinyin lựa chọn A, B, C
    for q in range(31, 36):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 2: Thiếu câu đọc {q} (cần id='q-{q}')")
        else:
            if 'reading-passage-box' not in chunk:
                warnings.append(f"Tab 2 Câu {q}: Khuyến nghị bọc đoạn văn trong class .reading-passage-box")

            if '<div class="sentence-footer">' not in chunk:
                errors.append(f"Tab 2 Câu {q}: Thiếu thẻ <div class=\"sentence-footer\"> phía trên quiz-actions")

            if '<div class="sentence-trans-box">' not in chunk:
                errors.append(f"Tab 2 Câu {q}: Thiếu hộp dịch <div class=\"sentence-trans-box\">")

            # Must have bullet points for A, B, C with pinyin
            pattern_a = r'&bull;\s*<strong>A\.[^<]+</strong>\s*\([^\)]+\):'
            pattern_b = r'&bull;\s*<strong>B\.[^<]+</strong>\s*\([^\)]+\):'
            pattern_c = r'&bull;\s*<strong>C\.[^<]+</strong>\s*\([^\)]+\):'

            if not re.search(pattern_a, chunk):
                errors.append(f"Tab 2 Câu {q}: Lựa chọn A thiếu Chữ Hán hoặc Phiên âm Pinyin trong ngoặc đơn!")
            if not re.search(pattern_b, chunk):
                errors.append(f"Tab 2 Câu {q}: Lựa chọn B thiếu Chữ Hán hoặc Phiên âm Pinyin trong ngoặc đơn!")
            if not re.search(pattern_c, chunk):
                errors.append(f"Tab 2 Câu {q}: Lựa chọn C thiếu Chữ Hán hoặc Phiên âm Pinyin trong ngoặc đơn!")

    # ----------------------------------------------------
    # 4. Check TAB 3: WRITING (36 - 45)
    # ----------------------------------------------------
    # Phần 1 (36-40): Sắp xếp từ (phải có dấu /)
    for q in range(36, 41):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 3: Thiếu câu viết {q} (cần card-num hoặc id='q-{q}')")
        else:
            if '/' not in chunk:
                errors.append(f"Tab 3 Câu {q}: Thiếu chuỗi cụm từ phân cách bằng dấu gạch chéo '/' để sắp xếp câu!")
            if 'sentence-trans-box' not in chunk:
                errors.append(f"Tab 3 Câu {q}: Thiếu hộp hiển thị đáp án đúng (.sentence-trans-box)")

    # Phần 2 (41-45): Điền chữ Hán (phải có pinyin trong ngoặc)
    for q in range(41, 46):
        chunk = get_card_chunk(content, q)
        if not chunk:
            errors.append(f"Tab 3: Thiếu câu viết {q} (cần card-num hoặc id='q-{q}')")
        else:
            if '（' not in chunk and '(' not in chunk:
                errors.append(f"Tab 3 Câu {q}: Thiếu phiên âm pinyin trong ngoặc đơn để điền chữ Hán!")
            if 'sentence-trans-box' not in chunk:
                errors.append(f"Tab 3 Câu {q}: Thiếu hộp hiển thị chữ Hán cần điền (.sentence-trans-box)")

    # ----------------------------------------------------
    # 5. Check TAB 4: SÁCH GIÁO KHOA
    # ----------------------------------------------------
    t4_idx = content.find('id="tab-textbook"')
    if t4_idx != -1:
        tab4_text = content[t4_idx:content.rfind('<script>')]
        if 'global-toolbar' in tab4_text:
            errors.append("Tab 4: Phát hiện thanh .global-toolbar thừa trong Tab 4 (thanh công cụ chỉ thuộc về Tab 1, 2, 3)!")
        if 'bài khóa' in tab4_text.lower():
            errors.append("Tab 4 vẫn còn chứa nội dung hoặc tiêu đề 'Bài khóa'!")
        if 'vocab-table' not in tab4_text:
            errors.append("Tab 4: Thiếu bảng từ vựng mới chuẩn (.vocab-table)")
        if 'grammar-card' not in tab4_text and 'grammar-point-box' not in tab4_text:
            errors.append("Tab 4: Thiếu thẻ ngữ pháp chuẩn (.grammar-card hoặc .grammar-point-box)! BẮT BUỘC dùng .grammar-card, .grammar-title, .grammar-formula, .example-item")
        if 'grammar-formula' not in tab4_text:
            errors.append("Tab 4: Thiếu khung công thức ngữ pháp (.grammar-formula)!")
        if 'example-item' not in tab4_text and 'grammar-example-item' not in tab4_text:
            errors.append("Tab 4: Thiếu các câu ví dụ mẫu (.example-item hoặc .grammar-example-item)!")

        forbidden_tab4_vars = ['--bg-main', '--border-color', '--text-muted', 'grammar-box', 'pos-tag']
        for fb in forbidden_tab4_vars:
            if fb in tab4_text:
                errors.append(f"Tab 4: Phát hiện biến CSS hoặc class tự chế không hợp lệ '{fb}'! Vui lòng dùng Design System chuẩn trong core/template_master.html")

    # ----------------------------------------------------
    # 6. Check Scripts DICT & QUIZ_DATA
    # ----------------------------------------------------
    if 'const DICT =' not in content:
        errors.append("Thiếu khai báo const DICT trong script!")
    if 'const QUIZ_DATA =' not in content:
        errors.append("Thiếu khai báo const QUIZ_DATA trong script!")
    else:
        for q in range(1, 36):
            if f'"{q}":' not in content and f"'{q}':" not in content and f' {q}:' not in content:
                errors.append(f"QUIZ_DATA: Thiếu cấu hình đáp án và giải thích cho câu {q} (bắt buộc đầy đủ 35 câu từ 1 đến 35)!")

    # ----------------------------------------------------
    # 7. Check DICTIONARY TOOLTIP Structure (Chống vỡ giao diện tooltip tra từ)
    # ----------------------------------------------------
    if 'id="dict-tooltip"' not in content and "id='dict-tooltip'" not in content:
        errors.append("Thiếu thẻ khung hiển thị từ điển (#dict-tooltip)!")
    else:
        if 'tooltip-word' not in content:
            errors.append("Cấu trúc #dict-tooltip bị lỗi: Thiếu thẻ bọc <div class=\"tooltip-word\">!")
        if 'tooltip-pinyin' not in content:
            errors.append("Cấu trúc #dict-tooltip bị lỗi: Thiếu class .tooltip-pinyin cho #tt-pinyin!")
        if 'tooltip-hv' not in content:
            errors.append("Cấu trúc #dict-tooltip bị lỗi: Thiếu class .tooltip-hv cho #tt-hv!")
        if 'tooltip-meaning' not in content:
            errors.append("Cấu trúc #dict-tooltip bị lỗi: Thiếu class .tooltip-meaning cho #tt-meaning!")
        if 'poly-badge' not in content or 'poly-detail-box' not in content:
            errors.append("Cấu trúc #dict-tooltip bị lỗi: Thiếu class .poly-badge hoặc .poly-detail-box cho phần chữ đa âm tự!")

    # ----------------------------------------------------
    # Summary
    # ----------------------------------------------------
    if errors:
        print(f"❌ VALIDATION FAILED with {len(errors)} error(s):")
        for e in errors:
            print(f"   - {e}")
        return False
    else:
        print("✅ ALL CRITICAL FORMAT CHECKS PASSED (100% COMPLIANT)!")
        if warnings:
            print(f"⚠️  {len(warnings)} warning(s):")
            for w in warnings:
                print(f"   - {w}")
        return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'Bai_02/index.html'
    success = validate_lesson_file(target)
    sys.exit(0 if success else 1)
