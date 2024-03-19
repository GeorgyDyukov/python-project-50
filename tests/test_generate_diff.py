from gendiff_package.generate_diff import generate_diff


def test_generate_diff():
    file_path_1 = 'tests/fixtures/file1.json'
    file_path_2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result_diff_plain_json.txt', 'r') as file:
        exp_result = file.read()
    assert generate_diff(file_path_1, file_path_2) == exp_result
