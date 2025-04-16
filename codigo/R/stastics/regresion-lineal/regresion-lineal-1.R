

house <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/house_sales.csv')
# head(lung)
# plot(lung$Exposure, lung$PEFR, xlab="Exposure", ylab="PEFR")

model <- lm(PEFR ~ Exposure, data=lung)
model

