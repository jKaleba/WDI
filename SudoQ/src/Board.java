import java.util.ArrayList;

class Board {

    ArrayList<ArrayList<Integer>> board;

    public Board(int size) {

        board = new ArrayList<ArrayList<Integer>>(size);
    }

    public void show() {

        for(int i = 0; i < 9; i++) {
            System.out.print("| ");
            for(int j = 0; j < 9; j++) {

                System.out.print(board.get(i).get(j) + " ");
                if ((j + 1) % 3 == 0) {
                    System.out.print(" | ");
                }
            }

            System.out.println();
            if((i + 1) % 3 == 0) {
                System.out.println("\n");
            }

        }


    }


}
