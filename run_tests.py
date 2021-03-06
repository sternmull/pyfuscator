import pyfuscator
from pathlib import (Path)
import sys
import subprocess
import difflib

this_dir = Path(__file__).parent.resolve()
test_in_dir = this_dir / 'test_inputs'
test_out_dir = this_dir / 'test_outputs'

def main():
    for out in test_out_dir.glob('*'):
        if out.name == '.gitignore':
            continue
        out.unlink()

    failed_tests = list()

    for org_py in test_in_dir.glob('*.py'):
        print('==== Testing', org_py)
        out_base = test_out_dir / org_py.name
        obf_py = out_base.with_suffix('.obf.py')
        pyfuscator.obfuscate(org_py, obf_py)

        results = list()
        failed = False
        for py in [org_py, obf_py]:
            r = subprocess.run([sys.executable, py], capture_output=True, text=True)
            results.append(f'exit code = {r.returncode}\n---------- stdout:\n{r.stdout}\n---------- stderr:\n{r.stderr}\n')
            if r.returncode:
                print(f' ERROR: Exit code {r.returncode} for {py}')
                failed = True

        org, obf = results
        if org != obf:
            failed = True
            print('\n'.join(difflib.unified_diff(org.splitlines(), obf.splitlines(), 'output for original script', 'output for obfuscated script')))

        if failed:
            failed_tests.append(org_py)

    if failed_tests:
        print(f'{len(failed_tests)} tests failed:')
        for fn in failed_tests:
            print('  ', fn)
        return 1
    else:
        print('All tests succeeded.')
        return 0

if __name__ == '__main__':
    exit(main())
