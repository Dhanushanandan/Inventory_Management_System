document.addEventListener('DOMContentLoaded', () => {
    const heroContent = document.querySelector('.hero-content');
    const ctaButton = document.querySelector('#getstartbtn');

    // Scroll animation for hero content
    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;
        heroContent.style.transform = `translateY(${scrollPosition * 0.3}px)`;
        ctaButton.style.transform = `translateY(${scrollPosition * 0.5}px)`;
    });

    // Click event for the "Get Started" button
    ctaButton.addEventListener('click', () => {
        alert('Welcome to Tadco Mart! Let’s get started with Tadco Mart.');
        window.location.href = '/login';
    });
});