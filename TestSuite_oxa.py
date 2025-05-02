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
            "INSERT var number",
            "LOOKUP var1",
        ]
        expected = ["Undeclared: LOOKUP var1"]

        self.assertTrue(TestUtils.check(input, expected, 107))

    def test_8(self):
        input = [
            "INSERT value string",
            "INSERT value number",
        ]
        expected = ["Redeclared: INSERT value number"]

        self.assertTrue(TestUtils.check(input, expected, 108))

    def test_9(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "LOOKUP x",
            "LOOKUP y",
            "END",
            "LOOKUP x",
        ]
        expected = ["success", "success", "0", "1", "0"]
        self.assertTrue(TestUtils.check(input, expected, 109))

    def test_10(self):
        input = [
            "INSERT a string",
            "BEGIN",
            "INSERT b number",
            "LOOKUP a",
            "END",
            "LOOKUP a",
        ]
        expected = ["success", "success", "0", "0"]
        self.assertTrue(TestUtils.check(input, expected, 110))


#chờ xét xử
    def test_11(self):
        input = [
            "INSERT a number",
            "INSERT c string",
            "ASSIGN c a",
        ]
        expected = ["TypeMismatch: ASSIGN c a"]
        self.assertTrue(TestUtils.check(input, expected, 111))

    def test_12(self):
        input = [
            "INSERT abc number",
            "BEGIN",
            "ASSIGN d abc",
            "END",
        ]
        expected = ["Undeclared: ASSIGN d abc"]
        self.assertTrue(TestUtils.check(input, expected, 112))


# ê cái test này không có hiểu tại sao luôn á
    def test_13(self):
        input = [
            "INSERT target string",
            "BEGIN",
            "ASSIGN target source",
            "END",
        ]
        expected = ["Undeclared: ASSIGN target source"]
        self.assertTrue(TestUtils.check(input, expected, 113))

    def test_14(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "BEGIN",
            "INSERT a string",
            "PRINT",
            "END",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "b//1 a//2", "a//0 b//1"]
        self.assertTrue(TestUtils.check(input, expected, 114))

    def test_15(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "BEGIN",
            "INSERT a number",
            "PRINT",
            "END",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "b//1 a//2", "a//0 b//1"]
        self.assertTrue(TestUtils.check(input, expected, 115))

    def test_16(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT a string",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 116))

    def test_17(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT a string",
            "BEGIN",
            "INSERT b number",
            "INSERT c string",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 117))

    def test_18(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "BEGIN",
            "INSERT a string",
            "BEGIN",
            "INSERT b number",
            "INSERT c string",
            "END",
        ]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 118))

    def test_19(self):
        input = [
            "BEGIN",
            "INSERT b string",
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 119))

    def test_20(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "BEGIN",
            "INSERT a string",
            "RPRINT",
            "END",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "a//2 b//1", "b//1 a//0"]
        self.assertTrue(TestUtils.check(input, expected, 120))

    def test_21(self):
        input = [
            "INSERT a number",
            "INSERT a abde",
        ]
        expected = ["Invalid: INSERT a abde"]
        self.assertTrue(TestUtils.check(input, expected, 121))

    def test_22(self):
        input = [
            "INERT a number"
        ]
        expected = ["Invalid: INERT a number"]
        self.assertTrue(TestUtils.check(input, expected, 122))

    def test_23(self):
        input = [
            "INSERT a number",
            "ASSIGN a 123.1",
        ]
        expected = ["Invalid: ASSIGN a 123.1"]
        self.assertTrue(TestUtils.check(input, expected, 123))

    def test_24(self):
        input = [
            "INSERT a number",
            "ASSIGN a 123ABC",
        ]
        expected = ["Invalid: ASSIGN a 123ABC"]
        self.assertTrue(TestUtils.check(input, expected, 124))

    def test_25(self):
        input = [
            "INSERT a string",
            "ASSIGN a 'abc'",
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 125))

    def test_26(self):
        input = [
            "INSERT a strng",
            "ASSIGN a 'abc123'",
        ]
        expected = ["Invalid: INSERT a strng"]
        self.assertTrue(TestUtils.check(input, expected, 126))
