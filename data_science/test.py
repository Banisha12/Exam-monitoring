from sqlalchemy import create_engine
from urllib.parse import quote_plus

print("Let's test the MySQL connection.")

# 1. Type your exact password here
raw_password = "Banisha@890"

# 2. Safely encode the password (this fixes the % symbol issue)
safe_password = quote_plus(raw_password)

# 3. Create the connection string
DB_URI = f"mysql+pymysql://root:{safe_password}@localhost:3306/exam_monitor"

try:
    engine = create_engine(DB_URI)
    connection = engine.connect()
    print("✅ SUCCESS! Connected to MySQL perfectly.")
    connection.close()
except Exception as e:
    print(f"❌ FAILED. Error: {e}")