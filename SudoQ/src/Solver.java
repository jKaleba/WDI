class Solver {

    private static boolean stop;

    public static void solveSudoku(Board board) {

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

//            TODO

        }
    }


    private static int[] nextMove(Board board, int row, int col) {

        do {
            row = row + (int)((col + 1) / 9);
            col = (col + 1) % 9;
        }
        while(row < 9);

        return row == 9 ? new int[]{0, 0} : new int[]{row, col};
    }
}
