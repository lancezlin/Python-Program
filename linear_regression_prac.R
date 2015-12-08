library(MASS)
library(ISLR)

# predict house price in Boston
fix(Boston)
names(Boston)
lm <- lm(medv ~ lstat, data=Boston)
attach(Boston)
summary(lm)
names(lm)
#lm$coefficients[1]
res <- lm$residuals
