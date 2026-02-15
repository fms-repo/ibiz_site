// Card Organization System
let cardsConfig = null;
let defaultConfig = null;

// Load configuration from JSON file or localStorage
async function loadCardsConfig() {
  try {
    // Load default config from JSON file first (if not already saved)
    const defaultSaved = localStorage.getItem('defaultCardsConfig');
    if (!defaultSaved) {
      const response = await fetch('cards-config.json');
      if (response.ok) {
        const jsonConfig = await response.json();
        defaultConfig = JSON.parse(JSON.stringify(jsonConfig)); // Deep copy for reset
        localStorage.setItem('defaultCardsConfig', JSON.stringify(defaultConfig));
      } else {
        // Fallback to hardcoded default
        defaultConfig = getDefaultConfig();
        localStorage.setItem('defaultCardsConfig', JSON.stringify(defaultConfig));
      }
    } else {
      defaultConfig = JSON.parse(defaultSaved);
    }
    
    // Try to load user's saved config from localStorage
    const savedConfig = localStorage.getItem('cardsConfig');
    if (savedConfig) {
      cardsConfig = JSON.parse(savedConfig);
      return cardsConfig;
    }
    
    // If no saved config, use default
    cardsConfig = JSON.parse(JSON.stringify(defaultConfig));
    localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
    return cardsConfig;
  } catch (error) {
    console.error('Error loading cards config:', error);
    // Fallback to default hardcoded config
    cardsConfig = getDefaultConfig();
    defaultConfig = JSON.parse(JSON.stringify(cardsConfig));
    localStorage.setItem('defaultCardsConfig', JSON.stringify(defaultConfig));
    localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
    return cardsConfig;
  }
}

// Get default configuration (fallback)
function getDefaultConfig() {
  return {
    "cards": [
      { "id": "erp", "name": "ERP", "href": "erp.html", "icon": "bi-building", "title": "ERP", "description": "Enterprise Resource Planning", "sortOrder": 1, "visible": true },
      { "id": "qhse", "name": "QHSE", "href": "qhse.html", "icon": "bi-shield-check", "title": "QHSE", "description": "Quality, Health, Safety & Environment", "sortOrder": 2, "visible": true },
      { "id": "hrms", "name": "HRMS", "href": "hrms.html", "icon": "bi-people", "title": "HRMS", "description": "Human Resource Management System", "sortOrder": 3, "visible": true },
      { "id": "business-intelligence", "name": "Business Intelligence", "href": "business-intelligence.html", "icon": "bi-graph-up-arrow", "title": "Business Intelligence", "description": "AI-Enabled Analytics Platform", "sortOrder": 4, "visible": true },
      { "id": "cloud-infrastructure", "name": "Cloud Infrastructure", "href": "cloud-infrastructure.html", "icon": "bi-cloud", "title": "Cloud Infrastructure", "description": "AWS Architecture & Data Flow", "sortOrder": 5, "visible": true },
      { "id": "ivms", "name": "IVMS", "href": "ivms.html", "icon": "bi-geo-alt-fill", "title": "IVMS", "description": "Integrated Vehicle Management System", "sortOrder": 6, "visible": true },
      { "id": "agentic-agent", "name": "Agentic Agent (AI)", "href": "agentic-agent.html", "icon": "bi-robot", "title": "Agentic Agent (AI)", "description": "Intelligent AI Agent Platform", "sortOrder": 7, "visible": true }
    ]
  };
}

// Render cards on the page
function renderCards() {
  const grid = document.getElementById('applicationsGrid');
  if (!grid || !cardsConfig) return;
  
  // Sort cards by sortOrder
  const sortedCards = [...cardsConfig.cards].sort((a, b) => a.sortOrder - b.sortOrder);
  
  // Clear existing cards
  grid.innerHTML = '';
  
  // Render visible cards
  sortedCards.forEach((card, index) => {
    if (card.visible) {
      const delay = 300 + (index * 100);
      const cardElement = document.createElement('a');
      cardElement.href = card.href;
      cardElement.className = 'app-card';
      cardElement.setAttribute('data-aos', 'zoom-in');
      cardElement.setAttribute('data-aos-delay', delay);
      cardElement.setAttribute('data-card-id', card.id);
      
      cardElement.innerHTML = `
        <div class="app-icon">
          <i class="bi ${card.icon}"></i>
        </div>
        <h3>${card.title}</h3>
        <p>${card.description}</p>
        <div class="app-card-hover-text">Click to explore</div>
      `;
      
      grid.appendChild(cardElement);
    }
  });
  
  // Re-trigger animations
  setTimeout(() => {
    const elements = Array.from(document.querySelectorAll('[data-aos]'));
    elements.sort((a, b) => {
      const rectA = a.getBoundingClientRect();
      const rectB = b.getBoundingClientRect();
      return rectA.top - rectB.top;
    });
    elements.forEach((el, idx) => {
      setTimeout(() => {
        el.classList.add('aos-animate');
      }, idx * 150);
    });
  }, 100);
}

