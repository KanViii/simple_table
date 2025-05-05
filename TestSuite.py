import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    def test_0(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 100))

    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 101))

    def test_2(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]

        self.assertTrue(TestUtils.check(input, expected, 102))

    def test_3(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 103))

    def test_4(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "LOOKUP x",
            "LOOKUP y",
            "END",
        ]
        expected = ["success", "success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 104))

    def test_5(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]

        self.assertTrue(TestUtils.check(input, expected, 105))

    def test_6(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 106))

    def test_7(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 107))

    def test_8(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 108))

    def test_9(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 'ab@c'",
        ]
        expected = ["Invalid: ASSIGN y 'ab@c'"]
        self.assertTrue(TestUtils.check(input, expected, 109))

    def test_10(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGNS x",
        ]
        expected = ["Invalid: ASSIGNS x"]
        self.assertTrue(TestUtils.check(input, expected, 110))

    
    def test_11(self):
        input = [
            "INSERT y string",
            "ASSIGN y 'ABC'",
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 111))

    def test_12(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
        ]
        expected = ["UnclosedBlock: 10"]
        self.assertTrue(TestUtils.check(input, expected, 112))

    def test_13(self):
        input = [
            "INSERT x number", 
            "BEGIN",
            "INSERT x string",
            "END",
            "BEGIN", 
            "LOOKUP x",
            "END",
        ]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 113))

    def test_14(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 114))

    def test_15(self):
        input = [
            "INSERT x string",
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 5",
            "ASSIGN y '5'",
            "BEGIN",
            "INSERT z number",
            "INSERT abc string",
            "INSERT cba number",
            "PRINT",
            "RPRINT",
            "END",
            "RPRINT",
            "LOOKUP x",
            "LOOKUP y",
            "END",
            "PRINT"
        ]
        expected = [
            "success", "success", "success", "success", "success", "success", "success", "success",
            "x//1 y//1 z//2 abc//2 cba//2",
            "cba//2 abc//2 z//2 y//1 x//1",
            "y//1 x//1", 
            "1", "1",
            "x//0"
        ]
        self.assertTrue(TestUtils.check(input, expected, 115))
        
    def test_16(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 5",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 116))

    def test_17(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 5",
            "END",
        ]
        expected = ["success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 117))

    def test_18(self):
        input = [
            "ASSIGN x 5",
            "INSERT x number",
        ]
        expected = ["Undeclared: ASSIGN x 5"]
        self.assertTrue(TestUtils.check(input, expected, 118))

    def test_19(self):
        input = [
            "INSERT khanh string",
            "INSERT vy string",
            "ASSIGN khanh vy",
            "ASSIGN vy khanh",
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 119))

    def test_20(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string",
            "END",
            "INSERT x string",
        ]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 120))

    def test_21(self):
        input = [
            "LOOKUP x",
        ]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 121))



    def test_22(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "END",
        ]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 122))

    def test_23(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
            "LOOKUP y",
        ]
        expected = ["Undeclared: LOOKUP y"]
        self.assertTrue(TestUtils.check(input, expected, 123))

    def test_24(self):
        input = [
            "INSERT a number",
            "ASSIGN a 132",
            "BEGIN",
            "INSERT a string",
            "INSERT c number",
            "INSERT d string",
            "LOOKUP a",
            "LOOKUP c",
            "LOOKUP d",
            "END",
            "LOOKUP a",
            "LOOKUP d",
        ]
        expected = ["Undeclared: LOOKUP d"]
        self.assertTrue(TestUtils.check(input, expected, 124))

    def test_25(self):
        input = [
            "INSERT a number",
            "ASSIGN a 132",
            "BEGIN",
            "INSERT a string",
            "INSERT c number",
            "INSERT d string",
            "LOOKUP a",
            "LOOKUP c",
            "LOOKUP d",
            "END",
            "LOOKUP a",
        ]
        expected = ["success", "success", "success", "success", "success", "1", "1", "1", "0"]
        self.assertTrue(TestUtils.check(input, expected, 125))

    def test_26(self):
        input = [
            "INSERT a1 number",
            "INSERT a2 string",
            "ASSIGN a1 a2"
        ]
        expected = ["TypeMismatch: ASSIGN a1 a2"]
        self.assertTrue(TestUtils.check(input, expected, 126))

    def test_27(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1 'Hello'",
            "ASSIGN a1 'World'"
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 127))
    
    def test_28(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "ASSIGN b a",
        ]
        expected = ["TypeMismatch: ASSIGN b a"]
        self.assertTrue(TestUtils.check(input, expected, 128))

    def test_29(self):
        input = [
        ]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 129))
    
    def test_30(self):
        input = [
            "INSERT x string",
            "BEGIN",
            "INSERT x number",
            "END",
            "ASSIGN x 'huhuhu'"
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 130))

    def test_31(self):
        input = [
            "INSERT x string",
            "BEGIN",
            "INSERT x number",
            "ASSIGN x 2005",
            "END",
            "ASSIGN x 'huhuhu'"
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 131))

    def test_32(self):
        input = [
            "INSERT x string",
            "ASSIGN x 'a@b'"
        ]
        expected = ["Invalid: ASSIGN x 'a@b'"]
        self.assertTrue(TestUtils.check(input, expected, 132))

    def test_33(self):
        input = [
            "INSERT a number",
            "ASSIGN a 12a"
        ]
        expected = ["Invalid: ASSIGN a 12a"]
        self.assertTrue(TestUtils.check(input, expected, 133))

    def test_34(self):
        input = [
            "INSERT a number",
            "ASSIGN a 6.9"
        ]
        expected = ["Invalid: ASSIGN a 6.9"]
        self.assertTrue(TestUtils.check(input, expected, 134))

    def test_35(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "END",
            "BEGIN",
            "LOOKUP x",
            "END"
        ]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 135))

    def test_36(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "BEGIN",
            "END",
            "END",
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 136))

    def test_37(self):
        input = [
            "INSERT x number",
            "ASSIGN x 'abc'"
        ]
        expected = ["TypeMismatch: ASSIGN x 'abc'"]
        self.assertTrue(TestUtils.check(input, expected, 137))

    def test_38(self):
        input = [
            "INSERT x string",
            "ASSIGN x 123"
        ]
        expected = ["TypeMismatch: ASSIGN x 123"]
        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "INSERT x string",
            "ASSIGN x '696969'"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_40(self):
        input = [
            "INSERT x number",
            "ASSIGN x x"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 140))


    def test_42(self):
        input = [
            "INSERT a number",
            "INSERT b number",
            "ASSIGN a b",
            "BEGIN",
            "INSERT b string",
            "ASSIGN a b",
        ]
        expected = ["TypeMismatch: ASSIGN a b"]
        self.assertTrue(TestUtils.check(input, expected, 142))
 
    def test_43(self):
        input = [
            "INSERT a number",
            "ASSIGN a 'khanhvyhuhu'"
        ]
        expected = ["TypeMismatch: ASSIGN a 'khanhvyhuhu'"]
        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "INSERT a string",
            "ASSIGN a 'khanhvyhihi'"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 144))

    def test_45(self):
        input = [
            "INSERT a number",
            "ASSIGN a 2353353"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_45(self):
        input = [
            "INSERT a number",
            "ASSIGN a -100"
        ]
        expected = ["Invalid: ASSIGN a -100"]
        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_46(self):
        input = [
            "INSERT a string",
            "INSERT b string",
            "ASSIGN a b"
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 146))

    def test_47(self):
        input = [
            "BEGIN",
            "INSERT a number",
            "END",
            "ASSIGN a 1"
        ]
        expected = ["Undeclared: ASSIGN a 1"]
        self.assertTrue(TestUtils.check(input, expected, 147))

    def test_48(self):
        input = [
            "INSERT a string",
            "ASSIGN a ''"
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_49(self):
        input = [
            "INSERT a string",
            "ASSIGN a"
        ]
        expected = ["Invalid: ASSIGN a"]
        self.assertTrue(TestUtils.check(input, expected, 149))

    def test_50(self):
        input = [
            "BEGIN",
            "INSERT x string",
            "ASSIGN x 'abc'",
            "LOOKUP x",
            "END"
        ]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 150))

    def test_51(self):
        input = [
            "INSERT x   string"
        ]
        expected = ["Invalid: INSERT x   string"]
        self.assertTrue(TestUtils.check(input, expected, 151))

    

