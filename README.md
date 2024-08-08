# Typing-Speed-Calculator

Typing Speed Test is a Python-based application that allows users to test their typing speed and accuracy.

## Features

- **Difficulty Levels**: The application offers three difficulty levels - Easy, Medium, and Hard, with corresponding paragraphs of varying complexity.
- **Responsive User Interface**: The application provides clear instructions and feedback to the user during the test.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/typing-speed-test.git
   ```

2. Navigate to the project directory:

   ```
   cd typing-speed-test
   ```

3. Run the application:

   ```
   python main.py
   ```

## Usage

1. When the application starts, you'll see the welcome message and the main menu.
2. Choose "1. Start a new test" to begin the typing test.
3. Select the difficulty level you want to practice with (Easy, Medium, or Hard).
4. For paragraph mode, type the displayed text as quickly and accurately as possible. 
6. After the test, the application will display your typing speed (in words per minute) and the number of mistakes made.
7. You can repeat the test with a different difficulty level
8. To exit the application, choose "2. Exit" from the main menu.

## Development

This project was developed using Python 3. The following libraries are used:

- `time`: for measuring the time taken to type the text
- `random`: for randomly selecting a paragraph from the difficulty-specific lists

The code is structured with the following functions:

- `mistake(paraTest, userInput)`: Calculates the number of mistakes made by the user.
- `speed_wpm(startTime, endTime, userInput)`: Calculates the user's typing speed in words per minute.

The difficulty-specific paragraphs are stored in separate lists (`easy_paragraphs`, `medium_paragraphs`, `hard_paragraphs`), and a dictionary `difficulty_choices` is used to map the difficulty levels to the corresponding paragraph lists.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
