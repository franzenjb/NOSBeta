#!/usr/bin/env python3
"""
Update menu system with extracted Experience Builder data
"""

import json
from collections import defaultdict

def remove_duplicates(menu_items):
    """Remove duplicate menu items based on name and URL"""
    seen = set()
    unique_items = []
    
    for item in menu_items:
        key = (item['name'], item['url'])
        if key not in seen:
            seen.add(key)
            unique_items.append(item)
    
    return unique_items

def fix_navigation_urls(menu_items):
    """Fix URLs for proper embed widget navigation"""
    for item in menu_items:
        # Extract page ID from URL
        if 'page=' in item['url']:
            page_id = item['url'].split('page=')[1]
            
            # Create proper navigation URL for embed widget
            # Option 1: Direct page navigation (recommended)
            item['url'] = f"https://experience.arcgis.com/experience/ce0b7dc7574c49a8a82f36443fee494f?page={page_id}"
            
            # Option 2: Add target="_parent" for breaking out of iframe
            item['target'] = "_parent"
            
            # Option 3: JavaScript navigation (for embed context)
            item['js_navigation'] = f"parent.postMessage({{action: 'navigate', page: '{page_id}'}}, '*');"
    
    return menu_items

def update_menu_json(extracted_menu_file, output_file):
    """Update menu.json with extracted data"""
    
    # Load extracted menu
    with open(extracted_menu_file, 'r') as f:
        menu_items = json.load(f)
    
    # Remove duplicates
    unique_items = remove_duplicates(menu_items)
    print(f"Removed {len(menu_items) - len(unique_items)} duplicates")
    
    # Fix navigation URLs
    fixed_items = fix_navigation_urls(unique_items)
    
    # Group by category for better organization
    categories = defaultdict(list)
    for item in fixed_items:
        categories[item['category']].append(item)
    
    # Sort items within each category
    for category in categories:
        categories[category].sort(key=lambda x: x['name'])
    
    # Create final menu structure
    final_menu = []
    
    # Define category order
    category_order = [
        'Active Disasters',
        'Command & Control', 
        'Weather & Hazards',
        'Client Services',
        'Operations',
        'Risk & Planning',
        'General'
    ]
    
    # Add items in category order
    for category in category_order:
        if category in categories:
            final_menu.extend(categories[category])
    
    # Add any remaining categories
    for category, items in categories.items():
        if category not in category_order:
            final_menu.extend(items)
    
    # Save updated menu
    with open(output_file, 'w') as f:
        json.dump(final_menu, f, indent=2)
    
    print(f"✅ Updated menu saved to {output_file}")
    print(f"📊 Total items: {len(final_menu)}")
    
    # Print category summary
    print("\n📋 Category Summary:")
    for category in category_order:
        if category in categories:
            print(f"  {category}: {len(categories[category])} items")

def update_backend_menu(menu_file, api_url):
    """Update the backend menu via API"""
    try:
        with open(menu_file, 'r') as f:
            menu_data = json.load(f)
        
        # Send to backend
        response = requests.post(f"{api_url}/update-menu", json=menu_data)
        
        if response.status_code == 200:
            print("✅ Backend menu updated successfully")
        else:
            print(f"❌ Backend update failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Backend update error: {e}")

def create_embed_friendly_navigation():
    """Create JavaScript for embed-friendly navigation"""
    
    js_code = """
// Embed-friendly navigation for Experience Builder
function navigateToPage(pageId) {
    // Method 1: Try parent window navigation
    if (window.parent && window.parent !== window) {
        try {
            window.parent.postMessage({
                action: 'navigate',
                page: pageId,
                experience: 'ce0b7dc7574c49a8a82f36443fee494f'
            }, '*');
            return;
        } catch (e) {
            console.log('Parent navigation failed:', e);
        }
    }
    
    // Method 2: Direct navigation
    const url = `https://experience.arcgis.com/experience/ce0b7dc7574c49a8a82f36443fee494f?page=${pageId}`;
    window.open(url, '_parent');
}

// Update menu button click handlers
document.addEventListener('DOMContentLoaded', function() {
    const menuButtons = document.querySelectorAll('.menu-button');
    
    menuButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const url = this.href;
            if (url.includes('page=')) {
                const pageId = url.split('page=')[1];
                navigateToPage(pageId);
            } else {
                window.open(url, '_blank');
            }
        });
    });
});
"""
    
    with open('embed_navigation.js', 'w') as f:
        f.write(js_code)
    
    print("✅ Created embed_navigation.js")

def main():
    """Main function"""
    print("🚀 Updating menu system with Experience Builder data...")
    
    # Update menu.json
    update_menu_json('menu_extracted.json', 'menu_updated.json')
    
    # Create embed-friendly navigation
    create_embed_friendly_navigation()
    
    # Backend update will be done separately
    print("⚠️  Backend update skipped (will update manually)")
    
    print("\n🎉 Menu system update complete!")
    print("\n📝 Next steps:")
    print("1. Replace menu.json with menu_updated.json")
    print("2. Include embed_navigation.js in your HTML")
    print("3. Test navigation in Experience Builder embed")
    print("4. Deploy to GitHub Pages")

if __name__ == "__main__":
    main() 