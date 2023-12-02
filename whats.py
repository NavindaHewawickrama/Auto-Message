import pywhatkit as kit
import datetime

# Replace 'your_message' with the message you want to send
message = "Hello, this is a group message!"

# Replace 'group_name' with the exact name of the WhatsApp group
group_name = "Final Year Project"

# Get the current time
current_time = datetime.datetime.now()
# Set the time you want to send the message (in 24-hour format)
scheduled_time = current_time + datetime.timedelta(minutes=1)  # Send the message in 1 minute

# Convert the time to the required format (hour and minute)
hour, minute = scheduled_time.hour, scheduled_time.minute

# Send the message to the group
kit.sendwhatmsg_to_group(group_name, message, hour, minute)

print(f"Message scheduled to be sent to {group_name} at {hour}:{minute}")
