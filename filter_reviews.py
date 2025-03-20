import sqlite3

conn = sqlite3.connect("databse.db")
cursor = conn.cursor()

def get_reviews(sort_by="created_at", min_rating=None, max_rating=None, product_id=None, category_id=None):
    
  query = '''
    SELECT r.id, r.product_id, p.product_name, r.user_id, u.name, r.rating, r.review_text, r.created_at 
    FROM reviews r
    JOIN products p ON r.product_id = p.id
    LEFT JOIN users u ON r.user_id = u.id
    LEFT JOIN review_category_map rc ON r.id = rc.review_id
    LEFT JOIN review_categories c ON rc.category_id = c.id
    WHERE 1=1
    '''
  params = []

if min_rating:
  query += " AND r.rating >= ?"
  params.append(min_rating)
if max_rating:
  query += "AND r.rating <= ?"
  params.append(max_rating)
if product_id:
  query += "AND r.product_id = ?"
  params.append(product_id)
if category_id:
  query += "AND c.id = ?"
  params.append(category_id)

query += f" ORDER BY r.{sort_by} DESC"

cursor.execute(query, params)
results = cursor.fetchall()

# Close the connection
conn.close()
return results

if __name__ == "__main__":
  print("\nReviews sorted by date (default): ")
  for review in get_reviews():
    print(review)
  print("\nReviews for product_id = 1 sorted by rating: ")
  for review in get_reviews(sort_by="rating", product_id=1):
    print(review)
  print("\nReviews with a rating of at least 4:")
  for review in get_reviews(min_rating=4):
    print(review)


