import random
import yaml
import tkinter as tk

# Load the messages from the file
with open('messages.txt', 'r') as f:
    messages = [line.strip() for line in f.readlines()]

def generate_alerts():
    num_money_alerts = int(num_alerts.get())
    # Generate a random value between 5 and 45 for each Money_Alerts
    money_alerts = {}
    for i in range(1, num_money_alerts+1):
        money_alert_name = f"Money_Alerts_{i:03d}"
        random_value = random.randint(5, 45)
        message = random.choice(messages)
        money_alerts[money_alert_name] = {
            'default': {
                'chance': 1,
                'commands': [f"rec purse remove %player% {random_value}"],
                'messages': [message]
            }
        }

    # Write the YAML file
    with open('config.yml', 'w') as f:
        yaml.dump({'reward-list': money_alerts}, f)

# Create the window
root = tk.Tk()
root.title("Money Alerts Generator")

# Add the label and input for the number of alerts
num_alerts_label = tk.Label(root, text="Number of alerts:")
num_alerts_label.pack(side=tk.LEFT)
num_alerts = tk.Entry(root)
num_alerts.pack(side=tk.LEFT)

# Add the generate button
generate_button = tk.Button(root, text="Generate", command=generate_alerts)
generate_button.pack(side=tk.LEFT)

# Start the main loop
root.mainloop()
