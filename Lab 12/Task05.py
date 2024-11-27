library(tm)
library(e1071)

d <- read.csv("emails.csv")
t <- Corpus(VectorSource(d$email))

t <- tm_map(t, content_transformer(tolower))
t <- tm_map(t, removePunctuation)
t <- tm_map(t, removeNumbers)
t <- tm_map(t, removeWords, stopwords("en"))
t <- tm_map(t, stripWhitespace)

v <- DocumentTermMatrix(t)
m <- as.matrix(v)
x <- m
y <- d$label

n <- naiveBayes(x, as.factor(y))

p <- predict(n, x)

acc <- sum(p == y) / length(y)
cat("Accuracy:", acc, "\n")
