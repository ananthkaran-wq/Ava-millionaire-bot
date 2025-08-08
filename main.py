import telebot
import schedule
import time
from datetime import datetime

# Your bot token
os.environ['BOT_TOKEN']
CHAT_ID = "979707505"  # Replace with your Telegram user ID

bot = telebot.TeleBot(BOT_TOKEN)

# 30-day millionaire bootcamp tasks
tasks = [
    "Day 1: Wealth Reset Ritual – Write your Millionaire Vision Statement. Burn old limiting beliefs.",
    "Day 2: Audit Your Circle – List your top 5 people. Spend 10% more time with the ‘fuel’ crowd.",
    "Day 3: Zero Excuses Rule – Reframe all blame as: 'What’s my next move?'",
    "Day 4: Opportunity Spotting Drill – Write down every money-making idea you see today.",
    "Day 5: Rich Morning Ritual – Wake 1 hr earlier, 20 min workout, 20 min reading, 20 min market research.",
    "Day 6: No-News Day – Protect your mental bandwidth.",
    "Day 7: Weekly Wealth Review – Wins, lessons, next steps.",
    "Day 8: Skill Identification – Pick or refine 3 high-income skills.",
    "Day 9: Time ROI Audit – Track all activities as $10/hr, $100/hr, or $1000/hr work.",
    "Day 10: Millionaire Networking Move – Reach out to someone richer/smarter.",
    "Day 11: Monetize a Skill – Offer a paid service today.",
    "Day 12: Simplify to Multiply – Cut 1 low-value activity.",
    "Day 13: Leverage List – Write 10 ways to multiply efforts with tools/people/systems.",
    "Day 14: Weekly Wealth Review.",
    "Day 15: Net Worth Day – Calculate assets, debts, net worth.",
    "Day 16: Cash Flow Map – Cut 1 expense, boost 1 income stream.",
    "Day 17: Investing Basics Drill – Learn index funds & REITs.",
    "Day 18: Automated Investing Setup – Even $10/month counts.",
    "Day 19: Buy an Asset – Stock, domain, course, etc.",
    "Day 20: Leverage Other People’s Skills – Hire a freelancer for a task.",
    "Day 21: Weekly Wealth Review.",
    "Day 22: Decision-Making Mastery – Apply 10-10-10 rule to a choice.",
    "Day 23: System Build Day – Automate a repetitive task.",
    "Day 24: Offer Creation Drill – Create a $100+ product/service.",
    "Day 25: Raise Your Rate Day – Increase your prices/value.",
    "Day 26: Delegate Something – Remove a task from your plate.",
    "Day 27: Risk Expansion Day – Take a calculated risk.",
    "Day 28: Weekly Wealth Review.",
    "Day 29: Empire Vision Planning – Write your 10-year wealth plan.",
    "Day 30: Celebration & Compounding Check – Celebrate wins, commit to continuing."
]

# Send today's message based on start date
start_date = datetime(2025, 8, 9)  # Change to your Day 1 date
def send_daily_task():
    day_number = (datetime.now().date() - start_date.date()).days
    if 0 <= day_number < len(tasks):
        bot.send_message(CHAT_ID, tasks[day_number])

# Schedule for 6:30 AM IST
def job():
    send_daily_task()

schedule.every().day.at("01:00").do(job)  # 01:00 UTC = 6:30 IST

while True:
    schedule.run_pending()
    time.sleep(30)
