# -*- coding: utf-8 -*-

PRESENTATION_HTML = """
<section id="presentation-section" class="section-card presentation-section">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">12</span> 15页文献汇报幻灯片架构与20分钟逐字讲稿 (Presentation Deck & Script)</h2>
    <p class="section-subtitle">专为高规格学术汇报（Journal Club / 组会 / 答辩）量身定制：含视觉蓝图、激光笔动作、衔接过渡语与现场逐字讲稿</p>
  </div>

  <div class="trans-content">
    
    <div class="seminar-block">
      <div class="meta-card-alert" style="background: rgba(2, 132, 199, 0.08); border-left: 4px solid var(--primary); padding: 1rem; margin-bottom: 1.5rem; border-radius: 6px;">
        <strong style="color: var(--primary);"><i class="fas fa-chalkboard-teacher"></i> 汇报时长与节奏控制指南：</strong>
        本方案严格按照 <strong>20 分钟标准 Journal Club 汇报</strong> 编排（共 15 页核心 Slide）。每页均配备<strong>【视觉呈现与版面设计】</strong>、<strong>【激光笔动作指引】</strong>、<strong>【幻灯片衔接过渡语】</strong>与<strong>【现场汇报逐字讲稿】</strong>。语速建议控制在 220-250 字/分钟，重点图表处适度停顿留白，留出 5-10 分钟导师与评委提问时间。
        <div style="margin-top: 0.85rem; padding-top: 0.75rem; border-top: 1px dashed rgba(2, 132, 199, 0.3); display: flex; flex-wrap: wrap; gap: 0.75rem; align-items: center;">
          <a href="SCN_CCK_Circadian_Clock_Journal_Club.pptx" download style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--primary); color: #fff; padding: 0.45rem 0.9rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem; text-decoration: none;">
            <i class="fas fa-download"></i> 一键下载 16:9 完整 PPTX 演示文稿 (含高清图与演说者讲稿备注)
          </a>
          <a href="JOURNAL_CLUB_DEFENSE_CHEATSHEET.md" target="_blank" style="display: inline-flex; align-items: center; gap: 0.5rem; background: rgba(217, 119, 6, 0.1); color: #d97706; border: 1px solid #d97706; padding: 0.45rem 0.9rem; border-radius: 6px; font-weight: 600; font-size: 0.85rem; text-decoration: none;">
            <i class="fas fa-shield-alt"></i> 查看答辩防身卡片 (10大高难度攻防)
          </a>
        </div>
      </div>

      <div class="presentation-deck" style="display: flex; flex-direction: column; gap: 2rem;">

        <!-- Slide 01 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 01 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">封面与论文背景概览 (Title & Overview)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：00:00 - 01:15</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>主视觉：</strong>左侧放置《Neuron》当期封面或 SCN 脑区解剖定位示意图；右侧展示论文中英文标题、作者列表与通讯作者（严军研究员，中科院脑智卓越中心）。</li>
              <li><strong>核心要素：</strong>突出关键词 <em>Cholecystokinin (CCK)</em>、<em>Suprachiasmatic Nucleus (SCN)</em>、<em>Circadian Clock</em>、<em>Robustness</em>。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑首先指向投影中央的论文主标题，特别是圈出 <strong>“Robustness”</strong>（稳健性）一词；随后移动至右下角的通讯作者严军研究员姓名与单位 Logo，向评审专家及在场师生示意。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “各位老师、各位同仁上午好！今天我非常荣幸能向大家分享中国科学院脑科学与智能技术卓越创新中心严军研究组最新发表在《Neuron》上的重要工作。这项研究回答了一个长期困扰昼夜节律领域的根本悖论——生物钟是如何在‘坚不可摧的稳定性’与‘灵活应变的重置能力’之间维持精妙平衡的？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (00:00 - 01:15)】</strong><br>
            各位老师、评委、同学们，大家上午好。今天我为大家汇报的文献题目是：《小鼠视交叉上核胆囊收缩素神经元调控生物钟的稳健性》（<em>Cholecystokinin neurons in mouse suprachiasmatic nucleus regulate the robustness of circadian clock</em>）。本篇论文于 2023 年发表于神经科学顶级期刊《Neuron》，由中科院脑科学与智能技术卓越创新中心（神经科学研究所）严军研究员领衔完成，第一作者为解鹏博士与张定峰博士。<br>
            大家知道，视交叉上核（SCN）是调控哺乳动物几乎所有昼夜生理与行为的‘中枢起搏器’。然而，一个由数万个神经元构成的复杂网络，究竟凭借怎样的回路设计，才能既日复一日抵抗内部生化噪声的干扰，又能在跨越时区时灵活适应外界授时因子的重塑？严军课题组通过这篇论文，首次揭示了 SCN 内部由胆囊收缩素（CCK）神经元构成的‘负反馈制动与阻尼刹车系统’。接下来，我将从核心科学问题、实验验证体系到理论物理建模，为大家全面解析这项突破性成果。
          </div>
        </div>

        <!-- Slide 02 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 02 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">核心科学问题：生物钟“稳健性与可塑性”的权衡悖论 (The Trade-off Paradox)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：01:15 - 02:30</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左半屏（稳健性 Robustness）：</strong>展示 TTFL 转录翻译负反馈环路与内源性生化随机波动；标出“抵御噪声、维持精准 24 小时自主周期、防止相位散乱”。</li>
              <li><strong>右半屏（可塑性 Plasticity）：</strong>展示日照季节变化、跨时区飞行（Jetlag）引起的光重夹带（Entrainment）；标出“快速响应外界授时信号、相位移动能力”。</li>
              <li><strong>中央天平与疑问：</strong>两端不可兼得的天平模型，打上红色问号：“SCN 神经元网络如何在分子与回路水平设置动态‘缓冲阻尼’，避免时钟失控？”</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑由左向右横扫，先在左侧的 TTFL 环路上划出圆圈，说明细胞内部的脆弱性；随后移至右侧天平右端的光照图标，在中央红色的问号处快速双击抖动，强调这一两难选择正是本领域的百年经典谜题。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “理解了这一两难悖论，我们自然会追问：大自然究竟进化出了怎样的具体神经元群体与分子递质，来充当这个系统的‘减震器’？严军团队将目光锁定在了此前鲜为人知的 CCK 神经元上。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (01:15 - 02:30)】</strong><br>
            首先，请允许我向大家剖析本课题面临的核心科学痛点。在昼夜节律理论中，有一个著名的基本矛盾——<strong>稳健性与可塑性的权衡（Trade-off）</strong>。<br>
            一方面，单个细胞内的转录翻译负反馈回路（TTFL）本质上是非常脆弱的，极易受到基因转录涨落、胞内热噪声与代谢波动的干扰。但哺乳动物 SCN 作为一个由两万个神经元构成的多细胞网络，却展现出了惊人的稳健性——即使在全黑暗（DD）环境下数月，小鼠依然保持着近乎恒定的自发节律。以往研究认为，这依赖于腹外侧腹侧核心区 VIP 和背内侧外壳区 AVP 等神经肽构成的强正向耦合。<br>
            但另一方面，生物体绝不能生活在绝对刚性的象牙塔里。无论是季节更替导致的日照长短变化，还是人类跨越时区引发的时差，都需要生物钟快速进行相位重置（Phase Resetting）。然而，如果网络正向耦合过于强大，时钟就会变得极其‘迟钝’，难以响应外界光照调整；反之，若网络耦合过弱，微弱的随机闪光就会导致整个系统节律崩溃。这就提出一个关键假说：SCN 内部必须存在一个具有负反馈作用的‘阻尼刹车机制’。那么，究竟是谁在扮演这个减震刹车的关键角色？
          </div>
        </div>

        <!-- Slide 03 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 03 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">研究假设与多层级技术路线架构 (Pipeline & Strategy)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：02:30 - 03:45</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>假说框：</strong>SCN 腹外侧多肽 CCK 神经元作为网络阻尼器，在夜间活跃并制动光致相位漂移。</li>
              <li><strong>四阶验证金字塔图：</strong>
                <br>1. <strong>体内节律追踪：</strong>光纤记录 GCaMP 游离钙信号（Figure 1）；
                <br>2. <strong>必要性遗传操纵：</strong>taiep 突变体与 AAV-taCasp3 细胞靶向消融（Figure 2）；
                <br>3. <strong>突触与分子机制：</strong>光遗传学抵消光延迟（Figure 3）+ 脑片膜片钳与发光成像解析 CCK-B 受体（Figure 4）；
                <br>4. <strong>网络相干性与行为转化：</strong>单细胞 Per2-luc 成像（Figure 5）+ 8小时时差模型与两群体 Kuramoto 理论物理分岔模型（Figure 6）。
              </li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑由上至下沿四层金字塔逐级滑动：“活体记录” -> “行为缺失” -> “微回路机制” -> “理论与时差闭环”，在“单细胞发光成像与理论物理模型”处做回旋停留，展现技术方案的系统性。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “好，技术路线已经清晰。我们首先进入第一个实验事实：在活体小鼠的大脑中，SCN CCK 神经元究竟何时处于活动状态？它与传统的节律神经元有何不同？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (02:30 - 03:45)】</strong><br>
            基于这一理论痛点，严军团队提出了明确的科学假说：在 SCN 中占比较小、但在腹外侧有特定富集的胆囊收缩素（CCK）阳性神经元，正是承担网络阻尼刹车功能的关键枢纽。<br>
            为了全面验证这一假说，作者设计了一套跨越宏观到微观、连接实验生物学与理论物理学的四阶技术路线：<br>
            第一阶，利用体内光纤记录（Fiber Photometry），实时追踪自由活动小鼠 SCN CCK 神经元的钙活动昼夜节律；<br>
            第二阶，利用自发基因突变株（taiep）以及 Cre 依赖的病毒诱导细胞凋亡（AAV-flex-taCasp3），在活体行为层面上检验敲除该神经元对生物钟自由运行周期的直接影响；<br>
            第三阶，利用光遗传学（ChR2）与电生理膜片钳，在突触和受体亚型水平上破解 CCK 如何抑制神经元兴奋性并引发 PER2 蛋白相位提前；<br>
            第四阶，结合单细胞超高灵敏生物发光延时成像与非线性动力学两群体 Kuramoto 数学模型，在网络相干性与时差（Jetlag）行为学上实现全方位的假说闭环。这套体系逻辑极其缜密，下面我们逐一拆解。
          </div>
        </div>

        <!-- Slide 04 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 04 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 1: SCN CCK 神经元具有独特的夜间体内钙活动高峰 (Nocturnal Peak)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：03:45 - 05:00</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 1A-C）：</strong>病毒注射策略（AAV-DIO-GCaMP6s 注入 Cck-Cre 小鼠 SCN）及光纤埋植示意；展示小鼠在 12:12 LD 周期与持续全黑暗（DD）下的 24 小时连续钙信号波形。</li>
              <li><strong>右图（Figure 1D-G）：</strong>钙信号峰值时相雷达图。对比 VIP 神经元（日间 ZT4-ZT6 高峰）与 CCK 神经元（主观夜晚 CT16-CT18 高峰）的反相分布。</li>
              <li><strong>核心结论小结：</strong>CCK 神经元打破了 SCN 神经元白天普遍高放电的传统认知，表现为夜间特异性活化。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            激光笔沿着波形图的时间轴移动，在右侧灰色阴影区域（ZT12-ZT24 夜晚时段）画出波浪形轨迹，重点指向位于 CT16 附近的钙尖峰；再移向右下角雷达图，对比 VIP 与 CCK 箭头 180 度的相位相反朝向。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “在生物学中，表达时相往往预示着生理功能。既然 CCK 神经元只在夜晚达到放电顶峰，那么如果我们通过遗传学手段将它们彻底破坏，小鼠的自主生物钟节律会发生什么呢？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (03:45 - 05:00)】</strong><br>
            请大家看 Figure 1。这是整篇工作的立论基石。<br>
            作者首先在 <em>Cck-Cre</em> 小鼠的 SCN 立体定位注射 Cre 依赖表达钙敏感荧光蛋白的 AAV-DIO-GCaMP6s，并植入光纤进行长期监测。众所周知，SCN 中的经典神经元，无论是负责光信号输入的 VIP 神经元，还是主导节律输出的 AVP 神经元，其放电与胞内钙信号的高峰全部集中在<strong>主观白天</strong>（Subjective Day）。<br>
            然而，Figure 1C 和 1D 给出了令人惊讶的结果：SCN CCK 神经元在白天放电平缓，而一旦进入夜晚（无论是 LD 还是全暗 DD 条件），其钙活动显著抬升，在主观夜晚的 <strong>CT16 到 CT18 达到明显峰值</strong>！<br>
            右侧雷达图（Figure 1G）非常直观地展现了这一点：CCK 神经元的钙节律相位与 VIP 神经元几乎完全正交、呈反相排列（Antiphase）。这一发现极其反常，却极其关键——因为在小鼠的生物钟特性中，夜间正是光线能够诱发强烈相位重置（Phase Shift）的敏感窗口期。CCK 神经元在夜间的活跃，预示着它可能扮演着专门在夜间‘站岗放哨’的调控角色。
          </div>
        </div>

        <!-- Slide 05 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 05 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 2: 遗传消融 CCK 神经元导致自主节律失稳与振幅衰减 (Loss of Robustness)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：05:00 - 06:15</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 2A-C）：</strong>经典自发髓鞘病变小鼠 <em>taiep</em>（具有 CCK 表达缺陷）转轮行为记纹图（Actogram），展现日间变异度增加。</li>
              <li><strong>中图（Figure 2D-F）：</strong>AAV-flex-taCasp3 立体定位注射消除 CCK 神经元；对照组 vs 消融组小鼠自由运行周期（DD条件）跑轮 Actogram。</li>
              <li><strong>右图（Figure 2G-H）：</strong>统计柱状图：展示消融后每日活动起始点（Onset）标准差显著升高，节律能量（Power amplitude）大幅衰减。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            将激光笔对准 Figure 2E 消融组小鼠在 DD 条件下的跑轮图，沿着每天活动起始点垂直向下画一条抖动的波浪线，并与对照组笔直的斜线做对比；随后点按 Figure 2H 的振幅衰减统计柱状图（p < 0.001）。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “表型非常明确：缺乏 CCK 神经元后，生物钟虽然还能跑，但变得极其散乱且‘虚弱’。那么，如果我们人为增强它的功能，直接激活 CCK 神经元，能否阻止外界强光引起的节律突变呢？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (05:00 - 06:15)】</strong><br>
            接下来我们看 Figure 2，作者利用行为学手段检验了 CCK 神经元的<strong>功能必要性</strong>。<br>
            首先，作者分析了 <em>taiep</em> 突变小鼠。这种突变会导致 CCK 神经元功能受损，行为学显示其自由运行周期不稳定。为了排除全身性突变对发育和其它脑区的干扰，作者采用了极为特异的手术手段：向成年 <em>Cck-Cre</em> 小鼠 SCN 双侧微量注射表达转基因凋亡酶的 <strong>AAV-flex-taCasp3</strong>，精准消融 SCN 内部的 CCK 神经元，对照组注射 mCherry。<br>
            大家看 Figure 2E 的双重绘图 Actogram：在最初的 12:12 光暗周期中，小鼠尚能跟上外界明暗交替；然而，一旦将环境切换到没有任何时间线索的全黑暗（DD）下，对照组小鼠（左图）保持着笔直、整齐且紧凑的自发活动周期（约 23.8 小时）；但消融了 CCK 神经元的小鼠（中图），每日活动的起始点发生了严重的散乱漂移，呈现显著的‘毛刺化’。<br>
            量化统计（Figure 2G-H）进一步证实：消融组每日起跑时间的变异系数（Variability）翻倍，利用卡方周期图谱分析计算的节律振幅（Circadian Power）衰减了近 40%。这强有力地证明：<strong>SCN CCK 神经元并非决定节律‘有或无’的核心振荡器，而是维持节律‘稳健性与高振幅’不可或缺的稳态调节器</strong>。
          </div>
        </div>

        <!-- Slide 06 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 06 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 3: 光遗传激活 CCK 神经元特异性抵消光致相位延迟 (Canceling Light Delay)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：06:15 - 07:30</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 3A-B）：</strong>光遗传学范式设计（AAV-DIO-ChR2-mCherry 注入 SCN）及 CT14 时段 15 分钟光脉冲刺激；单独光脉冲诱发行为节律大幅向后延迟（Phase delay ~2.5小时）。</li>
              <li><strong>中图（Figure 3C）：</strong>在给予光脉冲的同时，通过蓝光光纤特异性激活 CCK 神经元；跑轮节律延迟被完全‘拉回’甚至消失。</li>
              <li><strong>右图（Figure 3D-E）：</strong>相位改变统计量化柱状图与相位响应曲线（PRC）校正图；明确 CCK 激活具有特异性的‘抗延迟制动效应’。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑由图 3B 移至 3C：首先圈出单独光照下向右下方平移的跑轮红色虚线，指出约 2.5 小时的严重延迟；随后猛然移至图 3C，重点画圈指出在激活 CCK 神经元后，原本向右偏折的虚线竟恢复笔直直下，直观展现‘刹车制动’效果。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “在活体行为上，激活 CCK 神经元能够完美抵消光诱导的相位延迟。那么在微观回路与分子层面上，CCK 究竟是如何给其它生物钟神经元踩下刹车的？我们来看 Figure 4 的细胞与电生理机制。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (06:15 - 07:30)】</strong><br>
            请看 Figure 3。作者在此设计了一个堪称教科书级别的心思缜密的实验。<br>
            在昼夜节律生理学中，主观夜晚的早期（CT14）是一个极为敏感的时间节点——此时外界环境出现光脉冲，小鼠生物钟会发生强烈的<strong>相位延迟（Phase Delay）</strong>，这对应于向西跨时区飞行时身体顺延时间。如图 3B 所示，对照小鼠在 CT14 接受 15 分钟白光脉冲后，其活动节律向后推迟了大约 2.5 个小时。<br>
            但是，作者在小鼠 SCN CCK 神经元中表达了光敏蛋白 ChR2。当在给予外界光照的同时，通过植入的光纤给予 20Hz 蓝光脉冲特异激活 CCK 神经元时，奇迹发生了（Figure 3C）：光脉冲诱发的大幅相位延迟被<strong>完全抵消（Canceling Effect）</strong>！统计柱状图（Figure 3D）清晰显示，这种激活不仅抹平了延迟，甚至在部分小鼠中诱导了轻微的相位前移。<br>
            这就向我们确凿地证明：CCK 神经元的激活在小鼠体内产生了一种反向的‘拉拽力’，能够强力阻尼并中和外界光信号对中央起搏器的冲击，起到了生理‘安全带’和‘减震阻尼器’的作用。
          </div>
        </div>

        <!-- Slide 07 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 07 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 4A-D: CCK 抑制突触后放电并诱发 PER2 发光相位提前 (Postsynaptic Inhibition)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：07:30 - 08:45</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 4A-B）：</strong>离体 SCN 脑片全细胞膜片钳记录（Whole-cell patch-clamp）；加入外源 CCK-8S 神经肽后突触后神经元膜电位超极化（Hyperpolarization）与动作电位放电频率骤降的原始电生理轨迹。</li>
              <li><strong>右图（Figure 4C-D）：</strong>PER2::LUC 报告基因发光记录系统；在 CT14 时段给予 CCK-8S 脉冲刺激，导致发光峰值相位显著向前偏移（Phase Advance ~1.8小时）。</li>
              <li><strong>机制提炼：</strong>CCK 在电生理上起到‘抑制性制动’，在分子钟机制上诱发‘相位提前’，恰与光照引起的‘兴奋+延迟’形成镜像拮抗。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            激光笔先指向左侧膜电位迹线（Figure 4B），在加入 CCK 的瞬间画线，指出密集的动作电位瞬间归零、基线向下塌陷；随后快速移向右侧 PER2 发光拟合曲线，对比虚线（对照）与实线（CCK），展示峰值向左侧的时间提前。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “电生理抑制与分子相位提前的现象明确了。但在药理学上，CCK 在中枢神经系统作用于两种 G 蛋白偶联受体——CCK-A 与 CCK-B。具体是哪一种受体在介导这一关键效应？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (07:30 - 08:45)】</strong><br>
            在 Figure 4 中，作者深入微观细胞与分子机制，回答了‘CCK 如何实施制动’这一核心问题。<br>
            首先看电生理学证据（Figure 4A-B）：作者利用急性 SCN 脑片进行全细胞膜片钳记录。当在灌流液中加入生理活性八肽胆囊收缩素（CCK-8S）时，绝大多数突触后 SCN 神经元发生了迅速的<strong>膜超极化</strong>，自发动作电位放电频率出现断崖式下跌，表明 CCK 对突触后网络行使的是强烈的抑制效应。<br>
            更令人兴奋的是分子节律层面的发现（Figure 4C-D）：作者采用表达周期蛋白 PER2::LUC 荧光素酶报告基因的小鼠脑片，利用光度计进行长达数天的实时生物发光记录。在主观夜间（CT14）给予外源 CCK 脉冲处理，诱发了 PER2 表达节律的显著<strong>相位提前（Phase Advance）</strong>，提前量达 1.5 到 2 小时。<br>
            大家请注意这一机制的精妙对偶性：夜间光脉冲会引起突触后神经元去极化高频放电并导致节律‘延迟’；而 CCK 释放却引起超极化静息并诱导节律‘提前’！这就揭示了 CCK 抵消光延迟的本质——<strong>它在突触后电活动与分子钟蛋白两个尺度上，同时施加了与光输入方向完全相反的代偿性拉拽</strong>。
          </div>
        </div>

        <!-- Slide 08 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 08 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 4E-H: CCK-B 受体介导相位重塑并可被拮抗剂完全消除 (CCKBR Mediation)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：08:45 - 10:00</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 4E-F）：</strong>SCN 中 CCK 受体表达检测；原位杂交显示 CCK-B 受体（<em>Cckbr</em>）广泛高表达于 SCN 腹侧与背侧。</li>
              <li><strong>中图（Figure 4G）：</strong>药理学剖析：CCK-A 受体拮抗剂 Devazepide 处理 vs CCK-B 受体特异性拮抗剂 CI-988（L-365,260）处理。</li>
              <li><strong>右图（Figure 4H）：</strong>PER2::LUC 相位变化量化；CI-988 预处理完全消除 CCK 引起的相位前移，而 Devazepide 毫无阻断效果。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑首先指向图 4E 中高密度的 <em>Cckbr</em> 表达荧光杂交点；随后跳跃至图 4H 的定量统计柱状图，在 CI-988 + CCK 柱状条（高度完全压制归零至 Baseline）上做点按圈选，强调排他性的特异性阻断。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “既然 CCK 通过 CCK-B 受体抑制突触后放电并重排单神经元相位，那么当在成百上千个神经元构成的全局网络中，缺乏 CCK 会导致整个组织产生何种微观病理？我们必须进入单细胞生物发光成像的宏大视野。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (08:45 - 10:00)】</strong><br>
            明确了 CCK 的表型效应后，作者进一步利用受体特异性拮抗剂进行了严密的药理学剖析（Figure 4E-H）。<br>
            哺乳动物大脑中存在两种 CCK 受体：CCK-A（主要分布在外周消化道及少数中枢核团）与 CCK-B（脑内最丰富的主型受体）。原位杂交实验（Figure 4E）表明，在 SCN 内部，<em>Cckbr</em> 受体 mRNA 呈现弥漫性高丰度表达，几乎覆盖了绝大部分振荡神经元。<br>
            为了验证是否完全由 CCK-B 受体介导，作者进行了严密的双拮抗剂对照筛选（Figure 4G-H）：<br>
            加入 CCK-A 受体选择性拮抗剂 Devazepide，CCK 诱导的突触后放电抑制与 PER2 相位前移丝毫未受影响；<br>
            然而，一旦加入 CCK-B 受体特异性拮抗剂 <strong>CI-988</strong>（或 L-365,260），CCK 诱导的电生理超极化被 100% 阻断，PER2::LUC 的相位提前也被彻底抹平！<br>
            这一关键实验不仅闭环了受体特异性分子机制，更提供了一个至关重要的转化医学启示：<strong>如果我们使用能够透过血脑屏障的 CCK-B 受体小分子拮抗剂，是否就能够人为关闭这个‘刹车’，从而达到干预生物钟的目的？</strong>这一推论为后文的时差实验埋下了精妙的伏笔。
          </div>
        </div>

        <!-- Slide 09 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 09 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 5A-D: 单细胞发光网络成像：消融导致振荡器发散与去同步化 (Desynchronization)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：10:00 - 11:15</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 5A）：</strong>高灵敏度低温 EMCCD 单细胞生物发光成像系统（Single-cell PER2::LUC imaging），追踪 SCN 脑片中数百个独立神经元空间 ROI。</li>
              <li><strong>中图（Figure 5B）：</strong>极坐标相位玫瑰图与单细胞相位时空热图对比；对照组神经元相位整齐划一，消融组神经元相位各向发散。</li>
              <li><strong>右图（Figure 5C-D）：</strong>量化相干性物理参数——Kuramoto 秩序参量（Order Parameter R）；消融组 R 值随时间由 0.85 锐减至 0.35 以下。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑在图 5B 的极坐标图上做对比：先圈出对照组紧密抱团、指向一致的红色箭头束；接着移至右侧消融组散布在 360 度圆周上的杂乱箭头，形象地比喻为‘交响乐团失控’；最后在图 5D 下滑的 R 曲线处重重一点。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “单细胞成像揭示了令人震惊的事实：原来小鼠行为节律的衰减，微观根源在于上千个振荡器失去了协调同步。那么，这一去同步化过程是不可逆的吗？外源补充 CCK 能否将散乱的乐队重新凝聚？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (10:00 - 11:15)】</strong><br>
            请看 Figure 5A-D。如果说前面的实验是宏观和微观的切片，那么这部分则是整篇工作在<strong>复杂生物网络动力学</strong>上的核心高潮。<br>
            大家知道，以前很多研究只能测量整个脑片的总体发光，这往往掩盖了单个细胞的异质性。作者在此动用了业界顶尖的高分辨 EMCCD 单细胞荧光素酶成像平台，对对照组和 CCK 消融小鼠的 SCN 脑片进行长达 5 天的逐秒单细胞延时拍摄，提取出数百个独立振荡神经元的相位迹线。<br>
            大家看 Figure 5B 的极坐标玫瑰图：在正常对照组中，几百个神经元就像一支训练有素的交响乐团，每个细胞都以极其严格的一致性在相同时间达到峰值，系统呈现出高度的全局相干性；<br>
            然而，在利用 Caspase3 消融 CCK 神经元的脑片中，单个细胞本身的自主节律并没有死掉，但它们彼此之间的相位发生了严重的<strong>发散与去同步化（Desynchronization）</strong>！有的在中午达到顶峰，有的在半夜达到顶峰，彼此抵消。<br>
            作者引入了统计物理学中描述振荡相干性的经典参量——<strong>Kuramoto 秩序参数（Order Parameter R）</strong>。R=1 代表绝对同步，R=0 代表完全无序。统计显示（Figure 5D），消融组的 R 值从正常的 0.85 断崖式下跌到 0.4 以下。这从微观网络层面彻底解释了 Figure 2 中小鼠行为节律振幅衰减的深层本质。
          </div>
        </div>

        <!-- Slide 10 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 10 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 5E-H: 外源 CCK 逆转去同步化并重塑全局网络相干性 (Network Resynchronization)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：11:15 - 12:30</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 5E）：</strong>实验方案：对去同步化的 SCN 脑片加入脉冲式外源性 CCK-8S（Rescue 拯救实验）。</li>
              <li><strong>中图（Figure 5F-G）：</strong>单细胞发光相位热图动态演变；原本散乱的横向色带在加入 CCK 后被迅速‘拉齐’，重新建立同步波纹。</li>
              <li><strong>右图（Figure 5H）：</strong>Kuramoto 秩序参数 R 值的反弹恢复折线图；R 值由 0.38 强劲回升至 0.78 以上。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑紧跟图 5F 中标注的加入 CCK 虚线竖线，用激光笔水平划过所有单细胞轨道，展示杂乱无章的色斑在虚线后迅速对齐为垂直整齐条带的惊人过程；最后指向图 5H 中强势 V 字反弹的 R 值曲线。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “至此，充分性与必要性已全面闭环！但严军研究组并没有止步于离体网络机制。他们提出了一个最具现实意义、最引人入胜的转化问题：如果消融 CCK 卸掉了生物钟的‘刹车’，小鼠倒时差会发生什么奇迹？”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (11:15 - 12:30)】</strong><br>
            请看 Figure 5E-H。严谨的生物学证明讲求‘有破坏就必须有拯救’。<br>
            为了无可辩驳地证明正是缺乏 CCK 导致了网络去同步化，作者进行了一项极其惊艳的 Rescue 挽救实验：他们在这些已经完全去同步化、秩序参量跌入低谷的 SCN 脑片培养基中，给予短暂的脉冲式外源 CCK-8S 处理。<br>
            大家看 Figure 5F 的单细胞动态相图：在施加 CCK 之前，各通道的单细胞相位如同一盘散沙；然而就在加入 CCK 的瞬间，原本各自行事的数百个细胞被强行统一‘重置’，在接下来的几个周期内，混乱的色带迅速重新对齐成了规律清晰、步调一致的纵向条带！<br>
            量化统计（Figure 5H）更是直观：系统的 Kuramoto 秩序参数 R 呈现出强劲的 V 字型反弹，从 0.38 一路攀升恢复至 0.78，几乎达到了野生型的相干性水平。<br>
            这个挽救实验彻底夯实了 CCK 的分子地位：<strong>CCK 不仅是单个神经元的抑制剂，它更是一种全网络级的‘相位对齐与相干重塑因子’，负责在夜间把偏离轨道的离散细胞牢牢拉回正轨</strong>。
          </div>
        </div>

        <!-- Slide 11 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 11 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 6A-D: CCK 神经元消融显著加速小鼠对时差的重夹带 (Accelerated Jetlag Re-entrainment)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：12:30 - 13:45</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 6A）：</strong>急进性时差范式示意：光照周期突然提前 8 小时（+8h Phase Advance，模拟由西向东跨越 8 个时区的高难度时差）。</li>
              <li><strong>中图（Figure 6B-C）：</strong>跑轮行为 Actogram 对比：对照小鼠（重夹带极其缓慢，出现长期时相解偶联） vs CCK 神经元消融小鼠（迅速同步对齐）。</li>
              <li><strong>右图（Figure 6D）：</strong>完全重夹带所需天数统计柱状图：对照组需要 8.6 ± 0.5 天，而 CCK 消融小鼠仅需 4.3 ± 0.4 天，适应速度整整加快了一倍！</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑由图 6B 的第 0 天时差突变线向下移动：在对照组跑轮图中划出一条漫长缓慢倾斜的爬坡虚线（历经 8-9 天）；随后猛地移至消融组跑轮图，划出一条角度极其陡峭、仅用 4 天就完全咬合新光照周期的直线，并在右侧统计图的 p &lt; 0.0001 显著性星号上快速画圈。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “表型极其震撼——把刹车拆掉，小鼠倒时差竟然快了一倍！但是，作为严谨的科学探索，作者没有满足于现象描述。他们提出了更深层的理论物理问题：为什么破坏内部耦合，反而能提高对外界驱动的适应速度？我们来看两群体 Kuramoto 数学模型的精彩推演。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (12:30 - 13:45)】</strong><br>
            请大家聚焦 Figure 6A-D。这是本篇论文在行为学与转化医学上最引人瞩目的突破性发现。<br>
            在实际生活中，跨时区旅行导致的‘时差反应（Jetlag）’是困扰现代人类的一大顽疾，尤其是<strong>向东飞行（Phase Advance 相位提前）</strong>，倒时差最为痛苦而漫长。作者模拟了最严苛的 +8 小时东向飞行时差范式（例如从伦敦飞往北京）。<br>
            大家看 Figure 6B 的双重绘图记纹图：对照组小鼠面临突发的 8 小时光照提前，表现出非常典型的‘重夹带惯性’——每天只能微调大约 1 个小时，平均需要长达 <strong>8.6 天</strong>才能让自己的活动节奏完全与新的光暗周期对齐；<br>
            然而，奇迹发生在消融了 SCN CCK 神经元的小鼠身上：由于失去了夜间 CCK 对相位的负向制动，这些小鼠每天可以实现 2 小时以上的跳跃式相位移动，仅仅用了 <strong>4.3 天</strong>就彻底完成了时差重夹带，耗时缩短了整整一半（Figure 6D）！<br>
            这个看似‘反常识’的结果，完美印证了作者最初的假说：<strong>CCK 神经元在正常小鼠体内就是一副死死踩住的刹车片。它限制了生物钟对突发授时信号的随波逐流，维持了系统的刚性稳健；而一旦解除了这道刹车，生物钟的可塑性便被彻底释放，使机体能以极高速度适应全新的时间环境</strong>！
          </div>
        </div>

        <!-- Slide 12 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 12 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">Figure 6E-H: 基于两群体 Kuramoto 模型的动力学分岔解析 (Theoretical Bifurcation Analysis)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：13:45 - 15:00</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>左图（Figure 6E）：</strong>两群体耦合 Kuramoto 模型架构：腹外侧群体（接收光输入与 CCK 介导的负反馈）与背内侧群体（维持自主节律）之间的耦合常数矩阵。</li>
              <li><strong>中图（Figure 6F）：</strong>系统分岔相图（Phase Diagram）：展示在不同耦合强度 K 下，系统跨越临界点产生鞍结分岔（Saddle-node bifurcation）的相空间轨迹。</li>
              <li><strong>右图（Figure 6G-H）：</strong>计算机数值模拟（Simulation）与小鼠实验实测（Empirical Data）重夹带曲线的高度拟合叠加对比。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑指向图 6E 的两群体耦合拓扑结构，强调 CCK 提供的内部负耦合权重；接着平移至图 6F 相图中的分岔临界线，解释消融 CCK 相当于将参数从高耦合稳态区平移到了临界加速区；最后在图 6H 理论曲线与实验散点几乎重合的轨迹上横向划过。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “实验现象与理论物理模型在此达成了完美的统一！现在，我们可以把全篇论文所有的实验拼图，拼接成一个宏大而精致的生物钟神经微回路工作模型。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (13:45 - 15:00)】</strong><br>
            在 Figure 6E-H 中，作为理论计算生物学见长的研究组，严军团队展现了其高超的数理建模功底。<br>
            为什么消融一个神经元群体反而会‘优化’适应速度？作者将 SCN 抽象为腹侧核心区（Core）与背侧外壳区（Shell）两个相互耦合的非线性振荡子群体，建立了<strong>拓展的两群体 Kuramoto 相位动力学微分方程</strong>。<br>
            在这个模型中，CCK 神经元被形式化为一个赋予系统内部强阻尼的非线性负耦合项。在正常状态下（野生型），内部的高耦合强度构建了一个高耸的‘势能能垒’（Energy barrier），使系统紧紧锁定在原有的相位引力阱中，外界光照每次只能将其微弱推动一步；<br>
            而消融 CCK 神经元，在物理上等价于<strong>降低了网络内部的相互作用阻尼能垒</strong>。如 Figure 6F 的动力学相图所示，随着耦合强度的削弱，系统逼近了鞍结分岔临界点，使得外界光强驱动更容易诱发相位的快速滑动。<br>
            最令人叹为观止的是 Figure 6H：完全基于理论物理模型计算得出的重夹带动力学轨迹（绿色实线），与我们在跑轮箱里实测的小鼠行为学数据（红色散点）呈现出了几乎完美的重合！这赋予了这项生物学发现极其罕见而坚实的理论数理支撑。
          </div>
        </div>

        <!-- Slide 13 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--primary); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 13 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">总结与核心工作模型：CCK 神经元作为生物钟的“分子刹车/阻尼器” (Working Model)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：15:00 - 16:30</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--primary);"><i class="fas fa-desktop"></i>【视觉呈现与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>中央核心机制全景图（Figure 7）：</strong>
                <br>&bull; <strong>日间（Daytime）：</strong>VIP/AVP 活跃，CCK 保持静息；生物钟高效输出节律。
                <br>&bull; <strong>夜间（Nighttime）：</strong>CCK 神经元爆发高钙与放电，释放 CCK 神经肽作用于突触后 CCKBR，抑制自发放电，诱导 PER2 相位提前，抵消意外光照诱发的相位延迟。
              </li>
              <li><strong>四点核心结论列表：</strong>
                <br>1. 发现夜间特异放电的 SCN CCK 神经元新亚群；
                <br>2. 证实 CCK 是维持生物钟网络高相干性（R参量）与振幅稳健性的必要要素；
                <br>3. 阐明 CCK-CCKBR 抑制通路作为光重置的‘生理减震阻尼器’；
                <br>4. 确立了调控 CCK 刹车可实现对时差重夹带速度的人为干预。
              </li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            激光笔围绕中央全景图做顺时针回旋，按‘夜间活化’ -> ‘释放CCK’ -> ‘结合CCK-B受体’ -> ‘突触后超极化+PER2提前’ -> ‘稳健性刹车制动’的回路路径有序指示，最后定格在中央加粗的总结关键词上。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “以上是作者呈现给我们的精彩工作与完美故事。然而，作为一名博士研究生，在 Journal Club 汇报中，除了学习优秀工作的亮点，我们更需要带着独立、严苛的审辩式思维（Critical Thinking）去审视其潜在的盲区与局限。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (15:00 - 16:30)】</strong><br>
            各位老师、同学，让我们把上述所有证据汇总到这个最终的核心工作模型中（Figure 7）。<br>
            这项发表在《Neuron》上的重大成果，首次打破了过去认为 SCN 主要是全兴奋、正反馈网络的传统教条，确立了 CCK 神经元作为中枢生物钟<strong>‘分子制动器与网络减震器（Brake & Damper）’</strong>的全新科学范式：<br>
            在白天，CCK 保持沉默，生物钟遵循高频兴奋传导；<br>
            而在主观夜晚，CCK 神经元特异性激活，通过致密核心囊泡向全 SCN 弥散释放 CCK 神经肽，激活广泛分布的 CCK-B 受体。这种激活一方面抑制突触后自发放电，另一方面诱发 PER2 蛋白相位提前，从而巧妙地抵消了外界偶发光线导致的节律延迟。<br>
            这解释了为什么大自然要在体内保留这样一个‘阻碍快速倒时差’的刹车——因为在漫长的自然演化中，野生动物面临的是雷电、闪光或月光等偶发环境噪声，这种强有力的夜间刹车能够确保中央生物钟不会因为偶发的光刺激而陷入灾难性的相位紊乱。这是生命系统在演化历程中锤炼出的极富智慧的稳态权衡。
          </div>
        </div>

        <!-- Slide 14 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: #dc2626; color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 14 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">批判性审视与局限性 (Critical Evaluation, Limitations & Caveats)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：16:30 - 18:00</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: #dc2626;"><i class="fas fa-exclamation-triangle"></i>【博士生高阶思维呈现与版面设计】</strong>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 0.5rem;">
              <div style="background: var(--bg-sidebar); padding: 0.75rem; border-radius: 6px; border-left: 3px solid #dc2626; font-size: 0.88rem;">
                <strong>1. 细胞亚型异质性未穷尽：</strong>泛 <em>Cck-Cre</em> 工具可能混淆共表达 GRP/Nms 的亚群，缺乏单细胞单突触逆行标记。
              </div>
              <div style="background: var(--bg-sidebar); padding: 0.75rem; border-radius: 6px; border-left: 3px solid #f59e0b; font-size: 0.88rem;">
                <strong>2. 离体浴洗与生理释放鸿沟：</strong>微摩尔级 CCK-8S 脑片恒定浸泡可能诱发受体内吞脱敏，不能等同于囊泡脉冲释放动力学。
              </div>
              <div style="background: var(--bg-sidebar); padding: 0.75rem; border-radius: 6px; border-left: 3px solid #0284c7; font-size: 0.88rem;">
                <strong>3. 突触后靶细胞接线未明：</strong>CCKBR 究竟是直接表达在 VIP 神经元上还是通过局部 GABA 能中间神经元间接去抑制？微回路拓扑未闭环。
              </div>
              <div style="background: var(--bg-sidebar); padding: 0.75rem; border-radius: 6px; border-left: 3px solid #7c3aed; font-size: 0.88rem;">
                <strong>4. 夜行性向日行性转化代沟：</strong>小鼠是夜行性动物（Nocturnal），而人类是日行性（Diurnal），灵长类 SCN 中 CCK 表达时相是否存在倒错仍未可知。
              </div>
            </div>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑依次点过四个方块，在第 3 个方块（微回路接线）和第 4 个方块（日行性转化）做重点停留，语调沉稳有力，展现成熟扎实的科研辨析能力。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “发现局限正是科学进步的起点。正是基于这些尚未完全解决的方法学挑战，我们才能够展望出更加激动人心的未来研究方向与临床转化路径。”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (16:30 - 18:00)】</strong><br>
            接下来，我希望能以审辩式的学术眼光，向各位老师汇报我对这篇论文若干局限性（Caveats）的独立思考：<br>
            <strong>第一，是遗传工具特异性与细胞异质性问题。</strong>文章依赖通用的 <em>Cck-Cre</em> 小鼠。但最新空间转录组学表明，SCN 内部多肽神经元高度异质，部分 CCK 神经元可能与 GRP 甚至 Nms 存在微量共表达。当前的消融实验是否误伤了具有其它功能的侧支亚群？这需要未来结合单细胞空间测序与交叉 Cre-Flp 系统做进一步厘清。<br>
            <strong>第二，是离体脑片外源浴洗与体内突触释放的浓度代沟。</strong>Figure 4 中施加的是高浓度（微摩尔级）外源 CCK-8S 恒定灌流。而体内致密核心囊泡的生理释放具有高度的时间脉冲性与空间局域性。长时间高浓度浸泡是否会造成 CCK-B 受体的代偿性内吞脱敏？内源 CCK 的实时释放动力学亟需新型 GRAB 探针在活体内直接监测。<br>
            <strong>第三，是突触后微回路图谱的接线黑盒。</strong>虽然证明了 CCK-B 受体必不可少，但 CCK 到底作用于谁？是直接超极化了 VIP 神经元，还是通过激活局部的抑制性 GABA 中间神经元实现了间接抑制？这种微回路解剖拓扑尚未完全画全。<br>
            <strong>第四，也是最核心的临床转化壁垒——夜行性小鼠向日行性人类的外推风险。</strong>小鼠在夜间活跃，人类在日间活跃。尽管分子时钟核心机制高度保守，但在日行性灵长类动物大脑中，SCN CCK 神经元的放电时相是否也发生反转？直接在人类身上阻断 CCKBR 是否会导致认知迟钝或情绪异常？这些问题论文尚未给出答案。
          </div>
        </div>

        <!-- Slide 15 -->
        <div class="slide-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.5rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-color); padding-bottom: 0.75rem; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
              <span style="background: var(--success); color: white; font-weight: 800; font-size: 0.85rem; padding: 4px 10px; border-radius: 4px;">Slide 15 / 15</span>
              <h3 style="margin: 0; font-size: 1.2rem; color: var(--text-main);">未来展望、转化应用与致谢答辩 (Future Outlook & Q&A)</h3>
            </div>
            <span style="background: var(--bg-sidebar); color: var(--text-muted); font-size: 0.85rem; font-weight: 600; padding: 4px 8px; border-radius: 4px;"><i class="far fa-clock"></i> 建议耗时：18:00 - 20:00</span>
          </div>

          <div style="margin-bottom: 1rem;">
            <strong style="color: var(--success);"><i class="fas fa-lightbulb"></i>【未来发展路线与版面设计】</strong>
            <ul style="margin: 0.5rem 0 0 1.25rem; font-size: 0.92rem; color: var(--text-main); line-height: 1.6;">
              <li><strong>转化应用突破点：</strong>开发兼具高脑血脑屏障穿透性（BBB-penetrant）与短半衰期的新型口服 CCK-B 受体拮抗剂（‘口服抗时差/倒班智能药片’）。</li>
              <li><strong>前沿学术深化：</strong>利用单细胞空间转录组与 Patch-seq 解密靶神经元；在食蟹猴或树鼩等日行性模式动物中检验转化有效性。</li>
              <li><strong>版面底部：</strong>致谢实验室导师、评委专家及课题组成员；醒目展示“诚挚感谢各位老师倾听！恳请批评指正与提问交流（Q&A）”。</li>
            </ul>
          </div>

          <div style="background: rgba(217, 119, 6, 0.08); border-left: 3px solid var(--accent); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--accent);"><i class="fas fa-magic"></i>【激光笔动作指引】</strong><br>
            光斑先指向药物分子小结构图，再移动至日行性非人灵长类图标，最后稳稳关闭激光笔并放在讲台上，面带微笑目视全场评委，微微鞠躬致敬。
          </div>

          <div style="background: rgba(2, 132, 199, 0.06); border-left: 3px solid var(--primary); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong style="color: var(--primary);"><i class="fas fa-random"></i>【幻灯片衔接过渡语】</strong><br>
            “最后，再次向严军研究员及其团队做出的杰出贡献致敬。我的汇报到此结束，非常期待老师和同仁们的提问与指导！”
          </div>

          <div style="background: var(--code-bg); border: 1px solid var(--border-color); padding: 1rem 1.25rem; border-radius: 6px; font-size: 0.92rem; line-height: 1.7;">
            <strong style="color: var(--text-main);"><i class="fas fa-comment-dots"></i>【现场汇报逐字讲稿 (18:00 - 20:00)】</strong><br>
            总结全篇工作，严军团队通过极其优雅扎实的实验设计，不仅从生物物理、神经微回路和理论物理层面，完美诠释了生物钟网络稳健性与可塑性的权衡机制，更为现代社会的健康难题开辟了极具前景的转化道路。<br>
            基于这一发现，一个非常直接且激动人心的应用前景是：开发具有良好中枢穿透性且代谢迅速的<strong>短效 CCK-B 受体拮抗剂</strong>。跨国航班旅客或轮班工作者只需在需要重新校准节律的特定时间窗口服用药物，即可短暂松开大脑中央生物钟的‘刹车片’，加速重置并迅速适应全新作息，随后药物被迅速代谢清除，恢复系统正常的抗噪声稳健性。<br>
            未来，结合高通量空间单细胞测序、新型神经肽荧光传感器以及非人灵长类模型，我们将能进一步打通从啮齿类机理到人类临床转化的最后一道屏障。<br>
            最后，衷心感谢我的指导老师、评委老师以及在座各位同仁的耐心聆听！由于水平有限，汇报中难免有理解不当之处，热切期待各位老师的批评、指正与提问。谢谢大家！
          </div>
        </div>

      </div>
    </div>

  </div>
</section>
"""
