# pytest_flags

This project is a Python project that utilizes the pytest framework for testing. It aims to demonstrate the usage of various pytest flags and options.


## Usage

To run the tests, use the following command:

###
```bash
make test
```
###

To run the tests with a specific keyword, use the following command:

###
```bash
make test-keyword keyword="book"
```

###


To run the tests with exclude keyword, use the following command:

###
```bash
make test-exclude-keyword keyword="edge_case"
```

###


To run the tests with a specific keyword and exclude keyword, use the following command:

###
```bash
make test-keyword keyword="book and not edge_case"
```

###

To run the tests with a specific marker, use the following command:

###
```bash
make test-marker marker="success"
```
###

To run the tests with a specific marker and exclude marker, use the following command:

###
```bash
make test-marker marker="success and not slow"
```
###

To run the tests with a specific parametrization, use the following command:

###
```bash
make test-parametrize
```
###

To run the tests with a specific file, use the following command:

###
```bash
make test-file file=tests/test_more_sample_test_cases.py
```
###

To run the tests with a specific file and a specific test case, use the following command:

###
```bash
make test-file file=tests/test_more_sample_test_cases.py::test_create_book_failure
```
###

To run the tests with a specific file and a specific test case and specific parametrized option, use the following command:

###
```bash
make test-file file="tests/test_more_sample_test_cases.py::test_create_book_failure[-1]"
```
###

To run the tests with a specific file and a specific test case in case it needs to add escape character, use the following command:

###
```bash
make test-file file="tests/test_more_sample_test_cases.py::test_create_book_success[Book\ A-Author\ A-10]"
```
###

To run the test(s) that last failed (if not run all tests) with a specific flag, use the following command:

###
```bash
make test-custom flag="--lf"
```
###

To run the test(s) that failed first (if not run all tests) with a specific flag, use the following command:

###
```bash
make test-custom flag="--ff"
```
###

To run the test(s) that new first and then run all tests with a specific flag, use the following command:

###
```bash
make test-custom flag="--nf"
```

###

To debug your tests by using `breakpoint()`, use the following command:

Simply put the `breakpoint` wherever you want to debug and you can track your code by using [pdb](https://docs.python.org/3/library/pdb.html#debugger-commands) commands

###
```bash
make test-debug
```

###

To debug your tests by using `assert 0`, use the following command:

You can put `assert 0` into the test case you want debug with `pdb` commands

###
```bash
make test-debug-alternative
```


## Available Flags

The project showcases the usage of the following pytest flags:

- `-v` or `--verbose`: Increases the verbosity of the test output.
- `-k EXPRESSION`: Only runs tests that match the given expression.
- `-m MARKEXPR`: Only runs tests that have the specified marker.

For more information on pytest flags and options, refer to the [pytest documentation](https://docs.pytest.org/en/latest/usage.html#pytest-command-line-flags).
