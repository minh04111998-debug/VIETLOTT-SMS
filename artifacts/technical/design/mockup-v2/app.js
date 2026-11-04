/**
 * Vietlott SMS - Vanilla JS Prototype
 * 
 * Includes navigation, game logic, payment flows, and UI interactions.
 */

document.addEventListener('DOMContentLoaded', () => {
    // === 16. INITIALIZATION ===
    initNavigation();
    initGameInteractions();
    initLotto();
    initBingo18();
    initMega();
    initPayment();
    initHistoryTabs();
    initResults();
    initCountdowns();
    initDarkMode();
    initRipple();
    initPullToRefresh();
});

// === 1. SCREEN NAVIGATION SYSTEM ===
let navStack = ['screen-home'];
let currentScreenId = 'screen-home';

function initNavigation() {
    // Back buttons
    document.querySelectorAll('.back-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            goBack();
        });
    });

    // Bottom Navigation taps
    document.querySelectorAll('.bottom-nav-item').forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const target = item.getAttribute('data-target');
            if (target) {
                // Clear nav stack when navigating via bottom nav
                navStack = [target];
                updateBottomNav(item);
                navigateTo(target, 'fade');
            }
        });
    });

    // Explicit navigation links
    document.querySelectorAll('[data-nav]').forEach(el => {
        el.addEventListener('click', (e) => {
            e.preventDefault();
            const target = el.getAttribute('data-nav');
            navigateTo(target, 'forward');
        });
    });
}

function navigateTo(screenId, direction = 'forward') {
    if (screenId === currentScreenId) return;

    const currentScreen = document.getElementById(currentScreenId);
    const targetScreen = document.getElementById(screenId);

    if (!targetScreen) {
        console.warn(`Screen ${screenId} not found`);
        return;
    }

    if (direction === 'forward') {
        navStack.push(screenId);
    }

    // Reset classes
    currentScreen.classList.remove('active', 'slide-in-right', 'slide-in-left', 'slide-out-right', 'slide-out-left', 'fade-in', 'fade-out');
    targetScreen.classList.remove('active', 'slide-in-right', 'slide-in-left', 'slide-out-right', 'slide-out-left', 'fade-in', 'fade-out');

    if (direction === 'forward') {
        currentScreen.classList.add('slide-out-left');
        targetScreen.classList.add('active', 'slide-in-right');
    } else if (direction === 'back') {
        currentScreen.classList.add('slide-out-right');
        targetScreen.classList.add('active', 'slide-in-left');
    } else if (direction === 'fade') {
        currentScreen.classList.add('fade-out');
        targetScreen.classList.add('active', 'fade-in');
    }

    setTimeout(() => {
        currentScreen.classList.remove('active', 'slide-out-left', 'slide-out-right', 'fade-out');
        targetScreen.classList.remove('slide-in-right', 'slide-in-left', 'fade-in');
    }, 300); // match transition duration

    currentScreenId = screenId;
}

function goBack() {
    if (navStack.length > 1) {
        navStack.pop();
        const previousScreenId = navStack[navStack.length - 1];
        navigateTo(previousScreenId, 'back');
    } else {
        // If empty stack, default to home
        navigateTo('screen-home', 'back');
    }
}

// === 2. BOTTOM NAVIGATION ===
function updateBottomNav(clickedItem) {
    document.querySelectorAll('.bottom-nav-item').forEach(item => {
        item.classList.remove('active');
    });
    clickedItem.classList.add('active');
    
    // Animate indicator if it exists
    const indicator = document.querySelector('.bottom-nav-indicator');
    if (indicator) {
        const itemRect = clickedItem.getBoundingClientRect();
        const parentRect = clickedItem.parentElement.getBoundingClientRect();
        const left = itemRect.left - parentRect.left + (itemRect.width / 2) - 10;
        indicator.style.transform = `translateX(${left}px)`;
    }
}

