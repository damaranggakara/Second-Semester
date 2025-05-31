library(rpart)
library(randomForest)
library(caret)
install.packages("rpart.plot") # Menginstal paket rpart.plot
library(rpart.plot) # Memuat paket rpart.plot

# Membaca data dari file CSV
df <- read.csv("C:/Users/muham/OneDrive/Documents/one drive/OneDrive/Documents/KULIAH/SEMESTER 2/TVD/Kuis 2/StudentsPerformance.csv")
# Menambahkan label untuk math score
df$tinggi <- ifelse(df$`math.score` > 50, 1, 0)

# Memisahkan fitur dan label
x <- df[, !names(df) %in% c("tinggi", "math.score")]
x <- model.matrix(~ . - 1, data = x)
y <- df$tinggi

# Membagi data menjadi data latih dan data uji
set.seed(10)
train_index <- createDataPartition(y, p = 0.2, list = FALSE)
x_train <- x[train_index, ]
y_train <- y[train_index]
x_test <- x[-train_index, ]
y_test <- y[-train_index]

# Membangun Decision Tree
dcsn <- rpart(tinggi ~ ., data = data.frame(x_train, tinggi = y_train), method = "class")
prp(dcsn, main = "Decision Tree", box.palette = "auto", tweak = 1.2)

# Membangun Random Forest
forest <- randomForest(tinggi ~ ., data = data.frame(x_train, tinggi = y_train), ntree = 100)
plot(forest, main = "Random Forest")
#NO 2
# Memuat library yang dibutuhkan
library(ggplot2)
library(dplyr)

# Membaca data dari file CSV
data <- read.csv("C:/Users/muham/OneDrive/Documents/one drive/OneDrive/Documents/KULIAH/SEMESTER 2/TVD/Kuis 2/StudentsPerformance.csv")

# Memilih kolom yang dibutuhkan
X <- data[, c('reading.score', 'writing.score')]

# Melakukan clustering KMeans dengan 3 cluster
set.seed(123)  # Mengatur seed untuk reproduktibilitas
kmeans_result <- kmeans(X, centers = 3)

# Menambahkan hasil cluster ke data asli
data$cluster <- as.factor(kmeans_result$cluster)

# Membuat plot hasil clustering
ggplot(data, aes(x = reading.score, y = writing.score, color = cluster)) +
  geom_point(size = 3) +
  scale_color_manual(values = c('red', 'blue', 'grey')) +
  labs(title = 'KMeans Clustering of Students', x = 'Reading Score', y = 'Writing Score') +
  theme_minimal()

