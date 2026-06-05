import requests
import random

# Mock IIT Canteen Data (Replace with real API when available)
CANTINA_MENU = [
    {"name": "Masala Dosa", "price": 25, "type": "Breakfast"},
    {"name": "Vada Pav", "price": 15, "type": "Snacks"},
    {"name": "Chicken Biryani", "price": 80, "type": "Lunch"},
    {"name": "Paneer Tikka", "price": 120, "type": "Dinner"},
    {"name": "Idli Sambhar", "price": 20, "type": "Breakfast"}
]

def get_canteen_menu():
    """Get today's canteen menu"""
    return random.sample(CANTINA_MENU, k=min(5, len(CANTINA_MENU)))