# Function to calculate grade based on score
calculate_grade <- function(score) {
  if (score >= 90) {
    return("A")
  } else if (score >= 80) {
    return("B")
  } else if (score >= 70) {
    return("C")
  } else {
    return("Fail")
  }
}

# Input: Take the score from the user
score <- as.numeric(readline(prompt = "Enter the student's score: "))

# Output: Display the grade based on the score
grade <- calculate_grade(score)
cat("The grade for the score", score, "is:", grade, "\n")
