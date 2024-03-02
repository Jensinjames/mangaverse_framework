import json
import logging

class FeedbackHandler:
    """
    A class that handles feedback by saving it to a JSON file and sending a notification.

    Attributes:
        feedback_file (str): The name of the JSON file to save the feedback to.

    Methods:
        handle_feedback(feedback): Handles the given feedback by saving it and sending a notification.
        save_feedback(feedback): Saves the feedback to the JSON file.
        send_notification(feedback): Simulates sending a notification about the feedback.
    """

    def __init__(self, feedback_file='feedback.json'):
        self.feedback_file = feedback_file
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def handle_feedback(self, feedback):
        logging.info("Handling feedback: %s", feedback)
        self.save_feedback(feedback)
        self.send_notification(feedback)

def save_feedback(self, feedback):
    """Saves feedback to a JSON file."""
    try:
        feedback_list = []
        try:
            # Try to read existing feedback into a list
            with open(self.feedback_file, 'r') as file:
                feedback_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # If file doesn't exist or is empty/corrupt, start a new list
            pass
        
        # Append new feedback and write back to the file
        feedback_list.append(feedback)
        with open(self.feedback_file, 'w') as file:
            json.dump(feedback_list, file, indent=4)  # Use indent for better readability
        
        logging.info("Feedback saved successfully.")
    except Exception as e:
        logging.error("Failed to save feedback: %s", e)

# Example usage
if __name__ == "__main__":
    feedback_handler = FeedbackHandler()
    test_feedback = {"user": "User123", "comment": "This is a test feedback."}
    feedback_handler.handle_feedback(test_feedback)
# Output: INFO:root:Handling feedback: {'user': 'User123', 'comment': 'This is a test feedback.'}
# INFO:root:Feedback saved successfully.
# INFO:root:Sending notification for feedback: {'user': 'User123', 'comment': 'This is a test feedback.'}