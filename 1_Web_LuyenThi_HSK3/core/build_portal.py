# -*- coding: utf-8 -*-
"""
Build Universal Navigation & Portal Landing Page for 1_Web_LuyenThi_HSK3
Ensures 100% compliance with user requirements:
1. Header bar keeps ONLY the dropdown select menu.
2. The other 2 menu positions (floating hamburger button and sidebar drawer) are completely removed/hidden.
3. Top-left corner has the button back to Cổng Tổng (../index.html or ../../index.html).
4. 1_Web_LuyenThi_HSK3/index.html serves as the Cổng 1 Landing Page with section descriptions and lesson catalog (Lessons 1-20).
"""

import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

CORE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB1_DIR = os.path.dirname(CORE_DIR)

LESSON_TITLES = [
    (1, "周末你有什么打算？", "Zhōumò nǐ yǒu shénme dǎsuàn?", "Cuối tuần bạn có dự định gì?"),
    (2, "他什么时候回来？", "Tā shénme shíhou huílái?", "Khi nào anh ấy về?"),
    (3, "桌子上放着很多饮料", "Zhuōzi shang fàngzhe hěnduō yǐnliào", "Trên bàn để rất nhiều đồ uống"),
    (4, "她总是笑着跟客人说话", "Tā zǒngshì xiàozhe gēn kèrén shuōhuà", "Cô ấy luôn cười nói với khách"),
    (5, "我最近越来越胖了", "Wǒ zuìjìn yuè lái yuè pàng le", "Dạo này em ngày càng béo ra"),
    (6, "怎么突然找不到了", "Zěnme tūrán zhǎobúdào le", "Sao tự nhiên lại không tìm thấy"),
    (7, "我跟他都认识五年了", "Wǒ gēn tā dōu rènshi wǔ nián le", "Tôi và anh ấy quen nhau 5 năm rồi"),
    (8, "你去哪儿我就去哪儿", "Nǐ qù nǎr wǒ jiù qù nǎr", "Em đi đâu anh đi theo đó"),
    (9, "她的汉语说得跟中国人一样好", "Tā de hànyǔ shuō de gēn zhōngguórén yíyàng hǎo", "Tiếng Trung của cô ấy nói hay như người Trung Quốc"),
    (10, "数学比历史难多了", "Shùxué bǐ lìshǐ nán duō le", "Toán khó hơn Lịch sử nhiều"),
    (11, "别忘了把空调关了", "Bié wàng le bǎ kōngtiáo guān le", "Đừng quên tắt máy điều hòa"),
    (12, "把重要的事写在笔记本上", "Bǎ zhòngyào de shì xiě zài bǐjìběn shang", "Hãy viết việc quan trọng vào sổ tay"),
    (13, "我是走回来的", "Wǒ shì zǒu huílái de", "Tôi đi bộ về đấy"),
    (14, "你把水果拿过来", "Nǐ bǎ shuǐguǒ ná guòlái", "Em mang hoa quả qua đây"),
    (15, "其他都没什么问题", "Qítā dōu méi shénme wèntí", "Những thứ khác đều không vấn đề gì"),
    (16, "我现在累得想睡觉", "Wǒ xiànzài lèi de xiǎng shuìjiào", "Bây giờ tôi mệt đến mức chỉ muốn ngủ"),
    (17, "谁都有办法看好病", "Shéi dōu yǒu bànfǎ kànhǎo bìng", "Ai cũng có cách chữa khỏi bệnh"),
    (18, "我相信他们会同意的", "Wǒ xiāngxìn tāmen huì tóngyì de", "Tôi tin rằng họ sẽ đồng ý"),
    (19, "你没看出来吗？", "Nǐ méi kàn chūlái ma?", "Bạn không nhận ra à?"),
    (20, "我被他影响了", "Wǒ bèi tā yǐngxiǎng le", "Tôi bị anh ấy ảnh hưởng")
]

