

lung <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/LungDisease.csv')
# head(lung)
# plot(lung$Exposure, lung$PEFR, xlab="Exposure", ylab="PEFR")

model <- lm(PEFR ~ Exposure, data=lung)
model

plot(lung$Exposure, lung$PEFR, xlab="Exposure", ylab="PEFR", ylim=c(300,450), type="n", xaxs="i")
abline(a=model$coefficients[1], b=model$coefficients[2], col="blue", lwd=2)
text(x=.3, y=model$coefficients[1], labels=expression("b"[0]),  adj=0, cex=1.5)
x <- c(7.5, 17.5)
y <- predict(model, newdata=data.frame(Exposure=x))
segments(x[1], y[2], x[2], y[2] , col="red", lwd=2, lty=2)
segments(x[1], y[1], x[1], y[2] , col="red", lwd=2, lty=2)
text(x[1], mean(y), labels=expression(Delta~Y), pos=2, cex=1.5)
text(mean(x), y[2], labels=expression(Delta~X), pos=1, cex=1.5)
text(mean(x), 400, labels=expression(b[1] == frac(Delta ~ Y, Delta ~ X)), cex=1.5)

### Fitted Values and Residuals

fitted <- predict(model)
resid <- residuals(model)

fitted
resid