// === 3. GAME CARD INTERACTIONS ===
function initGameInteractions() {
    const playButtons = document.querySelectorAll('.game-card .btn-play');
    playButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const card = e.target.closest('.game-card');
            if (card.classList.contains('lotto-card')) {
                navigateTo('screen-lotto');
            } else if (card.classList.contains('bingo-card')) {
                navigateTo('screen-bingo');
            } else if (card.classList.contains('mega-card')) {
                navigateTo('screen-mega');
            }
        });
    });
}

// === 4. LOTTO 5/35 NUMBER SELECTION ===
function initLotto() {
    const grid = document.querySelector('.lotto-grid');
    if (!grid) return;

    let selectedNumbers = [];
    const MAX_SELECT = 5;

    // Generate balls
    for (let i = 1; i <= 35; i++) {
        const ball = document.createElement('div');
        ball.className = 'number-ball';
        ball.textContent = i < 10 ? `0${i}` : i;
        ball.dataset.num = i;
        
        ball.addEventListener('click', () => {
            if (ball.classList.contains('selected')) {
                ball.classList.remove('selected');
                selectedNumbers = selectedNumbers.filter(n => n !== i);
            } else {
                if (selectedNumbers.length < MAX_SELECT) {
                    ball.classList.add('selected');
                    selectedNumbers.push(i);
                    // Animate scale
                    ball.style.transform = 'scale(1.2)';
                    setTimeout(() => ball.style.transform = '', 150);
                } else {
                    showToast('Đã chọn đủ 5 số', 'info');
                }
            }
            updateLottoSelection();
        });
        
        grid.appendChild(ball);
    }

    const randomBtn = document.querySelector('.btn-random-lotto');
    if (randomBtn) {
        randomBtn.addEventListener('click', () => {
            // Deselect all
            document.querySelectorAll('.lotto-grid .number-ball').forEach(b => b.classList.remove('selected'));
            selectedNumbers = [];
            
            // Randomly select 5
            const allNums = Array.from({length: 35}, (_, i) => i + 1);
            for (let i = allNums.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [allNums[i], allNums[j]] = [allNums[j], allNums[i]];
            }
            
            const toSelect = allNums.slice(0, 5);
            toSelect.forEach((num, index) => {
                setTimeout(() => {
                    const ball = document.querySelector(`.lotto-grid .number-ball[data-num="${num}"]`);
                    if(ball) {
                        ball.classList.add('selected');
                        ball.style.transform = 'scale(1.2)';
                        setTimeout(() => ball.style.transform = '', 150);
                        selectedNumbers.push(num);
                        updateLottoSelection();
                    }
                }, index * 100);
            });
        });
    }

    const clearBtn = document.querySelector('.btn-clear-lotto');
    if (clearBtn) {
        clearBtn.addEventListener('click', () => {
            document.querySelectorAll('.lotto-grid .number-ball').forEach(b => b.classList.remove('selected'));
            selectedNumbers = [];
            updateLottoSelection();
        });
    }

    const buyBtn = document.querySelector('.btn-buy-lotto');
    if(buyBtn) {
        buyBtn.addEventListener('click', () => {
            if (selectedNumbers.length === MAX_SELECT) {
                navigateTo('screen-payment');
            } else {
                showToast('Vui lòng chọn đủ 5 số', 'error');
            }
        });
    }

    function updateLottoSelection() {
        const displayRow = document.querySelector('.lotto-selection-row');
        if (displayRow) {
            displayRow.innerHTML = '';
            selectedNumbers.sort((a,b) => a-b).forEach(num => {
                const b = document.createElement('div');
                b.className = 'display-ball';
                b.textContent = num < 10 ? `0${num}` : num;
                displayRow.appendChild(b);
            });
            for(let i = selectedNumbers.length; i < 5; i++) {
                const b = document.createElement('div');
                b.className = 'display-ball empty';
                displayRow.appendChild(b);
            }
        }
        
        const priceDisplay = document.querySelector('.lotto-price');
        if (priceDisplay) {
            priceDisplay.textContent = selectedNumbers.length === 5 ? '10.000đ' : '0đ';
        }
    }
}

