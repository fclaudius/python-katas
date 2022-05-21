import codewars_test as test

from main import solution

test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
test.assert_equals(solution("know NewFirstGood"), "know New First Good")
