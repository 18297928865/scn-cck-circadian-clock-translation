# -*- coding: utf-8 -*-
"""
Assembler script to build the complete academic literature presentation webpage (index.html).
"""

import sys
import os

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from sections.meta import META_HTML
from sections.intro import INTRO_HTML
from sections.results_1_2 import RESULTS_1_2_HTML
from sections.results_3_4 import RESULTS_3_4_HTML
from sections.results_5_6 import RESULTS_5_6_HTML
from sections.discussion import DISCUSSION_HTML
from sections.methods import METHODS_HTML
from sections.seminar import SEMINAR_HTML

INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>小鼠视交叉上核胆囊收缩素神经元调控生物钟稳健性 - 论文全译与汇报研讨指南 | Neuron 2023</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Inter:wght@300;400;500;600;700;800&family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-body: #f8fafc;
      --bg-card: #ffffff;
      --bg-sidebar: #f1f5f9;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --border-color: #e2e8f0;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-light: #e0f2fe;
      --accent: #d97706;
      --accent-light: #fef3c7;
      --success: #16a34a;
      --success-light: #dcfce7;
      --code-bg: #f1f5f9;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
      --nav-height: 64px;
      --sidebar-width: 280px;
    }

    [data-theme="dark"] {
      --bg-body: #0f172a;
      --bg-card: #1e293b;
      --bg-sidebar: #131d31;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --border-color: #334155;
      --primary: #38bdf8;
      --primary-hover: #7dd3fc;
      --primary-light: #082f49;
      --accent: #f59e0b;
      --accent-light: #451a03;
      --success: #22c55e;
      --success-light: #052e16;
      --code-bg: #0b1120;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.5);
      --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.4);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.5);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.8;
      font-size: 16px;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Reading Progress Bar */
    #progress-bar {
      position: fixed;
      top: 0;
      left: 0;
      height: 4px;
      background: linear-gradient(90deg, #0284c7, #38bdf8, #f59e0b);
      width: 0%;
      z-index: 1000;
      transition: width 0.1s ease;
    }

    /* Top Navigation */
    .top-nav {
      position: sticky;
      top: 0;
      height: var(--nav-height);
      background-color: var(--bg-card);
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      z-index: 900;
      box-shadow: var(--shadow-sm);
    }

    .nav-brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--text-main);
      text-decoration: none;
    }

    .journal-badge {
      background: linear-gradient(135deg, #e11d48, #be123c);
      color: white;
      font-size: 0.75rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn-action {
      background-color: var(--bg-sidebar);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.875rem;
      font-weight: 500;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }

    .btn-action:hover {
      background-color: var(--primary-light);
      color: var(--primary);
      border-color: var(--primary);
    }

    /* Layout Container */
    .app-container {
      display: flex;
      min-height: calc(100vh - var(--nav-height));
      max-width: 1720px;
      margin: 0 auto;
    }

    /* Sidebar Navigation */
    .sidebar {
      width: var(--sidebar-width);
      position: sticky;
      top: var(--nav-height);
      height: calc(100vh - var(--nav-height));
      overflow-y: auto;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      padding: 1.5rem 1rem;
      flex-shrink: 0;
    }

    .sidebar-title {
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      font-weight: 700;
      padding-left: 0.5rem;
    }

    .toc-list {
      list-style: none;
    }

    .toc-item {
      margin-bottom: 0.25rem;
    }

    .toc-link {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.5rem 0.75rem;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      border-radius: 6px;
      transition: all 0.2s ease;
      line-height: 1.4;
    }

    .toc-link:hover {
      background-color: var(--bg-card);
      color: var(--primary);
    }

    .toc-link.active {
      background-color: var(--primary-light);
      color: var(--primary);
      font-weight: 600;
      border-left: 3px solid var(--primary);
    }

    .toc-num {
      font-family: 'Fira Code', monospace;
      font-size: 0.75rem;
      opacity: 0.8;
      flex-shrink: 0;
    }

    /* Main Content Area */
    .main-content {
      flex: 1;
      padding: 2.5rem 3.5rem;
      max-width: 1200px;
      overflow-x: hidden;
    }

    /* Section Cards */
    .section-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 2.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      scroll-margin-top: calc(var(--nav-height) + 1.5rem);
    }

    .section-title-wrap {
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 1.25rem;
      margin-bottom: 2rem;
    }

    .section-title {
      font-size: 1.75rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.75rem;
      letter-spacing: -0.02em;
    }

    .sec-num {
      background: var(--primary-light);
      color: var(--primary);
      font-family: 'Fira Code', monospace;
      font-size: 1.1rem;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      font-weight: 700;
    }

    .section-subtitle {
      color: var(--text-muted);
      font-size: 1rem;
      margin-top: 0.4rem;
    }

    /* Typography & Content */
    p {
      margin-bottom: 1.4rem;
      text-align: justify;
    }

    em {
      font-family: 'Noto Serif SC', serif;
      font-style: italic;
    }

    /* Terminology Explanations Box */
    .term-box {
      background-color: var(--primary-light);
      border-left: 4px solid var(--primary);
      padding: 1.25rem 1.5rem;
      border-radius: 0 8px 8px 0;
      margin: 1.75rem 0;
      font-size: 0.925rem;
    }

    .term-title {
      font-weight: 700;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.5rem;
      font-size: 1rem;
    }

    /* Figure Cards */
    .figure-card {
      background-color: var(--bg-body);
      border: 1px solid var(--border-color);
      border-radius: 10px;
      padding: 1.5rem;
      margin: 2.5rem 0;
      box-shadow: var(--shadow-sm);
    }

    .figure-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }

    .figure-badge {
      background: var(--primary);
      color: white;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.25rem 0.75rem;
      border-radius: 20px;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    .figure-actions {
      display: flex;
      gap: 0.5rem;
    }

    .btn-zoom {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 0.3rem 0.6rem;
      border-radius: 4px;
      font-size: 0.8rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      transition: all 0.2s;
    }

    .btn-zoom:hover {
      color: var(--primary);
      border-color: var(--primary);
    }

    .figure-img-container {
      background-color: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1rem;
      text-align: center;
      margin-bottom: 1.25rem;
      cursor: zoom-in;
      overflow: hidden;
    }

    .figure-img-container img {
      max-width: 100%;
      height: auto;
      border-radius: 4px;
      transition: transform 0.2s ease;
    }

    .figure-caption-zh {
      font-size: 0.925rem;
      line-height: 1.7;
      margin-bottom: 1rem;
      color: var(--text-main);
    }

    .figure-caption-zh strong {
      color: var(--primary);
    }

    .figure-caption-en {
      font-size: 0.825rem;
      color: var(--text-muted);
      border-top: 1px dashed var(--border-color);
      padding-top: 0.75rem;
      line-height: 1.6;
    }

    /* English Original Collapsible Box */
    .en-source-box {
      background-color: var(--bg-sidebar);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin-top: 2rem;
      font-size: 0.875rem;
    }

    .en-source-title {
      font-weight: 700;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      margin-bottom: 0.75rem;
      user-select: none;
    }

    .en-orig {
      color: var(--text-muted);
      font-size: 0.875rem;
      line-height: 1.7;
      margin-bottom: 1rem;
      text-align: justify;
    }

    /* Highlights & Abstract Boxes */
    .highlights-box {
      background-color: var(--accent-light);
      border-left: 4px solid var(--accent);
      padding: 1.25rem 1.5rem;
      border-radius: 0 8px 8px 0;
      margin: 1.5rem 0;
    }

    .highlights-title {
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.5rem;
      font-size: 1.05rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* Seminar Section Specific Styling */
    .seminar-section {
      border: 2px solid var(--primary);
      background: linear-gradient(180deg, var(--bg-card) 0%, var(--bg-sidebar) 100%);
    }

    .seminar-block {
      margin-bottom: 2.5rem;
    }

    .seminar-heading {
      font-size: 1.35rem;
      color: var(--text-main);
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      border-bottom: 2px dashed var(--border-color);
      padding-bottom: 0.5rem;
    }

    .novelty-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
      margin-top: 1rem;
    }

    .novelty-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .novelty-card:hover {
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--primary);
    }

    .novelty-badge {
      align-self: flex-start;
      background-color: var(--primary-light);
      color: var(--primary);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      font-family: 'Fira Code', monospace;
    }

    .novelty-card h4 {
      font-size: 1rem;
      color: var(--text-main);
      line-height: 1.4;
    }

    .novelty-card p {
      font-size: 0.875rem;
      color: var(--text-muted);
      margin-bottom: 0;
      line-height: 1.6;
    }

    .significance-box {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.5rem;
    }

    .styled-list {
      padding-left: 1.25rem;
    }

    .styled-list li {
      margin-bottom: 1rem;
      line-height: 1.7;
    }

    .bg-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1.5rem;
      margin-bottom: 1.25rem;
    }

    .bg-card h4 {
      color: var(--primary);
      margin-bottom: 0.75rem;
      font-size: 1.1rem;
    }

    .bg-card ul, .bg-card ol {
      padding-left: 1.25rem;
      margin-bottom: 0.75rem;
    }

    .bg-card li {
      margin-bottom: 0.5rem;
      font-size: 0.925rem;
      line-height: 1.6;
    }

    .academic-table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0;
      font-size: 0.875rem;
    }

    .academic-table th, .academic-table td {
      border: 1px solid var(--border-color);
      padding: 0.75rem 1rem;
      text-align: left;
    }

    .academic-table th {
      background-color: var(--bg-sidebar);
      font-weight: 700;
      color: var(--text-main);
    }

    .qa-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      margin-bottom: 1.25rem;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }

    .qa-q {
      background-color: var(--bg-sidebar);
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
    }

    .qa-badge-q {
      background-color: #ef4444;
      color: white;
      font-size: 0.75rem;
      font-weight: 800;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      flex-shrink: 0;
      font-family: 'Fira Code', monospace;
    }

    .qa-q strong {
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.5;
    }

    .qa-a {
      padding: 1.25rem;
      font-size: 0.925rem;
      line-height: 1.7;
    }

    .qa-badge-a {
      display: inline-block;
      background-color: var(--success-light);
      color: var(--success);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      margin-bottom: 0.75rem;
    }

    .qa-a ol, .qa-a ul {
      padding-left: 1.25rem;
      margin-top: 0.5rem;
    }

    .qa-a li {
      margin-bottom: 0.5rem;
    }

    /* Lightbox Modal */
    #lightbox-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background-color: rgba(0, 0, 0, 0.9);
      z-index: 2000;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      padding: 2rem;
    }

    #lightbox-img {
      max-width: 92%;
      max-height: 85vh;
      object-fit: contain;
      border-radius: 4px;
      box-shadow: 0 0 25px rgba(0, 0, 0, 0.8);
      transition: transform 0.2s ease;
    }

    #lightbox-caption {
      color: #f1f5f9;
      font-size: 0.9rem;
      margin-top: 1rem;
      text-align: center;
      max-width: 80%;
    }

    .close-lightbox {
      position: absolute;
      top: 1.5rem;
      right: 2rem;
      color: #ffffff;
      font-size: 2rem;
      cursor: pointer;
      background: none;
      border: none;
    }

    /* Back to Top */
    #back-to-top {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background-color: var(--primary);
      color: white;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: none;
      display: none;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: var(--shadow-lg);
      transition: all 0.2s ease;
      z-index: 800;
    }

    #back-to-top:hover {
      background-color: var(--primary-hover);
      transform: translateY(-3px);
    }

    /* Responsive adjustments */
    @media (max-width: 1024px) {
      .sidebar {
        display: none;
      }
      .main-content {
        padding: 1.5rem;
      }
      .section-card {
        padding: 1.5rem;
      }
    }
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div id="progress-bar"></div>

  <!-- Top Navigation Bar -->
  <header class="top-nav">
    <a href="#" class="nav-brand">
      <span class="journal-badge">Neuron</span>
      <span>SCN CCK 神经元与生物钟稳健性</span>
    </a>
    <div class="nav-actions">
      <button class="btn-action" id="theme-toggle" title="切换深色/浅色模式">
        <i class="fas fa-moon"></i> <span>深色模式</span>
      </button>
      <button class="btn-action" id="en-toggle" title="显示或隐藏英文原文">
        <i class="fas fa-language"></i> <span>隐藏英文原文</span>
      </button>
      <a href="https://doi.org/10.1016/j.neuron.2023.04.026" target="_blank" rel="noopener" class="btn-action" style="text-decoration:none;">
        <i class="fas fa-external-link-alt"></i> <span>原刊 DOI</span>
      </a>
    </div>
  </header>

  <!-- Main Container -->
  <div class="app-container">

    <!-- Sticky Table of Contents Sidebar -->
    <aside class="sidebar">
      <div class="sidebar-title">论文导航目录 (Contents)</div>
      <ul class="toc-list">
        <li class="toc-item"><a href="#meta-info" class="toc-link"><span class="toc-num">01</span><span>论文概要与摘要</span></a></li>
        <li class="toc-item"><a href="#introduction" class="toc-link"><span class="toc-num">02</span><span>引言 (Introduction)</span></a></li>
        <li class="toc-item"><a href="#results-1" class="toc-link"><span class="toc-num">03</span><span>结果 1: 钙活动动力学</span></a></li>
        <li class="toc-item"><a href="#results-2" class="toc-link"><span class="toc-num">04</span><span>结果 2: 消融导致失稳</span></a></li>
        <li class="toc-item"><a href="#results-3" class="toc-link"><span class="toc-num">05</span><span>结果 3: 激活抵消光延迟</span></a></li>
        <li class="toc-item"><a href="#results-4" class="toc-link"><span class="toc-num">06</span><span>结果 4: 神经网动力学重构</span></a></li>
        <li class="toc-item"><a href="#results-5" class="toc-link"><span class="toc-num">07</span><span>结果 5: 时差反应与制动</span></a></li>
        <li class="toc-item"><a href="#discussion" class="toc-link"><span class="toc-num">08</span><span>讨论 (Discussion)</span></a></li>
        <li class="toc-item"><a href="#methods" class="toc-link"><span class="toc-num">09</span><span>实验方法 (STAR Methods)</span></a></li>
        <li class="toc-item"><a href="#seminar-guide" class="toc-link"><span class="toc-num">10</span><span>汇报与答辩指南</span></a></li>
      </ul>
    </aside>

    <!-- Main Content Reader -->
    <main class="main-content">
      <!-- REPLACE_META_HTML -->
      <!-- REPLACE_INTRO_HTML -->
      <!-- REPLACE_RESULTS_1_2_HTML -->
      <!-- REPLACE_RESULTS_3_4_HTML -->
      <!-- REPLACE_RESULTS_5_6_HTML -->
      <!-- REPLACE_DISCUSSION_HTML -->
      <!-- REPLACE_METHODS_HTML -->
      <!-- REPLACE_SEMINAR_HTML -->
    </main>

  </div>

  <!-- Back to Top Button -->
  <button id="back-to-top" title="返回顶部"><i class="fas fa-arrow-up"></i></button>

  <!-- Lightbox Modal -->
  <div id="lightbox-modal">
    <button class="close-lightbox" title="关闭"><i class="fas fa-times"></i></button>
    <img id="lightbox-img" src="" alt="放大图片">
    <div id="lightbox-caption"></div>
  </div>

  <script>
    // Theme toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElem = document.documentElement;
    let currentTheme = localStorage.getItem('theme') || 'light';
    htmlElem.setAttribute('data-theme', currentTheme);
    updateThemeBtn();

    themeToggleBtn.addEventListener('click', () => {
      currentTheme = currentTheme === 'light' ? 'dark' : 'light';
      htmlElem.setAttribute('data-theme', currentTheme);
      localStorage.setItem('theme', currentTheme);
      updateThemeBtn();
    });

    function updateThemeBtn() {
      if (currentTheme === 'dark') {
        themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i> <span>浅色模式</span>';
      } else {
        themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i> <span>深色模式</span>';
      }
    }

    // Toggle English text
    const enToggleBtn = document.getElementById('en-toggle');
    let enVisible = true;
    enToggleBtn.addEventListener('click', () => {
      enVisible = !enVisible;
      const enBoxes = document.querySelectorAll('.en-source-box, .figure-caption-en');
      enBoxes.forEach(box => {
        box.style.display = enVisible ? 'block' : 'none';
      });
      enToggleBtn.innerHTML = enVisible 
        ? '<i class="fas fa-language"></i> <span>隐藏英文原文</span>' 
        : '<i class="fas fa-language"></i> <span>显示英文原文</span>';
    });

    // Reading progress & Scrollspy
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progress-bar').style.width = scrolled + '%';

      // Back to top button
      const btt = document.getElementById('back-to-top');
      if (winScroll > 400) {
        btt.style.display = 'flex';
      } else {
        btt.style.display = 'none';
      }

      // Scrollspy
      const sections = document.querySelectorAll('section[id]');
      const navLinks = document.querySelectorAll('.toc-link');
      let currentSectionId = '';

      sections.forEach(sec => {
        const top = sec.offsetTop - 120;
        if (winScroll >= top) {
          currentSectionId = sec.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + currentSectionId) {
          link.classList.add('active');
        }
      });
    });

    document.getElementById('back-to-top').addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Lightbox functionality
    const modal = document.getElementById('lightbox-modal');
    const modalImg = document.getElementById('lightbox-img');
    const modalCaption = document.getElementById('lightbox-caption');
    const closeBtn = document.querySelector('.close-lightbox');

    document.querySelectorAll('.figure-img-container img, .btn-zoom').forEach(item => {
      item.addEventListener('click', (e) => {
        let imgElem = e.target.tagName === 'IMG' ? e.target : e.target.closest('.figure-card').querySelector('img');
        if (imgElem) {
          modal.style.display = 'flex';
          modalImg.src = imgElem.src;
          modalCaption.textContent = imgElem.alt || '论文插图全高清视图';
        }
      });
    });

    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });

    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.style.display === 'flex') {
        modal.style.display = 'none';
      }
    });
  </script>
</body>
</html>
"""

def build():
    print("Assembling index.html from sections...")
    full_html = INDEX_HTML_TEMPLATE
    full_html = full_html.replace("<!-- REPLACE_META_HTML -->", META_HTML)
    full_html = full_html.replace("<!-- REPLACE_INTRO_HTML -->", INTRO_HTML)
    full_html = full_html.replace("<!-- REPLACE_RESULTS_1_2_HTML -->", RESULTS_1_2_HTML)
    full_html = full_html.replace("<!-- REPLACE_RESULTS_3_4_HTML -->", RESULTS_3_4_HTML)
    full_html = full_html.replace("<!-- REPLACE_RESULTS_5_6_HTML -->", RESULTS_5_6_HTML)
    full_html = full_html.replace("<!-- REPLACE_DISCUSSION_HTML -->", DISCUSSION_HTML)
    full_html = full_html.replace("<!-- REPLACE_METHODS_HTML -->", METHODS_HTML)
    full_html = full_html.replace("<!-- REPLACE_SEMINAR_HTML -->", SEMINAR_HTML)

    output_path = os.path.join(current_dir, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"Successfully generated {output_path} ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    build()
