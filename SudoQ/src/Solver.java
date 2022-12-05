import java.util.ArrayList;
import java.util.Arrays;

class Solver {


    private static boolean stop;


    public static void solveSudoku(Board board) {

        stop = false;

        int i = 0;

        while(board.board.get((int)(i / 9)).get(0) != 0) {
            i++;
        }

        recursiveSolve(board, i, 0, 0);

    }


    private static void recursiveSolve(Board board, int n, int row, int col) {

        if(n == board.board.size() * board.board.size()) {
            stop = true;
            board.show();
        }
        else {



        }



    }


    private static void possibleMoves(Board board) {

        ArrayList<Integer> dx = new ArrayList<>(
                Arrays.asList(-1, -1, 1, 1, 1)
        );
        ArrayList<Integer> dy = new ArrayList<>(Arrays.asList(
                1, 1, 1, 1, 1)
        );


    }




}
