import sqlite3

# Connect to database 
conn = sqlite3.connect("database.db")
cursor = conn.cursor()  

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    description TEXT
);
''')

# Create the reviews table
cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    user_id INTEGER,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
);
''')

# Create review categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS review_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE NOT NULL
);
''')

# Create review category map table
cursor.execute('''
CREATE TABLE IF NOT EXISTS review_category_map (
    review_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (review_id, category_id),
    FOREIGN KEY (review_id) REFERENCES reviews(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES review_categories(id) ON DELETE CASCADE
);
''')

# Commit and close the connection
conn.commit()
conn.close()

print("Database setup complete.")
