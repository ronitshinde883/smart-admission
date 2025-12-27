import random
from datetime import datetime

def generate_tracking_id():
    year = datetime.now().year
    random_number = random.randint(1000, 9999)
    return f"ADM-{year}-{random_number}"
