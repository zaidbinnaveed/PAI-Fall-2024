t <- as.numeric(readline(prompt = "Enter the annual income: "))

if (t < 30000) {
  tax <- 0
} else if (t >= 30000 && t < 70000) {
  tax <- t * 0.10
} else if (t >= 70000 && t < 100000) {
  tax <- t * 0.15
} else {
  tax <- t * 0.20
}

cat("The tax is: $", tax, "\n")
