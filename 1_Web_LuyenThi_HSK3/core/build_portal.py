# -*- coding: utf-8 -*-
"""
Build Universal Portal and Update Root index.html + Lesson Navbars
Ensures 100% visual and functional identity between localhost and GitHub Pages deployment.
"""

import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

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
      background: rgba(13, 19, 34, 0.88);
      backdrop-filter: blur(16px);
      border: 1px solid var(--card-border);
      padding: 10px 18px;
      border-radius: 18px;
      margin-bottom: 22px;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
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
    .lesson-nav-bar .drawer-btn {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.3), rgba(56, 189, 248, 0.15));
      border-color: rgba(56, 189, 248, 0.3);
      color: var(--accent);
    }
    .lesson-nav-bar .drawer-btn:hover {
      background: var(--accent);
      color: #04101e;
    }
    .lesson-nav-bar .nav-select-box {
      flex: 1;
      max-width: 520px;
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
    @media (max-width: 680px) {
      .lesson-nav-bar { flex-wrap: wrap; padding: 10px 12px; gap: 8px; }
      .lesson-nav-bar .nav-select-box { order: 1; width: 100%; max-width: 100%; }
      .lesson-nav-bar .nav-btn { order: 2; flex: 1; justify-content: center; font-size: 12px; padding: 7px 6px; }
    }
"""

def generate_nav_bar(current_lesson, is_root=False):
    # Select options
    opts = []
    for num, zh, py, vi in LESSON_TITLES:
        if is_root:
            url = "index.html" if num == 1 else f"Bai_{num:02d}/index.html"
        else:
            if num == current_lesson:
                url = "index.html"
            elif num == 1:
                url = "../Bai_01/index.html"
            else:
                url = f"../Bai_{num:02d}/index.html"
        
        sel = ' selected' if num == current_lesson else ''
        opts.append(f'        <option value="{url}"{sel}>Bài {num:02d}: {zh} ({vi})</option>')
    
    options_html = "\n".join(opts)

    # Prev button
    if current_lesson == 1:
        prev_btn = '<button class="nav-btn prev-btn" disabled title="Đây là bài học đầu tiên">◀ Bài trước</button>'
    else:
        if is_root:
            prev_url = "index.html" if current_lesson == 2 else f"Bai_{current_lesson-1:02d}/index.html"
        else:
            prev_url = "../Bai_01/index.html" if current_lesson == 2 else f"../Bai_{current_lesson-1:02d}/index.html"
        prev_btn = f'<a href="{prev_url}" class="nav-btn prev-btn" title="Quay lại bài {current_lesson-1}">◀ Bài trước</a>'

    # Next button
    if current_lesson == 20:
        next_btn = '<button class="nav-btn next-btn" disabled title="Đây là bài học cuối cùng">Bài tiếp ▶</button>'
    else:
        if is_root:
            next_url = f"Bai_{current_lesson+1:02d}/index.html"
        else:
            next_url = f"../Bai_{current_lesson+1:02d}/index.html"
        next_btn = f'<a href="{next_url}" class="nav-btn next-btn" title="Chuyển sang bài {current_lesson+1}">Bài tiếp ▶</a>'

    nav_bar_html = f"""<!-- TOP LESSON NAVIGATION BAR -->
    <div class="lesson-nav-bar">
      {prev_btn}
      <div class="nav-select-box">
        <select id="lessonNavSelect" onchange="if(this.value) window.location.href=this.value;">
{options_html}
        </select>
      </div>
      {next_btn}
      <button class="nav-btn drawer-btn" onclick="toggleDrawer()" title="Mở danh mục toàn bộ 20 bài">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        <span>20 Bài học</span>
      </button>
    </div>
    <!-- END TOP LESSON NAVIGATION BAR -->"""
    return nav_bar_html

def inject_nav_bar(content, current_lesson, is_root=False):
    # 1. Inject CSS if not present
    if '.lesson-nav-bar' not in content:
        content = content.replace('</style>', f"{NAV_BAR_CSS}\n  </style>")

    # 2. Generate new nav_bar HTML
    new_nav = generate_nav_bar(current_lesson, is_root=is_root)

    # 3. Replace existing or insert new
    if '<!-- TOP LESSON NAVIGATION BAR -->' in content:
        content = re.sub(
            r'<!-- TOP LESSON NAVIGATION BAR -->.*?<!-- END TOP LESSON NAVIGATION BAR -->',
            new_nav,
            content,
            flags=re.DOTALL
        )
    else:
        target = '<div class="container" id="app">'
        if target in content:
            content = content.replace(target, f"{target}\n    {new_nav}")
        else:
            content = content.replace('<header>', f"    {new_nav}\n    <header>")
    
    return content

def main():
    print("==================================================")
    print("BUILDING UNIFIED LESSON PORTALS (ROOT + LESSONS 1-20)")
    print("==================================================")

    # 1. Revert Bai_01/index.html to clean git version first if needed
    os.system('& "C:\\Users\\My PC\\mingit\\cmd\\git.exe" checkout Bai_01/index.html')

    # Read clean Bai_01/index.html
    with open('Bai_01/index.html', 'r', encoding='utf-8') as f:
        bai1_clean = f.read()

    # Update Bai_01/index.html with nav bar
    bai1_updated = inject_nav_bar(bai1_clean, 1, is_root=False)
    with open('Bai_01/index.html', 'w', encoding='utf-8') as f:
        f.write(bai1_updated)
    print(f"Updated Bai_01/index.html ({len(bai1_updated)} bytes)")

    # 2. Build root index.html from Bai_01
    root_content = inject_nav_bar(bai1_clean, 1, is_root=True)
    
    # Adjust paths for root execution
    root_content = root_content.replace('src="audio.mp3"', 'src="Bai_01/audio.mp3"')
    for letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        root_content = root_content.replace(f'src="pic_{letter}.png"', f'src="Bai_01/pic_{letter}.png"')
    
    # Drawer links adjustment: remove ../
    root_content = root_content.replace('"url": "../Bai_', '"url": "Bai_')
    root_content = root_content.replace('`../Bai_', '`Bai_')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(root_content)
    print(f"Created root index.html ({len(root_content)} bytes)")

    with open('HSK3_Bai1_LuyenNghe.html', 'w', encoding='utf-8') as f:
        f.write(root_content)
    print(f"Created HSK3_Bai1_LuyenNghe.html ({len(root_content)} bytes)")

    # 3. Update Bai_02 to Bai_20
    for i in range(2, 21):
        p = f"Bai_{i:02d}/index.html"
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                c = f.read()
            c_up = inject_nav_bar(c, i, is_root=False)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(c_up)
            print(f"Updated {p} ({len(c_up)} bytes)")

    print("\n✅ ALL LESSON PORTALS COMPLETED!")

if __name__ == '__main__':
    main()
