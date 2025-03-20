import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def add_review(product_id, user_id, rating, review_text):
  try:
     cursor.execute('''
            INSERT INTO reviews (product_id, user_id, rating, review_text)
            VALUES (?, ?, ?, ?)
        ''', (product_id, user_id, rating, review_text))
        
        conn.commit()
        print(f"Review added successfully for product ID {product_id}!")
    except sqlite3.Error as e:
        print(f"Error adding review: {e}")

  if __name__ == "__main__":
    print("\nAdding test reviews: \n")
    add_review(1, 1, 5, 