// === 5. BINGO18 INTERACTIONS ===
function initBingo18() {
    const bettingOptions = document.querySelectorAll('.bingo-bet-btn');
    let totalBet = 0;

    bettingOptions.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.classList.toggle('selected');
            if (btn.classList.contains('selected')) {
                totalBet += 10000;
            } else {
                totalBet -= 10000;
            }
            updateBingoTotal();
        });
    });

    function updateBingoTotal() {
        const totalEl = document.querySelector('.bingo-total-price');
        if (totalEl) {
            totalEl.textContent = totalBet.toLocaleString('vi-VN') + 'đ';
        }
    }

    const confirmBtn = document.querySelector('.btn-bingo-confirm');
    if (confirmBtn) {
        confirmBtn.addEventListener('click', () => {
            if (totalBet > 0) {
                navigateTo('screen-payment');
            } else {
                showToast('Vui lòng chọn ít nhất 1 cửa', 'error');
            }
        });
    }
}

// === 6. MEGA 6/45 NUMBER SELECTION ===
function initMega() {
    const grid = document.querySelector('.mega-grid');
    if (!grid) return;

    let selectedNumbers = [];
    const MAX_SELECT = 6;

    // Generate balls
    for (let i = 1; i <= 45; i++) {
        const ball = document.createElement('div');
        ball.className = 'number-ball';
        ball.textContent = i < 10 ? `0${i}` : i;
        ball.dataset.num = i;
        
        ball.addEventListener('click', () => {
            if (ball.classList.contains('selected')) {
                ball.classList.remove('selected');
                selectedNumbers = selectedNumbers.filter(n => n !== i);
            } else {
                if (selectedNumbers.length < MAX_SELECT) {
                    ball.classList.add('selected');
                    selectedNumbers.push(i);
                    ball.style.transform = 'scale(1.2)';
                    setTimeout(() => ball.style.transform = '', 150);
                } else {
                    showToast('Đã chọn đủ 6 số', 'info');
                }
            }
            updateMegaSelection();
        });
        
        grid.appendChild(ball);
    }
    
    // Add random, clear logic similar to lotto...
    function updateMegaSelection() {
        const displayRow = document.querySelector('.mega-selection-row');
        if (displayRow) {
            displayRow.innerHTML = '';
            selectedNumbers.sort((a,b) => a-b).forEach(num => {
                const b = document.createElement('div');
                b.className = 'display-ball';
                b.textContent = num < 10 ? `0${num}` : num;
                displayRow.appendChild(b);
            });
            for(let i = selectedNumbers.length; i < 6; i++) {
                const b = document.createElement('div');
                b.className = 'display-ball empty';
                displayRow.appendChild(b);
            }
        }
        
        const priceDisplay = document.querySelector('.mega-price');
        if (priceDisplay) {
            priceDisplay.textContent = selectedNumbers.length === 6 ? '10.000đ' : '0đ';
        }
    }
}

// === 7. PAYMENT FLOW ===
function initPayment() {
    const paymentOptions = document.querySelectorAll('.payment-option');
    paymentOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            paymentOptions.forEach(o => o.classList.remove('selected'));
            opt.classList.add('selected');
            const radio = opt.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

    const submitBtn = document.querySelector('.btn-submit-payment');
    if (submitBtn) {
        submitBtn.addEventListener('click', () => {
            if (submitBtn.disabled) return;
            
            // Loading state
            submitBtn.disabled = true;
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang xử lý...';
            
            setTimeout(() => {
                // Success state
                submitBtn.innerHTML = '<i class="fa-solid fa-check"></i> Thành công!';
                submitBtn.style.backgroundColor = '#28a745';
                
                setTimeout(() => {
                    // Reset and navigate
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                    submitBtn.style.backgroundColor = '';
                    navigateTo('screen-payment-success');
                    
                    // Trigger success animation on next screen
                    const circle = document.querySelector('.success-circle');
                    if (circle) {
                        circle.style.transform = 'scale(0)';
                        setTimeout(() => circle.style.transform = 'scale(1)', 50);
                    }
                }, 1000);
            }, 1500);
        });
    }
}

// === 8. PAYMENT SUCCESS SCREEN ===
// Buttons logic
document.querySelector('.btn-view-history')?.addEventListener('click', () => {
    navigateTo('screen-history');
});
document.querySelector('.btn-buy-more')?.addEventListener('click', () => {
    navigateTo('screen-home');
});

