import pandas as pd
import random

spam_templates = [
    "Congratulations! You have won {amount}. Click here to claim.",
    "Get {discount}% discount on {product}. Limited time offer!",
    "Earn {amount} daily from home. No experience needed.",
    "Your account is at risk. Verify immediately using this link.",
    "Win a brand new {product}. Participate now!",
    "Exclusive deal: Buy {product} at {discount}% off.",
    "Free {subscription} for {time}. Activate now.",
    "Claim your reward of {amount} now.",
    "Limited offer expires in {time}. Hurry up!",
    "Click here to unlock premium features for free."
]

ham_templates = [
    "Hey, are we meeting at {time}?",
    "Please send me the {document}.",
    "Let's catch up this {day}.",
    "Meeting is scheduled at {time}.",
    "Can you call me when free?",
    "Thanks for your help with {task}.",
    "I will be late today.",
    "Please review the {document}.",
    "Your order will arrive on {day}.",
    "Let me know your availability."
]

amounts = ["₹1000", "₹5000", "$100", "$500", "₹10000"]
discounts = ["50", "60", "70", "80", "90"]
products = ["iPhone", "laptop", "headphones", "course", "subscription"]
times = ["today", "tomorrow", "tonight", "in 2 hours"]
days = ["Monday", "Tuesday", "Friday", "weekend"]
documents = ["report", "assignment", "notes", "file"]
tasks = ["project", "assignment", "presentation"]
subscriptions = ["Netflix", "Amazon Prime", "Spotify"]

data = []

# Generate spam
for _ in range(2500):
    text = random.choice(spam_templates).format(
        amount=random.choice(amounts),
        discount=random.choice(discounts),
        product=random.choice(products),
        time=random.choice(times),
        subscription=random.choice(subscriptions)
    )
    data.append([text, "spam"])

# Generate ham
for _ in range(2500):
    text = random.choice(ham_templates).format(
        time=random.choice(times),
        day=random.choice(days),
        document=random.choice(documents),
        task=random.choice(tasks)
    )
    data.append([text, "ham"])

# Add tricky real-world mixed cases
extra = [
    ["Hey, get 50% off pizza today!", "spam"],
    ["Your OTP is 482193. Do not share it.", "ham"],
    ["Reminder: your subscription expires today.", "ham"],
    ["Limited seats available. Register now.", "spam"],
    ["Your electricity bill is due.", "ham"],
]

data.extend(extra)

random.shuffle(data)

df = pd.DataFrame(data, columns=["text", "label"])

df.to_csv("data/spam.csv", index=False)

print("✅ 5000 dataset generated successfully!")