import java.util.ArrayList;

class Board {

    protected ArrayList<ArrayList<Integer>> board;
    int size;
 
    public Board(int size) {

        board = new ArrayList<ArrayList<Integer>>(size);
        this.size = size;

        for(int i = 0; i < size; i++) {

            ArrayList<Integer> row = new ArrayList<>();
            board.add(row);
        }
    }

    public ArrayList<ArrayList<Integer>> getBoard() {
        return this.board;
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
