import os

def collect_feedback(filename):
    print("Enter feedback (type 'END' on a new line to finish):")
    with open(filename, 'w') as file:
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            file.write(line.strip() + '\n')
    print("Feedback saved successfully.\n")

def count_word_occurrences(filename, word="good"):
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                count += line.lower().count(word.lower())
        print(f"The word '{word}' appeared {count} times in the feedback.\n")
    except FileNotFoundError:
        print("Feedback file not found.")

def remove_empty_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line for line in file if line.strip()]
        with open(filename, 'w') as file:
            file.writelines(lines)
        print("Empty lines removed successfully.\n")
    except FileNotFoundError:
        print("Feedback file not found.")

def display_feedback_with_keywords(filename):
    keywords = ["excellent", "poor", "average"]
    print("Feedback containing rating words:")
    try:
        with open(filename, 'r') as file:
            for line in file:
                if any(word in line.lower() for word in keywords):
                    print(f"- {line.strip()}")
    except FileNotFoundError:
        print("Feedback file not found.")

def generate_summary_report(filename):
    positive_keywords = ["good", "excellent", "great", "amazing", "satisfactory"]
    negative_keywords = ["poor", "bad", "unsatisfactory", "average", "worst"]
    total = 0
    positive = 0
    negative = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():
                    total += 1
                    lower_line = line.lower()
                    if any(word in lower_line for word in positive_keywords):
                        positive += 1
                    elif any(word in lower_line for word in negative_keywords):
                        negative += 1
        print("\n--- Feedback Summary Report ---")
        print(f"Total feedback entries: {total}")
        print(f"Positive comments: {positive}")
        print(f"Negative comments: {negative}\n")
    except FileNotFoundError:
        print("Feedback file not found.")

# ======================
# Main Menu
# ======================
def main():
    filename = "feedback.txt"
    
    while True:
        print("\n--- Feedback Collection System ---")
        print("1. Collect and store feedback")
        print("2. Count occurrences of the word 'good'")
        print("3. Remove empty lines from feedback")
        print("4. Display feedback with rating words")
        print("5. Generate summary report")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            collect_feedback(filename)
        elif choice == '2':
            count_word_occurrences(filename)
        elif choice == '3':
            remove_empty_lines(filename)
        elif choice == '4':
            display_feedback_with_keywords(filename)
        elif choice == '5':
            generate_summary_report(filename)
        elif choice == '6':
            print("Exiting Feedback Collection System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
