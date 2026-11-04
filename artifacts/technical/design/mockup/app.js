/* ==========================================================================
   VIETLOTT SMS 2.0 - INTERACTIVE MOCKUP JAVASCRIPT ENGINE
   Controls: 6 Screen Views, Dark Mode Switching, 3 Micro-Animations, 
   Streamlined 3-Step Purchase Flow, Gamification & Celebration Confetti.
   ========================================================================== */

// --- Global App State ---
const state = {
  currentScreen: 'home',
  isDarkMode: false,
  selectedGame: 'mega', // 'mega', 'power', 'bingo', 'lotto535', 'max3d'
  selectedNumbers: [],
  maxNumbers: 6,
  maxNumberVal: 45,
  includeCrossSell: false,
  bingoOption: 'lon',
  bingoAmount: 10,
  spinsRemaining: 1,
  streakDays: 6,
  hasCheckedInToday: false
};

// --- DOM Loaded Initialization ---
document.addEventListener('DOMContentLoaded', () => {
  initClock();
  initBingoCountdown();
  initBallsGrid(45);
  initThemeToggles();
  initButtonRippleEffects();
  initConfettiCanvas();
  
  // Set default active tab
  switchScreen('home');
});

/* --------------------------------------------------------------------------
   1. SCREEN & TAB NAVIGATION ENGINE
   -------------------------------------------------------------------------- */
function switchScreen(screenId) {
  state.currentScreen = screenId;

  // 1. Toggle screen views
  const screens = document.querySelectorAll('.screen-view');
  screens.forEach(screen => {
    if (screen.id === `screen-${screenId}`) {
      screen.classList.add('active');
    } else {
      screen.classList.remove('active');
    }
  });

  // 2. Update Bottom Nav Tabs
  const tabs = document.querySelectorAll('.nav-tab');
  let activeIndex = 0;

  tabs.forEach((tab, index) => {
    if (tab.dataset.target === screenId) {
      tab.classList.add('active');
      activeIndex = index;
    } else {
      tab.classList.remove('active');
    }
  });

  // 3. Move Nav Active Indicator Line
  const indicator = document.getElementById('navIndicator');
  if (indicator) {
    indicator.style.transform = `translateX(${activeIndex * 100}%)`;
  }

  // 4. Update Dropdown Select
  const dropdown = document.getElementById('screenSelect');
  if (dropdown && dropdown.value !== screenId) {
    dropdown.value = screenId;
  }

  // Scroll to top of app content
  const content = document.getElementById('appContentScroll');
  if (content) content.scrollTop = 0;
}

/* --------------------------------------------------------------------------
   2. DARK MODE THEME TOGGLER
   -------------------------------------------------------------------------- */
function initThemeToggles() {
  const toggleRootBtn = document.getElementById('themeToggleSwitch');
  const toggleTopBtn = document.getElementById('toggleThemeTopBtn');
  const toggleProfileBtn = document.getElementById('profileThemeToggle');

  const toggleHandler = () => {
    state.isDarkMode = !state.isDarkMode;
    if (state.isDarkMode) {
      document.documentElement.classList.add('dark-theme');
    } else {
      document.documentElement.classList.remove('dark-theme');
    }
    // Sync top btn text
    if (toggleTopBtn) {
      toggleTopBtn.querySelector('.theme-text').textContent = state.isDarkMode ? 'Light Mode' : 'Dark Mode';
    }
  };

  if (toggleRootBtn) toggleRootBtn.addEventListener('click', toggleHandler);
  if (toggleTopBtn) toggleTopBtn.addEventListener('click', toggleHandler);
  if (toggleProfileBtn) toggleProfileBtn.addEventListener('click', toggleHandler);
}

/* --------------------------------------------------------------------------
   3. MICRO-ANIMATION 1: BUTTON RIPPLE & PRESS SCALE
   -------------------------------------------------------------------------- */
function initButtonRippleEffects() {
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('button, .ball-choice, .turbo-opt-btn, .chip');
    if (!btn) return;

    // Trigger scale animation effect
    btn.style.transform = 'scale(0.95)';
    setTimeout(() => {
      btn.style.transform = '';
    }, 150);
  });
}

