import java.util.ArrayList;

class Board {

    ArrayList<ArrayList<Integer>> board;

    public Board(int size) {

        board = new ArrayList<ArrayList<Integer>>(size);
    }

    public void show() {

        for(int i = 0; i < 3 * board.size(); i++) {
            System.out.print("-");
        }
        System.out.println();

        for(int i = 0; i < board.size(); i++) {
            System.out.print(" | ");
            for(int j = 0; j < board.size(); j++) {

                System.out.print(board.get(i).get(j) + " ");
                if ((j + 1) % 3 == 0) {
                    System.out.print("| ");
                }
            }

            System.out.println();
            if((i + 1) % 3 == 0) {
                for(int l = 0; l < 3 * board.size(); l++) {
                    System.out.print("-");
                }
                System.out.println();
            }
        }
    }
}
