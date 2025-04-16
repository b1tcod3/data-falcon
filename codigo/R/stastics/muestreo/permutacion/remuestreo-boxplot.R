library(ggplot2)

session_times <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/web_page_data.csv')
head(session_times)
session_times[,2] <- session_times[,2] * 100

graph <- ggplot(session_times, aes(x=Page, y=Time)) + 
  geom_boxplot() +
  labs(y='Time (in seconds)') + 
  theme_bw()
graph