/* --------------------------------------------------------------------------
   4. MICRO-ANIMATION 2: CELEBRATION CONFETTI CANVAS
   -------------------------------------------------------------------------- */
let confettiCtx = null;
let confettiParticles = [];
let confettiAnimationId = null;

function initConfettiCanvas() {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas) return;
  
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  confettiCtx = canvas.getContext('2d');

  window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  });
}

function triggerCelebrationConfetti() {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas || !confettiCtx) return;

  confettiParticles = [];
  const colors = ['#FFD700', '#E31937', '#00C853', '#FFFFFF', '#3B82F6', '#FF8F00'];

  for (let i = 0; i < 120; i++) {
    confettiParticles.push({
      x: window.innerWidth / 2,
      y: window.innerHeight / 2 - 100,
      vx: (Math.random() - 0.5) * 14,
      vy: Math.random() * -12 - 4,
      size: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      rotation: Math.random() * 360,
      rSpeed: (Math.random() - 0.5) * 10,
      opacity: 1
    });
  }

  if (confettiAnimationId) cancelAnimationFrame(confettiAnimationId);
  renderConfetti();

  // Play sound indicator log
  console.log('🎉 Confetti Celebration Activated!');
}

function renderConfetti() {
  const canvas = document.getElementById('confettiCanvas');
  if (!canvas || !confettiCtx) return;

  confettiCtx.clearRect(0, 0, canvas.width, canvas.height);

  let activeCount = 0;
  confettiParticles.forEach(p => {
    if (p.opacity <= 0) return;
    activeCount++;

    p.x += p.vx;
    p.y += p.vy;
    p.vy += 0.3; // gravity
    p.rotation += p.rSpeed;
    p.opacity -= 0.008;

    confettiCtx.save();
    confettiCtx.translate(p.x, p.y);
    confettiCtx.rotate((p.rotation * Math.PI) / 180);
    confettiCtx.globalAlpha = Math.max(0, p.opacity);
    confettiCtx.fillStyle = p.color;
    confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
    confettiCtx.restore();
  });

  if (activeCount > 0) {
    confettiAnimationId = requestAnimationFrame(renderConfetti);
  } else {
    confettiCtx.clearRect(0, 0, canvas.width, canvas.height);
  }
}

/* --------------------------------------------------------------------------
   5. MICRO-ANIMATION 3: CLOCK & BINGO COUNTDOWN TIMER
   -------------------------------------------------------------------------- */
function initClock() {
  const updateClock = () => {
    const now = new Date();
    const hrs = String(now.getHours()).padStart(2, '0');
    const mins = String(now.getMinutes()).padStart(2, '0');
    const clockEl = document.getElementById('statusClock');
    if (clockEl) clockEl.textContent = `${hrs}:${mins}`;
  };
  updateClock();
  setInterval(updateClock, 10000);
}

let bingoSeconds = 222; // 03:42

function initBingoCountdown() {
  const timerTick = document.getElementById('timerTick');
  setInterval(() => {
    if (!timerTick) return;
    bingoSeconds--;
    if (bingoSeconds < 0) bingoSeconds = 360; // Reset to 6 mins

    const m = String(Math.floor(bingoSeconds / 60)).padStart(2, '0');
    const s = String(bingoSeconds % 60).padStart(2, '0');
    timerTick.textContent = `${m}:${s}`;
  }, 1000);
}

/* --------------------------------------------------------------------------
   6. BINGO18 TURBO FAST-PLAY WIDGET MECHANICS
   -------------------------------------------------------------------------- */
