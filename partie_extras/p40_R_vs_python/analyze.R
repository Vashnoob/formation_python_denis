# Appel du script Python
system("python3 preprocess.py")

# Analyse des données nettoyées
data <- read.csv("data_clean.csv")
summary(data)

plot(data$x, data$y_norm, type="b", col="darkgreen", pch=16,
     main="Analyse R après traitement Python",
     xlab="x", ylab="y normalisé")
