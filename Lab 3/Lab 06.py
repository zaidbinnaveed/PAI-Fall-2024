def write_question_to_file():
    try:
        sentence = input("Enter your sentence : ")
        if sentence.strip().endswith('?'):
            with open('questions.txt', 'a') as file:
                file.write(f"Question: {sentence}\n")
                print("Question added to file")
        else:
            print("Sentence is not a question. Please enter a question.")
    
    except:
        print("Error: Unable to open file. Please try again later.")


write_question_to_file()