function selectBingoOpt(btn) {
  document.querySelectorAll('.turbo-opt-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  state.bingoOption = btn.dataset.opt;
}

function selectChip(btn, amount) {
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  btn.classList.add('active');
  state.bingoAmount = amount;
}

function executeTurboCheckout() {
  // Simulate 1-tap fast checkout
  const btn = document.getElementById('btnTurboSubmit');
  if (btn) {
    btn.disabled = true;
    btn.style.opacity = '0.7';
    btn.querySelector('.btn-text').textContent = '⏳ Đang Chốt Đơn Turbo (Idempotent Key...)...';
  }

  setTimeout(() => {
    if (btn) {
      btn.disabled = false;
      btn.style.opacity = '1';
      btn.querySelector('.btn-text').textContent = '⚡ Chốt Đơn Turbo (1-Tap Checkout)';
    }
    triggerCelebrationConfetti();
    alert(`🎉 THÀNH CÔNG! Đơn BINGO18 [${state.bingoOption.toUpperCase()} - ${state.bingoAmount}.000đ] đã được chốt tức thì trong 1.8 giây với Idempotency Key!`);
  }, 1800);
}

/* --------------------------------------------------------------------------
   7. STREAMLINED 3-STEP PURCHASE FLOW MECHANICS
   -------------------------------------------------------------------------- */
function startPurchaseFlow(gameType) {
  state.selectedGame = gameType;
  state.selectedNumbers = [];

  if (gameType === 'power') {
    state.maxNumbers = 6;
    state.maxNumberVal = 55;
    document.getElementById('selectedGameName').textContent = 'Power 6/55';
    document.querySelector('.step-desc').textContent = 'Chọn 6 số may mắn từ 01 đến 55';
  } else if (gameType === 'lotto535') {
    state.maxNumbers = 5;
    state.maxNumberVal = 35;
    document.getElementById('selectedGameName').textContent = 'Lotto 5/35 (Top Gainer)';
    document.querySelector('.step-desc').textContent = 'Chọn 5 số may mắn từ 01 đến 35';
  } else if (gameType === 'bingo') {
    switchScreen('home');
    const turboWidget = document.querySelector('.turbo-bingo-widget');
    if (turboWidget) turboWidget.scrollIntoView({ behavior: 'smooth' });
    return;
  } else {
    // Mega 6/45 default
    state.maxNumbers = 6;
    state.maxNumberVal = 45;
    document.getElementById('selectedGameName').textContent = 'Mega 6/45';
    document.querySelector('.step-desc').textContent = 'Chọn 6 số may mắn từ 01 đến 45';
  }

  initBallsGrid(state.maxNumberVal);
  updateSelectedBallsUI();
  switchScreen('purchase');
  goToStep(1);
}

function initBallsGrid(maxVal) {
  const grid = document.getElementById('ballsGridSelector');
  if (!grid) return;
  grid.innerHTML = '';

  for (let i = 1; i <= maxVal; i++) {
    const numStr = String(i).padStart(2, '0');
    const ball = document.createElement('button');
    ball.className = 'ball-choice';
    ball.textContent = numStr;
    ball.onclick = () => toggleBallSelection(numStr, ball);
    grid.appendChild(ball);
  }
}

function toggleBallSelection(numStr, ballEl) {
  const index = state.selectedNumbers.indexOf(numStr);
  if (index > -1) {
    state.selectedNumbers.splice(index, 1);
    ballEl.classList.remove('selected');
  } else {
    if (state.selectedNumbers.length >= state.maxNumbers) {
      alert(`Bạn chỉ được chọn tối đa ${state.maxNumbers} số!`);
      return;
    }
    state.selectedNumbers.push(numStr);
    ballEl.classList.add('selected');
  }
  updateSelectedBallsUI();
}

function quickPickRandom() {
  state.selectedNumbers = [];
  while (state.selectedNumbers.length < state.maxNumbers) {
    const rand = String(Math.floor(Math.random() * state.maxNumberVal) + 1).padStart(2, '0');
    if (!state.selectedNumbers.includes(rand)) {
      state.selectedNumbers.push(rand);
    }
  }
  state.selectedNumbers.sort((a, b) => parseInt(a) - parseInt(b));
  updateGridSelections();
  updateSelectedBallsUI();
}

function quickPickAI() {
  quickPickRandom();
}

function clearSelectedNumbers() {
  state.selectedNumbers = [];
  updateGridSelections();
  updateSelectedBallsUI();
}

function updateGridSelections() {
  const balls = document.querySelectorAll('.ball-choice');
  balls.forEach(b => {
    if (state.selectedNumbers.includes(b.textContent)) {
      b.classList.add('selected');
    } else {
      b.classList.remove('selected');
    }
  });
}

function updateSelectedBallsUI() {
  const container = document.getElementById('selectedBallsDisplay');
  if (!container) return;

  container.innerHTML = '';
  for (let i = 0; i < state.maxNumbers; i++) {
    const slot = document.createElement('span');
    if (state.selectedNumbers[i]) {
      slot.className = 'ball-slot filled';
      slot.textContent = state.selectedNumbers[i];
    } else {
      slot.className = 'ball-slot empty';
      slot.textContent = '?';
    }
    container.appendChild(slot);
  }

  // Update footer price
  const btnNext = document.getElementById('btnGoToStep2');
  if (btnNext) {
    if (state.selectedNumbers.length === state.maxNumbers) {
      btnNext.disabled = false;
      btnNext.style.opacity = '1';
    } else {
      btnNext.disabled = true;
      btnNext.style.opacity = '0.5';
    }
  }
}

function goToStep(stepNum) {
  // Step indicators
  document.querySelectorAll('.step-item').forEach((item, idx) => {
    if (idx + 1 <= stepNum) item.classList.add('active');
    else item.classList.remove('active');
  });

  // Step contents
  document.getElementById('purchaseStep1').classList.add('hidden');
  document.getElementById('purchaseStep2').classList.add('hidden');
  document.getElementById('purchaseStep3').classList.add('hidden');

  document.getElementById(`purchaseStep${stepNum}`).classList.remove('hidden');

  if (stepNum === 2) {
    // Populate summary
    document.getElementById('summaryGameName').textContent = getGameName(state.selectedGame);
    const ballsBox = document.getElementById('summaryBalls');
    ballsBox.innerHTML = '';
    state.selectedNumbers.forEach(n => {
      const b = document.createElement('span');
      b.className = 'ball-mini';
      b.textContent = n;
      ballsBox.appendChild(b);
    });
    updateFinalPayAmount();
  }

  if (stepNum === 3) {
    startIdempotentPaymentSimulation();
  }
}

function getGameName(type) {
  if (type === 'power') return 'Power 6/55';
  if (type === 'lotto535') return 'Lotto 5/35';
  if (type === 'max3d') return 'Max 3D Pro';
  return 'Mega 6/45';
}

function toggleCrossSell(chk) {
  state.includeCrossSell = chk.checked;
  updateFinalPayAmount();
}

function updateFinalPayAmount() {
  const base = 10000;
  const total = state.includeCrossSell ? base + 10000 : base;
  const payEl = document.getElementById('finalPayAmount');
  if (payEl) payEl.textContent = `${total.toLocaleString('vi-VN')}đ`;
}

function selectPaymentOpt(card, type) {
  document.querySelectorAll('.payment-opt-card').forEach(c => c.classList.remove('active'));
  card.classList.add('active');
  card.querySelector('input').checked = true;
}

/* Simulated Idempotent Payment */
let payTimer = null;

function startIdempotentPaymentSimulation() {
  document.getElementById('idempotentBox').classList.remove('hidden');
  document.getElementById('paymentSuccessInvoice').classList.add('hidden');

  // Random Idempotency Key
  const randKey = 'IDEM-20260811-' + Math.floor(10000 + Math.random() * 90000);
  document.getElementById('idemKeyVal').textContent = randKey;

  let countdown = 3;
  const numEl = document.getElementById('payCountdownNum');
  if (numEl) numEl.textContent = countdown;

  if (payTimer) clearInterval(payTimer);

  payTimer = setInterval(() => {
    countdown--;
    if (numEl) numEl.textContent = countdown;

    if (countdown <= 0) {
      clearInterval(payTimer);
      finishPaymentSuccess();
    }
  }, 1000);
}

function triggerBiometricAuth() {
  if (payTimer) clearInterval(payTimer);
  finishPaymentSuccess();
}

function finishPaymentSuccess() {
  document.getElementById('idempotentBox').classList.add('hidden');
  const invoice = document.getElementById('paymentSuccessInvoice');
  invoice.classList.remove('hidden');

  document.getElementById('invGameName').textContent = getGameName(state.selectedGame);
  document.getElementById('invBalls').textContent = state.selectedNumbers.join(' - ');
  const total = state.includeCrossSell ? 20000 : 10000;
  document.getElementById('invAmount').textContent = `${total.toLocaleString('vi-VN')}đ`;

  triggerCelebrationConfetti();
}

function resetPurchaseFlow() {
  state.selectedNumbers = [];
  state.includeCrossSell = false;
  const chk = document.getElementById('chkAddCrossSell');
  if (chk) chk.checked = false;
  startPurchaseFlow('mega');
}

/* --------------------------------------------------------------------------
   8. GAMIFICATION & SYNDICATE INTERACTIVITY
   -------------------------------------------------------------------------- */
function claimDay7Streak() {
  if (state.hasCheckedInToday) {
    alert('Bạn đã điểm danh ngày hôm nay rồi!');
    return;
  }
  state.hasCheckedInToday = true;
  state.spinsRemaining++;
  
  const box = document.getElementById('day7Box');
  if (box) {
    box.classList.remove('today-gift');
    box.classList.add('checked');
    box.innerHTML = '<span>N7</span><span class="check-mark">✓</span>';
  }

  document.getElementById('streakCount').textContent = '7/7';
  document.getElementById('spinsCount').textContent = `${state.spinsRemaining} Lượt`;

  triggerCelebrationConfetti();
  alert('🎉 CHÚC MỪNG! Bạn đã hoàn thành chuỗi 7 ngày điểm danh & nhận +1 Lượt quay Vòng Quay 6 Năm!');
}

let isSpinning = false;

function spinLuckyWheel() {
  if (state.spinsRemaining <= 0) {
    alert('Bạn đã hết lượt quay! Hãy mua vé hoặc điểm danh để tích thêm lượt.');
    return;
  }
  if (isSpinning) return;

  isSpinning = true;
  state.spinsRemaining--;
  document.getElementById('spinsCount').textContent = `${state.spinsRemaining} Lượt`;

  const disc = document.getElementById('wheelDisc');
  const randomDegrees = 1440 + 60 * Math.floor(Math.random() * 6) + 30; // Spin at least 4 full rounds

  if (disc) {
    disc.style.transform = `rotate(${randomDegrees}deg)`;
  }

  setTimeout(() => {
    isSpinning = false;
    triggerCelebrationConfetti();
    alert('🎁 CHÚC MỪNG! Bạn đã quay trúng: [Voucher Mua Vé 20.000 VNĐ] nhân dịp Kỷ Niệm 6 Năm!');
  }, 3200);
}

function openCreateSyndicateModal() {
  const modal = document.getElementById('modalCreateSyndicate');
  if (modal) modal.classList.remove('hidden');
}

function submitCreateSyndicate() {
  closeModal('modalCreateSyndicate');
  triggerCelebrationConfetti();
  alert('🎉 THÀNH CÔNG! Phòng Mua Vé Nhóm #SYN-8813 đã được tạo. Hợp đồng mua chung số hóa đã phát hành link mời nhóm!');
}

function shareSyndicateLink(roomId) {
  alert(`🔗 Đã chép link mời tham gia phòng ${roomId} vào khay nhớ tạm! Gửi ngay cho bạn bè qua Zalo/SMS.`);
}

function joinSyndicateRoom(roomId) {
  triggerCelebrationConfetti();
  alert(`🎉 THÀNH CÔNG! Bạn đã nộp 84.000đ tham gia 1 suất trong phòng ${roomId}. Tiền thưởng sẽ tự động chia về Ví của bạn.`);
}

/* Modal Helpers */
function showVerifiedModal() {
  const modal = document.getElementById('modalVerified');
  if (modal) modal.classList.remove('hidden');
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) modal.classList.add('hidden');
}

function showGameDetail(gameType) {
  alert(`ℹ️ Thông tin chi tiết luật chơi & cơ cấu giải thưởng cho game: ${getGameName(gameType)}`);
}
