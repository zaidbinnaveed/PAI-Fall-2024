# Function to calculate the sum of even numbers in a list
sum_of_even_numbers <- function(numbers) {
  # Filter out even numbers and calculate the sum
  even_numbers <- numbers[numbers %% 2 == 0]
  return(sum(even_numbers))
}

# Example list of numbers
numbers_list <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Calculate the sum of even numbers
sum_even <- sum_of_even_numbers(numbers_list)

# Print the result
cat("The sum of even numbers is:", sum_even, "\n")
