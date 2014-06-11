redo-ifchange protobuf-java-2.5.0.jar
redo-ifchange traviscj

TMPDIR=`mktemp -d -t $2`
javac -d $TMPDIR -cp protobuf-java-2.5.0.jar:$TMPDIR:. CoinFlipMain.java
mv $TMPDIR/$2 $3
rm -rf $TMPDIR
