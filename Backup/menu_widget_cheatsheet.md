# 🚦 Menu Widget Cheat Sheet for Experience Builder

## 1. Add the Menu Widget to Your Experience
- Upload or embed your `index.html` menu file as a custom widget or via an iframe in Experience Builder.
- Make sure the file is accessible (hosted on the same server or a public URL).

---

## 2. Add or Edit Pages in Experience Builder
- Create new pages in Experience Builder as usual.
- Each page will have a unique “slug” (the part after `/page/` in the URL).

  **Example:**  
  `https://experience.arcgis.com/experience/ce0b7dc7574c49a8a82f36443fee494f/page/New-Page`  
  → The slug is `New-Page`

---

## 3. Edit the Menu (Add/Edit/Delete Items)
1. **Open your menu HTML in a browser.**
2. **Click the faint “Admin” button** (top right of the menu).
3. **Enter the password:** `redcross`
4. **Use the editor to:**
   - **Add a new menu item:**  
     - Click “Add Item” under the desired category.
     - Set the **Title** (what users see).
     - Set the **URL** (the page slug, e.g., `New-Page`).
     - Set the **Search Term** (for search/filtering).
   - **Edit or delete items/categories** as needed.
5. **Export JSON (optional):**  
   - Click “Export JSON” to save a backup of your menu data.

---

## 4. Save and Deploy
- After editing, save the HTML file.
- Re-upload or update the file in Experience Builder or your hosting location.

---

## 5. Transferring to Another Project
- Copy the HTML file to the new project.
- Update menu items’ URLs to match the new project’s page slugs.

---

## Quick Reference
- **Admin password:** `redcross`
- **URL field:** Only the page slug (not the full URL)
- **Export JSON:** For backup or sharing menu data

---

**Need help?**  
Just open the menu, click “Admin,” and you’re in control! 