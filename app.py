# Demo Scenarios:
# Case 1: Weak Wifi Connection (Home Internet)
# Case 2: Slow Connection Speed & Frequent Disconnections (Home Internet)
# Case 3: Regional Internet Outage Due To Scheduled/Known Maintenance (Home Internet)
# Case 4: Regional Internet Outage Due To Unknown Reasons (Home Internet)



from openai import OpenAI
import os

# Set up the API client with your secret key
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

# Various logs will be read from a log file. 
# This function will simply read the contents of the log file into a string.
def read_log_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data


# This list will be populated with the messages that we send to the API
messagesList=[
    {
        "role": "system",
        "content": "You are AI assistant that will help users of Turk Telekom solve their internet problems. You will be fed with many different logs and you will analyze them to find the problem and the solution. You should point out the important findings in the data you are given, provide a problem analysis and potential solutions. You should be polite and helpful."
    }
]






####################################################
def ask_gpt4():
    # Send the message to the API
    # Create a completion
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messagesList,
        temperature=0.8,
        max_tokens=600,

    )
    
    # Extract the response text and print it
    ai_text = completion.choices[0].message.content 
    
    

    # Append the interaction to the session prompt to maintain context
    new_answer = {
        "role": "assistant",
        "content": ai_text
    }
    messagesList.append(new_answer)
    
    return("AI: " + ai_text + "\n")


def select_scenario():
    print("Please select a scenario for the demo:")
    print("1. Weak Wifi Connection (Home Internet)")
    print("2. Slow Connection Speed & Frequent Disconnections (Home Internet)")
    print("3. Regional Internet Outage Due To Scheduled/Known Maintenance (Home Internet)")
    print("4. Regional Internet Outage Due To Unknown Reasons (Home Internet)")
    scenario = input("Enter the scenario number: ")
    if scenario == "1":
        return 1
    elif scenario == "2":
        return 2
    elif scenario == "3":
        return 3
    elif scenario == "4":
        return 4
    else:
        print("Invalid scenario number. Please try again.")
        quit()


def executeFlow(scenario, mode):
  
    first_message = ""
    # Execute the flow based on the selected mode
    if mode == 1:
        # User AI (Turk Telekom Chatbot)
        first_message= "You are now a ChatBot for Turk Telekom Users. The User will describe their problem to you. Then you will receive the logs from the router, connection and ISP. You will analyze the logs and provide a diagnosis and a solution to the problem. You should be polite and helpful. Focus on the problem and the solution, don't talk much about unrelated things. Give a short, brief answer. Give your answer in Turkish."
        
        systemMessage = {
            "role": "system",
            "content": first_message
        }
        
        
        
        messagesList.append(systemMessage)
        
        readLogs()
        
        print("AI: Welcome to Turk Telekom. How can I assist you today?")
        user_input = input("Describe your problem: ")
        
        user_message = {
            "role": "system",
            "content": "User's problem description: " + user_input
        }
        
        messagesList.append(user_message)
        
        print(ask_gpt4())
        while True:
            # Get user input
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "goodbye"]:
                print("AI: Goodbye!")
                break
            newUserMessage = {
                "role": "user",
                "content": user_input
            }
            messagesList.append(newUserMessage)
            print(ask_gpt4())
        
        
    elif mode == 2:
        # Call Center - AI (Diagnosis Help for Customer Care)
        # Directly read log files. No need for user input.
        first_message= "You are now an AI assistant for Turk Telekom Customer Care. You will receive the logs from the router, connection and ISP. You will analyze the logs and provide a diagnosis and a solution to the problem. You should be polite and helpful. Focus on the problem and the solution, don't talk much about unrelated things. Give a short, brief answer. Give your answer in Turkish."
        
        systemMessage = {
            "role": "system",
            "content": first_message
        }
        
        messagesList.append(systemMessage)
        
        readLogs()
        
        
        
        
        
    elif mode == 3:
        # Internal Communication
        # You will provide summary of the diagnosed problem and the actions taken by previous Customer Care agents.
        # Note: This mode is not implemented yet. Logs of previous problem diagnosis and actions taken by Customer Care agents will be used in the same way as mode 1 and 2.
        pass
    else:
        print("Invalid mode number. Please try again.")
        quit()
    
    
    
    if mode == 1:
        print(ask_gpt4())
        while True:
            # Get user input
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "goodbye"]:
                print("AI: Goodbye!")
                break
            newUserMessage = {
                "role": "user",
                "content": user_input
            }
            messagesList.append(newUserMessage)
            print(ask_gpt4())
    elif mode == 2:
        print(ask_gpt4())
    

def select_mode():
    print("Please select a mode:")
    print("1. User AI (Turk Telekom Chatbot)")
    print("2. Call Center - AI (Diagnosis Help for Customer Care)")
    print("3. Internal Communication")
    mode = input("Enter the mode number: ")
    # Check if the mode number is valid
    if mode == "1":
        return 1
    elif mode == "2":
        return 2
    elif mode == "3":
        return 3
    else:
        print("Invalid mode number. Please try again.")
        quit()

def readLogs():
    # Read all the basic log files for the selected scenario. (router.log, connection.log, isp.log) 
    router_log = open(f"logs/scenario{scenario}/router.log", "r")
    connection_log = open(f"logs/scenario{scenario}/connection.log", "r")
    isp_log = open(f"logs/scenario{scenario}/isp.log", "r")
    extra_notes = open(f"logs/scenario{scenario}/notes.log", "r")
    
    # Read router logs
    router_message = "Here are the logs from the router:" + router_log.read()

    # Read connection logs
    connection_message = "\nHere are the logs from the connection:" + connection_log.read()
    
    # Read ISP logs
    isp_message = "\nHere are the logs from the ISP:" + isp_log.read()
    
    # Read extra notes
    notes_message = "\nHere are the extra notes:" + extra_notes.read()
    
    logs_message = router_message + connection_message + isp_message + notes_message
    
    newMessage = {
        "role": "system",
        "content": logs_message
    }
    
    messagesList.append(newMessage)
    
    # Close the log files
    router_log.close()
    connection_log.close()
    isp_log.close()

if __name__ == "__main__":
    
    # Ask user to select a scenario for the demo
    scenario = select_scenario()
    
    mode = select_mode()
    
    # Execute the flow for the selected scenario
    executeFlow(scenario, mode)

    
