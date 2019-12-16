
#loading data  
PCA10 <- read_excel("~\project 3-1\Data_PCA.xlsx")
library(readxl)
Data_PCA <- read_excel("D:/project 3-1/Data_PCA.xlsx",
col_types = c("skip", "numeric", "numeric",
"numeric", "numeric", "numeric",
"numeric", "numeric", "numeric",
"text"))
View(Data_PCA)

#PCA

pc10 <- prcomp(Data_PCA[,-9],
center = TRUE,
scale = TRUE)

print(pc10)
summary(pc10)
pc10$scale
attributes(pc10)
plot(pc10, type = "lines")

#ggbiplot
library(ggbiplot)
g <- ggbiplot(pc,
              obs.scale = 1,
              var.scale = 1,
              groups = PCA1$`Dataset Name`,
              ellipse = TRUE,
              circle = TRUE,
              ellipse.prob = 0.68)
g <- g + scale_color_discrete(name = '')
g <- g + theme(legend.direction = 'horizontal',
               legend.position = 'top')
print(g)

#3d plot
library(BiplotGUI)
library(pca3d)
gr <- factor(Data_PCA$`Database name`)

pca3d(pc10, group=gr, show.ellipses=TRUE,
ellipse.ci=0.75, show.plane=FALSE)
snapshotPCA3d(file="ellipses.png")


