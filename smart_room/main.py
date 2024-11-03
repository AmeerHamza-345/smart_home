import streamlit as st
import emoji
import speech_recognition as sr

# Device base class
class Device:
    def __init__(self, name):
        self.name = name
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def status(self):
        return self.state

    def display(self):
        return f"{self.name}: {emoji.emojize(':green_circle:') if self.state else emoji.emojize(':red_circle:')} {'🟢 On' if self.state else '🔴 Off'}"


# Individual device classes
class Light(Device):
    def __init__(self):
        super().__init__("Light")


class Fan(Device):
    def __init__(self):
        super().__init__("Fan")


class AC(Device):
    def __init__(self):
        super().__init__("AC")


class LED(Device):
    def __init__(self):
        super().__init__("LED")


# Smart Room class
class SmartRoom:
    def __init__(self):
        self.devices = {
            "light": Light(),
            "fan": Fan(),
            "ac": AC(),
            "led": LED()
        }

    def turn_on_device(self, device_name):
        if device_name in self.devices:
            self.devices[device_name].turn_on()

    def turn_off_device(self, device_name):
        if device_name in self.devices:
            self.devices[device_name].turn_off()

    def get_device_status(self):
        return {name: device.display() for name, device in self.devices.items()}


# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        st.write(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        st.write("Sorry, I did not understand that.")
    except sr.RequestError:
        st.write("Could not request results from Google Speech Recognition service.")

# Streamlit App UI
smart_room = SmartRoom()

st.title("Smart Room Automation")
st.write("Control your room devices: Light, Fan, AC, and LED.")

# Create two columns for device status and updated status
col1, col2 = st.columns(2)

# Device Status
with col1:
    st.subheader("Device Status")
    for device in smart_room.get_device_status().values():
        st.write(device)

# Control buttons for manual toggling
if st.button("Turn On Light"):
    smart_room.turn_on_device("light")
if st.button("Turn Off Light"):
    smart_room.turn_off_device("light")
if st.button("Turn On Fan"):
    smart_room.turn_on_device("fan")
if st.button("Turn Off Fan"):
    smart_room.turn_off_device("fan")
if st.button("Turn On AC"):
    smart_room.turn_on_device("ac")
if st.button("Turn Off AC"):
    smart_room.turn_off_device("ac")
if st.button("Turn On LED"):
    smart_room.turn_on_device("led")
if st.button("Turn Off LED"):
    smart_room.turn_off_device("led")

# Listen for voice commands
if st.button("Listen for Commands"):
    command = recognize_speech()
    if command:
        if "turn on light" in command:
            smart_room.turn_on_device("light")
        elif "turn off light" in command:
            smart_room.turn_off_device("light")
        elif "turn on fan" in command:
            smart_room.turn_on_device("fan")
        elif "turn off fan" in command:
            smart_room.turn_off_device("fan")
        elif "turn on ac" in command:
            smart_room.turn_on_device("ac")
        elif "turn off ac" in command:
            smart_room.turn_off_device("ac")
        elif "turn on led" in command:
            smart_room.turn_on_device("led")
        elif "turn off led" in command:
            smart_room.turn_off_device("led")

# Updated Device Status
with col2:
    st.subheader("Updated Device Status")
    for device in smart_room.get_device_status().values():
        st.write(device)
