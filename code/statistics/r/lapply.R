mylist<-list(A=matrix(1:9,nrow=3),B=1:5,C=8)

#suma de cada elemento

lapply(mylist,sum)

unlist(lapply(mylist,sum))

lapply(mylist,function(x) x*20)

