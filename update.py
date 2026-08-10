from datetime import datetime
from pathlib import Path

file = Path("data.txt")

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with file.open("a", encoding="utf-8") as f:
    f.write(f"Repository maintenance: {today}\n")

print("Updated:", today)
