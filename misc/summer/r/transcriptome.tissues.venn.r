library("VennDiagram");

venn.plot <- draw.quad.venn(
area1 = 4947,
area2 = 5012,
area3 = 4971,
area4 = 4937,
n12 = 4276,
n13 = 4255,
n14 = 4142,
n23 = 4343,
n24 = 4318,
n34 = 4320,
n123 = 3931,
n124 = 3844,
n134 = 3852,
n234 = 3970,
n1234 = 3644,
fontfamily = 'sans',
fontface = 'plain',
label.fontface = 'sans',
label.fontfamily = 'plain',
category = c("Adult", "Embryo", "Female rear", "Stichosome"),
cat.fontfamily = 'plain',
fill = c("orange", "red", "green", "blue"),
lty = "solid",
cex = 2,
cat.cex = 2,
cat.col = c("orange", "red", "green", "blue")
);