import os  
import re  
from datetime import datetime, timezone  
from pathlib import Path  

REPO_ROOT = Path(__file__).resolve().parent.parent  
PROBLEMS_DIR = REPO_ROOT / "problems"  
README_PATH = REPO_ROOT / "README.md"  

DIFFICULTY_MAP = {  
    "easy": "🟢 Easy",  
    "medium": "🟡 Medium",  
    "hard": "🔴 Hard",  
}  

DIFFICULTY_ORDER = {"easy": 0, "medium": 1, "hard": 2}  

def parse_problem_metadata(folder_path: Path):  
    """Parse solution metadata from folder name and README inside it."""  
    folder_name = folder_path.name  

    # Folder format: {number}-{slug}  e.g., "0001-two-sum"  
    match = re.match(r"^(\d+)-(.+)$", folder_name)  
    if not match:  
        return None  

    problem_number = int(match.group(1))  
    slug = match.group(2)  

    # Default values  
    title = slug.replace("-", " ").title()  
    difficulty = "easy"  
    date = datetime.fromtimestamp(  
        os.path.getmtime(folder_path / "Solution.java")  
    ).strftime("%d-%m-%Y")  

    # Check if there's a README with metadata  
    readme_path = folder_path / "README.md"  
    if readme_path.exists():  
        content = readme_path.read_text()  

        # Extract title from first heading  
        title_match = re.search(r"^# (.+)$", content, re.MULTILINE)  
        if title_match:  
            title = title_match.group(1).strip()  

        # Extract difficulty  
        diff_match = re.search(r"\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)", content, re.IGNORECASE)  
        if diff_match:  
            difficulty = diff_match.group(1).lower()  

    return {  
        "number": problem_number,  
        "title": title,  
        "difficulty": difficulty,  
        "date": date,  
        "folder": folder_name,  
        "slug": slug,  
    }  

def build_solution_table(problems):  
    """Build the solution log table."""  
    if not problems:  
        return "| # | Date | Problem | Difficulty | Solution |\n|---|------|---------|------------|----------|\n| _No solutions yet. Push your first one!_ | | | | |"  
