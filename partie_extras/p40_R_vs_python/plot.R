library(ggplot2)

# Lecture des données
data <- read.csv("data.csv")

# Tracé ggplot2
ggplot(data, aes(x = x, y = y)) +
  geom_point(color = "blue", size = 3) +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  ggtitle("Données analysées en Python, visualisées en R")
