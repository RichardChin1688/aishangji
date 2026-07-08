// 启橙 AI 生态平台 - 交互逻辑

// 资料下载列表
const downloadResources = [
  { name: '📘 AI 套餐手册.pdf', size: '2.5 MB', desc: '全套技术服务套餐详情' },
  { name: '📗 合伙人分润规则.pdf', size: '1.8 MB', desc: '三级分润模型详解' },
  { name: '📙 私董会介绍.pdf', size: '3.2 MB', desc: 'AI 私董会权益与加入流程' },
  { name: '📕 城市代理政策.pdf', size: '2.1 MB', desc: 'OPC 孵化扶持政策' },
  { name: '📓 招商 PPT 全套.zip', size: '15.6 MB', desc: '完整招商资料包' }
];

function renderDownloadList() {
  const list = document.getElementById('downloadList');
  if (!list) return;
  
  list.innerHTML = downloadResources.map(item => `
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 16px; border-bottom: 1px solid #E5E7E9; gap: 16px;">
      <div style="flex: 1;">
        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: 4px;">${item.name}</div>
        <div style="font-size: 0.85rem; color: var(--text-secondary);">${item.desc} · ${item.size}</div>
      </div>
      <button class="btn btn-primary" onclick="downloadFile('${item.name}')" style="padding: 10px 20px; font-size: 0.85rem;">下载</button>
    </div>
  `).join('');
}

function downloadFile(filename) {
  alert(`正在下载：${filename}\n\n（实际部署时将从服务器下载文件）`);
  console.log('下载文件:', filename);
}

// 数字动画
function animateNumber(element, target, duration = 2000) {
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;
  let hasFormatted = false;
  
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
      hasFormatted = true;
    }
    
    // 格式化数字
    let displayValue;
    if (target >= 10000) {
      displayValue = (current / 10000).toFixed(1) + '万+';
    } else if (target >= 1000) {
      const thousands = Math.floor(current / 1000);
      const remainder = Math.floor(current % 1000);
      displayValue = thousands + ',' + remainder.toString().padStart(3, '0');
    } else {
      displayValue = Math.floor(current);
    }
    
    element.textContent = displayValue;
  }, 16);
}

// 初始化数字动画
function initNumberAnimation() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
        const numberEl = entry.target.querySelector('.stat-number');
        if (numberEl) {
          const target = parseInt(numberEl.getAttribute('data-target'));
          if (target) {
            animateNumber(numberEl, target);
            entry.target.classList.add('animated');
          }
        }
      }
    });
  }, { threshold: 0.5 });
  
  document.querySelectorAll('.stat-item').forEach(el => {
    observer.observe(el);
  });
}

// 滚动动画
function initScrollAnimation() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    observer.observe(el);
  });
}

// 导航栏滚动效果
function initNavbarScroll() {
  window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    const currentScroll = window.pageYOffset;
    
    if (currentScroll > 50) {
      // 滚动时加深背景，增强毛玻璃效果
      navbar.style.background = 'rgba(13, 27, 42, 0.98)';
      navbar.style.boxShadow = '0 4px 32px rgba(0, 0, 0, 0.5)';
      navbar.style.borderColor = 'rgba(0, 212, 255, 0.2)';
    } else {
      // 顶部时恢复默认
      navbar.style.background = 'rgba(13, 27, 42, 0.95)';
      navbar.style.boxShadow = '0 4px 24px rgba(0, 0, 0, 0.3)';
      navbar.style.borderColor = 'rgba(255, 255, 255, 0.1)';
    }
  });
}

// 平滑滚动
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });
}

// 当前页面导航高亮
function initActiveNav() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

// 移动端菜单
function initMobileMenu() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function(e) {
      e.stopPropagation();
      navLinks.classList.toggle('active');
      menuToggle.classList.toggle('active');
    });
    
    // 点击菜单外部关闭
    document.addEventListener('click', function(e) {
      if (!navLinks.contains(e.target) && !menuToggle.contains(e.target)) {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
      }
    });
    
    // 点击菜单项后关闭
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
      });
    });
  }
}

// 模态框
function initModals() {
  const downloadBtn = document.getElementById('downloadBtn');
  const appointmentBtn = document.getElementById('appointmentBtn');
  const appointmentBtn2 = document.getElementById('appointmentBtn2');
  const downloadModal = document.getElementById('downloadModal');
  const appointmentModal = document.getElementById('appointmentModal');
  const closeButtons = document.querySelectorAll('.modal-close');
  
  if (downloadBtn && downloadModal) {
    downloadBtn.addEventListener('click', () => {
      downloadModal.classList.add('active');
    });
  }
  
  [appointmentBtn, appointmentBtn2].forEach(btn => {
    if (btn && appointmentModal) {
      btn.addEventListener('click', () => {
        appointmentModal.classList.add('active');
      });
    }
  });
  
  closeButtons.forEach(btn => {
    btn.addEventListener('click', function() {
      this.closest('.modal').classList.remove('active');
    });
  });
  
  window.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal')) {
      e.target.classList.remove('active');
    }
  });
}

// 预约表单
function initAppointmentForm() {
  const appointmentForm = document.getElementById('appointmentForm');
  const appointmentModal = document.getElementById('appointmentModal');
  
  if (!appointmentForm) return;
  
  appointmentForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
      companyName: document.getElementById('companyName').value,
      industry: document.getElementById('industry').value,
      contact: document.getElementById('contact').value,
      phone: document.getElementById('phone').value,
      interests: Array.from(document.querySelectorAll('input[name="interest"]:checked'))
        .map(cb => cb.value)
    };
    
    const leads = JSON.parse(localStorage.getItem('appointmentLeads') || '[]');
    leads.push({
      ...formData,
      submitTime: new Date().toISOString()
    });
    localStorage.setItem('appointmentLeads', JSON.stringify(leads));
    
    alert('✅ 提交成功！\n\n我们的销售顾问将在 24 小时内与您联系。');
    appointmentModal.classList.remove('active');
    appointmentForm.reset();
    
    console.log('新线索:', formData);
  });
}

// 联系表单
function initContactForm() {
  const contactForm = document.getElementById('contactForm');
  
  if (!contactForm) return;
  
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = {
      companyName: document.getElementById('contactCompanyName').value,
      industry: document.getElementById('contactIndustry').value,
      contact: document.getElementById('contactName').value,
      phone: document.getElementById('contactPhone').value,
      interests: Array.from(document.querySelectorAll('input[name="contactInterest"]:checked'))
        .map(cb => cb.value),
      message: document.getElementById('contactMessage').value
    };
    
    const leads = JSON.parse(localStorage.getItem('appointmentLeads') || '[]');
    leads.push({
      ...formData,
      submitTime: new Date().toISOString(),
      source: 'contact-page'
    });
    localStorage.setItem('appointmentLeads', JSON.stringify(leads));
    
    alert('✅ 提交成功！\n\n我们的顾问将在 24 小时内与您联系。');
    contactForm.reset();
    
    console.log('新线索:', formData);
  });
}

// 初始化
document.addEventListener('DOMContentLoaded', function() {
  renderDownloadList();
  initScrollAnimation();
  initNumberAnimation();
  initNavbarScroll();
  initSmoothScroll();
  initActiveNav();
  initMobileMenu();
  initModals();
  initAppointmentForm();
  initContactForm();
  
  console.log('🚀 启橙 AI 官网 - 特斯拉视觉风格已加载');
});
