################ NEW #### EXAMPLE CODE SHOWING A PYTHON FUNCTIONS AS SEPERATION OF CONCERN

# Function 1: Get user input (responsible only for input)
def get_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

# Function 2: Perform addition (responsible only for calculation)
def add_numbers(a, b):
    return a + b

# Function 3: Display the result (responsible only for output)
def display_result(result):
    print(f"The sum is: {result}")

# Main function to coordinate all parts
def main():
    x, y = get_numbers()      # Input concern
    total = add_numbers(x, y) # Processing concern
    display_result(total)     # Output concern

# Run the program
if __name__ == "__main__":
    main()




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
