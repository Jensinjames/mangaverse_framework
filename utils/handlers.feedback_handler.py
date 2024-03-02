import json
import logging

class FeedbackHandler:
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
            with open(self.feedback_file, 'a') as file:
                json.dump(feedback, file)
                file.write('\n')  # For readability in the JSON file
            logging.info("Feedback saved successfully.")
        except Exception as e:
            logging.error("Failed to save feedback: %s", e)

    def send_notification(self, feedback):
        """Simulates sending a notification about the feedback."""
        # Placeholder for sending a notification (e.g., email, SMS)
        logging.info("Sending notification for feedback: %s", feedback)

# Example usage
if __name__ == "__main__":
    feedback_handler = FeedbackHandler()
    test_feedback = {"user": "User123", "comment": "This is a test feedback."}
    feedback_handler.handle_feedback(test_feedback)
