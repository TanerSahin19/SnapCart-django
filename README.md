# SnapCart

SnapCart is a backend-focused e-commerce project built with Django.  
The main goal of this project is to build a solid understanding of real-world e-commerce logic by implementing products, categories, authentication, cart management, checkout, and order flow step by step.

This project was developed with a backend-first approach.  
The priority was not visual design, but building a clean and functional system architecture.

---

## Features

### User Authentication
- Register
- Login
- Logout
- User-based access control

### Product System
- Product listing
- Product detail page
- Category-based filtering
- Slug-based detail routing

### Cart System
- Database-based cart structure with `CartItem`
- Add product to cart
- Increase quantity
- Decrease quantity
- Remove product from cart
- Prevent adding more items than available stock
- Dynamic cart total calculation

### Checkout & Order System
- Checkout form
- Order creation from cart items
- OrderItem creation for each cart record
- Total price saved in order
- Cart cleanup after successful checkout
- Success page after order completion

### Order Management
- My Orders page
- Order detail page
- Order status system:
  - Pending
  - Shipped
  - Delivered

### Admin Panel
- Product and category management
- Order and OrderItem management
- Order status updates from admin panel

---

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Bootstrap 5

---

## Project Structure

This project follows a backend-first and app-based Django structure.

- `products` → product and category logic
- `cart` → database-based cart system
- `orders` → checkout and order flow
- `accounts` → authentication system
- `templates` → shared global templates
- app-specific templates → organized by feature

---

## Cart Logic

SnapCart uses a **database-based cart system**, not a session-based cart.

Each cart item is stored with:
- user
- product
- quantity

This makes the cart structure more suitable for real e-commerce workflows and order creation.

---

## Order Logic

Orders are separated into two models:

- `Order` → main order information
- `OrderItem` → products inside the order

Each order item stores:
- related order
- related product
- quantity
- price at the time of ordering

This makes the system more stable for future improvements.

---

## Learning Purpose

This project was built to practice and understand:

- Django app structure
- Model → View → URL → Template workflow
- Real cart logic
- Stock control
- Checkout flow
- Order relationships
- Backend thinking for e-commerce systems

The focus of the project is understanding the logic instead of memorizing code.

---

## Current Status

SnapCart currently includes the full basic e-commerce backend flow:

- authentication
- products
- categories
- cart
- checkout
- orders
- order history
- order detail

This project serves as a strong base for more advanced e-commerce projects in the future.

---

## Future Improvements

Possible next improvements:

- stock decrease after order completion
- payment integration
- coupon system
- product variation system
- search and filtering improvements
- order snapshots for product name/slug/image

---

## Author

Built as part of a long-term Django backend learning journey focused on understanding, repetition, and building production-style project logic.