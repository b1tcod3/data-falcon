x<-c(A=20,B=1,C=40)
y<-c(J=430,K=50,L=10)

simply<-function(u,v){
  (u+v)*2
}
mapply(simply,x,y)