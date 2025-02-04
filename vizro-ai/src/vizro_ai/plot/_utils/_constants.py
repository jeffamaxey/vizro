"""File to store all constants."""

WHITELISTED_PACKAGES = [
    "pandas",
    "numpy",
    "vizro",
    "plotly",
    "datetime",
    "matplotlib",
    "dash",
    "scipy",
    "sklearn",
    "random",
]

WHITELISTED_BUILTINS = [
    # '__name__',
    # '__doc__',
    # '__package__',
    # '__loader__',
    # '__spec__',
    # '__build_class__',
    # '__import__',
    "abs",
    "all",
    "any",
    # 'ascii',
    # 'bin',
    # 'breakpoint',
    # 'callable',
    # 'chr',
    # 'compile',
    # 'delattr',
    # 'dir',
    # 'divmod',
    # 'eval',
    # 'exec',
    # 'format',
    # 'getattr',
    # 'globals',
    # 'hasattr',
    # 'hash',
    # 'hex',
    # 'id',
    # 'input',
    # 'isinstance',
    # 'issubclass',
    "iter",
    # 'aiter',
    "len",
    # 'locals',
    "max",
    "min",
    "next",
    # 'anext',
    # 'oct',
    # 'ord',
    # 'pow',
    "print",
    # 'repr',
    "round",
    # 'setattr',
    "sorted",
    "sum",
    # 'vars',
    "None",
    # 'Ellipsis',
    # 'NotImplemented',
    "False",
    "True",
    "bool",
    # 'memoryview',
    # 'bytearray',
    # 'bytes',
    # 'classmethod',
    # 'complex',
    "dict",
    "enumerate",
    "filter",
    "float",
    # 'frozenset',
    # 'property',
    "int",
    "list",
    "map",
    # 'object',
    "range",
    "reversed",
    "set",
    # 'slice',
    # 'staticmethod',
    "str",
    # 'super',
    "tuple",
    # 'type',
    "zip",
    # '__debug__',
    # 'BaseException',
    # 'BaseExceptionGroup',
    # 'Exception',
    # 'GeneratorExit',
    # 'KeyboardInterrupt',
    # 'SystemExit',
    # 'ArithmeticError',
    # 'AssertionError',
    # 'AttributeError',
    # 'BufferError',
    # 'EOFError',
    # 'ImportError',
    # 'LookupError',
    # 'MemoryError',
    # 'NameError',
    # 'OSError',
    # 'ReferenceError',
    # 'RuntimeError',
    # 'StopAsyncIteration',
    # 'StopIteration',
    # 'SyntaxError',
    # 'SystemError',
    # 'TypeError',
    # 'ValueError',
    # 'Warning',
    # 'FloatingPointError',
    # 'OverflowError',
    # 'ZeroDivisionError',
    # 'BytesWarning',
    # 'DeprecationWarning',
    # 'EncodingWarning',
    # 'FutureWarning',
    # 'ImportWarning',
    # 'PendingDeprecationWarning',
    # 'ResourceWarning',
    # 'RuntimeWarning',
    # 'SyntaxWarning',
    # 'UnicodeWarning',
    # 'UserWarning',
    # 'BlockingIOError',
    # 'ChildProcessError',
    # 'ConnectionError',
    # 'FileExistsError',
    # 'FileNotFoundError',
    # 'InterruptedError',
    # 'IsADirectoryError',
    # 'NotADirectoryError',
    # 'PermissionError',
    # 'ProcessLookupError',
    # 'TimeoutError',
    # 'IndentationError',
    # 'IndexError',
    # 'KeyError',
    # 'ModuleNotFoundError',
    # 'NotImplementedError',
    # 'RecursionError',
    # 'UnboundLocalError',
    # 'UnicodeError',
    # 'BrokenPipeError',
    # 'ConnectionAbortedError',
    # 'ConnectionRefusedError',
    # 'ConnectionResetError',
    # 'TabError',
    # 'UnicodeDecodeError',
    # 'UnicodeEncodeError',
    # 'UnicodeTranslateError',
    # 'ExceptionGroup',
    # 'EnvironmentError',
    # 'IOError',
    # 'open',
    # 'copyright',
    # 'credits',
    # 'license',
    # 'help',
    # 'execfile',
    # 'runfile',
    # '__IPYTHON__',
    # 'display',
    # "get_ipython",
]

REDLISTED_CLASS_METHODS = ["__subclasses__", "__builtins__", "sys"]

REDLISTED_DATA_HANDLING = [
    ".csv",
    ".tsv",
    ".xlsx",
    ".xls",
    ".json",
    ".sql",
    ".feather",
    ".hdf",
    ".parquet",
    ".pkl",
    ".gbq",
    ".dta",
    ".html",
    ".md",
    ".zip",
    ".mat",
    ".nc",
    ".wav",
    ".sav",
    ".mtx",
    ".arff",
    ".hb",
    ".bin",
    ".uf",
    ".h5py",
    ".obj",
    ".dot",
    ".model",
    ".clipboard",
    ".to_csv",
    ".to_excel",
    ".to_json",
    ".to_sql",
    ".to_feather",
    ".to_hdf",
    ".to_parquet",
    ".to_pickle",
    ".to_gbq",
    ".to_stata",
    ".to_records",
    ".to_latex",
    ".to_html",
    ".to_markdown",
    ".to_clipboard",
    ".read_csv",
    ".read_excel",
    ".read_json",
    ".read_sql",
    ".read_feather",
    ".read_hdf",
    ".read_parquet",
    ".read_pickle",
    ".read_gbq",
    ".read_stata",
    ".read_html",
    ".read_clipboard",
    ".txt",
    ".loadtxt",
    ".genfromtxt",
    ".load",
    ".fromfile.save",
    ".savetxt",
    ".tofile",
    ".loadmat",
    ".savemat",
    ".whosmat",
    ".mminfo",
    ".mmread",
    ".mmwrite",
    ".FortranFile",
    ".FortranEOFError",
    ".FortranFormattingError",
    ".hb_read",
    ".hb_write",
    ".loadarff",
    ".readsav",
    ".netcdf",
    ".wavfile",
    ".load_sample_images",
    ".load_sample_image",
    ".load_svmlight_file",
    ".fetch_openml",
    ".load_files",
    ".export_text",
    ".export_graphviz",
]
