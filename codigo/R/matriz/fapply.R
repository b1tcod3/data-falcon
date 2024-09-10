mymatrix<-matrix(1:9,nrow=3)
mymatrix

#suma de las filas
apply(mymatrix,1,sum) 

#suma de las columnas
apply(mymatrix,2,sum) 