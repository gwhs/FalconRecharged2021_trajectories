#
set terminal png size 1024
set output "slalom.png"
set size ratio -1

set datafile separator ","
set xrange [0:360]
set yrange [-180:0]
set xtics 30
set ytics 30
set grid back dt 3

set style line 1 \
    linecolor rgb 'blue' \
    linetype 1 linewidth 1 \
    pointtype 2 pointsize 1.5

set style line 2 lc rgb 'red' pointtype 9 pointsize 2  

plot 'slalom.csv' using 1:($2*-1):($0+1) with labels notitle , \
     '' using 1:($2*-1) with lines linestyle 1 notitle, \
     'slalom_markers.csv' using 1:2 with points linestyle 2 notitle

