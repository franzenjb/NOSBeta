#!/usr/bin/env python3
"""
Convert extracted menu format to existing NOSBeta menu format
"""

import json
from collections import defaultdict

def convert_to_nos_format(input_file, output_file):
    """Convert the extracted menu format to NOSBeta format"""
    
    # Load the extracted menu
    with open(input_file, 'r') as f:
        extracted_menu = json.load(f)
    
    # Group by category
    categories_dict = defaultdict(list)
    for item in extracted_menu:
        # Extract page ID from URL
        page_id = item['url'].split('page=')[1] if 'page=' in item['url'] else item['url']
        
        # Create menu item in NOSBeta format
        menu_item = {
            "title": item['name'],
            "url": page_id,  # Just the page ID, not full URL
            "searchTerm": item['keywords']
        }
        
        categories_dict[item['category']].append(menu_item)
    
    # Define category mappings and colors
    category_config = {
        "Active Disasters": {"id": "disasters", "color": "red", "title": "Active Disasters"},
        "Command & Control": {"id": "command", "color": "orange", "title": "Command & Control"},
        "Weather & Hazards": {"id": "weather", "color": "blue", "title": "Weather & Hazards"},
        "Client Services": {"id": "services", "color": "green", "title": "Client Services"},
        "Operations": {"id": "operations", "color": "purple", "title": "Operations"},
        "Risk & Planning": {"id": "planning", "color": "teal", "title": "Risk & Planning"},
        "General": {"id": "general", "color": "gray", "title": "General Resources"}
    }
    
    # Create categories array
    categories = []
    
    for category_name, config in category_config.items():
        if category_name in categories_dict:
            category = {
                "id": config["id"],
                "title": config["title"],
                "color": config["color"],
                "items": sorted(categories_dict[category_name], key=lambda x: x['title'])
            }
            categories.append(category)
    
    # Create the final menu structure
    nos_menu = {
        "categories": categories,
        "footerButton": {
            "title": "Contact with Questions",
            "url": "page_117",
            "color": "red",
            "searchTerm": "contact, questions, help, support"
        }
    }
    
    # Save the converted menu
    with open(output_file, 'w') as f:
        json.dump(nos_menu, f, indent=2)
    
    print(f"✅ Converted menu saved to {output_file}")
    print(f"📊 Categories: {len(categories)}")
    
    for category in categories:
        print(f"  {category['title']}: {len(category['items'])} items")

def main():
    """Main function"""
    print("🔄 Converting menu format to NOSBeta structure...")
    convert_to_nos_format('menu_updated.json', 'menu_converted.json')
    print("\n🎉 Conversion complete!")

if __name__ == "__main__":
    main() 