// Render organize modal
function renderOrganizeModal() {
  const list = document.getElementById('organizeCardsList');
  if (!list || !cardsConfig) return;
  
  // Sort cards by sortOrder
  const sortedCards = [...cardsConfig.cards].sort((a, b) => a.sortOrder - b.sortOrder);
  
  list.innerHTML = '';
  
  sortedCards.forEach((card, index) => {
    const cardItem = document.createElement('div');
    cardItem.className = 'organize-card-item';
    cardItem.setAttribute('data-card-id', card.id);
    
    cardItem.innerHTML = `
      <div class="organize-card-info">
        <div class="organize-card-icon">
          <i class="bi ${card.icon}"></i>
        </div>
        <div class="organize-card-details">
          <h4>${card.name}</h4>
          <small>${card.description}</small>
        </div>
      </div>
      <div class="organize-card-controls">
        <div class="organize-control-group">
          <label>Sort Order:</label>
          <input type="number" class="organize-sort-input" value="${card.sortOrder}" min="1" 
                 onchange="updateCardSortOrder('${card.id}', this.value)">
        </div>
        <div class="organize-control-group">
          <label>Visible:</label>
          <label class="organize-toggle-switch">
            <input type="checkbox" ${card.visible ? 'checked' : ''} 
                   onchange="updateCardVisibility('${card.id}', this.checked)">
            <span class="organize-toggle-slider"></span>
          </label>
        </div>
      </div>
    `;
    
    list.appendChild(cardItem);
  });
}

// Update card sort order
function updateCardSortOrder(cardId, newOrder) {
  const card = cardsConfig.cards.find(c => c.id === cardId);
  if (card) {
    card.sortOrder = parseInt(newOrder) || 1;
    // Re-render organize modal to reflect changes
    renderOrganizeModal();
  }
}

// Update card visibility
function updateCardVisibility(cardId, visible) {
  const card = cardsConfig.cards.find(c => c.id === cardId);
  if (card) {
    card.visible = visible;
  }
}

// Open organize modal
function openOrganizeModal() {
  const modal = document.getElementById('organizeModal');
  if (modal) {
    renderOrganizeModal();
    modal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }
}

// Close organize modal
function closeOrganizeModal(event) {
  const modal = document.getElementById('organizeModal');
  if (!modal) return;
  
  if (!event || event.target.id === 'organizeModal' || event.target.closest('.organize-modal-close')) {
    modal.style.display = 'none';
    document.body.style.overflow = 'auto';
  }
}

// Save cards configuration
function saveCardsConfig() {
  // Validate sort orders (ensure no duplicates, fill gaps)
  const sortedCards = [...cardsConfig.cards].sort((a, b) => a.sortOrder - b.sortOrder);
  sortedCards.forEach((card, index) => {
    card.sortOrder = index + 1;
  });
  
  // Save to localStorage
  localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
  
  // Re-render cards
  renderCards();
  
  // Close modal
  closeOrganizeModal();
  
  // Show success message
  showNotification('Cards configuration saved successfully!', 'success');
}

// Reset cards configuration
function resetCardsConfig() {
  if (confirm('Are you sure you want to reset all cards to their default configuration? This cannot be undone.')) {
    // Load default config from localStorage or JSON
    const savedDefault = localStorage.getItem('defaultCardsConfig');
    if (savedDefault) {
      cardsConfig = JSON.parse(savedDefault);
    } else {
      // Load from JSON file
      fetch('cards-config.json')
        .then(response => response.json())
        .then(data => {
          cardsConfig = data;
          defaultConfig = JSON.parse(JSON.stringify(data));
          localStorage.setItem('defaultCardsConfig', JSON.stringify(defaultConfig));
          localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
          renderCards();
          renderOrganizeModal();
          showNotification('Cards configuration reset to default!', 'success');
        })
        .catch(() => {
          cardsConfig = getDefaultConfig();
          defaultConfig = JSON.parse(JSON.stringify(cardsConfig));
          localStorage.setItem('defaultCardsConfig', JSON.stringify(defaultConfig));
          localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
          renderCards();
          renderOrganizeModal();
          showNotification('Cards configuration reset to default!', 'success');
        });
      return;
    }
    
    localStorage.setItem('cardsConfig', JSON.stringify(cardsConfig));
    renderCards();
    renderOrganizeModal();
    showNotification('Cards configuration reset to default!', 'success');
  }
}

// Show notification
function showNotification(message, type = 'info') {
  // Create notification element
  const notification = document.createElement('div');
  notification.className = `organize-notification organize-notification-${type}`;
  notification.textContent = message;
  document.body.appendChild(notification);
  
  // Show notification
  setTimeout(() => {
    notification.classList.add('show');
  }, 10);
  
  // Hide and remove notification
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => {
      document.body.removeChild(notification);
    }, 300);
  }, 3000);
}

// Close modal on Escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    const modal = document.getElementById('organizeModal');
    if (modal && modal.style.display === 'flex') {
      closeOrganizeModal();
    }
  }
});

// Initialize on page load
document.addEventListener('DOMContentLoaded', async function() {
  await loadCardsConfig();
  renderCards();
});

