from notepad_page import NotepadPage
from logger_setup import setup_logger
import time

logger = setup_logger()

def run_notepad_test():
    notepad = NotepadPage()
    try:
        notepad.launch()
        time.sleep(1)  
        notepad.type_text("Refactored with POM for Maintainability!")
        time.sleep(1)

        # verifies if the text are entered correctly
        typed_text = notepad.editor.window_text()
        assert "Refactored with POM for Maintainability!" in typed_text, "Text not typed correctly"
    
        logger.info("Text verified successfully!")

    except Exception as e:
        logger.error(f"Test failed: {e}")
        notepad.capture_screenshot()
        raise

if __name__ == "__main__":
    run_notepad_test()