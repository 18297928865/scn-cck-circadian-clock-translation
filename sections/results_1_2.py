# -*- coding: utf-8 -*-

RESULTS_1_2_HTML = """
<section id="results-1" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">03</span> 结果 1：SCN CCK 神经元的活动追踪昼夜节律行为活动的起始</h2>
    <div class="sec-title-en">Activities of SCN CCK neurons track the onset of circadian behavioral activities</div>
  </div>

  <div class="trans-content">
    <p>我们首先通过在自由活动（free-moving）的小鼠体内进行长期活体光纤记录（in vivo fiber photometry），检测了 SCN CCK 神经元与 VIP 神经元的自发钙活动（spontaneous calcium activities）。实验中，我们将编码 GCaMP6s（一种敏感的基因编码钙指示蛋白）的腺相关病毒载体（adeno-associated virus, AAV：AAV-EF1a-DIO-GCaMP6s-P2A-nls-tdTomato）注射至 CCK-Cre 和 VIP-Cre 小鼠的 SCN 中，并同时监测它们自主运动活动（locomotor activity, LMA）和核心体温（body temperature, Tb）（<strong>Figure 1A</strong>）。CCK-Cre 小鼠中表达 tdTomato 的细胞主要位于前侧 SCN 的外壳区（shell region of anterior SCN），而 VIP-Cre 小鼠中的阳性细胞则主要位于后侧 SCN 的腹侧区（ventral region of the posterior SCN），这与先前报道的 CCK 和 VIP 神经元在 SCN 中的特定空间分布一致<sup>25</sup>（<strong>Figures 1B 和 S1A</strong>）。</p>

    <p>在 12 小时光照: 12 小时黑暗（12L:12D，常规光暗周期）条件下，我们发现 SCN CCK 神经元的活体自发钙活动呈现出昼夜节律振荡，其峰值出现在授时时间 ZT7.05 ± 0.37（Zeitgeber time，ZT；将开灯时间设为 ZT0，关灯时间设为 ZT12），比关灯时（ZT12）自主运动开始及核心体温上升的时间大约提前了 5 小时（<strong>Figures 1C, 1D, 和 1I</strong>）。相比之下，SCN VIP 神经元在整个白天期间均维持高水平的钙活动，这与之前的研究报道相一致<sup>26</sup>。CCK 神经元与 VIP 神经元的钙活动波形存在极其显著的差异（$p = 2.25 \\times 10^{-5}$，Kolmogorov-Smirnov 检验）。我们测量了它们钙活动峰在上升相（rising phase, W1）和下降相（declining phase, W2）的半峰全宽（half widths），发现与 VIP 神经元相比，CCK 神经元的钙活动波形在总半高宽（total half-width, W1 + W2）上更窄，而在不对称比值（W1/W2）上更加不对称（<strong>Figures 1J 和 1K</strong>）。VIP 神经元的活性峰值出现在 ZT6.06 ± 0.29 左右，早于 CCK 神经元的峰值时间（<strong>Figure 1I</strong>）。光纤植入位点和被感染 CCK 神经元的数量并未对 SCN CCK 神经元的每日钙活动轮廓产生显著影响（<strong>Figures S1A 和 S1B</strong>）。当小鼠从 12L:12D 释放进入恒定黑暗（constant dark, DD）条件时，CCK 和 VIP 神经元的昼夜节律钙活动与自主运动及核心体温节律一同进入游离运转（free run），在此期间 CCK 神经元与 VIP 神经元钙活动波形的差异性特征得以维持（<strong>Figures 1C, 1E, 和 1M</strong>）。</p>

    <div class="term-box">
      <div class="term-title"><i class="fas fa-microscope"></i> 专业术语解析：授时时间 (ZT) vs 主观节律时间 (CT) vs 峰值相位 (Acrophase)</div>
      <p><strong>授时时间 (Zeitgeber Time, ZT)：</strong>环境外源时间标尺。在常规 12L:12D 中，ZT0 为亮灯 (Lights-on)，ZT12 为熄灯 (Lights-off)。</p>
      <p><strong>昼夜节律时间 / 主观时间 (Circadian Time, CT)：</strong>内源生物钟的主观时间标尺（常用于恒暗 DD 或恒光 LL 下）。CT0 代表主观白天的开始，CT12 代表主观夜间的开始（对应夜行性啮齿类动物活动开始 onset）。</p>
      <p><strong>峰值相位 (Acrophase, $\\phi$)：</strong>利用余弦函数拟合昼夜振荡波形时，振荡达到最高峰所对应的相位时间点。</p>
      <p><strong>波形参数 (W1, W2, RA)：</strong>W1 为上升期半高宽，W2 为下降期半高宽；RA 为相对振幅 (Relative Amplitude)，反映节律波动剧烈程度。</p>
    </div>

    <p>已知长日照光周期会增加 SCN 神经元之间的相位离散度（phase dispersion），而释放入 DD 则会促使其重新同步化（resynchronization）<sup>17,21</sup>。随后，我们测量了长日照光周期（20L:4D，20 小时光照: 4 小时黑暗）下 CCK 和 VIP 神经元的钙活动（<strong>Figures 1C, 1F, 和 S1C</strong>）。在 20L:4D 下，VIP 神经元的钙活动峰值出现在 ZT2.42 ± 0.25（关灯被定义为 ZT12），该时间点再次位于活动开始（onset）与活动结束（offset）的中点，导致其相对于活动起始时间的相位差显著增大（$\\Delta$ phase-onset；<strong>Figures 1I, 1F, 和 S2A–S2D</strong>）。VIP 神经元的每日钙活动曲线在白天显著展宽，表现出振荡相对振幅（relative amplitude, RA）下降以及在长光周期下基线水平升高（<strong>Figures 1L 和 S2E</strong>）。具体而言，VIP 神经元在 20L:4D 下表现出钙活动的对称性延伸，与 12L:12D 相比总半高宽增加（<strong>Figures 1J, S2F, 和 S2G</strong>）。在 CCK 神经元中，其钙活动振荡的 RA 亦有所下降，但下降幅度要小得多，且与 12L:12D 相比，20L:4D 下钙活动的基线水平没有显著差异（<strong>Figures 1L 和 S2H</strong>）。在 20L:4D 条件下，CCK 神经元的钙活动在白天前半段缓慢上升并在 ZT7.33 ± 0.49 达到峰值，依然处于小鼠自主运动开始和体温升高前约 5 小时（<strong>Figures 1C, 1G, 1M, S2C, 和 S2D</strong>）。CCK 神经元在 20L:4D 下表现出钙活动不对称性（W1/W2）的增加（<strong>Figure 1K</strong>），这是由于 W1 增加而 W2 保持不变所致（<strong>Figure S2B</strong>）。从 20L:4D 释放进入 DD 后，相位领先的 VIP 神经元的钙活动峰值发生短暂后缩（retracted），而相位落后的 CCK 神经元的峰值发生前移（advanced），直至 VIP 神经元与 CCK 神经元之间的相位关系重新恢复至类似于 12L:12D 下的状态，表明在重新同步化的过程中 VIP 与 CCK 神经元之间存在相互作用（<strong>Figures 1I 和 1M</strong>）。在此过程中，行为活动结束时间发生回缩，活动开始时间发生前移，而 CCK 神经元的钙峰值始终与行为活动开始时间保持相位锁定（phase-locked with activity onset time），VIP 神经元的钙峰值则始终与活动开始和结束的中点时间保持相位锁定（<strong>Figures 1M, 1N, 和 S2I–S2K</strong>）。</p>

    <p>此外，我们通过使用单分子荧光原位杂交（single-molecule fluorescence in situ hybridization, smFISH）技术，将神经元活性标志物 <em>Fos</em> 与 <em>Avp</em>、<em>Vip</em> 和 <em>Cck</em> 共同荧光标记，检测了在 12L:12D 诱导后处于 DD 中或处于 20L:4D 下的小鼠 SCN VIP、CCK 和 AVP 神经元在一天中不同时间点的 Fos 表达（<strong>Figures S3A 和 S3D</strong>）。我们发现，在 12L:12D 下，<em>Avp</em><sup>+</sup> 神经元的 Fos 表达在 CT3（昼夜节律时间，Circadian time）达到峰值，<em>Vip</em><sup>+</sup> 神经元在 CT6 达到峰值，而 <em>Cck</em><sup>+</sup> 神经元在 CT9 达到峰值（<strong>Figure S3B</strong>）。在 20L:4D 下，smFISH 分析表明，相对于开灯时间而言，<em>Cck</em><sup>+</sup> 神经元中的 Fos 表达因长日照条件而发生了相位延迟，但与关灯时间始终保持相位锁定（<strong>Figure S3E</strong>）。与此相反，<em>Avp</em><sup>+</sup> 神经元中的 Fos 表达相对于关灯时间发生相位前移，但与开灯时间保持相位锁定。在 <em>Vip</em><sup>+</sup> 神经元中，白天的 Fos 表达依然高于夜间，但在 20L:4D 下 Fos 表达昼夜节律的相对振幅（RA）降低，且 Fos 表达的基线水平升高。我们发现，CCK 神经元和 VIP 神经元中的 Fos 表达振荡与其各自的钙活动节律处于相同的相位（<strong>Figures S3C 和 S3F</strong>），并且从 12L:12D 转变为 20L:4D 时经历了相似的定量变化（<strong>Figures S3G 和 S3H</strong>）。综上所述，SCN CCK 神经元的钙活动和 Fos 表达均与关灯时间保持紧密的相位锁定，能够在不同光周期下精准预示昼夜节律行为活动的起始。</p>

    <div class="figure-container card-figure">
      <div class="figure-image-box">
        <img src="figures/figure1.png" alt="Figure 1" class="zoomable-img" loading="lazy" />
        <div class="figure-img-caption">Figure 1. SCN CCK 与 VIP 神经元的体内钙活动特征</div>
      </div>
      <div class="figure-legend">
        <h4 class="legend-title">Figure 1 图注详细逐项翻译：</h4>
        <p><strong>(A)</strong> 在自由活动小鼠中利用光纤记录（fiber photometry）对 SCN 钙信号（GCaMP6s）进行长期体内记录，并同时记录小鼠核心体温（Tb）和自主运动活性（LMA）的实验示意图。</p>
        <p><strong>(B)</strong> 光纤记录实验时间线（上图）以及显示位于 SCN 上方的光纤套管位置的代表性脑片图像（下图）。标尺：100 μm。</p>
        <p><strong>(C)</strong> 在 12L:12D 转入恒定黑暗（DD）（上图）或 20L:4D 转入恒定黑暗（DD）（下图）的自主活动记录图（actogram）中，SCN CCK 与 VIP 神经元体内 GCaMP6s 信号（灰色）的代表性曲线图，叠加了自主运动活性（LMA，绿色）和核心体温（Tb，橙色）。</p>
        <p><strong>(D)</strong> 12L:12D 条件下（LD1–3 天）SCN CCK（红色，$\\phi = \\text{ZT}7.05 \\pm 0.37$）和 VIP（蓝色，$\\phi = \\text{ZT}6.06 \\pm 0.29$）神经元体内 GCaMP6s 信号的平均昼夜变化轮廓。$\\phi$（峰值相位，acrophase）表示预测的峰值或昼夜节律相位。底部展示了 12L:12D 下 Tb（橙色）和 LMA（绿色）的平均日曲线。$p$ 值表示 SCN CCK 与 VIP 神经元 GCaMP 信号曲线之间的 Kolmogorov-Smirnov 检验结果；均值 $\\pm$ SEM；CCK, $n = 6$；VIP, $n = 6$。</p>
        <p><strong>(E)</strong> 从 12L:12D 释放进入 DD（DD1–3 天）小鼠 SCN CCK（红色，$\\phi = \\text{CT}7.37 \\pm 0.61$）和 VIP（蓝色，$\\phi = \\text{CT}6.01 \\pm 0.21$）神经元体内 GCaMP6 信号的平均昼夜节律轮廓。同 (D)；CCK, $n = 3$；VIP, $n = 4$。</p>
        <p><strong>(F)</strong> 20L:4D 条件下（LD1–3 天）SCN CCK（红色，$\\phi = \\text{ZT}7.23 \\pm 0.41$）和 VIP（蓝色，$\\phi = \\text{ZT}2.89 \\pm 0.54$）神经元体内 GCaMP6 信号的平均昼夜变化轮廓。同 (D)；CCK, $n = 5$；VIP, $n = 5$。</p>
        <p><strong>(G)</strong> 从 20L:4D 释放进入 DD（DD7–9 天）小鼠 SCN CCK（红色，$\\phi = \\text{CT}7.22 \\pm 0.36$）和 VIP（蓝色，$\\phi = \\text{CT}6.11 \\pm 0.17$）神经元体内 GCaMP6 信号的平均昼夜节律轮廓。同 (D)；CCK, $n = 4$；VIP, $n = 4$。</p>
        <p><strong>(H)</strong> 示意图说明如何通过相对振幅（RA）、上升相半高宽（W1）、下降相半高宽（W2）以及预测的峰值相位或昼夜节律相位（$\\phi$, acrophase）来表征钙信号的波形特征。</p>
        <p><strong>(I)</strong> 12L:12D、12L:12D 转入 DD、20L:4D 以及 20L:4D 转入 DD 条件下 SCN CCK（红色）和 VIP（蓝色）神经元 GCaMP6s 信号峰值相位（$\\phi$）的差异（通过双因素方差分析及 Tukey 事后检验：****$p < 0.0001$, ***$p < 0.001$, **$p < 0.01$, *$p < 0.05$）。各条件下使用的动物数量：12L:12D（CCK, $n = 6$；VIP, $n = 6$），12L:12D 转 DD（CCK, $n = 3$；VIP, $n = 4$），20L:4D（CCK, $n = 5$；VIP, $n = 5$），以及 20L:4D 转 DD（CCK, $n = 4$；VIP, $n = 4$）。</p>
        <p><strong>(J)</strong> 12L:12D、12L:12D 转入 DD、20L:4D 以及 20L:4D 转入 DD 条件下 SCN CCK（红色）和 VIP（蓝色）神经元 GCaMP6s 信号总半高宽（W1 + W2）的差异（通过双因素方差分析及 Tukey 事后检验：****$p < 0.0001$, ***$p < 0.001$）。使用动物数量同 (I)。</p>
        <p><strong>(K)</strong> 12L:12D、12L:12D 转入 DD、20L:4D 以及 20L:4D 转入 DD 条件下 SCN CCK（红色）和 VIP（蓝色）神经元 GCaMP6s 信号 W1 与 W2 比值的差异（通过双因素方差分析及 Tukey 事后检验：****$p < 0.0001$, **$p < 0.01$, *$p < 0.05$）。使用动物数量同 (I)。</p>
        <p><strong>(L)</strong> 同一小鼠在 12L:12D、12L:12D 转 DD、20L:4D 以及 20L:4D 转 DD 条件下 SCN CCK（红色）和 VIP（蓝色）神经元 GCaMP6s 信号相对振幅（RA）的差异（配对 t 检验：**$p < 0.01$, *$p < 0.05$）。CCK, $n = 3$；VIP, $n = 3$。</p>
        <p><strong>(M)</strong> 从 12L:12D 释放进入 DD（上图）以及从 20L:4D 释放进入 DD（下图）过程中，SCN CCK（红色）和 VIP（蓝色）神经元 GCaMP6s 信号峰值相位、LMA 开始与结束时间（绿色）、Tb 开始与升高时间（橙色）的轨迹图。12L:12D 转 DD：CCK, $n = 3$；VIP, $n = 3$；20L:4D 转 DD：CCK, $n = 4$；VIP, $n = 4$。</p>
        <p><strong>(N)</strong> 从 12L:12D 转入 DD（上图，Pearson 相关，$R^2 = 0.95$, $p = 5.07 \\times 10^{-7}$）以及从 20L:4D 转入 DD（下图，Pearson 相关，$R^2 = 0.98$, $p = 1.52 \\times 10^{-13}$）期间，SCN CCK 神经元 GCaMP6s 信号的峰值相位与自主运动（LMA）开始时间之间的线性相关关系。12L:12D 转 DD：CCK, $n = 3$；20L:4D 转 DD：CCK, $n = 4$。</p>
      </div>
    </div>
  </div>
</section>

<section id="results-2" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">04</span> 结果 2：CCK 神经元在长光周期下调控昼夜节律活动</h2>
    <div class="sec-title-en">CCK neurons regulate circadian activity under long-day photoperiods</div>
  </div>

  <div class="trans-content">
    <p>接下来，我们利用表达 Caspase-3（半胱天冬酶-3，促凋亡蛋白酶）的 AAV 特异性消融 SCN CCK 神经元，以研究 CCK 神经元在昼夜节律行为调控中的功能。我们将编码 Cre 依赖型 taCasp3（AAV-DIO-taCasp3）或对照荧光蛋白（AAV-DIO-EYFP）的 AAV 双侧立体定位注射到 CCK-Cre 小鼠的 SCN 中（<strong>Figure 2A</strong>）。注射 4 周后，我们测定了 SCN CCK 神经元缺失小鼠（CCK-Casp3）的自主跑轮活动（wheel running activities）的昼夜节律。注射导致 SCN 中 CCK 神经元数量极显著减少（对照组，$n = 1,149 \\pm 57.78$ 个；CCK 神经元消融组，$n = 368.88 \\pm 156.18$ 个）（<strong>Figures 2B 和 2C</strong>）。我们发现，在 12L:12D 条件下，CCK-Casp3 小鼠的跑轮活动曲线与对照小鼠相比没有显著差异（<strong>Figures 2D, 2E, 和 S4A; Data S1</strong>）。然而，当从小鼠 12L:12D 条件释放进入恒暗（DD）环境后，CCK-Casp3 小鼠表现出显著缩短的游离运转周期（$\\tau = 23.22 \\pm 0.04$ h），相比之下对照小鼠周期为（$\\tau = 23.6 \\pm 0.07$ h）（<strong>Figure 2F</strong>）。</p>

    <div class="term-box">
      <div class="term-title"><i class="fas fa-tools"></i> 实验工具解析：taCasp3 消融 vs TeNT 突触阻断</div>
      <p><strong>taCasp3 (转座工程化半胱天冬酶3)：</strong>在缺乏特异性促凋亡信号时仍具有酶活性的重组 Caspase-3，在 Cre 重组酶介导下特异性诱发目标神经元发生凋亡消融（ablated）。本实验中 CCK 阳性神经元减少约 70%。</p>
      <p><strong>TeNT (破伤风毒素轻链，Tetanus toxin light chain)：</strong>能够特异性酶切突触小泡结合蛋白 synaptobrevin/VAMP2，从而彻底阻断神经递质从突触前膜的胞吐释放（silencing），但不引起细胞死亡。用于区分“完全破坏神经元环路”与“仅阻断化学递质传递”。</p>
    </div>

    <p>随后，我们检测了 CCK-Casp3 小鼠在长日照（20L:4D）条件下的跑轮活动。在如此长的白昼条件下，正常对照小鼠的活动持续时长（activity durations, alpha，$\\alpha$）被高度压缩，活动开始时间（activity onset）非常靠近活动结束时间（activity offset）。有趣的是，我们发现与对照小鼠相比，消融 SCN CCK 神经元导致 20L:4D 下的活动持续时间（$\\alpha$）显著延长（<strong>Figure 2G</strong>）。具体而言，与对照组相比，CCK-Casp3 小鼠的活动开始时间发生了前移（advanced onset），而活动结束时间发生了后移（delayed offset）（<strong>Figures 2H 和 S4E</strong>）。CCK-Casp3 小鼠似乎无法在长日照条件下将其活动开始引带对齐于关灯时间，亦无法将其活动结束引带对齐于开灯时间。总体而言，CCK-Casp3 小鼠表现出节律性下降，在 20L:4D 下饲养至第 4 周时，22 只实验动物中有 2 只甚至完全丧失了节律性（节律丧失型 CCK-Casp3 小鼠）（<strong>Figures S4C 和 S4D</strong>）。一旦释放进入 DD，对照小鼠被压缩的活动区间会缓慢解压缩（decompressed），恢复到与 12L:12D 下相当的水平，这与 SCN 在季节变化下表现出的昼夜授时可塑性观点高度吻合。相反，CCK-Casp3 小鼠则从原本就未能充分压缩的活动模式中，表现出异常快速的活动模式恢复（<strong>Figure 2I</strong>）。在 20L:4D 下变为无节律的 CCK-Casp3 小鼠在进入 DD 后依然维持无节律状态。而保持节律的 CCK-Casp3 小鼠在 DD 下再次表现出显著缩短的游离运转周期（$\\tau = 23.38 \\pm 0.05$ h），对照组为（$\\tau = 23.58 \\pm 0.06$ h）（<strong>Figure 2F; Data S1</strong>）。</p>

    <p>此外，我们通过 AAV 介导表达破伤风毒素（tetanus toxins, CCK-TeNT）特异性阻断 SCN CCK 神经元的神经递质释放，检测了其在 20L:4D 下的行为改变（<strong>Figures 2J 和 S4J</strong>）。类似地，我们发现 CCK-TeNT 小鼠在 20L:4D 下的活动持续时间同样缺乏充分压缩（<strong>Figures 2K 和 S4F</strong>），并且在释放入 DD 后相比对照小鼠呈现更快速的解压缩（<strong>Figures 2L 和 S4I; Data S1</strong>）。在 DD 条件下，CCK-TeNT 小鼠的游离运转周期与野生型（WT）小鼠相比没有显著差异（<strong>Figures S4G 和 S4H</strong>）。综合上述结果，在长日照光周期下，SCN CCK 神经元功能受损的动物其昼夜节律活动表现出明显减弱的季节性可塑性。</p>

    <div class="figure-container card-figure">
      <div class="figure-image-box">
        <img src="figures/figure2.png" alt="Figure 2" class="zoomable-img" loading="lazy" />
        <div class="figure-img-caption">Figure 2. CCK 神经元缺陷小鼠在不同光周期下的昼夜节律行为</div>
      </div>
      <div class="figure-legend">
        <h4 class="legend-title">Figure 2 图注详细逐项翻译：</h4>
        <p><strong>(A)</strong> 在 CCK-IRES-Cre 小鼠 SCN 中双侧注射 AAV-DIO-taCasp3-TEVp 或 AAV-DIO-EYFP 以及在不同光周期下检测跑轮行为的实验示意图。</p>
        <p><strong>(B)</strong> 对照组与 CCK-Casp3 小鼠 SCN 中 CCK 神经元空间分布的代表性图像。标尺：100 μm。</p>
        <p><strong>(C)</strong> SCN 中 CCK 神经元的数量：对照小鼠为 $1,149 \\pm 57.78$（均值 $\\pm$ SEM），$n = 4$；CCK-Casp3 小鼠为 $368.88 \\pm 156.18$，$n = 8$（***$p < 0.001$，非配对 Student's t 检验）。</p>
        <p><strong>(D)</strong> 对照组和 CCK-Casp3 小鼠跑轮活动的代表性双重绘制自主活动记录图（double-plotted actograms）。所有小鼠最初饲养在 12L:12D 条件下，随后转入恒定黑暗（DD）。</p>
        <p><strong>(E)</strong> 与对照组小鼠相比，CCK-Casp3 小鼠的日活动轮廓未见显著差异。</p>
        <p><strong>(F)</strong> CCK-Casp3 小鼠的游离运转周期显著缩短。从 12L:12D 引带后转 DD：对照小鼠为 $23.6 \\pm 0.07$ h，$n = 7$；CCK-Casp3 小鼠为 $23.22 \\pm 0.04$ h，$n = 18$。从 20L:4D 引带后转 DD：对照小鼠为 $23.58 \\pm 0.06$ h，$n = 13$；CCK-Casp3 小鼠为 $23.38 \\pm 0.05$ h，$n = 20$（*$p = 0.038$, ***$p < 0.001$，双因素方差分析及 Scheffe 事后检验）。</p>
        <p><strong>(G)</strong> 对照小鼠和 CCK-Casp3 小鼠跑轮活动的代表性双重绘制自主活动记录图。所有小鼠最初饲养在 12L:12D 下，随后转入 20L:4D，最终释放进入恒定黑暗（DD）。</p>
        <p><strong>(H)</strong> 在 20L:4D 下，CCK-Casp3 小鼠的活动轮廓表现出活动开始时间提前且活动结束时间推迟（***$p < 0.001$，双因素方差分析）。对照小鼠，$n = 13$；CCK-Casp3 小鼠，$n = 20$。</p>
        <p><strong>(I)</strong> 在 20L:4D 条件下，CCK-Casp3 小鼠的活动持续时长（alpha，$\\alpha$）较对照小鼠显著延长（*$p < 0.05$, **$p < 0.01$, ***$p < 0.001$，双因素方差分析及 Tukey 事后检验）。误差棒代表 SEM。实验动物数量同 (H)。</p>
        <p><strong>(J)</strong> 在 CCK-IRES-Cre 小鼠 SCN 双侧注射 AAV-DIO-TeNT 或 AAV-DIO-EYFP 以及在 20L:4D 下记录跑轮行为的示意图。标尺：100 μm。</p>
        <p><strong>(K)</strong> CCK-TeNT 小鼠在 20L:4D 下的活动曲线显示活动开始提前而结束推迟（*$p < 0.05$; ***$p < 0.001$; n.s. 表示无显著性差异，$p > 0.05$，双因素方差分析）。对照小鼠，$n = 7$；CCK-TeNT 小鼠，$n = 8$。</p>
        <p><strong>(L)</strong> 在 20L:4D 下，CCK-TeNT 小鼠的活动持续时长（alpha，$\\alpha$）较对照小鼠显著延长（*$p < 0.05$, **$p < 0.01$, ***$p < 0.001$，双因素方差分析及 Tukey 事后检验）。误差棒代表 SEM。实验动物数量同 (K)。</p>
      </div>
    </div>
  </div>
</section>
"""
