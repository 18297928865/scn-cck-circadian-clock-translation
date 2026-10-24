# -*- coding: utf-8 -*-

METHODS_HTML = """
<section id="methods" class="section-card">
  <div class="section-title-wrap">
    <h2 class="section-title"><span class="sec-num">09</span> 研究方法与实验细节 (STAR+Methods)</h2>
  </div>

  <div class="trans-content">
    <h3 class="sub-heading">资源可用性 (RESOURCE AVAILABILITY)</h3>
    <p><strong>主要联系人 (Lead contact)：</strong>有关进一步信息以及资源和试剂的合理索取请求，请直接联系资深通讯作者严军博士（Dr. Jun Yan，电子邮箱：<a href="mailto:junyan@ion.ac.cn">junyan@ion.ac.cn</a>），并将由其协调答复。</p>
    <p><strong>材料可用性 (Materials availability)：</strong>本研究所采用的相关常规耗材及实验质粒均可通过商业化途径获得，未产生新的不可替代的特异性试剂。</p>
    <p><strong>数据与代码可用性 (Data and code availability)：</strong>
      <ul>
        <li>本论文中报道的实验数据可根据合理请求由通讯作者严军博士提供。</li>
        <li>研究所使用的原始定制分析代码已存入 Zenodo 公共数据库并公开可用（DOI：<a href="https://doi.org/10.5281/zenodo.7824372" target="_blank" rel="noopener">10.5281/zenodo.7824372</a>；RRID: SCR_001905, SCR_001622）。</li>
        <li>重新分析论文数据所需的任何附加技术细节亦可应请求提供。</li>
      </ul>
    </p>

    <h3 class="sub-heading">实验模型与受试对象细节 (EXPERIMENTAL MODEL AND SUBJECT DETAILS)</h3>
    <p><strong>实验动物 (Animals)：</strong>所有实验均使用 8–24 周龄的雄性小鼠。所有小鼠均饲养在无特定病原体（specific pathogen-free, SPF）级别、配备排风换气的密闭鼠架系统中。每个垫料为玉米芯的标准笼盒中最多合笼饲养 5 只小鼠。动物房环境维持在温度 20–22°C、相对湿度 30–70%，实行 12 小时光照/12 小时黑暗（12L:12D）标准光暗周期循环。小鼠自由进食标准小鼠饲料（Shoobree）并自由饮水。在进行活体光纤记录（in vivo fiber photometry）和光遗传学（optogenetics）实验时，使用了 C57BL/6 背景、在注射病毒时周龄至少达到 7 周的杂合子 CCK-IRES-Cre 和 VIP-IRES-Cre 小鼠。在完成脑立体定位病毒注射、光纤套管植入并恢复 1 周后，小鼠被单笼饲养于定制的行为观察箱（20 cm × 20 cm × 30 cm）中，并允许自由获取食物和饮水。在化学遗传学实验中，同样使用了周龄至少 7 周的杂合子 CCK-IRES-Cre 和 VIP-IRES-Cre 小鼠。在某些实验中为了辅助鉴定 CCK 神经元，将 CCK-IRES-Cre 小鼠与 Ai9 荧光报告小鼠进行杂交，获得在 CCK 细胞中特异性表达 tdTomato 红色荧光报告蛋白的 CCK-IRES-Cre:Ai9 杂合子小鼠。所有动物实验均严格遵守中国科学院脑科学与智能技术卓越创新中心/神经科学研究所实验动物伦理委员会制定的管理与使用协议（伦理审批编号：IACUC no. NA-023-2022）。</p>

    <h3 class="sub-heading">方法细节 (METHOD DETAILS)</h3>
    
    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-dna"></i> 1. 病毒载体 (Viruses)</h4>
      <p>为特异性消融 SCN CCK 神经元，将 AAV-CAG-DIO-taCaspase3-TEVp-WPRE-pA（AAV2/9，滴度 $5.5 \\times 10^{12}$ v.g./mL，购自和元生物 Taitool Bioscience）或对照 AAV-EF1a-DIO-EYFP-WPRE-pA（AAV2/9，滴度 $8.3 \\times 10^{12}$ v.g./mL）以每侧 150 nL 的体积双侧微量注射至 CCK-IRES-Cre 小鼠的 SCN 中。为记录 SCN CCK 和 VIP 神经元的钙活动，将 AAV-EF1a-DIO-GCaMP6s-P2A-nls-tdTomato（AAV2/9，滴度 $8.0 \\times 10^{12}$ v.g./mL）以 100 nL 的体积单侧注射至 CCK-IRES-Cre 和 VIP-IRES-Cre 小鼠的 SCN。为阻断 SCN CCK 神经元的递质囊泡释放，将 AAV-hSyn-DIO-TeNT-P2A-EGFP-WPRE-pA（AAV2/9，滴度 $2.0 \\times 10^{12}$ v.g./mL，购自枢密生物 BrainVTA）以每侧 80 nL 双侧注射至 SCN。为化学遗传抑制 SCN CCK 神经元活性，将 AAV-hSyn-DIO-hM4D(Gi)-EGFP-WPRE-pA（AAV2/9，滴度 $5.0 \\times 10^{12}$ v.g./mL）以每侧 80 nL 双侧注射至 SCN。为光遗传激活 SCN CCK 或 VIP 神经元，将 AAV-hEF1a-DIO-hChR2-EYFP-WPRE-pA（AAV2/9，滴度 $9.6 \\times 10^{12}$ v.g./mL）以每侧 40 nL 双侧注射至 CCK-IRES-Cre 或 VIP-IRES-Cre 小鼠 SCN。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-syringe"></i> 2. 脑立体定位注射与手术 (Virus injection and stereotaxic surgery)</h4>
      <p>所有立体定位手术均在 RWD 脑立体定位仪（型号 68507）上完成。小鼠在异氟烷吸入麻醉下固定，体温由恒温加热毯维持。暴露颅骨后，利用微操微推进器（NARISHIGE MO-10）连接拉制的微细玻璃微吸管（尖端直径 10–30 μm），以 20 nL/min 的流速进行病毒注射。根据标准小鼠脑图谱（Paxinos & Franklin Mouse Brain Atlas, 第 2 版），SCN 的注射坐标设定为：前囟后（AP）-0.550 mm，中线旁开（LM）0.750 mm，硬膜下（DV）5.65 mm，进针倾斜角度为 6 度以避开上矢状窦。对于光遗传操纵，将单侧光纤套管（直径 200 μm；数值孔径 N.A. 0.37；长度 7 mm；安立生物 AniLab）植入 SCN（坐标：AP: -0.550 mm, LM: 0.200 mm, DV: 5.250 mm），并使用牙科水泥和 3M 胶牢固固定于颅骨表面。对于活体光纤记录，将单侧记录光纤（纤芯直径 400 μm；0.57 NA；长 1.5 m；Doric Lenses）植入 SCN（AP: -0.550 mm, LM: 0.200 mm, DV: 5.250 mm）并固定。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-wave-square"></i> 3. 活体光纤钙信号记录 (Fiber photometry recordings)</h4>
      <p>使用 Doric Lenses 光纤记录系统监测自由活动小鼠 SCN 神经元的钙活动。系统包含 Doric 神经科学工作站软件、双通道 LED 驱动器、整合了光电探测器和 405 nm（等吸收参考光，isosbestic control）与 470 nm（GCaMP 激发光）LED 的荧光微型立方体（MiniCube）。激发光以 20 Hz 交替发射 470 nm 和 405 nm 光波，探测器信号采集频率为 12 kHz。405 nm 通道信号专门用于校正和消除动物运动伪影及环境光电噪声干扰。光纤跳线末端光功率控制在 30–40 μW。小鼠在 12L:12D 下适应记录至少 5 天后，转入持续黑暗（DD）、持续光照（LL）约 10 天或长日照（20L:4D）条件。实验结束后通过脑组织学切片验证，若光纤或病毒注射靶点脱靶，该动物的数据将被严格剔除。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-chart-line"></i> 4. 光纤记录数据处理 (Fiber photometry data analysis)</h4>
      <p>采集的原始数据由 MATLAB 定制程序进行解析。提取 470 nm（钙依赖信号）与 405 nm（非钙依赖参比信号），以 30 秒为一个平滑计算窗（session）。以 405 nm 信号作为荧光基线（F），计算荧光变化量 $\\Delta F = F_{475\\text{nm}} - F_{405\\text{nm}}$，相对荧光强度变化率表示为 $\\Delta F/F = (F_{475\\text{nm}} - F_{405\\text{nm}}) / F_{405\\text{nm}}$。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-bolt"></i> 5. 光遗传学操纵与生理遥测节律记录 (Optogenetic manipulations & Telemetry recordings)</h4>
      <p>在植入光纤套管并恢复 1 周后，为小鼠外科手术植入无线生理遥测发射器（TA-F10 植入子，Data Sciences International, DSI）。术后恢复 1 周，将单笼放置在 DSI 接收盘上方，利用 Ponemah 6.5 软件以 1 Hz 连续采集体温（Tb）和自主运动活性（LMA），以 1 分钟平均值保存。小鼠通过轻质柔性跳线连接至 470 nm 蓝光 LED（功率 10–25 mW）。小鼠在恒暗（DD）或恒光（LL）下自由运转至少 5 天以确立稳定的内源相位后，在不同主观节律时间点施加蓝光脉冲刺激（470 nm, 4 Hz, 脉宽 10 ms, 持续 1 小时）。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-thermometer-half"></i> 6. 体温 (Tb) 与自主运动 (LMA) 数据分析 (Tb & LMA analyses)</h4>
      <p>通过检测光遗传刺激前后动物体温与运动活动起始时间（onsets）的偏离程度计算相位反应曲线（PRC）。相移量（phase shift）定义为预测相位（根据刺激前小鼠内源自由运转周期 $\\tau$ 外推计算出的基线相位）与实验观察到的实际相位之间的差值。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-eye"></i> 7. 单分子荧光原位杂交 (smFISH)</h4>
      <p>在预定的节律时间点，小鼠在暗红光下快速实施心室内灌注：先灌注 1× PBS，随后灌注冰预冷的 4% 多聚甲醛（PFA）。快速取脑，4% PFA 4°C 固定 24 小时以上，随后依次经 10%、20%、30% 蔗糖/PBS 梯度脱水沉底。OCT 包埋液包埋并置于液氮中速冻，转入 -80°C 保存。利用 Leica CM1950 冷冻切片机以 10 μm 厚度切片。使用 Advanced Cell Diagnostics (ACD) 的 RNAscope Multiplex Fluorescent Reagent Kit V2 试剂盒对 <em>Mm-Vip</em>、<em>Mm-Avp-C2</em>、<em>Mm-Cck-C3</em> 和 <em>Mm-Fos</em> 特异性探针进行杂交。使用 Nikon A1 激光共聚焦显微镜以 20× 物镜扫描成像。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-vial"></i> 8. 免疫组织化学染色 (Immunohistochemistry)</h4>
      <p>为评估 SCN 神经元的激活程度，在 CT14 给予 1 小时光刺激（4 Hz, 10 ms 脉宽）后检测 FOS 蛋白表达。小鼠经氨基甲酸乙酯麻醉后灌流固定，30% 蔗糖脱水后切片（厚度 30–40 μm）。切片经 5% 正常山羊血清（GS）封闭 2 小时，加入兔抗 FOS 单克隆抗体（1:1000，Cell Signaling Technology，货号 #2250）4°C 孵育过夜；洗涤后加 FITC 标记山羊抗兔二抗（1:200）室温孵育 2 小时，DAPI 封片，共聚焦显微镜采集图像。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-pills"></i> 9. CNO 药物给药 (CNO administration)</h4>
      <p>氯氮平-N-氧化物（Clozapine N-oxide, CNO；Sigma-Aldrich, C0832）溶于无菌生理盐水配制成 1 mg/mL 储存液，避光冻存。临用前用生理盐水稀释至 0.5 mg/mL，以 1 mg/kg（每 30 g 体重注射 0.3 mL）剂量向小鼠腹腔注射（i.p.）。在光脉冲诱导相移实验中，于光脉冲前 1 小时（ZT14 或 ZT22）注射 CNO；在 6 小时前移时差模型中，于时差前 2 天熄灯前 ZT6 注射 CNO。</p>
    </div>

    <div class="method-box">
      <h4 class="method-title"><i class="fas fa-running"></i> 10. 跑轮行为学分析 (Wheel running behavior analyses)</h4>
      <p>小鼠单笼饲养于配有低阻力无线跑轮（Low-Profile Wireless Running Wheel, Med Associates Inc）的笼具中，自由采食饮水。小鼠在 12L:12D（光照强度 200–300 lux）下至少适应 7 天，随后转入 DD、20L:4D 或持续光照 LL（100 lux）。利用卡方周期图（$\\chi^2$ periodogram）以 7 天为一个分析区间计算每只动物的内源运转周期（$\\tau$）。使用 ActogramJ（ImageJ 插件）以 1 分钟为一个时间柱（bin）精确识别运动活动的起始（onset）、结束（offset）和持续时间（alpha）。丧失明显节律的个体不纳入周期计算。</p>
    </div>

    <h3 class="sub-heading">数据定量与统计学分析 (QUANTIFICATION AND STATISTICAL ANALYSIS)</h3>
    <p>具体的统计学检验方法与样本量大小已详细标注于对应图注中。数据分析采用 R 语言（R Software, https://www.r-project.org）及 MATLAB 完成。对于光纤记录钙信号波形比较，采用 Kolmogorov-Smirnov 检验和带有 Tukey HSD 事后检验的双因素方差分析（two-way ANOVA）；对于跑轮行为周期比较，采用非配对 Student's t 检验；对于活动轮廓、起始点、结束点和活动持续时长的比较，采用双因素方差分析；对于体温和自主运动相移分析，采用单因素方差分析或带有 Tukey / Scheffe HSD 事后检验的双因素方差分析。实验数据以均值 $\\pm$ 标准误（Mean $\\pm$ SEM）表示。统计学显著性水平定义如下：n.s. 表示无显著差异（not significant, $p > 0.05$），*$p < 0.05$，**$p < 0.01$，***$p < 0.001$，以及 ****$p < 0.0001$。</p>
  </div>
</section>
"""
