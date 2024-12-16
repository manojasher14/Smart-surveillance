from telegram import Bot
# Telegram Bot credentials
BOT_TOKEN = 7690326782:AAE0w6MMKiudA9L-Ww-WfmfsyfKEgcDvV8Q  # Replace with your BotFather token
CHAT_ID = 6786809522  # Replace with the recipient's Chat ID

# Alert message and video file
alert_message = "🚨 Alert! Suspicious activity detected.\nPlease check the attached video."
video_file_path = "/Users/manojasher/Downloads/IMG_9061.mov"  # Replace with the path to your video file

# Function to send an alert message with a video
def send_alert_with_video():
    bot = Bot(token=BOT_TOKEN)
    try:
        # Send an alert text message
        bot.send_message(chat_id=CHAT_ID, text=alert_message)
        print("Alert message sent successfully!")

        # Send the video clip
        with open(video_file_path, "rb") as video_file:
            bot.send_video(chat_id=CHAT_ID, video=video_file, caption="🔍 Video Footage")
            print("Video clip sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Run the function
if __name__ == "__main__":
    send_alert_with_video()
