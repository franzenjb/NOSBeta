#!/usr/bin/env python3
"""
Extract menu structure from ArcGIS Experience Builder data
"""

import json
import re

def extract_menu_from_experience_builder(json_file):
    """Extract menu items from Experience Builder JSON data"""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract widgets (buttons)
    widgets = data.get('widgets', {})
    
    # Extract page structure
    page_structure = data.get('pageStructure', [])
    
    menu_items = []
    
    # Process each widget to find buttons
    for widget_id, widget_data in widgets.items():
        if widget_data.get('uri') == 'widgets/common/button/':
            config = widget_data.get('config', {})
            function_config = config.get('functionConfig', {})
            
            # Get button text
            button_text = function_config.get('text', '')
            
            # Get link information
            link_param = function_config.get('linkParam', {})
            link_type = link_param.get('linkType', '')
            
            if link_type == 'PAGE':
                page_id = link_param.get('value', '')
                
                # Create menu item
                menu_item = {
                    'name': button_text,
                    'url': f'https://experience.arcgis.com/experience/ce0b7dc7574c49a8a82f36443fee494f?page={page_id}',
                    'category': classify_button(button_text),
                    'keywords': generate_keywords(button_text),
                    'widget_id': widget_id,
                    'page_id': page_id
                }
                
                menu_items.append(menu_item)
    
    # Sort and categorize
    categorized_menu = categorize_menu_items(menu_items)
    
    return categorized_menu

def classify_button(button_text):
    """Classify button into categories based on text"""
    text_lower = button_text.lower()
    
    if any(word in text_lower for word in ['dr ', 'disaster', 'dro', 'kentucky', 'tennessee', 'missouri', 'oklahoma', 'texas', 'indiana', 'illinois', 'oregon']):
        return 'Active Disasters'
    elif any(word in text_lower for word in ['weather', 'storm', 'hurricane', 'fire', 'flood', 'precipitation', 'heat']):
        return 'Weather & Hazards'
    elif any(word in text_lower for word in ['shelter', 'housing', 'erv', 'client', 'assistance', 'casework']):
        return 'Client Services'
    elif any(word in text_lower for word in ['staffing', 'volunteer', 'dat', 'resourcing', 'logistics']):
        return 'Operations'
    elif any(word in text_lower for word in ['docc', 'activation', 'ops', 'current', 'portal']):
        return 'Command & Control'
    elif any(word in text_lower for word in ['risk', 'adaptation', 'community', 'planning']):
        return 'Risk & Planning'
    else:
        return 'General'

def generate_keywords(button_text):
    """Generate keywords from button text"""
    # Remove common words and split
    stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'a', 'an'}
    
    # Clean and split text
    words = re.findall(r'\b\w+\b', button_text.lower())
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    
    return ', '.join(keywords)

def categorize_menu_items(menu_items):
    """Organize menu items by category"""
    categories = {}
    
    for item in menu_items:
        category = item['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(item)
    
    # Sort items within each category
    for category in categories:
        categories[category].sort(key=lambda x: x['name'])
    
    return categories

def main():
    """Main function"""
    print("Extracting menu structure from Experience Builder data...")
    
    try:
        menu_data = extract_menu_from_experience_builder('experience_builder_data.json')
        
        # Convert to the format expected by your menu system
        formatted_menu = []
        
        for category, items in menu_data.items():
            for item in items:
                formatted_item = {
                    'name': item['name'],
                    'url': item['url'],
                    'category': category,
                    'keywords': item['keywords'],
                    'description': f"{item['name']} - {category}"
                }
                formatted_menu.append(formatted_item)
        
        # Save to menu.json
        with open('menu_extracted.json', 'w') as f:
            json.dump(formatted_menu, f, indent=2)
        
        print(f"✅ Extracted {len(formatted_menu)} menu items")
        print("📁 Saved to menu_extracted.json")
        
        # Print summary by category
        print("\n📊 Menu Summary by Category:")
        for category, items in menu_data.items():
            print(f"  {category}: {len(items)} items")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 