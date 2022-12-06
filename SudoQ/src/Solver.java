import java.util.ArrayList;
import java.util.Arrays;

class Solver {

    private static boolean stop;

    public static void solveSudoku(Board board) {

        stop = false;

        int i = 0;

        while(board.board.get((i / 9)).get(i % 9) != 0) {
            i++;
        }

        if(i == board.board.size() * board.board.size())  return;

        int n = 0;
        for(ArrayList<Integer> row : board.board) {

            for(int element : row) {
                if(element != 0) {
                    n++;
                }
            }
        }

        if(n != 81) {
            recursiveSolve(board, n, (i / 9), i % 9);
        }
    }

    private static void recursiveSolve(Board board, int n, int row, int col) {

        if(n == 81) {
            stop = true;
            board.show();
            return;
        }

        else {
            boolean[] values = possibleValues(board, row, col);
            for(int i = 1; i < values.length; i++) {

                if(stop) break;

                if(values[i]) {
                    board.board.get(row).set(col, i);

                    int[] free = nextMove(board, row, col);

                    recursiveSolve(board, n + 1, free[0], free[1]);
                }
            }
        }
        board.board.get(row).set(col, 0);
    }

    private static boolean[] possibleValues(Board board, int row, int col) {

        boolean[] defaults = new boolean[board.board.size() + 1];
        Arrays.fill(defaults, true);

        try{
            for(int i = 0; i < board.board.size(); i++) {
                defaults[board.board.get(row).get(i)] = false;
                defaults[board.board.get(i).get(col)] = false;
            }
        }
        catch(Exception e) {
            e.printStackTrace();
        }

        int startRow = row / 3 * 3;
        int startCol = col / 3 * 3;

        for(int i = startRow; i < startRow + 3; i++) {
            for(int j = startCol; j < startCol + 3; j++) {
                defaults[board.board.get(i).get(j)] = false;
            }
        }

        return defaults;
    }

    private static int[] nextMove(Board board, int row, int col) {

        do {
            row = row + ((col + 1) / 9);
            col = (col + 1) % 9;
        }
        while(row < 9 && board.board.get(row).get(col) != 0);

        return row == 9 ? new int[]{-1, -1} : new int[]{row, col};
    }
}
