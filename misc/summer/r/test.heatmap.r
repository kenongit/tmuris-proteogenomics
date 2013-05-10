exp <- read.csv("transcriptome.alignmentFrequencies.csv", sep=",")

exp_matrix <- data.matrix(exp)

exp_heatmap <- heatmap(exp_matrix, Rowv=NA, Colv=NA, col = cm.colors(256), scale="column", margins=c(5,10))

# http://flowingdata.com/2010/01/21/how-to-make-a-heatmap-a-quick-and-easy-solution/