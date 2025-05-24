import os
import shutil
from yaspin import yaspin

DATABASE_PATH = "chroma"

def main():
    with yaspin(text="Clearing database...", color="cyan") as sp:
        clear_database()
        sp.ok("✅")
    print(f"\nDatabase has been cleared.")

def clear_database():
    if os.path.exists(DATABASE_PATH):
        shutil.rmtree(DATABASE_PATH)

if __name__ == "__main__":
    main()