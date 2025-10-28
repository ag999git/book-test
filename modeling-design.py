################ NEW ####################





################ NEW ###### EXAMPLE CODE SHOWING A PYTHON CLASSES AS SEPERATION OF CONCERN
# --- Step 1: Define an abstract class (common interface) ---
class Message:
    def send(self, text):
        pass  # Each subclass will define its own send method


# --- Step 2A: Define concrete classes (specific implementations) ---
class EmailMessage(Message):
    def send(self, text):
        print("Sending EMAIL:", text)

# --- Step 2B: Define concrete classes (specific implementations) ---
class SMSMessage(Message):
    def send(self, text):
        print("Sending SMS:", text)


# --- Step 3: Factory class (handles object creation) ---
class MessageFactory:
    def create_message(self, msg_type):
        if msg_type == "email":
            return EmailMessage()
        elif msg_type == "sms":
            return SMSMessage()
        else:
            print("Unknown message type!")
            return None


# --- Step 4: Client code (uses factory, not concrete classes directly) ---
def main():
    factory = MessageFactory()

    email = factory.create_message("email")
    sms = factory.create_message("sms")

    if email:
        email.send("Hello via Email!")

    if sms:
        sms.send("Hello via SMS!")


# --- Step 5: Run program ---
if __name__ == "__main__":
    main()



################ NEW ####################


################ NEW ####################


################ NEW ####################


################ NEW ####################
