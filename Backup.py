import random
import yaml

# Load the messages from the file
with open('messages.txt', 'r') as f:
    messages = [line.strip() for line in f.readlines()]

# Generate a random value between 5 and 45 for each Money_Alerts
def generate_random_money_alerts(num_money_alerts):
    money_alerts = {}
    for i in range(1, num_money_alerts+1):
        money_alert_name = f"Money_Alerts_{i:03d}"
        random_value = random.randint(5, 45)
        message = random.choice(messages)
        if '"' not in message:
            message = f"'{message}'"
        money_alerts[money_alert_name] = {
            'default': {
                'chance': 1,
                'commands': [f"rec purse remove %player% {random_value}"],
                'messages': [message]
            }
        }
    return money_alerts

# Generate 3 Money_Alerts with random messages and values
money_alerts = generate_random_money_alerts(215)

# Write the YAML file
with open('config.yml', 'w') as f:
    yaml.dump({'reward-list': money_alerts}, f)
