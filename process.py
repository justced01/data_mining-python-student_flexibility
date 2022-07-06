class formData:
    # Class attributes 
    a1 = None
    a2 = None
    a3 = None
    a4 = None
    a5 = None
    a6 = None
    a7 = None
    a8 = None
    a9 = None
    a10 = None

    def process(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
        a1 = q1
        a2 = q2
        a3 = q3
        a4 = q4
        a5 = q5
        a6 = q6
        a7 = q7
        a8 = q8
        a9 = q9     
        a10 = q10

    def show(self):
        return "A1: {self.a1}, A2: {self.a2}, A3: {self.a3}, A4: {self.a4}, A5: {self.a5}, A6: {self.a6}, A7: {self.a7}, A8: {self.a8}, A9: {self.a9}, A10: {self.a10}."

    def submit():
        print("Clicked")