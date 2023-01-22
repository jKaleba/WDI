class Main {

    public static void main(String[] args) {
        Board emptySudoQBoard = new EmptySudoQBoard(9);
        Board sudoQBoard = new SudoQBoard(9);

        emptySudoQBoard.show();
        Solver.solveSudoku(emptySudoQBoard);

        sudoQBoard.show();
        Solver.solveSudoku(sudoQBoard);



//        TODO solved sudoku board saving in file for other games

    }
}
