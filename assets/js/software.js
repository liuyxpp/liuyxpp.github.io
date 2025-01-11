// Emoji mapping for categories
const categoryEmojis = {
  'Scientific Computing': '🧮',
  'Utility': '🛠️',
  'Legacy': '🕰️'
};

function toggleTocDropdown(event) {
  event.preventDefault();
  event.stopPropagation();
  
  const button = event.currentTarget;
  const dropdown = button.parentElement.querySelector('.toc-dropdown');
  const caret = button.querySelector('.toc-caret');
  
  // Toggle current dropdown
  const isShowing = dropdown.classList.toggle('show');
  caret.style.transform = isShowing ? 'rotate(180deg)' : 'rotate(0)';
  
  // Add emojis to dropdown items
  if (isShowing) {
    // Extract category name by removing caret symbol and trimming
    const category = button.textContent.replace('▼', '').trim();
    const emoji = categoryEmojis[category] || '📄';
    
    dropdown.querySelectorAll('.toc-item').forEach(item => {
      if (!item.textContent.startsWith(emoji)) {
        // Create span for emoji to maintain layout
        const emojiSpan = document.createElement('span');
        emojiSpan.className = 'toc-emoji';
        emojiSpan.textContent = emoji;
        emojiSpan.style.marginRight = '8px';
        
        // Insert emoji before existing content
        item.insertBefore(emojiSpan, item.firstChild);
      }
    });
  }
  
  // Close other dropdowns
  document.querySelectorAll('.toc-dropdown').forEach(d => {
    if (d !== dropdown && d.classList.contains('show')) {
      d.classList.remove('show');
      d.previousElementSibling.querySelector('.toc-caret').style.transform = 'rotate(0)';
    }
  });
}

// Close dropdowns when clicking outside
document.addEventListener('click', function(event) {
  if (!event.target.closest('.toc-category')) {
    document.querySelectorAll('.toc-dropdown.show').forEach(d => {
      d.classList.remove('show');
      d.previousElementSibling.querySelector('.toc-caret').style.transform = 'rotate(0)';
    });
  }
});

// Close dropdowns on window resize
window.addEventListener('resize', function() {
  document.querySelectorAll('.toc-dropdown.show').forEach(d => {
    d.classList.remove('show');
    d.previousElementSibling.querySelector('.toc-caret').style.transform = 'rotate(0)';
  });
});
