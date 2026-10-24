# -*- coding: utf-8 -*-

META_HTML = """
<header id="meta-info" class="paper-header">
  <div class="journal-badge">
    <span class="badge-tag">Neuron</span>
    <span class="badge-vol">Volume 111, Issue 14, p2201–2217.e4, July 19, 2023</span>
    <span class="badge-doi"><a href="https://doi.org/10.1016/j.neuron.2023.04.016" target="_blank" rel="noopener">DOI: 10.1016/j.neuron.2023.04.016</a></span>
  </div>

  <h1 class="paper-title-cn">小鼠视交叉上核中的胆囊收缩素神经元调控生物钟的稳健性</h1>
  <div class="paper-title-en">Cholecystokinin neurons in mouse suprachiasmatic nucleus regulate the robustness of circadian clock</div>

  <div class="authors-block">
    <div class="author-list">
      <span class="author">谢路成 (Lucheng Xie)<sup>1,2,6</sup></span>,
      <span class="author">熊洋洋 (Yangyang Xiong)<sup>1,2,6</sup></span>,
      <span class="author">马丹怡 (Danyi Ma)<sup>1,6</sup></span>,
      <span class="author">施凯文 (Kaiwen Shi)<sup>1</sup></span>,
      <span class="author">陈赳 (Jiu Chen)<sup>1</sup></span>,
      <span class="author">杨巧巧 (Qiaoqiao Yang)<sup>5</sup></span>,
      <span class="author corr">严军 (Jun Yan)<sup>1,3,4,7,*</sup></span>
    </div>
    <div class="affiliations">
      <p><sup>1</sup> 中国科学院脑科学与智能技术卓越创新中心/神经科学研究所，神经科学国家重点实验室，上海 200031</p>
      <p><sup>2</sup> 中国科学院大学，北京 100049</p>
      <p><sup>3</sup> 上海脑科学与类脑研究中心，上海 201210</p>
      <p><sup>4</sup> 中国科学院大学未来技术学院，北京 101408</p>
      <p><sup>5</sup> 复旦大学附属中山医院神经外科，上海 200032</p>
      <p><sup>6</sup> 共同第一作者； <sup>7</sup> 资深通讯作者 (Lead Contact)</p>
      <p><sup>*</sup> 通讯邮箱：<a href="mailto:junyan@ion.ac.cn">junyan@ion.ac.cn</a></p>
    </div>
  </div>

  <div class="report-meta-box">
    <div class="report-badge"><i class="fas fa-graduation-cap"></i> 博士生学术文献汇报专案</div>
    <div class="report-tip">包含逐字忠实全文翻译（图文对照保留Figure编号）、核心专业词汇解析、图表原位插图与深度图注、新颖点与学术重要性提炼、以及面向答辩的超全背景知识拓展。</div>
  </div>
</header>

<section id="graphical-abstract" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">00</span> 图文摘要与研究要点 (Graphical Abstract & Highlights)</h2>
  </div>

  <div class="figure-container card-figure">
    <div class="figure-image-box">
      <img src="figures/graphical_abstract.png" alt="Graphical Abstract" class="zoomable-img" loading="lazy" />
      <div class="figure-img-caption">图文摘要 (Graphical Abstract)：SCN CCK 神经元调控生物钟稳健性与昼夜节律行为机制图</div>
    </div>
    <div class="figure-text-block">
      <div class="term-box">
        <div class="term-title"><i class="fas fa-lightbulb"></i> 环路机制极简读图：</div>
        <p><strong>左侧（常规周期 12L:12D）：</strong>CCK 神经元位于视交叉上核 (suprachiasmatic nucleus, SCN) 背侧前外壳区，在光暗交替（黄昏）前活性上升并精准预测活动起始时间。VIP 神经元（腹侧）接收光输入介导相位延迟，CCK 对其施加负反馈抑制；AVP 神经元（背侧）在黎明对齐，三者共同形成网络耦合平衡。</p>
        <p><strong>右侧（极端长光周期 20L:4D）：</strong>VIP 神经元光反应与节律显著耗竭；CCK 神经元节律依然保持，且从抑制转为激活 VIP 神经元，维系 SCN 网络耦合，防止节律崩溃与行为分裂。</p>
      </div>
    </div>
  </div>

  <div class="highlights-box">
    <h3 class="sub-heading"><i class="fas fa-star"></i> 研究亮点 (Highlights)</h3>
    <ul class="highlights-list">
      <li>
        <strong>SCN CCK 神经元的神经活性追踪昼夜节律行为活动的起始</strong><br>
        <span class="en-sub">Activities of SCN CCK neurons track the onset of circadian behavioral activities</span>
        <div class="hl-desc">在不同光周期下，CCK 神经元的钙活动峰值始终稳定出现在小鼠夜间运动和体温升高前约 5 小时，充当活动起始的内在定时器。</div>
      </li>
      <li>
        <strong>SCN CCK 神经元在长光周期下协调昼夜节律活动</strong><br>
        <span class="en-sub">SCN CCK neurons coordinate the circadian activities under long photoperiods</span>
        <div class="hl-desc">特异性消融或沉默 CCK 神经元会导致小鼠在长日照（20L:4D）下活动时间异常延长（无法正常压缩活动区间），并在恒光（LL）下迅速发生行为分裂或节律丧失。</div>
      </li>
      <li>
        <strong>SCN CCK 神经元在光授时通路中与 VIP 神经元相互作用</strong><br>
        <span class="en-sub">SCN CCK neurons interact with VIP neurons in the light entrainment pathway</span>
        <div class="hl-desc">CCK 神经元不直接感光，但激活 CCK 神经元可诱导相位前移，并在初夜通过负反馈抑制 VIP 神经元激活，从而对冲和门控光诱发的相位延迟。</div>
      </li>
      <li>
        <strong>SCN CCK 神经元调控时差的恢复速度</strong><br>
        <span class="en-sub">SCN CCK neurons regulate the recovery rate of jet lag</span>
        <div class="hl-desc">CCK 神经元对光暗周期的骤变响应较慢，其储存的“旧时区记忆”构成了时差适应迟缓的神经基础；在时差早期特异性化学遗传抑制 CCK 神经元能够显著加速时差恢复。</div>
      </li>
    </ul>
  </div>

  <div class="in-brief-box">
    <h3 class="sub-heading"><i class="fas fa-file-alt"></i> 简要介绍 (In Brief)</h3>
    <p>哺乳动物中央昼夜节律生物钟位于视交叉上核 (SCN)，由多种神经元亚型组成。Xie 等人揭示了一个包含胆囊收缩素 (cholecystokinin, CCK) 神经元的神经环路，该环路为昼夜节律活动的起始计时，并在长日照光周期以及时差中的相位转移过程中调控昼夜节律行为。</p>
    <div class="en-quote">The mouse central circadian clock residing in the SCN consists of multiple neuronal subtypes. Xie et al. uncover a neural circuit involving CCK neurons that times the onset of circadian activities and regulates circadian behaviors under a long-day photoperiod and phase shift in jet lag.</div>
  </div>
</section>

<section id="summary" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">01</span> 摘要 (Summary)</h2>
  </div>

  <div class="trans-content">
    <p>视交叉上核（suprachiasmatic nucleus, SCN，哺乳动物下丘脑控制全身昼夜节律的主起搏器）能够在不同环境下使哺乳动物产生稳健的昼夜节律行为（circadian behaviors，生物体内约 24 小时的周期性生理与行为活动），但其潜在的神经机制仍不清楚。</p>
    
    <p>在此，我们证明小鼠 SCN 中胆囊收缩素（cholecystokinin, CCK，一种经典的多肽类神经调质）神经元的活动在不同光周期（photoperiods，一昼夜中光照与黑暗的比例）下均先于行为活动的起始（onset of behavioral activities）。</p>
    
    <p>CCK 神经元缺陷的小鼠表现出游离运转周期（free-running periods，在无外界时间线索如恒黑条件下的内源生物节律周期，常记作 $\\tau$）缩短，在长光周期（long photoperiod，如 20 小时光照: 4 小时黑暗）下无法压缩其活动时间，并在持续光照（constant light, LL）下迅速出现行为分裂（splitting，原为一个整体的夜间活动段分裂为两个独立的、运转周期不同的游离组分）或变为心律失常/节律丧失（arrhythmic）。</p>
    
    <p>此外，与血管活性肠肽（vasoactive intestinal polypeptide, VIP，SCN 腹侧接收视网膜直接光输入的核心神经肽）神经元不同，CCK 神经元不直接感光（not directly light sensitive），但它们的激活能够引发相位前移（phase advance，生物钟时间提前），并抵消由 VIP 神经元介导的光诱导相位后移（phase delay，生物钟时间推迟）。</p>
    
    <p>在长光周期下，CCK 神经元对 SCN 的影响超过了 VIP 神经元。最后，我们发现反应迟缓的 CCK 神经元控制着时差（jet lag，生物体内源钟与新外界光暗周期失步的生理状态）过程中的恢复速度。</p>
    
    <p>总之，我们的结果表明，SCN CCK 神经元对于哺乳动物昼夜节律生物钟的稳健性（robustness，系统抵抗外界扰动保持节律稳定的能力）和可塑性（plasticity，系统适应季节日长及环境骤变的可变性）至关重要。</p>

    <div class="en-source-box">
      <div class="en-source-title"><i class="fas fa-language"></i> 英文原文 (English Original)</div>
      <p class="en-orig">The suprachiasmatic nucleus (SCN) can generate robust circadian behaviors in mammals under different environments, but the underlying neural mechanisms remained unclear. Here, we showed that the activities of cholecystokinin (CCK) neurons in the mouse SCN preceded the onset of behavioral activities under different photoperiods. CCK-neuron-deficient mice displayed shortened free-running periods, failed to compress their activities under a long photoperiod, and developed rapid splitting or became arrhythmic under constant light. Furthermore, unlike vasoactive intestinal polypeptide (VIP) neurons, CCK neurons are not directly light sensitive, but their activation can elicit phase advance and counter light-induced phase delay mediated by VIP neurons. Under long photoperiods, the impact of CCK neurons on SCN dominates over that of VIP neurons. Finally, we found that the slow-responding CCK neurons control the rate of recovery during jet lag. Together, our results demonstrated that SCN CCK neurons are crucial for the robustness and plasticity of the mammalian circadian clock.</p>
    </div>
  </div>
</section>
"""
