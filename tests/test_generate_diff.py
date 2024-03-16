from gendiff_package.generate_diff import generate_diff


def test_generate_diff():
    file_path_1 = 'gendiff_package/file1.json'
    file_path_2 = 'gendiff_package/file2.json'
    assert generate_diff(file_path_1, file_path_2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
