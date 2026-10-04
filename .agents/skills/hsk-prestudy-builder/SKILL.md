---
name: hsk-prestudy-builder
description: Tiêu chuẩn xây dựng ứng dụng web Soạn & Ôn Trước Bài Học tiếng Trung HSK 3 (Pre-Study Studio). Sử dụng khi tạo mới hoặc cập nhật các bài soạn trước (từ vựng, Flashcard 3D, game nối từ 2 cột, canvas ô mễ viết Hán tự, mổ xẻ bài khóa AI Shadowing, xưởng ngữ pháp, kiểm tra từ vựng tích lũy).
---

# HSK 3 PRE-STUDY BUILDER SPECIFICATION

Kỹ năng này định nghĩa toàn bộ quy chuẩn sư phạm, cấu trúc giao diện tươi sáng (Tone Vàng Tươi - Sunshine Gold), logic tương tác và engine tự động hóa cho **Phân hệ Web Soạn Bài Trước HSK 3** nằm hoàn toàn trong thư mục `2_Web_SoanBai_HSK3/`.

---

## 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM

1. **Tuyệt đối không can thiệp vào `1_Web_LuyenThi_HSK3/`**: Mọi file, mã nguồn, cấu trúc của Web Luyện Thi phải được giữ nguyên 100%.
2. **Toàn bộ tài nguyên của Web Soạn Bài nằm trọn trong `2_Web_SoanBai_HSK3/`**:
   - `core/`: Template master, builder engine, validator.
   - `data/`: Kho từ vựng `vocab_master.js`, dữ liệu bài học `extracted_soan_bai_XX.py`.
   - `audio_textbook/`: File âm thanh MP3 bài khóa chuẩn từ Sách giáo khoa.
   - `Bai_XX/`: Từng bài soạn học cụ thể (`Bai_03/index.html`, v.v.).
   - `kiem_tra_tu_vung.html`: Đấu trường kiểm tra từ vựng tích lũy random.
   - `index.html`: Cổng danh mục 20 bài soạn bài.

---

## 2. QUY CHUẨN DESIGN SYSTEM: TONE VÀNG TƯƠI SÁNG (SUNSHINE GOLD)

- **Tone chủ đạo**: Vàng tươi (`#f59e0b`, `#fbbf24`, `#eab308`, `#fef08a`), tạo cảm giác hứng khởi, giàu năng lượng học tập.
- **Màu nền**: Ambient ấm áp rực rỡ `radial-gradient(circle at 50% 0%, #fffbeb 0%, #fef3c7 25%, #f8fafc 80%)`.
- **Màu chữ**: Deep Charcoal `#0f172a` và Slate `#334155` cho độ tương phản sắc nét, chống mỏi mắt.
- **Thẻ Card**: Glassmorphism sáng trong trẻo `background: rgba(255, 255, 255, 0.88); backdrop-filter: blur(16px); border: 1px solid rgba(245, 158, 11, 0.25); box-shadow: 0 10px 30px rgba(217, 119, 6, 0.08)`.
- **Phông chữ**:
  - Tiêu đề & Giao diện: `Plus Jakarta Sans`, sans-serif.
  - Chữ Hán: `Noto Serif SC`, `Songti SC`, serif.

---

## 3. CẤU TRÚC 5 MODULE TRỌNG TÂM MỖI BÀI HỌC

### Module 1: Từ Vựng & Canvas Vẽ Chữ Hán Ô Mễ (米字格)
- Hiển thị đầy đủ danh sách từ mới SGK (Bài 3: 17 từ).
- Mỗi từ bao gồm: Chữ Hán, Pinyin, Âm Hán Việt, Từ loại, Giải nghĩa, Chiết tự bộ thủ.
- 2 câu ví dụ: 1 câu giao tiếp đời sống + 1 câu trích đề thi HSK.
- **Interactive Canvas Ô Mễ**: Tích hợp thẻ `<canvas>` dạng ô mễ (Mǐzìgé) cho phép người học trực tiếp rê chuột hoặc chạm ngón tay tập viết từng nét Hán tự, kèm nút `Xóa nét` và `Phát âm`.

### Module 2: Flashcard 3D & Minigame Nối Từ 2 Cột
- **Tab 1: Flashcard 3D**: Thẻ xoay 180 độ; mặt trước Chữ Hán to + Audio; mặt sau Pinyin + Hán Việt + Dịch + Ví dụ. Có nút "Đã thuộc" / "Cần ôn lại".
- **Tab 2: Game Nối Từ 2 Cột**: Toàn bộ từ mới xuất hiện trên 2 cột; cột trái Chữ Hán (mặc định ẩn Pinyin, có nút toggle Bật/Tắt Pinyin); cột phải Tiếng Việt xáo trộn. Đúng đổi xanh `#10b981` + âm "Ting", sai rung lắc đỏ `#ef4444`. Có timer và đếm bước.

### Module 3: Mổ Xẻ 4 Bài Khóa SGK & AI Shadowing
- Audio chuẩn bài khóa SGK trích từ Google Drive (`03-1.mp3` đến `03-4.mp3`).
- Phân tích 3 lớp: Bối cảnh -> Bóc tách từng câu -> Câu hỏi đọc hiểu.
- **AI Shadowing / Repeat câu**: Bấm microphone thu âm giọng đọc -> Trình duyệt nhận diện bằng Web Speech Recognition API -> Chấm điểm % độ chính xác phát âm so với câu mẫu.

### Module 4: Xưởng Ngữ Pháp (Grammar Lab)
- Công thức đóng khung nổi bật, giải thích bản chất tư duy tiếng Trung.
- Bảng phân tích "Bẫy đề thi và lỗi người Việt hay mắc".
- Mini Quiz 5 câu trắc nghiệm làm bài nộp điểm tức thì kèm giải thích.

### Module 5: Đấu Trường Kiểm Tra Từ Vựng Tích Lũy (`kiem_tra_tu_vung.html`)
- Bộ lọc Checkbox chọn các bài đã học (Bài 1..20).
- Random ngẫu nhiên câu hỏi.
- 4 chế độ: 🇻🇳 -> 🇨🇳, 🇨🇳 -> 🇻🇳, 🔤 -> 🇻🇳, và 🎲 Hỗn hợp.
- Bảng xếp loại kết quả & Sổ tay luyện lại các từ sai.

---

## 4. QUY TRÌNH BIÊN DỊCH & KIỂM ĐỊNH CHẤT LƯỢNG

1. Mọi bài học mới phải được tạo dữ liệu trong `2_Web_SoanBai_HSK3/data/extracted_soan_bai_XX.py`.
2. Chạy `python 2_Web_SoanBai_HSK3/core/build_prestudy_engine.py XX` để sinh file `Bai_XX/index.html`.
3. Kiểm tra tự động bằng `python 2_Web_SoanBai_HSK3/core/validate_prestudy.py Bai_XX/index.html`.
4. Chỉ hoàn tất khi đạt tiêu chuẩn **100% COMPLIANT**.
