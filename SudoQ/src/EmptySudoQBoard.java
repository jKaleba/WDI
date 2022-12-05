import java.util.ArrayList;

class EmptySudoQBoard extends SudoQBoard {

    public EmptySudoQBoard(int size) {

        board = new ArrayList<>(size);

        for(var row : board) {

            row = new ArrayList<Integer>(size);
            for(int i = 0; i < size; i++) {
                row.set(i, 0);
            }
        }




    }


}
