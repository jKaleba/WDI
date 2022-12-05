import java.util.ArrayList;

class EmptySudoQBoard extends SudoQBoard {

    public EmptySudoQBoard(int size) {

        super(size);

        System.out.println(size);
        for(int i = 0; i < size; i++) {

            ArrayList<Integer> row = new ArrayList<>(size);
            for(int j = 0; j < size; j++) {
                row.add(0);
            }
            board.add(row);
        }
    }


}
