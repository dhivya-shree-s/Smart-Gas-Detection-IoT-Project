# main_gas_detector.py
# Python Backend Logic for Smart Gas Detection System

import random
import time

# --- Configuration ---
GAS_THRESHOLD = 700  # Sensor reading (MQ-2) for danger level
REFILL_THRESHOLD = 500  # Weight in grams for low gas alert

# --- Sensor Simulation Functions ---

def read_gas_sensor():
    """Simulates reading the gas sensor from the ESP8266."""
    # Returns a simulated reading
    return random.randint(50, 600)

def read_weight_sensor():
    """Simulates reading the gas cylinder weight (Load Cell)."""
    # Returns a simulated weight (e.g., 5.5 kg)
    return random.randint(5000, 14000)

def send_alert(message):
    """Placeholder for sending alerts (e.g., via mobile app or web API)."""
    print(f"[ALERT SENT]: {message}")

# --- Main System Logic ---

def check_system_status():
    print("--- System Status Check ---")

    # 1. Check for Gas Leak
    current_gas_level = read_gas_sensor()

    if current_gas_level > GAS_THRESHOLD:
        print(f"🔥 DANGER! GAS LEAK DETECTED. Level: {current_gas_level} units")
        send_alert("CRITICAL: Gas Leak Detected! Immediate Action Required.")
    else:
        print(f"✅ Safe. Gas Level: {current_gas_level} units")

    # 2. Check for Refill Status (Smart Booking Logic)
    current_weight = read_weight_sensor()

    if current_weight < REFILL_THRESHOLD:
        print(f"🟡 Gas Low. Weight: {current_weight}g. Triggering Automated Refill Booking...")
        send_alert("Gas Low: Automated refill booking initiated.")
    else:
        print(f"🟢 Gas OK. Weight: {current_weight}g.")

    print("-" * 30)

if __name__ == "__main__":
    # In a real environment, this would run continuously
    check_system_status() 
    print("Script executed successfully. Upload this file to GitHub.")
