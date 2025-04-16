library(ggplot2)

session_times <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/web_page_data.csv')
head(session_times)
session_times[,2] <- session_times[,2] * 100

mean_a <- mean(session_times[session_times['Page'] == 'Page A', 'Time'])
mean_b <- mean(session_times[session_times['Page'] == 'Page B', 'Time'])
mean_b - mean_a

