# FalconRecharged2021_trajectories

Trajectory makers
[Infinity at Home challeneges 2021](https://firstfrc.blob.core.windows.net/frc2021/Manual/AtHomeManualSections/2021AtHomeChallengesManualSection02.pdf)


folders description:

* Pathveawer - experiments with [pathweaver tool](https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/pathweaver/index.html)
* python - python based model ( python 3.x, matplotlib, pandas and scipy pip modules ) 
* gnuplot - [gnuplot](http://www.gnuplot.info/) model
 

for gnuplot:

You'll need:

* gnuplot [http://www.gnuplot.info/]

Trajectory is described in csv file, similar to ``` public static double[][] ```  sections in TrajectoryHelper.java \
To generate image from the plot run ```gnuplot barrel.plot```  ( as example ) \
Resulted svg (or png) image will be located in the same folder

To prepare csv for copy/paste to jave code ```awk '{print "{"$1"},"}' barrel.csv``` can be used

hi
