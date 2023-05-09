import random
import yaml

# Load the messages from the file
with open('messages.txt', 'r') as f:
    messages = [line.strip() for line in f.readlines()]

# Generate a random value between 5 and 45 for each Money_Alerts
def generate_random_money_alerts(num_money_alerts):
    money_alerts = {}
    shuffled_messages = messages.copy()
    random.shuffle(shuffled_messages)
    message_counter = 0
    for i in range(1, num_money_alerts+1):
        money_alert_name = f"Money_Alerts_{i:03d}"
        random_value = random.randint(5, 45)
        message = shuffled_messages[message_counter]
        message_counter += 1
        if message_counter >= len(messages):
            message_counter = 0
            random.shuffle(shuffled_messages)
        money_alerts[money_alert_name] = {
            'default': {
                'chance': 1,
                'commands': [f"rec purse remove %player% {random_value}"],
                'messages': [message]
            }
        }
    return money_alerts


# Generate 215 Money_Alerts with random messages and values
money_alerts = generate_random_money_alerts(950)

# Write the YAML file
with open('config.yml', 'w') as f:
    yaml.dump({'reward-list': money_alerts}, f, default_flow_style=False)
