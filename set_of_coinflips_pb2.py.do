TMPDIR=`mktemp -d -t $2`
protoc set_of_coinflips.proto --python_out=$TMPDIR
mv $TMPDIR/$2 $3
rmdir $TMPDIR
