# -*- coding: utf-8 -*-

DISCUSSION_HTML = """
<section id="discussion" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">09</span> 讨论 (Discussion)</h2>
  </div>

  <div class="trans-content">
    <p>在本研究中，我们探究了小鼠视交叉上核（SCN）中胆囊收缩素（CCK）神经元在昼夜节律生物钟中的功能。我们证明了 SCN CCK 神经元的钙活动能够追踪傍晚（E）行为活动的起始，且 CCK 神经元的功能障碍会显著破坏长光周期和持续光照（LL）下的昼夜节律计时维持。我们进一步证实，激活这些 CCK 神经元能够在不同的光周期条件下诱发相位前移，并且 CCK 神经元在光授时通路中拮抗 VIP 神经元的功能。我们发现，在长日照光周期下，VIP 神经元对 CCK 神经元的激活作用显著减弱，而 CCK 神经元则从抑制转而开始激活 VIP 神经元。最后，我们提出 SCN CCK 神经元在昼夜循环突变下的缓慢适应过程构成了时差反应（jet lag）的细胞与神经基础。因此，CCK 神经元及其与 SCN 其他神经元的相互作用，为哺乳动物昼夜节律生物钟所必需的稳健性（robustness）和可塑性（plasticity）提供了关键的神经环路基础。</p>

    <h3 class="sub-heading">SCN 神经元亚型的异质性昼夜节律功能 (Heterogeneous circadian functions of SCN neuronal subtypes)</h3>
    <p>作为哺乳动物的中央昼夜节律生物钟，SCN 包含许多不同的神经元亚型。对于其中许多亚型而言，它们在日常时间维持中的具体作用仍有待系统性检验。在本研究中，我们主要在与 VIP 神经元对比的背景下研究了 CCK 神经元的功能。我们先前的研究揭示，VIP 和 CCK 神经元各自均可进一步细分为亚群：VIP 神经元由具有强昼夜节律性的 <em>Vip</em><sup>+</sup>/<em>Nms</em><sup>+</sup> 亚型和具有最强光响应能力的 <em>Grp</em><sup>+</sup>/<em>Vip</em><sup>+</sup> 亚型组成<sup>25</sup>。因此，我们在本研究中测得的 VIP 神经元钙活动，实际上代表了 <em>Vip</em><sup>+</sup>/<em>Nms</em><sup>+</sup> 和 <em>Grp</em><sup>+</sup>/<em>Vip</em><sup>+</sup> 亚型的复合活性。同样地，CCK 神经元由 <em>Cck</em><sup>+</sup>/<em>C1ql3</em><sup>+</sup> 和 <em>Cck</em><sup>+</sup>/<em>Bdnf</em><sup>+</sup> 两个亚型组成。根据我们的单细胞 RNA 测序（scRNA-seq）数据，<em>Cck</em><sup>+</sup>/<em>C1ql3</em><sup>+</sup> 神经元构成了 CCK 神经元的绝大多数，并可能赋予了钙活动的节律性振荡，其相位相对于其他 SCN 神经元亚型存在显著延迟。有趣的是，先前已有报道脑源性神经营养因子（brain-derived neurotrophic factor, BDNF）能够调控光脉冲诱发的相位转移<sup>29</sup>。因此，<em>Cck</em><sup>+</sup>/<em>Bdnf</em><sup>+</sup> 亚型可能是介导我们在本研究中观察到的 CCK 神经元在光授时通路中调控作用的细胞亚群。</p>

    <p>精氨酸加压素（AVP）神经元和 AVP 神经肽信号也被认为在 SCN 中扮演着重要角色<sup>13–15</sup>。当 AVP 神经元内部的自主细胞时钟或 GABA 能神经传递受到破坏时，即使在常规 12L:12D 条件下，傍晚（E）和早晨（M）活动峰也开始出现解离<sup>13,30,31</sup>。据报道，AVP 神经元的钙活动在黎明时达到峰值<sup>30</sup>，这与我们在本研究中于 12L:12D 条件下测得的 AVP 神经元 <em>Fos</em> 表达峰值时间高度一致。相反，CCK 神经元的钙活动在黄昏前达到峰值，并与行为活动的开始时间保持相位锁定。此外，我们发现 CCK-Casp3 小鼠在 12L:12D 下表现出正常的昼夜节律行为，但仅在长光周期条件下出现活动时程无法压缩（解压缩）的行为异常。与 AVP 神经元相比，CCK 神经元对于 E 振荡器与 M 振荡器之间的耦合似乎更为关键，尤其是在 SCN 神经元极易发生去同步化的长光周期条件下。在持续光照（LL）下，CCK-Casp3 和 CCK-TeNT 小鼠的昼夜节律行为变得更加多变——部分动物表现出节律完全丧失（无节律），部分表现出行为分裂（splitting），还有部分维持正常节律。这一观察进一步强有力地支持了我们的结论，即 CCK 神经元对维持 SCN 系统的稳健性不可或缺。</p>

    <h3 class="sub-heading">SCN 神经网络及其可塑性 (The SCN neural network and its plasticity)</h3>
    <p>由异质性神经元亚型构成的 SCN 神经网络负责将环境光照信息转化为节律性生理和行为。在该网络中，SCN VIP 神经元一直被认为是昼夜节律生物钟光授时的关键核心<sup>10,26,32</sup>。如本研究和既往研究所证明的，VIP 神经元的钙活动具有高度的光敏响应性<sup>12,26</sup>。相反，我们发现主观初夜的光脉冲并不会即刻升高 CCK 神经元的钙活动。然而，直接光遗传刺激 VIP 神经元能够激活 CCK 神经元，并且在光脉冲刺激后的次日，CCK 神经元的钙节律依然表现出相位转移。这些结果表明，CCK 神经元处于 VIP 神经元的下游，且 CCK 神经元对 VIP 神经元的自然响应相对微弱，以至于只有通过高频光遗传刺激人为强烈激活 VIP 神经元时才能诱发 CCK 神经元中 <em>Fos</em> 的表达。我们通过光遗传学或化学遗传学操纵 CCK 神经元并配合光脉冲，能够改变昼夜节律行为的相位转移，这表明响应缓慢的 CCK 神经元可能通过抑制 VIP 神经元的激活，从而阻断光脉冲所引起的相位后移。尽管 CCK 神经元不直接感光，但已有解剖学研究表明 SCN CCK 神经元接收来自大脑多个非光照通路（non-photic pathways，如摄食、温觉、社交、自主运动等）相关脑区的神经投射<sup>33</sup>。因此，我们的研究可能为生物钟的非光授时机制以及光照通路与非光通路之间的交叉互作提供了潜在的神经环路机制。基于编码这些神经肽及其受体在 SCN 神经元各亚型中的表达特征，VIP 与 CCK 神经元之间的相互耦合可由多种神经肽介导，包括 VIP、CCK、BDNF 和前动力蛋白 2（prokineticin 2, PROK2）<sup>25</sup>。此前，Hannibal 等人曾报道 CCK 基因敲除小鼠（CCK-null）表现出与野生型对照相似的昼夜节律表型<sup>34</sup>。而在本研究中，我们针对 CCK 神经元的靶向消融不仅彻底消除了 CCK 基因本身的表达，同时也去除了由 CCK 神经元在 SCN 网络中所介导的全部细胞信号输出和输入。因此，我们的 CCK 神经元缺失小鼠与 CCK 敲除小鼠之间的表型差异提示：除了 CCK 神经肽本身的释放之外，其他神经机制（如共释放的 GABA 或其他神经调质）可能对我们在本研究中鉴定的 CCK 神经元的昼夜节律功能发挥了主要作用。</p>

    <p>除神经肽信号外，神经递质 GABA 亦可能参与 SCN 神经元之间的相互耦合。在 SCN 中，GABA 信号的作用既可以是抑制性的，也可以是兴奋性的，这取决于受体神经元内部的细胞内氯离子浓度（intra-cellular chloride concentration）<sup>21</sup>。本研究中发现的 VIP 与 CCK 神经元之间的负反馈相互作用，令人联想到此前学者提出的 SCN 核心区（core）与外壳区（shell）之间由 GABA 介导的非对称性连接模式<sup>28</sup>。我们利用 Caspase 消融 CCK 神经元与利用 TeNT 沉默 CCK 神经元所获得的结果差异亦提示，CCK 神经元可能利用了多种信号通路，因为在 CCK-TeNT 突触沉默中小鼠由 GABA 介导的囊泡传递被更彻底地阻断。最后，我们注意到 CCK 神经元在主观白天的活性时间窗口恰好与相位反应曲线（PRC）中生物钟对光刺激不发生任何相移的“死区”（dead zone）相重合。因此，VIP 与 CCK 神经元构成的负反馈回路，可能在一天中的特定时间点为生物钟对外部光照的响应提供了关键的“门控”机制（gating of the response）。</p>

    <p>作为界定地球季节更迭的主要环境因素，光照在长日照光周期<sup>24</sup>和持续光照（LL）<sup>23</sup>下对 SCN 的网络同步性具有显著的去稳定效应（destabilizing effect）。这种去同步化可能是由于 GABA 兴奋性增加<sup>18</sup>以及 VIP 信号传导升高所共同导致的<sup>35</sup>。尽管神经肽转换也被报道参与了哺乳动物的光周期适应<sup>16</sup>，但我们在 smFISH 分析中并未观察到长光周期下 <em>Vip</em>、<em>Cck</em> 或 <em>Avp</em> 基因表达水平发生显著改变。与 CCK 神经元相比，VIP 神经元受长光周期的影响更为显著，表现为在 20L:4D 条件下其昼夜节律钙活动与 <em>Fos</em> 表达的基线水平升高以及相对振幅（RA）降低。这一结果很好地解释了为何长日照阻断了 VIP 神经元介导的相位重置，却未阻断 CCK 神经元介导的相位重置。这也与以往文献报道的长光周期下光照诱发的相位转移能力明显下降的现象一致<sup>36</sup>。相比之下，在 LL 下钙活动受影响较小的 CCK 神经元受到刺激时仍能产生显著的相位转移。在 20L:4D 下，CCK 神经元激活所诱发的 VIP 神经元 <em>Fos</em> 表达升高，可能进一步促进了 VIP 神经元中钙信号与 Fos 表达的病理性高企——进而导致 VIP 神经元失去了正常的相位重置能力。有趣的是，既往有文献报道 VIP 敲除小鼠在 LL 下表现出更强的节律性活动<sup>35</sup>，而我们发现 SCN CCK 神经元缺陷的小鼠在 LL 下却无法维持节律行为，这再次有力地佐证了 CCK 神经元与 VIP 神经元在 SCN 中截然相反且相互制衡的功能角色。</p>

    <h3 class="sub-heading">早晨与傍晚振荡器模型 (E and M oscillator model)</h3>
    <p>我们的研究为 Pittendrigh 和 Daan 于 1976 年提出的早晨和傍晚（E 和 M）振荡器模型提供了全新的视角。在其最初的理论模型中，在夜行性啮齿动物体内，E 振荡器和 M 振荡器分别追踪傍晚活动开始（E activity onset）和早晨活动结束（M activity offset）。在我们的 <em>Fos</em> 表达动态分析中，AVP 神经元似乎主要追踪 M 峰，CCK 神经元追踪 E 峰，而 VIP 神经元则位于二者之间。CCK 神经元相对于 VIP 和 AVP 神经元的相位延迟，可能是由于 CCK 神经元具有更长的内在内源周期所致，因为特异性敲除 CCK 神经元会导致动物整体的游离运转周期缩短。其他神经机制（例如神经肽信号转导）可能会进一步促进哺乳动物生物钟起搏器不同神经元亚型之间活动节律的多样化，这与果蝇中发现的机制类似<sup>37,38</sup>。E 和 M 理论模型还预测，E 振荡器和 M 振荡器分别负责减慢（decelerate）和加快（accelerate）生物钟。与 VIP 神经元不同，激活 CCK 神经元特异性地在主观深夜诱发相位前移，而不在主观初夜产生相位后移，这表明 VIP 神经元与 CCK 神经元可能分别构成了生物钟相位反应曲线（PRC）中延迟相（delay portion）与前移相（advance portion）的神经环路实体。此外，经典的 E/M 模型假设了 E 和 M 振荡器之间存在双向互偶（mutual coupling）。我们的研究结果表明 VIP 神经元与 CCK 神经元之间形成了一个负反馈环路。最后，在 E 和 M 模型中，E 和 M 振荡器之间的相位关系会随着季节发生改变，并伴随着它们耦合强度的动态重构。事实上，我们确实发现，在长光周期下，VIP 神经元对 CCK 神经元的激活显著减弱，而 CCK 对 VIP 神经元的信号传递则从抑制转变为兴奋。综合来看，我们发现 VIP 和 CCK 神经元之间的相互耦合在很大程度上契合了经典的 E/M 振荡器模型，但 SCN 中其他的神经元亚型（如 AVP 神经元）仍需被系统整合进该模型中，未来需要更多的实验来进一步充实和巩固这一理论构架。</p>

    <p>在果蝇（<em>Drosophila</em>）的生物钟神经元中，位于腹外侧小神经元（sLNv）表达色素扩散因子（pigment-dispersing factor, PDF）的 M 细胞，以及位于背外侧神经元（LNd）的 E 细胞已被清晰鉴定<sup>4,5</sup>。此外，果蝇 E 细胞已被证实表达 PDF 受体<sup>39</sup>。根据我们的单细胞 RNA 测序（scRNA-seq）数据，小鼠 SCN CCK 神经元同样高度富集表达 VIP 受体 VIPR2，这表明小鼠 SCN 中从 VIP 神经元到 CCK 神经元的信号传导通路，在拓扑结构上高度类同于果蝇中从 M 细胞到 E 细胞的 PDF 信号级联。在果蝇中，M 细胞与 E 细胞之间的相位差正是编码季节性日长信息的关键载体<sup>40</sup>。同样地，在小鼠中，VIP、CCK 和 AVP 神经元的钙活动以及 <em>Fos</em> 基因表达的昼夜节律相位也共同编码了季节信息，其中 AVP 神经元与 CCK 神经元分别与黎明和黄昏精准对齐。在果蝇研究中，学者们提出 M 细胞在持续黑暗（DD）下维持振荡，而 E 细胞在持续光照（LL）下维持振荡，且在长日照光周期下 E 细胞支配主导 M 细胞<sup>41</sup>。小鼠 SCN CCK 神经元在长光周期和 LL 下均能持续正常运转，提示哺乳动物 SCN CCK 神经元的功能可能类似于果蝇中的候选 E 细胞。至于小鼠 SCN 中的 VIP 还是 AVP 神经元承担了类似于果蝇 M 细胞的功能，仍需后续深入研究。综上所述，由 VIP、CCK 和 AVP 神经元构成的哺乳动物 SCN 昼夜节律起搏系统，与果蝇的时钟神经元系统展现出惊人的演化相似性，表明生物钟季节性可塑性的神经机制在漫长的物种演化历程中可能具有高度的保守性。</p>

    <div class="term-box">
      <div class="term-title"><i class="fas fa-project-diagram"></i> 跨物种对比：果蝇 vs 哺乳动物 E/M 振荡器核心元件映射</div>
      <table class="term-table">
        <thead>
          <tr>
            <th>功能维度</th>
            <th>果蝇 (Drosophila melanogaster)</th>
            <th>小鼠视交叉上核 (Mus musculus SCN)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>M 振荡器 (早晨/黎明)</strong></td>
            <td>sLNv 神经元（释放 PDF 肽）</td>
            <td>AVP 神经元（对齐黎明） / VIP 神经元（部分功能）</td>
          </tr>
          <tr>
            <td><strong>E 振荡器 (傍晚/黄昏)</strong></td>
            <td>LNd 神经元（表达 PDF 受体 Han/PDFR）</td>
            <td><strong>CCK 神经元</strong>（富集于背前外壳区，表达 VIPR2）</td>
          </tr>
          <tr>
            <td><strong>信号连接拓扑</strong></td>
            <td>M 细胞 $\\xrightarrow{\\text{PDF}}$ E 细胞（单向/非对称支配）</td>
            <td>VIP 神经元 $\\leftrightarrow$ CCK 神经元（双向负反馈与季节性重构）</td>
          </tr>
          <tr>
            <td><strong>极端光照 (LL) 表现</strong></td>
            <td>E 细胞在 LL 下维持节律振荡</td>
            <td>CCK 神经元在 LL 下维持节律振荡；消融后行为分裂/无节律</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""
