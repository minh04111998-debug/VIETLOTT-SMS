#!/usr/bin/env python3
"""
Test generator for custom themed cards.
"""
import subprocess
from pathlib import Path

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not Path(EDGE).exists():
    EDGE = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

test_html = Path(r"f:\VIETLOTT-SMS\references\ba-book\test_card.html")
test_png = Path(r"f:\VIETLOTT-SMS\references\ba-book\test_card.png")

html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1200px;
  height: 675px;
  overflow: hidden;
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: #0f172a;
}
.card {
  width: 1200px;
  height: 675px;
  position: relative;
  background: radial-gradient(circle at 15% 20%, #1e293b 0%, #0f172a 100%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 36px 48px 28px 48px;
  color: #f8fafc;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.badge {
  background: rgba(56, 189, 248, 0.15);
  border: 1px solid #38bdf8;
  color: #38bdf8;
  padding: 6px 14px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 14px;
  letter-spacing: 0.5px;
}
.logo {
  font-size: 24px;
  font-weight: 900;
  color: #94a3b8;
  letter-spacing: -0.5px;
}
.logo span { color: #f8fafc; }
.title-area {
  text-align: center;
  margin-top: 10px;
}
.headline {
  font-size: 42px;
  font-weight: 900;
  color: #38bdf8;
  line-height: 1.2;
  margin-bottom: 8px;
}
.subheadline {
  font-size: 26px;
  font-weight: 600;
  color: #cbd5e1;
  max-width: 900px;
  margin: 0 auto;
}
.graphic-area {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px 0;
}
.footer {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #64748b;
  font-weight: 600;
}
</style>
</head>
<body>
<div class="card">
  <div class="header">
    <div class="badge">SYSTEM ARCHITECTURE · DDD</div>
    <div class="logo">iTBA <span>Mentor</span></div>
  </div>
  <div class="title-area">
    <div class="headline">Domain-Driven Design (DDD) là gì?</div>
    <div class="subheadline">Và tại sao BA nên biết sớm để không xây hệ thống rời rạc?</div>
  </div>
  <div class="graphic-area">
    <svg width="600" height="260" viewBox="0 0 600 260">
      <!-- Domain node 1 -->
      <rect x="30" y="50" width="160" height="150" rx="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" />
      <text x="110" y="85" text-anchor="middle" fill="#38bdf8" font-size="16" font-weight="bold">SALES CONTEXT</text>
      <rect x="50" y="110" width="120" height="30" rx="6" fill="#334155" />
      <text x="110" y="130" text-anchor="middle" fill="#f8fafc" font-size="12">Order Aggregate</text>
      <rect x="50" y="150" width="120" height="30" rx="6" fill="#334155" />
      <text x="110" y="170" text-anchor="middle" fill="#94a3b8" font-size="12">Customer Info</text>
      
      <!-- Connection line -->
      <line x1="190" y1="125" x2="250" y2="125" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,4" />
      <circle cx="220" cy="125" r="14" fill="#f59e0b" />
      <text x="220" y="130" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="bold">API</text>
      
      <!-- Domain node 2 -->
      <rect x="250" y="30" width="170" height="190" rx="16" fill="#1e293b" stroke="#10b981" stroke-width="2.5" />
      <text x="335" y="65" text-anchor="middle" fill="#10b981" font-size="16" font-weight="bold">INVENTORY CONTEXT</text>
      <rect x="270" y="90" width="130" height="30" rx="6" fill="#334155" />
      <text x="335" y="110" text-anchor="middle" fill="#f8fafc" font-size="12">Stock Balance</text>
      <rect x="270" y="130" width="130" height="30" rx="6" fill="#334155" />
      <text x="335" y="150" text-anchor="middle" fill="#f8fafc" font-size="12">Warehouse Event</text>
      <rect x="270" y="170" width="130" height="30" rx="6" fill="#334155" />
      <text x="335" y="190" text-anchor="middle" fill="#94a3b8" font-size="12">Reserved Items</text>

      <!-- Connection line -->
      <line x1="420" y1="125" x2="480" y2="125" stroke="#ec4899" stroke-width="3" stroke-dasharray="6,4" />
      <circle cx="450" cy="125" r="14" fill="#ec4899" />
      <text x="450" y="130" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">MSG</text>
      
      <!-- Domain node 3 -->
      <rect x="480" y="50" width="100" height="150" rx="16" fill="#1e293b" stroke="#a855f7" stroke-width="2.5" />
      <text x="530" y="85" text-anchor="middle" fill="#a855f7" font-size="15" font-weight="bold">BILLING</text>
      <rect x="495" y="110" width="70" height="30" rx="6" fill="#334155" />
      <text x="530" y="130" text-anchor="middle" fill="#f8fafc" font-size="12">Invoice</text>
      <rect x="495" y="150" width="70" height="30" rx="6" fill="#334155" />
      <text x="530" y="170" text-anchor="middle" fill="#94a3b8" font-size="12">Tax Rule</text>
    </svg>
  </div>
  <div class="footer">
    <div>Day 23/100 · Sách 100 ngày làm BA</div>
    <div>Nguyễn Bá Phú — ITBA Mentor</div>
  </div>
</div>
</body>
</html>
"""

test_html.write_text(html_content, encoding="utf-8")

cmd = [
    EDGE,
    "--headless",
    "--disable-gpu",
    "--force-device-scale-factor=1",
    "--window-size=1200,675",
    f"--screenshot={test_png}",
    str(test_html),
]
subprocess.run(cmd, check=True)
print(f"Generated test_png: exists={test_png.exists()}, size={test_png.stat().st_size} bytes")