#warn !!!!
    def test_27(self):
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
        # expected = ["success", "success", "success", "success", "success", "1", "1", "1", "0", "0"]
        expected = ["Undeclared: LOOKUP d"]
        self.assertTrue(TestUtils.check(input, expected, 127))

    def test_28(self):
        input = [
            "ASSIGN a 4n123"
        ]
        expected = ["Invalid: ASSIGN a 4n123"]
        self.assertTrue(TestUtils.check(input, expected, 128))

    def test_29(self):
        input = [
            "RPRINT"
        ]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 129))

    def test_30(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "END",
            "END",
        ]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 130))

    def test_31(self):
        input = [
            "INSERT a string",
            "ASSIGN a 'd b c'",
        ]
        expected = ["Invalid: ASSIGN a 'd b c'"]
        self.assertTrue(TestUtils.check(input, expected, 131))

    # def test_32(self):
    #     input = [
    #         "INSERT a number",
    #         "ASSIGN a 0",
    #     ]
    #     expected = ["Invalid: ASSIGN a 0"]
    #     self.assertTrue(TestUtils.check(input, expected, 132))

    def test_33(self):
        input = [
            "INSERT a number",
            "ASSIGN a -17262.62",
        ]
        expected = ["Invalid: ASSIGN a -17262.62"]
        self.assertTrue(TestUtils.check(input, expected, 133))

    def test_34(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT a string",
            "END",
            "BEGIN",
            "LOOKUP a",
            "END",
        ]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 134))

    def test_35(self):
        input = [
            "INSERT a string",
            "ASSIGN a ''",
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 135))

    def test_36(self):
        input = [
            "INSERT a string",
            "ASSIGN a 'b '",
        ]
        expected = ["Invalid: ASSIGN a 'b '"]
        self.assertTrue(TestUtils.check(input, expected, 136))

    def test_37(self):
        input = [
            "BEGIN",
            "INSERT a string",
            "END",
            "INSERT a number",
        ]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 137))

    def test_38(self):
        input = [
            "INSERT a string",
            "ASSIGN a 'abc'",
            "INSERT b number",
            "ASSIGN b 123",
            "END",
            "PRINT"
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "INSERT a number",
            "INSERT b number",
            "ASSIGN a b",
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 139))

    def test_40(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "ASSIGN a b",
        ]
        expected = ["TypeMismatch: ASSIGN a b"]
        self.assertTrue(TestUtils.check(input, expected, 140))

    # def test_41(self):
    #     input = [
    #         "INSERT a number",
    #         "BEGIN",
    #         "INSERT a string",
    #         "ASSIGN a 123",
    #         "END", (end hay ko end co anh huong khong)
    #     ]
    #     expected = ["TypeMismatch: ASSIGN a 123"]
    #     self.assertTrue(TestUtils.check(input, expected, 141))

    def test_42(self):
        input = [
            "INSERT a number",
            "BEGN",
            "INSERT b string",
            "ASSIGN a 123",
            "END",
        ]
        expected = ["Invalid: BEGN"]
        self.assertTrue(TestUtils.check(input, expected, 142))

    def test_43(self):
        input = [
            "INSERT a123_ number",
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "INSERT Abc123_ number",
        ]
        expected = ["Invalid: INSERT Abc123_ number"]
        self.assertTrue(TestUtils.check(input, expected, 144))

    def test_45(self):
        input = [
            "INSERT c12a_b number",
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_46(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "ASSIGN x 20",
            "LOOKUP x",
            "END",
        ]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 146))
#warn !!!
    def test_47(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "ASSIGN x 20",
            "INSERT x number",
            "END",
            "LOOKUP x",
        ]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 147))

    def test_48(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "ASSIGN b 123",
            "END",
        ]
        expected = ["TypeMismatch: ASSIGN b 123"]
        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_49(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "ASSIGN a 123",
            "END",
            "INSERT b string",
            "ASSIGN b 123",
        ]
        expected = ["TypeMismatch: ASSIGN b 123"]
        self.assertTrue(TestUtils.check(input, expected, 149))

    def test_50(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 150))

    def test_51(self):
        input = [
            "INSERT x string",
            "ASSIGN 1x 'string'",
        ]
        expected = ["Invalid: ASSIGN 1x 'string'"]
        self.assertTrue(TestUtils.check(input, expected, 151))

    def test_52(self):
        input = [
            "INSERT number string",
        ]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 152))

    def test_53(self):
        input = [
            "INSERT  number string"
        ]
        expected = ["Invalid: INSERT  number string"]
        self.assertTrue(TestUtils.check(input, expected, 153))

    def test_54(self):
        input = [
            "INSERT 123 number",
        ]
        expected = ["Invalid: INSERT 123 number"]
        self.assertTrue(TestUtils.check(input, expected, 154))

    def test_55(self):
        input = [
            "INSERT A123_ number",
        ]
        expected = ["Invalid: INSERT A123_ number"]
        self.assertTrue(TestUtils.check(input, expected, 155))

    def test_56(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "ASSIGN a 123",
            "END",
        ]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 156))

    def test_57(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "ASSIGN a b",
            "END"
        ]
        expected = ["Undeclared: ASSIGN a b"]
        self.assertTrue(TestUtils.check(input, expected, 157))

    def test_58(self):
        input = [
            "INSERT global_a number",
            "INSERT global_b string",
            "PRINT",
            "BEGIN",
            "INSERT inner_a number",
            "ASSIGN inner_a global_a",
            "INSERT global_a string",
            "LOOKUP global_a",
            "LOOKUP global_b",
            "PRINT",
            "BEGIN",
            "INSERT inner_b number",
            "LOOKUP inner_a",
            "LOOKUP global_a",
            "ASSIGN global_a 'level2string'",
            "RPRINT",
            "END",
            "LOOKUP global_a",
            "RPRINT",
            "END",
            "LOOKUP global_a",
            "PRINT",
        ]
        expected = ["success", "success", "global_a//0 global_b//0", "success", "success", "success", "1", "0",
                    "global_b//0 inner_a//1 global_a//1", "success", "1", "1", "success",
                    "inner_b//2 global_a//1 inner_a//1 global_b//0", "1", "global_a//1 inner_a//1 global_b//0",
                    "0", "global_a//0 global_b//0"]
        self.assertTrue(TestUtils.check(input, expected, 158))

    def test_59(self):
        input = [
            "INSERT a number",
            "INSERT a sssss@@",
        ]
        expected = ["Invalid: INSERT a sssss@@"]
        self.assertTrue(TestUtils.check(input, expected, 159))

    def test_60(self):
        input = [
            "ASSIGN a ssjnsnsnsj@",
        ]
        expected = ["Invalid: ASSIGN a ssjnsnsnsj@"]
        self.assertTrue(TestUtils.check(input, expected, 160))


