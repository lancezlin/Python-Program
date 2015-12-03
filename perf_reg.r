observed <- c(0.22, 0.83, -0.12, 0.89, -0.23, -1.30, -0.15, -1.4,
                0.62, 0.99, -0.18, 0.32, 0.34, -0.30, 0.04, -0.87,
                0.55, -1.30, -1.15, 0.20)
predicted <- c(0.24, 0.78, -0.66, 0.53, 0.70, -0.75, -0.41, -0.43, 
                 0.49, 0.79, -1.19, 0.06, 0.75, -0.07, 0.43, -0.42,
                 -0.25, -0.64, -1.26, -0.07)

residualValues <- observed - predicted
# summary(residualValues)
# observed values vs pred values
axisRange <- extendrange(c(observed, predicted))
plot(observed, predicted, ylim = axisRange, xlim = axisRange)
abline(0, 1, col="darkgrey", lty=2)
# residual vs predicted
plot(predicted, observed, ylab = "residual")
abline(h = 0, col="darkgrey", lty=2)
# Calculate R square and RMSE with caret package
library("caret")
R2(predicted, observed)
RMSE(predicted, observed)
# correlation
cor(predicted, observed)
cor(predicted, observed, method = "spearman")
library(lubridate)
library(reshape2)


body <- read.table("http://www.amstat.org/publications/jse/datasets/body.dat.txt")
boxplot(body)
keep.par <- par() # stored the original settings >par(keep.par)
par(mar=c(5, 4, 4, 2))
boxplot(body, las=3)
x <- 1:10
set.seed(23)
y <- x + rnorm(10)
plot(x, y)
plot(x, y, col=x)
plot(x, y, col=x, cex=x)
breaks <- seq(min(body$V22), max(body$V22), 5)
v22_group <- cut((body$V22), breaks)
body$group <- v22_group
plot(body$V11, body$V20, pch=body$V25, col=body$group)
