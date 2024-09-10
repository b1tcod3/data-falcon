par(mfrow = c(1, 2))

# Rejilla de valores para el eje X
x <- seq(-4, 8, 0.1)

#-----------------------------------------
# Misma desviación típica, distinta media
#-----------------------------------------
# Media 0, desviación típica 1
plot(x, dnorm(x, mean = 0, sd = 1), type = "l",
     ylim = c(0, 0.6), ylab = "", lwd = 2, col = "red")
# Media 3, desviación típica 1
lines(x, dnorm(x, mean = 3, sd = 1), col = "blue", lty = 1, lwd = 2)

# Añadimos una leyenda
legend("topright", c(expression(paste(, mu, " ", sigma)), "0 1", "3 1"),
       lty = c(0, 1, 1), col = c("blue", "red"), box.lty = 0, lwd = 2)

#-----------------------------------------
# Misma media, distinta desviación típica
#-----------------------------------------
# Media 1, desviación típica 1
plot(x, dnorm(x, mean = 1, sd = 1), type = "l",
     ylim = c(0, 1), ylab = "", lwd = 2, col = "red")
# Media 1, desviación típica 0.5
lines(x, dnorm(x, mean = 1, sd = 0.5), col = "blue", lty = 1, lwd = 2)

# Añadimos una leyenda
legend("topright", c(expression(paste(, mu, " ", sigma)), "1 1", "1 0.5"),
       lty = c(0, 1, 1), col = c("blue", "red"), box.lty = 0, lwd = 2)

par(mfrow = c(1, 1))