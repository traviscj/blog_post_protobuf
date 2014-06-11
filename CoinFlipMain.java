import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;

import static traviscj.SetOfCoinflips.CoinFlip;
import static traviscj.SetOfCoinflips.SetOfCoinFlipsPacked;

// before running, do:
//     $ wget http://mirrors.ibiblio.org/maven2/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar
//     $ brew install protobuf
//     $ protoc set_of_coinflips.proto --python_out=. --java_out=.
//     $ pip install protobuf
//     $ python use_set_of_coinflips.py packed_obj
// compile with:
//     $ javac -cp ~/protobufs_blog_post/protobuf-java-2.5.0.jar:. CoinFlipMain.java
// run with:
//     $ java -cp ~/protobufs_blog_post/protobuf-java-2.5.0.jar:. CoinFlipMain

// or just:
//     $ brew install redo
//     $ redo run
// and check in the file named 'run'

public class CoinFlipMain {
  public static void main(String[] args) throws IOException {
    // basic construction:
    CoinFlip cf = CoinFlip.newBuilder()
        .setHeads(true)
        .build();

    // basic reading (of !packed! object):
    InputStream inputStream = new FileInputStream(new File("packed_obj"));
    SetOfCoinFlipsPacked setOfCoinFlipsPacked = SetOfCoinFlipsPacked.parseFrom(inputStream);

    // loop over those coin flips:
    int i=0;
    for (Boolean currentCoinFlip : setOfCoinFlipsPacked.getCoinflipsList()) {
      System.out.println("cf[i=" + i++ + "]: " + currentCoinFlip);
    }
  }
}
