import unittest
from TestUtils import TestUtils

class TestSymbolTable(unittest.TestCase):
    # Testing Insertion
    def test_0(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 100))

    # Testing Insertion with redeclaration
    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 101))


    # Testing Assignment with type mismatch
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

    # Testing nested blocks
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

    # Testing Lookup
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

    # Testing Print and RPrint
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

    # Testing Assign undeclared variable
    def test_7(self):
        input = [
            "INSERT x number",
            "ASSIGN y 5",
        ]
        expected = ["Undeclared: ASSIGN y 5"]

        self.assertTrue(TestUtils.check(input, expected, 107))

    # Testing Assign with type mismatch in nested blocks
    def test_8(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string",
            "ASSIGN x 'hello'",
            "END",
            "ASSIGN x 'world'"
        ]
        expected = ["TypeMismatch: ASSIGN x 'world'"]

        self.assertTrue(TestUtils.check(input, expected, 108))

    # Testing unknown block
    def test_9(self):
        input = [
            "BEGIN",
            "INSERT x number",
            "END",
            "END"
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 109))

    def test_10(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "ASSIGN x 10",
            "LOOKUP x",
            "LOOKUP y",
            "END"
        ]
        expected = ["success", "success", "success", "0", "1"]

        self.assertTrue(TestUtils.check(input, expected, 110))

    def test_11(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string",
            "LOOKUP x",
            "END",
            "LOOKUP x"
        ]
        expected = ["success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 111))

    # Testing Print and RPRINT with no variables
    def test_12(self):
        input = [
            "PRINT", 
            "RPRINT"
        ]
        expected = ["", ""]

        self.assertTrue(TestUtils.check(input, expected, 112))

    # Testing shadowing
    def test_13(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string",  # shadowing allowed
            "END",
            "LOOKUP x"
        ]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 113))


    # Testing type mismatch in assignment
    def test_14(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "ASSIGN x 'abc'",
            "END"
        ]
        expected = ["TypeMismatch: ASSIGN x 'abc'"]
        self.assertTrue(TestUtils.check(input, expected, 114))

    # Testing unknown block
    def test_15(self):
        input = [
            "END"
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 115))

    # Testing undeclared variable in assignment
    def test_16(self):
        input = ["ASSIGN x 5"]
        expected = ["Undeclared: ASSIGN x 5"]
        self.assertTrue(TestUtils.check(input, expected, 116))

    # Testing undeclared variable in lookup
    def test_17(self):
        input = ["LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 117))

    # Testing Print with multiple variables in nested blocks
    def test_18(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "INSERT d number",
            "BEGIN",
            "INSERT c number",
            "PRINT",
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "success", "a//0 b//1 d//1 c//2"]
        self.assertTrue(TestUtils.check(input, expected, 118))

    # Testing Print with shadowing
    def test_19(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a string",
            "PRINT",
            "END"
        ]
        expected = ["success", "success", "a//1"]
        self.assertTrue(TestUtils.check(input, expected, 119))

    # Testing Look up in nested blocks with multiple levels
    def test_20(self):
        input = [
            "INSERT a number",
            "BEGIN",             # level 1
            "BEGIN",             # level 2
            "BEGIN",             # level 3
            "LOOKUP a",
            "END",
            "END",
            "END",
            "LOOKUP a",
        ]
        expected = ["success", "0", "0"]
        self.assertTrue(TestUtils.check(input, expected, 120))

    # Testing inserting same variable in nested blocks should allow shadowing
    def test_21(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a string",
            "END",
            "LOOKUP a"
        ]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 121))

    # Testing LOOKUP on variable that only exists in parent after nested scope ends
    def test_22(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "BEGIN",
            "LOOKUP x",
            "END",
            "END"
        ]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 122))

    # Testing PRINT after multiple insertions and ends should reflect current scope only
    def test_23(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y number",
            "BEGIN",
            "INSERT z string",
            "PRINT",
            "END",
            "PRINT",
            "END",
            "PRINT"
        ]
        expected = [
            "success", "success", "success", 
            "x//0 y//1 z//2", 
            "x//0 y//1", 
            "x//0"
        ]
        self.assertTrue(TestUtils.check(input, expected, 123))

    # Testing deep nested BEGIN/END to check stability
    def test_24(self):
        input = [
            "BEGIN", "BEGIN", "BEGIN", "BEGIN", 
            "INSERT x number", 
            "LOOKUP x", 
            "END", "END", "END", "END"
        ]
        expected = ["success", "4"]
        self.assertTrue(TestUtils.check(input, expected, 124))

    # Testing RPRINT in a deeply nested block
    def test_25(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y number",
            "BEGIN",
            "INSERT z string",
            "RPRINT",
            "END",
            "END"
        ]
        expected = ["success", "success", "success", "z//2 y//1 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 125))

    # Testing inserting reserved keyword as identifier (assuming keywords are not restricted)
    def test_26(self):
        input = [
            "INSERT string number",
            "LOOKUP string"
        ]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 126))

    # Testing multiple ENDs exceeding BEGINs to check error handling
    def test_27(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "END",
            "END",
            "END"
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 127))

    # Testing multiple shadowings of same identifier across nested blocks
    def test_28(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT x string",
            "BEGIN",
            "INSERT x number",
            "LOOKUP x",
            "END",
            "LOOKUP x",
            "END",
            "LOOKUP x"
        ]
        expected = ["success", "success", "success", "2", "1", "0"]
        self.assertTrue(TestUtils.check(input, expected, 128))

    
    def test_29(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "END",
            "END",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 129))

    
    def test_30(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "END",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 130))

    def test_31(self):
        input = [
            "INSERT  x number"
        ]
        expected = ["Invalid: INSERT  x number"]
        self.assertTrue(TestUtils.check(input, expected, 131))

    def test_32(self):
        input = [
            "INSERT x  number"
        ]
        expected = ["Invalid: INSERT x  number"]
        self.assertTrue(TestUtils.check(input, expected, 132))
    
    
    def test_33(self):
        input = [
            "INSERT          x          number"
        ]
        expected = ["Invalid: INSERT          x          number"]
        self.assertTrue(TestUtils.check(input, expected, 133))

    def test_34(self):
        input = ["BEGIN   HELLO"]
        expected = ["Invalid: BEGIN   HELLO"]
        self.assertTrue(TestUtils.check(input, expected, 134))
    
    def test_35(self):
        input = ["END   xy z"]
        expected = ["Invalid: END   xy z"]
        self.assertTrue(TestUtils.check(input, expected, 135))
    
    def test_36(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "ASSIGN x y",
            "END",
        ]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 136))
        
    def test_37(self):
        input = [
            "INSERT x string",
            "INSERT y string",
            "ASSIGN x y",
            "ASSIGN y x",
        ]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 137))
        
    def test_38(self):
        input = [
            "INSERT x string",
            "ASSIGN x ''",
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "INSERT x string",
            "ASSIGN x aFDFDSF",
        ]
        expected = ["Undeclared: ASSIGN x aFDFDSF"]
        self.assertTrue(TestUtils.check(input, expected, 139))
    
    def test_40(self):
        input = [
            "INSERT x number",
            "ASSIGN x 14.5",
        ]
        expected = ["Invalid: ASSIGN x 14.5"]
        self.assertTrue(TestUtils.check(input, expected, 140))
        
    def test_41(self):
        input = [
            "INSERT x number",
            "ASSIGN x -1242",
        ]
        expected = ["Invalid: ASSIGN x -1242"]
        self.assertTrue(TestUtils.check(input, expected, 141))
        
    def test_42(self):
        input = [
            "INSERT x number",
            "INSERT x fasfsb"
        ]
        expected = ["Invalid: INSERT x fasfsb"]
        self.assertTrue(TestUtils.check(input, expected, 142))
    
    
    def test_43(self):
        input = [
            "INSERT x abc"
        ]
        expected = ["Invalid: INSERT x abc"]
        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "BEGIN",
            "INSERT y string",
            "ASSIGN y 'abbc@@1'"
        ]
        expected = ["Invalid: ASSIGN y 'abbc@@1'"]
        self.assertTrue(TestUtils.check(input, expected, 144))
    
    def test_45(self):
        input = ["BEGIN"]* 1000 + ["END"]*1000
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 145))
        
    def test_46(self):
        input = [
            "INSERT y string",
            "ASSIGN x 5",
            "ASSIGN y '5'"
        ]
        expected = ["Undeclared: ASSIGN x 5"]
        self.assertTrue(TestUtils.check(input, expected, 146))
    
    def test_47(self):
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
        self.assertTrue(TestUtils.check(input, expected, 147))
        
    def test_48(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a string",
            "ASSIGN a 'hello'",
            "LOOKUP a",
            "BEGIN",
            "INSERT b number",
            "ASSIGN b 123",
            "LOOKUP b",
            "END",
            "END",
            "LOOKUP a",
        ]
        expected = [
            "success", "success", "success", "1", "success", "success", "2", "0"
        ]
        self.assertTrue(TestUtils.check(input, expected, 148))
        
    def test_49(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "BEGIN",
            "INSERT z number",
            "PRINT",
            "RPRINT",
            "END",
            "PRINT",
            "RPRINT",
            "END",
            "PRINT",
            "RPRINT"
        ]
        expected = [
            "success", "success", "success",
            "x//0 y//1 z//2",
            "z//2 y//1 x//0",
            "x//0 y//1",
            "y//1 x//0",
            "x//0",
            "x//0"
        ]
        self.assertTrue(TestUtils.check(input, expected, 149))
    
    def test_50(self):
        input = ["INSERT s string", "ASSIGN s hello"]
        expected = ["Undeclared: ASSIGN s hello"]
        self.assertTrue(TestUtils.check(input, expected, 150))
        
    def test_51(self):
        input = ["INSERT s number", "ASSIGN s hello"]
        expected = ["Undeclared: ASSIGN s hello"]
        self.assertTrue(TestUtils.check(input, expected, 151))
        
    def test_52(self):
        input = ["INSERT a number", "INSERT a AAAAA"]
        expected = ["Invalid: INSERT a AAAAA"]
        self.assertTrue(TestUtils.check(input, expected, 152))
    
    def test_53(self):
        input = ["ASSIGN a 1AAAA"]
        expected = ["Invalid: ASSIGN a 1AAAA"]
        self.assertTrue(TestUtils.check(input, expected, 153))