library(MASS)
library(ISLR)

# predict house price in Boston
fix(Boston)
names(Boston)
lm <- lm(medv ~ lstat, data=Boston)
attach(Boston)
summary(lm)
names(lm)  #lm$coefficients[1]
res <- lm$residuals
confint(lm, level = 0.95) # obtain a CI for coefficients
predict(lm, data.frame(lstat=(c(6, 8, 17))), interval="confidence")
predict(lm, data.frame(lstat=(c(6, 8, 17))), interval="prediction")
# plot
plot(lstat, medv)
abline(lm, lwd = 3, col="red")

par(mfrow=c(2,2))
plot(lm)
plot(predict(lm), residuals(lm))
plot(predict(lm), rstudent(lm))
plot(hatvalues(lm))
which.max(hatvalues(lm))

