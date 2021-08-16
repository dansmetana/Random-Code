install.packages("DAAG")

library(DAAG)

#4 Models
#Linear: Y = B0 + B1x + e
#Quadratic: Y = B0 + B1x + B2x^2 + e
#Exponential: log(Y) = log(B0) + B1x + e
#Log-Log: log(Y) = B0 + log(B1x) + e

#creating independent x/y values

X <- c(.9575155, 1.0576610, .9817954, 1.0766035, 1.0880935,
       .9091113, 1.0056211, 1.0784838, 1.0102870, .9913229,
       1.0913667, .9906668, 1.0355141, 1.0145267, .9205849)

Y <- c(-.6038890, -.1741176, 1.5403360, .1443196, .2317148,
       1.6197772, .4665216, -1.1895051, -.6766184, -.4543769,
       1.3115125, .3504368, .4356695, .1251049, -.6385871)

plot(X, Y, main = "Test Data")

a <- seq(-80,80,.1)

#Linear
L1 <- lm(Y~X)
plot(X, Y, main = "Linear", pch = 16)
yhat1 <- L1$coef[1] + L1$coef[2]*a
lines(a, yhat1, lwd = 2)

#Quadratic
L2 <- lm(Y ~ X + I(X^2))
plot(X, Y, main = "Quadratic", pch = 16)
yhat2 <- L2$coef[1] + L2$coef[2]*a + L2$coef[3]*a^2
lines(a, yhat2, lwd = 2)

#Exponential
L3 <- lm(log(Y)~X)
plot(X, Y, main = "Exponential", pch = 16)
logyhat3 <- L3$coef[1] + L3$coef[2]*a
yhat3 <- exp(logyhat3)
lines(a, yhat3, lwd = 2)

#Log-Log
L4 <- lm(log(Y)~ log(X))
plot(log(X), log(Y), main = "Log-Log", pch = 16)
logyhat4 <- L4$coef[1] + L4$coef[2]*log(a)
lines(log(a), logyhat4, lwd = 2)

#N-Fold Cross Validation
#For k = 1,2,3,...,n, let observation (x(k), y(k)) be the test point
#Fit the models using only n-1 observations in the training set
#Compute the predicted response yhat(k) = B0hat + B1hatx(k) for the test point
#Compute the predicted error e(k) = y(k) - yhat(k)
#Estimate the mean of the sqaure prediction errors

n <- length(X)
n

e1 <- e2 <- e3 <- e4 <- numeric(n) #locations to store calculations

#fit models on one left out samples

for(k in 1:n){
  y <- Y[-k]
  x <- X[-k]
  J1 <- lm(y~x)
  yhat1 <- J1$coef[1] + J1$coef[2]*X[k]
  e1[k] <- Y[k] - yhat1
  
  J2 <- lm(y~x + I(x^2))
  yhat2 <- J2$coef[1] + J2$coef[2]*X[k] + J2$coef[3]*X[k]^2
  e2[k] <- Y[k] - yhat2
  
  J3 <- lm(log(y)~x)
  logyhat3 <- J3$coef[1] + J3$coef[2]*X[k]
  yhat3 <- exp(logyhat3)
  e3[k] <- Y[k] - yhat3
  
  J4 <- lm(log(y)~log(x))
  logyhat4 <- J4$coef[1] + J4$coef[2]*log(X[k])
  yhat4 <- exp(logyhat4)
  e4[k] <- Y[k] - yhat4
}

c(mean(e1^2), mean(e2^2), mean(e3^2), mean(e4^2))

#Bayesian Information Criteria
BIC(L1)
BIC(L2)
BIC(L3)
BIC(L4)

#Akaike's Information Criteria
AIC(L1)
AIC(L2)
AIC(L3)
AIC(L4)


L1
L2
L3
L4


#Linear
plot(L1$fit, L1$res) #fitted vs residuals value
abline(0,0)
qqnorm(L1$res) #Normal probability plot
qqline(L1$res) #Reference Line

##############################################################

#Quadratic
plot(L2$fit, L2$res) 
abline(0,0)
qqnorm(L2$res) 
qqline(L2$res)

##############################################################

#Exponential
plot(L3$fit, L3$res) 
abline(0,0)
qqnorm(L3$res) 
qqline(L3$res)

##############################################################

#Log-Log
plot(L4$fit, L4$res) 
abline(0,0)
qqnorm(L4$res) 
qqline(L4$res)

##############################################################

#Model Summaries
summary(L1)
summary(L2)
summary(L3)
summary(L4)


#Big F statistic and small p-value is the goal
