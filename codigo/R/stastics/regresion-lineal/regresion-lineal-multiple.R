# Cargar los datos
house <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/house_sales.csv',sep='\t')

# Inspeccionar las primeras filas de las columnas relevantes
head(house[, c('AdjSalePrice', 'SqFtTotLiving', 'SqFtLot', 'Bathrooms', 
               'Bedrooms', 'BldgGrade')])

# Ajustar el modelo de regresión lineal múltiple
house_lm <- lm(
  AdjSalePrice ~ SqFtTotLiving + SqFtLot + Bathrooms + Bedrooms + BldgGrade,  
  data = house,
  na.action = na.omit
)

# Mostrar el resumen del modelo
summary(house_lm)
