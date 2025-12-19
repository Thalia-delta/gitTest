// 导航栏滚动效果
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// 移动端汉堡菜单
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navLinkItems = document.querySelectorAll('.nav-link');

    hamburger.addEventListener('click', function() {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
        
        // 汉堡菜单动画
        hamburger.children[0].style.transform = hamburger.classList.contains('active') ? 'rotate(45deg) translate(5px, 5px)' : 'rotate(0) translate(0, 0)';
        hamburger.children[1].style.opacity = hamburger.classList.contains('active') ? '0' : '1';
        hamburger.children[2].style.transform = hamburger.classList.contains('active') ? 'rotate(-45deg) translate(7px, -6px)' : 'rotate(0) translate(0, 0)';
    });

    // 点击导航链接关闭菜单
    navLinkItems.forEach(link => {
        link.addEventListener('click', function() {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
            
            // 重置汉堡菜单样式
            hamburger.children[0].style.transform = 'rotate(0) translate(0, 0)';
            hamburger.children[1].style.opacity = '1';
            hamburger.children[2].style.transform = 'rotate(0) translate(0, 0)';
        });
    });
});

// 平滑滚动
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetElement.offsetTop - navbarHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// 滚动动画效果
function revealOnScroll() {
    const reveals = document.querySelectorAll('.scroll-reveal');
    
    reveals.forEach(reveal => {
        const windowHeight = window.innerHeight;
        const elementTop = reveal.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < windowHeight - elementVisible) {
            reveal.classList.add('visible');
        } else {
            reveal.classList.remove('visible');
        }
    });
}

// 初始检查
revealOnScroll();

// 滚动时检查
window.addEventListener('scroll', revealOnScroll);

// 添加滚动动画类到所有需要的元素
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section');
    const cards = document.querySelectorAll('.card');
    const serviceItems = document.querySelectorAll('.service-item');
    const contactForm = document.querySelector('.contact-form');
    
    sections.forEach(section => {
        section.classList.add('scroll-reveal');
    });
    
    cards.forEach(card => {
        card.classList.add('scroll-reveal');
    });
    
    serviceItems.forEach(item => {
        item.classList.add('scroll-reveal');
    });
    
    if (contactForm) {
        contactForm.classList.add('scroll-reveal');
    }
});

// 表单提交处理
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 简单的表单提交动画
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = '发送中...';
            submitBtn.disabled = true;
            
            // 模拟提交
            setTimeout(() => {
                submitBtn.textContent = '发送成功！';
                submitBtn.style.backgroundColor = 'var(--secondary-color)';
                
                // 重置表单
                this.reset();
                
                // 恢复按钮
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.backgroundColor = '';
                }, 2000);
            }, 1500);
        });
    }
});

// 鼠标跟随效果（可选）
document.addEventListener('DOMContentLoaded', function() {
    const cursor = document.createElement('div');
    cursor.className = 'cursor';
    document.body.appendChild(cursor);
    
    // 检查是否为移动设备
    if (!navigator.userAgent.match(/(iPhone|iPod|iPad|Android|BlackBerry|BB10|IEMobile)/)) {
        let mouseX = 0;
        let mouseY = 0;
        let cursorX = 0;
        let cursorY = 0;
        let speed = 0.1;
        
        document.addEventListener('mousemove', function(e) {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        function animateCursor() {
            cursorX += (mouseX - cursorX) * speed;
            cursorY += (mouseY - cursorY) * speed;
            
            cursor.style.left = cursorX + 'px';
            cursor.style.top = cursorY + 'px';
            
            requestAnimationFrame(animateCursor);
        }
        
        animateCursor();
    } else {
        // 移动设备隐藏自定义光标
        cursor.style.display = 'none';
    }
});

// 添加光标样式
const cursorStyle = document.createElement('style');
cursorStyle.textContent = `
    .cursor {
        position: fixed;
        width: 20px;
        height: 20px;
        border: 2px solid var(--primary-color);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        mix-blend-mode: difference;
        transition: transform 0.1s ease;
    }
    
    .cursor.hover {
        transform: scale(2);
        background-color: var(--primary-color);
    }
`;
document.head.appendChild(cursorStyle);

// 鼠标悬停效果
document.addEventListener('DOMContentLoaded', function() {
    const interactiveElements = document.querySelectorAll('a, button, .card, .service-item');
    const cursor = document.querySelector('.cursor');
    
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            cursor.classList.add('hover');
        });
        
        element.addEventListener('mouseleave', function() {
            cursor.classList.remove('hover');
        });
    });
});