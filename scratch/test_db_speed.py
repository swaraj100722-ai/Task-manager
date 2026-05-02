import os
import sys
import time
import django

# Add the project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.db import connection

def test_db():
    print("Testing database connection speed with CONN_MAX_AGE...")
    
    for i in range(3):
        start = time.time()
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        end = time.time()
        print(f"Query {i+1} took: {end - start:.4f} seconds")
        
        # Don't close connection manually to test persistence

if __name__ == "__main__":
    test_db()
