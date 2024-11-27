# Function to check if a year is a leap year
is_leap_year <- function(year) {
  # Check if the year is divisible by 4
  if (year %% 4 == 0) {
    # If divisible by 100, it must also be divisible by 400 to be a leap year
    if (year %% 100 == 0) {
      if (year %% 400 == 0) {
        return(TRUE)  # Divisible by 400, so it's a leap year
      } else {
        return(FALSE)  # Divisible by 100 but not by 400, not a leap year
      }
    } else {
      return(TRUE)  # Divisible by 4 but not by 100, it's a leap year
    }
  } else {
    return(FALSE)  # Not divisible by 4, so it's not a leap year
  }
}

# Example: Check if a year is a leap year
year <- as.integer(readline(prompt = "Enter a year: "))

# Check and print the result
if (is_leap_year(year)) {
  cat(year, "is a leap year.\n")
} else {
  cat(year, "is not a leap year.\n")
}
