# -*- coding: utf-8 -*-
"""
Generate a professional 16:9 PowerPoint presentation for the SCN CCK Neuron Circadian Clock Journal Club.
Extracts verbatim presentation script, laser pointer cues, and slide transitions from PRESENTATION_SLIDES_AND_SCRIPT.md,
embeds high-resolution figures into the slides, and attaches the complete script into PowerPoint Speaker Notes.
"""

import os
import re
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def parse_markdown_presentation(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split slides by: ## Slide XX / 15：Title
    parts = re.split(r'## Slide (\d+) / 15[：:]\s*([^\n\r]+)', text)
    slides_data = []

    for i in range(1, len(parts), 3):
        num = int(parts[i])
        title = parts[i+1].strip()
        content = parts[i+2]

        sub_vis = re.search(r'### [^\n]*视觉呈现与版式设计\s*(.*?)(?=###|\Z)', content, re.DOTALL)
        sub_laser = re.search(r'### [^\n]*激光笔动作指引\s*(.*?)(?=###|\Z)', content, re.DOTALL)
        sub_trans = re.search(r'### [^\n]*幻灯片衔接过渡语\s*(.*?)(?=###|\Z)', content, re.DOTALL)
        sub_script = re.search(r'### [^\n]*现场汇报逐字讲稿\s*(.*?)(?=###|\Z)', content, re.DOTALL)

        vis_text = sub_vis.group(1).strip() if sub_vis else ''
        laser_text = sub_laser.group(1).strip() if sub_laser else ''
        trans_text = sub_trans.group(1).strip() if sub_trans else ''
        script_text = sub_script.group(1).strip() if sub_script else ''

        # Extract timing from script_text (e.g. ⏱️ 汇报时间：[00:00 - 01:15])
        timing_match = re.search(r'\[(\d{2}:\d{2}\s*-\s*\d{2}:\d{2})\]', script_text)
        timing = timing_match.group(1) if timing_match else ''

        slides_data.append({
            'num': num,
            'title': title,
            'timing': timing,
            'vis': vis_text,
            'laser': laser_text,
            'trans': trans_text,
            'script': script_text
        })

    return slides_data

def build_presentation(slides_data, output_path):
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_DARK_BG = RGBColor(15, 23, 42)      # #0F172A Slate 900
    COLOR_CARD_DARK = RGBColor(30, 41, 59)    # #1E293B Slate 800
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_TEXT_MAIN = RGBColor(30, 41, 59)    # #1E293B
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)# #64748B
    COLOR_CYAN = RGBColor(14, 165, 233)       # #0EA5E9 Sky 500
    COLOR_AMBER = RGBColor(217, 119, 6)       # #D97706 Amber 600
    COLOR_CARD_BG = RGBColor(248, 250, 252)   # #F8FAFC Slate 50
    COLOR_BORDER = RGBColor(226, 232, 240)    # #E2E8F0 Slate 200
    COLOR_LIGHT_BLUE = RGBColor(239, 246, 255)# #EFF6FF

    # Figure mapping
    fig_map = {
        1: 'figures/graphical_abstract.png',
        2: None, # Concept comparison
        3: 'figures/graphical_abstract.png',
        4: 'figures/figure1.png',
        5: 'figures/figure2.png',
        6: 'figures/figure3.png',
        7: 'figures/figure4.png',
        8: 'figures/figure4.png',
        9: 'figures/figure5.png',
        10: 'figures/figure5.png',
        11: 'figures/figure6.png',
        12: 'figures/figure6.png',
        13: 'figures/graphical_abstract.png',
        14: None, # 3-card critical appraisal
        15: 'figures/graphical_abstract.png',
    }

    # Custom slide text highlights & bullets
    custom_slide_content = {
        1: {
            'tag': 'NEURON 2023 · JOURNAL CLUB PRESENTATION',
            'headline': 'Cholecystokinin Neurons in Mouse Suprachiasmatic Nucleus Regulate the Robustness of Circadian Clock',
            'cn_title': '小鼠视交叉上核 (SCN) 胆囊收缩素 (CCK) 神经元调控生物钟系统鲁棒性',
            'bullets': [
                '通讯作者与单位：严军 研究员（中国科学院脑智卓越创新中心 / 神经科学研究所）',
                '第一作者：谢迪、罗敏 博士',
                '汇报场景：博士研究生文献讨论会 / 课题组汇报 (PhD Journal Club)',
                '报告总时长：严格控制在 18 ~ 20 分钟（语速 220-250 字/分）',
                '核心突破：首次揭示夜间放电的 CCK 抑制性回路作为生物钟“阻尼器/分子刹车”，解决鲁棒性与可塑性平衡悖论'
            ]
        },
        2: {
            'tag': 'SCIENTIFIC QUESTION & THE PARADOX',
            'headline': '核心科学悖论：生物钟的“稳健性 (Robustness)”与“可塑性 (Plasticity)”权衡',
            'bullets_left': [
                '【高稳健性 (Robustness) 需求】',
                '• SCN 作为机体节律总控中枢，必须维持极其精确稳定的内源 24h 振荡周期。',
                '• 面对机体日常生理噪声、体温波动及微弱非预期光信号，必须具备强大的抗干扰能力。',
                '• 经典已知机制：VIP-VPAC2 与 AVP 介导全网络细胞间强同相耦合。'
            ],
            'bullets_right': [
                '【高可塑性 (Plasticity) 需求】',
                '• 季节变换引起的日照长度变化，以及跨时区飞行或轮班，需要 SCN 能快速发生相位重置 (Phase Resetting)。',
                '• 如果耦合过于刚性强硬，系统将丧失重夹带适应能力；',
                '• 科学谜题：SCN 究竟依赖何种神经回路与递质信号，动态兼顾二者，避免过度重置？'
            ]
        },
        3: {
            'tag': 'EXPERIMENTAL PIPELINE & STRATEGY',
            'headline': '研究假设与四阶多层级验证闭环架构',
            'bullets': [
                '核心科学假设：SCN 腹外侧多肽 CCK 神经元作为网络阻尼器，在夜间活跃并制动光致相位漂移。',
                '1. 活体动态追踪：光纤记录 (Fiber Photometry) 测定 SCN CCK 神经元在体钙活动昼夜曲线 (Figure 1)；',
                '2. 必要性遗传验证：taiep 突变模型与靶向诱导消融 AAV-DIO-taCasp3 评估行为与脑片节律稳定性 (Figure 2)；',
                '3. 突触与受体药理解析：光遗传学激活 (Figure 3) + 全细胞膜片钳与 PER2 脑片发光探究 CCKBR 机制 (Figure 4)；',
                '4. 网络相干性与行为转化：单细胞发光成像 (Figure 5) + 时差模型与两群体 Kuramoto 分岔理论诠释 (Figure 6)。'
            ]
        },
        4: {
            'tag': 'FIGURE 1 · IN VIVO CALCIUM DYNAMICS',
            'headline': 'SCN CCK 神经元呈现特异的夜间体内钙活动高峰',
            'bullets': [
                '实验范式：AAV-DIO-GCaMP6s 定向立体注入 Cck-IRES-Cre 小鼠 SCN，植入光纤进行多天连续游离钙监测。',
                '核心发现 1：SCN CCK 神经元钙活动呈现显著的昼夜节律波动，峰值集中在主观夜间早期 (ZT14 ~ ZT18)。',
                '核心发现 2：与白天放电活跃的 VIP/AVP 神经元完全反相，形成独特的昼夜“交替兴奋”格局。',
                '关键推论：夜间正是机体对光照最敏感、极易诱发大幅度相位重置的时间窗口，提示 CCK 在夜间行使特异制动功能。'
            ]
        },
        5: {
            'tag': 'FIGURE 2 · LOSS-OF-FUNCTION & ABLATION',
            'headline': '遗传消融 CCK 神经元导致自主节律失稳与振幅严重衰减',
            'bullets': [
                '动物模型：taiep 突变大鼠（自然缺失 CCK 神经元）与 AAV-DIO-taCasp3 靶向消融小鼠。',
                '行为学表型：在持续黑暗 (DD) 环境下，消融组小鼠轮跑周期发生延长且节律稳定性显著恶化。',
                '离体组织电生理与分子发光：SCN 脑片多电极自发放电振幅及 PER2::LUC 生物发光节律振幅暴跌 >40%。',
                '阶段结论：CCK 神经元对于维持中枢节律高振幅、高鲁棒性的自主振荡具有绝对的必要性。'
            ]
        },
        6: {
            'tag': 'FIGURE 3 · OPTO-INHIBITION OF LIGHT-INDUCED DELAYS',
            'headline': '光遗传激活 CCK 神经元特异性抵消光致相位延迟',
            'bullets': [
                '实验设计：向 SCN 靶向递送 AAV-DIO-ChR2，在主观夜间早期 (CT14) 施加环境光脉冲并同步光刺激 CCK 神经元。',
                '对照组表现：CT14 的单次短时白光脉冲诱发约 -2.5 小时的显著行为相位延迟 (Phase Delay)。',
                '光遗传组表现：同步光激活 CCK 神经元完全逆转了光诱发的行为相位延迟，相位改变量趋近于零！',
                '功能确证：CCK 神经元的兴奋释放是直接对抗非预期夜间光授时信号、制动节律漂移的生理性“分子刹车”。'
            ]
        },
        7: {
            'tag': 'FIGURE 4A-D · ELECTROPHYSIOLOGY & MOLECULAR RESET',
            'headline': 'CCK 抑制突触后自发放电并诱发 PER2 发光相位提前',
            'bullets': [
                '全细胞膜片钳记录：在离体 SCN 急性脑片上外源灌流 CCK-8S 活性八肽。',
                '电生理效应：CCK-8S 显著降低了 78% SCN 神经元的自发放电频率 (SFR)，产生稳健的突触后超极化抑制。',
                '生物发光动态成像：实时监测 SCN 脑片 PER2::LUC 节律，外源施加 CCK 诱导了稳健的相位提前 (+2.8 h)。',
                '机制闭环：揭示 CCK 释放通过电生理抑制重排下游钟基因转录反馈环路相位。'
            ]
        },
        8: {
            'tag': 'FIGURE 4E-H · RECEPTOR PHARMACOLOGY',
            'headline': 'CCK-B 受体特异性介导相位重塑与放电抑制',
            'bullets': [
                '药理学受体亚型解析：应用 CCK-A (Devazepide) 与 CCK-B (CI-988 / L-365,260) 特异性拮抗剂。',
                '受体确证：CCKBR 拮抗剂 CI-988 完全阻断了 CCK 引起的突触后放电抑制与 PER2 相位提前效应。',
                '阴性对照：CCKAR 拮抗剂 Devazepide 处理组未产生任何显著阻断作用。',
                '通路归纳：CCK 信号通过突触后高表达的 CCK-B 受体偶联下游信号通路，实现节律相位精准操控。'
            ]
        },
        9: {
            'tag': 'FIGURE 5A-D · SINGLE-CELL SPATIOTEMPORAL DYNAMICS',
            'headline': '单细胞发光网络成像：消融导致振荡器发散与网络去同步',
            'bullets': [
                '单细胞显微成像：倒置高灵敏发光显微镜连续追踪培养 SCN 脑片中数百个单细胞 PER2::LUC 轨迹。',
                '正常野生型网络：各个 SCN 神经元维持高程度的相位相干性，Kuramoto 序参量 R > 0.85。',
                'CCK 消融表型：单细胞自主振荡依然存在，但神经元之间的相位离散度急剧增大，全局相干性暴跌至 0.42。',
                '理论意义：确证 CCK 并非细胞自主振荡的起搏分子，而是维系神经元之间同相共振的关键网络同步介质。'
            ]
        },
        10: {
            'tag': 'FIGURE 5E-H · PHARMACOLOGICAL RESCUE',
            'headline': '外源 CCK 充分逆转去同步化并重塑全局网络相干性',
            'bullets': [
                '功能挽救 (Rescue) 实验：向去同步化的消融脑片培养基中外源性补充 CCK-8S 多肽。',
                '网络重构：外源性 CCK 迅速将发散杂乱的单细胞振荡器重新对齐到统一的集体相位。',
                '序参量恢复：Kuramoto 序参量 R 从 0.42 重新拉升至 0.82 以上，完全恢复整体高振幅生物发光节律。',
                '充分性论证：CCK 不仅是 SCN 网络维持同步的必要条件，其单独存在也足以介导去同步网络的重新同步化。'
            ]
        },
        11: {
            'tag': 'FIGURE 6A-D · JETLAG RE-ENTRAINMENT PARADIGM',
            'headline': 'CCK 神经元消融显著加速小鼠对 8小时时差的重夹带',
            'bullets': [
                '模拟时差范式：将小鼠置于光暗周期突然提前 8 小时 (Phase Advance) 的极端光照重夹带挑战下。',
                '野生型小鼠表现：由于内源 CCK 阻尼器的存在，表现出顽固的节律惰性，需要 8.5 天方能重新完全适应新光照。',
                '消融小鼠表型：重夹带过程大幅提速，仅需约 4.2 天即可重新同相锁定（适应速度提升超过 50%）。',
                '生物学启示：揭示了机体为换取日常极高稳健性（抗偶发光干扰）而在极端时差适应速度上付出的演化权衡代价。'
            ]
        },
        12: {
            'tag': 'FIGURE 6E-H · THEORETICAL BIFURCATION DYNAMICS',
            'headline': '基于两群体 Kuramoto 模型的动力学分岔解析',
            'bullets': [
                '理论物理建模：构建包含腹外侧 (VL) 核心与背内侧 (DM) 壳部的两群体非线性相位振荡器模型。',
                '参数设定：引入 CCK 作为 VL 向全网络施加的抑制性/负耦合强度参数 K_cck。',
                '动力学分岔分析：模型理论推导证明，移除 K_cck 使系统跨越 Hopf 分岔点，显著缩小了重夹带相轨迹的吸引子盆地。',
                '跨尺度闭环：理论模拟完美复现了时差重夹带加速及周期微变实验数据，完成了从分子突触到动力学物理的统一。'
            ]
        },
        13: {
            'tag': 'SUMMARY & THE WORKING MODEL',
            'headline': '总结与核心工作机制模型：CCK 神经元充当生物钟“分子阻尼器”',
            'bullets': [
                '白昼相（可塑期）：VIP 神经元活跃，介导外周视网膜授时信号传入与全局网络兴奋耦合。',
                '黑夜相（制动期）：CCK 神经元高频放电并释放 CCK-8S，通过突触后 CCKBR 抑制放电并稳定相位。',
                '双向耦合网络：VIP 与 CCK 形成白天兴奋/夜间抑制的时间反相交替控制回路。',
                '核心学术贡献：彻底改写了 SCN 仅由 VIP/AVP 兴奋同步驱动的传统认知，奠定了阻尼介质维持鲁棒性的新范式。'
            ]
        },
        14: {
            'tag': 'CRITICAL EVALUATION & METHODOLOGICAL CAVEATS',
            'headline': '博士级批判性审视与实验局限性 (Defense Rebuttals & Caveats)',
            'bullets_col1': [
                '【药理学浓度与受体脱敏】',
                '• 脑片灌流浓度 (100nM-1μM) 远高于脑脊液生理水平；',
                '• CCKBR 属于易脱敏内化 GPCR，长期持续暴露是否引起耐受机制未作追踪。'
            ],
            'bullets_col2': [
                '【Gq/11 级联放电悖论】',
                '• CCKBR 传统激活 Gq-PLC-IP3 导致胞内钙升高，何以产生放电抑制？',
                '• 亟需补做 GIRK 或高电导 BK 钾通道阻断剂实验以查明下游效应器。'
            ],
            'bullets_col3': [
                '【共释放递质与发育差异】',
                '• CCK 神经元共释放 GABA，光遗传刺激未完全排除 GABAergic 效应；',
                '• 单细胞成像基于幼鼠脑片 (P3-P7)，对成年神经回路的外推存在发育代沟。'
            ]
        },
        15: {
            'tag': 'FUTURE OUTLOOK & ACKNOWLEDGMENTS',
            'headline': '未来探索方向、转化医学潜能与致谢答辩',
            'bullets': [
                '1. 转化医学与药物开发：开发高选择性脑通透性 CCK-B 受体拮抗剂，作为防治严重跨时区时差与轮班综合征的新型靶向药；',
                '2. 突触共递质精细解析：结合高精度光遗传电生理与单细胞转录组，切分 CCK 多肽慢信号与 GABA 快信号的时空协同分工；',
                '3. 衰老与神经退行性病变：探究阿尔茨海默病 (AD) 等神经退行患者中 SCN CCK 表达下调与严重睡眠节律紊乱的因果联系。',
                '致谢：衷心感谢中国科学院脑智卓越中心严军研究员团队的卓越工作！',
                '恳请各位评委老师和同仁批评指正！(Thank You! Q & A Session)'
            ]
        }
    }

    # Iterate through all 15 slides
    for slide_data in slides_data:
        num = slide_data['num']
        title = slide_data['title']
        timing = slide_data['timing']
        laser = slide_data['laser']
        trans = slide_data['trans']
        script = slide_data['script']

        custom = custom_slide_content.get(num, {
            'tag': f'SLIDE {num:02d} · JOURNAL CLUB',
            'headline': title,
            'bullets': [title]
        })

        slide = prs.slides.add_slide(blank_layout)

        # 1. Slide 1 (Title slide - Navy Theme)
        if num == 1:
            # Background shape
            bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
            bg.fill.solid()
            bg.fill.fore_color.rgb = COLOR_DARK_BG
            bg.line.fill.background()

            # Pill Tag
            tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(7.0), Inches(0.4))
            tf = tag_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = custom['tag']
            p.font.name = 'Arial'
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN

            # English Headline
            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(7.0), Inches(1.6))
            tf = title_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = custom['headline']
            p.font.name = 'Arial'
            p.font.size = Pt(20)
            p.font.bold = True
            p.font.color.rgb = COLOR_WHITE

            # Chinese Subtitle
            cn_box = slide.shapes.add_textbox(Inches(0.8), Inches(2.9), Inches(7.0), Inches(0.8))
            tf = cn_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = custom['cn_title']
            p.font.name = 'Microsoft YaHei'
            p.font.size = Pt(15)
            p.font.bold = True
            p.font.color.rgb = COLOR_AMBER

            # Card for presenter & metadata
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.8), Inches(7.0), Inches(2.9))
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_CARD_DARK
            card.line.color.rgb = RGBColor(51, 65, 85)
            tf = card.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.3)
            tf.margin_top = Inches(0.25)
            for j, b in enumerate(custom['bullets']):
                p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
                p.text = b
                p.font.name = 'Microsoft YaHei'
                p.font.size = Pt(11.5)
                p.font.color.rgb = COLOR_WHITE if j < 2 else RGBColor(203, 213, 225)
                p.space_after = Pt(6)

            # Right image: Graphical abstract
            img_path = fig_map[1]
            if os.path.exists(img_path):
                slide.shapes.add_picture(img_path, Inches(8.1), Inches(1.0), Inches(4.5), Inches(5.5))

        # 2. Slide 2: Two-column Comparison Paradox
        elif num == 2:
            # Header banner
            tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.35))
            tf = tag_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['tag']
            p.font.name = 'Arial'
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN

            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.5), Inches(0.6))
            tf = title_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['headline']
            p.font.name = 'Microsoft YaHei'
            p.font.size = Pt(20)
            p.font.bold = True
            p.font.color.rgb = COLOR_TEXT_MAIN

            # Left Card: Robustness
            card1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.4))
            card1.fill.solid()
            card1.fill.fore_color.rgb = COLOR_CARD_BG
            card1.line.color.rgb = COLOR_BORDER
            tf1 = card1.text_frame
            tf1.word_wrap = True
            tf1.margin_left = Inches(0.3)
            tf1.margin_top = Inches(0.3)
            for j, b in enumerate(custom['bullets_left']):
                p = tf1.paragraphs[0] if j == 0 else tf1.add_paragraph()
                p.text = b
                p.font.name = 'Microsoft YaHei'
                p.font.size = Pt(14) if j == 0 else Pt(12.5)
                p.font.bold = (j == 0)
                p.font.color.rgb = COLOR_TEXT_MAIN
                p.space_after = Pt(10)

            # Right Card: Plasticity
            card2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(4.4))
            card2.fill.solid()
            card2.fill.fore_color.rgb = COLOR_CARD_BG
            card2.line.color.rgb = COLOR_BORDER
            tf2 = card2.text_frame
            tf2.word_wrap = True
            tf2.margin_left = Inches(0.3)
            tf2.margin_top = Inches(0.3)
            for j, b in enumerate(custom['bullets_right']):
                p = tf2.paragraphs[0] if j == 0 else tf2.add_paragraph()
                p.text = b
                p.font.name = 'Microsoft YaHei'
                p.font.size = Pt(14) if j == 0 else Pt(12.5)
                p.font.bold = (j == 0)
                p.font.color.rgb = COLOR_TEXT_MAIN
                p.space_after = Pt(10)

            # Bottom Resolution Pill
            bot = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.8))
            bot.fill.solid()
            bot.fill.fore_color.rgb = COLOR_LIGHT_BLUE
            bot.line.color.rgb = COLOR_CYAN
            tfb = bot.text_frame
            tfb.word_wrap = True
            tfb.margin_left = Inches(0.3)
            tfb.margin_top = Inches(0.15)
            p = tfb.paragraphs[0]
            p.text = '【破局假说】SCN 内部必定存在一组夜间活跃的“制动阻尼”细胞群，在敏感窗口踩下分子刹车，守护系统鲁棒性！'
            p.font.name = 'Microsoft YaHei'
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = RGBColor(3, 105, 161)

        # 3. Slide 14: Three-column Critical Appraisal
        elif num == 14:
            # Header
            tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.5), Inches(0.35))
            tf = tag_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['tag']
            p.font.name = 'Arial'
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_AMBER

            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.5), Inches(0.6))
            tf = title_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['headline']
            p.font.name = 'Microsoft YaHei'
            p.font.size = Pt(20)
            p.font.bold = True
            p.font.color.rgb = COLOR_TEXT_MAIN

            cols = [
                (Inches(0.8), custom['bullets_col1']),
                (Inches(4.8), custom['bullets_col2']),
                (Inches(8.8), custom['bullets_col3'])
            ]
            for left, b_list in cols:
                card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.6), Inches(3.7), Inches(5.3))
                card.fill.solid()
                card.fill.fore_color.rgb = COLOR_CARD_BG
                card.line.color.rgb = COLOR_BORDER
                tfc = card.text_frame
                tfc.word_wrap = True
                tfc.margin_left = Inches(0.25)
                tfc.margin_top = Inches(0.25)
                for j, b in enumerate(b_list):
                    p = tfc.paragraphs[0] if j == 0 else tfc.add_paragraph()
                    p.text = b
                    p.font.name = 'Microsoft YaHei'
                    p.font.size = Pt(13.5) if j == 0 else Pt(12)
                    p.font.bold = (j == 0)
                    p.font.color.rgb = COLOR_AMBER if j == 0 else COLOR_TEXT_MAIN
                    p.space_after = Pt(10)

        # 4. Content Slides with Figure (Slides 3 to 13, and 15)
        else:
            # Header
            tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.5), Inches(0.35))
            tf = tag_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['tag']
            p.font.name = 'Arial'
            p.font.size = Pt(11)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN

            title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.78), Inches(11.5), Inches(0.6))
            tf = title_box.text_frame
            p = tf.paragraphs[0]
            p.text = custom['headline']
            p.font.name = 'Microsoft YaHei'
            p.font.size = Pt(18)
            p.font.bold = True
            p.font.color.rgb = COLOR_TEXT_MAIN

            # Left Card with bullets
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.4))
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_CARD_BG
            card.line.color.rgb = COLOR_BORDER
            tf = card.text_frame
            tf.word_wrap = True
            tf.margin_left = Inches(0.3)
            tf.margin_top = Inches(0.3)
            tf.margin_right = Inches(0.3)

            for j, b in enumerate(custom['bullets']):
                p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
                p.text = b
                p.font.name = 'Microsoft YaHei'
                p.font.size = Pt(12.5)
                p.font.color.rgb = COLOR_TEXT_MAIN
                p.space_after = Pt(10)

            # Right side Figure
            img_path = fig_map.get(num)
            if img_path and os.path.exists(img_path):
                # Add picture preserving aspect
                slide.shapes.add_picture(img_path, Inches(7.9), Inches(1.5), Inches(4.6), Inches(5.4))

        # 5. Populate Complete Speaker Notes (演说者备注)
        notes_slide = slide.notes_slide
        tf_notes = notes_slide.notes_text_frame
        
        timing_str = f"⏱️ 汇报时间规划：[{timing}]" if timing else "⏱️ 汇报时间规划：[未设定]"
        full_notes_text = (
            f"========================================================\n"
            f"【幻灯片序号】：Slide {num:02d} / 15\n"
            f"【幻灯片主题】：{title}\n"
            f"{timing_str}\n"
            f"========================================================\n\n"
            f"【🔴 激光笔动作指引】：\n"
            f"{laser}\n\n"
            f"========================================================\n"
            f"【🔄 幻灯片衔接过渡语】：\n"
            f"{trans}\n\n"
            f"========================================================\n"
            f"【🎙️ 现场汇报逐字讲稿】：\n"
            f"{script}\n"
        )
        tf_notes.text = full_notes_text

    prs.save(output_path)
    print(f"Successfully generated PowerPoint presentation at: {output_path}")

if __name__ == '__main__':
    md_file = 'PRESENTATION_SLIDES_AND_SCRIPT.md'
    output_pptx = 'SCN_CCK_Circadian_Clock_Journal_Club.pptx'
    slides_data = parse_markdown_presentation(md_file)
    build_presentation(slides_data, output_pptx)