NAV_BAR_CSS = """
    /* TOP LESSON NAVIGATION BAR */
    .lesson-nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      background: rgba(13, 19, 34, 0.92);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      padding: 10px 18px;
      border-radius: 18px;
      margin-bottom: 22px;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
      flex-wrap: wrap;
    }
    .lesson-nav-bar .nav-left, .lesson-nav-bar .nav-right {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .lesson-nav-bar .nav-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 8px 14px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
      text-decoration: none;
    }
    .lesson-nav-bar .nav-btn:hover:not(:disabled) {
      background: var(--accent);
      color: #04101e;
      border-color: var(--accent);
      transform: translateY(-1px);
    }
    .lesson-nav-bar .nav-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
    }
    .lesson-nav-bar .nav-btn.btn-hub {
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      color: #04101e;
      font-weight: 700;
      border-color: transparent;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }
    .lesson-nav-bar .nav-btn.btn-hub:hover {
      background: linear-gradient(135deg, #0369a1, #0284c7);
      color: #fff;
    }
    .lesson-nav-bar .nav-select-box {
      flex: 1;
      min-width: 240px;
      max-width: 480px;
      position: relative;
    }
    .lesson-nav-bar select {
      width: 100%;
      background: rgba(26, 34, 52, 0.95);
      color: var(--text-main);
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 8px 14px;
      border-radius: 10px;
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      outline: none;
      transition: border-color 0.2s ease;
    }
    .lesson-nav-bar select:focus {
      border-color: var(--accent);
      box-shadow: 0 0 10px var(--accent-glow);
    }
    @media (max-width: 720px) {
      .lesson-nav-bar { flex-direction: column; align-items: stretch; gap: 10px; }
      .lesson-nav-bar .nav-left, .lesson-nav-bar .nav-right { justify-content: space-between; width: 100%; }
      .lesson-nav-bar .nav-select-box { max-width: 100%; width: 100%; }
    }
    /* HIDE / REMOVE FLOATING HAMBURGER AND SIDEBAR DRAWER */
    .btn-hamburger, #btnHamburger, .sidebar-drawer, #sidebarDrawer, .drawer-overlay, #drawerOverlay {
      display: none !important;
    }
"""

def generate_nav_bar(current_lesson):
    opts = []
    for num, zh, py, vi in LESSON_TITLES:
        url = "index.html" if num == current_lesson else f"../Bai_{num:02d}/index.html"
        sel = ' selected' if num == current_lesson else ''
        opts.append(f'            <option value="{url}"{sel}>Bài {num:02d}: {zh} ({vi})</option>')
    
    options_html = "\n".join(opts)

    hub_url = "../../index.html"
    catalog_url = "../index.html"

    # Prev button
    if current_lesson == 1:
        prev_btn = '<button class="nav-btn prev-btn" disabled title="Đây là bài học đầu tiên">◀</button>'
    else:
        prev_url = f"../Bai_{current_lesson-1:02d}/index.html"
        prev_btn = f'<a href="{prev_url}" class="nav-btn prev-btn" title="Quay lại bài {current_lesson-1}">◀</a>'

    # Next button
    if current_lesson == 20:
        next_btn = '<button class="nav-btn next-btn" disabled title="Đây là bài học cuối cùng">▶</button>'
    else:
        next_url = f"../Bai_{current_lesson+1:02d}/index.html"
        next_btn = f'<a href="{next_url}" class="nav-btn next-btn" title="Chuyển sang bài {current_lesson+1}">▶</a>'

    nav_bar_html = f"""<!-- TOP LESSON NAVIGATION BAR -->
    <div class="lesson-nav-bar">
      <div class="nav-left">
        <a href="{hub_url}" class="nav-btn btn-hub" title="Quay về Cổng Tổng HSK 3">🏠 Cổng Tổng</a>
        <a href="{catalog_url}" class="nav-btn" title="Quay về danh mục 20 bài">📚 Danh mục</a>
      </div>
      <div class="nav-right" style="flex:1; justify-content:flex-end;">
        {prev_btn}
        <div class="nav-select-box">
          <select id="lessonNavSelect" onchange="if(this.value) window.location.href=this.value;">
{options_html}
          </select>
        </div>
        {next_btn}
      </div>
    </div>
    <!-- END TOP LESSON NAVIGATION BAR -->"""
    return nav_bar_html

