class EmptySudoQBoard extends Board {

    public EmptySudoQBoard(int size) {

        super(size);

        for(int i = 0; i < size; i++) {

            for(int j = 0; j < size; j++) {
                board.get(i).add(0);
            }
        }
    }
}
