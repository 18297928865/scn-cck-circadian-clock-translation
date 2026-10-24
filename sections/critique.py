# -*- coding: utf-8 -*-

CRITIQUE_HTML = """
<section id="critique-section" class="section-card critique-section">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">11</span> 论文局限性、方法学考量与批判性思考 (Critiques, Caveats & Limitations)</h2>
    <p class="section-subtitle">展现博士生独立学术审辩思维（Critical Thinking）的核心模块：解析实验盲区、方法局限与未来突破口</p>
  </div>

  <div class="trans-content">
    
    <div class="seminar-block">
      <div class="meta-card-alert" style="background: rgba(239, 68, 68, 0.08); border-left: 4px solid #ef4444; padding: 1rem; margin-bottom: 1.5rem; border-radius: 6px;">
        <strong style="color: #ef4444;"><i class="fas fa-exclamation-triangle"></i> 导师汇报加分秘籍：</strong>
        在学术期刊俱乐部（Journal Club）中，优秀的汇报绝不仅是对论文的复述和盲目背书，更重要的是展现<strong>独立审辨式思考（Critical Thinking）</strong>。指出论文在技术手段、实验设计、分子特异性及模型假设上的潜在漏洞，能直接体现您扎实的科研功底与敏锐的洞察力。
      </div>

      <div class="critique-grid" style="display: grid; grid-template-columns: 1fr; gap: 1.5rem;">
        
        <!-- Caveat 1 -->
        <div class="critique-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <h4 style="color: var(--primary); margin: 0; font-size: 1.1rem;"><i class="fas fa-microscope"></i> 局限 1：CCK-Cre 小鼠工具的细胞特异性与 SCN 亚型异质性未被彻底穷尽</h4>
            <span style="background: #fee2e2; color: #dc2626; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">分子与遗传学局限</span>
          </div>
          <p><strong>现状与问题：</strong>本研究所使用的 <em>Cck-Cre</em> 小鼠为通用转基因工具。虽然作者通过立体定位微量注射将病毒局限在 SCN 内部，但近年来单细胞转录组（scRNA-seq）测序表明，SCN 内部的 CCK 神经元群体并非均质单一（homogeneous）。部分 CCK 神经元可能与 GRP（胃泌素释放肽）或 Nms（神经介素S）存在部分共表达重叠。</p>
          <p><strong>潜在漏洞：</strong>利用泛 CCK 启动子驱动的 Cre 酶消融或抑制的是所有 CCK 阳性细胞，是否其中存在微小的亚群（如投射向不同下丘脑亚区的分支）发挥了相反或调节性的作用？目前文章尚未开展单细胞分辨率下的单突触跨亚群逆行追踪。</p>
          <div style="background: var(--code-bg); padding: 0.75rem; border-radius: 6px; font-size: 0.9rem; margin-top: 0.5rem;">
            <strong>答辩/汇报应对语录：</strong>“尽管作者严格控制了病毒注射的解剖体积，但未来若能结合单细胞空间转录组学（Spatial Transcriptomics）对 CCK 阳性细胞进行二级亚群细分（CCK<sup>sub1</sup> vs CCK<sup>sub2</sup>），将能更精准地揭示这一刹车机制的微回路网络架构。”
          </div>
        </div>

        <!-- Caveat 2 -->
        <div class="critique-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <h4 style="color: var(--primary); margin: 0; font-size: 1.1rem;"><i class="fas fa-vial"></i> 局限 2：外源性神经肽浴洗（Bath Application）与突触内源性释放的浓度鸿沟</h4>
            <span style="background: #fef3c7; color: #b45309; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">离体电生理生理学考量</span>
          </div>
          <p><strong>现状与问题：</strong>在验证 CCK 诱发突触后细胞抑制与相位前移的实验中（Figure 4），作者主要在离体脑片浴槽中加入外源合成的八肽胆囊收缩素（CCK-8S，浓度通常在微摩尔级 nM~μM）。</p>
          <p><strong>潜在漏洞：</strong>生理状态下，致密核心囊泡（Dense-core vesicles）释放的神经肽在突触间隙中的浓度、扩散半径及降解动力学（受细胞外肽酶水解速度调控）与全组织恒定浴洗存在显著差异。长时间浸泡高浓度外源肽可能诱发受体内吞（Internalization）或脱敏（Desensitization），不能完全等同于内源神经元以生理脉冲频率放电所释放的多肽效应。</p>
          <div style="background: var(--code-bg); padding: 0.75rem; border-radius: 6px; font-size: 0.9rem; margin-top: 0.5rem;">
            <strong>答辩/汇报应对语录：</strong>“浴洗实验提供了明确的因果充分性证据，但内源性 CCK 释放的动力学特征仍需未来借助新型新型基因编码神经肽荧光探针（如 CCK GRAB 探针）在活体内进行皮秒级的光学监测。”
          </div>
        </div>

        <!-- Caveat 3 -->
        <div class="critique-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <h4 style="color: var(--primary); margin: 0; font-size: 1.1rem;"><i class="fas fa-network-wired"></i> 局限 3：突触后靶细胞类型的受体表达图谱尚未完成单细胞配对</h4>
            <span style="background: #e0f2fe; color: #0369a1; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">回路连接组学未解之谜</span>
          </div>
          <p><strong>现状与问题：</strong>论文阐明了 CCK 神经元通过释放 CCK 作用于突触后受体诱发相位前移，但在 SCN 复杂的微网络中，受体到底分布在哪些具体的细胞上？</p>
          <p><strong>潜在漏洞：</strong>SCN 突触后靶标是 VIP 神经元、AVP 神经元，还是局部的 GABA 能中间神经元？尽管作者利用 CCK-B 受体拮抗剂阻断了效应，但 CCKBR 是直接表达在 VIP 细胞上起超极化作用，还是通过激活中间抑制性中间神经元间接抑制 VIP 神经元？这种微回路接线拓扑结构（Direct vs Polysynaptic Disinhibition）在文中尚未完全剖析清楚。</p>
          <div style="background: var(--code-bg); padding: 0.75rem; border-radius: 6px; font-size: 0.9rem; margin-top: 0.5rem;">
            <strong>答辩/汇报应对语录：</strong>“明确 CCK 受体的下游细胞靶标（例如是直接刹车 VIP，还是通过局部 GABA 中介）是解析 SCN 内部 E/M 振荡器协同偶联的下一个核心科学盲区。”
          </div>
        </div>

        <!-- Caveat 4 -->
        <div class="critique-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <h4 style="color: var(--primary); margin: 0; font-size: 1.1rem;"><i class="fas fa-dna"></i> 局限 4：夜行性小鼠向日行性人类外推的演化鸿沟与时差转化壁垒</h4>
            <span style="background: #fdf4ff; color: #a21caf; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">转化医学与临床外推</span>
          </div>
          <p><strong>现状与问题：</strong>小鼠是典型的夜行性动物（Nocturnal），而人类是日行性动物（Diurnal）。虽然哺乳动物 SCN 的核心分子振荡机制（TTFL）高度保守，但二者在行为输出、甚至部分 SCN 细胞群对光的相位响应曲线上存在显著的倒错（Inversion）或者时相偏移。</p>
          <p><strong>潜在漏洞：</strong>作者在讨论中提出开发 CCKBR 拮抗剂来帮助人类倒时差。但日行性灵长类大脑中 SCN CCK 神经元的空间构型、放电高峰与行为周期的对齐关系是否完全与小鼠一致？在人类中盲目抑制 CCK 是否会带来不可预知的睡眠-觉醒节律紊乱或抗药性？目前仍缺乏非人灵长类（NHP）的验证数据。</p>
          <div style="background: var(--code-bg); padding: 0.75rem; border-radius: 6px; font-size: 0.9rem; margin-top: 0.5rem;">
            <strong>答辩/汇报应对语录：</strong>“从夜行性啮齿类动物向日行性人类的临床转化存在明显的生态演化代沟。在开发抗时差药物前，亟需在树鼩或食蟹猴等日行性模式动物中检验 CCK 神经元的节律动力学。”
          </div>
        </div>

        <!-- Caveat 5 -->
        <div class="critique-card" style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 8px; padding: 1.25rem; box-shadow: var(--shadow-sm);">
          <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
            <h4 style="color: var(--primary); margin: 0; font-size: 1.1rem;"><i class="fas fa-calculator"></i> 局限 5：两群体 Kuramoto 数学模型的简化假设与真实非线性生化系统的差异</h4>
            <span style="background: #ecfdf5; color: #047857; font-size: 0.75rem; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">理论计算生物学假设</span>
          </div>
          <p><strong>现状与问题：</strong>在论文 Figure 6 中，作者建立了一个由两组相位振荡器（Phase oscillators）组成的耦合 Kuramoto 模型，用于模拟 Core 与 Shell 神经元在不同耦合强度下的动力学分岔与稳态。</p>
          <p><strong>潜在漏洞：</strong>Kuramoto 模型本质上是只考虑相位变量的一阶唯象方程，忽略了神经元内部复杂的分子振幅（Amplitude）、多重转录负反馈级联延迟（Delays）以及神经递质/神经肽浓度的非线性饱和动力学。模型能够定性复现行为与矢量场分岔，但对于定量预测真实生物系统的相变临界点存在过度简化的风险。</p>
          <div style="background: var(--code-bg); padding: 0.75rem; border-radius: 6px; font-size: 0.9rem; margin-top: 0.5rem;">
            <strong>答辩/汇报应对语录：</strong>“Kuramoto 模型成功抓住了相干性与稳定性的核心物理本质，但未来应结合包含生化分子细节的 Goodwin 或 Relógio 详细分子模型，构建多尺度物理-生物混合动力学仿真。”
          </div>
        </div>

      </div>
    </div>

  </div>
</section>
"""
