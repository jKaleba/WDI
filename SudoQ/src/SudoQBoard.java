import java.io.File;
import java.util.Random;
import java.util.Scanner;

class SudoQBoard extends Board {

    public SudoQBoard(int size) {

        super(size);

        try {
            String pathname = "boards" + String.valueOf(size) + ".txt";
            Scanner scanner = new Scanner(new File(pathname));
            downloadBoard(scanner);

        }
        catch(Exception e) {
            e.printStackTrace();
        }
    }

    private void downloadBoard(Scanner scanner) {

        int differentBoards = scanner.nextInt();

        int currBoard = new Random().nextInt(0, differentBoards);

        for(int i = 0; i < currBoard; i++) {
            for(int j = 0; j < super.size * super.size; j++) {
                scanner.nextInt();
            }
        }

        for(int i = 0; i < this.size; i++) {
            for(int j = 0; j < this.size; j++) {
                board.get(i).add(scanner.nextInt());
            }
        }

        Random random = new Random();
        int emptyAmount = random.nextInt(40, 55);

        for(int i = 0; i < emptyAmount; i++) {

            int empty = random.nextInt(0, size * size);
            board.get(empty / 9).set(empty % 9, 0);
        }
    }
}