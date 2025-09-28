# flask-app
Web Application based on Flask.

The main idea behind this project is to play with Flask, Materialize and
Alpine.js and implement various patterns and functions in a minimalistic and
simple manner.

## Features
### Backend
- Blog
    - Post
    - Category
    - Tag
- Administration Panel
- User Management (Register\Login)
    - Roles:
        - Admin (has access to dashboard)
        - User (has access to some features but not to the dashboard)
- Localization
    - Two languages for now (English and Persian)

### Frontend
- Playground
    - Counter
    - MiniApp: Simple navigation between 2-3 pages with transitions and other
      eye-candy stuff
- Scroll-to-top
- Dark-mode Switcher
- Minimal Data-table component (using MaterializeCSS table and API
  pagination/filtering instead of 3rd-party plugins/libraries

## Dependencies
- **UI:** Materialize CSS, Alpine.js
- **Templating:** Jinja2
- **Database:** SQLite

## Issues
- [ ] Styling for the active navbar menu item
