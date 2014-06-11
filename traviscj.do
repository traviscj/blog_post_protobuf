redo-ifchange protobuf-java-2.5.0.jar
PROTOC=/usr/local/Cellar/protobuf/2.5.0/bin/protoc
TMPDIR=`mktemp -d -t $2`

$PROTOC set_of_coinflips.proto --java_out=$TMPDIR
javac -d $TMPDIR -cp protobuf-java-2.5.0.jar:. $TMPDIR/$2/SetOfCoinflips.java
mv $TMPDIR/$2 $3
rmdir $TMPDIR
