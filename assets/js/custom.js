// Custom JavaScript for ClawMark
// Add your custom functionality here

// Example: Analytics tracking
function trackLinkClick(linkTitle) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'click', {
            event_category: 'Link',
            event_label: linkTitle
        });
    }
    console.log('Link clicked:', linkTitle);
}

// Example: Add click tracking to all links
document.addEventListener('DOMContentLoaded', function() {
    const linkButtons = document.querySelectorAll('.link-button');
    linkButtons.forEach(button => {
        button.addEventListener('click', function() {
            const title = this.querySelector('.link-title')?.textContent || 'Unknown';
            trackLinkClick(title);
        });
    });
});

// Add your custom JavaScript below