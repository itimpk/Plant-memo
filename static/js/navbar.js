document.addEventListener('DOMContentLoaded', () => {
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');

    // Safety check to ensure elements exist on the current page
    if (mobileBtn && mobileMenu && menuIcon) {
        mobileBtn.addEventListener('click', () => {
            // Toggle visibility
            const isHidden = mobileMenu.classList.toggle('hidden');
            
            // Toggle icon classes
            if (isHidden) {
                menuIcon.classList.replace('fa-xmark', 'fa-bars');
            } else {
                menuIcon.classList.replace('fa-bars', 'fa-xmark');
            }
        });
    }
});