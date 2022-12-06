import java.util.Scanner;

class Solver {

    private static boolean stop;

    public static void solveSudoku(Board board) {

        System.out.println(board.board.size());
        Scanner scanner = new Scanner(System.in);

        stop = false;

        int i = 0;

        while(board.board.get((int)(i / 9)).get(0) != 0) {
            i++;
        }
        if(i == board.board.size() * board.board.size())  return;

        recursiveSolve(board, i, (int)(i / 9), i % 9);
    }


    private static void recursiveSolve(Board board, int n, int row, int col) {

        if(n == board.board.size() * board.board.size()) {
            stop = true;
            board.show();
        }
        else {

            boolean[] values = possibleValues(board, row, col);
            for(int i = 1; i <= board.board.size(); i++) {

                if(stop) break;

                if(values[i]) {
                    board.board.get(row).set(col, i);

                    int[] free = nextMove(board, row, col);

                    if(free[0] >= 0) {
                        recursiveSolve(board, n + 1, free[0], free[1]);
                    }

                }

            }

        }
        board.board.get(row).set(col, 0);
    }

    private static boolean[] possibleValues(Board board, int row, int col) {

//        TODO
        return new boolean[0];

    }

    private static int[] nextMove(Board board, int row, int col) {

        do {
            row = row + (int)((col + 1) / 9);
            col = (col + 1) % 9;
        }
        while(row < 9);

        return row == 9 ? new int[]{-1, -1} : new int[]{row, col};
    }
}