// === 9. HISTORY TABS ===
function initHistoryTabs() {
    const tabs = document.querySelectorAll('.history-tab');
    const contents = document.querySelectorAll('.history-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active classes
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            // Add active class to clicked tab and corresponding content
            tab.classList.add('active');
            const targetId = tab.dataset.target;
            document.getElementById(targetId)?.classList.add('active');
        });
    });
}

// === 10. RESULTS INTERACTIONS ===
function initResults() {
    const resultCards = document.querySelectorAll('.result-card');
    resultCards.forEach(card => {
        card.addEventListener('click', () => {
            navigateTo('screen-result-detail');
        });
    });
}

// === 11. LIVE COUNTDOWN TIMERS ===
function initCountdowns() {
    const timers = document.querySelectorAll('.countdown-timer');
    
    timers.forEach(timerEl => {
        let timeText = timerEl.dataset.time || "06:00"; // default or custom
        let timeParts = timeText.split(':');
        let seconds = 0;
        
        if (timeParts.length === 3) { // HH:MM:SS
            seconds = parseInt(timeParts[0])*3600 + parseInt(timeParts[1])*60 + parseInt(timeParts[2]);
        } else if (timeParts.length === 2) { // MM:SS
            seconds = parseInt(timeParts[0])*60 + parseInt(timeParts[1]);
        }
        
        const interval = setInterval(() => {
            if (seconds > 0) {
                seconds--;
                
                let h = Math.floor(seconds / 3600);
                let m = Math.floor((seconds % 3600) / 60);
                let s = seconds % 60;
                
                let display = '';
                if (timeParts.length === 3) {
                    display = `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
                } else {
                    display = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
                }
                
                timerEl.textContent = display;
            } else {
                // Flash red
                timerEl.classList.add('time-up');
                setTimeout(() => timerEl.classList.remove('time-up'), 1000);
                
                // Reset (simulate repeating cycle for BINGO)
                if(timerEl.classList.contains('bingo-timer')) {
                    seconds = 6 * 60;
                } else {
                    clearInterval(interval);
                }
            }
        }, 1000);
    });
}

// === 12. DARK MODE TOGGLE ===
function initDarkMode() {
    const toggle = document.getElementById('dark-mode-toggle');
    if (!toggle) return;

    // Load pref
    const isDark = localStorage.getItem('vietlott_dark') === 'true';
    if (isDark) {
        document.body.classList.add('dark-mode');
        toggle.checked = true;
    }

    toggle.addEventListener('change', () => {
        if (toggle.checked) {
            document.body.classList.add('dark-mode');
            localStorage.setItem('vietlott_dark', 'true');
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('vietlott_dark', 'false');
        }
    });
}

// === 13. TOAST NOTIFICATION SYSTEM ===
function showToast(message, type = 'info', duration = 3000) {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.style.position = 'fixed';
        container.style.bottom = '80px';
        container.style.left = '50%';
        container.style.transform = 'translateX(-50%)';
        container.style.zIndex = '9999';
        container.style.display = 'flex';
        container.style.flexDirection = 'column';
        container.style.gap = '10px';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    // Base styles
    toast.style.padding = '12px 20px';
    toast.style.borderRadius = '24px';
    toast.style.color = 'white';
    toast.style.fontSize = '14px';
    toast.style.fontWeight = '500';
    toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
    toast.style.animation = 'slideUpToast 0.3s forwards';
    toast.style.opacity = '0';
    
    // Colors
    if (type === 'success') toast.style.backgroundColor = '#28a745';
    else if (type === 'error') toast.style.backgroundColor = '#dc3545';
    else toast.style.backgroundColor = '#007bff';

    container.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'fadeOutToast 0.3s forwards';
        setTimeout(() => toast.remove(), 300);
    }, duration);
}

// Add CSS keyframes for toast dynamically if not present
if (!document.getElementById('toast-styles')) {
    const style = document.createElement('style');
    style.id = 'toast-styles';
    style.textContent = `
        @keyframes slideUpToast {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes fadeOutToast {
            from { opacity: 1; }
            to { opacity: 0; }
        }
    `;
    document.head.appendChild(style);
}

// === 14. BUTTON RIPPLE EFFECT ===
function initRipple() {
    document.addEventListener('click', function (e) {
        const target = e.target.closest('.btn-primary, .btn-play, .bottom-nav-item');
        if (!target) return;

        const rect = target.getBoundingClientRect();
        const ripple = document.createElement('span');
        
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.width = ripple.style.height = `${size}px`;
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        ripple.className = 'ripple';
        
        // Ensure parent has position relative/overflow hidden
        const computedStyle = window.getComputedStyle(target);
        if (computedStyle.position === 'static') {
            target.style.position = 'relative';
        }
        target.style.overflow = 'hidden';

        target.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    });
}

// Ripple CSS
if (!document.getElementById('ripple-styles')) {
    const style = document.createElement('style');
    style.id = 'ripple-styles';
    style.textContent = `
        .ripple {
            position: absolute;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple-anim 0.6s linear;
            pointer-events: none;
        }
        @keyframes ripple-anim {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(style);
}

// === 15. PULL-TO-REFRESH (Optional) ===
function initPullToRefresh() {
    let startY = 0;
    const pTrThreshold = 60;
    const body = document.body;
    let ptrIndicator = null;

    document.addEventListener('touchstart', (e) => {
        if (window.scrollY === 0) {
            startY = e.touches[0].clientY;
        }
    }, {passive: true});

    document.addEventListener('touchmove', (e) => {
        if (startY > 0) {
            const currentY = e.touches[0].clientY;
            const diff = currentY - startY;

            if (diff > 0 && window.scrollY === 0) {
                // Pulling down
                if (!ptrIndicator) {
                    ptrIndicator = document.createElement('div');
                    ptrIndicator.className = 'ptr-indicator';
                    ptrIndicator.innerHTML = '<i class="fa-solid fa-arrow-down"></i> Kéo để làm mới';
                    ptrIndicator.style.position = 'fixed';
                    ptrIndicator.style.top = '0';
                    ptrIndicator.style.left = '0';
                    ptrIndicator.style.right = '0';
                    ptrIndicator.style.height = '60px';
                    ptrIndicator.style.display = 'flex';
                    ptrIndicator.style.alignItems = 'center';
                    ptrIndicator.style.justifyContent = 'center';
                    ptrIndicator.style.background = '#f5f5f5';
                    ptrIndicator.style.zIndex = '99';
                    ptrIndicator.style.color = '#888';
                    ptrIndicator.style.transition = 'transform 0.2s';
                    ptrIndicator.style.transform = 'translateY(-100%)';
                    body.appendChild(ptrIndicator);
                }
                
                const translateY = Math.min(diff - 60, 0);
                ptrIndicator.style.transform = `translateY(${translateY}px)`;
                
                if (diff > pTrThreshold) {
                    ptrIndicator.innerHTML = '<i class="fa-solid fa-rotate"></i> Thả để làm mới';
                }
            }
        }
    }, {passive: true});

    document.addEventListener('touchend', (e) => {
        if (startY > 0 && ptrIndicator) {
            const currentY = e.changedTouches[0].clientY;
            const diff = currentY - startY;
            
            if (diff > pTrThreshold && window.scrollY === 0) {
                // Trigger refresh
                ptrIndicator.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Đang làm mới...';
                ptrIndicator.style.transform = 'translateY(0)';
                
                setTimeout(() => {
                    ptrIndicator.style.transform = 'translateY(-100%)';
                    setTimeout(() => {
                        if(ptrIndicator) {
                            ptrIndicator.remove();
                            ptrIndicator = null;
                        }
                    }, 300);
                }, 1000);
            } else {
                ptrIndicator.style.transform = 'translateY(-100%)';
                setTimeout(() => {
                    if(ptrIndicator) {
                        ptrIndicator.remove();
                        ptrIndicator = null;
                    }
                }, 300);
            }
        }
        startY = 0;
    });
}
