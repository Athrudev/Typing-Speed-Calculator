from time import *
import random as r


def mistake(paraTest,userInput):
  err=0
  for i in range(len(paraTest)):
    try:
      if paraTest[i]!=userInput[i]:
        err=err+1
    except: #we are adding this try except block because if user inputs more than the paraTest then it will thorow an out of bound error
      err=err+1
  return err

def speed_wpm(startTime,endTime,userInput):
  timeDelay=endTime-startTime
  timeDelay=round(timeDelay,2)
  speed=len(userInput)/timeDelay
  return round(speed)


easy_paragraphs = [
    "The sun is shining brightly today. It's a perfect day for a picnic in the park.",
    "I love to read books in my free time. Reading helps me learn new things and relax.",
    "Cooking is a fun hobby. I enjoy trying new recipes and sharing meals with friends.",
    "Music has the power to change our mood. A good song can make us feel happy or calm.",
    "Weekends are a great time to catch up with family and friends. We often have barbecues in the backyard.",
    "Pets can be wonderful companions. Dogs are known for their loyalty and cats for their independence.",
    "Gardening is a relaxing activity. It's satisfying to watch plants grow from seeds to flowers.",
    "Riding a bicycle is good exercise. It's also an eco-friendly way to travel short distances.",
    "Watching movies is a popular pastime. Everyone has their favorite genres and actors.",
    "Taking a walk in nature can be very refreshing. It helps clear the mind and reduce stress."
]

medium_paragraphs = [
    "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the English alphabet at least once.",
    "Learning a new language can be challenging, but it's also very rewarding. It opens up new cultures and perspectives.",
    "Exercise is important for maintaining good health. A combination of cardio and strength training is often recommended.",
    "Photography is both an art and a science. It requires technical knowledge as well as a creative eye for composition.",
    "The Internet has revolutionized the way we communicate and access information. It has connected people across the globe.",
    "Climate change is a pressing issue that affects us all. Small changes in our daily lives can contribute to a more sustainable future.",
    "Artificial intelligence is becoming increasingly prevalent in our lives. From smartphones to smart homes, AI is all around us.",
    "The human brain is capable of incredible feats. It can process vast amounts of information and make complex decisions in seconds.",
    "Space exploration continues to captivate our imagination. The possibility of finding life on other planets is particularly intriguing.",
    "Renewable energy sources like solar and wind power are becoming more important as we try to reduce our reliance on fossil fuels."
]

hard_paragraphs = [
    "Quantum computing leverages the principles of quantum mechanics to process information. It has the potential to revolutionize fields such as cryptography and drug discovery.",
    "The human brain is a complex organ that scientists are still working to fully understand. It contains approximately 86 billion neurons, each forming thousands of connections.",
    "Climate change is a pressing global issue that requires international cooperation to address. It affects various aspects of our environment, from weather patterns to ecosystems.",
    "The theory of relativity, proposed by Albert Einstein, fundamentally changed our understanding of space, time, and gravity. It has been extensively tested and verified over the past century.",
    "Blockchain technology, best known for underpinning cryptocurrencies, has potential applications in various fields including finance, supply chain management, and voting systems.",
    "The human genome project, completed in 2003, mapped all human genes. This breakthrough has paved the way for personalized medicine and deeper understanding of genetic diseases.",
    "Artificial neural networks, inspired by biological neural networks, form the basis of many modern machine learning algorithms. They've achieved remarkable results in tasks such as image and speech recognition.",
    "The concept of dark matter was proposed to explain gravitational effects observed in the universe that cannot be accounted for by visible matter alone. It remains one of the biggest mysteries in modern physics.",
    "CRISPR-Cas9 is a revolutionary gene-editing tool that allows scientists to make precise changes to DNA. It has potential applications in treating genetic disorders and improving crop yields.",
    "The Internet of Things (IoT) refers to the interconnected network of physical devices embedded with electronics, software, and network connectivity. It's transforming how we interact with our environment and manage resources."
]

difficulty_choices = {
    "1": ("Easy", easy_paragraphs),
    "2": ("Medium", medium_paragraphs),
    "3": ("Hard", hard_paragraphs)
}

print("===== Welcome to the Typing Speed Test =====")
print("This test will measure your typing speed and accuracy.")
print("Are you ready to challenge your typing skills?\n")


while True:

    print("\n===== Welcome to the Typing Speed Test =====")
    print("1. Start a new test")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        print("\nChoose difficulty level:")
        for key, (name, _) in difficulty_choices.items():
            print(f"{key}. {name}")
        difficulty = input("Enter difficulty (1/2/3): ")



        difficulty_name, paragraphs = difficulty_choices.get(difficulty, ("Medium", medium_paragraphs))
        print(f"\nSelected difficulty: {difficulty_name}")



        test = r.choice(paragraphs)
        print("\n===== Typing Speed Test =====")
        print("Type the following text as quickly and accurately as you can:\n")
        print(test, "\n")
        start_time = time()
        user_input = input("Start typing: ")
        end_time = time()

        print(f"\nTest completed!")
        print(f"Your typing speed: {speed_wpm(start_time, end_time, user_input)} words per minute")
        print(f"Mistakes made: {mistake(test, user_input)}")
        print("Keep practicing to improve your speed and accuracy!")

    elif choice == "2":
        print("Thank you for using our Typing Speed Test tool. Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")

