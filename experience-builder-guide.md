# Florida Regional Operating Summary (FLROS) - Experience Builder Implementation Guide

## Step 1: Create New Experience Builder App

1. Go to [ArcGIS Experience Builder](https://experience.arcgis.com/builder/)
2. Click **Create New**
3. Select **Blank** template
4. Name your experience: "Florida Regional Operating Summary (FLROS)"

## Step 2: Set Up Page Structure

### Create Main Pages
1. In the **Page** panel, rename the default page to "Home"
2. Add new pages for each Florida category:
   - Right-click in Page panel → **Add Page**
   - Create pages:
     - 1 Situational Awareness
     - 2 Weather & Hazards
     - 3 Logistics & Resources
     - 4 Operations
     - 5 Response Services

### Create Sub-pages
For each main Florida category page, add sub-pages:

**1 Situational Awareness sub-pages:**
- Operating Picture
- SECAR SitAware

**2 Weather & Hazards sub-pages:**
- Weather / Maps / Radar
- National Weather
- National Hurricane Center
- Tropical Atlantic
- Flood Gauges

**3 Logistics & Resources sub-pages:**
- Trailer & Warehouse
- Workforce
- Partnerships

**4 Operations sub-pages:**
- Current Operations
- Shelter Intake
- Call Center
- Disaster Service Tech

**5 Response Services sub-pages:**
- DAT Response
- Home Fire Campaign
- FD Engage Dashboard
- Level 1-2 Response

## Step 3: Configure Menu Widget

### Add Menu Widget to Home Page
1. Go to **Home** page
2. Click **Insert** → Search for "Menu"
3. Drag **Menu Widget** to top of page
4. Configure Menu Widget:
   - **Type**: Horizontal
   - **Style**: Pills
   - **Spacing**: 10px
   - **Alignment**: Center
   - **Show Icon**: Yes
   - **Submenu Expand Mode**: Foldable

### Menu Widget Settings
```json
{
  "type": "horizontal",
  "style": "pills",
  "spacing": 10,
  "alignment": "center",
  "showIcon": true,
  "submenuExpandMode": "foldable"
}
```

## Step 4: Add Featured Button Navigation

### Create Button Widgets on Home Page
1. Add **Button Widget** for each featured section
2. Configure each button:

**Situational Awareness Button:**
- Text: "Situational Awareness"
- Icon: Dashboard icon
- Set Link → Page → 1 Situational Awareness
- Style: Primary button
- Color: Purple theme

**Weather & Hazards Button:**
- Text: "Weather & Hazards"  
- Icon: Weather icon
- Set Link → Page → 2 Weather & Hazards
- Style: Secondary button
- Color: Blue theme

**Operations Button:**
- Text: "Operations"
- Icon: Operations icon
- Set Link → Page → 4 Operations
- Style: Secondary button
- Color: Orange theme

## Step 5: Configure Page Navigation

### For Each Sub-page:
1. Select the page (e.g., "National")
2. Add **Button Widget** or **Menu Widget**
3. Configure button:
   - **Set Link** → **Page** → Select target page
   - **Open in**: App window
   - **Tooltip**: Descriptive text

### Link Configuration Example:
```
Link to: Page
Select a page: [Target Page Name]
Open in: App window
```

## Step 6: Add Content to Pages

### For Each Operational Page:
1. Add **Embed Widget** or **Map Widget**
2. Configure to display your operational dashboard
3. Set source URL to your existing Florida Experience Builder pages:
   - Base URL: `https://experience.arcgis.com/experience/f0cdcfa1d08d48da97197c51c6e3169d`
   - Page URLs: `/page/[PageName]`

## Step 7: Advanced Features

### Sidebar Dropdown Menu (Optional)
1. Add **Sidebar Widget**
2. Configure:
   - **Dock Side**: Down (third option)
   - **Size**: 200px
   - **Overlay**: Off
   - **Resizable**: Off
   - **Default State**: Collapsed
3. Add **List Widget** or **Button Widgets** inside sidebar
4. Style collapse button as needed

### Views Navigation (For Data Switching)
1. Add **Section Widget** with multiple views
2. Add **Views Navigation Widget**
3. Link to section for automatic view switching

## Step 8: Styling and Theming

### Theme Configuration
1. Go to **Theme** panel
2. Select or customize theme colors to match your brand
3. Configure:
   - Primary colors
   - Secondary colors
   - Button styles
   - Typography

### Custom Styling
- Use **Advanced** settings in widget panels
- Override theme colors as needed
- Set consistent spacing and alignment

## Step 9: Testing and Publishing

### Testing
1. Click **Live View** to test navigation
2. Verify all buttons and menu items work
3. Test on different screen sizes
4. Check mobile responsiveness

### Publishing
1. Click **Save** regularly during development
2. Click **Publish** when ready
3. Share published URL with users

## Key Benefits of This Approach

✅ **Native Experience Builder integration**
✅ **Automatic page synchronization**
✅ **Theme inheritance**
✅ **Mobile responsiveness**
✅ **No iframe/embedding issues**
✅ **Built-in accessibility features**
✅ **Easy maintenance and updates**

## Troubleshooting

### Common Issues:
1. **Menu not populating**: Check page visibility settings
2. **Buttons not working**: Verify "Set Link" configuration
3. **Mobile issues**: Test responsive design settings
4. **Theme conflicts**: Use Advanced styling to override

### Best Practices:
- Keep page hierarchy simple
- Use consistent naming conventions
- Test navigation flow thoroughly
- Optimize for mobile devices
- Use tooltips for better UX 