class InvalidSeqError(Exception):
    def __init__(self, error):
        self.message=error.args[0]
        self.tip="Please enter the correct Seq Notation."
        super().__init__(self.message)