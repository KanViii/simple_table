import unittest
from TestUtils import TestUtils
class TestSymbolTable(unittest.TestCase):

	def test_0(self):
		input = [
			"PRINT",
			"ASSIGN g_1 unimportant",
			"RPRINT",
			"END",
			"INSERT f_FF number",
			"INSERT x string",
			"RPRINT",
		]
		expected = ["Undeclared: ASSIGN g_1 unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 0))
	def test_1(self):
		input = [
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 1))
	def test_2(self):
		input = [
			"INSERT g_1 number",
			"ASSIGN g_1 1001",
			"ASSIGN g_1 789",
			"PRINT",
			"LOOKUP g_1",
			"PRINT",
			"RPRINT",
			"INSERT b string",
			"LOOKUP g_1",
			"PRINT",
			"ASSIGN g_1 123",
			"BEGIN",
			"LOOKUP y",
			"RPRINT",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 2))
	def test_3(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"UWAAAA",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 3))
	def test_4(self):
		input = [
			"END",
			"RPRINT",
			"INSERT a string",
			"ASSIGN a '1234ABC'",
			"ASSIGN a '1234ABC'",
			"INSERT b string",
			"END",
			"INSERT f_FF string",
			"RPRINT",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"ASSIGN y unimportant",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 4))
	def test_5(self):
		input = [
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN random",
			"RPRINT",
			"INSERT d number",
			"BEGIN",
			"LOOKUP d",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 5))
	def test_6(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"END",
			"INSERT y number",
			"ASSIGN y 987654",
			"INSERT b string",
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"INSERT f_FF string",
			"RPRINT",
			"INSERT g_1 number",
			"RPRINT",
			"ASSIGN g_1 123",
			"LOOKUP f_FF",
			"ASSIGN g_1 987654",
			"PRINT",
			"LOOKUP b",
			"INSERT z number",
			"ASSIGN b 'Test123'",
			"ASSIGN b '1234ABC'",
			"ASSIGN g_1 987654",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 6))
	def test_7(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 7))
	def test_8(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 8))
	def test_9(self):
		input = [
			"PRINT",
			"INSERT c number",
			"ASSIGN z unimportant",
			"INSERT f_FF string",
			"END",
		]
		expected = ["Undeclared: ASSIGN z unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 9))
	def test_10(self):
		input = [
			"BEGIN",
			"PRINT",
			"ASSIGN d unimportant",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"END random",
		]
		expected = ["Undeclared: ASSIGN d unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 10))
	def test_11(self):
		input = [
			"PRINT",
			"INSERT z number",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT d string",
			"INSERT b number",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 11))
	def test_12(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT b number",
			"INSERT c string",
			"INSERT d number",
			"BEGIN",
			"RPRINT",
			"INSERT b string",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 12))
	def test_13(self):
		input = [
			"INSERT x number",
			"INSERT f_FF number",
			"INSERT e_123_2r string",
			"INSERT g_1 number",
			"PRINT",
			"LOOKUP x",
			"RPRINT",
			"RPRINT",
			"LOOKUP e_123_2r",
			"PRINT random",
			"RPRINT",
			"ASSIGN 1xyz 123",
			"BEGIN",
			"LOOKUP g_1",
			"LOOKUP e_123_2r",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"END",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 13))
	def test_14(self):
		input = [
			"INSERT g_1 string",
			"BEGIN",
			"PRINT",
			"ASSIGN g_1 'HelloWorld'",
			"PRINT",
			"INSERT a number",
			"END",
			"INSERT c number",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT z number",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"ASSIGN z 'Test123'",
			"ASSIGN z 'HelloWorld'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 14))
	def test_15(self):
		input = [
			"BEGIN random",
			"END",
			"BEGIN",
			"ASSIGN aak e 123",
			"RPRINT",
			"ASSIGN b unimportant",
			"BEGIN",
			"INSERT z number",
			"BEGIN random",
			"RPRINT",
			"LOOKUP z",
			"LOOKUP z",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT y number",
			"PRINT",
			"ASSIGN z 1001",
			"LOOKUP z",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
			"ASSIGN e_123_2r unimportant",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 15))
	def test_16(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 16))
	def test_17(self):
		input = [
			"RPRINT",
			"LOOKUP x",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 17))
	def test_18(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 18))
	def test_19(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT b string random",
			"BEGIN",
		]
		expected = ["Invalid: INSERT b string random"]

		self.assertTrue(TestUtils.check(input, expected, 19))
	def test_20(self):
		input = [
			"ASSIGN 21_3c 123",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"INSERT z number",
		]
		expected = ["Invalid: ASSIGN 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 20))
	def test_21(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"END",
			"BEGIN",
			"INSERT g_1 number",
			"BEGIN",
			"INSERT e_123_2r number",
			"ASSIGN g_1 789",
			"PRINT",
			"ASSIGN e_123_2r 987654",
			"INSERT b number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 21))
	def test_22(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT a number",
			"END",
			"INSERT e_123_2r number",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"ASSIGN e_123_2r 987654",
			"INSERT c string",
			"BEGIN",
			"LOOKUP e_123_2r",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 22))
	def test_23(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT d string",
			"ASSIGN d 'Test123'",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
			"RPRINT random",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT g_1 string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 23))
	def test_24(self):
		input = [
			"UWAAAA",
			"INSERT b string",
			"ASSIGN b '1234ABC'",
			"LOOKUP b",
			"END",
			"RPRINT",
			"UWAAAA",
			"INSERT g_1 string",
			"PRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"INSERT x string",
			"INSERT a string",
			"BEGIN",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 24))
	def test_25(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 25))
	def test_26(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 26))
	def test_27(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 27))
	def test_28(self):
		input = [
			"RPRINT",
			"BEGIN",
			"ASSIGN e_123_2r unimportant",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 28))
	def test_29(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT z string",
			"END",
			"BEGIN",
			"INSERT a number",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["", "", "", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 29))
	def test_30(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT a number",
			"ASSIGN a 'abcABC'",
			"ASSIGN a 987654",
			"INSERT b number",
			"BEGIN",
			"ASSIGN b 123",
			"INSERT d string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 30))
	def test_31(self):
		input = [
			"END",
			"END",
			"RPRINT",
			"ASSIGN aak e 123",
			"END",
			"INSERT a string",
			"BEGIN",
			"INSERT a number",
			"RPRINT",
			"PRINT",
			"INSERT a number",
			"BEGIN",
			"ASSIGN a 123",
			"END",
			"LOOKUP a",
			"LOOKUP a",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 31))
	def test_32(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT c number random",
			"INSERT z number",
			"LOOKUP z",
			"INSERT a string",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"LOOKUP z",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"RPRINT",
			"LOOKUP a",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
			"INSERT f_FF string",
		]
		expected = ["Invalid: INSERT c number random"]

		self.assertTrue(TestUtils.check(input, expected, 32))
	def test_33(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT d string random",
			"INSERT z number",
			"ASSIGN z 123",
			"RPRINT",
			"LOOKUP z",
			"PRINT",
			"LOOKUP d",
			"LOOKUP d",
			"ASSIGN z 1001",
			"PRINT",
			"END",
			"INSERT z number",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT x number",
			"RPRINT",
			"ASSIGN x 789",
		]
		expected = ["Invalid: INSERT d string random"]

		self.assertTrue(TestUtils.check(input, expected, 33))
	def test_34(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT 1xyz 123",
			"END",
			"BEGIN",
			"END random",
			"RPRINT",
			"PRINT",
			"INSERT b string",
			"BEGIN",
			"ASSIGN b '1234ABC'",
			"BEGIN",
			"INSERT z string",
			"ASSIGN b 'UPPERlower'",
			"LOOKUP z",
			"ASSIGN b 987654",
			"PRINT",
			"ASSIGN b 'Test123'",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 34))
	def test_35(self):
		input = [
			"INSERT z string random",
			"PRINT",
		]
		expected = ["Invalid: INSERT z string random"]

		self.assertTrue(TestUtils.check(input, expected, 35))
	def test_36(self):
		input = [
			"INSERT c string",
			"END",
			"RPRINT",
			"INSERT b string",
			"LOOKUP b",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 36))
	def test_37(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 37))
	def test_38(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"INSERT d number",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP d",
			"END",
		]
		expected = ["", "success", "d//0", "d//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 38))
	def test_39(self):
		input = [
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT random",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 39))
	def test_40(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT e_123_2r number",
			"INSERT g_1 string",
			"RPRINT",
			"END random",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 40))
	def test_41(self):
		input = [
			"END",
			"INSERT c number",
			"UWAAAA",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT g_1 string",
			"PRINT",
			"RPRINT",
			"LOOKUP g_1",
			"ASSIGN g_1 'Test123'",
			"INSERT x number",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT c number",
			"INSERT g_1 number",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 41))
	def test_42(self):
		input = [
			"END",
			"INSERT g_1 string",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"END",
			"ASSIGN e_123_2r unimportant",
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT d string",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 42))
	def test_43(self):
		input = [
			"RPRINT",
			"INSERT b number",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"LOOKUP b",
			"BEGIN",
			"INSERT z number",
			"END",
			"END",
			"ASSIGN ()z 123",
			"END",
			"INSERT a number",
			"END",
			"INSERT z string",
			"END",
			"PRINT",
			"PRINT",
			"INSERT c number",
			"ASSIGN c 123",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN c 123",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 43))
	def test_44(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 44))
	def test_45(self):
		input = [
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 45))
	def test_46(self):
		input = [
			"INSERT b string",
			"RPRINT",
			"LOOKUP b",
			"LOOKUP b",
			"INSERT e_123_2r string",
			"INSERT x number",
			"BEGIN random",
			"PRINT",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 46))
	def test_47(self):
		input = [
			"UWAAAA",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 47))
	def test_48(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"ASSIGN b 'abcABC'",
			"ASSIGN b '1234ABC'",
		]
		expected = ["", "", "", "", "", "success", "b//0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 48))
	def test_49(self):
		input = [
			"BEGIN",
			"END",
			"INSERT z number",
			"INSERT z number",
			"RPRINT",
			"PRINT",
			"INSERT b string",
			"INSERT c number",
			"RPRINT",
			"INSERT x number",
			"INSERT __ g 123",
			"RPRINT",
			"BEGIN",
			"ASSIGN x 456",
			"PRINT",
			"INSERT g_1 string",
			"END",
		]
		expected = ["Redeclared: INSERT z number"]

		self.assertTrue(TestUtils.check(input, expected, 49))
	def test_50(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"END",
			"INSERT e_123_2r string",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT y string",
			"LOOKUP e_123_2r",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"LOOKUP e_123_2r",
		]
		expected = ["", "", "success", "1", "success", "e_123_2r//0", "e_123_2r//0", "e_123_2r//0", "success", "0", "e_123_2r//0", "e_123_2r//0", "e_123_2r//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 50))
	def test_51(self):
		input = [
			"END",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT x string",
			"PRINT",
			"UWAAAA",
			"INSERT d number",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"ASSIGN d 456",
			"INSERT z string",
			"ASSIGN d 987654",
			"LOOKUP f_FF",
			"INSERT g_1 number",
			"ASSIGN g_1 456",
			"BEGIN",
			"RPRINT",
			"LOOKUP d",
			"ASSIGN g_1 123",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 51))
	def test_52(self):
		input = [
			"END",
			"BEGIN",
			"INSERT c number",
			"UWAAAA",
			"ASSIGN c 456",
			"ASSIGN c 1001",
			"LOOKUP c",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"LOOKUP c",
			"LOOKUP c",
			"UWAAAA",
			"END",
			"END",
			"PRINT",
			"INSERT f_FF string",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"BEGIN",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 456 random",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 52))
	def test_53(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 53))
	def test_54(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number",
			"BEGIN",
			"END",
		]
		expected = ["", "success"]

		self.assertTrue(TestUtils.check(input, expected, 54))
	def test_55(self):
		input = [
			"LOOKUP x",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT a number",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 55))
	def test_56(self):
		input = [
			"INSERT 2_3f 123",
			"PRINT",
			"INSERT g_1 number",
			"RPRINT",
			"BEGIN",
			"RPRINT random",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: INSERT 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 56))
	def test_57(self):
		input = [
			"INSERT g_1 number",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"INSERT y string",
			"INSERT a string",
			"ASSIGN f_FF unimportant",
			"PRINT",
			"ASSIGN y '1234ABC'",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"ASSIGN a 'Test123'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 57))
	def test_58(self):
		input = [
			"INSERT b number",
			"ASSIGN b 987654",
			"RPRINT",
			"PRINT",
			"INSERT z string",
			"LOOKUP b",
			"PRINT",
			"LOOKUP b",
			"RPRINT",
			"INSERT g_1 number",
			"LOOKUP z",
			"BEGIN",
			"INSERT d string",
			"LOOKUP b",
			"ASSIGN d 'UPPERlower'",
			"LOOKUP d",
			"INSERT f_FF string",
			"END random",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 58))
	def test_59(self):
		input = [
			"BEGIN",
			"INSERT z number",
			"PRINT",
			"BEGIN",
			"INSERT b string",
			"INSERT d number",
			"ASSIGN d 123",
			"INSERT c number",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT d string",
			"RPRINT",
			"LOOKUP d",
			"ASSIGN d '1234ABC'",
			"END",
			"PRINT",
		]
		expected = ["success", "z//1", "success", "success", "success", "success", "z//1", "z//1", "z//1", "success", "d//1", "1", "success", ""]

		self.assertTrue(TestUtils.check(input, expected, 59))
	def test_60(self):
		input = [
			"BEGIN",
			"INSERT c string",
			"BEGIN",
			"INSERT y number",
			"ASSIGN c 'Test123'",
			"BEGIN",
			"LOOKUP a",
			"END",
			"ASSIGN y 123",
			"END",
			"LOOKUP c",
			"LOOKUP c",
			"INSERT e_123_2r number",
			"ASSIGN c 'UPPERlower'",
			"INSERT f_FF number",
			"INSERT d number",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 60))
	def test_61(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT x number",
			"PRINT",
			"PRINT",
			"LOOKUP x",
			"INSERT d string",
			"INSERT x string",
			"RPRINT",
			"ASSIGN d 'HelloWorld'",
			"INSERT g_1 string",
			"RPRINT",
			"INSERT e_123_2r number",
			"LOOKUP g_1",
			"BEGIN",
			"INSERT f_FF number",
			"ASSIGN x 987654",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
		]
		expected = ["Redeclared: INSERT x string"]

		self.assertTrue(TestUtils.check(input, expected, 61))
	def test_62(self):
		input = [
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 62))
	def test_63(self):
		input = [
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 63))
	def test_64(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number",
			"RPRINT",
			"LOOKUP e_123_2r",
		]
		expected = ["", "success", "e_123_2r//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 64))
	def test_65(self):
		input = [
			"BEGIN",
			"INSERT x string",
			"PRINT",
			"INSERT b string",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
		]
		expected = ["success", "x//1", "success", "x//1 b//1", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 65))
	def test_66(self):
		input = [
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 66))
	def test_67(self):
		input = [
			"LOOKUP a",
			"RPRINT",
			"RPRINT",
			"INSERT y string",
			"RPRINT",
			"BEGIN random",
			"RPRINT",
			"BEGIN",
			"ASSIGN y 'HelloWorld'",
			"BEGIN",
			"INSERT z number",
			"END",
			"BEGIN",
			"LOOKUP y",
			"LOOKUP y",
			"RPRINT",
			"INSERT z number",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 67))
	def test_68(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"LOOKUP d",
			"BEGIN",
			"RPRINT",
			"INSERT g_1 number",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 68))
	def test_69(self):
		input = [
			"INSERT g_1 number",
			"INSERT g_1 string",
			"PRINT",
			"INSERT a string",
			"LOOKUP a",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"INSERT c number random",
			"ASSIGN x '@stArt'",
			"ASSIGN x 'Test123'",
			"INSERT x string",
			"LOOKUP x",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
		]
		expected = ["Redeclared: INSERT g_1 string"]

		self.assertTrue(TestUtils.check(input, expected, 69))
	def test_70(self):
		input = [
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"INSERT a string",
			"END",
			"END",
			"INSERT z string",
			"PRINT",
			"PRINT",
			"LOOKUP z",
			"ASSIGN e_123_2r unimportant",
			"LOOKUP z",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"INSERT f_FF number",
			"INSERT a string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 70))
	def test_71(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 71))
	def test_72(self):
		input = [
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 72))
	def test_73(self):
		input = [
			"PRINT",
			"INSERT f_FF number",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["", "success", "f_FF//0", "f_FF//0", "f_FF//0"]

		self.assertTrue(TestUtils.check(input, expected, 73))
	def test_74(self):
		input = [
			"PRINT",
			"UWAAAA",
			"INSERT g_1 number",
			"RPRINT",
			"RPRINT",
			"LOOKUP g_1",
			"BEGIN",
			"ASSIGN g_1 456",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 74))
	def test_75(self):
		input = [
			"INSERT y number",
			"ASSIGN y 123 random",
			"BEGIN",
			"PRINT",
			"ASSIGN a unimportant",
			"END",
			"ASSIGN y 987654",
			"BEGIN",
			"LOOKUP y",
			"PRINT",
			"RPRINT",
			"INSERT a number",
		]
		expected = ["Invalid: ASSIGN y 123 random"]

		self.assertTrue(TestUtils.check(input, expected, 75))
	def test_76(self):
		input = [
			"BEGIN",
			"PRINT",
			"INSERT 1xyz 123",
			"END",
			"INSERT y string",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"LOOKUP y",
			"LOOKUP y",
			"RPRINT",
			"ASSIGN y 'Test123' random",
			"LOOKUP y",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 76))
	def test_77(self):
		input = [
			"INSERT d number random",
			"INSERT y number",
			"RPRINT",
			"LOOKUP d",
			"INSERT c string",
			"PRINT",
			"ASSIGN y 987654",
			"ASSIGN c 'UPPERlower'",
			"PRINT",
			"ASSIGN c 'Test123'",
			"INSERT x string",
			"LOOKUP d",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["Invalid: INSERT d number random"]

		self.assertTrue(TestUtils.check(input, expected, 77))
	def test_78(self):
		input = [
			"END",
			"INSERT x string",
			"PRINT",
			"INSERT y number",
			"LOOKUP x",
			"ASSIGN y 'Test123'",
			"END",
			"INSERT c number",
			"END",
			"END",
			"END",
			"PRINT",
			"LOOKUP e_123_2r",
			"INSERT y_12@! 123",
			"PRINT",
			"INSERT c number",
			"LOOKUP c",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 78))
	def test_79(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT b number",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT g_1 string",
			"UWAAAA",
			"LOOKUP g_1",
			"BEGIN",
			"LOOKUP g_1",
			"PRINT",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 79))
	def test_80(self):
		input = [
			"INSERT x string",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"BEGIN",
			"ASSIGN x 'HelloWorld'",
			"ASSIGN x '1234ABC'",
			"PRINT",
			"ASSIGN x 'abcABC'",
			"BEGIN",
			"PRINT",
			"ASSIGN x '1234ABC'",
			"INSERT e_123_2r string",
			"END",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"RPRINT",
			"END",
			"END",
			"LOOKUP x",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"LOOKUP x",
			"END",
			"END",
		]
		expected = ["success", "x//0", "0", "success", "success", "x//0", "success", "x//0", "success", "success", "x//0", "0", "x//0", "0", "x//0", "success", "x//0 a//2", "x//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 80))
	def test_81(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 81))
	def test_82(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 82))
	def test_83(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT y string",
			"BEGIN",
			"ASSIGN y '1234ABC'",
			"END",
		]
		expected = ["", "", "", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 83))
	def test_84(self):
		input = [
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"END",
			"INSERT d string",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT g_1 number",
			"INSERT c string",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 84))
	def test_85(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT d string",
			"UWAAAA",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT random",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 85))
	def test_86(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"INSERT z number",
			"RPRINT",
			"ASSIGN z '1234ABC'",
			"RPRINT",
			"ASSIGN z 789",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN z '1234ABC'"]

		self.assertTrue(TestUtils.check(input, expected, 86))
	def test_87(self):
		input = [
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"ASSIGN e_123_2r 1001",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 87))
	def test_88(self):
		input = [
			"LOOKUP x",
			"INSERT f_FF string",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"LOOKUP f_FF",
			"END",
			"INSERT b string",
			"PRINT",
			"ASSIGN g_1 unimportant",
			"ASSIGN f_FF 'abcABC'",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 88))
	def test_89(self):
		input = [
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT a string",
			"INSERT c string",
			"INSERT x string",
			"LOOKUP c",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"BEGIN",
			"LOOKUP e_123_2r",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT c string",
			"LOOKUP c",
			"ASSIGN e_123_2r 'abcABC'",
			"PRINT",
			"BEGIN",
			"LOOKUP e_123_2r",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 89))
	def test_90(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 90))
	def test_91(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"BEGIN",
			"LOOKUP x",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 91))
	def test_92(self):
		input = [
			"BEGIN",
			"END random",
			"INSERT z string",
			"RPRINT",
			"INSERT f_FF string",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 92))
	def test_93(self):
		input = [
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT d string",
			"LOOKUP d",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 93))
	def test_94(self):
		input = [
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 123",
			"PRINT",
			"INSERT b number",
			"END",
			"RPRINT random",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 94))
	def test_95(self):
		input = [
			"END",
			"ASSIGN z unimportant",
			"PRINT",
			"INSERT a string",
			"END",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 95))
	def test_96(self):
		input = [
			"INSERT g_1 number",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT d string",
			"ASSIGN d 1001",
			"END",
			"BEGIN",
			"END",
			"END",
			"END",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"LOOKUP g_1",
			"PRINT",
			"LOOKUP g_1",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN d 1001"]

		self.assertTrue(TestUtils.check(input, expected, 96))
	def test_97(self):
		input = [
			"INSERT a string",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT x number",
			"ASSIGN x 456",
			"LOOKUP x",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT y number",
			"LOOKUP y",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"LOOKUP x",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 97))
	def test_98(self):
		input = [
			"INSERT y number",
			"LOOKUP y",
			"RPRINT",
			"ASSIGN y 789",
			"INSERT d number",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN f_FF unimportant",
			"ASSIGN y 987654",
			"END",
			"RPRINT",
			"ASSIGN d 123a",
			"ASSIGN d abc123",
			"ASSIGN y 123",
			"RPRINT",
			"INSERT x number",
			"ASSIGN d 789",
			"ASSIGN d 987654",
			"ASSIGN x 1001",
			"END",
		]
		expected = ["Undeclared: ASSIGN f_FF unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 98))
	def test_99(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 99))
	def test_100(self):
		input = [
			"LOOKUP a",
			"INSERT g_1 string",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 100))
	def test_101(self):
		input = [
			"RPRINT",
			"INSERT z number",
			"LOOKUP z",
			"BEGIN",
			"INSERT f_FF number",
			"ASSIGN f_FF 1001",
			"END",
		]
		expected = ["", "success", "0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 101))
	def test_102(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"END",
		]
		expected = ["", "", "", "success", "0", "x//0", "x//0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 102))
	def test_103(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 103))
	def test_104(self):
		input = [
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"INSERT f_FF number",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 104))
	def test_105(self):
		input = [
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"INSERT g_1 number",
			"INSERT x number",
			"ASSIGN x 456",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"INSERT d number",
			"BEGIN",
			"ASSIGN d 789",
			"INSERT y number",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 105))
	def test_106(self):
		input = [
			"END",
			"END",
			"BEGIN",
			"INSERT x string",
			"RPRINT",
			"BEGIN",
			"ASSIGN x 'HelloWorld'",
			"LOOKUP x",
			"RPRINT",
			"UWAAAA",
			"INSERT g_1 number",
			"INSERT a string",
			"BEGIN",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT f_FF number",
			"BEGIN",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 106))
	def test_107(self):
		input = [
			"INSERT x number",
			"ASSIGN x 456",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"UWAAAA",
			"ASSIGN x 'HelloWorld'",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT y string",
			"END",
			"INSERT z string",
			"UWAAAA",
			"INSERT y string",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT d number",
			"ASSIGN x unimportant",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 107))
	def test_108(self):
		input = [
			"INSERT 1xyz 123",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 108))
	def test_109(self):
		input = [
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 109))
	def test_110(self):
		input = [
			"PRINT",
			"INSERT f_FF string",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 110))
	def test_111(self):
		input = [
			"END",
			"LOOKUP d",
			"UWAAAA",
			"END random",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 111))
	def test_112(self):
		input = [
			"RPRINT",
			"INSERT f_FF number",
			"ASSIGN e_123_2r unimportant",
			"LOOKUP f_FF",
			"INSERT c number",
			"PRINT",
			"BEGIN",
			"ASSIGN __ g 123",
			"LOOKUP z",
			"INSERT c string",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN f_FF 789",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 112))
	def test_113(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"PRINT",
			"ASSIGN e_123_2r 'HelloWorld'",
			"END",
			"INSERT a number",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT f_FF number",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 113))
	def test_114(self):
		input = [
			"END",
			"INSERT b number",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT b string",
			"BEGIN",
			"LOOKUP b",
			"LOOKUP b",
			"END",
			"LOOKUP b",
			"ASSIGN b 'UPPERlower'",
			"ASSIGN b 'Test123'",
			"LOOKUP b",
			"BEGIN",
			"ASSIGN b 'UPPERlower'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 114))
	def test_115(self):
		input = [
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT d string",
			"ASSIGN d 'abcABC' random",
			"INSERT e_123_2r string",
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"UWAAAA",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"END",
			"END",
			"INSERT z string",
			"PRINT",
			"LOOKUP z",
			"LOOKUP z",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 115))
	def test_116(self):
		input = [
			"END random",
			"INSERT 1xyz 123",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT f_FF number",
			"ASSIGN f_FF 789",
			"LOOKUP f_FF",
			"INSERT e_123_2r number",
			"UWAAAA",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 116))
	def test_117(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 117))
	def test_118(self):
		input = [
			"INSERT c string",
			"INSERT a number",
			"LOOKUP a",
		]
		expected = ["success", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 118))
	def test_119(self):
		input = [
			"INSERT e_123_2r string",
			"BEGIN",
			"ASSIGN e_123_2r 'HelloWorld'",
			"BEGIN",
			"INSERT 2_3f 123",
			"INSERT g_1 number",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 119))
	def test_120(self):
		input = [
			"INSERT d number",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 120))
	def test_121(self):
		input = [
			"BEGIN",
			"RPRINT",
			"LOOKUP z",
			"INSERT d number",
			"PRINT",
			"INSERT y string",
			"INSERT a number",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP z"]

		self.assertTrue(TestUtils.check(input, expected, 121))
	def test_122(self):
		input = [
			"INSERT f_FF number",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT y number",
			"PRINT",
			"ASSIGN y 123",
			"LOOKUP x random",
			"ASSIGN y 'Test123'",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT b string",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 122))
	def test_123(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT c string",
			"ASSIGN c 'UPPERlower'",
			"INSERT c number",
			"LOOKUP c",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT a string",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT y number",
			"END",
		]
		expected = ["Redeclared: INSERT c number"]

		self.assertTrue(TestUtils.check(input, expected, 123))
	def test_124(self):
		input = [
			"UWAAAA",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT e_123_2r string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 124))
	def test_125(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT d number random",
			"END",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT z number",
			"END",
			"RPRINT",
			"INSERT z number",
			"END",
		]
		expected = ["Invalid: INSERT d number random"]

		self.assertTrue(TestUtils.check(input, expected, 125))
	def test_126(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 126))
	def test_127(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 127))
	def test_128(self):
		input = [
			"PRINT random",
			"PRINT",
			"LOOKUP b",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 128))
	def test_129(self):
		input = [
			"INSERT z string",
			"RPRINT",
			"BEGIN",
			"ASSIGN z '1234ABC'",
			"BEGIN",
			"INSERT y number",
			"RPRINT",
			"INSERT z string",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["success", "z//0", "success", "success", "y//2 z//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 129))
	def test_130(self):
		input = [
			"INSERT y string",
			"ASSIGN y 'UPPERlower'",
			"RPRINT random",
			"END",
			"PRINT",
			"PRINT",
			"ASSIGN b@B((*@ 123",
			"BEGIN",
			"INSERT 2_3f 123",
			"PRINT",
			"RPRINT",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 130))
	def test_131(self):
		input = [
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"BEGIN",
			"INSERT b number",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"ASSIGN e_123_2r 123",
			"END",
			"LOOKUP e_123_2r",
			"PRINT",
			"INSERT y number",
			"END",
			"INSERT x number",
			"ASSIGN x 987654",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 131))
	def test_132(self):
		input = [
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT f_FF number",
			"INSERT b string",
			"ASSIGN f_FF 987654",
			"INSERT a number",
			"END",
			"PRINT",
			"INSERT y string",
			"END",
			"RPRINT",
			"INSERT b number",
			"RPRINT",
			"INSERT f_FF string",
		]
		expected = ["", "", "", "", "", "success", "success", "success", "success", "", "success", "", "success", "b//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 132))
	def test_133(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"END",
			"PRINT",
		]
		expected = ["", "", "", "", "", "success", ""]

		self.assertTrue(TestUtils.check(input, expected, 133))
	def test_134(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"INSERT z number",
			"ASSIGN z 987654 random",
			"PRINT",
			"INSERT f_FF number",
			"LOOKUP z",
			"LOOKUP f_FF",
			"UWAAAA",
			"ASSIGN z 123",
			"LOOKUP f_FF",
			"PRINT",
			"RPRINT",
			"INSERT x number",
			"PRINT",
			"UWAAAA",
			"INSERT b number",
			"LOOKUP x",
			"PRINT",
			"LOOKUP z",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: ASSIGN z 987654 random"]

		self.assertTrue(TestUtils.check(input, expected, 134))
	def test_135(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"UWAAAA",
			"ASSIGN x 'HelloWorld'",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN x 789",
			"UWAAAA",
			"LOOKUP x",
			"RPRINT",
			"INSERT d string",
			"INSERT c string",
			"END",
			"LOOKUP x",
			"ASSIGN x 'HelloWorld'",
			"BEGIN",
			"INSERT d string",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 135))
	def test_136(self):
		input = [
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 136))
	def test_137(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r string",
		]
		expected = ["", "", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 137))
	def test_138(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT c number",
			"ASSIGN c 987654",
			"END",
			"END",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 138))
	def test_139(self):
		input = [
			"UWAAAA",
			"PRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT c string",
			"ASSIGN z unimportant",
			"INSERT y number",
			"INSERT x number",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 139))
	def test_140(self):
		input = [
			"INSERT b string",
			"PRINT",
			"BEGIN",
			"ASSIGN b 'HelloWorld'",
			"PRINT",
			"LOOKUP b",
			"END",
			"PRINT",
			"PRINT",
			"LOOKUP b",
			"ASSIGN b 'abcABC'",
			"RPRINT",
			"INSERT z number",
			"ASSIGN z 789",
			"INSERT g_1 string",
		]
		expected = ["success", "b//0", "success", "b//0", "0", "b//0", "b//0", "0", "success", "b//0", "success", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 140))
	def test_141(self):
		input = [
			"INSERT z number",
			"INSERT z number",
			"INSERT g_1 number",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"ASSIGN z 987654",
			"ASSIGN z 456",
			"PRINT",
			"END",
			"ASSIGN z 987654",
			"PRINT",
			"LOOKUP z",
			"END",
			"LOOKUP z",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Redeclared: INSERT z number"]

		self.assertTrue(TestUtils.check(input, expected, 141))
	def test_142(self):
		input = [
			"INSERT y number",
			"BEGIN",
			"INSERT z number",
			"ASSIGN z 789",
			"RPRINT",
			"PRINT",
			"ASSIGN z 123",
			"END",
			"ASSIGN y 123",
			"INSERT y string",
			"ASSIGN y 456",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP y",
			"LOOKUP y",
			"INSERT z number",
			"LOOKUP z",
			"ASSIGN y 123.5",
			"LOOKUP z",
			"PRINT",
			"LOOKUP z",
			"UWAAAA",
		]
		expected = ["Redeclared: INSERT y string"]

		self.assertTrue(TestUtils.check(input, expected, 142))
	def test_143(self):
		input = [
			"BEGIN",
			"BEGIN random",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT b string",
			"END",
			"PRINT",
			"INSERT b number",
			"BEGIN",
			"BEGIN",
			"LOOKUP b random",
			"BEGIN",
			"LOOKUP b",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 143))
	def test_144(self):
		input = [
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"UWAAAA",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT c number",
			"LOOKUP c",
			"BEGIN",
			"ASSIGN c 789",
			"INSERT c number",
			"ASSIGN c 456",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"LOOKUP b",
			"ASSIGN c 987654",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r number",
			"PRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 144))
	def test_145(self):
		input = [
			"RPRINT",
			"INSERT x string",
		]
		expected = ["", "success"]

		self.assertTrue(TestUtils.check(input, expected, 145))
	def test_146(self):
		input = [
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 146))
	def test_147(self):
		input = [
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"INSERT f_FF string",
			"END",
			"UWAAAA",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 147))
	def test_148(self):
		input = [
			"END",
			"INSERT a number random",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT b string random",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 148))
	def test_149(self):
		input = [
			"END",
			"BEGIN",
			"END",
			"INSERT g_1 string random",
			"RPRINT",
			"LOOKUP g_1",
			"INSERT f_FF string",
			"ASSIGN f_FF 'HelloWorld'",
			"INSERT y number",
			"BEGIN",
			"INSERT c number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 149))
	def test_150(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"LOOKUP b",
			"INSERT e_123_2r string",
			"INSERT z string",
			"BEGIN",
			"ASSIGN z 456",
			"PRINT",
			"LOOKUP e_123_2r",
			"LOOKUP e_123_2r",
			"PRINT",
			"ASSIGN z 'UPPERlower'",
			"LOOKUP e_123_2r",
			"INSERT e_123_2r string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 150))
	def test_151(self):
		input = [
			"INSERT g_1 number",
			"LOOKUP g_1",
			"BEGIN",
			"END",
			"PRINT",
			"END",
			"PRINT",
			"INSERT x string",
			"INSERT z string",
			"RPRINT",
			"PRINT",
			"ASSIGN z 'abcABC'",
			"ASSIGN x 'HelloWorld'",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"INSERT y string",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END random",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 151))
	def test_152(self):
		input = [
			"INSERT b number",
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT y string",
			"PRINT",
			"LOOKUP y",
			"PRINT",
			"LOOKUP y",
			"ASSIGN y 'UPPERlower'",
			"END",
			"INSERT e_123_2r number",
			"BEGIN",
			"BEGIN",
			"ASSIGN e_123_2r 123",
			"END",
			"END",
			"RPRINT",
			"INSERT x number",
			"PRINT",
			"RPRINT",
			"LOOKUP x",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 152))
	def test_153(self):
		input = [
			"INSERT f_FF string",
			"ASSIGN f_FF 'Test123'",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"UWAAAA",
			"LOOKUP f_FF",
			"RPRINT",
			"ASSIGN _@??e 123",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"LOOKUP f_FF",
			"END",
			"PRINT",
			"END",
			"PRINT",
			"INSERT f_FF string",
			"INSERT e_123_2r number",
			"ASSIGN f_FF 987654",
			"END",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 153))
	def test_154(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 154))
	def test_155(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 155))
	def test_156(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"END",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 156))
	def test_157(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT x string",
			"INSERT z string",
		]
		expected = ["", "", "", "", "", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 157))
	def test_158(self):
		input = [
			"INSERT c string",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"ASSIGN c 'Test123'",
			"INSERT g_1 string",
			"LOOKUP c",
			"LOOKUP g_1",
			"PRINT",
			"INSERT b string",
			"LOOKUP g_1",
			"END",
			"END random",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 158))
	def test_159(self):
		input = [
			"END",
			"INSERT aak e 123",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 159))
	def test_160(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT b string",
			"RPRINT random",
			"LOOKUP b",
			"ASSIGN b 'HelloWorld' random",
			"BEGIN",
			"RPRINT",
			"ASSIGN x unimportant",
			"BEGIN",
			"INSERT b number",
			"INSERT a string",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 160))
	def test_161(self):
		input = [
			"LOOKUP y",
			"PRINT",
			"BEGIN",
			"END",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT g_1 number",
			"RPRINT",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"ASSIGN g_1 123",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"END",
			"INSERT d number random",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 161))
	def test_162(self):
		input = [
			"UWAAAA",
			"END",
			"INSERT y string",
			"INSERT d string",
			"INSERT f_FF string",
			"ASSIGN y '1234ABC'",
			"LOOKUP y",
			"ASSIGN d 'abcABC'",
			"BEGIN",
			"END",
			"END",
			"END",
			"PRINT",
			"RPRINT random",
			"BEGIN",
			"INSERT b number",
			"ASSIGN b 987654",
			"RPRINT",
			"PRINT",
			"INSERT c string",
			"LOOKUP c",
			"LOOKUP c",
			"BEGIN",
			"ASSIGN b 987654",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 162))
	def test_163(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 163))
	def test_164(self):
		input = [
			"INSERT a string",
			"INSERT b@B((*@ 123",
			"ASSIGN a 456",
			"LOOKUP a",
		]
		expected = ["Invalid: INSERT b@B((*@ 123"]

		self.assertTrue(TestUtils.check(input, expected, 164))
	def test_165(self):
		input = [
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"INSERT d number",
			"LOOKUP d",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 165))
	def test_166(self):
		input = [
			"BEGIN",
			"INSERT x number",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 number",
			"INSERT b number",
			"LOOKUP b",
			"PRINT",
			"LOOKUP d",
			"LOOKUP b",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 166))
	def test_167(self):
		input = [
			"PRINT",
			"PRINT",
			"ASSIGN 21_3c 123",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT a string",
			"END",
			"END",
			"END random",
		]
		expected = ["Invalid: ASSIGN 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 167))
	def test_168(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT z number",
			"INSERT f_FF number",
			"END",
			"LOOKUP g_1",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 123",
			"INSERT g_1 string",
			"ASSIGN e_123_2r 456",
			"BEGIN",
			"LOOKUP g_1",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP g_1"]

		self.assertTrue(TestUtils.check(input, expected, 168))
	def test_169(self):
		input = [
			"END",
			"PRINT",
			"END",
			"INSERT x number",
			"ASSIGN x 789",
			"RPRINT",
			"ASSIGN x 123",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"END",
			"END",
			"END",
			"RPRINT",
			"INSERT g_1 number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 169))
	def test_170(self):
		input = [
			"RPRINT random",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT d number",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT random",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 170))
	def test_171(self):
		input = [
			"PRINT",
			"RPRINT random",
			"END",
			"END",
			"INSERT y string",
			"PRINT",
			"ASSIGN y 'UPPERlower'",
			"RPRINT",
			"PRINT",
			"ASSIGN y 'UPPERlower'",
			"ASSIGN y 'abcABC'",
			"LOOKUP y",
			"BEGIN",
			"LOOKUP y",
			"BEGIN",
			"END",
			"PRINT",
			"UWAAAA",
			"ASSIGN y 'HelloWorld'",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT a string",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 171))
	def test_172(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 172))
	def test_173(self):
		input = [
			"INSERT c number",
			"ASSIGN c 987654",
			"RPRINT",
		]
		expected = ["success", "success", "c//0"]

		self.assertTrue(TestUtils.check(input, expected, 173))
	def test_174(self):
		input = [
			"INSERT x string",
			"LOOKUP x",
			"ASSIGN x 'HelloWorld'",
			"ASSIGN x 'abcABC'",
			"LOOKUP f_FF",
			"INSERT c number",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 174))
	def test_175(self):
		input = [
			"INSERT d string",
			"INSERT x number",
			"BEGIN",
			"END",
			"LOOKUP f_FF",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 175))
	def test_176(self):
		input = [
			"BEGIN",
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 176))
	def test_177(self):
		input = [
			"BEGIN",
			"END",
			"INSERT e_123_2r string",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN z unimportant",
			"INSERT x string",
			"INSERT a number",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"RPRINT",
			"INSERT c string",
			"ASSIGN a 12 34",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN z unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 177))
	def test_178(self):
		input = [
			"PRINT",
			"END",
			"INSERT z number",
			"LOOKUP z",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"BEGIN",
			"LOOKUP z",
			"LOOKUP z",
			"LOOKUP z",
			"ASSIGN z 'abcABC'",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 178))
	def test_179(self):
		input = [
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"RPRINT random",
			"INSERT a number",
			"PRINT",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 179))
	def test_180(self):
		input = [
			"END",
			"RPRINT",
			"PRINT",
			"INSERT 1xyz 123",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"BEGIN random",
			"BEGIN",
			"INSERT y number",
			"BEGIN",
			"END",
			"LOOKUP y",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 180))
	def test_181(self):
		input = [
			"INSERT c string",
			"RPRINT",
			"RPRINT",
			"INSERT y string",
			"LOOKUP c",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"ASSIGN c 'abcABC'",
			"ASSIGN y 987654",
			"LOOKUP c",
			"ASSIGN c 'Test123'",
			"RPRINT",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP y",
			"RPRINT",
			"LOOKUP c",
			"BEGIN",
			"BEGIN",
			"INSERT x number",
			"BEGIN",
			"INSERT c number",
			"LOOKUP x",
			"LOOKUP x",
			"LOOKUP y",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 181))
	def test_182(self):
		input = [
			"LOOKUP f_FF",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 182))
	def test_183(self):
		input = [
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 183))
	def test_184(self):
		input = [
			"RPRINT",
			"INSERT c string",
			"RPRINT",
			"ASSIGN c 'UPPERlower'",
			"BEGIN",
			"INSERT a string",
			"PRINT",
			"INSERT z string",
			"PRINT",
			"END",
		]
		expected = ["", "success", "c//0", "success", "success", "c//0 a//1", "success", "c//0 a//1 z//1"]

		self.assertTrue(TestUtils.check(input, expected, 184))
	def test_185(self):
		input = [
			"INSERT c string",
			"BEGIN",
			"LOOKUP b",
			"UWAAAA",
			"PRINT",
			"INSERT z string",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"ASSIGN c 'abcABC'",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP b"]

		self.assertTrue(TestUtils.check(input, expected, 185))
	def test_186(self):
		input = [
			"INSERT e_123_2r number",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT random",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"LOOKUP e_123_2r",
			"PRINT",
			"ASSIGN e_123_2r 123",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 987654",
			"ASSIGN e_123_2r 'abcABC'",
			"ASSIGN e_123_2r 987654",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 186))
	def test_187(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"UWAAAA",
			"END",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"LOOKUP x",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 187))
	def test_188(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"LOOKUP z",
			"INSERT f_FF number",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT 21_3c 123",
			"RPRINT",
			"INSERT g_1 string",
			"PRINT",
			"ASSIGN g_1 'abcABC'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 188))
	def test_189(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT y string",
			"LOOKUP y",
			"RPRINT",
			"LOOKUP y",
			"ASSIGN y 'UPPERlower'",
			"INSERT a number",
			"BEGIN",
			"INSERT 1xyz 123",
			"BEGIN",
			"END",
			"ASSIGN y '1234ABC'",
			"ASSIGN a 123",
			"INSERT x number",
			"BEGIN",
			"END",
			"LOOKUP a",
			"RPRINT",
			"LOOKUP x",
			"UWAAAA",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 189))
	def test_190(self):
		input = [
			"END",
			"END",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"BEGIN random",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT __ g 123",
			"INSERT a string",
			"ASSIGN a 'HelloWorld'",
			"INSERT d string",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT y_12@! 123",
			"BEGIN",
			"RPRINT",
			"INSERT f_FF number",
			"END",
			"RPRINT",
			"PRINT",
			"LOOKUP d",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 190))
	def test_191(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 191))
	def test_192(self):
		input = [
			"ASSIGN g_1 unimportant",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN g_1 unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 192))
	def test_193(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT g_1 number",
			"INSERT e_123_2r number",
			"INSERT c string",
			"INSERT f_FF string",
			"PRINT",
			"END",
			"END",
		]
		expected = ["success", "success", "success", "success", "g_1//2 e_123_2r//2 c//2 f_FF//2"]

		self.assertTrue(TestUtils.check(input, expected, 193))
	def test_194(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT z string",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", "success", "z//2", "z//2"]

		self.assertTrue(TestUtils.check(input, expected, 194))
	def test_195(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT z string",
			"ASSIGN z 'Test123'",
			"BEGIN",
			"ASSIGN z 'UPPERlower'",
			"END",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 195))
	def test_196(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT a string",
			"INSERT g_1 number",
			"END",
			"END",
			"INSERT x number",
			"BEGIN",
			"BEGIN",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 196))
	def test_197(self):
		input = [
			"INSERT y number random",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP y",
			"LOOKUP y",
			"INSERT e_123_2r number",
			"END",
			"PRINT",
			"UWAAAA",
			"ASSIGN y 789",
			"ASSIGN y 987654",
			"END",
			"LOOKUP y",
			"LOOKUP y",
			"LOOKUP y",
			"LOOKUP y",
			"ASSIGN 2_3f 123",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: INSERT y number random"]

		self.assertTrue(TestUtils.check(input, expected, 197))
	def test_198(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"END",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"INSERT f_FF number",
			"BEGIN",
			"LOOKUP f_FF",
			"RPRINT",
			"BEGIN",
			"ASSIGN f_FF 987654",
			"END",
			"PRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 198))
	def test_199(self):
		input = [
			"BEGIN",
			"UWAAAA",
			"INSERT z string",
			"END",
			"INSERT e_123_2r number",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"INSERT f_FF string",
			"LOOKUP e_123_2r",
			"END",
			"INSERT z number",
			"PRINT",
			"PRINT",
			"ASSIGN z 789",
			"BEGIN",
			"UWAAAA",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"END",
			"LOOKUP e_123_2r",
			"INSERT a string",
			"UWAAAA",
			"PRINT",
			"ASSIGN a 1001",
			"ASSIGN z 'HelloWorld'",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 199))
	def test_200(self):
		input = [
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 200))
	def test_201(self):
		input = [
			"PRINT random",
			"INSERT f_FF number",
			"INSERT b string",
			"ASSIGN b '1234ABC'",
			"ASSIGN f_FF 789",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 201))
	def test_202(self):
		input = [
			"INSERT e_123_2r string",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"ASSIGN e_123_2r 'HelloWorld'",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["success", "e_123_2r//0", "success", "e_123_2r//0", "e_123_2r//0"]

		self.assertTrue(TestUtils.check(input, expected, 202))
	def test_203(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
			"INSERT x string",
			"LOOKUP x",
			"INSERT e_123_2r number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 203))
	def test_204(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT b number",
			"INSERT y string random",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP y",
			"ASSIGN y 'Test123'",
			"BEGIN",
			"INSERT c number",
			"ASSIGN y 'UPPERlower'",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT y string random"]

		self.assertTrue(TestUtils.check(input, expected, 204))
	def test_205(self):
		input = [
			"INSERT y number",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT f_FF string",
			"UWAAAA",
			"ASSIGN y 123",
			"PRINT",
			"BEGIN",
			"ASSIGN f_FF 'HelloWorld'",
			"PRINT",
			"INSERT z string",
			"INSERT x string",
			"END",
			"PRINT",
			"INSERT y number",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 205))
	def test_206(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT c string",
			"END",
			"BEGIN",
			"INSERT x string",
			"RPRINT",
			"INSERT g_1 number",
			"RPRINT",
			"INSERT b string",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 206))
	def test_207(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"INSERT y number",
			"PRINT",
			"RPRINT",
			"LOOKUP y",
			"BEGIN random",
			"BEGIN",
			"END",
			"RPRINT",
			"INSERT x number",
			"ASSIGN y 789",
			"RPRINT",
			"RPRINT",
			"INSERT f_FF number",
			"ASSIGN y 987654",
			"LOOKUP f_FF",
			"PRINT",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 207))
	def test_208(self):
		input = [
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"RPRINT",
			"LOOKUP f_FF",
			"BEGIN",
			"ASSIGN f_FF 456",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"INSERT b number",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"LOOKUP f_FF",
			"RPRINT",
			"ASSIGN f_FF 123",
			"RPRINT",
			"INSERT z number",
			"LOOKUP f_FF",
			"LOOKUP b",
			"BEGIN",
			"LOOKUP f_FF",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 208))
	def test_209(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 209))
	def test_210(self):
		input = [
			"BEGIN",
			"END",
			"UWAAAA",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 210))
	def test_211(self):
		input = [
			"PRINT",
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"ASSIGN f_FF 789",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 211))
	def test_212(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT a string",
			"RPRINT",
			"LOOKUP a",
			"RPRINT",
			"INSERT b string",
			"LOOKUP a",
			"LOOKUP b",
		]
		expected = ["", "", "", "success", "a//0", "0", "a//0", "success", "0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 212))
	def test_213(self):
		input = [
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"RPRINT",
			"LOOKUP z",
			"END",
			"INSERT c number",
			"PRINT",
			"INSERT y number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 213))
	def test_214(self):
		input = [
			"INSERT c string",
			"BEGIN",
			"END",
			"BEGIN",
			"LOOKUP c",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT c string",
			"END",
			"BEGIN",
			"ASSIGN c '1234ABC'",
			"BEGIN",
			"INSERT c number",
			"ASSIGN c 987654",
			"END",
			"END",
		]
		expected = ["success", "0", "c//0", "c//0", "c//0", "success", "success", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 214))
	def test_215(self):
		input = [
			"INSERT b number",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"LOOKUP b",
			"ASSIGN b 987654",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"LOOKUP b",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["success", "b//0", "b//0", "b//0", "b//0", "b//0", "b//0", "b//0", "0", "success", "b//0", "b//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 215))
	def test_216(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"END",
			"END random",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 216))
	def test_217(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT a string",
			"PRINT",
			"PRINT",
			"LOOKUP a",
			"RPRINT",
			"INSERT b number",
			"RPRINT",
			"LOOKUP b",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"LOOKUP b",
			"ASSIGN a 'HelloWorld'",
			"LOOKUP b",
			"LOOKUP a",
		]
		expected = ["", "", "", "", "success", "a//0", "a//0", "0", "a//0", "success", "b//0 a//0", "0", "b//0 a//0", "b//0 a//0", "0", "success", "0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 217))
	def test_218(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 218))
	def test_219(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 219))
	def test_220(self):
		input = [
			"BEGIN",
			"INSERT d string",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["success", "d//1"]

		self.assertTrue(TestUtils.check(input, expected, 220))
	def test_221(self):
		input = [
			"BEGIN",
			"INSERT a string",
			"RPRINT",
			"INSERT d string",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN d 'HelloWorld'",
			"LOOKUP a",
			"END",
		]
		expected = ["success", "a//1", "success", "a//1 d//1", "d//1 a//1", "d//1 a//1", "success", "1"]

		self.assertTrue(TestUtils.check(input, expected, 221))
	def test_222(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r '1234ABC'",
			"END",
			"PRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["", "", "success", "success", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 222))
	def test_223(self):
		input = [
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 223))
	def test_224(self):
		input = [
			"INSERT f_FF string",
			"INSERT e_123_2r number",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT d string",
			"LOOKUP e_123_2r",
			"ASSIGN d '1234ABC'",
			"END",
			"ASSIGN f_FF 'abcABC'",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT a string",
			"ASSIGN a 789",
			"END",
			"RPRINT",
			"INSERT g_1 number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 224))
	def test_225(self):
		input = [
			"INSERT y number",
			"BEGIN",
			"ASSIGN y 456",
			"BEGIN",
			"END",
			"END",
			"ASSIGN y 'HelloWorld'",
			"BEGIN",
			"ASSIGN x unimportant",
			"LOOKUP y",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
		]
		expected = ["TypeMismatch: ASSIGN y 'HelloWorld'"]

		self.assertTrue(TestUtils.check(input, expected, 225))
	def test_226(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"RPRINT",
			"END",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"INSERT a number",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN a 987654",
			"PRINT",
			"LOOKUP a",
			"ASSIGN d unimportant",
			"INSERT c string",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 226))
	def test_227(self):
		input = [
			"INSERT c string",
			"PRINT",
			"END",
			"INSERT d string random",
			"RPRINT",
			"RPRINT",
			"INSERT z string",
			"RPRINT",
			"PRINT",
			"LOOKUP c",
			"LOOKUP z",
			"PRINT",
			"END",
			"PRINT",
			"END",
			"INSERT d number",
			"END",
			"INSERT b string",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT a number",
			"LOOKUP a",
			"ASSIGN a 789",
			"BEGIN",
			"ASSIGN a 1001",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 227))
	def test_228(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 228))
	def test_229(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 229))
	def test_230(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT b string",
			"INSERT _@??e 123",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 230))
	def test_231(self):
		input = [
			"RPRINT",
			"BEGIN random",
			"INSERT z number",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 231))
	def test_232(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT x string",
			"END",
			"PRINT",
			"INSERT d string",
			"BEGIN",
			"INSERT x number",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
		]
		expected = ["success", "", "success", "success", "d//0 x//1", "d//0 x//1", "d//0 x//1", "d//0"]

		self.assertTrue(TestUtils.check(input, expected, 232))
	def test_233(self):
		input = [
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT b number",
			"RPRINT",
			"UWAAAA",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 233))
	def test_234(self):
		input = [
			"PRINT random",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"INSERT z string",
			"END",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 234))
	def test_235(self):
		input = [
			"INSERT a number",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"ASSIGN aak e 123",
			"RPRINT",
			"LOOKUP a",
			"ASSIGN a 123",
			"LOOKUP a",
			"RPRINT",
			"BEGIN",
			"LOOKUP a",
			"RPRINT",
			"ASSIGN a 987654",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT f_FF string",
			"INSERT y string",
			"INSERT e_123_2r string",
			"INSERT c string",
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN aak e 123"]

		self.assertTrue(TestUtils.check(input, expected, 235))
	def test_236(self):
		input = [
			"INSERT 2_3f 123",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT d string",
			"INSERT c number",
			"ASSIGN g_1 unimportant",
			"LOOKUP d",
			"ASSIGN d 'abcABC'",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT g_1 number",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: INSERT 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 236))
	def test_237(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 237))
	def test_238(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 238))
	def test_239(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 239))
	def test_240(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"LOOKUP a",
			"LOOKUP z",
			"ASSIGN z 'Test123'",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 240))
	def test_241(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT d string",
			"RPRINT",
			"RPRINT random",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 241))
	def test_242(self):
		input = [
			"END",
			"END",
			"PRINT",
			"RPRINT",
			"LOOKUP b",
			"BEGIN",
			"END",
			"ASSIGN g_1 unimportant",
			"INSERT d number",
			"BEGIN",
			"LOOKUP d",
			"LOOKUP d",
			"END",
			"UWAAAA",
			"INSERT b string",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 242))
	def test_243(self):
		input = [
			"END",
			"BEGIN",
			"INSERT c string",
			"ASSIGN c 'Test123'",
			"BEGIN",
			"ASSIGN c 'abcABC'",
			"INSERT f_FF number",
			"PRINT",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"BEGIN",
			"END",
			"RPRINT",
			"ASSIGN c 'HelloWorld'",
			"PRINT",
			"INSERT f_FF number",
			"RPRINT",
			"PRINT",
			"LOOKUP f_FF",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 243))
	def test_244(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT a number",
			"ASSIGN a 987654",
			"ASSIGN 2_3f 123",
			"ASSIGN a 456",
			"RPRINT",
			"BEGIN",
			"LOOKUP a",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"LOOKUP a",
			"BEGIN",
			"ASSIGN a 456",
			"ASSIGN a 456",
			"LOOKUP a",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 244))
	def test_245(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"LOOKUP z",
			"UWAAAA",
			"LOOKUP z",
			"INSERT z number",
			"RPRINT",
			"BEGIN",
			"INSERT d string",
			"ASSIGN z 'abcABC'",
			"PRINT",
			"LOOKUP z",
			"UWAAAA",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"LOOKUP d",
			"LOOKUP z",
			"RPRINT",
			"RPRINT",
			"INSERT b string",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 245))
	def test_246(self):
		input = [
			"INSERT b@B((*@ 123",
		]
		expected = ["Invalid: INSERT b@B((*@ 123"]

		self.assertTrue(TestUtils.check(input, expected, 246))
	def test_247(self):
		input = [
			"INSERT a string",
			"INSERT y string",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["success", "success", "a//0 y//0", "y//0 a//0", "a//0 y//0"]

		self.assertTrue(TestUtils.check(input, expected, 247))
	def test_248(self):
		input = [
			"BEGIN",
			"END",
			"INSERT e_123_2r number",
			"INSERT x number",
			"ASSIGN x 789",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["success", "success", "success", "x//0 e_123_2r//0"]

		self.assertTrue(TestUtils.check(input, expected, 248))
	def test_249(self):
		input = [
			"ASSIGN f_FF unimportant",
			"PRINT",
			"INSERT f_FF string",
			"INSERT y_12@! 123",
			"RPRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["Undeclared: ASSIGN f_FF unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 249))
	def test_250(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"ASSIGN a unimportant",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 250))
	def test_251(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT f_FF string",
			"INSERT d string",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = ["", "", "", "", "", "", "success", "success", "d//0 f_FF//0", "f_FF//0 d//0"]

		self.assertTrue(TestUtils.check(input, expected, 251))
	def test_252(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT z string",
			"ASSIGN z 'UPPERlower'",
			"PRINT",
			"ASSIGN z 'abcABC'",
			"RPRINT",
			"RPRINT",
			"INSERT a string",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", "", "", "", "", "", "", "success", "success", "z//1", "success", "z//1", "z//1", "success", "z//1 a//1"]

		self.assertTrue(TestUtils.check(input, expected, 252))
	def test_253(self):
		input = [
			"INSERT d string",
			"LOOKUP d",
			"INSERT y number",
			"INSERT g_1 string",
			"RPRINT",
			"PRINT",
			"INSERT y number",
			"PRINT",
			"RPRINT",
			"INSERT a string",
			"LOOKUP g_1",
			"RPRINT",
			"BEGIN",
			"ASSIGN z unimportant",
			"RPRINT",
			"ASSIGN 1xyz 123",
			"END",
			"BEGIN",
			"END",
			"UWAAAA",
			"BEGIN",
			"END",
		]
		expected = ["Redeclared: INSERT y number"]

		self.assertTrue(TestUtils.check(input, expected, 253))
	def test_254(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"INSERT z number",
			"INSERT z number",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT y string",
			"ASSIGN z 987654",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"INSERT g_1 string",
			"INSERT a string",
			"ASSIGN a 'Test123'",
			"BEGIN",
			"END",
			"INSERT x number",
			"INSERT b string",
			"RPRINT",
			"PRINT",
			"LOOKUP a",
			"LOOKUP z",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 254))
	def test_255(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 255))
	def test_256(self):
		input = [
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 256))
	def test_257(self):
		input = [
			"INSERT d number",
			"LOOKUP d",
			"RPRINT",
			"ASSIGN d 123.8.7",
			"LOOKUP d",
			"INSERT f_FF number",
			"INSERT z string",
		]
		expected = ["Invalid: ASSIGN d 123.8.7"]

		self.assertTrue(TestUtils.check(input, expected, 257))
	def test_258(self):
		input = [
			"INSERT d string random",
			"RPRINT",
			"UWAAAA",
			"ASSIGN d '1234ABC'",
			"ASSIGN d 'HelloWorld'",
			"ASSIGN d 'Test123'",
			"BEGIN",
			"LOOKUP d",
			"ASSIGN d '1234ABC'",
			"LOOKUP d",
			"END",
		]
		expected = ["Invalid: INSERT d string random"]

		self.assertTrue(TestUtils.check(input, expected, 258))
	def test_259(self):
		input = [
			"BEGIN",
			"RPRINT",
			"ASSIGN a unimportant",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT c number",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN a unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 259))
	def test_260(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"LOOKUP y",
			"INSERT g_1 string",
			"ASSIGN y 'HelloWorld'",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT c number",
			"LOOKUP c",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["", "", "success", "2", "success", "success", "g_1//2 y//2", "y//2 g_1//2", "success", "1"]

		self.assertTrue(TestUtils.check(input, expected, 260))
	def test_261(self):
		input = [
			"RPRINT",
			"INSERT y string",
			"INSERT e_123_2r string",
			"PRINT",
			"INSERT f_FF number",
			"ASSIGN f_FF 1001",
			"BEGIN",
			"INSERT a number",
			"ASSIGN f_FF 789",
			"INSERT z number",
			"RPRINT",
			"INSERT x number",
			"RPRINT",
			"LOOKUP e_123_2r",
			"PRINT",
			"LOOKUP d",
			"LOOKUP y",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 261))
	def test_262(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT a string random",
			"LOOKUP a",
			"ASSIGN a 'HelloWorld'",
			"INSERT b string",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT a string random"]

		self.assertTrue(TestUtils.check(input, expected, 262))
	def test_263(self):
		input = [
			"RPRINT",
			"INSERT 1xyz 123",
			"INSERT y string random",
			"INSERT a number",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT y number",
			"ASSIGN y 'ab c",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN x 'ab c",
			"INSERT e_123_2r string",
			"UWAAAA",
			"PRINT",
			"END",
			"END",
			"PRINT",
			"ASSIGN a 1001",
			"BEGIN",
			"LOOKUP y",
			"PRINT",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 263))
	def test_264(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 264))
	def test_265(self):
		input = [
			"PRINT",
			"PRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 265))
	def test_266(self):
		input = [
			"BEGIN",
			"INSERT b number",
			"RPRINT",
			"INSERT a string",
			"PRINT",
			"END",
		]
		expected = ["success", "b//1", "success", "b//1 a//1"]

		self.assertTrue(TestUtils.check(input, expected, 266))
	def test_267(self):
		input = [
			"PRINT",
			"INSERT b string",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT a string",
			"BEGIN",
			"LOOKUP a",
			"RPRINT",
			"LOOKUP a",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 267))
	def test_268(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
			"END",
			"END",
			"END",
			"BEGIN",
			"INSERT f_FF string",
			"INSERT b number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 268))
	def test_269(self):
		input = [
			"INSERT e_123_2r string",
			"INSERT g_1 number",
			"PRINT",
			"INSERT x number",
			"INSERT b number",
			"ASSIGN e_123_2r 'HelloWorld'",
			"ASSIGN g_1 789",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT y string",
			"LOOKUP g_1",
			"RPRINT",
			"END",
			"END",
			"INSERT b number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 269))
	def test_270(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT g_1 number",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
			"INSERT d number",
			"END",
			"INSERT y_12@! 123",
			"END",
			"INSERT _@_$$d 123",
			"RPRINT",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 270))
	def test_271(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"END",
			"RPRINT",
			"INSERT g_1 string",
			"PRINT",
			"RPRINT",
			"ASSIGN g_1 'HelloWorld'",
			"END",
			"PRINT",
			"INSERT c string",
			"INSERT b string",
			"LOOKUP c",
		]
		expected = ["", "success", "2", "", "success", "g_1//1", "g_1//1", "success", "", "success", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 271))
	def test_272(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT y number",
			"BEGIN",
			"PRINT",
			"LOOKUP y",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT x string",
			"ASSIGN x 'HelloWorld'",
			"PRINT",
			"LOOKUP y",
			"ASSIGN y 'abcABC'",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"PRINT",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN y 'abcABC'"]

		self.assertTrue(TestUtils.check(input, expected, 272))
	def test_273(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 273))
	def test_274(self):
		input = [
			"RPRINT random",
			"RPRINT",
			"UWAAAA",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 274))
	def test_275(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r number",
			"INSERT c number",
			"INSERT y_12@! 123",
			"END",
		]
		expected = ["Invalid: INSERT y_12@! 123"]

		self.assertTrue(TestUtils.check(input, expected, 275))
	def test_276(self):
		input = [
			"INSERT z string",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT g_1 string",
			"INSERT b string",
			"LOOKUP b",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 276))
	def test_277(self):
		input = [
			"END",
			"INSERT b number",
			"ASSIGN b 456",
			"INSERT x number",
			"ASSIGN x 123",
			"INSERT d number",
			"BEGIN",
			"LOOKUP x",
			"ASSIGN b 789",
			"PRINT",
			"END",
			"LOOKUP b",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 277))
	def test_278(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT a number",
			"ASSIGN a 1001",
			"INSERT y string",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 278))
	def test_279(self):
		input = [
			"INSERT y string",
			"LOOKUP y",
			"LOOKUP y",
			"INSERT f_FF string",
			"ASSIGN y 'UPPERlower'",
			"LOOKUP f_FF",
			"PRINT",
			"INSERT a string random",
			"PRINT",
			"LOOKUP a",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r number",
			"INSERT x number",
			"INSERT d string",
			"LOOKUP y random",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT a string random"]

		self.assertTrue(TestUtils.check(input, expected, 279))
	def test_280(self):
		input = [
			"INSERT y number",
			"RPRINT",
			"RPRINT",
			"INSERT y string",
			"PRINT",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"END",
			"INSERT x string",
			"ASSIGN x 'HelloWorld'",
			"PRINT",
			"INSERT f_FF string",
			"INSERT c string",
			"INSERT d string",
			"INSERT z string",
			"INSERT g_1 number random",
			"ASSIGN c 'Test123'",
			"RPRINT",
			"BEGIN",
			"LOOKUP c",
			"END",
		]
		expected = ["Redeclared: INSERT y string"]

		self.assertTrue(TestUtils.check(input, expected, 280))
	def test_281(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT g_1 string",
			"PRINT",
			"LOOKUP g_1",
			"PRINT",
			"BEGIN",
			"END random",
			"BEGIN",
			"ASSIGN g_1 'Test123'",
			"END",
			"BEGIN",
			"ASSIGN g_1 '1234ABC'",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN g_1 '1234ABC'",
			"END",
			"INSERT f_FF string",
			"END",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 281))
	def test_282(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"LOOKUP a",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"INSERT c string",
			"INSERT e_123_2r number",
			"LOOKUP c",
			"END",
			"INSERT y string",
			"ASSIGN y 'Test123'",
			"LOOKUP y",
			"BEGIN",
			"ASSIGN y 'HelloWorld'",
			"ASSIGN f_FF unimportant",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 282))
	def test_283(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 283))
	def test_284(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"INSERT c string",
			"END",
		]
		expected = ["", "", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 284))
	def test_285(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"INSERT y number",
			"END",
			"LOOKUP y",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 285))
	def test_286(self):
		input = [
			"PRINT",
			"INSERT g_1 number",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 1001",
			"LOOKUP b",
			"END",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 286))
	def test_287(self):
		input = [
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"INSERT d string",
			"LOOKUP d",
			"BEGIN",
			"ASSIGN d 'HelloWorld'",
			"PRINT",
			"PRINT",
			"LOOKUP d",
			"INSERT z string",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 287))
	def test_288(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT z string",
			"BEGIN",
			"LOOKUP z",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT e_123_2r number",
			"END",
			"ASSIGN z 'UPPERlower'",
			"END",
		]
		expected = ["", "", "", "", "", "", "", "success", "1", "z//1", "z//1", "z//1", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 288))
	def test_289(self):
		input = [
			"END",
			"INSERT x number",
			"INSERT a string",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT d string",
			"BEGIN",
			"INSERT z number",
			"PRINT random",
			"LOOKUP d",
			"PRINT",
			"INSERT a string",
			"LOOKUP z",
			"PRINT",
			"INSERT g_1 string",
			"END random",
			"INSERT e_123_2r number",
			"ASSIGN x unimportant",
			"LOOKUP a",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 289))
	def test_290(self):
		input = [
			"INSERT f_FF string",
			"BEGIN",
			"RPRINT",
			"ASSIGN f_FF 'abc! 1'",
			"LOOKUP c",
			"LOOKUP f_FF",
			"ASSIGN f_FF 'ab c",
			"END",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT x number",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"ASSIGN x 1001",
			"RPRINT",
			"LOOKUP x",
		]
		expected = ["Invalid: ASSIGN f_FF 'abc! 1'"]

		self.assertTrue(TestUtils.check(input, expected, 290))
	def test_291(self):
		input = [
			"INSERT f_FF number",
			"PRINT",
			"INSERT b string",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT a number",
			"BEGIN",
			"LOOKUP a",
			"PRINT",
			"PRINT",
			"PRINT random",
			"INSERT b string",
			"INSERT e_123_2r string",
			"BEGIN",
			"END",
			"LOOKUP a",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 291))
	def test_292(self):
		input = [
			"BEGIN",
			"INSERT g_1 string",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 292))
	def test_293(self):
		input = [
			"BEGIN",
			"INSERT b number",
			"ASSIGN b 1001",
			"BEGIN",
			"INSERT z number",
			"END",
			"END",
		]
		expected = ["success", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 293))
	def test_294(self):
		input = [
			"PRINT",
			"INSERT d number",
			"LOOKUP d",
			"BEGIN",
			"INSERT a number",
			"END",
			"PRINT",
			"INSERT g_1 number",
		]
		expected = ["", "success", "0", "success", "d//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 294))
	def test_295(self):
		input = [
			"PRINT",
			"PRINT",
			"ASSIGN e_123_2r unimportant",
			"RPRINT random",
			"INSERT f_FF number",
			"LOOKUP c",
			"PRINT",
			"PRINT",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 295))
	def test_296(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT f_FF number",
			"RPRINT",
			"LOOKUP f_FF",
			"UWAAAA",
			"INSERT g_1 string",
			"END",
			"PRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 296))
	def test_297(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"INSERT e_123_2r string",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 297))
	def test_298(self):
		input = [
			"RPRINT",
			"INSERT d number",
			"LOOKUP d",
			"INSERT c string",
			"LOOKUP c",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"INSERT b number",
			"INSERT x string",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"UWAAAA",
			"INSERT d string",
			"LOOKUP d",
			"ASSIGN d 'HelloWorld'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 298))
	def test_299(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT x number",
			"LOOKUP x",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"INSERT f_FF string random",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"LOOKUP f_FF",
			"PRINT",
			"LOOKUP f_FF",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 299))
	def test_300(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT c number",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["", "", "", "", "", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 300))
	def test_301(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 301))
	def test_302(self):
		input = [
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 302))
	def test_303(self):
		input = [
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 303))
	def test_304(self):
		input = [
			"BEGIN",
			"END",
			"RPRINT",
			"INSERT x number",
			"PRINT",
			"INSERT e_123_2r number",
			"BEGIN",
			"LOOKUP x",
			"RPRINT",
			"LOOKUP x",
			"END",
		]
		expected = ["", "success", "x//0", "success", "0", "e_123_2r//0 x//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 304))
	def test_305(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"LOOKUP d",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"ASSIGN z '1234ABC'",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 305))
	def test_306(self):
		input = [
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r string",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 306))
	def test_307(self):
		input = [
			"END",
			"INSERT g_1 number",
			"UWAAAA",
			"LOOKUP g_1",
			"PRINT",
			"PRINT random",
			"INSERT x string",
			"ASSIGN g_1 987654",
			"LOOKUP g_1",
			"RPRINT",
			"LOOKUP x",
			"ASSIGN __ g 123",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 307))
	def test_308(self):
		input = [
			"END",
			"END",
			"INSERT d string",
			"ASSIGN d '@stArt'",
			"ASSIGN d 'UPPERlower'",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
			"UWAAAA",
			"INSERT z string",
			"LOOKUP z",
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 308))
	def test_309(self):
		input = [
			"INSERT b string",
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"ASSIGN b 'a@bc'",
			"RPRINT",
			"PRINT",
			"ASSIGN b 'abcABC'",
			"ASSIGN b 'UPPERlower'",
			"ASSIGN b 'Test123'",
			"END",
			"UWAAAA",
			"END",
			"END",
			"BEGIN",
			"INSERT a number",
			"PRINT",
			"PRINT",
			"ASSIGN a 987654",
			"BEGIN",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: ASSIGN b 'a@bc'"]

		self.assertTrue(TestUtils.check(input, expected, 309))
	def test_310(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 310))
	def test_311(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 311))
	def test_312(self):
		input = [
			"RPRINT",
			"INSERT z number",
			"INSERT x number random",
			"LOOKUP z",
			"ASSIGN _@_$$d 123",
			"BEGIN",
			"LOOKUP z",
			"END",
		]
		expected = ["Invalid: INSERT x number random"]

		self.assertTrue(TestUtils.check(input, expected, 312))
	def test_313(self):
		input = [
			"INSERT a string",
			"BEGIN",
			"PRINT",
			"LOOKUP a",
			"PRINT",
			"BEGIN",
			"ASSIGN a 'abcABC' random",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN a 'abcABC' random"]

		self.assertTrue(TestUtils.check(input, expected, 313))
	def test_314(self):
		input = [
			"BEGIN",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT c number",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["", "success", "b//1", "", "", "", "", "success", "c//2"]

		self.assertTrue(TestUtils.check(input, expected, 314))
	def test_315(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT e_123_2r string",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"INSERT c number",
			"RPRINT",
			"ASSIGN c 1001",
			"LOOKUP c",
			"PRINT",
			"END",
			"END",
		]
		expected = ["", "", "", "", "success", "e_123_2r//2", "e_123_2r//2", "e_123_2r//2", "success", "c//2 e_123_2r//2", "success", "2", "e_123_2r//2 c//2"]

		self.assertTrue(TestUtils.check(input, expected, 315))
	def test_316(self):
		input = [
			"PRINT",
			"PRINT random",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT z string",
			"ASSIGN z 'abcABC'",
			"PRINT",
			"LOOKUP z",
			"PRINT",
			"INSERT g_1 string",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"ASSIGN z 'abcABC'",
			"PRINT",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 316))
	def test_317(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT b string",
			"PRINT",
			"INSERT c number",
			"ASSIGN c 456",
			"BEGIN",
			"INSERT f_FF number",
			"RPRINT",
			"LOOKUP f_FF",
			"PRINT",
			"LOOKUP b",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"LOOKUP f_FF",
			"ASSIGN b 987654",
			"INSERT f_FF string",
			"BEGIN",
			"INSERT 21_3c 123",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN b 987654"]

		self.assertTrue(TestUtils.check(input, expected, 317))
	def test_318(self):
		input = [
			"END",
			"INSERT y string",
			"ASSIGN y 'HelloWorld'",
			"ASSIGN y 'abcABC'",
			"INSERT g_1 number",
			"BEGIN",
			"RPRINT",
			"LOOKUP g_1",
			"LOOKUP y",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT a string",
			"RPRINT",
			"END",
			"ASSIGN g_1 123.8.7",
			"ASSIGN y '1234ABC'",
			"INSERT c string",
			"BEGIN",
			"LOOKUP c",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"ASSIGN g_1 123",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 318))
	def test_319(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 319))
	def test_320(self):
		input = [
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 320))
	def test_321(self):
		input = [
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 321))
	def test_322(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"UWAAAA",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 322))
	def test_323(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT z string",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 323))
	def test_324(self):
		input = [
			"RPRINT",
			"ASSIGN c unimportant",
			"INSERT b number",
			"RPRINT",
			"RPRINT",
			"ASSIGN b 987654",
			"RPRINT",
			"INSERT f_FF string",
			"ASSIGN f_FF 'HelloWorld'",
			"BEGIN",
			"INSERT a number",
			"BEGIN",
			"PRINT",
			"ASSIGN b 789",
			"END",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 324))
	def test_325(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT f_FF string",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["", "", "", "success", "f_FF//3"]

		self.assertTrue(TestUtils.check(input, expected, 325))
	def test_326(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"ASSIGN d unimportant",
			"INSERT e_123_2r string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 326))
	def test_327(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT y number",
			"PRINT",
			"INSERT d number",
			"ASSIGN d 789",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT y string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 327))
	def test_328(self):
		input = [
			"END",
			"PRINT",
			"INSERT b number",
			"RPRINT",
			"BEGIN",
			"LOOKUP b",
			"BEGIN",
			"ASSIGN b 987654",
			"RPRINT",
			"BEGIN random",
			"LOOKUP g_1",
			"LOOKUP b",
			"PRINT",
			"RPRINT",
			"LOOKUP b",
			"RPRINT",
			"END",
			"BEGIN",
			"LOOKUP b",
			"ASSIGN b 1001",
			"ASSIGN b 1001",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"ASSIGN b 789",
			"END",
			"INSERT c number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 328))
	def test_329(self):
		input = [
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 329))
	def test_330(self):
		input = [
			"INSERT c number",
			"BEGIN",
			"END",
			"ASSIGN c 1001",
			"LOOKUP c",
			"LOOKUP c",
		]
		expected = ["success", "success", "0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 330))
	def test_331(self):
		input = [
			"PRINT",
			"RPRINT",
			"INSERT y number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 331))
	def test_332(self):
		input = [
			"INSERT e_123_2r string",
			"INSERT d string",
			"RPRINT",
			"ASSIGN d 'HelloWorld'",
			"RPRINT",
			"ASSIGN e_123_2r 123",
			"RPRINT",
			"LOOKUP d",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN e_123_2r 123"]

		self.assertTrue(TestUtils.check(input, expected, 332))
	def test_333(self):
		input = [
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"UWAAAA",
			"ASSIGN aak e 123",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 333))
	def test_334(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"INSERT c string",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"INSERT d number",
			"ASSIGN d 1001",
			"RPRINT",
			"RPRINT",
			"LOOKUP d",
			"BEGIN",
			"RPRINT",
			"INSERT y string",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 334))
	def test_335(self):
		input = [
			"RPRINT",
			"INSERT y string",
			"PRINT",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"END",
			"PRINT",
			"LOOKUP y",
			"INSERT c number",
			"BEGIN",
			"UWAAAA",
			"INSERT a number",
			"INSERT y string",
			"BEGIN",
			"PRINT",
			"LOOKUP a",
			"PRINT",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 335))
	def test_336(self):
		input = [
			"INSERT g_1 number",
			"ASSIGN g_1 1001",
			"PRINT",
			"RPRINT",
			"LOOKUP g_1",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN random",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 336))
	def test_337(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT c string",
			"BEGIN",
			"ASSIGN c 'Test123'",
			"INSERT a number",
			"BEGIN",
			"END",
			"PRINT",
			"INSERT c number",
			"ASSIGN a 789",
			"UWAAAA",
			"ASSIGN c 987654",
			"ASSIGN b@B((*@ 123",
			"INSERT a number",
			"BEGIN",
			"ASSIGN a abc123",
			"ASSIGN c 1001",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 337))
	def test_338(self):
		input = [
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 338))
	def test_339(self):
		input = [
			"PRINT",
			"INSERT __ g 123",
			"INSERT g_1 number",
			"INSERT a string",
		]
		expected = ["Invalid: INSERT __ g 123"]

		self.assertTrue(TestUtils.check(input, expected, 339))
	def test_340(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"INSERT f_FF number",
			"BEGIN",
			"END",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 340))
	def test_341(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"PRINT",
			"LOOKUP e_123_2r",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"ASSIGN e_123_2r 987654",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 341))
	def test_342(self):
		input = [
			"INSERT c string",
			"LOOKUP c",
			"END",
			"INSERT g_1 number",
			"RPRINT",
			"RPRINT",
			"ASSIGN g_1 987654",
			"ASSIGN g_1 1001",
			"LOOKUP g_1",
			"INSERT g_1 string",
			"PRINT",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 342))
	def test_343(self):
		input = [
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"BEGIN",
			"LOOKUP e_123_2r",
			"LOOKUP e_123_2r",
			"RPRINT",
			"LOOKUP e_123_2r",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"LOOKUP e_123_2r",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["success", "0", "0", "0", "e_123_2r//0", "0", "0", "e_123_2r//0", "e_123_2r//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 343))
	def test_344(self):
		input = [
			"PRINT",
			"END",
			"INSERT z number",
			"LOOKUP z",
			"INSERT g_1 number",
			"LOOKUP z",
			"BEGIN",
			"ASSIGN a unimportant",
			"RPRINT",
			"INSERT b string",
			"END",
			"BEGIN",
			"ASSIGN g_1 'Test123'",
			"RPRINT",
			"RPRINT",
			"ASSIGN z 456",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 344))
	def test_345(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT z number",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT random",
			"INSERT _@??e 123",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT a string",
			"RPRINT",
			"ASSIGN 1xyz 123",
			"END",
			"ASSIGN b unimportant",
			"PRINT",
			"END",
			"PRINT random",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 345))
	def test_346(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"PRINT",
			"RPRINT",
			"ASSIGN f_FF 'abcABC'",
			"END",
			"INSERT g_1 string",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 346))
	def test_347(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 347))
	def test_348(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT f_FF number",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 348))
	def test_349(self):
		input = [
			"PRINT",
			"END",
			"END",
			"BEGIN",
			"INSERT d number",
			"LOOKUP e_123_2r",
			"PRINT",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 349))
	def test_350(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN random",
			"BEGIN",
			"PRINT",
			"INSERT d number",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"INSERT a number",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 350))
	def test_351(self):
		input = [
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"LOOKUP x random",
			"PRINT",
			"INSERT b number",
			"LOOKUP b random",
			"LOOKUP b",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 351))
	def test_352(self):
		input = [
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"ASSIGN f_FF unimportant",
			"UWAAAA",
			"RPRINT",
			"END",
			"END",
			"UWAAAA",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 352))
	def test_353(self):
		input = [
			"INSERT z number",
			"BEGIN",
			"BEGIN",
			"LOOKUP z",
			"LOOKUP z",
			"LOOKUP z",
			"LOOKUP z",
			"END",
			"BEGIN",
			"ASSIGN z 1001",
			"PRINT",
			"BEGIN",
			"ASSIGN z 123",
			"BEGIN",
			"INSERT b number",
			"LOOKUP z random",
			"PRINT",
			"RPRINT",
			"END",
			"LOOKUP z",
			"INSERT e_123_2r string",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: LOOKUP z random"]

		self.assertTrue(TestUtils.check(input, expected, 353))
	def test_354(self):
		input = [
			"RPRINT",
			"PRINT",
			"LOOKUP x",
			"INSERT b string",
			"INSERT x string",
			"END",
			"INSERT b string",
			"LOOKUP b",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"ASSIGN b 'UPPERlower'",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r 'abcABC'",
			"LOOKUP b",
			"BEGIN",
			"ASSIGN b 'abcABC'",
			"END",
			"ASSIGN e_123_2r 987654",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 354))
	def test_355(self):
		input = [
			"END",
			"RPRINT",
			"INSERT d string",
			"INSERT 21_3c 123",
			"BEGIN",
			"BEGIN",
			"LOOKUP d",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP d",
			"INSERT a string",
			"ASSIGN a '1234ABC'",
			"PRINT",
			"INSERT e_123_2r number",
			"INSERT b string",
			"RPRINT",
			"LOOKUP d",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"LOOKUP b",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 355))
	def test_356(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 356))
	def test_357(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 357))
	def test_358(self):
		input = [
			"END random",
			"BEGIN",
			"PRINT",
			"PRINT",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 358))
	def test_359(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 359))
	def test_360(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"END random",
			"INSERT z string random",
			"INSERT f_FF number",
			"ASSIGN z '1234ABC'",
			"END",
			"END",
			"BEGIN",
			"INSERT b number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 360))
	def test_361(self):
		input = [
			"END",
			"PRINT",
			"END",
			"INSERT c string",
			"ASSIGN c 'UPPERlower'",
			"ASSIGN x unimportant",
			"LOOKUP c",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"RPRINT",
			"ASSIGN c 'abcABC'",
			"ASSIGN c 'Test123'",
			"END",
			"ASSIGN c 'HelloWorld'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 361))
	def test_362(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT d string",
			"PRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"ASSIGN d '1234ABC'",
			"RPRINT",
			"LOOKUP d",
			"INSERT e_123_2r number",
			"RPRINT",
			"RPRINT",
			"ASSIGN d 'UPPERlower'",
			"RPRINT",
		]
		expected = ["", "", "success", "d//0", "d//0", "d//0", "d//0", "d//0", "d//0", "d//0", "success", "d//0", "0", "success", "e_123_2r//0 d//0", "e_123_2r//0 d//0", "success", "e_123_2r//0 d//0"]

		self.assertTrue(TestUtils.check(input, expected, 362))
	def test_363(self):
		input = [
			"INSERT e_123_2r string",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END random",
			"INSERT f_FF number",
			"PRINT",
			"PRINT",
			"INSERT a number",
			"RPRINT",
			"END",
			"INSERT y number",
			"END",
			"UWAAAA",
			"INSERT d number",
			"PRINT",
			"BEGIN",
			"INSERT a string",
			"BEGIN",
			"RPRINT",
			"LOOKUP d",
			"BEGIN random",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 363))
	def test_364(self):
		input = [
			"INSERT b number",
			"ASSIGN b 'Test123'",
			"PRINT",
			"ASSIGN b 1001",
			"INSERT z number",
			"RPRINT",
			"RPRINT",
			"ASSIGN b 789",
			"LOOKUP b",
			"LOOKUP z",
			"INSERT a string",
			"RPRINT",
			"LOOKUP z",
			"BEGIN",
			"ASSIGN a 'abcABC'",
			"LOOKUP a",
			"UWAAAA",
			"END",
			"ASSIGN z 987654",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"ASSIGN b 123",
			"BEGIN",
			"ASSIGN b 789",
			"INSERT a number random",
		]
		expected = ["TypeMismatch: ASSIGN b 'Test123'"]

		self.assertTrue(TestUtils.check(input, expected, 364))
	def test_365(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 365))
	def test_366(self):
		input = [
			"INSERT a number",
			"ASSIGN a 1001",
		]
		expected = ["success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 366))
	def test_367(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 number",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["", "", "success", "g_1//1", "g_1//1"]

		self.assertTrue(TestUtils.check(input, expected, 367))
	def test_368(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN random",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 368))
	def test_369(self):
		input = [
			"INSERT f_FF string",
			"INSERT y string",
			"ASSIGN f_FF 'HelloWorld'",
			"RPRINT",
			"PRINT",
			"ASSIGN f_FF 'Test123'",
			"ASSIGN y 'UPPERlower'",
			"PRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN y 987654",
			"ASSIGN f_FF '1234ABC'",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN y 987654"]

		self.assertTrue(TestUtils.check(input, expected, 369))
	def test_370(self):
		input = [
			"BEGIN",
			"ASSIGN g_1 unimportant",
			"END random",
			"INSERT a string",
			"ASSIGN a 'abcABC'",
			"UWAAAA",
			"END",
			"END",
			"PRINT",
		]
		expected = ["Undeclared: ASSIGN g_1 unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 370))
	def test_371(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT f_FF string",
			"INSERT d string",
			"INSERT d number",
			"INSERT x string",
			"PRINT",
			"INSERT g_1 string",
			"END",
			"ASSIGN f_FF unimportant",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 371))
	def test_372(self):
		input = [
			"END",
			"INSERT f_FF number",
			"UWAAAA",
			"LOOKUP f_FF",
			"BEGIN",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"INSERT d number",
			"ASSIGN b unimportant",
			"PRINT",
			"END",
			"INSERT x number",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 372))
	def test_373(self):
		input = [
			"INSERT f_FF string",
			"BEGIN",
			"INSERT z string",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"LOOKUP z",
			"BEGIN",
			"ASSIGN z 'Test123'",
			"LOOKUP f_FF",
			"RPRINT",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP z",
			"ASSIGN e_123_2r '1234ABC'",
			"ASSIGN z 'UPPERlower'",
			"LOOKUP f_FF",
			"INSERT z string",
			"RPRINT",
			"LOOKUP f_FF",
			"RPRINT",
			"LOOKUP z",
			"INSERT f_FF number",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["success", "success", "1", "success", "0", "z//1 f_FF//0", "success", "1", "success", "success", "0", "success", "z//4 e_123_2r//4 f_FF//0", "0", "z//4 e_123_2r//4 f_FF//0", "4", "success", "f_FF//4 z//4 e_123_2r//4", "f_FF//4 z//4 e_123_2r//4", "f_FF//4 z//4 e_123_2r//4"]

		self.assertTrue(TestUtils.check(input, expected, 373))
	def test_374(self):
		input = [
			"INSERT y number random",
			"PRINT",
			"INSERT z number",
			"INSERT d number",
			"ASSIGN z 789",
			"ASSIGN y 'UPPERlower'",
			"INSERT x number",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"INSERT f_FF string",
			"RPRINT",
			"PRINT",
			"LOOKUP f_FF",
			"RPRINT",
			"INSERT g_1 number",
			"BEGIN",
			"PRINT",
			"BEGIN random",
			"RPRINT",
			"RPRINT",
			"INSERT b number",
			"PRINT",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT y number random"]

		self.assertTrue(TestUtils.check(input, expected, 374))
	def test_375(self):
		input = [
			"INSERT g_1 number",
			"INSERT _@_$$d 123",
			"INSERT a number",
		]
		expected = ["Invalid: INSERT _@_$$d 123"]

		self.assertTrue(TestUtils.check(input, expected, 375))
	def test_376(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 376))
	def test_377(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 377))
	def test_378(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT z string",
			"LOOKUP z",
			"BEGIN",
			"END",
			"BEGIN",
			"ASSIGN z 'abcABC'",
			"BEGIN",
			"ASSIGN z 'Test123'",
			"END",
			"END",
		]
		expected = ["", "", "", "", "success", "0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 378))
	def test_379(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"UWAAAA",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 379))
	def test_380(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT c number",
			"LOOKUP c",
			"ASSIGN c 987654",
			"RPRINT",
			"INSERT x number",
			"INSERT x string",
			"ASSIGN z unimportant",
			"INSERT f_FF string",
			"LOOKUP x",
			"ASSIGN c 123",
			"LOOKUP f_FF",
			"INSERT y string",
			"LOOKUP f_FF",
			"BEGIN",
			"INSERT e_123_2r number",
			"PRINT",
			"END",
		]
		expected = ["Redeclared: INSERT x string"]

		self.assertTrue(TestUtils.check(input, expected, 380))
	def test_381(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT y_12@! 123",
			"END",
			"BEGIN",
			"INSERT x number",
			"INSERT a number",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT _@_$$d 123",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT y_12@! 123"]

		self.assertTrue(TestUtils.check(input, expected, 381))
	def test_382(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"INSERT z string random",
			"INSERT z number",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"LOOKUP z",
			"END",
			"BEGIN",
			"INSERT a string",
			"ASSIGN a '1234ABC'",
			"RPRINT",
			"BEGIN",
			"LOOKUP a",
			"RPRINT",
			"LOOKUP z",
			"LOOKUP a",
			"ASSIGN z 'HelloWorld'",
			"LOOKUP z",
			"END",
			"BEGIN",
			"ASSIGN z 'abcABC'",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 382))
	def test_383(self):
		input = [
			"PRINT",
			"BEGIN",
			"END",
			"INSERT a number",
			"INSERT z number",
			"LOOKUP a",
			"INSERT e_123_2r string",
			"PRINT random",
			"INSERT b string",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"ASSIGN a unimportant",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT f_FF number",
			"INSERT c string",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"INSERT z string",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 383))
	def test_384(self):
		input = [
			"INSERT a string",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 384))
	def test_385(self):
		input = [
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"INSERT y number",
			"ASSIGN f_FF 987654",
			"BEGIN",
			"END",
		]
		expected = ["success", "0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 385))
	def test_386(self):
		input = [
			"INSERT x string",
			"RPRINT",
			"BEGIN",
			"END",
			"LOOKUP x",
			"BEGIN",
			"ASSIGN x 'UPPERlower'",
			"LOOKUP x",
			"PRINT",
			"END",
		]
		expected = ["success", "x//0", "0", "success", "0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 386))
	def test_387(self):
		input = [
			"BEGIN",
			"PRINT",
			"INSERT x string",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT f_FF number",
			"ASSIGN f_FF 789",
			"PRINT",
			"ASSIGN f_FF 1001",
			"ASSIGN f_FF 1001",
		]
		expected = ["", "success", "x//1", "x//1", "success", "success", "f_FF//0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 387))
	def test_388(self):
		input = [
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"INSERT c number",
			"INSERT x string",
			"INSERT f_FF string",
			"BEGIN",
			"BEGIN",
			"ASSIGN f_FF 'HelloWorld'",
			"RPRINT",
			"INSERT 21_3c 123",
			"LOOKUP x random",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 388))
	def test_389(self):
		input = [
			"RPRINT",
			"INSERT e_123_2r string",
			"INSERT b string",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"ASSIGN e_123_2r 'Test123'",
			"PRINT",
			"PRINT",
			"INSERT z string",
			"INSERT e_123_2r number",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"UWAAAA",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 389))
	def test_390(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 390))
	def test_391(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT random",
			"END",
			"INSERT e_123_2r string",
			"PRINT",
			"ASSIGN e_123_2r 'abcABC'",
			"END",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"ASSIGN g_1 456",
			"PRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 391))
	def test_392(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"INSERT d string",
			"END",
			"BEGIN",
			"INSERT x number",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 392))
	def test_393(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 393))
	def test_394(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 394))
	def test_395(self):
		input = [
			"INSERT d number",
			"INSERT y number",
			"LOOKUP y",
			"INSERT a string",
			"PRINT",
			"PRINT",
			"INSERT c string random",
			"RPRINT",
		]
		expected = ["Invalid: INSERT c string random"]

		self.assertTrue(TestUtils.check(input, expected, 395))
	def test_396(self):
		input = [
			"INSERT a number",
			"BEGIN",
			"INSERT z string",
			"BEGIN",
			"LOOKUP a",
			"ASSIGN d unimportant",
			"END",
			"INSERT x string",
			"INSERT x number",
			"ASSIGN a 123",
			"UWAAAA",
		]
		expected = ["Undeclared: ASSIGN d unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 396))
	def test_397(self):
		input = [
			"INSERT c string",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN c 'abcABC'",
			"RPRINT",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 987654",
			"INSERT a string",
			"UWAAAA",
			"RPRINT",
			"LOOKUP a",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 397))
	def test_398(self):
		input = [
			"BEGIN",
			"INSERT d number",
			"ASSIGN d 123",
			"LOOKUP d",
			"RPRINT",
			"END random",
			"BEGIN",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"INSERT _@??e 123",
			"END",
			"LOOKUP g_1",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 398))
	def test_399(self):
		input = [
			"BEGIN",
			"INSERT z string",
			"PRINT",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
		]
		expected = ["success", "z//1", "", "", "", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 399))
	def test_400(self):
		input = [
			"PRINT",
			"INSERT d number",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN b unimportant",
			"BEGIN",
			"INSERT y string",
			"INSERT f_FF number",
			"PRINT",
			"BEGIN",
			"INSERT z string",
			"END",
			"RPRINT",
			"LOOKUP d",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT e_123_2r number",
		]
		expected = ["Undeclared: ASSIGN b unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 400))
	def test_401(self):
		input = [
			"RPRINT",
			"INSERT z number",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"LOOKUP e_123_2r",
			"ASSIGN g_1 unimportant random",
			"LOOKUP z",
			"PRINT",
			"RPRINT",
			"LOOKUP e_123_2r",
			"BEGIN",
			"PRINT",
			"INSERT z number",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT z string",
			"BEGIN",
			"ASSIGN e_123_2r '1234ABC'",
			"ASSIGN e_123_2r 'abcABC'",
			"LOOKUP e_123_2r random",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN g_1 unimportant random"]

		self.assertTrue(TestUtils.check(input, expected, 401))
	def test_402(self):
		input = [
			"ASSIGN x unimportant",
		]
		expected = ["Undeclared: ASSIGN x unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 402))
	def test_403(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 403))
	def test_404(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 404))
	def test_405(self):
		input = [
			"END",
			"INSERT f_FF string",
			"BEGIN",
			"LOOKUP y",
			"LOOKUP f_FF",
			"BEGIN",
			"INSERT c string",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 405))
	def test_406(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"ASSIGN d unimportant",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 406))
	def test_407(self):
		input = [
			"INSERT d string",
			"ASSIGN f_FF unimportant",
			"BEGIN",
			"ASSIGN d 'Test123'",
			"PRINT",
			"END",
			"BEGIN",
			"LOOKUP d",
			"PRINT",
			"BEGIN",
			"ASSIGN d '1234ABC'",
			"RPRINT",
			"LOOKUP d",
			"ASSIGN d 'HelloWorld'",
			"INSERT z string",
			"END",
			"INSERT 21_3c 123",
			"END",
		]
		expected = ["Undeclared: ASSIGN f_FF unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 407))
	def test_408(self):
		input = [
			"INSERT z string",
			"LOOKUP d",
			"INSERT a number",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"LOOKUP z",
			"LOOKUP c",
			"INSERT c number",
			"INSERT b number",
			"LOOKUP z",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 408))
	def test_409(self):
		input = [
			"BEGIN",
			"END",
			"INSERT f_FF number",
			"ASSIGN f_FF 123a",
			"ASSIGN f_FF 987654",
			"RPRINT random",
			"INSERT c number",
			"END",
			"END",
			"INSERT b number",
			"ASSIGN b 123",
			"ASSIGN b 789",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"ASSIGN e_123_2r unimportant",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
		]
		expected = ["Invalid: ASSIGN f_FF 123a"]

		self.assertTrue(TestUtils.check(input, expected, 409))
	def test_410(self):
		input = [
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"LOOKUP z",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT random",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP z"]

		self.assertTrue(TestUtils.check(input, expected, 410))
	def test_411(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 411))
	def test_412(self):
		input = [
			"PRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r 'UPPERlower'",
		]
		expected = ["", "", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 412))
	def test_413(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 413))
	def test_414(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"ASSIGN g_1 456",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"RPRINT",
			"END",
		]
		expected = ["", "success", "1", "success", "1", "1", "g_1//1"]

		self.assertTrue(TestUtils.check(input, expected, 414))
	def test_415(self):
		input = [
			"UWAAAA",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"INSERT a string",
			"PRINT",
			"RPRINT",
			"LOOKUP a",
			"RPRINT",
			"UWAAAA",
			"ASSIGN a 'Test123'",
			"ASSIGN a 'Test123'",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 415))
	def test_416(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT random",
			"INSERT f_FF number",
			"INSERT x string",
			"END",
			"BEGIN",
			"END",
			"END",
			"INSERT x number",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"INSERT a number",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 416))
	def test_417(self):
		input = [
			"RPRINT",
			"LOOKUP d",
			"END",
			"BEGIN",
			"RPRINT",
			"INSERT x number",
			"END",
			"BEGIN",
			"INSERT g_1 string",
			"BEGIN",
			"INSERT a string",
			"LOOKUP g_1",
			"ASSIGN a 'HelloWorld'",
			"ASSIGN a 'HelloWorld'",
			"END",
			"INSERT a number",
			"RPRINT",
			"INSERT d number",
			"ASSIGN a 123.8.7",
			"ASSIGN d 987654",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 417))
	def test_418(self):
		input = [
			"INSERT e_123_2r string",
			"INSERT f_FF number",
			"RPRINT",
			"ASSIGN f_FF 789",
			"PRINT",
			"INSERT d number",
			"RPRINT",
			"ASSIGN e_123_2r 'Test123'",
			"RPRINT",
			"ASSIGN f_FF 123",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT d number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 418))
	def test_419(self):
		input = [
			"INSERT b string",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"LOOKUP b",
			"END",
			"END",
			"LOOKUP b",
			"INSERT x string",
			"BEGIN",
			"LOOKUP b",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN x '1234ABC'",
			"LOOKUP x",
			"RPRINT",
			"INSERT z number",
			"ASSIGN x 'Test123'",
			"INSERT b number",
			"PRINT",
			"ASSIGN x '1234ABC'",
			"BEGIN",
			"LOOKUP z",
			"INSERT a number random",
			"END",
		]
		expected = ["Redeclared: INSERT b number"]

		self.assertTrue(TestUtils.check(input, expected, 419))
	def test_420(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 420))
	def test_421(self):
		input = [
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 421))
	def test_422(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 422))
	def test_423(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 423))
	def test_424(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT b string",
			"LOOKUP b",
			"RPRINT",
			"LOOKUP b",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["", "", "", "success", "1", "b//1", "1", "b//1"]

		self.assertTrue(TestUtils.check(input, expected, 424))
	def test_425(self):
		input = [
			"END",
			"RPRINT",
			"INSERT y string",
			"INSERT d number random",
			"ASSIGN d 456",
			"END",
			"INSERT f_FF number",
			"RPRINT",
			"INSERT z number",
			"ASSIGN f_FF 1001",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 425))
	def test_426(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT g_1 number",
			"RPRINT",
			"INSERT f_FF string",
			"LOOKUP g_1",
			"INSERT x number",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"LOOKUP y",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 426))
	def test_427(self):
		input = [
			"PRINT",
			"INSERT b string",
			"END",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"END",
			"INSERT a string",
			"INSERT x string",
			"RPRINT",
			"LOOKUP a",
			"ASSIGN x 'abcABC'",
			"RPRINT",
			"RPRINT random",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"ASSIGN a 789",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 427))
	def test_428(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 1001",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN random",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"END",
			"RPRINT",
			"BEGIN",
			"LOOKUP z",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"ASSIGN f_FF unimportant",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 428))
	def test_429(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT d string",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 429))
	def test_430(self):
		input = [
			"INSERT g_1 number",
			"ASSIGN g_1 987654",
		]
		expected = ["success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 430))
	def test_431(self):
		input = [
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 431))
	def test_432(self):
		input = [
			"BEGIN",
			"INSERT d number",
			"PRINT",
			"ASSIGN d 987654",
			"INSERT e_123_2r number",
			"END",
		]
		expected = ["success", "d//1", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 432))
	def test_433(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"LOOKUP g_1",
			"BEGIN",
			"PRINT",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"PRINT",
			"INSERT x string",
			"END",
		]
		expected = ["Undeclared: LOOKUP g_1"]

		self.assertTrue(TestUtils.check(input, expected, 433))
	def test_434(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT g_1 number",
			"END",
			"BEGIN",
			"INSERT _@??e 123",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 434))
	def test_435(self):
		input = [
			"END",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT x string",
			"PRINT",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 435))
	def test_436(self):
		input = [
			"END",
			"INSERT d number random",
			"UWAAAA",
			"END",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"INSERT f_FF string",
			"INSERT y number",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 436))
	def test_437(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"INSERT y string",
			"LOOKUP y",
			"INSERT c number",
			"RPRINT",
			"INSERT d number",
			"RPRINT",
			"LOOKUP y",
			"ASSIGN d 1001",
			"LOOKUP c",
			"LOOKUP z",
			"ASSIGN y '1234ABC'",
			"END",
			"END random",
		]
		expected = ["Undeclared: LOOKUP z"]

		self.assertTrue(TestUtils.check(input, expected, 437))
	def test_438(self):
		input = [
			"INSERT x number",
			"INSERT e_123_2r string random",
			"LOOKUP x",
			"LOOKUP x",
			"RPRINT",
			"ASSIGN e_123_2r '1234ABC'",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 'HelloWorld' random",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: INSERT e_123_2r string random"]

		self.assertTrue(TestUtils.check(input, expected, 438))
	def test_439(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 439))
	def test_440(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 440))
	def test_441(self):
		input = [
			"RPRINT",
			"BEGIN",
			"INSERT z string",
			"INSERT a number",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
		]
		expected = ["", "success", "success", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 441))
	def test_442(self):
		input = [
			"BEGIN",
			"INSERT y_12@! 123",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"PRINT",
			"LOOKUP y",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT y_12@! 123"]

		self.assertTrue(TestUtils.check(input, expected, 442))
	def test_443(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT random",
			"RPRINT",
			"INSERT g_1 number",
			"RPRINT",
			"LOOKUP a",
			"ASSIGN g_1 789",
			"BEGIN",
			"INSERT y string",
			"END",
			"ASSIGN g_1 789",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 443))
	def test_444(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 444))
	def test_445(self):
		input = [
			"PRINT",
			"UWAAAA",
			"INSERT b string",
			"END",
			"END",
			"END",
			"INSERT f_FF number",
			"PRINT",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP f_FF",
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"ASSIGN f_FF 456",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 445))
	def test_446(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT d string",
			"BEGIN",
			"LOOKUP d",
			"LOOKUP d random",
			"INSERT c number",
			"PRINT",
			"BEGIN",
			"LOOKUP c",
			"BEGIN",
			"INSERT e_123_2r string",
			"BEGIN",
			"INSERT d string",
			"LOOKUP d",
			"BEGIN",
			"ASSIGN d 'abcABC'",
			"ASSIGN e_123_2r '1234ABC'",
			"PRINT",
			"BEGIN",
			"ASSIGN c 987654",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 446))
	def test_447(self):
		input = [
			"END",
			"END",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 447))
	def test_448(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 448))
	def test_449(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 449))
	def test_450(self):
		input = [
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"LOOKUP b",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 450))
	def test_451(self):
		input = [
			"RPRINT",
			"END",
			"PRINT",
			"INSERT g_1 number",
			"END",
			"RPRINT",
			"END",
			"INSERT x number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 451))
	def test_452(self):
		input = [
			"RPRINT",
			"BEGIN",
			"INSERT d string",
			"END",
			"INSERT g_1 number",
			"BEGIN",
			"END",
			"ASSIGN g_1 987654",
			"LOOKUP g_1",
			"ASSIGN g_1 123",
		]
		expected = ["", "success", "success", "success", "0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 452))
	def test_453(self):
		input = [
			"BEGIN random",
			"INSERT y number",
			"INSERT c string",
			"RPRINT",
			"PRINT",
			"END",
			"ASSIGN aak e 123",
			"PRINT",
			"PRINT",
			"INSERT z number",
			"END",
			"INSERT g_1 number",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 453))
	def test_454(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r number",
			"PRINT",
			"ASSIGN e_123_2r 789",
			"INSERT a string",
			"END",
			"RPRINT",
			"INSERT z number",
			"PRINT",
			"ASSIGN z 789",
			"INSERT d string",
			"INSERT f_FF number",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 454))
	def test_455(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT b number",
			"PRINT",
			"END",
			"INSERT a string",
			"PRINT",
			"LOOKUP y",
			"LOOKUP a",
			"INSERT d string",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"ASSIGN a 'HelloWorld'",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 455))
	def test_456(self):
		input = [
			"END",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT z string",
			"LOOKUP z",
			"BEGIN",
			"ASSIGN z '1234ABC'",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP z",
			"LOOKUP z",
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"ASSIGN z '1234ABC' random",
			"LOOKUP z",
			"RPRINT",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 456))
	def test_457(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 457))
	def test_458(self):
		input = [
			"INSERT b number",
			"INSERT e_123_2r string",
			"INSERT g_1 string",
			"PRINT",
		]
		expected = ["success", "success", "success", "b//0 e_123_2r//0 g_1//0"]

		self.assertTrue(TestUtils.check(input, expected, 458))
	def test_459(self):
		input = [
			"BEGIN",
			"UWAAAA",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 459))
	def test_460(self):
		input = [
			"INSERT y string",
			"PRINT",
			"RPRINT",
			"INSERT z number",
			"LOOKUP y",
			"ASSIGN y 'abcABC'",
			"RPRINT",
			"INSERT y string",
		]
		expected = ["Redeclared: INSERT y string"]

		self.assertTrue(TestUtils.check(input, expected, 460))
	def test_461(self):
		input = [
			"RPRINT",
			"UWAAAA",
			"LOOKUP g_1",
			"END",
			"BEGIN random",
			"END",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 461))
	def test_462(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT 1xyz 123",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 462))
	def test_463(self):
		input = [
			"RPRINT",
			"INSERT f_FF number",
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"ASSIGN f_FF 456",
			"ASSIGN y unimportant",
			"ASSIGN f_FF 1001",
			"INSERT z string",
			"ASSIGN f_FF 789",
			"RPRINT",
			"INSERT g_1 string",
			"ASSIGN b unimportant",
			"END",
			"BEGIN",
			"END",
			"INSERT x string",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN y unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 463))
	def test_464(self):
		input = [
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT d string",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT z number",
			"LOOKUP g_1",
			"BEGIN",
			"INSERT z string",
			"BEGIN",
			"ASSIGN z 'abcABC'",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 464))
	def test_465(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT d number",
			"BEGIN",
			"BEGIN",
			"ASSIGN d 987654",
			"LOOKUP d",
			"BEGIN",
			"LOOKUP d",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"LOOKUP a",
			"INSERT aak e 123",
			"INSERT c number",
			"ASSIGN c 123",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP d",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 465))
	def test_466(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 466))
	def test_467(self):
		input = [
			"PRINT",
			"INSERT d string",
			"LOOKUP d",
		]
		expected = ["", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 467))
	def test_468(self):
		input = [
			"INSERT b string",
			"LOOKUP b",
			"INSERT c string",
			"BEGIN random",
			"LOOKUP y",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 468))
	def test_469(self):
		input = [
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 469))
	def test_470(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"ASSIGN e_123_2r unimportant",
			"INSERT d number",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 470))
	def test_471(self):
		input = [
			"INSERT y string",
			"BEGIN",
			"END",
			"LOOKUP y",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"PRINT",
			"PRINT",
			"INSERT a number",
			"BEGIN",
			"LOOKUP y",
			"INSERT e_123_2r number",
			"INSERT y string",
			"PRINT random",
			"INSERT g_1 string",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 471))
	def test_472(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT y string",
			"ASSIGN y 'abcABC'",
			"END",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 472))
	def test_473(self):
		input = [
			"RPRINT",
			"INSERT c number",
			"BEGIN",
			"PRINT",
			"INSERT a number",
			"PRINT",
			"END",
			"PRINT",
			"INSERT b number",
			"PRINT",
			"END",
			"INSERT x string",
			"RPRINT",
			"LOOKUP x",
			"ASSIGN x 'abcABC'",
			"INSERT f_FF string",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 473))
	def test_474(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT y number",
			"ASSIGN y 1001",
			"INSERT e_123_2r number",
			"ASSIGN e_123_2r 987654 random",
			"INSERT c string",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT x string",
			"LOOKUP x random",
			"PRINT",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
			"PRINT",
		]
		expected = ["Invalid: ASSIGN e_123_2r 987654 random"]

		self.assertTrue(TestUtils.check(input, expected, 474))
	def test_475(self):
		input = [
			"INSERT f_FF number",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT c number",
			"LOOKUP c",
			"PRINT",
			"END",
			"PRINT",
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT c string",
			"INSERT z string",
			"LOOKUP z",
			"LOOKUP z",
			"ASSIGN c 'Test123'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 475))
	def test_476(self):
		input = [
			"BEGIN",
			"INSERT g_1 number",
			"END",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 476))
	def test_477(self):
		input = [
			"PRINT",
			"INSERT b string",
			"ASSIGN b 'HelloWorld'",
			"RPRINT",
			"BEGIN",
			"LOOKUP b",
			"END",
		]
		expected = ["", "success", "success", "b//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 477))
	def test_478(self):
		input = [
			"PRINT",
			"RPRINT",
			"INSERT a string",
			"END",
			"INSERT b number",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 478))
	def test_479(self):
		input = [
			"END",
			"INSERT e_123_2r string",
			"UWAAAA",
			"ASSIGN e_123_2r 'UPPERlower'",
			"INSERT z string",
			"LOOKUP y",
			"INSERT f_FF number",
			"ASSIGN f_FF 456",
			"RPRINT",
			"ASSIGN f_FF 789",
			"LOOKUP f_FF",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 479))
	def test_480(self):
		input = [
			"INSERT x string",
			"END",
			"BEGIN",
			"RPRINT random",
			"RPRINT",
			"RPRINT",
			"BEGIN random",
			"INSERT a string",
			"LOOKUP a",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 480))
	def test_481(self):
		input = [
			"BEGIN",
			"END",
			"RPRINT",
			"INSERT z number",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT y string",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 481))
	def test_482(self):
		input = [
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"END",
			"INSERT e_123_2r number",
			"INSERT d string",
			"ASSIGN e_123_2r 123",
			"INSERT b string",
			"END",
			"INSERT c number",
			"END random",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 482))
	def test_483(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"ASSIGN x 'abcABC'",
			"BEGIN",
			"BEGIN",
			"ASSIGN x 'UPPERlower'",
			"LOOKUP x",
			"BEGIN",
			"LOOKUP x",
			"ASSIGN x 'ab c",
			"END",
			"RPRINT",
			"END",
			"LOOKUP x",
			"LOOKUP x",
			"ASSIGN x 'abcABC'",
			"END random",
			"END",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"BEGIN",
		]
		expected = ["Invalid: ASSIGN x 'ab c"]

		self.assertTrue(TestUtils.check(input, expected, 483))
	def test_484(self):
		input = [
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"INSERT x string",
			"BEGIN",
			"INSERT f_FF string",
			"RPRINT random",
			"LOOKUP x",
			"PRINT",
			"END",
			"END",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT z string",
			"LOOKUP z",
			"END",
			"BEGIN",
			"ASSIGN aak e 123",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 484))
	def test_485(self):
		input = [
			"RPRINT",
			"PRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 485))
	def test_486(self):
		input = [
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 486))
	def test_487(self):
		input = [
			"LOOKUP d",
			"ASSIGN z unimportant",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT c number",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 487))
	def test_488(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"BEGIN",
			"LOOKUP g_1",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"UWAAAA",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 488))
	def test_489(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"INSERT e_123_2r string",
			"PRINT",
			"INSERT d string",
			"ASSIGN d 'UPPERlower'",
			"LOOKUP e_123_2r",
			"INSERT b number",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 489))
	def test_490(self):
		input = [
			"INSERT z number",
			"LOOKUP z",
			"ASSIGN z 456",
			"PRINT",
			"BEGIN",
			"INSERT b number",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"LOOKUP z",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT z number",
			"LOOKUP z",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 490))
	def test_491(self):
		input = [
			"INSERT c string",
			"RPRINT",
			"LOOKUP c",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"INSERT g_1 number",
			"BEGIN",
			"PRINT",
			"END",
			"UWAAAA",
			"UWAAAA",
			"END",
			"INSERT b number",
			"INSERT d string",
			"BEGIN",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 491))
	def test_492(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"PRINT",
			"LOOKUP g_1",
			"ASSIGN g_1 '1234ABC'",
			"PRINT",
			"RPRINT",
			"INSERT f_FF string",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"LOOKUP f_FF",
			"BEGIN",
			"END",
			"BEGIN",
			"ASSIGN g_1 'abcABC'",
			"PRINT",
			"LOOKUP f_FF",
			"PRINT",
			"LOOKUP f_FF random",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: LOOKUP f_FF random"]

		self.assertTrue(TestUtils.check(input, expected, 492))
	def test_493(self):
		input = [
			"BEGIN random",
			"RPRINT",
			"BEGIN",
			"INSERT z number",
			"LOOKUP z",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT b string",
			"ASSIGN b 'HelloWorld'",
			"ASSIGN b '1234ABC'",
			"LOOKUP b",
			"INSERT x number",
			"RPRINT",
			"ASSIGN b 'HelloWorld'",
			"LOOKUP b",
			"ASSIGN x 789",
			"BEGIN",
			"END",
			"ASSIGN b 'HelloWorld'",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 493))
	def test_494(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 494))
	def test_495(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 495))
	def test_496(self):
		input = [
			"RPRINT",
			"PRINT",
			"INSERT y string random",
			"ASSIGN y 'UPPERlower'",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: INSERT y string random"]

		self.assertTrue(TestUtils.check(input, expected, 496))
	def test_497(self):
		input = [
			"INSERT y number",
			"INSERT e_123_2r number",
			"LOOKUP y",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"ASSIGN e_123_2r 123",
			"PRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 497))
	def test_498(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT a number",
			"RPRINT",
			"ASSIGN a 789",
			"BEGIN",
			"BEGIN",
			"ASSIGN a 789",
			"END",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["", "success", "a//2", "success", "success", "a//2"]

		self.assertTrue(TestUtils.check(input, expected, 498))
	def test_499(self):
		input = [
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"RPRINT",
			"LOOKUP e_123_2r",
			"END",
			"INSERT a string",
			"ASSIGN a '1234ABC'",
			"ASSIGN a 'abcABC'",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT g_1 number",
			"INSERT f_FF string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 499))
	def test_500(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT y string",
			"END",
			"BEGIN",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 500))
	def test_501(self):
		input = [
			"UWAAAA",
			"ASSIGN 21_3c 123",
			"END",
			"END",
			"END",
			"END",
			"INSERT y string",
			"LOOKUP y",
			"END",
			"BEGIN",
			"BEGIN",
			"PRINT random",
			"END",
			"PRINT",
			"BEGIN",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 501))
	def test_502(self):
		input = [
			"INSERT z string",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP z",
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"LOOKUP z",
			"INSERT 1xyz 123",
			"END",
			"RPRINT",
			"END",
			"LOOKUP y",
			"ASSIGN z 'HelloWorld'",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 502))
	def test_503(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 503))
	def test_504(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 504))
	def test_505(self):
		input = [
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 505))
	def test_506(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r random",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 506))
	def test_507(self):
		input = [
			"RPRINT",
			"BEGIN",
			"INSERT x number",
			"END",
			"END",
			"INSERT e_123_2r number random",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 789",
			"PRINT",
			"ASSIGN e_123_2r 456",
			"INSERT a number",
			"BEGIN",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 507))
	def test_508(self):
		input = [
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r number random",
			"RPRINT",
			"BEGIN",
			"END",
			"LOOKUP e_123_2r",
			"INSERT y string",
			"BEGIN",
			"LOOKUP e_123_2r",
			"INSERT b number",
			"PRINT",
			"BEGIN",
			"UWAAAA",
			"LOOKUP b",
			"ASSIGN y 'a@bc'",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT e_123_2r number random"]

		self.assertTrue(TestUtils.check(input, expected, 508))
	def test_509(self):
		input = [
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 789",
			"RPRINT",
			"INSERT y string random",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 987654",
			"PRINT",
			"RPRINT",
			"LOOKUP e_123_2r",
			"ASSIGN y 'abcABC'",
			"BEGIN",
			"INSERT c number",
			"RPRINT",
			"END",
			"END",
			"END",
			"END random",
		]
		expected = ["Invalid: INSERT y string random"]

		self.assertTrue(TestUtils.check(input, expected, 509))
	def test_510(self):
		input = [
			"END",
			"PRINT",
			"END",
			"INSERT y string",
			"BEGIN",
			"UWAAAA",
			"ASSIGN y 'Test123'",
			"LOOKUP y",
			"INSERT f_FF string",
			"PRINT",
			"RPRINT random",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"ASSIGN 21_3c 123",
			"ASSIGN f_FF 'Test123'",
			"PRINT",
			"ASSIGN y 'UPPERlower'",
			"LOOKUP c",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 510))
	def test_511(self):
		input = [
			"BEGIN",
			"PRINT",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"INSERT d number",
			"LOOKUP d",
			"ASSIGN d 123",
			"BEGIN",
			"PRINT",
			"INSERT a string random",
			"PRINT",
			"ASSIGN d 123",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 511))
	def test_512(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 512))
	def test_513(self):
		input = [
			"INSERT b string",
			"LOOKUP b",
			"ASSIGN b 'HelloWorld'",
		]
		expected = ["success", "0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 513))
	def test_514(self):
		input = [
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT y string",
			"BEGIN",
			"LOOKUP y",
			"END",
			"END",
		]
		expected = ["", "success", "1"]

		self.assertTrue(TestUtils.check(input, expected, 514))
	def test_515(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"LOOKUP f_FF",
			"PRINT",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 515))
	def test_516(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT a string",
			"RPRINT random",
			"INSERT f_FF string",
			"BEGIN",
			"PRINT",
			"LOOKUP f_FF",
			"PRINT",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 516))
	def test_517(self):
		input = [
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT a string",
			"LOOKUP a",
			"ASSIGN a 'UPPERlower'",
			"PRINT",
			"END",
			"INSERT z string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 517))
	def test_518(self):
		input = [
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT c string",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT a string",
			"PRINT",
			"ASSIGN a 'HelloWorld'",
			"ASSIGN a 'Test123'",
			"END",
			"INSERT 1xyz 123",
			"END",
			"RPRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 518))
	def test_519(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"END random",
			"END",
			"INSERT g_1 number",
			"END",
			"PRINT",
			"INSERT f_FF number",
			"INSERT y number",
			"LOOKUP f_FF",
			"PRINT",
			"ASSIGN y '1234ABC' random",
			"END",
			"END",
			"PRINT",
			"INSERT e_123_2r string",
			"INSERT 21_3c 123",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 519))
	def test_520(self):
		input = [
			"END",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r 123",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"RPRINT",
			"LOOKUP e_123_2r",
			"BEGIN",
			"UWAAAA",
			"LOOKUP e_123_2r",
			"PRINT",
			"RPRINT",
			"ASSIGN e_123_2r '1234ABC'",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"ASSIGN e_123_2r 'HelloWorld'",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 520))
	def test_521(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT x number",
			"INSERT g_1 number",
			"END",
			"INSERT d number",
			"END",
			"RPRINT",
			"INSERT c number",
			"LOOKUP c",
			"PRINT",
			"BEGIN",
			"PRINT",
			"LOOKUP c",
			"INSERT g_1 string",
			"ASSIGN g_1 'Test123'",
			"LOOKUP g_1",
			"INSERT c string",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["", "", "success", "success", "success", "", "success", "1", "c//1", "c//1", "1", "success", "success", "2", "success"]

		self.assertTrue(TestUtils.check(input, expected, 521))
	def test_522(self):
		input = [
			"INSERT y string",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 522))
	def test_523(self):
		input = [
			"INSERT y string",
			"INSERT a number",
			"LOOKUP y",
			"ASSIGN y 'abcABC'",
			"INSERT g_1 string",
			"ASSIGN g_1 'abcABC'",
		]
		expected = ["success", "success", "0", "success", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 523))
	def test_524(self):
		input = [
			"UWAAAA",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 524))
	def test_525(self):
		input = [
			"BEGIN",
			"INSERT f_FF number",
			"BEGIN",
			"END",
			"RPRINT",
			"LOOKUP f_FF",
			"ASSIGN f_FF '1234ABC'",
			"END",
			"RPRINT",
			"INSERT a number",
		]
		expected = ["TypeMismatch: ASSIGN f_FF '1234ABC'"]

		self.assertTrue(TestUtils.check(input, expected, 525))
	def test_526(self):
		input = [
			"BEGIN random",
			"INSERT y string random",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT g_1 number",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 526))
	def test_527(self):
		input = [
			"PRINT",
			"INSERT z string",
			"INSERT e_123_2r number",
			"UWAAAA",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT f_FF number",
			"END",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 527))
	def test_528(self):
		input = [
			"PRINT",
			"RPRINT",
			"INSERT x string",
			"INSERT f_FF string",
			"LOOKUP y",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT d number",
			"LOOKUP d",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 528))
	def test_529(self):
		input = [
			"RPRINT",
			"INSERT b string",
			"LOOKUP b",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"INSERT z number",
			"LOOKUP z",
			"LOOKUP z",
			"ASSIGN z 456",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 529))
	def test_530(self):
		input = [
			"LOOKUP y",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"ASSIGN b 'HelloWorld'",
			"ASSIGN b 'abcABC'",
			"LOOKUP b",
			"END",
			"END",
			"RPRINT",
			"LOOKUP b",
			"ASSIGN b 'HelloWorld' random",
			"LOOKUP b",
			"ASSIGN b 789",
			"BEGIN",
			"END",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 530))
	def test_531(self):
		input = [
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 531))
	def test_532(self):
		input = [
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 532))
	def test_533(self):
		input = [
			"END",
			"INSERT c string",
			"ASSIGN c 'HelloWorld'",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN c 'abcABC'",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 533))
	def test_534(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT f_FF number",
		]
		expected = ["", "", "", "", "", "", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 534))
	def test_535(self):
		input = [
			"INSERT x number",
			"ASSIGN x 987654",
			"LOOKUP x",
			"END",
			"INSERT c number",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"LOOKUP c",
			"PRINT",
			"INSERT __ g 123",
			"ASSIGN c 789",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 535))
	def test_536(self):
		input = [
			"BEGIN",
			"END",
			"INSERT d string",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT y number",
			"ASSIGN y 1001",
			"LOOKUP y",
			"ASSIGN y 123",
			"BEGIN",
			"RPRINT",
			"ASSIGN y 987654",
			"PRINT",
			"BEGIN",
			"LOOKUP f_FF",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 536))
	def test_537(self):
		input = [
			"BEGIN",
			"END",
			"BEGIN",
			"INSERT 1xyz 123",
			"INSERT c number",
			"END",
			"RPRINT",
			"INSERT x string",
			"RPRINT",
			"PRINT",
			"LOOKUP e_123_2r",
			"PRINT",
			"PRINT",
			"LOOKUP x",
			"BEGIN",
			"LOOKUP x",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 537))
	def test_538(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT g_1 string",
			"RPRINT",
			"INSERT y number",
			"ASSIGN ()z 123",
			"RPRINT",
			"RPRINT",
			"INSERT g_1 string",
			"LOOKUP y",
			"PRINT",
			"ASSIGN y 789",
			"PRINT",
			"INSERT c string",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT g_1 string",
			"END random",
			"BEGIN",
			"BEGIN",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 538))
	def test_539(self):
		input = [
			"PRINT",
			"INSERT a string",
			"ASSIGN a 'HelloWorld'",
			"BEGIN",
			"INSERT e_123_2r string",
			"BEGIN",
			"RPRINT",
			"ASSIGN ()z 123",
			"LOOKUP a",
			"END",
			"BEGIN",
			"RPRINT",
			"LOOKUP e_123_2r",
			"INSERT x string",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"ASSIGN e_123_2r 'UPPERlower'",
			"ASSIGN a 'UPPERlower'",
			"BEGIN",
			"LOOKUP e_123_2r",
			"BEGIN",
			"ASSIGN x 'Test123'",
			"RPRINT",
			"INSERT y string",
			"ASSIGN e_123_2r 'UPPERlower'",
			"BEGIN",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 539))
	def test_540(self):
		input = [
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 540))
	def test_541(self):
		input = [
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 541))
	def test_542(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"INSERT x number",
			"INSERT g_1 number",
			"END",
		]
		expected = ["", "success", "1", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 542))
	def test_543(self):
		input = [
			"END",
			"RPRINT",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 543))
	def test_544(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 544))
	def test_545(self):
		input = [
			"RPRINT",
			"INSERT c string",
			"PRINT",
			"PRINT",
			"ASSIGN c 'HelloWorld'",
			"PRINT",
			"BEGIN",
			"ASSIGN c 'UPPERlower'",
			"ASSIGN c 'UPPERlower'",
			"END",
			"PRINT",
			"INSERT z number",
			"PRINT",
			"BEGIN",
			"INSERT g_1 string",
			"PRINT",
			"LOOKUP g_1",
			"END",
		]
		expected = ["", "success", "c//0", "c//0", "success", "c//0", "success", "success", "c//0", "success", "c//0 z//0", "success", "c//0 z//0 g_1//1", "1"]

		self.assertTrue(TestUtils.check(input, expected, 545))
	def test_546(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT f_FF number",
			"RPRINT",
			"ASSIGN f_FF 789",
			"BEGIN",
			"LOOKUP f_FF",
			"BEGIN",
			"ASSIGN f_FF 123.8.7",
			"LOOKUP b",
			"END",
			"INSERT a string",
			"RPRINT",
			"END",
			"RPRINT",
			"ASSIGN f_FF 1001",
			"END",
			"INSERT d number",
			"PRINT",
		]
		expected = ["Invalid: ASSIGN f_FF 123.8.7"]

		self.assertTrue(TestUtils.check(input, expected, 546))
	def test_547(self):
		input = [
			"UWAAAA",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT x string",
			"INSERT ()z 123",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 547))
	def test_548(self):
		input = [
			"BEGIN",
			"PRINT",
			"INSERT e_123_2r string",
			"RPRINT",
			"INSERT f_FF string",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT z string",
			"INSERT g_1 string random",
			"END",
			"LOOKUP e_123_2r",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"ASSIGN f_FF 'abc! 1'",
			"PRINT",
			"INSERT d string",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT g_1 number",
			"RPRINT",
			"INSERT b string",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT g_1 string random"]

		self.assertTrue(TestUtils.check(input, expected, 548))
	def test_549(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 549))
	def test_550(self):
		input = [
			"PRINT",
			"END",
			"INSERT g_1 number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 550))
	def test_551(self):
		input = [
			"PRINT",
			"PRINT random",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 551))
	def test_552(self):
		input = [
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"INSERT x number",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 552))
	def test_553(self):
		input = [
			"END",
			"END",
			"END",
			"PRINT",
			"END",
			"END",
			"UWAAAA",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 553))
	def test_554(self):
		input = [
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 554))
	def test_555(self):
		input = [
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT 21_3c 123",
			"RPRINT",
			"BEGIN",
			"INSERT z string",
			"LOOKUP z",
			"LOOKUP z",
			"BEGIN",
			"PRINT",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"LOOKUP z",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 555))
	def test_556(self):
		input = [
			"RPRINT",
			"INSERT d number",
			"RPRINT",
			"RPRINT",
			"ASSIGN d 456",
			"ASSIGN d 987654",
			"PRINT",
			"LOOKUP d",
			"ASSIGN 21_3c 123",
			"END",
			"RPRINT",
			"INSERT z string",
			"INSERT x string",
			"END",
			"INSERT y string",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"END random",
			"RPRINT",
		]
		expected = ["Invalid: ASSIGN 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 556))
	def test_557(self):
		input = [
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 557))
	def test_558(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 558))
	def test_559(self):
		input = [
			"BEGIN",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 559))
	def test_560(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"INSERT c string",
			"ASSIGN c 'Test123'",
			"RPRINT",
			"ASSIGN c 'Test123'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 560))
	def test_561(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"UWAAAA",
			"INSERT b number",
			"PRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 561))
	def test_562(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT random",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 562))
	def test_563(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT g_1 number",
			"ASSIGN b unimportant",
			"INSERT y_12@! 123",
			"LOOKUP g_1",
			"ASSIGN 2_3f 123",
			"ASSIGN g_1 456",
			"LOOKUP a",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 563))
	def test_564(self):
		input = [
			"END",
			"PRINT",
			"PRINT",
			"INSERT a number",
			"PRINT",
			"LOOKUP a",
			"INSERT b string",
			"INSERT g_1 string",
			"RPRINT",
			"LOOKUP a",
			"BEGIN",
			"RPRINT",
			"LOOKUP g_1",
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT y string",
			"ASSIGN y 'UPPERlower'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 564))
	def test_565(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"BEGIN",
			"PRINT random",
			"ASSIGN ()z 123",
			"INSERT e_123_2r number",
			"RPRINT",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"END",
			"PRINT",
			"ASSIGN e_123_2r 456",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT d number",
			"LOOKUP e_123_2r",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 565))
	def test_566(self):
		input = [
			"LOOKUP d",
			"INSERT g_1 number",
			"ASSIGN g_1 123",
			"INSERT b string",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"INSERT g_1 number",
			"INSERT d number",
			"BEGIN",
			"UWAAAA",
			"ASSIGN b 'Test123'",
			"LOOKUP b",
			"LOOKUP g_1",
			"LOOKUP d",
			"RPRINT",
			"ASSIGN g_1 123",
			"BEGIN",
			"ASSIGN f_FF 'UPPERlower'",
			"PRINT",
			"LOOKUP g_1",
			"END",
			"LOOKUP e_123_2r",
			"PRINT",
			"PRINT",
			"INSERT y number",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 566))
	def test_567(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 567))
	def test_568(self):
		input = [
			"RPRINT",
			"PRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 568))
	def test_569(self):
		input = [
			"INSERT f_FF string",
			"BEGIN",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"ASSIGN f_FF 'abcABC'",
			"END",
		]
		expected = ["success", "0", "0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 569))
	def test_570(self):
		input = [
			"UWAAAA",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 570))
	def test_571(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT f_FF string",
			"RPRINT",
			"INSERT a string",
			"BEGIN",
			"ASSIGN 21_3c 123",
			"ASSIGN f_FF 'abcABC'",
			"INSERT f_FF string",
			"PRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["Invalid: ASSIGN 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 571))
	def test_572(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"INSERT c number",
			"LOOKUP c",
			"RPRINT",
			"RPRINT",
			"BEGIN random",
			"INSERT f_FF number",
			"BEGIN",
			"RPRINT",
			"ASSIGN c 'abcABC'",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 572))
	def test_573(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT random",
			"PRINT",
			"PRINT",
			"INSERT y number",
			"UWAAAA",
			"PRINT",
			"LOOKUP y",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 573))
	def test_574(self):
		input = [
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN random",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"INSERT f_FF string",
			"PRINT",
			"PRINT",
			"ASSIGN f_FF 'abcABC'",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 574))
	def test_575(self):
		input = [
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r 'UPPERlower'",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"INSERT d string",
			"END",
			"LOOKUP e_123_2r",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"LOOKUP e_123_2r",
			"LOOKUP e_123_2r",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT d string",
			"END",
			"END",
			"INSERT a string",
			"ASSIGN a 'Test123'",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 575))
	def test_576(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"INSERT y string",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"RPRINT",
			"PRINT",
			"LOOKUP e_123_2r",
			"END",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 576))
	def test_577(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 577))
	def test_578(self):
		input = [
			"UWAAAA",
			"PRINT",
			"INSERT x number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 578))
	def test_579(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 579))
	def test_580(self):
		input = [
			"INSERT c number",
			"UWAAAA",
			"LOOKUP c",
			"RPRINT",
			"END",
			"UWAAAA",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 580))
	def test_581(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"BEGIN random",
			"RPRINT",
			"INSERT a string",
			"LOOKUP a",
			"BEGIN",
			"LOOKUP a",
			"LOOKUP a",
			"ASSIGN a 'Test123'",
			"INSERT d number",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 581))
	def test_582(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["", "", "", "", "", "", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 582))
	def test_583(self):
		input = [
			"PRINT",
			"END",
			"UWAAAA",
			"INSERT b number",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP b",
			"BEGIN",
			"INSERT c string",
			"INSERT 2_3f 123",
			"PRINT",
			"RPRINT",
			"PRINT",
			"ASSIGN b 987654",
			"LOOKUP b",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"BEGIN random",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 583))
	def test_584(self):
		input = [
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT c string",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 584))
	def test_585(self):
		input = [
			"INSERT z string",
			"UWAAAA",
			"BEGIN",
			"END",
			"PRINT",
			"ASSIGN z 'ab c",
			"INSERT a number",
			"BEGIN",
			"RPRINT",
			"END",
			"LOOKUP a",
			"BEGIN",
			"INSERT x string",
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"ASSIGN z 'Test123'",
			"RPRINT",
			"LOOKUP a",
			"ASSIGN z 123",
			"INSERT b number",
			"END",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 585))
	def test_586(self):
		input = [
			"INSERT y_12@! 123",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: INSERT y_12@! 123"]

		self.assertTrue(TestUtils.check(input, expected, 586))
	def test_587(self):
		input = [
			"INSERT y number",
			"BEGIN",
			"END",
			"ASSIGN y 1001",
		]
		expected = ["success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 587))
	def test_588(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 588))
	def test_589(self):
		input = [
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT z string",
			"PRINT",
			"END",
			"INSERT a string",
			"ASSIGN a 'abcABC'",
			"INSERT b number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 589))
	def test_590(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT x string",
			"BEGIN",
			"PRINT random",
			"END",
			"PRINT",
			"BEGIN",
			"ASSIGN x 'abcABC'",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT z number",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 590))
	def test_591(self):
		input = [
			"ASSIGN a unimportant",
			"PRINT",
			"PRINT",
			"ASSIGN b unimportant",
			"PRINT",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT b number",
			"INSERT b string",
			"END",
			"RPRINT",
			"RPRINT",
		]
		expected = ["Undeclared: ASSIGN a unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 591))
	def test_592(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"PRINT",
			"INSERT b number",
			"PRINT",
			"END",
			"ASSIGN _@_$$d 123",
			"RPRINT",
			"PRINT",
			"INSERT d string",
			"RPRINT",
			"RPRINT",
			"LOOKUP d",
			"ASSIGN b@B((*@ 123",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 592))
	def test_593(self):
		input = [
			"PRINT",
			"END",
			"PRINT",
			"INSERT d string",
			"LOOKUP f_FF",
			"PRINT",
			"LOOKUP d",
			"INSERT z string",
			"PRINT",
			"ASSIGN z 'abcABC'",
			"INSERT y string",
			"LOOKUP y",
			"PRINT",
			"ASSIGN d 'HelloWorld'",
			"LOOKUP d",
			"INSERT b number",
			"ASSIGN b 123",
			"BEGIN random",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"LOOKUP f_FF",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 593))
	def test_594(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT d number",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"ASSIGN y_12@! 123",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END random",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN y_12@! 123"]

		self.assertTrue(TestUtils.check(input, expected, 594))
	def test_595(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 595))
	def test_596(self):
		input = [
			"INSERT 2_3f 123",
			"INSERT g_1 string",
			"PRINT",
			"RPRINT",
		]
		expected = ["Invalid: INSERT 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 596))
	def test_597(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 597))
	def test_598(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
			"INSERT e_123_2r number",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 598))
	def test_599(self):
		input = [
			"LOOKUP d",
			"INSERT x string",
			"RPRINT",
			"INSERT f_FF number",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"ASSIGN f_FF 1001",
			"PRINT",
			"ASSIGN f_FF 'UPPERlower'",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 599))
	def test_600(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT f_FF number",
			"INSERT z string",
			"RPRINT",
			"ASSIGN f_FF 456",
			"ASSIGN f_FF 456",
			"BEGIN",
			"LOOKUP z",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["", "", "", "", "success", "success", "z//1 f_FF//1", "success", "success", "1", "z//1 f_FF//1"]

		self.assertTrue(TestUtils.check(input, expected, 600))
	def test_601(self):
		input = [
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT e_123_2r string",
			"INSERT g_1 string",
			"RPRINT",
			"INSERT b@B((*@ 123",
			"RPRINT",
			"PRINT",
			"PRINT",
			"LOOKUP e_123_2r",
			"ASSIGN g_1 'UPPERlower'",
			"LOOKUP e_123_2r",
			"INSERT c string",
			"ASSIGN c 'UPPERlower'",
			"INSERT d number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 601))
	def test_602(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"INSERT b string",
			"LOOKUP b",
			"END",
			"END",
			"INSERT x string",
			"RPRINT",
			"RPRINT",
			"INSERT c number",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 602))
	def test_603(self):
		input = [
			"INSERT y number",
			"PRINT",
			"BEGIN",
			"LOOKUP y",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
			"ASSIGN y 1001",
			"LOOKUP y",
			"PRINT",
			"BEGIN",
			"LOOKUP y",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN y 789",
			"BEGIN",
			"RPRINT",
			"LOOKUP y",
			"ASSIGN y 789",
			"RPRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnclosedBlock: 2"]

		self.assertTrue(TestUtils.check(input, expected, 603))
	def test_604(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 604))
	def test_605(self):
		input = [
			"PRINT",
			"INSERT g_1 number",
			"RPRINT",
			"INSERT c number",
		]
		expected = ["", "success", "g_1//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 605))
	def test_606(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT f_FF string",
			"INSERT g_1 number random",
			"LOOKUP g_1",
			"PRINT",
			"ASSIGN f_FF 'Test123'",
		]
		expected = ["Invalid: INSERT g_1 number random"]

		self.assertTrue(TestUtils.check(input, expected, 606))
	def test_607(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 607))
	def test_608(self):
		input = [
			"INSERT a number",
			"PRINT",
			"BEGIN",
			"END",
			"ASSIGN a 456",
			"INSERT y string",
			"BEGIN",
			"INSERT __ g 123",
			"INSERT c string",
			"PRINT",
			"END",
			"LOOKUP y",
			"LOOKUP y",
			"END",
		]
		expected = ["Invalid: INSERT __ g 123"]

		self.assertTrue(TestUtils.check(input, expected, 608))
	def test_609(self):
		input = [
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT y number random",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"LOOKUP y",
			"ASSIGN y 1001",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT y number random"]

		self.assertTrue(TestUtils.check(input, expected, 609))
	def test_610(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r '1234ABC' random",
			"ASSIGN e_123_2r 'UPPERlower'",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"END",
			"INSERT e_123_2r string",
			"INSERT a number",
			"PRINT random",
			"RPRINT",
		]
		expected = ["Invalid: ASSIGN e_123_2r '1234ABC' random"]

		self.assertTrue(TestUtils.check(input, expected, 610))
	def test_611(self):
		input = [
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"INSERT z number",
			"PRINT",
			"LOOKUP z",
			"RPRINT",
			"INSERT c number",
			"END",
			"RPRINT",
			"ASSIGN y unimportant",
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 611))
	def test_612(self):
		input = [
			"RPRINT",
			"RPRINT",
			"ASSIGN e_123_2r unimportant",
			"PRINT",
			"INSERT y number",
			"LOOKUP y",
			"LOOKUP y",
			"PRINT",
			"LOOKUP y",
			"INSERT g_1 number",
			"LOOKUP y",
			"RPRINT random",
			"LOOKUP g_1",
			"ASSIGN y 1001",
			"END",
			"RPRINT random",
			"PRINT",
			"RPRINT",
			"INSERT a string",
			"LOOKUP a",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 612))
	def test_613(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 613))
	def test_614(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 614))
	def test_615(self):
		input = [
			"INSERT g_1 number",
			"LOOKUP g_1",
			"RPRINT",
			"RPRINT",
			"ASSIGN g_1 123",
		]
		expected = ["success", "0", "g_1//0", "g_1//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 615))
	def test_616(self):
		input = [
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT f_FF number",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 616))
	def test_617(self):
		input = [
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT g_1 string",
			"BEGIN",
			"INSERT f_FF string",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT random",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 617))
	def test_618(self):
		input = [
			"INSERT x number",
			"ASSIGN x 12 34",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"ASSIGN x 12 34",
			"BEGIN",
			"LOOKUP x",
			"ASSIGN x 789",
			"RPRINT",
			"INSERT d string",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"END random",
		]
		expected = ["Invalid: ASSIGN x 12 34"]

		self.assertTrue(TestUtils.check(input, expected, 618))
	def test_619(self):
		input = [
			"INSERT d number",
			"LOOKUP d",
			"INSERT z number",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"END",
			"LOOKUP d",
			"BEGIN",
			"PRINT",
			"ASSIGN z 987654",
			"ASSIGN z 789",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"ASSIGN d 1001",
			"END",
			"INSERT b string",
			"LOOKUP b",
		]
		expected = ["success", "0", "success", "z//0 d//0", "d//0 z//0", "0", "d//0 z//0", "success", "success", "d//0 z//0", "z//0 d//0", "z//0 d//0", "success", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 619))
	def test_620(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 620))
	def test_621(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT z number",
			"INSERT g_1 number",
			"ASSIGN e_123_2r unimportant",
			"INSERT d number",
			"PRINT",
			"INSERT y string",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT x number",
			"BEGIN",
			"ASSIGN x 789",
			"LOOKUP x",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 621))
	def test_622(self):
		input = [
			"RPRINT",
			"INSERT __ g 123",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"INSERT b number",
			"INSERT x string",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"END",
		]
		expected = ["Invalid: INSERT __ g 123"]

		self.assertTrue(TestUtils.check(input, expected, 622))
	def test_623(self):
		input = [
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 623))
	def test_624(self):
		input = [
			"UWAAAA",
			"INSERT a number",
			"PRINT",
			"ASSIGN a 789",
			"PRINT",
			"ASSIGN a 'HelloWorld'",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 624))
	def test_625(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT g_1 number",
			"INSERT x number random",
			"RPRINT",
			"LOOKUP x",
			"LOOKUP g_1",
		]
		expected = ["Invalid: INSERT x number random"]

		self.assertTrue(TestUtils.check(input, expected, 625))
	def test_626(self):
		input = [
			"END",
			"RPRINT",
			"BEGIN",
			"INSERT y string",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"ASSIGN y 'UPPERlower'",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 626))
	def test_627(self):
		input = [
			"END",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"END",
			"PRINT",
			"INSERT b string",
			"INSERT a number",
			"LOOKUP b",
			"ASSIGN a 1001",
			"INSERT e_123_2r string",
			"BEGIN",
			"ASSIGN a 789",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 627))
	def test_628(self):
		input = [
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"LOOKUP b",
			"UWAAAA",
			"ASSIGN b 'abcABC'",
			"INSERT e_123_2r string",
			"BEGIN",
			"END",
			"BEGIN",
			"ASSIGN b 'HelloWorld'",
			"INSERT b string",
			"PRINT",
			"LOOKUP b",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 628))
	def test_629(self):
		input = [
			"INSERT c number",
			"INSERT x string",
			"ASSIGN c 456",
			"BEGIN",
			"PRINT",
			"LOOKUP x",
			"INSERT g_1 number",
			"RPRINT",
			"PRINT",
			"ASSIGN x '1234ABC'",
			"ASSIGN e_123_2r unimportant",
			"BEGIN",
			"ASSIGN c 1001",
			"UWAAAA",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 987654",
			"ASSIGN c 456",
			"RPRINT",
			"ASSIGN c 789",
			"LOOKUP e_123_2r",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 629))
	def test_630(self):
		input = [
			"INSERT e_123_2r string",
			"BEGIN",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"INSERT b string",
			"RPRINT",
			"END",
			"ASSIGN e_123_2r 'Test123'",
			"BEGIN",
			"ASSIGN 21_3c 123",
			"RPRINT",
			"END",
			"UWAAAA",
			"INSERT b number",
			"LOOKUP e_123_2r",
			"INSERT c number random",
			"PRINT",
			"PRINT",
			"LOOKUP c",
			"BEGIN",
			"RPRINT",
			"ASSIGN a unimportant",
			"PRINT",
			"ASSIGN b 789",
			"ASSIGN c 789",
			"END",
		]
		expected = ["Invalid: ASSIGN 21_3c 123"]

		self.assertTrue(TestUtils.check(input, expected, 630))
	def test_631(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN random",
			"INSERT g_1 number",
			"ASSIGN g_1 456",
			"INSERT c number",
			"UWAAAA",
			"INSERT x string",
			"INSERT y string",
			"INSERT d string",
			"RPRINT",
			"INSERT a string",
			"INSERT e_123_2r number",
			"LOOKUP a",
			"LOOKUP y",
			"END",
			"BEGIN",
			"ASSIGN c unimportant",
			"BEGIN",
			"END",
			"BEGIN random",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 631))
	def test_632(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r number",
			"END",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 632))
	def test_633(self):
		input = [
			"PRINT",
			"RPRINT",
			"INSERT a number",
			"RPRINT",
		]
		expected = ["", "", "success", "a//0"]

		self.assertTrue(TestUtils.check(input, expected, 633))
	def test_634(self):
		input = [
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"INSERT b number",
			"INSERT g_1 number",
			"ASSIGN b 456",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 634))
	def test_635(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 635))
	def test_636(self):
		input = [
			"BEGIN",
			"INSERT x number",
			"RPRINT",
			"ASSIGN x 'UPPERlower'",
			"ASSIGN x 789",
			"LOOKUP x random",
			"END",
			"INSERT f_FF number",
			"ASSIGN f_FF 456",
			"RPRINT",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN x 'UPPERlower'"]

		self.assertTrue(TestUtils.check(input, expected, 636))
	def test_637(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["", "", "", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 637))
	def test_638(self):
		input = [
			"END",
			"INSERT c string",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT g_1 number",
			"BEGIN",
			"INSERT z string",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT f_FF string",
			"PRINT",
			"ASSIGN f_FF 'HelloWorld'",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 638))
	def test_639(self):
		input = [
			"LOOKUP x",
			"PRINT",
			"INSERT b string",
			"INSERT a number",
			"BEGIN",
			"ASSIGN a '1234ABC'",
			"END",
			"END",
			"INSERT a number",
			"BEGIN",
			"LOOKUP a",
			"LOOKUP a",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"PRINT",
			"INSERT y string",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 639))
	def test_640(self):
		input = [
			"INSERT z number",
			"RPRINT",
			"ASSIGN z 123",
			"RPRINT",
			"PRINT",
			"LOOKUP z",
			"ASSIGN z 456",
			"ASSIGN d unimportant",
			"PRINT",
			"BEGIN",
			"LOOKUP z",
			"PRINT",
			"RPRINT",
			"INSERT y string",
			"INSERT z string",
			"PRINT",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Undeclared: ASSIGN d unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 640))
	def test_641(self):
		input = [
			"INSERT y string",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 641))
	def test_642(self):
		input = [
			"BEGIN",
			"END",
			"UWAAAA",
			"END",
			"INSERT e_123_2r number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 642))
	def test_643(self):
		input = [
			"BEGIN",
			"END",
			"INSERT e_123_2r number",
			"UWAAAA",
			"INSERT f_FF string",
			"INSERT a string",
			"BEGIN",
			"INSERT d string",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 643))
	def test_644(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
		]
		expected = ["", "", "", "", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 644))
	def test_645(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"END",
			"RPRINT random",
			"UWAAAA",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 645))
	def test_646(self):
		input = [
			"INSERT g_1 number",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"PRINT",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"END",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 646))
	def test_647(self):
		input = [
			"UWAAAA",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r number",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r 'abcABC'",
			"END",
			"PRINT",
			"INSERT c string",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"LOOKUP e_123_2r",
			"END",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 647))
	def test_648(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"INSERT b string",
			"INSERT a number",
			"END",
			"RPRINT",
			"INSERT y number",
			"BEGIN",
			"PRINT",
			"PRINT",
			"ASSIGN y 123a",
			"ASSIGN y 987654",
			"RPRINT",
			"INSERT y string",
			"END",
			"INSERT f_FF number",
			"RPRINT",
			"UWAAAA",
			"END",
			"BEGIN",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 648))
	def test_649(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT g_1 number",
			"ASSIGN g_1 987654",
			"BEGIN",
			"INSERT x number",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"INSERT z number",
			"LOOKUP z",
			"RPRINT",
			"LOOKUP z",
			"RPRINT random",
			"LOOKUP z",
			"ASSIGN z 1001",
			"ASSIGN 21_3c 123",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 649))
	def test_650(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 650))
	def test_651(self):
		input = [
			"RPRINT",
			"PRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 651))
	def test_652(self):
		input = [
			"INSERT f_FF string",
			"INSERT c string",
			"PRINT",
			"END",
			"INSERT b number",
			"INSERT f_FF string",
			"INSERT x number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 652))
	def test_653(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"ASSIGN 2_3f 123",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT c string",
			"PRINT",
		]
		expected = ["Invalid: ASSIGN 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 653))
	def test_654(self):
		input = [
			"BEGIN",
			"RPRINT",
			"INSERT d string",
			"LOOKUP d",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"ASSIGN b 456",
			"LOOKUP b",
			"INSERT c string random",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT c string random"]

		self.assertTrue(TestUtils.check(input, expected, 654))
	def test_655(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT z string",
			"END",
			"INSERT g_1 number",
			"INSERT b string",
			"LOOKUP b",
			"LOOKUP b",
			"LOOKUP g_1",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["", "success", "success", "success", "1", "1", "1", ""]

		self.assertTrue(TestUtils.check(input, expected, 655))
	def test_656(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT x number",
			"BEGIN",
			"INSERT a number",
			"RPRINT",
			"ASSIGN a 987654",
			"LOOKUP f_FF",
			"INSERT g_1 string",
			"END",
			"PRINT",
			"RPRINT",
			"ASSIGN x 987654",
			"ASSIGN x 456",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP f_FF"]

		self.assertTrue(TestUtils.check(input, expected, 656))
	def test_657(self):
		input = [
			"RPRINT",
			"BEGIN",
			"INSERT x number",
			"BEGIN",
			"UWAAAA",
			"PRINT",
			"ASSIGN x 456",
			"LOOKUP x",
			"LOOKUP x",
			"BEGIN",
			"LOOKUP x",
			"INSERT g_1 string",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"INSERT f_FF string",
			"END",
			"ASSIGN y_12@! 123",
			"PRINT",
			"BEGIN",
			"INSERT f_FF string",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 657))
	def test_658(self):
		input = [
			"ASSIGN ()z 123",
			"LOOKUP z",
			"END random",
			"BEGIN",
			"PRINT",
			"ASSIGN x unimportant",
			"PRINT",
			"INSERT x number",
			"RPRINT",
			"PRINT",
			"LOOKUP y",
			"PRINT",
			"RPRINT",
			"INSERT d number",
			"LOOKUP d",
			"PRINT",
			"INSERT z string",
			"RPRINT",
			"PRINT",
			"ASSIGN x '1234ABC'",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
			"RPRINT",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 658))
	def test_659(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 659))
	def test_660(self):
		input = [
			"ASSIGN d unimportant",
			"INSERT a string",
		]
		expected = ["Undeclared: ASSIGN d unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 660))
	def test_661(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"INSERT z number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 661))
	def test_662(self):
		input = [
			"RPRINT",
			"END",
			"INSERT c string",
			"UWAAAA",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 662))
	def test_663(self):
		input = [
			"INSERT a number",
			"RPRINT",
			"ASSIGN a 1001",
			"LOOKUP a",
			"ASSIGN a 1001",
			"BEGIN",
			"LOOKUP a",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT ()z 123",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 663))
	def test_664(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 664))
	def test_665(self):
		input = [
			"BEGIN",
			"ASSIGN b unimportant",
			"INSERT x number",
			"INSERT e_123_2r string",
			"PRINT",
			"UWAAAA",
			"LOOKUP e_123_2r",
			"LOOKUP x",
			"ASSIGN x 456",
			"RPRINT",
			"ASSIGN e_123_2r 'UPPERlower'",
			"LOOKUP e_123_2r",
			"RPRINT",
			"ASSIGN e_123_2r 'HelloWorld'",
			"ASSIGN e_123_2r 'UPPERlower'",
			"INSERT z number",
			"BEGIN",
			"RPRINT",
			"INSERT z number",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN b unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 665))
	def test_666(self):
		input = [
			"PRINT",
			"INSERT a number",
			"INSERT d number",
			"PRINT",
			"PRINT",
			"ASSIGN a 1001",
			"PRINT",
			"LOOKUP d",
			"PRINT",
			"BEGIN",
			"INSERT c string",
			"LOOKUP d",
			"END",
			"BEGIN",
			"INSERT x number",
			"INSERT e_123_2r string",
			"RPRINT",
			"LOOKUP a",
			"LOOKUP x",
			"INSERT x string",
			"RPRINT",
		]
		expected = ["Redeclared: INSERT x string"]

		self.assertTrue(TestUtils.check(input, expected, 666))
	def test_667(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT b number",
			"ASSIGN b 123",
			"END",
			"INSERT z number",
			"END",
			"INSERT g_1 number",
			"ASSIGN g_1 789",
			"RPRINT",
			"ASSIGN g_1 987654",
			"PRINT",
			"RPRINT",
			"INSERT g_1 string",
			"ASSIGN g_1 123",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
		]
		expected = ["Redeclared: INSERT g_1 string"]

		self.assertTrue(TestUtils.check(input, expected, 667))
	def test_668(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 668))
	def test_669(self):
		input = [
			"UWAAAA",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 669))
	def test_670(self):
		input = [
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"INSERT y string",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 670))
	def test_671(self):
		input = [
			"END",
			"END",
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT a string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 671))
	def test_672(self):
		input = [
			"LOOKUP x",
			"END",
			"RPRINT",
			"END",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 672))
	def test_673(self):
		input = [
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r number",
			"INSERT d string",
			"PRINT",
			"BEGIN",
			"LOOKUP e_123_2r",
			"ASSIGN d 'HelloWorld'",
			"RPRINT",
			"ASSIGN d 789",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN d 789"]

		self.assertTrue(TestUtils.check(input, expected, 673))
	def test_674(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"LOOKUP g_1",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN x 'UPPERlower'",
		]
		expected = ["Undeclared: LOOKUP g_1"]

		self.assertTrue(TestUtils.check(input, expected, 674))
	def test_675(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"INSERT y number",
			"LOOKUP x",
			"BEGIN",
			"INSERT g_1 number",
			"UWAAAA",
			"INSERT d number",
			"RPRINT",
			"INSERT x number",
			"LOOKUP g_1",
			"ASSIGN d 123",
			"ASSIGN c unimportant",
			"LOOKUP d",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 675))
	def test_676(self):
		input = [
			"BEGIN",
			"END",
			"ASSIGN x unimportant",
			"END",
			"INSERT e_123_2r number",
			"PRINT",
			"RPRINT",
			"ASSIGN e_123_2r 123",
			"INSERT y number",
			"BEGIN",
			"ASSIGN g_1 unimportant",
			"ASSIGN e_123_2r 123",
			"RPRINT",
			"ASSIGN e_123_2r 789",
			"LOOKUP e_123_2r",
			"RPRINT",
			"ASSIGN e_123_2r 123",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: ASSIGN x unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 676))
	def test_677(self):
		input = [
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT y number random",
			"BEGIN",
			"LOOKUP y",
			"INSERT e_123_2r string",
			"INSERT y string",
			"BEGIN",
			"ASSIGN y 'abcABC'",
			"END",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT d number random",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"LOOKUP d",
			"LOOKUP d",
			"ASSIGN y 456",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 677))
	def test_678(self):
		input = [
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 678))
	def test_679(self):
		input = [
			"INSERT f_FF string",
			"END",
			"PRINT",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 679))
	def test_680(self):
		input = [
			"INSERT y string",
			"RPRINT",
			"INSERT y number",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
		]
		expected = ["Redeclared: INSERT y number"]

		self.assertTrue(TestUtils.check(input, expected, 680))
	def test_681(self):
		input = [
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT b number",
			"LOOKUP b",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 681))
	def test_682(self):
		input = [
			"INSERT z number",
			"ASSIGN c unimportant",
			"RPRINT",
			"INSERT g_1 number",
			"END",
			"UWAAAA",
			"INSERT x string",
			"UWAAAA",
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"LOOKUP e_123_2r",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 682))
	def test_683(self):
		input = [
			"UWAAAA",
			"UWAAAA",
			"RPRINT",
			"INSERT a number",
			"PRINT",
			"BEGIN",
			"INSERT c string",
			"RPRINT random",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT y string",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 683))
	def test_684(self):
		input = [
			"RPRINT",
			"INSERT e_123_2r number",
			"INSERT f_FF number",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT y number",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT b string",
			"ASSIGN y 1001",
			"LOOKUP y",
			"UWAAAA",
			"ASSIGN y 1001",
			"LOOKUP y",
			"ASSIGN b 'abcABC'",
			"ASSIGN b 'HelloWorld'",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 684))
	def test_685(self):
		input = [
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"RPRINT",
			"ASSIGN f_FF unimportant",
			"RPRINT",
			"RPRINT random",
			"BEGIN",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"LOOKUP b",
			"END",
			"INSERT c number",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"LOOKUP c",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 685))
	def test_686(self):
		input = [
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"RPRINT random",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"INSERT g_1 string",
			"RPRINT",
			"ASSIGN g_1 '1234ABC'",
			"INSERT z number",
			"INSERT y number",
			"ASSIGN y abc123",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 686))
	def test_687(self):
		input = [
			"BEGIN",
			"INSERT f_FF string",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 687))
	def test_688(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 688))
	def test_689(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT z number",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 689))
	def test_690(self):
		input = [
			"INSERT a string",
			"BEGIN",
			"END",
			"ASSIGN a 'HelloWorld'",
			"LOOKUP a",
			"PRINT",
			"RPRINT",
			"LOOKUP a",
			"BEGIN",
			"ASSIGN a 'Test123'",
			"INSERT c string",
			"END",
		]
		expected = ["success", "success", "0", "a//0", "a//0", "0", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 690))
	def test_691(self):
		input = [
			"END",
			"RPRINT",
			"INSERT c string",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"LOOKUP y",
			"INSERT x string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 691))
	def test_692(self):
		input = [
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"ASSIGN _@_$$d 123",
			"INSERT x string",
			"ASSIGN x 'UPPERlower'",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 692))
	def test_693(self):
		input = [
			"BEGIN",
			"INSERT a string",
			"ASSIGN a '1234ABC'",
			"PRINT random",
			"RPRINT",
			"BEGIN",
			"ASSIGN a 'UPPERlower'",
			"LOOKUP a",
			"PRINT random",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 string",
			"END",
			"INSERT e_123_2r number",
			"ASSIGN a 'UPPERlower'",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 693))
	def test_694(self):
		input = [
			"RPRINT",
			"INSERT g_1 number",
			"UWAAAA",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT a number",
			"LOOKUP a",
			"INSERT y number",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"ASSIGN y unimportant",
			"INSERT z number",
			"INSERT c number",
			"INSERT x number",
			"RPRINT",
			"INSERT b string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 694))
	def test_695(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT a string",
			"ASSIGN a 'Test123'",
			"ASSIGN a 'HelloWorld'",
			"END",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"INSERT d number",
			"ASSIGN d 987654",
			"END",
			"BEGIN",
			"INSERT f_FF number",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 695))
	def test_696(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 696))
	def test_697(self):
		input = [
			"RPRINT",
			"INSERT z number",
			"INSERT e_123_2r number",
		]
		expected = ["", "success", "success"]

		self.assertTrue(TestUtils.check(input, expected, 697))
	def test_698(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r string",
			"INSERT z string",
			"LOOKUP e_123_2r",
			"INSERT c number",
			"END",
			"END",
		]
		expected = ["success", "success", "2", "success"]

		self.assertTrue(TestUtils.check(input, expected, 698))
	def test_699(self):
		input = [
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT a string",
			"RPRINT",
			"LOOKUP a",
			"PRINT",
			"END",
		]
		expected = ["", "", "", "", "success", "a//1", "1", "a//1"]

		self.assertTrue(TestUtils.check(input, expected, 699))
	def test_700(self):
		input = [
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 700))
	def test_701(self):
		input = [
			"INSERT d string",
			"ASSIGN d 'UPPERlower'",
			"INSERT y string",
			"END",
			"INSERT d string",
			"INSERT z string",
			"LOOKUP d",
			"RPRINT",
			"ASSIGN z 'UPPERlower'",
			"INSERT c string",
			"RPRINT",
			"ASSIGN c 'abcABC'",
			"LOOKUP d",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 701))
	def test_702(self):
		input = [
			"END",
			"RPRINT",
			"ASSIGN c unimportant",
			"END",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"END",
			"ASSIGN d unimportant",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT b string",
			"LOOKUP b",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 702))
	def test_703(self):
		input = [
			"BEGIN",
			"RPRINT",
			"INSERT b string",
			"LOOKUP b",
			"ASSIGN b 'UPPERlower'",
			"END",
			"PRINT",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"ASSIGN b 789",
			"PRINT",
			"PRINT",
			"RPRINT",
			"LOOKUP b",
			"PRINT",
			"BEGIN random",
			"LOOKUP b",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 703))
	def test_704(self):
		input = [
			"UWAAAA",
			"END",
			"INSERT a number",
			"LOOKUP a",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"INSERT d number",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 704))
	def test_705(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 705))
	def test_706(self):
		input = [
			"RPRINT",
			"INSERT a number",
		]
		expected = ["", "success"]

		self.assertTrue(TestUtils.check(input, expected, 706))
	def test_707(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 707))
	def test_708(self):
		input = [
			"INSERT x number",
			"BEGIN",
			"BEGIN",
			"ASSIGN x 987654",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP x",
			"END",
			"END",
		]
		expected = ["success", "success", "x//0", "x//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 708))
	def test_709(self):
		input = [
			"BEGIN",
			"END",
			"INSERT f_FF string",
			"RPRINT random",
			"INSERT y string",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r number",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 709))
	def test_710(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT f_FF number",
			"BEGIN",
			"ASSIGN _@_$$d 123",
			"PRINT",
			"BEGIN",
			"INSERT d number",
			"LOOKUP f_FF",
			"RPRINT",
			"END",
			"INSERT f_FF number",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN _@_$$d 123"]

		self.assertTrue(TestUtils.check(input, expected, 710))
	def test_711(self):
		input = [
			"PRINT",
			"BEGIN",
			"END",
			"INSERT g_1 string",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"ASSIGN g_1 'a@bc'",
			"RPRINT",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"BEGIN",
			"ASSIGN g_1 '1234ABC'",
			"INSERT z string",
			"PRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN g_1 'a@bc'"]

		self.assertTrue(TestUtils.check(input, expected, 711))
	def test_712(self):
		input = [
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT d string",
			"INSERT y string",
			"END",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 712))
	def test_713(self):
		input = [
			"INSERT d number random",
			"PRINT",
			"LOOKUP d",
			"LOOKUP d",
			"PRINT",
			"ASSIGN 21_3c 123",
			"LOOKUP d",
			"LOOKUP d",
			"ASSIGN d 456",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"END",
			"INSERT z number",
			"RPRINT",
			"ASSIGN z 789",
			"ASSIGN z 987654",
			"PRINT",
			"ASSIGN z 1001",
			"BEGIN",
			"INSERT b number",
			"INSERT a number",
			"END",
		]
		expected = ["Invalid: INSERT d number random"]

		self.assertTrue(TestUtils.check(input, expected, 713))
	def test_714(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 714))
	def test_715(self):
		input = [
			"BEGIN",
			"END",
			"INSERT g_1 number",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 715))
	def test_716(self):
		input = [
			"RPRINT",
			"PRINT random",
			"PRINT",
			"RPRINT",
			"INSERT f_FF number",
			"ASSIGN f_FF abc123",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 716))
	def test_717(self):
		input = [
			"RPRINT",
			"BEGIN",
			"END",
			"ASSIGN b unimportant",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: ASSIGN b unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 717))
	def test_718(self):
		input = [
			"RPRINT",
			"INSERT b number",
			"RPRINT",
			"PRINT",
			"INSERT x number",
			"ASSIGN x 987654",
			"LOOKUP x",
			"INSERT b number",
			"END",
			"INSERT g_1 number",
			"INSERT f_FF string",
			"PRINT",
		]
		expected = ["Redeclared: INSERT b number"]

		self.assertTrue(TestUtils.check(input, expected, 718))
	def test_719(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT c string",
			"ASSIGN c 'HelloWorld'",
			"BEGIN",
			"BEGIN",
			"END",
			"LOOKUP c",
			"END",
			"BEGIN",
			"END",
			"LOOKUP c",
			"END",
		]
		expected = ["", "", "success", "success", "1", "1"]

		self.assertTrue(TestUtils.check(input, expected, 719))
	def test_720(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"INSERT a number",
			"INSERT y string",
			"ASSIGN b unimportant",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN b unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 720))
	def test_721(self):
		input = [
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"LOOKUP y",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"LOOKUP c",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 721))
	def test_722(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT e_123_2r string",
			"BEGIN",
			"ASSIGN e_123_2r 'Test123'",
			"BEGIN",
			"END",
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"RPRINT",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"PRINT",
			"INSERT c string",
			"LOOKUP x",
			"END",
			"INSERT z number",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"END",
			"LOOKUP e_123_2r",
			"INSERT x number",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 722))
	def test_723(self):
		input = [
			"INSERT y number",
			"ASSIGN y 789",
			"END",
			"END",
			"ASSIGN 21_3c 123",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT a string",
			"UWAAAA",
			"ASSIGN a 'Test123'",
			"ASSIGN a '1234ABC'",
			"END",
			"END",
			"END",
			"END",
			"RPRINT",
			"INSERT y number",
			"RPRINT",
			"INSERT g_1 number",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"ASSIGN g_1 1001",
			"BEGIN",
			"LOOKUP g_1",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 723))
	def test_724(self):
		input = [
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
		]
		expected = ["success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 724))
	def test_725(self):
		input = [
			"END",
			"LOOKUP b",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 725))
	def test_726(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 726))
	def test_727(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT c number",
			"RPRINT",
			"INSERT c number",
			"END",
		]
		expected = ["Redeclared: INSERT c number"]

		self.assertTrue(TestUtils.check(input, expected, 727))
	def test_728(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT f_FF number",
			"ASSIGN f_FF 789",
			"PRINT",
			"LOOKUP f_FF",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"ASSIGN b@B((*@ 123",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT g_1 string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 728))
	def test_729(self):
		input = [
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT a number",
			"LOOKUP a",
			"PRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"INSERT b number",
			"INSERT e_123_2r number",
			"PRINT",
		]
		expected = ["", "", "", "", "", "success", "2", "a//2", "a//2", "", "success", "success", "b//0 e_123_2r//0"]

		self.assertTrue(TestUtils.check(input, expected, 729))
	def test_730(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"ASSIGN ()z 123",
			"INSERT f_FF number",
			"END",
			"PRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT a string",
			"ASSIGN a 'HelloWorld'",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 730))
	def test_731(self):
		input = [
			"INSERT x number",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"LOOKUP x",
			"PRINT",
			"END",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"LOOKUP f_FF",
			"PRINT",
			"INSERT d number",
			"ASSIGN d 1001",
			"PRINT",
			"LOOKUP d",
			"END",
			"BEGIN",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 731))
	def test_732(self):
		input = [
			"END",
			"RPRINT",
			"INSERT z string",
			"INSERT g_1 string",
			"INSERT y string",
			"BEGIN",
			"INSERT z number",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"LOOKUP z",
			"RPRINT",
			"ASSIGN g_1 'Test123'",
			"BEGIN",
			"RPRINT",
			"ASSIGN z 1001 random",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"ASSIGN z 123",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP z",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 732))
	def test_733(self):
		input = [
			"PRINT",
			"INSERT x number",
		]
		expected = ["", "success"]

		self.assertTrue(TestUtils.check(input, expected, 733))
	def test_734(self):
		input = [
			"INSERT z number",
			"INSERT c string",
			"RPRINT",
			"INSERT g_1 number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 734))
	def test_735(self):
		input = [
			"END",
			"BEGIN",
			"ASSIGN f_FF unimportant random",
			"RPRINT",
			"INSERT z number",
			"END random",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 735))
	def test_736(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT b number",
			"ASSIGN y unimportant",
			"UWAAAA",
			"ASSIGN b 123 random",
			"ASSIGN b 789",
			"END",
		]
		expected = ["Undeclared: ASSIGN y unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 736))
	def test_737(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"PRINT random",
			"END",
			"END",
			"BEGIN",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 737))
	def test_738(self):
		input = [
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 738))
	def test_739(self):
		input = [
			"RPRINT",
			"INSERT b string",
			"LOOKUP a",
			"PRINT",
			"ASSIGN b '1234ABC'",
			"ASSIGN b 'HelloWorld'",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 string",
			"ASSIGN g_1 'abcABC'",
			"INSERT y number",
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"ASSIGN b 'abcABC'",
			"END",
			"INSERT c number",
			"ASSIGN b 'HelloWorld'",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP a"]

		self.assertTrue(TestUtils.check(input, expected, 739))
	def test_740(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"INSERT a string",
			"BEGIN",
			"LOOKUP a",
			"END",
			"ASSIGN a 'UPPERlower'",
			"PRINT",
			"ASSIGN a '@stArt'",
			"RPRINT",
			"BEGIN",
			"ASSIGN a 'Test123'",
			"INSERT c number random",
			"INSERT d string",
			"BEGIN",
			"INSERT y number",
			"LOOKUP b",
			"PRINT",
			"LOOKUP d",
			"PRINT",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: ASSIGN a '@stArt'"]

		self.assertTrue(TestUtils.check(input, expected, 740))
	def test_741(self):
		input = [
			"END",
			"END",
			"END",
			"INSERT g_1 number",
			"INSERT e_123_2r number",
			"INSERT y string",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"RPRINT random",
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 741))
	def test_742(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 742))
	def test_743(self):
		input = [
			"INSERT x number",
			"PRINT",
			"RPRINT",
		]
		expected = ["success", "x//0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 743))
	def test_744(self):
		input = [
			"RPRINT",
			"INSERT d string random",
			"INSERT a number",
			"ASSIGN d 'HelloWorld'",
			"ASSIGN g_1 unimportant",
			"RPRINT",
		]
		expected = ["Invalid: INSERT d string random"]

		self.assertTrue(TestUtils.check(input, expected, 744))
	def test_745(self):
		input = [
			"END",
			"INSERT a string",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"BEGIN random",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r 'HelloWorld'",
			"RPRINT",
			"UWAAAA",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 745))
	def test_746(self):
		input = [
			"INSERT f_FF string",
			"ASSIGN f_FF 'abcABC'",
			"ASSIGN __ g 123",
			"LOOKUP f_FF",
			"PRINT",
			"RPRINT",
			"LOOKUP f_FF",
			"PRINT",
			"LOOKUP f_FF",
			"INSERT z number",
			"ASSIGN f_FF 'Test123'",
			"LOOKUP z",
			"END",
			"INSERT b number",
		]
		expected = ["Invalid: ASSIGN __ g 123"]

		self.assertTrue(TestUtils.check(input, expected, 746))
	def test_747(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT a number",
			"RPRINT",
			"ASSIGN a 123",
			"END",
			"PRINT",
			"RPRINT",
			"ASSIGN ()z 123",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 747))
	def test_748(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT z number",
			"ASSIGN z 123",
			"RPRINT",
			"INSERT c string",
			"END",
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"END",
			"INSERT f_FF string",
			"ASSIGN 2_3f 123",
			"ASSIGN f_FF '1234ABC'",
			"INSERT d number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 748))
	def test_749(self):
		input = [
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"RPRINT",
			"INSERT d string",
			"INSERT y number",
			"LOOKUP y",
			"RPRINT",
			"INSERT z number",
			"END",
			"BEGIN",
			"INSERT b number",
			"LOOKUP b",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 749))
	def test_750(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP g_1",
			"INSERT f_FF string",
			"PRINT",
			"ASSIGN f_FF 'Test123'",
			"BEGIN",
			"RPRINT",
			"INSERT x string",
			"INSERT c string",
			"END",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"ASSIGN f_FF 'abcABC'",
			"RPRINT",
			"ASSIGN f_FF 'Test123'",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP g_1"]

		self.assertTrue(TestUtils.check(input, expected, 750))
	def test_751(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 751))
	def test_752(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 752))
	def test_753(self):
		input = [
			"ASSIGN z unimportant",
			"END",
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN z unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 753))
	def test_754(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"RPRINT",
			"ASSIGN x 'HelloWorld'",
			"LOOKUP x",
			"LOOKUP x",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["", "success", "x//0", "success", "0", "0", "x//0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 754))
	def test_755(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"PRINT",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 755))
	def test_756(self):
		input = [
			"END",
			"INSERT f_FF number",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP f_FF",
			"ASSIGN f_FF 789",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"ASSIGN f_FF 456",
			"LOOKUP e_123_2r",
			"BEGIN",
			"INSERT f_FF number",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 756))
	def test_757(self):
		input = [
			"INSERT a number",
			"INSERT c string",
			"ASSIGN a 1001",
			"END",
			"END",
			"END",
			"PRINT",
			"END",
			"PRINT",
			"END",
			"END",
			"INSERT f_FF number",
			"LOOKUP f_FF",
			"BEGIN random",
			"BEGIN",
			"PRINT",
			"LOOKUP f_FF",
			"INSERT c string",
			"LOOKUP f_FF",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 757))
	def test_758(self):
		input = [
			"BEGIN",
			"INSERT d string",
			"INSERT a number",
			"ASSIGN d 'HelloWorld'",
			"ASSIGN a 123",
			"PRINT",
			"ASSIGN a 1001",
			"END",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 number",
			"UWAAAA",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT y number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 758))
	def test_759(self):
		input = [
			"BEGIN",
			"INSERT a number",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT e_123_2r string",
			"LOOKUP g_1",
			"BEGIN",
			"INSERT g_1 number",
			"PRINT",
			"INSERT f_FF number",
			"INSERT x string",
			"END",
			"LOOKUP e_123_2r",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"ASSIGN e_123_2r 'UPPERlower'",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP g_1"]

		self.assertTrue(TestUtils.check(input, expected, 759))
	def test_760(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 760))
	def test_761(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 761))
	def test_762(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 762))
	def test_763(self):
		input = [
			"END",
			"INSERT x string",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT g_1 string",
			"END",
			"RPRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 763))
	def test_764(self):
		input = [
			"BEGIN",
			"END",
			"INSERT y string",
			"RPRINT",
			"RPRINT",
			"ASSIGN y 'UPPERlower'",
			"RPRINT",
			"PRINT",
			"BEGIN",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 764))
	def test_765(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT y number",
			"RPRINT",
			"LOOKUP y",
			"ASSIGN y 'HelloWorld'",
			"BEGIN",
			"RPRINT",
			"ASSIGN y 456",
			"RPRINT random",
			"END",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN y 'HelloWorld'"]

		self.assertTrue(TestUtils.check(input, expected, 765))
	def test_766(self):
		input = [
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 766))
	def test_767(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"INSERT b number",
			"LOOKUP b",
			"RPRINT",
			"LOOKUP b",
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT c number",
			"LOOKUP c",
			"END",
			"INSERT z string",
			"PRINT",
		]
		expected = ["", "", "", "success", "1", "b//1", "1", "", "", "success", "1", "success", "z//0"]

		self.assertTrue(TestUtils.check(input, expected, 767))
	def test_768(self):
		print("test_768")
		input = [
			"INSERT d number",
			"RPRINT",
			"BEGIN",
			"LOOKUP d",
			"BEGIN",
			"BEGIN",
			"LOOKUP d",
			"BEGIN",
			"ASSIGN d 123.5",
			"INSERT f_FF string",
			"INSERT y string",
			"PRINT",
			"RPRINT",
			"LOOKUP f_FF",
			"PRINT",
			"RPRINT",
			"ASSIGN f_FF 'UPPERlower'",
			"ASSIGN d 'UPPERlower'",
			"INSERT e_123_2r number",
			"BEGIN random",
			"INSERT e_123_2r string",
			"LOOKUP f_FF",
			"END random",
			"PRINT",
			"END",
			"ASSIGN d 456 random",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN d 123.5"]

		self.assertTrue(TestUtils.check(input, expected, 768))
	def test_769(self):
		print("test_769")
		input = [
			"BEGIN",
			"END",
			"PRINT",
			"INSERT f_FF string",
			"INSERT z string",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"ASSIGN ()z 123",
			"RPRINT",
			"ASSIGN z 'UPPERlower'",
			"LOOKUP f_FF",
			"LOOKUP f_FF",
			"UWAAAA",
			"INSERT c number",
			"ASSIGN f_FF 'HelloWorld'",
			"ASSIGN c 456",
			"ASSIGN z 'abcABC'",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
			"ASSIGN c 456",
			"END",
			"RPRINT",
			"INSERT x number",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 769))
	def test_770(self):
		input = [
			"BEGIN",
			"END",
			"INSERT f_FF number",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 770))
	def test_771(self):
		input = [
			"PRINT",
			"UWAAAA",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 771))
	def test_772(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"BEGIN",
			"INSERT d number",
			"PRINT",
			"END",
			"PRINT",
			"END",
		]
		expected = ["", "success", "success", "y//1 d//2", "y//1"]

		self.assertTrue(TestUtils.check(input, expected, 772))
	def test_773(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT b string",
			"LOOKUP b",
			"INSERT f_FF number",
			"LOOKUP b",
			"END",
			"PRINT",
			"INSERT z number",
			"LOOKUP z",
		]
		expected = ["", "success", "1", "success", "1", "", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 773))
	def test_774(self):
		input = [
			"ASSIGN 2_3f 123",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT b number",
			"RPRINT",
			"ASSIGN b 456",
			"PRINT",
			"LOOKUP b",
			"RPRINT",
			"ASSIGN b 123",
			"ASSIGN b 456",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: ASSIGN 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 774))
	def test_775(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT z string",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 775))
	def test_776(self):
		input = [
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
			"END random",
			"INSERT y number",
			"PRINT",
			"END random",
			"LOOKUP d",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 776))
	def test_777(self):
		input = [
			"INSERT d string",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP d",
			"ASSIGN d 'abcABC'",
			"BEGIN",
			"LOOKUP d",
			"PRINT",
			"LOOKUP d",
			"INSERT d number",
			"INSERT f_FF number",
			"PRINT",
			"PRINT",
			"ASSIGN f_FF 987654",
			"INSERT a string",
			"INSERT x number",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["success", "d//0", "d//0", "0", "success", "0", "d//0", "0", "success", "success", "d//2 f_FF//2", "d//2 f_FF//2", "success", "success", "success", "x//2 a//2 f_FF//2 d//2", "x//2 a//2 f_FF//2 d//2"]

		self.assertTrue(TestUtils.check(input, expected, 777))
	def test_778(self):
		input = [
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT random",
			"INSERT z string",
			"LOOKUP y",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP z",
			"END",
			"ASSIGN z 'UPPERlower'",
			"LOOKUP z",
			"ASSIGN z 'Test123'",
			"INSERT y string",
			"END",
			"RPRINT",
			"PRINT",
			"INSERT d number",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 778))
	def test_779(self):
		input = [
			"RPRINT",
			"BEGIN",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 779))
	def test_780(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 780))
	def test_781(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT x string",
			"ASSIGN x 'HelloWorld'",
			"RPRINT",
			"RPRINT",
			"ASSIGN x '1234ABC'",
			"END",
		]
		expected = ["", "success", "success", "x//1", "x//1", "success"]

		self.assertTrue(TestUtils.check(input, expected, 781))
	def test_782(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"END",
			"UWAAAA",
			"INSERT a string",
			"LOOKUP a",
			"PRINT",
			"LOOKUP a",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 782))
	def test_783(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT c number",
			"ASSIGN c 789",
			"LOOKUP c",
			"PRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT x string",
		]
		expected = ["", "", "success", "success", "1", "c//1", "c//1", "c//1", "c//1", "c//1", "success"]

		self.assertTrue(TestUtils.check(input, expected, 783))
	def test_784(self):
		input = [
			"PRINT",
			"END",
			"END",
			"PRINT",
			"END",
			"INSERT d string",
			"LOOKUP d",
			"LOOKUP d",
			"END random",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT f_FF number",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 784))
	def test_785(self):
		input = [
			"INSERT a number",
			"RPRINT",
			"ASSIGN a 987654",
			"PRINT",
			"PRINT",
			"LOOKUP a",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"ASSIGN a 123",
			"RPRINT",
			"ASSIGN a 987654",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP a",
			"BEGIN",
			"END",
			"INSERT e_123_2r string",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 785))
	def test_786(self):
		input = [
			"INSERT y string",
			"PRINT",
			"BEGIN",
			"INSERT d number",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"END",
			"RPRINT",
			"LOOKUP y",
			"PRINT",
			"PRINT",
			"INSERT d number",
			"UWAAAA",
			"INSERT x number",
			"RPRINT",
			"LOOKUP y",
			"PRINT",
			"INSERT z string",
			"INSERT c string random",
			"PRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 786))
	def test_787(self):
		input = [
			"INSERT c number",
			"ASSIGN c 456 random",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT e_123_2r string",
			"END",
			"END",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT g_1 number",
			"INSERT b number",
			"BEGIN",
			"ASSIGN g_1 1001",
			"LOOKUP z",
			"RPRINT",
			"LOOKUP b",
		]
		expected = ["Invalid: ASSIGN c 456 random"]

		self.assertTrue(TestUtils.check(input, expected, 787))
	def test_788(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 788))
	def test_789(self):
		input = [
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 789))
	def test_790(self):
		input = [
			"RPRINT",
			"END",
			"END",
			"INSERT c number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 790))
	def test_791(self):
		input = [
			"RPRINT",
			"END",
			"END",
			"END",
			"END",
			"ASSIGN c unimportant",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 791))
	def test_792(self):
		input = [
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"INSERT d string",
			"LOOKUP x",
			"END",
			"END",
		]
		expected = ["", "", "", "success", "1", "success", "1"]

		self.assertTrue(TestUtils.check(input, expected, 792))
	def test_793(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"PRINT",
			"END",
			"PRINT",
			"PRINT",
			"UWAAAA",
			"INSERT x string",
			"RPRINT",
			"INSERT z number",
			"END",
			"RPRINT",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 793))
	def test_794(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT f_FF number",
			"PRINT",
			"END",
			"INSERT e_123_2r string",
			"ASSIGN e_123_2r '1234ABC'",
			"BEGIN",
			"PRINT",
			"LOOKUP e_123_2r",
			"INSERT y string random",
			"INSERT f_FF string",
			"BEGIN",
			"ASSIGN y 987654",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 794))
	def test_795(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"INSERT d number",
			"END",
			"PRINT random",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"PRINT",
			"ASSIGN e_123_2r '1234ABC'",
			"RPRINT",
			"RPRINT",
			"INSERT y number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 795))
	def test_796(self):
		input = [
			"INSERT d number",
			"PRINT",
			"BEGIN",
			"ASSIGN d 1001",
			"LOOKUP d",
			"BEGIN",
			"INSERT f_FF string",
			"ASSIGN x unimportant",
			"END",
			"INSERT x string",
			"ASSIGN x 'ab c",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"LOOKUP x",
			"UWAAAA",
			"ASSIGN x 'Test123'",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"ASSIGN x 'Test123'",
			"RPRINT",
			"ASSIGN x 'Test123'",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN x unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 796))
	def test_797(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 797))
	def test_798(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 798))
	def test_799(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 799))
	def test_800(self):
		input = [
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT x number",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 800))
	def test_801(self):
		input = [
			"RPRINT",
			"INSERT a number",
			"UWAAAA",
			"RPRINT",
			"INSERT c string",
			"LOOKUP a",
			"ASSIGN y unimportant",
			"PRINT",
			"LOOKUP c",
			"PRINT",
			"ASSIGN c 'abcABC'",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 801))
	def test_802(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"BEGIN",
			"END",
			"INSERT y number",
			"ASSIGN y 123",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT a number",
			"BEGIN",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 802))
	def test_803(self):
		input = [
			"BEGIN",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT x number",
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["", "success", "x//1", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 803))
	def test_804(self):
		input = [
			"PRINT",
			"END",
			"BEGIN",
			"LOOKUP g_1",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT c number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 804))
	def test_805(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number",
			"PRINT",
			"INSERT z string",
			"PRINT random",
			"INSERT y number",
			"UWAAAA",
			"LOOKUP e_123_2r",
			"ASSIGN e_123_2r '1234ABC'",
			"PRINT",
			"RPRINT",
			"INSERT z string",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"ASSIGN y 987654",
			"PRINT",
			"END",
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"LOOKUP b",
			"BEGIN",
			"INSERT b number",
			"PRINT",
			"INSERT f_FF string",
			"LOOKUP a",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 805))
	def test_806(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 806))
	def test_807(self):
		input = [
			"INSERT e_123_2r number",
			"LOOKUP e_123_2r",
			"RPRINT",
		]
		expected = ["success", "0", "e_123_2r//0"]

		self.assertTrue(TestUtils.check(input, expected, 807))
	def test_808(self):
		input = [
			"INSERT b string",
			"RPRINT",
			"INSERT g_1 string",
			"LOOKUP g_1",
			"RPRINT",
			"LOOKUP b",
			"INSERT d number",
		]
		expected = ["success", "b//0", "success", "0", "g_1//0 b//0", "0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 808))
	def test_809(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"INSERT g_1 string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 809))
	def test_810(self):
		input = [
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"INSERT y string",
			"RPRINT",
			"LOOKUP y",
			"ASSIGN y 123",
			"LOOKUP a",
			"END",
			"PRINT",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN y 123"]

		self.assertTrue(TestUtils.check(input, expected, 810))
	def test_811(self):
		input = [
			"RPRINT",
			"PRINT",
			"END",
			"INSERT f_FF string",
			"BEGIN",
			"ASSIGN _@_$$d 123",
			"INSERT d number",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"ASSIGN f_FF '1234ABC'",
			"ASSIGN d 789",
			"LOOKUP d",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 811))
	def test_812(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"INSERT b number",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"ASSIGN b 456",
			"END",
			"LOOKUP b",
			"LOOKUP b",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"LOOKUP d",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 812))
	def test_813(self):
		input = [
			"INSERT y string",
			"INSERT z number",
			"INSERT a number",
			"LOOKUP a",
			"LOOKUP a",
			"RPRINT",
			"RPRINT random",
			"BEGIN",
			"END",
			"END",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT b number",
			"INSERT d number",
			"LOOKUP d",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 813))
	def test_814(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT y string",
			"LOOKUP y",
			"LOOKUP y",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
			"BEGIN",
			"ASSIGN e_123_2r 1001",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT c number",
			"PRINT",
			"INSERT y string",
			"RPRINT",
			"INSERT e_123_2r string",
			"ASSIGN y 'UPPERlower'",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 814))
	def test_815(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 815))
	def test_816(self):
		input = [
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 816))
	def test_817(self):
		input = [
			"PRINT",
			"PRINT",
			"INSERT z number",
			"BEGIN",
			"BEGIN",
			"END",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 817))
	def test_818(self):
		input = [
			"INSERT y string",
			"BEGIN",
			"LOOKUP y",
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"PRINT",
			"LOOKUP y",
			"END",
		]
		expected = ["success", "0", "y//0", "y//0", "y//0", "0"]

		self.assertTrue(TestUtils.check(input, expected, 818))
	def test_819(self):
		input = [
			"END",
			"BEGIN",
			"INSERT y number",
			"LOOKUP y",
			"INSERT x string",
			"PRINT",
			"INSERT f_FF string",
			"LOOKUP c",
			"END",
			"END",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 819))
	def test_820(self):
		input = [
			"END",
			"RPRINT",
			"BEGIN random",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"PRINT",
			"INSERT e_123_2r number",
			"RPRINT",
			"INSERT g_1 number",
			"PRINT",
			"INSERT y number",
			"LOOKUP y",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 820))
	def test_821(self):
		input = [
			"INSERT d string",
			"PRINT",
			"ASSIGN d 'abcABC'",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"LOOKUP d",
			"LOOKUP d",
			"PRINT",
			"LOOKUP d",
			"END",
			"INSERT y number",
			"PRINT",
			"ASSIGN y 123",
			"LOOKUP y",
			"LOOKUP y",
			"ASSIGN __ g 123",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 821))
	def test_822(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"LOOKUP x",
			"LOOKUP x",
			"ASSIGN x '1234ABC'",
			"ASSIGN x '1234ABC'",
			"ASSIGN x 'Test123' random",
			"INSERT a string",
			"BEGIN",
			"ASSIGN a 'Test123'",
			"END",
			"LOOKUP x",
			"ASSIGN x 'HelloWorld'",
			"INSERT y string",
			"RPRINT",
			"END",
			"PRINT",
			"INSERT x number",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: ASSIGN x 'Test123' random"]

		self.assertTrue(TestUtils.check(input, expected, 822))
	def test_823(self):
		input = [
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r string",
			"END",
			"RPRINT",
			"INSERT z number",
			"INSERT z string",
			"LOOKUP z",
			"BEGIN",
			"ASSIGN z 456",
			"BEGIN",
			"LOOKUP a",
			"RPRINT",
			"ASSIGN z 'UPPERlower' random",
			"ASSIGN z abc123",
			"RPRINT",
			"INSERT f_FF string",
			"INSERT z number",
			"UWAAAA",
			"INSERT c number",
			"INSERT e_123_2r number random",
			"PRINT",
			"ASSIGN z 987654",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 823))
	def test_824(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"INSERT y number",
			"PRINT",
			"PRINT",
			"ASSIGN y 789",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"INSERT 2_3f 123",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"INSERT z number",
			"INSERT a number",
			"INSERT g_1 number",
			"INSERT e_123_2r number",
			"ASSIGN y 'HelloWorld'",
			"PRINT",
			"INSERT _@??e 123",
			"BEGIN",
			"INSERT x string",
			"LOOKUP x",
			"ASSIGN x 'abcABC'",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT 2_3f 123"]

		self.assertTrue(TestUtils.check(input, expected, 824))
	def test_825(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 825))
	def test_826(self):
		input = [
			"INSERT z number",
			"END",
			"UWAAAA",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 826))
	def test_827(self):
		input = [
			"PRINT",
			"END",
			"UWAAAA",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT z string",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 827))
	def test_828(self):
		input = [
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"LOOKUP z",
			"INSERT c number",
			"PRINT",
			"LOOKUP c",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP z"]

		self.assertTrue(TestUtils.check(input, expected, 828))
	def test_829(self):
		input = [
			"INSERT f_FF string",
			"ASSIGN f_FF 'abcABC'",
			"INSERT x string",
			"ASSIGN x 'HelloWorld'",
			"BEGIN",
			"INSERT e_123_2r number",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"LOOKUP e_123_2r",
			"BEGIN",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["success", "success", "success", "success", "success", "1", "f_FF//0 x//0 e_123_2r//1"]

		self.assertTrue(TestUtils.check(input, expected, 829))
	def test_830(self):
		input = [
			"END",
			"BEGIN",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"PRINT random",
			"BEGIN",
			"UWAAAA",
			"END random",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 830))
	def test_831(self):
		input = [
			"BEGIN",
			"INSERT z number",
			"RPRINT",
			"LOOKUP z",
			"PRINT",
			"BEGIN",
			"LOOKUP z",
			"ASSIGN c unimportant",
			"PRINT",
			"ASSIGN z 123a",
			"UWAAAA",
			"END",
			"PRINT",
			"LOOKUP x",
			"INSERT c string",
			"PRINT",
			"BEGIN",
			"INSERT f_FF number",
			"BEGIN",
			"ASSIGN c 'UPPERlower'",
			"ASSIGN c '1234ABC'",
			"INSERT c string",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 831))
	def test_832(self):
		input = [
			"INSERT x string",
			"INSERT a string",
			"ASSIGN a 'UPPERlower'",
			"LOOKUP a",
			"PRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"INSERT c number",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"ASSIGN c 1001",
			"LOOKUP c",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT x number",
			"UWAAAA",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 832))
	def test_833(self):
		input = [
			"RPRINT",
			"RPRINT",
			"END",
			"ASSIGN f_FF unimportant",
			"INSERT a number random",
			"PRINT",
			"LOOKUP a",
			"ASSIGN a 987654",
			"ASSIGN a 456",
			"LOOKUP a",
			"BEGIN",
			"RPRINT",
			"END",
			"ASSIGN a 'abcABC'",
			"END",
			"INSERT x number",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 833))
	def test_834(self):
		input = [
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 834))
	def test_835(self):
		input = [
			"ASSIGN aak e 123",
			"RPRINT",
			"RPRINT",
		]
		expected = ["Invalid: ASSIGN aak e 123"]

		self.assertTrue(TestUtils.check(input, expected, 835))
	def test_836(self):
		input = [
			"PRINT",
			"ASSIGN z unimportant",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"INSERT e_123_2r string",
		]
		expected = ["Undeclared: ASSIGN z unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 836))
	def test_837(self):
		input = [
			"END",
			"INSERT y_12@! 123",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT y string",
			"ASSIGN y 'a@bc'",
			"ASSIGN y 'UPPERlower'",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 837))
	def test_838(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"END",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 838))
	def test_839(self):
		input = [
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"INSERT a number",
			"PRINT",
			"INSERT d number",
			"PRINT",
			"END",
			"END",
			"INSERT a number",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 839))
	def test_840(self):
		input = [
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT z number",
			"END",
			"PRINT",
			"UWAAAA",
			"PRINT",
			"INSERT c number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 840))
	def test_841(self):
		input = [
			"INSERT c number",
			"BEGIN",
			"END",
			"BEGIN",
			"ASSIGN c 987654",
			"END",
			"BEGIN",
			"RPRINT",
			"INSERT f_FF string",
			"END",
			"END",
			"INSERT d string",
			"ASSIGN d 'UPPERlower'",
			"END",
			"ASSIGN 21_3c 123",
			"RPRINT",
			"RPRINT",
			"INSERT a number",
			"PRINT",
			"LOOKUP a",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT d number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 841))
	def test_842(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"END",
			"LOOKUP e_123_2r",
			"RPRINT",
			"INSERT b string",
			"LOOKUP b",
			"ASSIGN b '1234ABC'",
			"INSERT e_123_2r string",
			"INSERT d number",
			"INSERT y number",
			"END",
			"RPRINT",
			"INSERT c string",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP e_123_2r"]

		self.assertTrue(TestUtils.check(input, expected, 842))
	def test_843(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 843))
	def test_844(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 844))
	def test_845(self):
		input = [
			"RPRINT",
			"BEGIN",
			"INSERT b number",
			"ASSIGN c unimportant",
			"END",
			"LOOKUP b",
			"BEGIN",
			"END",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 845))
	def test_846(self):
		input = [
			"INSERT d string",
			"ASSIGN d 'UPPERlower'",
			"ASSIGN d 'HelloWorld'",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP d",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 846))
	def test_847(self):
		input = [
			"INSERT z string",
			"BEGIN",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"INSERT a string random",
			"PRINT",
			"PRINT",
			"LOOKUP b",
			"ASSIGN a 'abcABC'",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT a string random"]

		self.assertTrue(TestUtils.check(input, expected, 847))
	def test_848(self):
		input = [
			"PRINT",
			"RPRINT",
			"RPRINT",
			"INSERT b number",
			"LOOKUP b",
			"BEGIN",
			"INSERT d string",
			"END",
			"LOOKUP b",
			"RPRINT",
			"ASSIGN b 1001",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 848))
	def test_849(self):
		input = [
			"BEGIN",
			"INSERT g_1 string",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
			"LOOKUP g_1",
			"ASSIGN g_1 '1234ABC'",
			"PRINT random",
			"INSERT y number",
			"PRINT",
			"END",
			"INSERT z string",
			"LOOKUP a",
			"RPRINT",
			"END",
			"INSERT b number",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 849))
	def test_850(self):
		input = [
			"PRINT",
			"INSERT a number",
			"LOOKUP a",
			"RPRINT",
			"LOOKUP a",
			"RPRINT",
			"PRINT",
			"ASSIGN a 789",
			"LOOKUP a",
			"INSERT y string",
			"PRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"ASSIGN y 'UPPERlower'",
			"RPRINT",
			"ASSIGN a 987654",
			"PRINT",
			"LOOKUP a",
			"INSERT f_FF string",
			"INSERT b@B((*@ 123",
			"RPRINT",
			"ASSIGN f_FF 'HelloWorld'",
			"RPRINT",
			"END",
		]
		expected = ["Invalid: INSERT b@B((*@ 123"]

		self.assertTrue(TestUtils.check(input, expected, 850))
	def test_851(self):
		input = [
			"INSERT d number",
			"RPRINT",
			"ASSIGN d 1001",
			"LOOKUP d",
			"LOOKUP d",
			"INSERT _@??e 123",
			"LOOKUP d",
			"RPRINT",
			"LOOKUP d",
			"UWAAAA",
			"ASSIGN d 456",
			"BEGIN",
			"ASSIGN d 123",
			"END",
			"RPRINT",
			"BEGIN",
			"LOOKUP d",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"LOOKUP d",
			"RPRINT",
			"INSERT g_1 string",
			"INSERT e_123_2r number",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: INSERT _@??e 123"]

		self.assertTrue(TestUtils.check(input, expected, 851))
	def test_852(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 852))
	def test_853(self):
		input = [
			"END",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 853))
	def test_854(self):
		input = [
			"BEGIN",
			"PRINT",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 854))
	def test_855(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT b number",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT random",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 855))
	def test_856(self):
		input = [
			"RPRINT",
			"END",
			"UWAAAA",
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"INSERT e_123_2r string",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 856))
	def test_857(self):
		input = [
			"INSERT g_1 string",
			"LOOKUP g_1",
			"BEGIN",
			"ASSIGN g_1 'Test123'",
			"ASSIGN g_1 'Test123'",
			"END",
			"LOOKUP g_1",
			"ASSIGN g_1 'abcABC'",
			"INSERT d string",
			"UWAAAA",
			"ASSIGN y_12@! 123",
			"UWAAAA",
			"ASSIGN g_1 '1234ABC'",
			"RPRINT",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 857))
	def test_858(self):
		input = [
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 858))
	def test_859(self):
		input = [
			"END random",
			"PRINT",
			"INSERT b number",
			"ASSIGN b 1001",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT x string",
			"INSERT g_1 number",
			"RPRINT",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 859))
	def test_860(self):
		input = [
			"INSERT b string",
			"INSERT x string",
			"LOOKUP x",
			"BEGIN",
			"ASSIGN b 'Test123'",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"LOOKUP x",
			"ASSIGN b 'UPPERlower'",
			"END",
			"LOOKUP b",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"ASSIGN b 'abcABC'",
			"PRINT",
			"ASSIGN b '1234ABC'",
			"BEGIN",
			"RPRINT",
			"LOOKUP b",
			"ASSIGN b 'HelloWorld'",
			"INSERT x number",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 860))
	def test_861(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 861))
	def test_862(self):
		input = [
			"INSERT e_123_2r number",
			"PRINT",
			"ASSIGN e_123_2r 456",
		]
		expected = ["success", "e_123_2r//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 862))
	def test_863(self):
		input = [
			"END",
			"INSERT y number",
			"END",
			"RPRINT",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 863))
	def test_864(self):
		input = [
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"INSERT e_123_2r number",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["", "", "success", "e_123_2r//1", "e_123_2r//1", "e_123_2r//1"]

		self.assertTrue(TestUtils.check(input, expected, 864))
	def test_865(self):
		input = [
			"BEGIN",
			"INSERT f_FF number",
			"BEGIN",
			"LOOKUP f_FF",
			"RPRINT",
			"BEGIN",
			"ASSIGN f_FF 789 random",
			"ASSIGN f_FF 456",
			"RPRINT",
			"PRINT",
			"ASSIGN f_FF 789",
			"PRINT",
			"ASSIGN f_FF 123",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN f_FF 789 random"]

		self.assertTrue(TestUtils.check(input, expected, 865))
	def test_866(self):
		input = [
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"INSERT c string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 866))
	def test_867(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"PRINT random",
			"PRINT",
			"BEGIN",
			"INSERT y number",
			"ASSIGN y 789",
			"INSERT a string",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 867))
	def test_868(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"LOOKUP x",
			"ASSIGN x 'HelloWorld'",
			"LOOKUP x",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"RPRINT",
			"END",
			"INSERT g_1 number",
			"RPRINT",
			"END",
			"INSERT a number",
			"INSERT f_FF string",
			"INSERT c string",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 868))
	def test_869(self):
		input = [
			"PRINT",
			"INSERT d number",
			"ASSIGN x unimportant",
			"RPRINT",
			"ASSIGN g_1 unimportant",
			"PRINT",
			"RPRINT",
			"PRINT",
			"ASSIGN d 456",
			"INSERT c number",
			"LOOKUP c",
			"LOOKUP c",
			"INSERT z number",
			"RPRINT",
			"ASSIGN 1xyz 123",
			"PRINT",
			"END",
			"END",
			"PRINT random",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN x unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 869))
	def test_870(self):
		input = [
			"LOOKUP e_123_2r",
			"BEGIN",
			"END",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"INSERT y string",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"INSERT a string",
			"RPRINT",
			"INSERT z number",
			"LOOKUP z",
			"ASSIGN a 'abcABC'",
			"END",
			"INSERT f_FF number",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"END",
		]
		expected = ["Undeclared: LOOKUP e_123_2r"]

		self.assertTrue(TestUtils.check(input, expected, 870))
	def test_871(self):
		input = [
			"INSERT x string",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 871))
	def test_872(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT y number",
		]
		expected = ["", "success"]

		self.assertTrue(TestUtils.check(input, expected, 872))
	def test_873(self):
		input = [
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"INSERT d number",
			"INSERT b string",
			"INSERT e_123_2r number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 873))
	def test_874(self):
		input = [
			"BEGIN",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"INSERT e_123_2r number",
			"ASSIGN e_123_2r 1001",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 874))
	def test_875(self):
		input = [
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"INSERT y string",
			"INSERT c string",
			"LOOKUP y",
			"INSERT d number",
			"INSERT x number",
			"RPRINT",
			"RPRINT",
			"INSERT e_123_2r string",
			"INSERT b number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 875))
	def test_876(self):
		input = [
			"BEGIN",
			"END",
			"RPRINT",
			"INSERT z number",
			"INSERT b string",
			"LOOKUP z",
			"ASSIGN b 'Test123'",
			"INSERT d number",
			"RPRINT",
			"PRINT",
			"ASSIGN z 456 random",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"END",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN z 456 random"]

		self.assertTrue(TestUtils.check(input, expected, 876))
	def test_877(self):
		input = [
			"PRINT",
			"BEGIN random",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"INSERT c string",
			"END",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT d number random",
			"BEGIN",
			"ASSIGN d 1001 random",
			"INSERT a string",
			"ASSIGN a 1001",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 877))
	def test_878(self):
		input = [
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"ASSIGN 1xyz 123",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"BEGIN",
			"END",
			"INSERT a number",
			"INSERT y string",
			"INSERT z number",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 878))
	def test_879(self):
		input = [
			"PRINT",
			"BEGIN",
			"INSERT a string",
			"ASSIGN a 'UPPERlower'",
			"PRINT",
			"INSERT y number",
			"INSERT g_1 string",
			"END",
			"INSERT z number",
			"BEGIN",
			"END",
			"ASSIGN z 987654",
			"ASSIGN z 1001",
			"RPRINT",
			"INSERT b number",
			"BEGIN",
			"END",
			"INSERT d number",
			"LOOKUP b",
			"INSERT d string",
			"INSERT d number random",
			"PRINT",
			"INSERT e_123_2r number",
			"INSERT f_FF number",
			"ASSIGN z 456",
			"BEGIN",
			"BEGIN",
		]
		expected = ["Redeclared: INSERT d string"]

		self.assertTrue(TestUtils.check(input, expected, 879))
	def test_880(self):
		input = [
			"INSERT b string",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 880))
	def test_881(self):
		input = [
			"INSERT e_123_2r string",
			"INSERT d string",
			"PRINT",
			"PRINT random",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 881))
	def test_882(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"INSERT g_1 number",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 882))
	def test_883(self):
		input = [
			"END",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"END",
			"INSERT c string",
			"INSERT x string",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 883))
	def test_884(self):
		input = [
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT e_123_2r number",
			"ASSIGN e_123_2r 1001",
			"INSERT ()z 123",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP e_123_2r",
			"PRINT",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 884))
	def test_885(self):
		input = [
			"INSERT x string",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"INSERT g_1 number",
			"END",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 885))
	def test_886(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r number",
			"RPRINT",
			"BEGIN",
			"RPRINT random",
			"END",
			"PRINT",
			"END",
			"PRINT",
			"LOOKUP z",
			"UWAAAA",
			"END",
			"ASSIGN a unimportant",
			"RPRINT",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 886))
	def test_887(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT b string",
			"RPRINT",
			"RPRINT",
			"LOOKUP b",
			"RPRINT",
			"PRINT",
			"LOOKUP b",
			"ASSIGN b 789",
			"INSERT a string",
			"BEGIN",
			"UWAAAA",
			"INSERT f_FF string",
			"END",
			"PRINT",
			"ASSIGN a abc'",
			"PRINT",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["TypeMismatch: ASSIGN b 789"]

		self.assertTrue(TestUtils.check(input, expected, 887))
	def test_888(self):
		input = [
			"PRINT",
			"INSERT y number",
			"ASSIGN y 456",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"INSERT a string",
			"LOOKUP a",
			"ASSIGN a 'HelloWorld'",
			"BEGIN",
			"PRINT",
			"INSERT __ g 123",
			"ASSIGN a 'HelloWorld'",
			"ASSIGN a 'UPPERlower'",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 888))
	def test_889(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 889))
	def test_890(self):
		input = [
			"INSERT b number random",
			"LOOKUP b",
			"BEGIN",
			"LOOKUP b",
			"END",
		]
		expected = ["Invalid: INSERT b number random"]

		self.assertTrue(TestUtils.check(input, expected, 890))
	def test_891(self):
		input = [
			"END",
			"RPRINT",
			"END",
			"END",
			"INSERT c number",
			"RPRINT",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 891))
	def test_892(self):
		input = [
			"RPRINT",
			"ASSIGN y unimportant",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
		]
		expected = ["Undeclared: ASSIGN y unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 892))
	def test_893(self):
		input = [
			"UWAAAA",
			"END",
			"ASSIGN c unimportant",
			"END",
			"PRINT",
			"PRINT",
			"PRINT",
			"INSERT c number",
			"END",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 893))
	def test_894(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"END",
			"INSERT e_123_2r string",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"LOOKUP e_123_2r",
			"END",
			"BEGIN",
			"END",
			"ASSIGN e_123_2r 'abcABC'",
			"RPRINT random",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 894))
	def test_895(self):
		input = [
			"RPRINT",
			"RPRINT",
			"INSERT z string",
			"LOOKUP z",
			"END",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"INSERT z number",
			"ASSIGN 21_3c 123",
			"ASSIGN 1xyz 123",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 895))
	def test_896(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT a number",
			"LOOKUP a",
			"RPRINT",
			"ASSIGN a 987654",
			"BEGIN",
			"UWAAAA",
			"END",
			"INSERT c number",
			"LOOKUP c",
			"ASSIGN a 1001",
			"LOOKUP a",
			"ASSIGN a 123",
			"END",
			"END",
			"END",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 896))
	def test_897(self):
		input = [
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"UWAAAA",
			"END",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"UWAAAA",
			"PRINT",
			"END",
			"INSERT a string",
			"BEGIN",
			"RPRINT",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 897))
	def test_898(self):
		input = [
			"BEGIN",
			"END",
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 898))
	def test_899(self):
		input = [
			"PRINT",
			"RPRINT",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 899))
	def test_900(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 900))
	def test_901(self):
		input = [
			"RPRINT",
			"RPRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
		]
		expected = ["", "", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 901))
	def test_902(self):
		input = [
			"PRINT",
			"INSERT y number",
			"LOOKUP b",
			"LOOKUP y",
			"ASSIGN y 789",
			"INSERT z string",
			"PRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP y",
			"END",
			"ASSIGN y 456",
			"ASSIGN y 987654",
		]
		expected = ["Undeclared: LOOKUP b"]

		self.assertTrue(TestUtils.check(input, expected, 902))
	def test_903(self):
		input = [
			"LOOKUP e_123_2r",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT f_FF number",
			"ASSIGN f_FF 1001",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT x string",
			"RPRINT",
			"LOOKUP x",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP e_123_2r"]

		self.assertTrue(TestUtils.check(input, expected, 903))
	def test_904(self):
		input = [
			"END",
			"INSERT g_1 string",
			"END",
			"PRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 904))
	def test_905(self):
		input = [
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT z string",
			"BEGIN",
			"PRINT",
			"LOOKUP z",
			"PRINT",
			"END",
			"LOOKUP z",
			"PRINT",
			"ASSIGN z 'Test123'",
			"PRINT",
			"PRINT",
			"RPRINT",
			"ASSIGN z 'UPPERlower'",
			"PRINT",
			"PRINT",
			"BEGIN",
			"LOOKUP z",
			"INSERT 1xyz 123",
			"END",
		]
		expected = ["Invalid: INSERT 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 905))
	def test_906(self):
		input = [
			"RPRINT",
			"END",
			"BEGIN",
			"PRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
			"END",
			"RPRINT",
			"INSERT b string",
			"RPRINT",
			"ASSIGN b 'abcABC'",
			"LOOKUP b",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"LOOKUP b",
			"LOOKUP b",
			"END",
			"RPRINT",
			"LOOKUP b",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 906))
	def test_907(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 907))
	def test_908(self):
		input = [
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
		]
		expected = ["", ""]

		self.assertTrue(TestUtils.check(input, expected, 908))
	def test_909(self):
		input = [
			"BEGIN",
			"LOOKUP d",
			"INSERT c number",
			"RPRINT random",
			"ASSIGN c 789",
			"PRINT random",
			"LOOKUP c",
			"END",
		]
		expected = ["Undeclared: LOOKUP d"]

		self.assertTrue(TestUtils.check(input, expected, 909))
	def test_910(self):
		input = [
			"PRINT",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT a string",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 910))
	def test_911(self):
		input = [
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"INSERT a string",
			"END",
			"BEGIN",
			"PRINT",
			"RPRINT random",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: RPRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 911))
	def test_912(self):
		input = [
			"INSERT x string",
			"ASSIGN x 'abcABC'",
			"INSERT g_1 string",
			"BEGIN",
			"END",
			"END",
			"INSERT f_FF string",
			"END",
			"RPRINT",
			"END",
			"PRINT",
			"END random",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 912))
	def test_913(self):
		input = [
			"INSERT g_1 string",
			"LOOKUP g_1",
			"BEGIN",
			"PRINT",
			"ASSIGN g_1 'UPPERlower'",
			"END",
			"PRINT",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"END",
			"BEGIN",
			"INSERT a string",
			"BEGIN",
			"LOOKUP a",
			"PRINT",
			"INSERT g_1 number",
			"RPRINT",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 913))
	def test_914(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number random",
			"BEGIN",
			"INSERT e_123_2r number",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT random",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT x number",
			"RPRINT",
			"INSERT b number",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT e_123_2r number random"]

		self.assertTrue(TestUtils.check(input, expected, 914))
	def test_915(self):
		input = [
			"INSERT c string",
			"INSERT x number",
			"PRINT",
			"PRINT",
			"INSERT g_1 number",
			"ASSIGN x 987654",
			"BEGIN random",
			"RPRINT",
			"END",
			"END",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT y number",
			"INSERT e_123_2r string",
			"PRINT",
			"INSERT x string random",
			"INSERT d number",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"END",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 915))
	def test_916(self):
		input = [
			"PRINT",
			"END",
			"UWAAAA",
			"BEGIN",
			"END",
			"END",
			"INSERT c number",
			"LOOKUP c",
			"END",
			"INSERT x string",
			"INSERT b number",
			"LOOKUP b",
			"LOOKUP b",
			"LOOKUP b",
			"RPRINT",
			"END",
			"RPRINT random",
			"RPRINT",
			"PRINT",
			"PRINT",
			"END",
			"END",
			"END",
			"INSERT y number",
			"ASSIGN y 1001",
			"ASSIGN y 456",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 916))
	def test_917(self):
		input = [
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 917))
	def test_918(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT z number",
			"END",
		]
		expected = ["", "", "", "success"]

		self.assertTrue(TestUtils.check(input, expected, 918))
	def test_919(self):
		input = [
			"PRINT",
			"END",
			"UWAAAA",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 919))
	def test_920(self):
		input = [
			"BEGIN",
			"INSERT g_1 number",
			"BEGIN",
			"BEGIN",
			"LOOKUP g_1 random",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"INSERT c number",
			"LOOKUP g_1",
			"PRINT",
			"END",
			"END random",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: LOOKUP g_1 random"]

		self.assertTrue(TestUtils.check(input, expected, 920))
	def test_921(self):
		input = [
			"PRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"END",
			"BEGIN",
			"INSERT e_123_2r number",
			"END",
			"END",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 921))
	def test_922(self):
		input = [
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT f_FF string",
			"ASSIGN f_FF 'Test123'",
			"PRINT",
			"INSERT f_FF string",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 922))
	def test_923(self):
		input = [
			"INSERT c string",
			"INSERT c string",
			"ASSIGN c 'Test123'",
			"LOOKUP c",
			"ASSIGN c 'Test123'",
			"RPRINT",
			"INSERT b number",
			"ASSIGN c 'UPPERlower'",
			"INSERT d string",
			"INSERT y string",
			"INSERT z string",
			"INSERT a number",
			"LOOKUP b",
			"PRINT",
			"BEGIN",
			"PRINT",
			"INSERT f_FF number",
			"PRINT",
			"PRINT",
			"ASSIGN f_FF 456",
			"LOOKUP y",
			"PRINT",
		]
		expected = ["Redeclared: INSERT c string"]

		self.assertTrue(TestUtils.check(input, expected, 923))
	def test_924(self):
		input = [
			"INSERT x number",
			"BEGIN",
			"LOOKUP x",
			"PRINT",
			"ASSIGN x 1001",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"INSERT d string",
			"BEGIN",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"LOOKUP x",
			"ASSIGN x 1001",
			"INSERT d string",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"RPRINT",
		]
		expected = ["success", "0", "x//0", "success", "x//0", "x//0", "x//0", "success", "d//3 x//0", "d//3 x//0", "d//3 x//0", "0", "success", "success", "d//2 x//0", "d//2 x//0", "x//0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 924))
	def test_925(self):
		input = [
			"BEGIN",
			"PRINT",
			"INSERT f_FF number",
			"END",
			"BEGIN",
			"END",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"END",
			"PRINT",
			"LOOKUP e_123_2r",
			"END",
			"PRINT",
			"INSERT b string",
			"END",
			"INSERT e_123_2r string",
			"INSERT f_FF number",
			"ASSIGN e_123_2r '1234ABC'",
			"UWAAAA",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 925))
	def test_926(self):
		input = [
			"RPRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 926))
	def test_927(self):
		input = [
			"END",
			"INSERT d string random",
			"LOOKUP d",
			"LOOKUP d",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 927))
	def test_928(self):
		input = [
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"INSERT c number",
			"UWAAAA",
			"ASSIGN c 123",
			"ASSIGN y unimportant",
			"RPRINT",
			"INSERT x string",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 928))
	def test_929(self):
		input = [
			"RPRINT",
			"INSERT a string",
			"PRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT y number",
			"BEGIN",
			"RPRINT",
			"INSERT y string",
			"INSERT e_123_2r number",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 929))
	def test_930(self):
		input = [
			"PRINT",
			"INSERT x number",
			"BEGIN",
			"BEGIN",
			"BEGIN",
			"ASSIGN x 987654",
			"ASSIGN x 456",
			"LOOKUP x",
			"ASSIGN x 789",
			"LOOKUP x",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["", "success", "success", "success", "0", "success", "0", "x//0", "x//0", "x//0"]

		self.assertTrue(TestUtils.check(input, expected, 930))
	def test_931(self):
		input = [
			"INSERT x number",
			"PRINT",
			"LOOKUP x",
			"RPRINT",
			"BEGIN",
			"UWAAAA",
			"LOOKUP x",
			"LOOKUP x",
			"INSERT d string",
			"RPRINT",
			"ASSIGN x 123",
			"BEGIN",
			"ASSIGN x 987654",
			"LOOKUP b",
			"END",
			"ASSIGN x 987654",
			"ASSIGN x 123",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 931))
	def test_932(self):
		input = [
			"PRINT",
			"ASSIGN _@??e 123",
			"INSERT x string",
			"END",
			"RPRINT",
			"INSERT e_123_2r number",
			"END",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT x string",
			"BEGIN",
			"END",
			"LOOKUP x",
			"LOOKUP x",
			"RPRINT",
			"END",
			"INSERT a string",
		]
		expected = ["Invalid: ASSIGN _@??e 123"]

		self.assertTrue(TestUtils.check(input, expected, 932))
	def test_933(self):
		input = [
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"END",
			"END",
			"END",
			"LOOKUP y",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"LOOKUP f_FF",
			"END",
			"INSERT f_FF number",
			"PRINT",
			"BEGIN",
			"END",
			"LOOKUP f_FF",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 933))
	def test_934(self):
		input = [
			"INSERT z string",
			"ASSIGN z '1234ABC'",
			"END random",
			"INSERT d number",
			"INSERT e_123_2r string",
			"RPRINT",
			"INSERT f_FF string",
			"RPRINT",
			"RPRINT",
			"LOOKUP b",
			"END",
			"INSERT g_1 string",
			"END",
			"PRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"END",
		]
		expected = ["Invalid: END random"]

		self.assertTrue(TestUtils.check(input, expected, 934))
	def test_935(self):
		input = [
			"INSERT c number",
		]
		expected = ["success"]

		self.assertTrue(TestUtils.check(input, expected, 935))
	def test_936(self):
		input = [
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 936))
	def test_937(self):
		input = [
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT y number",
			"LOOKUP y",
			"ASSIGN y 789",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 937))
	def test_938(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"INSERT a string",
			"END",
			"BEGIN",
			"RPRINT",
		]
		expected = ["UnclosedBlock: 2"]

		self.assertTrue(TestUtils.check(input, expected, 938))
	def test_939(self):
		input = [
			"RPRINT",
			"END",
			"END",
			"PRINT",
			"INSERT y number",
			"BEGIN",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP y",
			"ASSIGN y 789",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 939))
	def test_940(self):
		input = [
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"INSERT a string",
			"BEGIN",
			"INSERT c number random",
			"LOOKUP c",
			"END",
			"RPRINT",
			"PRINT",
			"ASSIGN a 'ab c",
			"INSERT e_123_2r number",
			"ASSIGN e_123_2r 1001",
			"INSERT y number",
			"ASSIGN x unimportant",
		]
		expected = ["Invalid: INSERT c number random"]

		self.assertTrue(TestUtils.check(input, expected, 940))
	def test_941(self):
		input = [
			"UWAAAA",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"INSERT g_1 string random",
			"LOOKUP g_1",
			"PRINT",
			"ASSIGN g_1 'HelloWorld'",
			"LOOKUP g_1",
			"LOOKUP g_1",
			"END",
			"INSERT _@_$$d 123",
			"RPRINT random",
			"RPRINT",
			"INSERT x string",
			"PRINT",
			"RPRINT",
			"PRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 941))
	def test_942(self):
		input = [
			"ASSIGN e_123_2r unimportant",
			"RPRINT",
			"PRINT",
			"INSERT y number",
			"BEGIN",
			"END",
			"PRINT",
			"ASSIGN y 987654",
			"LOOKUP f_FF",
			"ASSIGN y abc123",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP y",
			"LOOKUP y",
			"BEGIN random",
			"END",
			"LOOKUP y",
			"END",
			"END",
			"BEGIN",
			"PRINT",
			"INSERT b number",
			"LOOKUP b",
		]
		expected = ["Undeclared: ASSIGN e_123_2r unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 942))
	def test_943(self):
		input = [
			"PRINT",
			"INSERT e_123_2r number",
			"INSERT g_1 number",
			"LOOKUP b",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"RPRINT",
			"PRINT",
			"INSERT c string",
			"ASSIGN y unimportant",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"END",
			"INSERT f_FF number",
			"ASSIGN e_123_2r 987654",
			"ASSIGN c 'HelloWorld'",
			"INSERT z string",
			"PRINT",
			"ASSIGN c 'Test123'",
			"BEGIN",
			"ASSIGN d unimportant",
			"UWAAAA",
			"END",
			"RPRINT",
			"RPRINT",
		]
		expected = ["Undeclared: LOOKUP b"]

		self.assertTrue(TestUtils.check(input, expected, 943))
	def test_944(self):
		input = [
			"PRINT",
		]
		expected = [""]

		self.assertTrue(TestUtils.check(input, expected, 944))
	def test_945(self):
		input = [
			"INSERT d number",
			"INSERT g_1 number",
			"BEGIN",
			"LOOKUP g_1",
			"END",
		]
		expected = ["success", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 945))
	def test_946(self):
		input = [
			"INSERT z number",
			"BEGIN",
			"PRINT",
			"END",
			"PRINT",
			"RPRINT",
			"INSERT b number",
		]
		expected = ["success", "z//0", "z//0", "z//0", "success"]

		self.assertTrue(TestUtils.check(input, expected, 946))
	def test_947(self):
		input = [
			"END",
			"INSERT y number",
			"INSERT c number",
			"RPRINT",
			"LOOKUP c",
			"INSERT f_FF string",
			"END",
			"RPRINT",
			"BEGIN",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 947))
	def test_948(self):
		input = [
			"END",
			"END",
			"INSERT z string",
			"END random",
			"PRINT",
			"END",
			"END",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 948))
	def test_949(self):
		input = [
			"RPRINT",
			"END",
			"RPRINT",
			"RPRINT",
			"ASSIGN c unimportant",
			"BEGIN",
			"RPRINT",
			"INSERT z string",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 949))
	def test_950(self):
		input = [
			"RPRINT",
			"INSERT x string",
			"ASSIGN x 'HelloWorld' random",
			"LOOKUP z",
			"LOOKUP x",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"ASSIGN x '1234ABC'",
			"RPRINT",
			"INSERT e_123_2r string",
			"LOOKUP e_123_2r",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"INSERT e_123_2r number random",
			"INSERT y string",
			"UWAAAA",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN x 'HelloWorld' random"]

		self.assertTrue(TestUtils.check(input, expected, 950))
	def test_951(self):
		input = [
			"RPRINT",
			"PRINT random",
			"INSERT g_1 string",
			"RPRINT",
			"INSERT c number",
			"BEGIN",
			"PRINT",
			"LOOKUP g_1",
			"LOOKUP c",
			"BEGIN",
			"END",
			"ASSIGN c 1001",
			"INSERT b number random",
			"END",
			"END",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END random",
			"INSERT x number",
			"PRINT",
			"PRINT",
			"INSERT d string",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: PRINT random"]

		self.assertTrue(TestUtils.check(input, expected, 951))
	def test_952(self):
		input = [
			"ASSIGN f_FF unimportant",
			"PRINT",
			"PRINT",
			"RPRINT",
			"INSERT z string",
			"PRINT",
			"PRINT",
			"BEGIN",
			"INSERT _@_$$d 123",
			"LOOKUP z",
			"PRINT",
			"RPRINT random",
			"PRINT",
			"END",
			"RPRINT",
			"LOOKUP z",
			"BEGIN",
			"PRINT",
			"LOOKUP z",
			"PRINT",
			"LOOKUP z",
			"ASSIGN z '1234ABC'",
			"RPRINT",
			"ASSIGN z 'UPPERlower'",
			"END",
		]
		expected = ["Undeclared: ASSIGN f_FF unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 952))
	def test_953(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 953))
	def test_954(self):
		input = [
			"RPRINT",
			"ASSIGN ()z 123",
		]
		expected = ["Invalid: ASSIGN ()z 123"]

		self.assertTrue(TestUtils.check(input, expected, 954))
	def test_955(self):
		input = [
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["", "", "", ""]

		self.assertTrue(TestUtils.check(input, expected, 955))
	def test_956(self):
		input = [
			"INSERT e_123_2r number",
			"RPRINT",
			"INSERT g_1 number",
			"PRINT",
			"ASSIGN 1xyz 123",
			"BEGIN",
			"ASSIGN g_1 789",
			"RPRINT",
			"RPRINT",
			"ASSIGN g_1 1001",
			"END",
		]
		expected = ["Invalid: ASSIGN 1xyz 123"]

		self.assertTrue(TestUtils.check(input, expected, 956))
	def test_957(self):
		input = [
			"INSERT b string",
			"ASSIGN b 'HelloWorld'",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"INSERT b string random",
			"ASSIGN c unimportant random",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"END",
			"LOOKUP b",
			"ASSIGN b 456",
		]
		expected = ["Invalid: INSERT b string random"]

		self.assertTrue(TestUtils.check(input, expected, 957))
	def test_958(self):
		input = [
			"END",
			"INSERT f_FF number",
			"RPRINT",
			"END",
			"BEGIN",
			"END",
			"PRINT",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 958))
	def test_959(self):
		input = [
			"BEGIN",
			"RPRINT",
			"PRINT",
			"END",
			"BEGIN",
			"INSERT c string",
			"RPRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"END",
			"PRINT",
			"UWAAAA",
			"BEGIN",
			"END",
			"END",
			"BEGIN",
			"END",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 959))
	def test_960(self):
		input = [
			"BEGIN",
			"RPRINT",
			"END",
			"INSERT x string",
			"LOOKUP x",
			"RPRINT",
			"LOOKUP x",
			"BEGIN",
			"END",
			"ASSIGN x '1234ABC'",
			"LOOKUP x",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"ASSIGN x 'abcABC'",
			"ASSIGN aak e 123",
			"PRINT",
			"PRINT",
			"BEGIN",
			"ASSIGN x 'abcABC'",
			"RPRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: ASSIGN aak e 123"]

		self.assertTrue(TestUtils.check(input, expected, 960))
	def test_961(self):
		input = [
			"RPRINT",
			"RPRINT",
			"END",
			"RPRINT",
			"PRINT random",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"END",
			"PRINT",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"INSERT y string",
			"PRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 961))
	def test_962(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 962))
	def test_963(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 963))
	def test_964(self):
		input = [
			"PRINT",
			"INSERT f_FF number",
			"INSERT z number",
			"ASSIGN z 789",
			"LOOKUP z random",
		]
		expected = ["Invalid: LOOKUP z random"]

		self.assertTrue(TestUtils.check(input, expected, 964))
	def test_965(self):
		input = [
			"PRINT",
			"END",
			"END",
			"RPRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 965))
	def test_966(self):
		input = [
			"END",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"UWAAAA",
			"BEGIN",
			"BEGIN",
			"INSERT a number",
			"END",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 966))
	def test_967(self):
		input = [
			"INSERT y number",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"INSERT a number",
			"RPRINT",
			"RPRINT",
			"ASSIGN y 789",
			"RPRINT",
			"RPRINT",
			"BEGIN random",
			"ASSIGN y 789",
		]
		expected = ["Invalid: BEGIN random"]

		self.assertTrue(TestUtils.check(input, expected, 967))
	def test_968(self):
		input = [
			"END",
			"RPRINT",
			"ASSIGN d unimportant",
			"INSERT __ g 123",
			"INSERT z number",
			"ASSIGN z 1001",
			"LOOKUP z",
			"INSERT x string",
			"PRINT",
			"ASSIGN d unimportant",
			"PRINT",
			"LOOKUP x",
			"ASSIGN z 987654",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"END",
			"BEGIN",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 968))
	def test_969(self):
		input = [
			"BEGIN",
			"BEGIN",
			"INSERT x number",
			"BEGIN",
			"BEGIN",
			"LOOKUP x",
			"LOOKUP x",
			"BEGIN",
			"INSERT b string",
			"LOOKUP b",
			"ASSIGN x 987654",
			"ASSIGN b 'HelloWorld'",
			"END",
			"RPRINT",
			"PRINT",
			"END",
			"ASSIGN x 789",
			"ASSIGN x 987654",
			"END",
			"LOOKUP x",
			"INSERT f_FF string",
			"PRINT",
			"END",
			"END",
		]
		expected = ["success", "2", "2", "success", "5", "success", "success", "x//2", "x//2", "success", "success", "2", "success", "x//2 f_FF//2"]

		self.assertTrue(TestUtils.check(input, expected, 969))
	def test_970(self):
		input = [
			"BEGIN",
			"BEGIN",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN y unimportant",
			"END",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
			"BEGIN",
			"INSERT x string",
			"ASSIGN x '1234ABC'",
			"BEGIN",
			"RPRINT",
			"LOOKUP x",
			"LOOKUP x",
			"LOOKUP x",
			"BEGIN",
			"LOOKUP x",
			"END",
			"PRINT",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN y unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 970))
	def test_971(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"INSERT a string",
			"BEGIN",
			"LOOKUP a",
			"LOOKUP a",
			"ASSIGN a 'UPPERlower'",
			"BEGIN",
			"ASSIGN a 'abcABC'",
			"RPRINT",
			"PRINT",
			"LOOKUP a random",
			"ASSIGN a 'Test123'",
			"BEGIN",
			"RPRINT",
			"PRINT",
			"LOOKUP a",
			"END",
			"PRINT",
			"ASSIGN a 123",
			"BEGIN",
			"LOOKUP a",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"UWAAAA",
			"ASSIGN a 'abc! 1'",
			"ASSIGN a 'Test123'",
			"END",
			"END",
			"END",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: LOOKUP a random"]

		self.assertTrue(TestUtils.check(input, expected, 971))
	def test_972(self):
		input = [
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 972))
	def test_973(self):
		input = [
			"RPRINT",
			"BEGIN",
			"PRINT",
			"INSERT d string",
			"LOOKUP d",
			"ASSIGN d '1234ABC'",
			"END",
		]
		expected = ["", "", "success", "1", "success"]

		self.assertTrue(TestUtils.check(input, expected, 973))
	def test_974(self):
		input = [
			"END",
			"BEGIN",
			"PRINT",
			"INSERT z string",
			"INSERT x number",
			"BEGIN",
			"LOOKUP x",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 974))
	def test_975(self):
		input = [
			"LOOKUP b",
			"PRINT",
			"BEGIN",
			"INSERT y string",
			"END",
			"PRINT",
			"UWAAAA",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"END",
		]
		expected = ["Undeclared: LOOKUP b"]

		self.assertTrue(TestUtils.check(input, expected, 975))
	def test_976(self):
		input = [
			"LOOKUP x",
			"INSERT x string",
			"INSERT a string",
			"BEGIN",
			"ASSIGN a 'UPPERlower'",
			"PRINT",
			"ASSIGN a 'HelloWorld'",
			"ASSIGN x abc'",
			"PRINT",
			"INSERT f_FF string",
			"BEGIN",
			"END",
			"RPRINT",
			"ASSIGN a 'abcABC'",
			"ASSIGN a 'HelloWorld'",
			"END random",
		]
		expected = ["Undeclared: LOOKUP x"]

		self.assertTrue(TestUtils.check(input, expected, 976))
	def test_977(self):
		input = [
			"INSERT y number",
			"INSERT z number",
			"ASSIGN y 789",
			"END",
			"END",
			"PRINT",
			"END",
			"INSERT c number",
			"ASSIGN c 123",
			"RPRINT",
			"ASSIGN c 123",
			"END",
			"BEGIN",
			"END",
			"END",
			"END",
			"INSERT c number",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 977))
	def test_978(self):
		input = [
			"INSERT f_FF string",
			"LOOKUP f_FF",
			"INSERT y number",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"ASSIGN y 789",
			"INSERT x string random",
			"PRINT",
			"INSERT c string",
			"UWAAAA",
			"BEGIN",
			"PRINT",
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"ASSIGN f_FF 'UPPERlower'",
			"PRINT",
			"END",
			"END",
			"INSERT y_12@! 123",
			"PRINT",
			"END",
			"END",
			"END",
		]
		expected = ["Invalid: INSERT x string random"]

		self.assertTrue(TestUtils.check(input, expected, 978))
	def test_979(self):
		input = [
			"INSERT x string",
			"RPRINT",
			"INSERT z number",
			"RPRINT",
			"RPRINT",
			"ASSIGN z 456",
			"PRINT",
			"BEGIN",
			"INSERT a number",
			"ASSIGN z 123",
			"PRINT",
			"BEGIN",
			"PRINT",
			"END",
			"LOOKUP x",
			"INSERT d string",
			"LOOKUP d",
			"PRINT",
			"ASSIGN d 'Test123'",
			"BEGIN",
			"END",
			"RPRINT",
			"PRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["success", "x//0", "success", "z//0 x//0", "z//0 x//0", "success", "x//0 z//0", "success", "success", "x//0 z//0 a//1", "x//0 z//0 a//1", "0", "success", "1", "x//0 z//0 a//1 d//1", "success", "d//1 a//1 z//0 x//0", "x//0 z//0 a//1 d//1"]

		self.assertTrue(TestUtils.check(input, expected, 979))
	def test_980(self):
		input = [
			"BEGIN",
			"PRINT",
			"RPRINT",
			"PRINT",
			"END",
			"INSERT d number",
			"LOOKUP d",
			"END",
			"BEGIN",
			"PRINT",
			"BEGIN",
			"RPRINT",
			"RPRINT",
			"END",
			"PRINT",
			"BEGIN",
			"ASSIGN c unimportant",
			"END",
			"PRINT",
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 980))
	def test_981(self):
		input = [
			"END",
			"PRINT",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 981))
	def test_982(self):
		input = [
			"BEGIN",
			"END",
			"BEGIN",
		]
		expected = ["UnclosedBlock: 1"]

		self.assertTrue(TestUtils.check(input, expected, 982))
	def test_983(self):
		input = [
			"PRINT",
			"BEGIN",
			"UWAAAA",
			"END",
			"BEGIN",
			"END",
			"INSERT z number",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 983))
	def test_984(self):
		input = [
			"RPRINT",
			"INSERT a number",
			"LOOKUP a",
			"BEGIN",
			"ASSIGN a 123",
			"END",
			"LOOKUP a",
			"BEGIN",
			"END",
		]
		expected = ["", "success", "0", "success", "0"]

		self.assertTrue(TestUtils.check(input, expected, 984))
	def test_985(self):
		input = [
			"ASSIGN c unimportant",
			"END",
			"RPRINT",
			"INSERT a number",
			"ASSIGN a 987654",
			"LOOKUP a",
			"END",
			"PRINT",
			"BEGIN",
			"INSERT d number",
			"END",
			"UWAAAA",
			"RPRINT",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 985))
	def test_986(self):
		input = [
			"BEGIN",
			"BEGIN",
			"END",
			"PRINT",
			"PRINT",
			"RPRINT",
			"UWAAAA",
			"INSERT c string",
			"LOOKUP c random",
			"END",
			"INSERT y string",
			"RPRINT",
			"PRINT",
			"ASSIGN y 'Test123'",
			"ASSIGN y 'abcABC'",
			"ASSIGN y 'Test123'",
			"LOOKUP y",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 986))
	def test_987(self):
		input = [
			"INSERT x number",
			"LOOKUP x",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"LOOKUP x",
			"INSERT z number",
			"UWAAAA",
			"END",
			"ASSIGN x 456",
			"BEGIN",
			"RPRINT",
			"END",
			"ASSIGN x 1001",
			"RPRINT",
			"RPRINT",
			"END",
			"BEGIN",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 987))
	def test_988(self):
		input = [
			"RPRINT",
			"PRINT",
			"PRINT",
			"PRINT",
			"RPRINT",
			"ASSIGN c unimportant",
			"INSERT a number",
			"PRINT",
			"INSERT g_1 string random",
			"ASSIGN a 789",
			"RPRINT",
			"ASSIGN g_1 '1234ABC'",
			"ASSIGN g_1 'HelloWorld'",
			"LOOKUP a",
			"END",
			"END",
		]
		expected = ["Undeclared: ASSIGN c unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 988))
	def test_989(self):
		input = [
			"RPRINT",
			"BEGIN",
			"BEGIN",
			"END",
			"END",
			"RPRINT",
			"END",
			"INSERT y string",
			"PRINT",
			"RPRINT",
			"RPRINT",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"LOOKUP y",
			"PRINT",
			"LOOKUP y",
			"ASSIGN y 'UPPERlower'",
			"LOOKUP d",
			"PRINT",
			"LOOKUP y",
			"LOOKUP y",
			"LOOKUP y",
			"BEGIN",
			"END",
			"LOOKUP y",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 989))
	def test_990(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 990))
	def test_991(self):
		input = [
			"END",
			"END",
			"BEGIN",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 991))
	def test_992(self):
		input = [
			"BEGIN",
			"INSERT e_123_2r string",
			"END",
			"BEGIN",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"END",
			"END",
			"END",
		]
		expected = ["success", ""]

		self.assertTrue(TestUtils.check(input, expected, 992))
	def test_993(self):
		input = [
			"BEGIN",
			"INSERT d string",
			"ASSIGN d 'UPPERlower' random",
			"INSERT f_FF string",
			"INSERT z string",
			"LOOKUP f_FF",
			"PRINT",
			"END",
		]
		expected = ["Invalid: ASSIGN d 'UPPERlower' random"]

		self.assertTrue(TestUtils.check(input, expected, 993))
	def test_994(self):
		input = [
			"PRINT",
			"INSERT z number",
			"PRINT",
			"RPRINT",
			"END",
			"INSERT x number",
			"BEGIN",
			"RPRINT",
			"ASSIGN x 987654",
			"ASSIGN 21_3c 123",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 994))
	def test_995(self):
		input = [
			"PRINT",
			"INSERT g_1 number",
			"LOOKUP g_1",
			"LOOKUP y",
			"END",
			"BEGIN",
			"PRINT",
			"UWAAAA",
			"INSERT b string",
			"ASSIGN b '1234ABC'",
			"ASSIGN b 'HelloWorld'",
			"LOOKUP b",
			"INSERT x string",
			"RPRINT",
			"ASSIGN b 'Test123'",
			"LOOKUP f_FF",
			"ASSIGN b 'UPPERlower'",
		]
		expected = ["Undeclared: LOOKUP y"]

		self.assertTrue(TestUtils.check(input, expected, 995))
	def test_996(self):
		print("test_996")
		input = [
			"ASSIGN z unimportant",
			"RPRINT",
			"INSERT c string",
			"INSERT z string",
			"LOOKUP c",
			"ASSIGN z 'HelloWorld'",
			"BEGIN",
			"LOOKUP z",
			"LOOKUP z",
			"ASSIGN c 'UPPERlower'",
			"END",
			"ASSIGN z 'HelloWorld'",
			"END",
			"END",
			"INSERT e_123_2r number",
			"END",
			"PRINT",
			"INSERT a number",
			"LOOKUP a",
			"INSERT e_123_2r number",
			"INSERT g_1 string random",
		]
		expected = ["Undeclared: ASSIGN z unimportant"]

		self.assertTrue(TestUtils.check(input, expected, 996))
	def test_997(self):
		print("test_997")
		input = [
			"PRINT",
			"PRINT",
			"UWAAAA",
			"END",
			"INSERT a string",
			"LOOKUP a",
			"PRINT",
			"ASSIGN a 'HelloWorld'",
			"END",
			"INSERT b string",
			"INSERT g_1 string",
			"INSERT f_FF number",
			"RPRINT",
			"END",
			"RPRINT",
			"INSERT x string",
			"BEGIN",
			"RPRINT",
		]
		expected = ["Invalid: UWAAAA"]

		self.assertTrue(TestUtils.check(input, expected, 997))
	def test_998(self):
		input = [
			"RPRINT",
			"END",
			"PRINT",
			"PRINT",
			"PRINT",
			"ASSIGN x unimportant",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN",
			"PRINT",
			"END",
			"RPRINT",
			"BEGIN",
			"RPRINT",
			"BEGIN random",
			"END",
			"RPRINT",
			"END",
		]
		expected = ["UnknownBlock"]

		self.assertTrue(TestUtils.check(input, expected, 998))
	def test_999(self):
		input = [
		]
		expected = []

		self.assertTrue(TestUtils.check(input, expected, 999))