def update_lesson_file(file_path, lesson_num):
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject or update CSS
    if '.btn-hamburger, #btnHamburger' not in content:
        content = content.replace('</style>', f"{NAV_BAR_CSS}\n  </style>")

    # 2. Inject or replace Nav Bar
    new_nav = generate_nav_bar(lesson_num)
    if '<!-- TOP LESSON NAVIGATION BAR -->' in content:
        content = re.sub(
            r'<!-- TOP LESSON NAVIGATION BAR -->.*?</div>\s*(?=<header>)',
            new_nav + '\n\n    ',
            content,
            flags=re.DOTALL
        )
    elif '<div class="lesson-nav-bar">' in content:
        content = re.sub(
            r'<div class="lesson-nav-bar">.*?</div>\s*(?=<header>)',
            new_nav + '\n\n    ',
            content,
            flags=re.DOTALL
        )
    else:
        target = '<div class="container" id="app">'
        if target in content:
            content = content.replace(target, f"{target}\n    {new_nav}")
        else:
            content = content.replace('<header>', f"    {new_nav}\n    <header>")

    # 3. Completely remove hamburger button and sidebar drawer from DOM
    content = re.sub(r'<!-- HAMBURGER BUTTON.*?-->\s*<button class="btn-hamburger".*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<button class="btn-hamburger".*?</button>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- DRAWER OVERLAY -->\s*<div class="drawer-overlay".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="drawer-overlay".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<aside class="sidebar-drawer".*?</aside>', '', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def generate_web1_landing_page():
    """Build the clean, dedicated Landing Page for Cổng 1 (Exam Practice Hub)"""
    lesson_cards = []
    for num, zh, py, vi in LESSON_TITLES:
        url = f"Bai_{num:02d}/index.html"
        lesson_cards.append(f"""
        <a href="{url}" class="lesson-card">
          <div class="lesson-badge">BÀI {num:02d}</div>
          <div class="lesson-zh">{zh}</div>
          <div class="lesson-py">{py}</div>
          <div class="lesson-vi">{vi}</div>
          <div class="lesson-footer">
            <span>20 Câu Nghe • 15 Đọc • 10 Viết</span>
            <span class="btn-enter">Làm bài ▶</span>
          </div>
        </a>
        """)

    cards_html = "\n".join(lesson_cards)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HSK 3 - Cổng 1: Luyện Thi & Bài Học 20 Bài (Exam Practice Hub)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Serif+SC:wght@500;700;900&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg: #090e17;
      --card-bg: rgba(22, 30, 48, 0.75);
      --card-hover: rgba(30, 42, 68, 0.9);
      --card-border: rgba(255, 255, 255, 0.08);
      --text-main: #f8fafc;
      --text-sub: #94a3b8;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --accent-dark: #0284c7;
      --chinese-font: "Noto Serif SC", serif;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: radial-gradient(circle at 50% -10%, #1e293b 0%, #0d1527 45%, #070b14 100%);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', sans-serif;
      min-height: 100vh;
      padding: 30px 20px 80px;
      line-height: 1.6;
    }}
    .container {{
      max-width: 1060px;
      margin: 0 auto;
    }}
    /* TOPBAR */
    .topbar-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(13, 19, 34, 0.9);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 10px 18px;
      margin-bottom: 24px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--card-border);
      color: var(--text-main);
      padding: 8px 14px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{
      background: var(--accent);
      color: #04101e;
      transform: translateY(-1px);
    }}
    .nav-btn.btn-hub {{
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      color: #04101e;
      font-weight: 700;
      border-color: transparent;
    }}

    /* HEADER */
    header {{
      text-align: center;
      margin-bottom: 34px;
      padding: 36px 24px;
      background: var(--card-bg);
      backdrop-filter: blur(20px);
      border-radius: 26px;
      border: 1px solid var(--card-border);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }}
    .badge-hero {{
      display: inline-block;
      background: rgba(2, 132, 199, 0.2);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--accent);
      padding: 6px 16px;
      border-radius: 30px;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 32px;
      font-weight: 800;
      margin-bottom: 10px;
    }}
    .subtitle {{
      font-size: 16px;
      color: var(--text-sub);
      max-width: 720px;
      margin: 0 auto;
    }}

    /* SECTIONS OVERVIEW */
    .sections-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
      margin-bottom: 34px;
    }}
    .section-desc-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      padding: 22px 18px;
      transition: all 0.2s;
    }}
    .section-desc-card:hover {{
      border-color: var(--accent);
      transform: translateY(-2px);
    }}
    .sec-icon {{
      font-size: 28px;
      margin-bottom: 10px;
    }}
    .sec-title {{
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 6px;
    }}
    .sec-desc {{
      font-size: 13px;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    /* LESSONS LIST */
    .catalog-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 26px;
      padding: 30px 24px;
    }}
    .catalog-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 22px;
      padding-bottom: 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      flex-wrap: wrap;
      gap: 10px;
    }}
    .catalog-title {{
      font-size: 20px;
      font-weight: 800;
    }}
    .lessons-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 16px;
    }}
    .lesson-card {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 20px;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }}
    .lesson-card:hover {{
      border-color: var(--accent);
      background: var(--card-hover);
      transform: translateY(-2px);
      box-shadow: 0 10px 25px rgba(2, 132, 199, 0.2);
    }}
    .lesson-badge {{
      display: inline-block;
      font-size: 11.5px;
      font-weight: 800;
      color: var(--accent);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 3px 10px;
      border-radius: 8px;
      align-self: flex-start;
      margin-bottom: 10px;
    }}
    .lesson-zh {{
      font-family: var(--chinese-font);
      font-size: 20px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }}
    .lesson-py {{
      font-size: 13px;
      color: var(--accent);
      margin-bottom: 6px;
    }}
    .lesson-vi {{
      font-size: 14px;
      color: var(--text-sub);
      margin-bottom: 16px;
    }}
    .lesson-footer {{
      font-size: 12px;
      color: #64748b;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 10px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      margin-top: auto;
    }}
    .btn-enter {{
      color: var(--accent);
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <div class="container">
    <!-- TOPBAR -->
    <div class="topbar-nav">
      <div style="display:flex; align-items:center; gap:8px;">
        <a href="../index.html" class="nav-btn btn-hub">🏠 Cổng Tổng HSK 3</a>
        <span style="font-size:13px; font-weight:700; color:var(--text-sub);">📁 1_Web_LuyenThi_HSK3/</span>
      </div>
      <div style="display:flex; align-items:center; gap:8px;">
        <a href="../2.1_Web_SoanBai_HSK3/index.html" class="nav-btn" style="color:#fbbf24; border-color:rgba(245, 158, 11, 0.4);">🤖 Sang Cổng 2: Soạn Bài (AI 2.1)</a>
      </div>
    </div>

    <!-- HEADER -->
    <header>
      <div class="badge-hero">🎧 CỔNG 1 &bull; PHÒNG THI &amp; BÀI HỌC HSK 3</div>
      <h1>Trung Tâm Luyện Thi HSK 3 (20 Bài Học)</h1>
      <p class="subtitle">Hệ thống đề thi và bài tập tương tác toàn diện theo chuẩn cấu trúc Đề thi HSK 3 Quốc tế và Giáo trình Chuẩn HSK 3</p>
    </header>

    <!-- 4 SECTIONS OVERVIEW -->
    <div class="sections-grid">
      <div class="section-desc-card">
        <div class="sec-icon">🎧</div>
        <div class="sec-title">1. Bài Nghe (听力 - 20 Câu)</div>
        <div class="sec-desc">Gồm 4 phần: Đối thoại chọn tranh (1-5), Đúng/Sai (6-10), Đối thoại ngắn (11-15), Đối thoại dài (16-20). Tích hợp thanh Audio có nút nhảy mốc thời gian tức thì.</div>
      </div>

      <div class="section-desc-card">
        <div class="sec-icon">📖</div>
        <div class="sec-title">2. Bài Đọc (阅读 - 15 Câu)</div>
        <div class="sec-desc">Gồm 3 phần: Ghép cặp câu đối ứng A-E (21-25), Điền từ vào chỗ trống trong đoạn văn (26-30), Đọc đoạn ngắn trả lời câu hỏi trắc nghiệm (31-35).</div>
      </div>

      <div class="section-desc-card">
        <div class="sec-icon">✍️</div>
        <div class="sec-title">3. Bài Viết (书写 - 10 Câu)</div>
        <div class="sec-desc">Gồm 2 phần: Sắp xếp các cụm từ xáo trộn thành câu hoàn chỉnh đúng ngữ pháp (36-40), Điền chữ Hán vào câu theo gợi ý phiên âm Pinyin (41-45).</div>
      </div>

      <div class="section-desc-card">
        <div class="sec-icon">📚</div>
        <div class="sec-title">4. Từ Vựng &amp; Ngữ Pháp SGK</div>
        <div class="sec-desc">Bảng từ vựng mới có tra nhanh pinyin/nghĩa/chiết tự, chữ đa âm tự và phân tích chi tiết các điểm ngữ pháp trọng điểm của từng bài học.</div>
      </div>
    </div>

    <!-- CATALOG OF 20 LESSONS -->
    <section class="catalog-box">
      <div class="catalog-header">
        <div>
          <h2 class="catalog-title">📚 Danh Sách 20 Bài Luyện Thi &amp; Bài Học</h2>
          <span style="font-size:13.5px; color:var(--text-sub);">Bấm vào bài bất kỳ để vào làm bài thi tương tác ngay lập tức</span>
        </div>
        <span style="font-size:13px; font-weight:700; color:var(--accent);">Trọn bộ 20/20 Bài hoàn chỉnh</span>
      </div>

      <div class="lessons-grid">
{cards_html}
      </div>
    </section>
  </div>
</body>
</html>"""
    return html

def main():
    print("==================================================")
    print("UPDATING 1_Web_LuyenThi_HSK3 NAVIGATION & LANDING PAGE")
    print("==================================================")

    # 1. Update Bai_01 to Bai_20
    for i in range(1, 21):
        p = os.path.join(WEB1_DIR, f"Bai_{i:02d}", "index.html")
        if os.path.exists(p):
            success = update_lesson_file(p, i)
            if success:
                print(f"✅ Updated navigation in: {p}")

    # 2. Build dedicated landing page for 1_Web_LuyenThi_HSK3/index.html
    landing_html = generate_web1_landing_page()
    landing_path = os.path.join(WEB1_DIR, "index.html")
    with open(landing_path, 'w', encoding='utf-8') as f:
        f.write(landing_html)
    print(f"✅ Created Landing Page: {landing_path} ({len(landing_html)} bytes)")

    print("\n🎉 DONE UPDATING WEB 1!")

if __name__ == '__main__':
    main()
