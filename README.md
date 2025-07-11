# FLROS - Experience Builder Menu System

## Overview
This project demonstrates proper Experience Builder menu navigation methods based on [ArcGIS Experience Builder documentation](https://doc.arcgis.com/en/experience-builder/latest/configure-widgets/menu-widget.htm) and [ESRI support articles](https://support.esri.com/en-us/knowledge-base/how-to-create-button-navigation-for-multiple-map-widget-000033685).

## Experience Builder Menu Methods

### 1. Menu Widget (Recommended)
- **Purpose**: Native Experience Builder widget for page navigation
- **Auto-populates** with pages, links, and folders from Page panel
- **Styles**: Default, underline, or pills
- **Types**: Horizontal, vertical, or icon (collapsible)
- **Best for**: Multi-page experiences with organized navigation

### 2. Button Widget Navigation
- **Purpose**: Custom buttons that link to specific pages or views
- **Configuration**: Use "Set link" → "Page" → Select target page
- **Best for**: Featured navigation, call-to-action buttons
- **Advantage**: Full control over button styling and placement

### 3. Views Navigation Widget
- **Purpose**: Navigate between different views within a Section widget
- **Auto-populates** buttons for views in selected section
- **Best for**: Switching between different data views on same page

### 4. Sidebar Widget Dropdown (Advanced)
- **Purpose**: Collapsible dropdown menu using Sidebar widget
- **Method**: Sidebar with collapsed state + List/Button widgets inside
- **Best for**: Space-saving navigation, mobile-friendly

## Project Structure

```
FLROS/
├── README.md                 # This documentation
├── menu-config.json         # Menu structure configuration
├── experience-builder-guide.md  # Step-by-step implementation guide
└── examples/                # Example configurations
    ├── menu-widget-config.json
    ├── button-navigation-config.json
    └── sidebar-dropdown-config.json
```

## Implementation Strategy

1. **Start with Menu Widget** for primary navigation
2. **Add Button Widgets** for featured/important pages
3. **Use Views Navigation** for data switching within pages
4. **Consider Sidebar Dropdown** for mobile or space-constrained layouts

## Key Advantages Over Custom HTML

- **Native Experience Builder integration**
- **Automatic page synchronization**
- **Theme inheritance**
- **Mobile responsiveness**
- **No iframe/embedding issues**
- **Built-in accessibility features**

## Next Steps

1. Create Experience Builder app
2. Set up page structure
3. Configure Menu widget
4. Add Button widgets for key navigation
5. Test and refine styling 